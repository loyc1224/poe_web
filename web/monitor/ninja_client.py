"""
poe.ninja API client — 附帶檔案快取，避免頻繁請求。
"""
import json
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

from .config import BEAST_TARGETS, CACHE_TTL, ECONOMY_TYPES, LEAGUE_NAME, POE1_ECONOMY_TYPES, POE1_LEAGUE
from .translations import ITEM_ZH

# ── 快取目錄 ─────────────────────────────────────────────────────────────────
CACHE_DIR = Path(__file__).resolve().parent.parent / "cache"
CACHE_DIR.mkdir(exist_ok=True)

# ── API 端點 ─────────────────────────────────────────────────────────────────
# PoE2 新版 economy API（Currency Exchange 措主）
_BASE_ECONOMY_POE2 = "https://poe.ninja/poe2/api/economy/exchange/current/overview"
# PoE1 economy API（exchange 類型，結構同 PoE2）
_BASE_ECONOMY_POE1 = "https://poe.ninja/poe1/api/economy/exchange/current/overview"
# PoE2 Builds 目前尚未公開，用舊路徑備用
_BASE_BUILDS      = "https://poe.ninja/api/data/getbuildoverview"

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


# ── Meta Builds（熱門流派 / 技能排行 / DPS）──────────────────────────────────

def fetch_meta_builds(league: str = LEAGUE_NAME, force: bool = False) -> dict:
    """抓取熱門流派：技能排行、DPS/等級排行、角色列表（含 poe.ninja 連結）。"""
    cache_key = f"meta_{league}"
    if not force:
        cached = _load_cache(cache_key, CACHE_TTL["builds"])
        if cached:
            return cached

    results: list[dict] = []
    errors: list[str] = []

    for btype in ("exp", "dps"):
        try:
            raw = _get(_BASE_BUILDS, {"overview": league, "type": btype, "language": "en"})
            results.append(_parse_meta_builds(raw, league, btype))
        except requests.HTTPError as exc:
            code = exc.response.status_code if exc.response is not None else 0
            errors.append(f"{btype}: {'聯盟尚未開始' if code == 404 else f'HTTP {code}'}")
        except Exception as exc:
            errors.append(f"{btype}: {exc}")

    if not results:
        result = {
            "status": "unavailable", "error": "、".join(errors),
            "league": league, "fetched_at": time.time(),
            "top_builds": [], "skill_stats": [], "asc_stats": [],
            "ninja_overview_url": f"https://poe.ninja/poe2/builds?league={league}",
        }
    else:
        base = results[0]
        # 若有 dps 類型的資料，補充 exp 列表裡 dps=0 的角色
        if len(results) > 1:
            dps_map = {
                b["character"]: b["dps"]
                for b in results[1].get("top_builds", [])
                if b.get("character") and b.get("dps", 0) > 0
            }
            for b in base.get("top_builds", []):
                if b["character"] in dps_map and b["dps"] == 0:
                    b["dps"] = dps_map[b["character"]]
        result = {
            **base,
            "status": "ok" if not errors else "partial",
            "errors": errors,
            "league": league,
            "fetched_at": time.time(),
            "ninja_overview_url": f"https://poe.ninja/poe2/builds?league={league}",
        }

    _save_cache(cache_key, result)
    return result


def _parse_meta_builds(raw: dict, league: str, btype: str) -> dict:
    headers = raw.get("headers", [])
    rows    = raw.get("data", [])
    total   = len(rows)

    def _col(name: str) -> int:
        try: return headers.index(name)
        except ValueError: return -1

    rank_idx   = _col("Rank")
    acct_idx   = _col("Account")
    char_idx   = _col("Character")
    class_idx  = _col("Class")
    asc_idx    = _col("Ascendancy")
    level_idx  = _col("Level")
    life_idx   = _col("Life")
    es_idx     = _col("EnergyShield")
    skills_idx = _col("ActiveSkills")
    dps_idx    = -1
    for alt in ("DPS", "TotalDPS", "Dps", "DamageDPS", "CombinedDPS"):
        dps_idx = _col(alt)
        if dps_idx >= 0:
            break

    skill_counts: dict[str, int] = {}
    asc_counts:   dict[str, int] = {}
    top_builds:   list[dict]     = []

    for row in rows[:150]:
        if not isinstance(row, list):
            continue

        def _v(idx, default=None):
            return row[idx] if 0 <= idx < len(row) else default

        account   = str(_v(acct_idx) or "")
        character = str(_v(char_idx) or "")
        cls       = str(_v(class_idx) or "")
        asc       = str(_v(asc_idx) or "")
        level     = int(_v(level_idx) or 0)
        life      = int(_v(life_idx) or 0)
        es        = int(_v(es_idx) or 0)
        rank      = int(_v(rank_idx) or 0)
        dps_raw   = _v(dps_idx, 0) or 0
        dps_m     = round(float(dps_raw) / 1_000_000, 2) if dps_raw else 0

        skills_raw = _v(skills_idx, [])
        skills: list[str] = []
        if isinstance(skills_raw, list):
            for s in skills_raw:
                name = ""
                if isinstance(s, dict):
                    name = s.get("name") or s.get("id") or ""
                elif isinstance(s, str):
                    name = s
                if name:
                    skills.append(name)
                    skill_counts[name] = skill_counts.get(name, 0) + 1
        elif isinstance(skills_raw, str) and skills_raw:
            skills.append(skills_raw)
            skill_counts[skills_raw] = skill_counts.get(skills_raw, 0) + 1

        if asc:
            asc_counts[asc] = asc_counts.get(asc, 0) + 1

        ninja_url = ""
        if account and character:
            ninja_url = (
                f"https://poe.ninja/poe2/builds/{account}/{character}"
                f"?league={league}"
            )

        top_builds.append({
            "rank":       rank or len(top_builds) + 1,
            "account":    account,
            "character":  character,
            "cls":        cls,
            "ascendancy": asc,
            "level":      level,
            "life":       life,
            "es":         es,
            "dps":        dps_m,
            "skills":     skills[:5],
            "ninja_url":  ninja_url,
        })

    skill_stats = sorted(
        [{"name": k, "count": v, "pct": round(v / max(total, 1) * 100, 1)}
         for k, v in skill_counts.items()],
        key=lambda x: x["count"], reverse=True
    )[:20]

    asc_stats = sorted(
        [{"name": k, "count": v, "pct": round(v / max(total, 1) * 100, 1)}
         for k, v in asc_counts.items()],
        key=lambda x: x["count"], reverse=True
    )

    return {
        "top_builds": top_builds,
        "skill_stats": skill_stats,
        "asc_stats": asc_stats,
        "total_characters": total,
    }


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
