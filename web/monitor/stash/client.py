import re
import time
from urllib.parse import quote
from urllib.parse import urlencode

import requests


API_BASE = "https://api.pathofexile.com"
SESSION_API_BASE = "https://pathofexile.tw"
SESSION_COOKIE_PATTERN = re.compile(r"^[A-Fa-f0-9]{32}$")
SESSION_MIN_REQUEST_INTERVAL_SECONDS = 0.25
APP_VERSION = "1.0.0"
CONTACT_URL = "https://github.com/loyc1224/poe_web/issues"


def build_oauth_user_agent(client_id):
    if not isinstance(client_id, str) or not client_id.strip():
        raise ValueError("A registered OAuth client ID is required")
    return f"OAuth {client_id.strip()}/{APP_VERSION} (contact: {CONTACT_URL}) poe-web/stash"


class StashApiError(RuntimeError):
    def __init__(self, status, message):
        self.status = status
        super().__init__(message)


def _get(path, access_token, client_id):
    try:
        response = requests.get(API_BASE + path, headers={"Authorization": f"Bearer {access_token}", "Accept": "application/json", "Accept-Language": "zh-TW", "User-Agent": build_oauth_user_agent(client_id)}, timeout=20)
    except requests.RequestException as error:
        raise StashApiError(502, "Official stash service is unreachable") from error
    if response.status_code == 401:
        raise StashApiError(401, "Account authorization expired; reconnect the account")
    if response.status_code == 403:
        raise StashApiError(403, "Account authorization does not include stash access")
    if response.status_code == 429:
        raise StashApiError(429, "Official stash API rate limit reached; try again later")
    if not response.ok:
        raise StashApiError(502, "Official stash API rejected the request")
    try:
        return response.json()
    except ValueError as error:
        raise StashApiError(502, "Official stash API returned invalid JSON") from error


def fetch_account_stashes(access_token, game, league, client_id, selected_tabs=None):
    if game != "poe1":
        raise StashApiError(409, "Official private stash API currently supports PoE1 only")
    profile = _get("/profile", access_token, client_id)
    if not isinstance(profile, dict) or not profile.get("name"):
        raise StashApiError(502, "Official account profile is invalid")
    root = _get("/stash/" + quote(league, safe=""), access_token, client_id)
    if not isinstance(root, dict) or not isinstance(root.get("stashes"), list):
        raise StashApiError(502, "Official stash list is invalid")
    selected = None if selected_tabs is None else set(selected_tabs)
    tabs = {}

    def visit(tab):
        if not isinstance(tab, dict) or not tab.get("id"):
            raise StashApiError(502, "Official stash tab is invalid")
        for child in tab.get("children") or []:
            visit(child)
        if tab.get("metadata", {}).get("folder"):
            return
        tab_id = str(tab["id"])
        if tab_id in tabs:
            return
        if selected is not None and tab_id not in selected:
            tabs[tab_id] = {**tab, "items": []}
            return
        path = "/stash/" + quote(league, safe="") + "/"
        if tab.get("parent"):
            path += quote(str(tab["parent"]), safe="") + "/"
        details = _get(path + quote(tab_id, safe=""), access_token, client_id)
        stash = details.get("stash") if isinstance(details, dict) else None
        if isinstance(stash, dict) and stash.get("id") != tab_id:
            stash = next((child for child in stash.get("children", []) if isinstance(child, dict) and child.get("id") == tab_id), None)
        if not isinstance(stash, dict) or not isinstance(stash.get("items") or [], list) or any(not isinstance(item, dict) for item in stash.get("items") or []):
            raise StashApiError(502, "Official stash contents are invalid")
        if any(item.get("realm") == "poe2" or (item.get("league") and item["league"] != league) for item in stash.get("items") or []):
            raise StashApiError(409, "Official stash items do not match the requested game and league")
        tabs[tab_id] = {**tab, **stash, "items": stash.get("items") or [], "children": []}

    for tab in root["stashes"]:
        visit(tab)
    return {"account_name": profile["name"], "game": game, "league": league, "tabs": list(tabs.values())}


