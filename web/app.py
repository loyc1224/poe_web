import threading
from pathlib import Path
import json
import sqlite3
import secrets
import hashlib
import time
import os
import base64
from contextlib import closing
from datetime import date
from urllib.parse import urlencode, quote_plus

import markdown
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, Response, request, abort, redirect, session

import re

from monitor import (
    CURRENT_LEAGUE_NAME,
    LEAGUE_NAME,
    POE1_LEAGUE,
    fetch_economy,
    fetch_poe1_economy,
)
from monitor.economy.config import POE2_LEAGUES, POE1_STANDARD
from monitor.economy.translations import ITEM_ZH
from monitor.tw_pricer.tw_pricer_client import load_tw_price_dataset, load_tw_price_navigation_icons
from monitor.tw_pricer.tw_pricer_source import refresh_all_tw_prices
from monitor.stash.store import StashStore
from monitor.stash.client import StashApiError, build_oauth_user_agent, fetch_account_stashes, fetch_account_stashes_with_session
from monitor.stash.pricer import value_stashes, flatten_stash_items

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY") or os.getenv("SECRET_KEY") or secrets.token_hex(32)
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = bool(os.getenv("K_SERVICE"))
STRATEGY_PASSWORD = os.getenv("STRATEGY_PASSWORD", "")
_strategy_login_attempts: dict[str, tuple[int, float]] = {}
_strategy_login_lock = threading.Lock()

CONTENT_DIR = BASE_DIR / "content"
TRAFFIC_DB = BASE_DIR / "cache" / "traffic.db"
STASH_DB = BASE_DIR / "cache" / "stash.db"
_traffic_lock = threading.Lock()
_stash_lock = threading.Lock()

OAUTH_AUTHORIZE_URL = "https://pathofexile.tw/oauth/authorize"
OAUTH_TOKEN_URL = "https://pathofexile.tw/oauth/token"
OAUTH_CLIENT_ID = os.getenv("POE_TW_CLIENT_ID", "").strip()
OAUTH_CLIENT_SECRET = os.getenv("POE_TW_CLIENT_SECRET", "").strip()
OAUTH_SCOPE = "account:profile account:stashes"
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
    "reference": "參考資料",
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


