import threading
from concurrent.futures import ThreadPoolExecutor, TimeoutError as FutureTimeout
from pathlib import Path
import json
import sqlite3
import secrets
import hashlib
import time
import os
import base64
from datetime import date
from urllib.parse import urlencode, quote_plus

import markdown
import requests
from flask import Flask, render_template, Response, request, abort, redirect, session

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
from monitor.config import POE2_LEAGUES, POE1_STANDARD
from monitor.translations import ITEM_ZH

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY", os.getenv("SECRET_KEY", "dev-insecure-change-me"))

BASE_DIR = Path(__file__).resolve().parent
CONTENT_DIR = BASE_DIR / "content"
TRAFFIC_DB = BASE_DIR / "cache" / "traffic.db"
STASH_DB = BASE_DIR / "cache" / "stash.db"
_traffic_lock = threading.Lock()
_stash_lock = threading.Lock()

OAUTH_AUTHORIZE_URL = "https://pathofexile.tw/oauth/authorize"
OAUTH_TOKEN_URL = "https://pathofexile.tw/oauth/token"
OAUTH_CLIENT_ID = os.getenv("POE_TW_CLIENT_ID", "").strip()
OAUTH_SCOPE = "account:profile account:leagues account:stashes account:characters"
OAUTH_REDIRECT_URI = os.getenv("POE_TW_REDIRECT_URI", "").strip()
OAUTH_STATE_TTL_SECONDS = 600

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


