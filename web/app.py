import threading
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeout
from pathlib import Path
import json
import sqlite3
import hashlib
from datetime import date

import markdown
from flask import Flask, render_template, Response, request, abort

import re

from monitor import (
    BEAST_TARGETS,
    CURRENT_LEAGUE_NAME,
    LEAGUE_NAME,
    POE1_LEAGUE,
    fetch_builds,
    fetch_economy,
    fetch_meta_builds,
    fetch_poe1_economy,
    fetch_reddit,
    generate_recommendations,
)

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
CONTENT_DIR = BASE_DIR / "content"
TRAFFIC_DB = BASE_DIR / "cache" / "traffic.db"
_traffic_lock = threading.Lock()

GAME_LABELS = {
    "poe1": "Path of Exile 1",
    "poe2": "Path of Exile 2",
}

CATEGORY_LABELS = {
    "strategy": "策略",
    "crafting": "做裝",
    "beetle": "甲蟲",
    "builds": "流派",
    "storyline": "主線劇情",
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


def load_trade_links() -> dict:
    """載入快速交易連結配置"""
    trade_links_file = CONTENT_DIR / "trade_links.json"
    if not trade_links_file.exists():
        return {"poe1": [], "poe2": []}
    try:
        with open(trade_links_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"poe1": [], "poe2": []}


def load_shop_filters() -> dict:
    """載入商店/換界石篩選配置（由文件生成前端篩選按鈕）"""
    filters_file = CONTENT_DIR / "shop_filters.json"
    fallback = {
        "poe2": {
            "shop_defaults": [],
            "shop_groups": [],
            "waystone_defaults": [],
            "waystone_keywords": [],
        }
    }
    if not filters_file.exists():
        return fallback
    try:
        with open(filters_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return fallback


def _ensure_traffic_db() -> None:
    TRAFFIC_DB.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(TRAFFIC_DB) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS traffic_stats (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                total_views INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS traffic_daily_uniques (
                day TEXT NOT NULL,
                visitor_hash TEXT NOT NULL,
                PRIMARY KEY (day, visitor_hash)
            )
            """
        )
        conn.execute("INSERT OR IGNORE INTO traffic_stats (id, total_views) VALUES (1, 0)")


def _get_client_ip(req) -> str:
    xff = req.headers.get("X-Forwarded-For", "").strip()
    if xff:
        return xff.split(",")[0].strip()
    return (req.remote_addr or "unknown").strip()


def record_home_visit(req) -> dict:
    """記錄首頁流量並回傳統計（總瀏覽、今日不重複訪客）。"""
    _ensure_traffic_db()
    today = date.today().isoformat()
    ip = _get_client_ip(req)
    ua = (req.headers.get("User-Agent") or "")[:200]
    visitor_hash = hashlib.sha256(f"{ip}|{ua}".encode("utf-8")).hexdigest()

    with _traffic_lock:
        with sqlite3.connect(TRAFFIC_DB) as conn:
            conn.execute("UPDATE traffic_stats SET total_views = total_views + 1 WHERE id = 1")
            conn.execute(
                "INSERT OR IGNORE INTO traffic_daily_uniques (day, visitor_hash) VALUES (?, ?)",
                (today, visitor_hash),
            )
            total_views = conn.execute(
                "SELECT total_views FROM traffic_stats WHERE id = 1"
            ).fetchone()[0]
            daily_uniques = conn.execute(
                "SELECT COUNT(*) FROM traffic_daily_uniques WHERE day = ?",
                (today,),
            ).fetchone()[0]

    return {
        "total_views": total_views,
        "daily_uniques": daily_uniques,
        "day": today,
    }


def get_traffic_stats() -> dict:
    """取得流量統計（不增加計數）。"""
    _ensure_traffic_db()
    today = date.today().isoformat()
    with sqlite3.connect(TRAFFIC_DB) as conn:
        total_views = conn.execute(
            "SELECT total_views FROM traffic_stats WHERE id = 1"
        ).fetchone()[0]
        daily_uniques = conn.execute(
            "SELECT COUNT(*) FROM traffic_daily_uniques WHERE day = ?",
            (today,),
        ).fetchone()[0]
    return {
        "total_views": total_views,
        "daily_uniques": daily_uniques,
        "day": today,
    }


@app.route("/")
def home():
    games = load_games()
    trade_links = load_trade_links()
    shop_filters = load_shop_filters()
    traffic_stats = record_home_visit(request)
    return render_template(
        "index.html",
        games=games,
        trade_links=trade_links,
        shop_filters=shop_filters,
        traffic_stats=traffic_stats,
    )


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/api/traffic")
def traffic():
    """首頁流量統計 API。"""
    return {"status": "ok", "traffic": get_traffic_stats()}


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
        poe1_league=POE1_LEAGUE,
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


@app.route("/api/monitor/poe1/economy")
def monitor_poe1_economy():
    """PoE1 目前聯盟物價資料。"""
    return fetch_poe1_economy()


@app.route("/api/monitor/poe1/economy/league/<league_name>")
def monitor_poe1_economy_by_league(league_name: str):
    """PoE1 指定聯盟物價資料。"""
    if not re.match(r'^[A-Za-z0-9 _\-]{1,60}$', league_name):
        return {"status": "error", "message": "無效的聯盟名稱"}, 400
    return fetch_poe1_economy(league=league_name)


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