def load_games(include_strategies: bool = True) -> list[dict[str, object]]:
    if not CONTENT_DIR.exists():
        return []

    games: list[dict[str, object]] = []
    for game_dir in sorted(path for path in CONTENT_DIR.iterdir() if path.is_dir()):
        categories: list[dict[str, object]] = []
        category_dirs = {
            path.name: path for path in game_dir.iterdir()
            if path.is_dir() and path.name not in ("beetle", "filter", "fliter")
        }
        if (game_dir / "beetle").is_dir():
            category_dirs.setdefault("strategy", game_dir / "strategy")
        for category_name in sorted(category_dirs):
            category_dir = category_dirs[category_name]
            documents: list[dict[str, str]] = []
            markdown_files = sorted(category_dir.glob("*.md"))
            beetle_files = sorted((game_dir / "beetle").glob("*.md")) if category_name == "strategy" else []
            markdown_files.extend(beetle_files)
            locked = category_dir.name == "strategy" and not include_strategies
            for file_path in ([] if locked else markdown_files):
                text = file_path.read_text(encoding="utf-8")
                title = get_doc_title(text, file_path.stem)
                doc_id = f"{game_dir.name}-{file_path.parent.name}-{file_path.stem}"
                documents.append(
                    {
                        "id": doc_id,
                        "title": title,
                        "filename": file_path.name,
                        "game": game_dir.name,
                        "category": category_dir.name,
                        "subcategory": "beetle" if file_path.parent.name == "beetle" else "",
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
                    "count": len(markdown_files),
                    "locked": locked,
                    "documents": documents,
                    "subcategories": [{"id": "beetle", "label": CATEGORY_LABELS["beetle"], "count": len(beetle_files)}] if beetle_files else [],
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
    with closing(sqlite3.connect(TRAFFIC_DB)) as conn, conn:
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
    with closing(sqlite3.connect(STASH_DB)) as conn, conn:
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
    data = _stash_data()
    data["pkce"] = {"state": state, "verifier": code_verifier, "created_at": time.time()}
    _stash_store().save(_stash_owner(create=True), data)


def _stash_owner(create=False):
    owner = session.get("stash_connection_id")
    if not owner and create:
        owner = secrets.token_urlsafe(32)
        session["stash_connection_id"] = owner
    return owner


def _stash_store():
    return StashStore(STASH_DB, app.config["SECRET_KEY"], os.getenv("STASH_STORAGE_BUCKET", "").strip())


def _stash_data():
    owner = _stash_owner()
    return _stash_store().load(owner) if owner else {}


def _stash_storage_ready():
    return not os.getenv("K_SERVICE") or bool(os.getenv("STASH_STORAGE_BUCKET"))


def _stash_selection_key(data):
    selection = data.get("selection", {})
    selected = selection.get("selected_tabs")
    if selected is None:
        selected = [str(tab["id"]) for tab in data.get("tabs", [])]
    encoded = json.dumps({"tabs": sorted(selected), "excluded": sorted(selection.get("excluded_items", []))}, sort_keys=True)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


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
    if not OAUTH_CLIENT_SECRET:
        return "missing+POE_TW_CLIENT_SECRET"
    if not app.testing:
        from urllib.parse import urlsplit

        callback = urlsplit(uri)
        if callback.scheme != "https" or callback.netloc != request.host:
            return "invalid+POE_TW_REDIRECT_URI"
    if not _stash_storage_ready():
        return "missing+STASH_STORAGE_BUCKET"
    return None


def _pop_pkce_verifier(state: str) -> str | None:
    data = _stash_data()
    pending = data.get("pkce", {})
    if pending.get("state") != state:
        return None
    data.pop("pkce", None)
    _stash_store().save(_stash_owner(), data)
    if time.time() - float(pending.get("created_at", 0)) > OAUTH_STATE_TTL_SECONDS:
        return None
    return pending.get("verifier")


def _save_tokens(token_payload: dict, initial_authorization=False) -> None:
    data = _stash_data()
    subject = token_payload.get("sub")
    if (initial_authorization and (not subject or data.get("subject") != subject)) or (subject and data.get("subject") and data["subject"] != subject):
        data = {}
    if subject:
        data["subject"] = subject
    data.pop("session_auth", None)
    previous = data.get("tokens", {})
    data["tokens"] = {
        "access_token": token_payload.get("access_token", ""),
        "refresh_token": token_payload.get("refresh_token") or previous.get("refresh_token"),
        "expires_at": time.time() + max(int(token_payload.get("expires_in") or 0), 0),
        "token_type": token_payload.get("token_type", "Bearer"),
    }
    _stash_store().save(_stash_owner(create=True), data)


def _clear_tokens() -> None:
    owner = _stash_owner()
    if owner:
        data = _stash_data()
        data.pop("tokens", None)
        data.pop("pkce", None)
        _stash_store().save(owner, data)


def _load_tokens() -> dict | None:
    return _stash_data().get("tokens")


def _refresh_access_token(refresh_token: str) -> dict:
    if not OAUTH_CLIENT_ID:
        raise RuntimeError("missing POE_TW_CLIENT_ID")
    token_resp = requests.post(
        OAUTH_TOKEN_URL,
        data={
            "grant_type": "refresh_token",
            "client_id": OAUTH_CLIENT_ID,
            "client_secret": OAUTH_CLIENT_SECRET,
            "refresh_token": refresh_token,
        },
        timeout=12,
        headers={"Accept": "application/json", "User-Agent": build_oauth_user_agent(OAUTH_CLIENT_ID)},
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
        with closing(sqlite3.connect(STASH_DB)) as conn, conn:
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
    if not _stash_storage_ready():
        raise StashApiError(503, "Configure persistent private stash storage before syncing")
    data = _stash_data()
    try:
        fetched = fetch_account_stashes(access_token, game, league, OAUTH_CLIENT_ID)
    except StashApiError as error:
        if error.status == 401:
            _clear_tokens()
        raise
    return _persist_fetched_stash(fetched, game, league, "official-oauth")


def _clear_session_auth() -> None:
    owner = _stash_owner()
    if not owner:
        return
    data = _stash_data()
    data.pop("session_auth", None)
    _stash_store().save(owner, data)


def _sync_stash_with_session(session_auth: dict, game: str, league: str) -> dict:
    if not _stash_storage_ready():
        raise StashApiError(503, "Configure persistent private stash storage before syncing")
    try:
        fetched = fetch_account_stashes_with_session(session_auth["poe_session"], session_auth["account_name"], game, league)
    except StashApiError as error:
        if error.status == 401:
            _clear_session_auth()
        raise
    return _persist_fetched_stash(fetched, game, league, "session-cookie", session_auth)


def _persist_fetched_stash(fetched: dict, game: str, league: str, source: str, session_auth: dict | None = None) -> dict:
    data = _stash_data()
    datasets = _stash_datasets(game, league)
    selection = data.get("selection", {}) if data.get("league") == league and data.get("game") == game else {}
    stable_ids = {str(item["id"]) for tab in fetched["tabs"] for item in flatten_stash_items(tab.get("items")) if item.get("id")}
    selection = {**selection, "excluded_items": [identifier for identifier in selection.get("excluded_items", []) if identifier in stable_ids]}
    result = value_stashes(fetched["tabs"], datasets, game, league, selection.get("selected_tabs"), selection.get("excluded_items"))
    updated_at = time.time()
    data.update({**fetched, "selection": selection, "valuation": result, "updated_at": updated_at})
    history = data.get("history", [])[-199:]
    history.append({"created_at": updated_at, "total_divine": result["total_divine"], "unpriced_count": result["unpriced_count"], "game": game, "league": league, "selection_key": _stash_selection_key(data)})
    data["history"] = history
    if session_auth is not None:
        data.pop("tokens", None)
        data.pop("subject", None)
        data["session_auth"] = session_auth
    _stash_store().save(_stash_owner(create=True), data)
    return {**result, "account_name": fetched["account_name"], "updated_at": updated_at, "source": source}


def _stash_datasets(game, league):
    datasets = {}
    for kind in ("currency", "unique", "gem", "beast"):
        try:
            dataset = load_tw_price_dataset(game, kind)
        except FileNotFoundError:
            continue
        if dataset.get("game") != game or dataset.get("league") != league:
            raise ValueError("Published prices do not match the selected game and league")
        datasets[kind] = dataset
    return datasets


def _read_stash_state() -> dict | None:
    data = _stash_data()
    if not data.get("valuation"):
        return None
    return {**data["valuation"], "account_name": data.get("account_name", ""), "updated_at": data.get("updated_at", 0)}


def _read_stash_raw_payload() -> object | None:
    data = _stash_data()
    return {"tabs": data["tabs"]} if data.get("tabs") is not None else None


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
        with closing(sqlite3.connect(TRAFFIC_DB)) as conn, conn:
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
    with closing(sqlite3.connect(TRAFFIC_DB)) as conn, conn:
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
    strategy_unlocked = _is_strategy_unlocked()
    games = load_games(include_strategies=strategy_unlocked)
    shop_filters = load_shop_filters()
    traffic_stats = record_home_visit(request)
    return render_template(
        "index.html",
        games=games,
        shop_filters=shop_filters,
        traffic_stats=traffic_stats,
        strategy_unlocked=strategy_unlocked,
        strategy_password_configured=bool(STRATEGY_PASSWORD),
        price_navigation_icons=load_tw_price_navigation_icons(),
    )


def _is_strategy_unlocked() -> bool:
    if not STRATEGY_PASSWORD:
        return False
    expected = hashlib.sha256(STRATEGY_PASSWORD.encode("utf-8")).hexdigest()
    stored = session.get("strategy_password_digest", "")
    return isinstance(stored, str) and secrets.compare_digest(stored, expected)


@app.route("/api/strategy/unlock", methods=["POST"])
def unlock_strategy():
    if not STRATEGY_PASSWORD:
        return {"status": "error", "message": "尚未設定策略密碼"}, 503

    ip_address = request.remote_addr or "unknown"
    now = time.time()
    with _strategy_login_lock:
        attempts, started_at = _strategy_login_attempts.get(ip_address, (0, now))
        if now - started_at >= 900:
            attempts, started_at = 0, now
        if attempts >= 5:
            return {"status": "error", "message": "嘗試次數過多，請 15 分鐘後再試"}, 429

    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return {"status": "error", "message": "請提供 JSON 物件"}, 400
    password = payload.get("password")
    if not isinstance(password, str) or not secrets.compare_digest(password.encode("utf-8"), STRATEGY_PASSWORD.encode("utf-8")):
        with _strategy_login_lock:
            attempts, started_at = _strategy_login_attempts.get(ip_address, (0, now))
            if now - started_at >= 900:
                attempts, started_at = 0, now
            _strategy_login_attempts[ip_address] = (attempts + 1, started_at)
        return {"status": "error", "message": "密碼錯誤"}, 401

    with _strategy_login_lock:
        _strategy_login_attempts.pop(ip_address, None)
    session["strategy_password_digest"] = hashlib.sha256(STRATEGY_PASSWORD.encode("utf-8")).hexdigest()
    return {"status": "ok"}


@app.route("/api/strategy/lock", methods=["POST"])
def lock_strategy():
    session.pop("strategy_password_digest", None)
    return {"status": "ok"}


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/health/ready")
def readiness():
    checks = {
        "strategy_password": bool(STRATEGY_PASSWORD),
        "session_secret": bool(os.getenv("FLASK_SECRET_KEY") or os.getenv("SECRET_KEY")),
    }
    ready = all(checks.values())
    return {"status": "ok" if ready else "unavailable", "checks": checks}, 200 if ready else 503


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


@app.route("/stash")
def stash_dashboard():
    return render_template("stash.html")


@app.after_request
def private_stash_cache(response):
    if request.path == "/stash" or request.path.startswith(("/api/stash/", "/api/pricer/stash/")):
        response.headers["Cache-Control"] = "private, no-store"
    return response


@app.before_request
def stash_write_origin():
    if request.path.startswith("/api/stash/") and request.method == "POST":
        from urllib.parse import urlsplit

        origin = request.headers.get("Origin")
        if origin and urlsplit(origin).netloc != request.host:
            return {"status": "error", "message": "Cross-origin stash changes are not allowed"}, 403
        if not isinstance(request.get_json(silent=True), dict):
            return {"status": "error", "message": "Provide a JSON object"}, 400


@app.route("/api/stash/state")
def stash_dashboard_state():
    data = _stash_data()
    config_error = _validate_oauth_config()
    try:
        league = load_tw_price_dataset("poe1", "currency")["league"]
    except (FileNotFoundError, ValueError):
        league = ""
    history = [entry for entry in data.get("history", []) if entry.get("game") == data.get("game") and entry.get("league") == data.get("league") and entry.get("selection_key") == _stash_selection_key(data)]
    connection_setup = {
        "client_id": bool(OAUTH_CLIENT_ID),
        "client_secret": bool(OAUTH_CLIENT_SECRET),
        "registered_callback": bool(OAUTH_REDIRECT_URI),
        "private_storage": _stash_storage_ready(),
    }
    session_auth = data.get("session_auth", {})
    session_connected = bool(session_auth.get("poe_session") and session_auth.get("account_name"))
    return {"status": "ok", "oauth_configured": config_error is None, "oauth_connected": bool(data.get("tokens", {}).get("access_token")), "session_connected": session_connected, "connection_mode": "session-cookie" if session_connected else "oauth" if data.get("tokens", {}).get("access_token") else None, "config_error": config_error, "connection_setup": connection_setup, "supported_games": ["poe1"], "account_name": data.get("account_name", ""), "league": data.get("league") or league, "updated_at": data.get("updated_at"), "valuation": data.get("valuation"), "selection": data.get("selection", {}), "history": history, "storage": "private-gcs" if os.getenv("STASH_STORAGE_BUCKET") else "local-encrypted-sqlite"}


@app.route("/api/stash/session/connect", methods=["POST"])
def stash_session_connect():
    payload = request.get_json()
    account_name = payload.get("account_name")
    poe_session = payload.get("poe_session")
    game = payload.get("game", "poe1")
    league = payload.get("league")
    if payload.get("accepted_risk") is not True:
        return {"status": "error", "message": "Confirm the session-cookie access warning before connecting"}, 400
    if game != "poe1":
        return {"status": "unavailable", "message": "Session-cookie stash access currently supports PoE1 only"}, 409
    if not isinstance(league, str) or not league.strip() or len(league) > 100:
        return {"status": "error", "message": "Choose a league"}, 400
    if not isinstance(account_name, str) or not account_name.strip() or len(account_name) > 80 or any(ord(character) < 32 for character in account_name):
        return {"status": "error", "message": "Enter a valid Path of Exile account name"}, 400
    session_auth = {"account_name": account_name.strip(), "poe_session": poe_session}
    with _stash_lock:
        try:
            result = _sync_stash_with_session(session_auth, game, league.strip())
        except StashApiError as error:
            return {"status": "error", "message": str(error)}, error.status
        except (ValueError, FileNotFoundError) as error:
            return {"status": "unavailable", "message": str(error)}, 409
    return {"status": "ok", "stash": result}


@app.route("/api/stash/sync", methods=["POST"])
def stash_dashboard_sync():
    payload = request.get_json()
    game = payload.get("game", "poe1")
    league = payload.get("league")
    if game != "poe1":
        return {"status": "unavailable", "message": "Official private stash API currently supports PoE1 only"}, 409
    if not isinstance(league, str) or not league.strip() or len(league) > 100:
        return {"status": "error", "message": "Choose a league"}, 400
    with _stash_lock:
        data = _stash_data()
        session_auth = data.get("session_auth")
        if session_auth:
            try:
                result = _sync_stash_with_session(session_auth, game, league.strip())
            except StashApiError as error:
                return {"status": "error", "message": str(error)}, error.status
            except (ValueError, FileNotFoundError) as error:
                return {"status": "unavailable", "message": str(error)}, 409
            return {"status": "ok", "stash": result}
        token = _get_valid_access_token()
        if not token:
            return {"status": "error", "message": "Connect an account before syncing"}, 401
        try:
            result = _sync_stash_with_token(token, game, league.strip())
        except StashApiError as error:
            return {"status": "error", "message": str(error)}, error.status
        except (ValueError, FileNotFoundError) as error:
            return {"status": "unavailable", "message": str(error)}, 409
    return {"status": "ok", "stash": result}


@app.route("/api/stash/selection", methods=["POST"])
def stash_dashboard_selection():
    payload = request.get_json()
    selected = payload.get("selected_tabs")
    excluded = payload.get("excluded_items", [])
    if not isinstance(selected, list) or not isinstance(excluded, list) or len(selected) > 1000 or len(excluded) > 10000 or any(not isinstance(value, str) for value in selected + excluded):
        return {"status": "error", "message": "Invalid stash selection"}, 400
    with _stash_lock:
        data = _stash_data()
        if not data.get("tabs"):
            return {"status": "error", "message": "Sync stash contents before selecting tabs"}, 409
        tab_ids = {str(tab["id"]) for tab in data["tabs"]}
        item_ids = {str(item.get("id") or f'{tab["id"]}:{position}') for tab in data["tabs"] for position, item in enumerate(flatten_stash_items(tab.get("items")))}
        if set(selected) - tab_ids or set(excluded) - item_ids:
            return {"status": "error", "message": "Selection does not belong to this account"}, 400
        selection = {"selected_tabs": selected, "excluded_items": excluded}
        try:
            result = value_stashes(data["tabs"], _stash_datasets(data["game"], data["league"]), data["game"], data["league"], selected, excluded)
        except (ValueError, FileNotFoundError) as error:
            return {"status": "unavailable", "message": str(error)}, 409
        data.update({"selection": selection, "valuation": result})
        _stash_store().save(_stash_owner(), data)
    return {"status": "ok", "valuation": result}


@app.route("/api/stash/disconnect", methods=["POST"])
def stash_dashboard_disconnect():
    owner = _stash_owner()
    if owner:
        _stash_store().delete(owner)
    session.pop("stash_connection_id", None)
    return {"status": "ok"}


@app.route("/tw-pricer")
def legacy_tw_pricer():
    game = (request.args.get("game") or "poe1").strip().lower()
    if game not in ("poe1", "poe2"):
        game = "poe1"
    return redirect(f"/?panel={game}-tw-currency", code=302)


@app.route("/api/tw-pricer/<kind>")
def tw_pricer_dataset(kind):
    game = (request.args.get("game") or "poe1").strip().lower()
    if game not in ("poe1", "poe2"):
        return {"status": "error", "message": "無效的 game 參數"}, 400
    if kind not in ("currency", "unique", "gem", "beast") or (kind == "beast" and game != "poe1"):
        return {"status": "error", "message": "無效的物價類別"}, 404

    try:
        return load_tw_price_dataset(game, kind)
    except FileNotFoundError as exc:
        return {"status": "unavailable", "message": str(exc)}, 503
    except Exception as exc:
        return {"status": "error", "message": str(exc)}, 502


@app.route("/api/tw-pricer/refresh", methods=["POST"])
def refresh_tw_pricer_data():
    refresh_token = os.getenv("TW_CURRENCY_REFRESH_TOKEN", "")
    request_token = request.headers.get("X-Refresh-Token", "")
    if not refresh_token or not secrets.compare_digest(request_token, refresh_token):
        return {"status": "error", "message": "未授權的資料更新請求"}, 403

    try:
        updated = refresh_all_tw_prices()
    except Exception as exc:
        return {"status": "error", "message": str(exc)}, 502

    return {
        "status": "ok",
        "updated": {
            game: {
                kind: {"league": data["league"], "count": len(data["items"])}
                for kind, data in game_data.items()
            }
            for game, game_data in updated.items()
        },
    }


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
    session["oauth_return_path"] = "/stash" if request.args.get("return_to") == "stash" else "/pricer"
    config_error = _validate_oauth_config()
    if config_error:
        return _oauth_error_redirect(config_error)

    state = secrets.token_urlsafe(24)
    code_verifier, code_challenge = _build_pkce_pair()
    session["oauth_state"] = state
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


def _oauth_error_redirect(message):
    target = session.get("oauth_return_path", "/pricer")
    if target not in ("/stash", "/pricer"):
        target = "/pricer"
    return redirect(f"{target}?{urlencode({'oauth': 'error', 'message': message})}", code=302)


@app.route("/callback")
def pricer_oauth_callback():
    config_error = _validate_oauth_config()
    if config_error:
        return _oauth_error_redirect(config_error)

    if request.args.get("error"):
        err = request.args.get("error_description") or request.args.get("error")
        return _oauth_error_redirect(err)

    state = (request.args.get("state") or "").strip()
    code = (request.args.get("code") or "").strip()
    if not state or not code:
        return _oauth_error_redirect("missing state or code")

    session_state = str(session.get("oauth_state") or "")
    verifier = _pop_pkce_verifier(state) if session_state == state else None

    session.pop("oauth_state", None)
    session.pop("oauth_code_verifier", None)
    session.pop("oauth_state_created_at", None)

    if not verifier:
        return _oauth_error_redirect("invalid or expired state")

    redirect_uri = _resolve_oauth_redirect_uri()

    try:
        token_resp = requests.post(
            OAUTH_TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "client_id": OAUTH_CLIENT_ID,
                "client_secret": OAUTH_CLIENT_SECRET,
                "code": code,
                "redirect_uri": redirect_uri,
                "scope": OAUTH_SCOPE,
                "code_verifier": verifier,
            },
            timeout=12,
            headers={"Accept": "application/json", "User-Agent": build_oauth_user_agent(OAUTH_CLIENT_ID)},
        )
        if token_resp.status_code >= 400:
            return _oauth_error_redirect(f"token exchange failed {token_resp.status_code}")
        payload = token_resp.json()
        if not payload.get("access_token"):
            return _oauth_error_redirect("token missing")
        _save_tokens(payload, initial_authorization=True)

        return redirect("/stash?oauth=connected", code=302)
    except Exception as exc:
        return _oauth_error_redirect(str(exc))


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
    elif config_error == "missing+POE_TW_CLIENT_SECRET":
        config_message = "請先設定本站 OAuth client secret。"
    elif config_error == "missing+STASH_STORAGE_BUCKET":
        config_message = "請先設定正式倉庫持久儲存。"
    if state:
        state = {**state, "tabs": [{**tab, "enabled": tab.get("included", True)} for tab in state["tabs"]]}

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
    if len(league) > 100 or any(ord(character) < 32 for character in league):
        return {"status": "error", "message": "無效的聯盟名稱"}, 400

    access_token = _get_valid_access_token()
    if not access_token:
        return {"status": "error", "message": "尚未授權，請先登入。"}, 401

    try:
        stash_state = _sync_stash_with_token(access_token, game=game, league=league)
        return {"status": "ok", "stash": {**stash_state, "tabs": [{**tab, "enabled": tab.get("included", True)} for tab in stash_state["tabs"]]}}
    except StashApiError as error:
        return {"status": "error", "message": str(error)}, error.status
    except Exception as exc:
        return {"status": "error", "message": str(exc)}, 502


@app.route("/api/pricer/stash/resources")
def pricer_stash_resources():
    refresh = (request.args.get("refresh") or "").strip().lower() in ("1", "true", "yes")
    stash_state = _read_stash_state()

    if refresh:
        if not _load_tokens():
            return {"status": "error", "message": "尚未授權，請先登入。"}, 401
        data = _stash_data()
        if data.get("tabs") is not None:
            selection = data.get("selection", {})
            result = value_stashes(data["tabs"], _stash_datasets(data["game"], data["league"]), data["game"], data["league"], selection.get("selected_tabs"), selection.get("excluded_items"))
            stash_state = {**result, "account_name": data.get("account_name", ""), "updated_at": data.get("updated_at", 0)}

    if not stash_state:
        return {"status": "error", "message": "尚無倉庫資料，請先完成授權並同步。"}, 404

    resources = [{**row, "tab_count": len(row["tabs"])} for row in stash_state["resources"]]
    categories = [{"category": category["id"], "value_divine": category["value_divine"], "kinds": sum(row["category"] == category["id"] for row in resources), "quantity": sum(row["quantity"] for row in resources if row["category"] == category["id"])} for category in stash_state["categories"]]
    stats = {"resources": resources, "categories": categories, "resource_count": len(resources), "item_instances": sum(len(row["item_ids"]) for row in resources), "unpriced_count": stash_state["unpriced_count"]}
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