def _ensure_stash_db() -> None:
    STASH_DB.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(STASH_DB) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS stash_snapshots (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at REAL NOT NULL,
                total_divine REAL NOT NULL,
                included_tabs INTEGER NOT NULL,
                source TEXT NOT NULL DEFAULT 'manual'
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS stash_state (
                id INTEGER PRIMARY KEY,
                account_name TEXT NOT NULL DEFAULT '',
                game TEXT NOT NULL DEFAULT 'poe2',
                league TEXT NOT NULL DEFAULT '',
                tabs_json TEXT NOT NULL DEFAULT '[]',
                raw_json TEXT NOT NULL DEFAULT '{}',
                updated_at REAL NOT NULL DEFAULT 0
            )
            """
        )
        columns = [row[1] for row in conn.execute("PRAGMA table_info(stash_state)").fetchall()]
        if "raw_json" not in columns:
            conn.execute("ALTER TABLE stash_state ADD COLUMN raw_json TEXT NOT NULL DEFAULT '{}'")
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS oauth_pkce_states (
                state TEXT PRIMARY KEY,
                code_verifier TEXT NOT NULL,
                created_at REAL NOT NULL
            )
            """
        )
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS oauth_tokens (
                id INTEGER PRIMARY KEY CHECK (id = 1),
                access_token TEXT NOT NULL,
                refresh_token TEXT,
                expires_at REAL NOT NULL DEFAULT 0,
                token_type TEXT NOT NULL DEFAULT 'Bearer'
            )
            """
        )


def _b64url(value: bytes) -> str:
    return base64.urlsafe_b64encode(value).decode("ascii").rstrip("=")


def _build_pkce_pair() -> tuple[str, str]:
    code_verifier = _b64url(secrets.token_bytes(32))
    challenge = hashlib.sha256(code_verifier.encode("ascii")).digest()
    code_challenge = _b64url(challenge)
    return code_verifier, code_challenge


def _save_pkce_state(state: str, code_verifier: str) -> None:
    _ensure_stash_db()
    cutoff = time.time() - (OAUTH_STATE_TTL_SECONDS * 2)
    with _stash_lock:
        with sqlite3.connect(STASH_DB) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO oauth_pkce_states (state, code_verifier, created_at) VALUES (?, ?, ?)",
                (state, code_verifier, time.time()),
            )
            conn.execute("DELETE FROM oauth_pkce_states WHERE created_at < ?", (cutoff,))


def _resolve_oauth_redirect_uri() -> str:
    """回呼位址優先採環境變數，否則使用目前站台 host。"""
    if OAUTH_REDIRECT_URI:
        return OAUTH_REDIRECT_URI
    return request.host_url.rstrip("/") + "/callback"


def _validate_oauth_config() -> str | None:
    if not OAUTH_CLIENT_ID:
        return "missing+POE_TW_CLIENT_ID"
    uri = _resolve_oauth_redirect_uri()
    if not (uri.startswith("http://") or uri.startswith("https://")):
        return "invalid+POE_TW_REDIRECT_URI"
    # The public poepricer client id is bound to its production callback only.
    if OAUTH_CLIENT_ID == "poetwpricer" and uri != "https://www.poepricer.com/callback":
        return "client_redirect_mismatch+poetwpricer"
    return None


def _pop_pkce_verifier(state: str) -> str | None:
    _ensure_stash_db()
    with _stash_lock:
        with sqlite3.connect(STASH_DB) as conn:
            row = conn.execute(
                "SELECT code_verifier, created_at FROM oauth_pkce_states WHERE state = ?",
                (state,),
            ).fetchone()
            conn.execute("DELETE FROM oauth_pkce_states WHERE state = ?", (state,))
    if not row:
        return None
    created_at = float(row[1])
    if time.time() - created_at > OAUTH_STATE_TTL_SECONDS:
        return None
    return row[0]


def _save_tokens(token_payload: dict) -> None:
    _ensure_stash_db()
    expires_in = int(token_payload.get("expires_in") or 0)
    expires_at = time.time() + max(expires_in, 0)
    with _stash_lock:
        with sqlite3.connect(STASH_DB) as conn:
            conn.execute(
                """
                INSERT INTO oauth_tokens (id, access_token, refresh_token, expires_at, token_type)
                VALUES (1, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    access_token=excluded.access_token,
                    refresh_token=excluded.refresh_token,
                    expires_at=excluded.expires_at,
                    token_type=excluded.token_type
                """,
                (
                    token_payload.get("access_token", ""),
                    token_payload.get("refresh_token"),
                    expires_at,
                    token_payload.get("token_type", "Bearer"),
                ),
            )


def _clear_tokens() -> None:
    _ensure_stash_db()
    with _stash_lock:
        with sqlite3.connect(STASH_DB) as conn:
            conn.execute("DELETE FROM oauth_tokens WHERE id = 1")


def _load_tokens() -> dict | None:
    _ensure_stash_db()
    with sqlite3.connect(STASH_DB) as conn:
        row = conn.execute(
            "SELECT access_token, refresh_token, expires_at, token_type FROM oauth_tokens WHERE id = 1"
        ).fetchone()
    if not row:
        return None
    return {
        "access_token": row[0],
        "refresh_token": row[1],
        "expires_at": float(row[2] or 0),
        "token_type": row[3] or "Bearer",
    }


def _refresh_access_token(refresh_token: str) -> dict:
    if not OAUTH_CLIENT_ID:
        raise RuntimeError("missing POE_TW_CLIENT_ID")
    token_resp = requests.post(
        OAUTH_TOKEN_URL,
        data={
            "grant_type": "refresh_token",
            "client_id": OAUTH_CLIENT_ID,
            "refresh_token": refresh_token,
        },
        timeout=12,
        headers={"Accept": "application/json"},
    )
    if token_resp.status_code >= 400:
        raise RuntimeError(f"refresh token failed: {token_resp.status_code}")
    payload = token_resp.json()
    _save_tokens(payload)
    return payload


def _get_valid_access_token() -> str | None:
    tokens = _load_tokens()
    if not tokens:
        return None
    if time.time() < tokens["expires_at"] - 30:
        return tokens["access_token"]
    if tokens.get("refresh_token"):
        try:
            payload = _refresh_access_token(tokens["refresh_token"])
            return payload.get("access_token")
        except Exception:
            return None
    return None


def _normalize_tab(tab: dict, index: int) -> dict:
    value = tab.get("value_divine")
    if value is None:
        value = tab.get("divine_value")
    if value is None:
        value = tab.get("value")
    try:
        value_divine = float(value or 0)
    except Exception:
        value_divine = 0.0

    return {
        "name": tab.get("name") or tab.get("label") or f"Tab {index + 1}",
        "color": tab.get("color") or tab.get("colour") or "",
        "enabled": bool(tab.get("enabled", True)),
        "value_divine": value_divine,
    }


def _extract_stash_payload(payload: object, default_game: str, default_league: str) -> dict | None:
    if isinstance(payload, list):
        tabs = payload
        account = ""
        game = default_game
        league = default_league
    elif isinstance(payload, dict):
        tabs = payload.get("tabs") or payload.get("stashes") or payload.get("items")
        if not isinstance(tabs, list):
            return None
        account = payload.get("account") or payload.get("accountName") or ""
        game = (payload.get("game") or default_game or "poe2").lower()
        league = payload.get("league") or default_league
    else:
        return None

    normalized_tabs = []
    for index, item in enumerate(tabs):
        if isinstance(item, dict):
            normalized_tabs.append(_normalize_tab(item, index))

    return {
        "account_name": str(account or ""),
        "game": game,
        "league": str(league or ""),
        "tabs": normalized_tabs,
    }


def _save_stash_state(
    account_name: str,
    game: str,
    league: str,
    tabs: list[dict],
    source: str,
    raw_payload: object | None = None,
) -> dict:
    _ensure_stash_db()
    now = time.time()
    total_divine = sum(float(t.get("value_divine") or 0) for t in tabs if t.get("enabled", True))
    included_tabs = sum(1 for t in tabs if t.get("enabled", True))

    with _stash_lock:
        with sqlite3.connect(STASH_DB) as conn:
            conn.execute(
                """
                INSERT INTO stash_state (id, account_name, game, league, tabs_json, raw_json, updated_at)
                VALUES (1, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    account_name=excluded.account_name,
                    game=excluded.game,
                    league=excluded.league,
                    tabs_json=excluded.tabs_json,
                    raw_json=excluded.raw_json,
                    updated_at=excluded.updated_at
                """,
                (
                    account_name,
                    game,
                    league,
                    json.dumps(tabs, ensure_ascii=False),
                    json.dumps(raw_payload if raw_payload is not None else {}, ensure_ascii=False),
                    now,
                ),
            )
            conn.execute(
                "INSERT INTO stash_snapshots (created_at, total_divine, included_tabs, source) VALUES (?, ?, ?, ?)",
                (now, total_divine, included_tabs, source),
            )

    return {
        "account_name": account_name,
        "game": game,
        "league": league,
        "tabs": tabs,
        "updated_at": now,
        "total_divine": total_divine,
        "included_tabs": included_tabs,
    }


def _sync_stash_with_token(access_token: str, game: str, league: str) -> dict:
    endpoints = [
        "https://pathofexile.tw/api/trade2/account/stashes",
        "https://pathofexile.tw/api/account/stashes",
    ]
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
    }

    errors: list[str] = []
    unauthorized_hits = 0
    for endpoint in endpoints:
        try:
            resp = requests.get(endpoint, params={"game": game, "league": league}, headers=headers, timeout=15)
            if resp.status_code == 401:
                unauthorized_hits += 1
                errors.append(f"{endpoint} => 401")
                continue
            if resp.status_code >= 400:
                errors.append(f"{endpoint} => {resp.status_code}")
                continue
            payload = resp.json()
            parsed = _extract_stash_payload(payload, game, league)
            if not parsed:
                errors.append(f"{endpoint} => invalid payload")
                continue
            return _save_stash_state(
                parsed["account_name"],
                parsed["game"],
                parsed["league"],
                parsed["tabs"],
                source="oauth",
                raw_payload=payload,
            )
        except Exception as exc:
            errors.append(f"{endpoint} => {exc}")

    if unauthorized_hits == len(endpoints):
        _clear_tokens()
        raise RuntimeError("授權已失效或 access token 無效，請重新登入後再同步。")

    raise RuntimeError("; ".join(errors) or "stash sync failed")


def _read_stash_state() -> dict | None:
    _ensure_stash_db()
    with sqlite3.connect(STASH_DB) as conn:
        row = conn.execute(
            "SELECT account_name, game, league, tabs_json, updated_at FROM stash_state WHERE id = 1"
        ).fetchone()
    if not row:
        return None
    tabs_json = row[3] or "[]"
    try:
        tabs = json.loads(tabs_json)
    except Exception:
        tabs = []
    return {
        "account_name": row[0],
        "game": row[1],
        "league": row[2],
        "tabs": tabs,
        "updated_at": float(row[4] or 0),
    }


def _read_stash_raw_payload() -> object | None:
    _ensure_stash_db()
    with sqlite3.connect(STASH_DB) as conn:
        row = conn.execute("SELECT raw_json FROM stash_state WHERE id = 1").fetchone()
    if not row:
        return None
    raw_json = row[0] or "{}"
    try:
        return json.loads(raw_json)
    except Exception:
        return None


def _to_number(value: object, fallback: float = 0.0) -> float:
    try:
        return float(value)
    except Exception:
        return fallback


def _pick_name(item: dict) -> str:
    for key in ("displayName", "name", "typeLine", "baseType"):
        value = str(item.get(key) or "").strip()
        if value:
            return value
    return "Unknown"


def _pick_category(item: dict) -> str:
    for key in ("itemClass", "category", "type", "className"):
        value = str(item.get(key) or "").strip()
        if value:
            return value
    return "Other"


def _is_resource_item_candidate(item: dict) -> bool:
    if not isinstance(item, dict):
        return False
    has_name = any(str(item.get(k) or "").strip() for k in ("displayName", "name", "typeLine", "baseType"))
    has_item_shape = any(k in item for k in ("stackSize", "inventoryId", "itemClass", "frameType", "icon", "typeLine", "baseType"))
    return has_name and has_item_shape


def _normalize_resource_item(item: dict, tab_name: str) -> dict:
    quantity = 1.0
    for key in ("stackSize", "stack", "amount", "count", "quantity", "qty"):
        if key in item:
            quantity = max(_to_number(item.get(key), 1.0), 0.0)
            break
    if quantity <= 0:
        quantity = 1.0

    value_divine = 0.0
    for key in ("value_divine", "divineValue", "valueDivine"):
        if key in item:
            value_divine = max(_to_number(item.get(key), 0.0), 0.0)
            break

    return {
        "name": _pick_name(item),
        "category": _pick_category(item),
        "quantity": quantity,
        "value_divine": value_divine,
        "tab_name": tab_name or "Unknown",
    }


def _collect_resource_items(node: object, tab_name: str, out: list[dict]) -> None:
    if isinstance(node, dict):
        if _is_resource_item_candidate(node):
            out.append(_normalize_resource_item(node, tab_name))
            return

        next_tab = tab_name
        node_name = str(node.get("name") or node.get("label") or "").strip()
        if node_name and any(isinstance(node.get(k), list) for k in ("items", "contents", "inventory")):
            next_tab = node_name

        for value in node.values():
            _collect_resource_items(value, next_tab, out)
        return

    if isinstance(node, list):
        for value in node:
            _collect_resource_items(value, tab_name, out)


def _build_stash_resource_stats(raw_payload: object) -> dict:
    collected: list[dict] = []
    _collect_resource_items(raw_payload, "", collected)

    merged: dict[tuple[str, str], dict] = {}
    for item in collected:
        key = (item["name"], item["category"])
        bucket = merged.setdefault(
            key,
            {
                "name": item["name"],
                "category": item["category"],
                "quantity": 0.0,
                "value_divine": 0.0,
                "tabs": set(),
            },
        )
        bucket["quantity"] += item["quantity"]
        bucket["value_divine"] += item["value_divine"]
        bucket["tabs"].add(item["tab_name"])

    resources = []
    for bucket in merged.values():
        resources.append(
            {
                "name": bucket["name"],
                "category": bucket["category"],
                "quantity": round(bucket["quantity"], 4),
                "value_divine": round(bucket["value_divine"], 4),
                "tab_count": len(bucket["tabs"]),
            }
        )

    resources.sort(key=lambda x: (x["value_divine"], x["quantity"]), reverse=True)

    category_totals: dict[str, dict] = {}
    for row in resources:
        cat = row["category"] or "Other"
        agg = category_totals.setdefault(cat, {"category": cat, "kinds": 0, "quantity": 0.0, "value_divine": 0.0})
        agg["kinds"] += 1
        agg["quantity"] += row["quantity"]
        agg["value_divine"] += row["value_divine"]

    categories = [
        {
            "category": v["category"],
            "kinds": v["kinds"],
            "quantity": round(v["quantity"], 4),
            "value_divine": round(v["value_divine"], 4),
        }
        for v in category_totals.values()
    ]
    categories.sort(key=lambda x: (x["value_divine"], x["quantity"]), reverse=True)

    return {
        "resources": resources,
        "categories": categories,
        "resource_count": len(resources),
        "item_instances": len(collected),
    }


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


@app.route("/pricer")
def pricer():
    """PoE1 / PoE2 通貨查價頁。"""
    game = (request.args.get("game") or "poe2").strip().lower()
    if game not in ("poe1", "poe2"):
        game = "poe2"

    return render_template(
        "pricer.html",
        active_game=game,
        poe2_default_league=CURRENT_LEAGUE_NAME,
        poe1_default_league=POE1_LEAGUE,
        poe2_leagues=POE2_LEAGUES,
        poe1_leagues=[POE1_LEAGUE, POE1_STANDARD],
    )


@app.route("/api/pricer/currency")
def pricer_currency():
    """統一查價 API：game=poe1|poe2，league=聯盟名。"""
    game = (request.args.get("game") or "poe2").strip().lower()
    league = (request.args.get("league") or "").strip()
    force = (request.args.get("force") or "").strip().lower() in ("1", "true", "yes")

    if game not in ("poe1", "poe2"):
        return {"status": "error", "message": "無效的 game 參數，僅支援 poe1 / poe2"}, 400

    if league and not re.match(r"^[A-Za-z0-9 _\-]{1,60}$", league):
        return {"status": "error", "message": "無效的聯盟名稱"}, 400

    if game == "poe2":
        target_league = league or LEAGUE_NAME
        data = fetch_economy(league=target_league, force=force)
        if not league and not (data.get("items") or []):
            target_league = CURRENT_LEAGUE_NAME
            data = fetch_economy(league=target_league, force=force)
    else:
        target_league = league or POE1_LEAGUE
        data = fetch_poe1_economy(league=target_league, force=force)

    items = data.get("items", [])
    for item in items:
        if not item.get("zh"):
            item_id = item.get("id", "")
            item_name = item.get("name", "")
            item["zh"] = ITEM_ZH.get(item_id, ITEM_ZH.get(item_name, ""))

    return {
        "status": data.get("status", "ok"),
        "game": game,
        "league": target_league,
        "fetched_at": data.get("fetched_at"),
        "errors": data.get("errors", []),
        "items": items,
    }


@app.route("/api/pricer/oauth/start")
def pricer_oauth_start():
    config_error = _validate_oauth_config()
    if config_error:
        return redirect(f"/pricer?oauth=error&message={config_error}", code=302)

    state = secrets.token_urlsafe(24)
    code_verifier, code_challenge = _build_pkce_pair()
    session["oauth_state"] = state
    session["oauth_code_verifier"] = code_verifier
    session["oauth_state_created_at"] = time.time()
    _save_pkce_state(state, code_verifier)
    redirect_uri = _resolve_oauth_redirect_uri()

    params = {
        "response_type": "code",
        "client_id": OAUTH_CLIENT_ID,
        "redirect_uri": redirect_uri,
        "scope": OAUTH_SCOPE,
        "state": state,
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
    }
    return redirect(f"{OAUTH_AUTHORIZE_URL}?{urlencode(params)}", code=302)


@app.route("/callback")
def pricer_oauth_callback():
    config_error = _validate_oauth_config()
    if config_error:
        return redirect(f"/pricer?oauth=error&message={config_error}", code=302)

    if request.args.get("error"):
        err = request.args.get("error_description") or request.args.get("error")
        return redirect(f"/pricer?oauth=error&message={quote_plus(err)}", code=302)

    state = (request.args.get("state") or "").strip()
    code = (request.args.get("code") or "").strip()
    if not state or not code:
        return redirect("/pricer?oauth=error&message=missing+state+or+code", code=302)

    session_state = str(session.get("oauth_state") or "")
    session_verifier = str(session.get("oauth_code_verifier") or "")
    state_created = float(session.get("oauth_state_created_at") or 0)

    verifier = None
    if session_state == state and session_verifier and (time.time() - state_created <= OAUTH_STATE_TTL_SECONDS):
        verifier = session_verifier
    else:
        verifier = _pop_pkce_verifier(state)

    session.pop("oauth_state", None)
    session.pop("oauth_code_verifier", None)
    session.pop("oauth_state_created_at", None)

    if not verifier:
        return redirect("/pricer?oauth=error&message=invalid+or+expired+state", code=302)

    redirect_uri = _resolve_oauth_redirect_uri()

    try:
        token_resp = requests.post(
            OAUTH_TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "client_id": OAUTH_CLIENT_ID,
                "code": code,
                "redirect_uri": redirect_uri,
                "code_verifier": verifier,
            },
            timeout=12,
            headers={"Accept": "application/json"},
        )
        if token_resp.status_code >= 400:
            return redirect(
                f"/pricer?oauth=error&message=token+exchange+failed+{token_resp.status_code}",
                code=302,
            )
        payload = token_resp.json()
        if not payload.get("access_token"):
            return redirect("/pricer?oauth=error&message=token+missing", code=302)
        _save_tokens(payload)

        sync_data = _sync_stash_with_token(payload["access_token"], game="poe2", league=CURRENT_LEAGUE_NAME)
        tabs_count = len(sync_data.get("tabs") or [])
        return redirect(f"/pricer?oauth=ok&tabs={tabs_count}", code=302)
    except Exception as exc:
        return redirect(f"/pricer?oauth=error&message={quote_plus(str(exc))}", code=302)


@app.route("/api/pricer/stash/state")
def pricer_stash_state():
    state = _read_stash_state()
    tokens = _load_tokens()
    config_error = _validate_oauth_config()

    config_message = ""
    if config_error == "missing+POE_TW_CLIENT_ID":
        config_message = "請先設定 POE_TW_CLIENT_ID。"
    elif config_error == "invalid+POE_TW_REDIRECT_URI":
        config_message = "POE_TW_REDIRECT_URI 格式不正確。"
    elif config_error == "client_redirect_mismatch+poetwpricer":
        config_message = "目前使用的 client_id=poetwpricer 僅允許 https://www.poepricer.com/callback，無法用本機 callback。"

    return {
        "status": "ok",
        "oauth_connected": bool(tokens and tokens.get("access_token")),
        "oauth_configured": config_error is None,
        "oauth_config_error": config_error,
        "oauth_config_message": config_message,
        "stash": state,
    }


@app.route("/api/pricer/stash/sync", methods=["POST"])
def pricer_stash_sync():
    payload = request.get_json(silent=True) or {}
    game = str(payload.get("game") or "poe2").strip().lower()
    league = str(payload.get("league") or CURRENT_LEAGUE_NAME).strip()
    if game not in ("poe1", "poe2"):
        return {"status": "error", "message": "無效的 game 參數"}, 400
    if league and not re.match(r"^[A-Za-z0-9 _\-]{1,60}$", league):
        return {"status": "error", "message": "無效的聯盟名稱"}, 400

    access_token = _get_valid_access_token()
    if not access_token:
        return {"status": "error", "message": "尚未授權，請先登入。"}, 401

    try:
        stash_state = _sync_stash_with_token(access_token, game=game, league=league)
        return {"status": "ok", "stash": stash_state}
    except Exception as exc:
        return {"status": "error", "message": str(exc)}, 502


@app.route("/api/pricer/stash/resources")
def pricer_stash_resources():
    refresh = (request.args.get("refresh") or "").strip().lower() in ("1", "true", "yes")
    stash_state = _read_stash_state()

    if refresh:
        access_token = _get_valid_access_token()
        if not access_token:
            return {"status": "error", "message": "尚未授權，請先登入。"}, 401
        game = str(request.args.get("game") or (stash_state or {}).get("game") or "poe2").lower()
        league = str(request.args.get("league") or (stash_state or {}).get("league") or CURRENT_LEAGUE_NAME)
        stash_state = _sync_stash_with_token(access_token, game=game, league=league)

    raw_payload = _read_stash_raw_payload()
    if not raw_payload:
        return {"status": "error", "message": "尚無倉庫資料，請先完成授權並同步。"}, 404

    stats = _build_stash_resource_stats(raw_payload)
    return {
        "status": "ok",
        "account_name": (stash_state or {}).get("account_name", ""),
        "game": (stash_state or {}).get("game", ""),
        "league": (stash_state or {}).get("league", ""),
        "updated_at": (stash_state or {}).get("updated_at", 0),
        **stats,
    }


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
