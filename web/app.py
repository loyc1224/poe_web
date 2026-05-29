import threading
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeout
from pathlib import Path

import markdown
from flask import Flask, render_template, Response, request, abort

import re

from monitor import (
    BEAST_TARGETS,
    CURRENT_LEAGUE_NAME,
    LEAGUE_NAME,
    fetch_builds,
    fetch_economy,
    fetch_meta_builds,
    fetch_reddit,
    generate_recommendations,
)

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
CONTENT_DIR = BASE_DIR / "content"

GAME_LABELS = {
    "poe1": "Path of Exile 1",
    "poe2": "Path of Exile 2",
}

CATEGORY_LABELS = {
    "strategy": "策略",
    "crafting": "做裝",
    "beetle": "甲蟲",
    "builds": "流派",
}


def get_doc_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip() or fallback
    return fallback


def render_markdown(text: str) -> str:
    text = text.replace("](./", "](/static/images/")
    return markdown.markdown(text, extensions=["extra", "tables", "sane_lists"])


def make_label(labels: dict, name: str) -> str:
    return labels.get(name, name.replace("-", " ").replace("_", " ").title())


def build_summary(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            return stripped[2:].strip()
    return "尚未提供摘要。"


def load_games() -> list[dict[str, object]]:
    if not CONTENT_DIR.exists():
        return []

    games: list[dict[str, object]] = []
    for game_dir in sorted(path for path in CONTENT_DIR.iterdir() if path.is_dir()):
        categories: list[dict[str, object]] = []
        for category_dir in sorted(path for path in game_dir.iterdir() if path.is_dir()):
            documents: list[dict[str, str]] = []
            for file_path in sorted(category_dir.glob("*.md")):
                text = file_path.read_text(encoding="utf-8")
                title = get_doc_title(text, file_path.stem)
                doc_id = f"{game_dir.name}-{category_dir.name}-{file_path.stem}"
                documents.append(
                    {
                        "id": doc_id,
                        "title": title,
                        "filename": file_path.name,
                        "game": game_dir.name,
                        "category": category_dir.name,
                        "summary": build_summary(text),
                        "html": render_markdown(text),
                    }
                )

            categories.append(
                {
                    "id": f"{game_dir.name}-{category_dir.name}",
                    "name": category_dir.name,
                    "label": make_label(CATEGORY_LABELS, category_dir.name),
                    "game": game_dir.name,
                    "count": len(documents),
                    "documents": documents,
                }
            )

        games.append(
            {
                "id": game_dir.name,
                "label": make_label(GAME_LABELS, game_dir.name),
                "categories": categories,
            }
        )

    return games


@app.route("/")
def home():
    games = load_games()
    return render_template("index.html", games=games)


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/api/img-proxy")
def img_proxy():
    """安全地代理 web.poecdn.com 圖示（僅允許 /gen/image/ 路徑）。"""
    import requests as _req
    path = request.args.get("path", "")
    # 白名單：只允許 /gen/image/ 路徑
    if not path.startswith("/gen/image/"):
        abort(400)
    url = "https://web.poecdn.com" + path
    try:
        r = _req.get(url, timeout=5, headers={
            "Referer": "https://poe.ninja/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        })
        r.raise_for_status()
    except Exception:
        abort(502)
    return Response(r.content, content_type=r.headers.get("Content-Type", "image/png"),
                    headers={"Cache-Control": "public, max-age=86400"})


# ── Spirit Walker 監控 ───────────────────────────────────────────────────────
_refresh_lock = threading.Lock()


@app.route("/monitor")
def monitor():
    return render_template(
        "monitor.html",
        beast_targets=BEAST_TARGETS,
        league=LEAGUE_NAME,
        current_league=CURRENT_LEAGUE_NAME,
    )


@app.route("/api/monitor/data")
def monitor_data():
    _TIMEOUT = 4  # 每個 fetch 最多等 4 秒，超時回傳空資料
    _empty_builds  = {"status": "unavailable", "total_characters": 0, "spirit_walker_count": 0,
                      "companion_counts": {b["id"]: 0 for b in BEAST_TARGETS}}
    _empty_economy = {"status": "unavailable", "items": [], "errors": []}
    _empty_reddit  = {"status": "unavailable", "posts": [], "beast_mention_counts": {}, "errors": []}
    with ThreadPoolExecutor(max_workers=3) as pool:
        f_builds  = pool.submit(fetch_builds)
        f_economy = pool.submit(fetch_economy)
        f_reddit  = pool.submit(fetch_reddit)
        try:    builds  = f_builds.result(timeout=_TIMEOUT)
        except Exception: builds = _empty_builds
        try:    economy = f_economy.result(timeout=_TIMEOUT)
        except Exception: economy = _empty_economy
        try:    reddit  = f_reddit.result(timeout=_TIMEOUT)
        except Exception: reddit = _empty_reddit
    recs = generate_recommendations(builds, economy, reddit)
    return {
        "builds":          builds,
        "economy":         economy,
        "reddit":          reddit,
        "recommendations": recs,
        "league":          LEAGUE_NAME,
    }


@app.route("/api/monitor/economy/league/<league_name>")
def monitor_economy_by_league(league_name: str):
    """依聯盟名稱取得 economy 資料（供現有聯盟物價分頁使用）。"""
    if not re.match(r'^[A-Za-z0-9 _\-]{1,60}$', league_name):
        return {"status": "error", "message": "無效的聯盟名稱"}, 400
    economy = fetch_economy(league=league_name)
    return economy


@app.route("/api/monitor/meta-builds")
def monitor_meta_builds():
    """開季聯盟熱門流派資料（技能排行、DPS 排行、角色清單）。"""
    return fetch_meta_builds()


@app.route("/api/monitor/meta-builds/league/<league_name>")
def monitor_meta_builds_by_league(league_name: str):
    """指定聯盟熱門流派資料。"""
    if not re.match(r'^[A-Za-z0-9 _\-]{1,60}$', league_name):
        return {"status": "error", "message": "無效的聯盟名稱"}, 400
    return fetch_meta_builds(league=league_name)


@app.route("/api/monitor/refresh", methods=["POST"])
def monitor_refresh():
    if not _refresh_lock.acquire(blocking=False):
        return {"status": "busy", "message": "重新整理已在進行中，請稍候"}, 429
    try:
        builds  = fetch_builds(force=True)
        economy = fetch_economy(force=True)
        reddit  = fetch_reddit(force=True)
        recs    = generate_recommendations(builds, economy, reddit)
        return {
            "status":          "ok",
            "builds":          builds,
            "economy":         economy,
            "reddit":          reddit,
            "recommendations": recs,
            "league":          LEAGUE_NAME,
        }
    except Exception as exc:
        return {"status": "error", "message": str(exc)}, 500
    finally:
        _refresh_lock.release()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
