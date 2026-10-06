"""
poe.ninja API client — 附帶檔案快取，避免頻繁請求。
"""
import json
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

from .config import CACHE_TTL, ECONOMY_TYPES, LEAGUE_NAME, POE1_ECONOMY_TYPES, POE1_LEAGUE
from .translations import ITEM_ZH

# ── 快取目錄 ─────────────────────────────────────────────────────────────────
CACHE_DIR = Path(__file__).resolve().parents[2] / "cache"
CACHE_DIR.mkdir(exist_ok=True)

# ── API 端點 ─────────────────────────────────────────────────────────────────
# PoE2 新版 economy API（Currency Exchange 措主）
_BASE_ECONOMY_POE2 = "https://poe.ninja/poe2/api/economy/exchange/current/overview"
# PoE1 economy API（exchange 類型，結構同 PoE2）
_BASE_ECONOMY_POE1 = "https://poe.ninja/poe1/api/economy/exchange/current/overview"
_HEADERS = {
    "User-Agent": "poe-monitor/1.0 (+personal project)",
    "Accept": "application/json",
}

# ── 快取工具 ─────────────────────────────────────────────────────────────────

def _cache_path(key: str) -> Path:
    return CACHE_DIR / f"{key}.json"


def _load_cache(key: str, ttl: int) -> dict | None:
    path = _cache_path(key)
    if not path.exists():
        return None
    if time.time() - path.stat().st_mtime > ttl:
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _save_cache(key: str, data: dict) -> None:
    with open(_cache_path(key), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def _get(url: str, params: dict) -> dict:
    resp = requests.get(url, params=params, headers=_HEADERS, timeout=5)
    resp.raise_for_status()
    return resp.json()


# ── Economy 資料 ─────────────────────────────────────────────────────────────

def fetch_economy(league: str = LEAGUE_NAME, force: bool = False) -> dict:
    """抓取 poe.ninja PoE2 Currency Exchange economy。"""
    cache_key = f"economy_{league}"
    if not force:
        cached = _load_cache(cache_key, CACHE_TTL["economy"])
        if cached:
            return cached

    items: list[dict] = []
    errors: list[str] = []

    def _fetch_type(item_type: str, label: str):
        raw = _get(_BASE_ECONOMY_POE2, {"league": league, "type": item_type})
        # id → {name, image} lookup
        id_to_item: dict[str, dict] = {}
        for entry in (raw.get("items") or []):
            if isinstance(entry, dict) and entry.get("id"):
                id_to_item[entry["id"]] = {"name": entry.get("name", entry["id"]), "image": entry.get("image", "")}
        result_items = []
        for line in (raw.get("lines") or []):
            item_id  = line.get("id", "")
            item_meta = id_to_item.get(item_id, {})
            name     = item_meta.get("name", item_id)
            icon     = item_meta.get("image", "")
            spark    = line.get("sparkline") or {}
            spark_d  = spark.get("data") or []
            divine_rate = line.get("maxVolumeRate", 0) or 0
            change_1d = 0.0
            valid = [v for v in spark_d if v is not None]
            if len(valid) >= 2:
                prev, curr = valid[-2], valid[-1]
                if prev and curr:
                    change_1d = round((curr - prev) / abs(prev) * 100, 1)
            pv = line.get("primaryValue") or 0
            result_items.append({
                "name":      name,
                "zh":        ITEM_ZH.get(item_id, ""),
                "type":      item_type,
                "label":     label,
                "chaos":     round(pv, 4),            # divine price per item
                "rate":      round(divine_rate, 1),   # items per divine
                "unit":      line.get("maxVolumeCurrency", "divine"),
                "change_1d": change_1d,
                "change_7d": round(spark.get("totalChange") or 0.0, 1),
                "volume":    round(line.get("volumePrimaryValue") or 0, 2),
                "icon":      icon,
            })
        return result_items, None

    with ThreadPoolExecutor(max_workers=len(ECONOMY_TYPES)) as pool:
        futures = {
            pool.submit(_fetch_type, item_type, label): item_type
            for item_type, label in ECONOMY_TYPES
        }
        for fut in futures:
            item_type = futures[fut]
            try:
                result_items, _ = fut.result()
                items.extend(result_items)
            except requests.HTTPError as exc:
                code = exc.response.status_code if exc.response is not None else 0
                errors.append(f"{item_type}: {'League not found' if code == 404 else f'HTTP {code}'}")
            except Exception as exc:
                errors.append(f"{item_type}: {exc}")

    # 依 1 日漲幅降冪排列
    items.sort(key=lambda x: x["change_1d"], reverse=True)

    result = {
        "items": items,
        "fetched_at": time.time(),
        "league": league,
        "status": "ok" if not errors else ("unavailable" if not items else "partial"),
        "errors": errors,
    }
    _save_cache(cache_key, result)
    return result


def fetch_poe1_economy(league: str = POE1_LEAGUE, force: bool = False) -> dict:
    """��� poe.ninja PoE1 economy�]Currency Exchange API�Achaos ����ǡ^�C"""
    cache_key = f"poe1_economy_{league}"
    if not force:
        cached = _load_cache(cache_key, CACHE_TTL["economy"])
        if cached:
            return cached

    items: list[dict] = []
    errors: list[str] = []

    def _fetch_type(item_type: str, label: str):
        raw = _get(_BASE_ECONOMY_POE1, {"league": league, "type": item_type})
        id_to_item: dict[str, dict] = {}
        for entry in (raw.get("items") or []):
            if isinstance(entry, dict) and entry.get("id"):
                id_to_item[entry["id"]] = {
                    "name":  entry.get("name", entry["id"]),
                    "image": entry.get("image", ""),
                }
        result_items = []
        for line in (raw.get("lines") or []):
            item_id   = line.get("id", "")
            item_meta = id_to_item.get(item_id, {})
            name      = item_meta.get("name", item_id)
            icon      = item_meta.get("image", "")
            spark     = line.get("sparkline") or {}
            spark_d   = spark.get("data") or []
            chaos_val = line.get("primaryValue") or 0
            change_1d = 0.0
            valid = [v for v in spark_d if v is not None]
            if len(valid) >= 2:
                prev, curr = valid[-2], valid[-1]
                if prev and curr:
                    change_1d = round((curr - prev) / abs(prev) * 100, 1)
            result_items.append({
                "name":      name,
                "zh":        ITEM_ZH.get(item_id, ""),
                "type":      item_type,
                "label":     label,
                "chaos":     round(chaos_val, 2),
                "change_1d": change_1d,
                "change_7d": round(spark.get("totalChange") or 0.0, 1),
                "volume":    round(line.get("volumePrimaryValue") or 0, 2),
                "icon":      icon,
            })
        return result_items, None

    with ThreadPoolExecutor(max_workers=len(POE1_ECONOMY_TYPES)) as pool:
        futures = {
            pool.submit(_fetch_type, item_type, label): item_type
            for item_type, label in POE1_ECONOMY_TYPES
        }
        for fut in futures:
            item_type = futures[fut]
            try:
                result_items, _ = fut.result()
                items.extend(result_items)
            except requests.HTTPError as exc:
                code = exc.response.status_code if exc.response is not None else 0
                errors.append(f"{item_type}: {'League not found' if code == 404 else f'HTTP {code}'}")
            except Exception as exc:
                errors.append(f"{item_type}: {exc}")

    items.sort(key=lambda x: x["change_1d"], reverse=True)

    result = {
        "items":      items,
        "fetched_at": time.time(),
        "league":     league,
        "status":     "ok" if not errors else ("unavailable" if not items else "partial"),
        "errors":     errors,
    }
    _save_cache(cache_key, result)
    return result


def fetch_poe1_economy(league: str = POE1_LEAGUE, force: bool = False) -> dict:
    """抓取 poe.ninja PoE1 economy（Currency Exchange API，chaos 為基準）。"""
    cache_key = f"poe1_economy_{league}"
    if not force:
        cached = _load_cache(cache_key, CACHE_TTL["economy"])
        if cached:
            return cached

    items: list[dict] = []
    errors: list[str] = []

    def _fetch_type(item_type: str, label: str):
        raw = _get(_BASE_ECONOMY_POE1, {"league": league, "type": item_type})
        id_to_item: dict[str, dict] = {}
        for entry in (raw.get("items") or []):
            if isinstance(entry, dict) and entry.get("id"):
                id_to_item[entry["id"]] = {
                    "name":  entry.get("name", entry["id"]),
                    "image": entry.get("image", ""),
                }
        result_items = []
        for line in (raw.get("lines") or []):
            item_id   = line.get("id", "")
            item_meta = id_to_item.get(item_id, {})
            name      = item_meta.get("name", item_id)
            icon      = item_meta.get("image", "")
            spark     = line.get("sparkline") or {}
            spark_d   = spark.get("data") or []
            chaos_val = line.get("primaryValue") or 0
            change_1d = 0.0
            valid = [v for v in spark_d if v is not None]
            if len(valid) >= 2:
                prev, curr = valid[-2], valid[-1]
                if prev and curr:
                    change_1d = round((curr - prev) / abs(prev) * 100, 1)
            result_items.append({
                "name":      name,
                "zh":        ITEM_ZH.get(item_id, ""),
                "type":      item_type,
                "label":     label,
                "chaos":     round(chaos_val, 2),
                "change_1d": change_1d,
                "change_7d": round(spark.get("totalChange") or 0.0, 1),
                "volume":    round(line.get("volumePrimaryValue") or 0, 2),
                "icon":      icon,
            })
        return result_items, None

    with ThreadPoolExecutor(max_workers=len(POE1_ECONOMY_TYPES)) as pool:
        futures = {
            pool.submit(_fetch_type, item_type, label): item_type
            for item_type, label in POE1_ECONOMY_TYPES
        }
        for fut in futures:
            item_type = futures[fut]
            try:
                result_items, _ = fut.result()
                items.extend(result_items)
            except requests.HTTPError as exc:
                code = exc.response.status_code if exc.response is not None else 0
                errors.append(f"{item_type}: {'League not found' if code == 404 else f'HTTP {code}'}")
            except Exception as exc:
                errors.append(f"{item_type}: {exc}")

    items.sort(key=lambda x: x["change_1d"], reverse=True)

    result = {
        "items":      items,
        "fetched_at": time.time(),
        "league":     league,
        "status":     "ok" if not errors else ("unavailable" if not items else "partial"),
        "errors":     errors,
    }
    _save_cache(cache_key, result)
    return result
