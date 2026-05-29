"""
Reddit 公開 JSON API 爬取模組。
不需要 OAuth，使用 User-Agent 標識自己，並加入適當的 rate-limit 保護。
"""
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests

from .config import BEAST_TARGETS, CACHE_TTL, REDDIT_QUERIES

CACHE_DIR = Path(__file__).resolve().parent.parent / "cache"
CACHE_DIR.mkdir(exist_ok=True)

_HEADERS = {
    "User-Agent": "poe-monitor/1.0 (+personal project)",
    "Accept": "application/json",
}

# 建立關鍵字 → beast_id 的查找表
_KW_TO_BEAST: dict[str, str] = {
    kw: b["id"]
    for b in BEAST_TARGETS
    for kw in b["keywords"]
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


# ── 標記函式 ─────────────────────────────────────────────────────────────────

def _tag_post(text: str) -> list[str]:
    """找出貼文提及哪些神獸（回傳 beast_id 列表）。"""
    lower = text.lower()
    seen: set[str] = set()
    tags = []
    for kw, bid in _KW_TO_BEAST.items():
        if kw in lower and bid not in seen:
            seen.add(bid)
            tags.append(bid)
    return tags


# ── 主要抓取函式 ─────────────────────────────────────────────────────────────

def fetch_reddit(force: bool = False) -> dict:
    """搜尋 Reddit 討論，統計神獸提及次數與 Spirit Walker 熱度。"""
    cache_key = "reddit_combined"
    if not force:
        cached = _load_cache(cache_key, CACHE_TTL["reddit"])
        if cached:
            return cached

    seen_ids: set[str] = set()
    posts: list[dict] = []
    beast_counts: dict[str, int] = {b["id"]: 0 for b in BEAST_TARGETS}
    sw_mentions = 0
    errors: list[str] = []

    def _query_one(subreddit: str, query: str):
        resp = requests.get(
            f"https://www.reddit.com/r/{subreddit}/search.json",
            params={"q": query, "sort": "new", "limit": 15, "restrict_sr": 1, "t": "week"},
            headers=_HEADERS,
            timeout=5,
        )
        if resp.status_code == 429:
            return [], f"r/{subreddit}: rate limited"
        resp.raise_for_status()
        return resp.json().get("data", {}).get("children", []), None

    with ThreadPoolExecutor(max_workers=len(REDDIT_QUERIES)) as pool:
        futures = {
            pool.submit(_query_one, sr, q): (sr, q)
            for sr, q in REDDIT_QUERIES
        }
        for fut in as_completed(futures, timeout=6):
            sr, q = futures[fut]
            try:
                children, err = fut.result()
                if err:
                    errors.append(err)
                    continue
                for child in children:
                    p = child.get("data", {})
                    pid = p.get("id", "")
                    if not pid or pid in seen_ids:
                        continue
                    seen_ids.add(pid)
                    title = p.get("title", "")
                    body  = p.get("selftext", "")
                    full  = f"{title} {body}".lower()
                    if any(v in full for v in ("spirit walker", "spiritwalker", "tame beast")):
                        sw_mentions += 1
                    tags = _tag_post(full)
                    for t in tags:
                        beast_counts[t] += 1
                    posts.append({
                        "id":           pid,
                        "title":        title,
                        "subreddit":    p.get("subreddit", sr),
                        "url":          f"https://reddit.com{p.get('permalink', '')}",
                        "score":        p.get("score", 0),
                        "num_comments": p.get("num_comments", 0),
                        "created_utc":  p.get("created_utc", 0),
                        "tags":         tags,
                    })
            except Exception as exc:
                errors.append(f"r/{sr} '{q}': {exc}")

    # 依 score 降冪，取前 30
    posts.sort(key=lambda x: x["score"], reverse=True)

    result = {
        "posts":               posts[:30],
        "beast_mention_counts": beast_counts,
        "spirit_walker_mentions": sw_mentions,
        "fetched_at":          time.time(),
        "status":              "ok" if not errors else ("partial" if posts else "error"),
        "errors":              errors,
    }
    _save_cache(cache_key, result)
    return result
