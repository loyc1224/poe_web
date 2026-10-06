from urllib.parse import quote

import requests


API_BASE = "https://api.pathofexile.com"


class StashApiError(RuntimeError):
    def __init__(self, status, message):
        self.status = status
        super().__init__(message)


def _get(path, access_token):
    try:
        response = requests.get(API_BASE + path, headers={"Authorization": f"Bearer {access_token}", "Accept": "application/json", "Accept-Language": "zh-TW", "User-Agent": "poe-web stash/1.0"}, timeout=20)
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


def fetch_account_stashes(access_token, game, league, selected_tabs=None):
    if game != "poe1":
        raise StashApiError(409, "Official private stash API currently supports PoE1 only")
    profile = _get("/profile", access_token)
    if not isinstance(profile, dict) or not profile.get("name"):
        raise StashApiError(502, "Official account profile is invalid")
    root = _get("/stash/" + quote(league, safe=""), access_token)
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
        details = _get(path + quote(tab_id, safe=""), access_token)
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