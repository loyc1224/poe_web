"""Scheduled collector for POE Pricer TW currency datasets."""
import time

import requests

from .tw_pricer_client import save_tw_price_dataset


_API_BASE = "https://www.poepricer.com/api/v1"
_HEADERS = {"Accept": "application/json", "User-Agent": "poe-web/1.0 scheduled-currency-refresh"}
_UNIT_ITEM_NAMES = {"chaos": "混沌石", "divine": "神聖石", "exalt": "崇高石"}
_UNIQUE_CATEGORY_LABELS = {
    "currency": "特殊物品",
    "heistmission": "劫盜契約",
    "map": "傳奇地圖",
    "sanctum": "聖所聖物",
}
_BEAST_CATEGORY_LABELS = {"red": "紅色野獸", "yellow": "黃色野獸"}


def _get_categories(game: str, kind: str, rows: list[dict]) -> list[dict]:
    response = requests.get(
        f"{_API_BASE}/{game}/{kind}/categories", headers=_HEADERS, timeout=20
    )
    response.raise_for_status()
    categories = response.json().get("categories", [])
    if not isinstance(categories, list):
        raise ValueError(f"{game} {kind} 分類資料格式無效")

    by_id = {}
    for source_category in categories:
        if not isinstance(source_category, dict) or not source_category.get("id"):
            continue
        category = dict(source_category)
        category_image = category.get("imageUrl") or category.get("image")
        if category_image:
            category["imageUrl"] = category_image
        by_id[category["id"]] = category

    for item in rows:
        category_id = _item_category_id(kind, item)
        if not category_id:
            continue
        category_label = item.get("category_label") or _UNIQUE_CATEGORY_LABELS.get(category_id) or category_id
        if category_id not in by_id:
            by_id[category_id] = {"id": category_id, "label": category_label}
        elif category_id in _UNIQUE_CATEGORY_LABELS:
            by_id[category_id]["label"] = _UNIQUE_CATEGORY_LABELS[category_id]

    for category_id, category in by_id.items():
        if category.get("imageUrl"):
            continue
        category_image = next(
            (
                item.get("imageUrl") or item.get("image")
                for item in rows
                if _item_category_id(kind, item) == category_id and (item.get("imageUrl") or item.get("image"))
            ),
            None,
        )
        if category_image:
            category["imageUrl"] = category_image
    return list(by_id.values())


def _item_category_id(kind: str, item: dict):
    if kind in ("currency", "gem"):
        return item.get("category_id")
    if kind == "beast":
        return item.get("beastType")
    return item.get("category")


def _dataset(game: str, kind: str, league: str, items: list[dict], categories: list[dict], unit_icons: dict) -> dict:
    if kind == "currency":
        updated_at = max((item.get("last_updated", "") for item in items), default="")
    else:
        updated_at = max(
            (item.get("lastPricedAt") or item.get("last_updated") or item.get("time", "") for item in items),
            default="",
        )
    status = "ok" if items else "unavailable"
    message = "" if items else f"此遊戲目前沒有可用的{ {'unique': '傳奇', 'gem': '寶石', 'beast': '野獸'}.get(kind, '物價') }行情資料"
    return {
        "schema_version": 1,
        "status": status,
        "message": message,
        "game": game,
        "kind": kind,
        "category": kind,
        "league": league,
        "fetched_at": time.time(),
        "source_updated_at": updated_at,
        "source": "POE Pricer TW",
        "categories": categories,
        "unit_icons": unit_icons,
        "items": items,
    }


def refresh_tw_prices(game: str) -> dict[str, dict]:
    if game not in ("poe1", "poe2"):
        raise ValueError("game must be poe1 or poe2")

    league_response = requests.get(
        f"{_API_BASE}/{game}/league/latest", headers=_HEADERS, timeout=10
    )
    league_response.raise_for_status()
    league = league_response.json().get("league")
    if not league:
        raise ValueError(f"{game} 行情來源未提供目前聯盟")

    results = {}
    unit_icons = {}
    kinds = ("currency", "unique", "gem", "beast") if game == "poe1" else ("currency", "unique", "gem")
    for kind in kinds:
        categories = []
        items = []
        response = requests.get(
            f"{_API_BASE}/{game}/gem/categories"
            if kind == "gem"
            else f"{_API_BASE}/{game}/beast/latest"
            if kind == "beast"
            else f"{_API_BASE}/{game}/{kind}/latest",
            params={"league": league} if kind not in ("gem", "beast") else None,
            headers=_HEADERS,
            timeout=20,
        )
        response.raise_for_status()
        payload = response.json()

        if kind == "beast":
            if not isinstance(payload, dict) or not isinstance(payload.get("items"), list):
                raise ValueError("poe1 beast 行情來源回傳格式無效")
            source_league = payload.get("league")
            if source_league and source_league != league:
                raise ValueError(f"野獸資料聯盟不符：{source_league} != {league}")
            items = payload["items"]
            type_ids = sorted({item.get("beastType") for item in items if item.get("beastType")})
            categories = [
                {
                    "id": type_id,
                    "label": _BEAST_CATEGORY_LABELS.get(type_id, type_id),
                    "imageUrl": next(
                        (item.get("imageUrl") for item in items if item.get("beastType") == type_id and item.get("imageUrl")),
                        "",
                    ),
                }
                for type_id in type_ids
            ]
        elif kind == "gem":
            if not isinstance(payload, dict) or not isinstance(payload.get("categories"), list):
                raise ValueError(f"{game} gem 分類清單格式無效")
            source_categories = payload["categories"]
            if not source_categories:
                categories = []
            else:
                for category in source_categories:
                    category_id = category.get("id")
                    if not category_id:
                        continue
                    gem_response = requests.get(
                        f"{_API_BASE}/{game}/gem/latest",
                        params={"league": league, "category": category_id},
                        headers=_HEADERS,
                        timeout=25,
                    )
                    gem_response.raise_for_status()
                    category_items = gem_response.json()
                    if not isinstance(category_items, list):
                        raise ValueError(f"{game} gem {category_id} 回傳格式無效")
                    categories.append({
                        **category,
                        "label": category.get("label") or category_id,
                        "imageUrl": category.get("imageUrl") or next(
                            (item.get("imageUrl") for item in category_items if item.get("imageUrl")),
                            "",
                        ),
                    })
                    items.extend(
                        {**item, "category_id": category_id, "category_label": category.get("label") or category_id}
                        for item in category_items
                    )
        else:
            if not isinstance(payload, list):
                raise ValueError(f"{game} {kind} 行情來源回傳格式無效")
            items = payload

        if kind == "currency":
            if not items:
                raise ValueError(f"{game} 行情來源沒有通貨資料，保留上一版資料集")
            unit_icons = {
                unit: item.get("image")
                for item in items
                for unit, item_name in _UNIT_ITEM_NAMES.items()
                if item.get("name") == item_name and item.get("image")
            }
        if kind in ("currency", "unique"):
            categories = _get_categories(game, kind, items)

        result = _dataset(game, kind, league, items, categories, unit_icons)
        save_tw_price_dataset(game, kind, result)
        results[kind] = result
    return results


def refresh_all_tw_prices() -> dict[str, dict]:
    results = {}
    errors = {}
    for game in ("poe1", "poe2"):
        try:
            results[game] = refresh_tw_prices(game)
        except Exception as error:
            errors[game] = str(error)
    if errors:
        raise RuntimeError(f"台服物價更新未完整完成：{errors}")
    return results