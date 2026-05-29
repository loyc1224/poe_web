"""
poe.ninja API client — 附帶檔案快取，避免頻繁請求。
"""
import json
import time
from pathlib import Path

import requests

from .config import BEAST_TARGETS, CACHE_TTL, ECONOMY_TYPES, LEAGUE_NAME

# ── 快取目錄 ─────────────────────────────────────────────────────────────────
CACHE_DIR = Path(__file__).resolve().parent.parent / "cache"
CACHE_DIR.mkdir(exist_ok=True)

# ── API 端點 ─────────────────────────────────────────────────────────────────
_BASE_BUILDS   = "https://poe.ninja/api/data/getbuildoverview"
_BASE_ITEM     = "https://poe.ninja/api/data/itemoverview"
_BASE_CURRENCY = "https://poe.ninja/api/data/currencyoverview"

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
    resp = requests.get(url, params=params, headers=_HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.json()


# ── Builds 資料 ──────────────────────────────────────────────────────────────

def fetch_builds(league: str = LEAGUE_NAME, force: bool = False) -> dict:
    """抓取 poe.ninja builds，分析 Spirit Walker companion 使用率。"""
    cache_key = f"builds_{league}"
    if not force:
        cached = _load_cache(cache_key, CACHE_TTL["builds"])
        if cached:
            return cached

    try:
        raw = _get(_BASE_BUILDS, {"overview": league, "type": "exp", "language": "en"})
        result = _parse_builds(raw)
        result.update({"fetched_at": time.time(), "league": league, "status": "ok"})
    except requests.HTTPError as exc:
        status_code = exc.response.status_code if exc.response is not None else 0
        msg = "聯盟尚未開始或找不到資料" if status_code == 404 else str(exc)
        result = {
            "status": "unavailable", "error": msg,
            "league": league, "fetched_at": time.time(),
            "total_characters": 0, "spirit_walker_count": 0,
            "companion_counts": {b["id"]: 0 for b in BEAST_TARGETS},
        }
    except Exception as exc:
        result = {
            "status": "error", "error": str(exc),
            "league": league, "fetched_at": time.time(),
            "total_characters": 0, "spirit_walker_count": 0,
            "companion_counts": {b["id"]: 0 for b in BEAST_TARGETS},
        }

    _save_cache(cache_key, result)
    return result


def _parse_builds(raw: dict) -> dict:
    """從 poe.ninja 原始 builds 資料解析 Spirit Walker 使用狀況。"""
    companion_counts = {b["id"]: 0 for b in BEAST_TARGETS}
    spirit_walker_count = 0
    total = 0

    headers = raw.get("headers", [])
    rows = raw.get("data", [])

    # 找出各欄位的 index
    def _col(name: str) -> int:
        try:
            return headers.index(name)
        except ValueError:
            return -1

    asc_idx    = _col("Ascendancy")
    skills_idx = _col("ActiveSkills")

    for row in rows:
        if not isinstance(row, list):
            continue
        total += 1

        asc = (row[asc_idx] or "").lower() if 0 <= asc_idx < len(row) else ""
        is_sw = any(v in asc for v in ("spiritwalker", "spirit walker", "spirit_walker"))
        if is_sw:
            spirit_walker_count += 1

        skills_raw = row[skills_idx] if 0 <= skills_idx < len(row) else []
        skills_text = " ".join(str(s).lower() for s in skills_raw) if isinstance(skills_raw, list) else str(skills_raw).lower()

        for beast in BEAST_TARGETS:
            for kw in beast["keywords"]:
                if kw in skills_text:
                    companion_counts[beast["id"]] += 1
                    break

    return {
        "total_characters": total,
        "spirit_walker_count": spirit_walker_count,
        "companion_counts": companion_counts,
    }


# ── Economy 資料 ─────────────────────────────────────────────────────────────

def fetch_economy(league: str = LEAGUE_NAME, force: bool = False) -> dict:
    """抓取 poe.ninja economy，整合各品項的漲幅資料。"""
    cache_key = f"economy_{league}"
    if not force:
        cached = _load_cache(cache_key, CACHE_TTL["economy"])
        if cached:
            return cached

    items: list[dict] = []
    errors: list[str] = []

    for ep_type, item_type, label in ECONOMY_TYPES:
        try:
            url = _BASE_CURRENCY if ep_type == "currency" else _BASE_ITEM
            raw = _get(url, {"league": league, "type": item_type, "language": "en"})

            for entry in raw.get("lines", []):
                spark = entry.get("sparkline") or {}
                spark_data = spark.get("data") or []

                # 計算 1 日漲幅
                change_1d = 0.0
                if len(spark_data) >= 2:
                    prev, curr = spark_data[-2], spark_data[-1]
                    if prev and curr:
                        change_1d = round((curr - prev) / prev * 100, 1)

                chaos_val = entry.get("chaosValue") or entry.get("chaosEquivalent") or 0

                items.append({
                    "name":       entry.get("name", ""),
                    "type":       item_type,
                    "label":      label,
                    "chaos":      round(chaos_val, 1),
                    "change_1d":  change_1d,
                    "change_7d":  round(spark.get("totalChange") or 0.0, 1),
                    "volume":     entry.get("count") or 0,
                    "icon":       entry.get("icon", ""),
                })
        except requests.HTTPError as exc:
            status_code = exc.response.status_code if exc.response is not None else 0
            if status_code == 404:
                errors.append(f"{item_type}: 聯盟尚未開始")
            else:
                errors.append(f"{item_type}: HTTP {status_code}")
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