def fetch_account_stashes_with_session(session_cookie, account_name, game, league):
    if game != "poe1":
        raise StashApiError(409, "Session-cookie stash access currently supports PoE1 only")
    if not isinstance(session_cookie, str) or not SESSION_COOKIE_PATTERN.fullmatch(session_cookie):
        raise StashApiError(400, "POESESSID must be the 32-character session value")
    if not isinstance(account_name, str) or not account_name.strip() or len(account_name) > 80 or any(ord(character) < 32 for character in account_name):
        raise StashApiError(400, "Enter a valid Path of Exile account name")

    last_request_at = 0.0

    def fetch_tab(index):
        nonlocal last_request_at
        if last_request_at:
            remaining = SESSION_MIN_REQUEST_INTERVAL_SECONDS - (time.monotonic() - last_request_at)
            if remaining > 0:
                time.sleep(remaining)
        query = urlencode({"league": league, "accountName": account_name.strip(), "tabs": 1, "tabIndex": index})
        try:
            response = requests.get(
                f"{SESSION_API_BASE}/character-window/get-stash-items?{query}",
                headers={
                    "Cookie": f"POESESSID={session_cookie}",
                    "Accept": "application/json",
                    "Accept-Language": "zh-TW",
                    "User-Agent": "POE-Knowledge-Base stash-session/1.0",
                },
                timeout=20,
                allow_redirects=False,
            )
        except requests.RequestException as error:
            raise StashApiError(502, "Path of Exile stash service is unreachable") from error
        last_request_at = time.monotonic()
        if response.status_code in (401, 403):
            raise StashApiError(401, "POESESSID is invalid or expired; reconnect the account")
        if response.status_code == 429:
            raise StashApiError(429, "Path of Exile stash service rate limit reached; try again later")
        if not response.ok:
            raise StashApiError(502, "Path of Exile stash service rejected the request")
        try:
            payload = response.json()
        except ValueError as error:
            raise StashApiError(502, "Path of Exile stash response is invalid JSON") from error
        if not isinstance(payload, dict) or not isinstance(payload.get("tabs"), list) or not isinstance(payload.get("items", []), list):
            raise StashApiError(502, "Path of Exile stash response has an invalid shape")
        return payload

    first_page = fetch_tab(0)
    tab_metadata = first_page["tabs"]
    if not tab_metadata or len(tab_metadata) > 256:
        raise StashApiError(502, "Path of Exile stash tab list is empty or too large")

    tabs = []
    for position, metadata in enumerate(tab_metadata):
        if not isinstance(metadata, dict):
            raise StashApiError(502, "Path of Exile stash tab is invalid")
        index = metadata.get("i", position)
        name = metadata.get("n")
        tab_type = metadata.get("type")
        if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < 256:
            raise StashApiError(502, "Path of Exile stash tab index is invalid")
        if not isinstance(name, str) or not name or len(name) > 160 or not isinstance(tab_type, str) or not tab_type:
            raise StashApiError(502, "Path of Exile stash tab metadata is invalid")
        detail = first_page if index == 0 else fetch_tab(index)
        items = detail.get("items", [])
        if any(not isinstance(item, dict) for item in items):
            raise StashApiError(502, "Path of Exile stash items are invalid")
        colour = metadata.get("colour") or {}
        colour_value = ""
        if isinstance(colour, dict) and all(isinstance(colour.get(channel), int) and 0 <= colour[channel] <= 255 for channel in ("r", "g", "b")):
            colour_value = "{:02x}{:02x}{:02x}".format(colour["r"], colour["g"], colour["b"])
        tabs.append({
            "id": str(metadata.get("id") or f"legacy-tab-{index}"),
            "name": name,
            "type": tab_type,
            "metadata": {"colour": colour_value, "folder": tab_type == "Folder"},
            "items": items,
            "children": [],
        })

    return {"account_name": account_name.strip(), "game": game, "league": league, "tabs": tabs}