"""
分析引擎：整合 poe.ninja builds、economy、Reddit 三路訊號，
產生「現在該抓哪隻王」與「該買/賣/囤什麼」的建議。
"""
import time
from typing import Any

from .config import BEAST_TARGETS


# ── 優先度數值化 ─────────────────────────────────────────────────────────────
_PRIORITY_SCORE = {"極高": 4, "高": 3, "中高": 2, "中": 1}


def generate_recommendations(builds: dict, economy: dict, reddit: dict) -> dict:
    """
    回傳結構：
    {
        "hunt_order":   [{beast + score + signals}],   # 依熱度排序的抓寵順序
        "buy_watch":    [{name, chaos, change_1d, ...}],
        "sell_watch":   [{name, chaos, change_1d, ...}],
        "alerts":       [{type, msg}],
        "generated_at": float,
    }
    """
    recs: dict[str, Any] = {
        "hunt_order":   [],
        "buy_watch":    [],
        "sell_watch":   [],
        "alerts":       [],
        "generated_at": time.time(),
    }

    # ── 神獸熱度計算 ─────────────────────────────────────────────────────────
    build_counts  = builds.get("companion_counts", {})
    reddit_counts = reddit.get("beast_mention_counts", {})

    scored: list[dict] = []
    for beast in BEAST_TARGETS:
        bid = beast["id"]
        build_n  = build_counts.get(bid, 0)
        reddit_n = reddit_counts.get(bid, 0)
        base     = _PRIORITY_SCORE.get(beast["priority"], 1)

        # 權重：poe.ninja build 資料最可靠，reddit 討論為早期訊號
        score = base * 10 + build_n * 8 + reddit_n * 3

        scored.append({
            **beast,
            "score":        score,
            "build_count":  build_n,
            "reddit_count": reddit_n,
            "signal":       _signal_label(build_n, reddit_n),
        })

    scored.sort(key=lambda x: x["score"], reverse=True)
    recs["hunt_order"] = scored

    # ── 物品買入 / 賣出觀察 ─────────────────────────────────────────────────
    items = economy.get("items", [])
    recs["buy_watch"]  = [i for i in items if i.get("change_1d", 0) >= 5  and i.get("volume", 0) >= 3][:10]
    recs["sell_watch"] = sorted(
        [i for i in items if i.get("change_1d", 0) <= -5 and i.get("volume", 0) >= 3],
        key=lambda x: x["change_1d"]
    )[:10]

    # ── 警示訊息 ────────────────────────────────────────────────────────────
    if builds.get("status") in ("unavailable", "error"):
        recs["alerts"].append({
            "type": "warning",
            "msg":  f"poe.ninja Builds 暫無資料（{builds.get('error', '未知')}）。聯盟可能尚未開始。",
        })

    if economy.get("status") in ("unavailable", "error"):
        recs["alerts"].append({
            "type": "warning",
            "msg":  "poe.ninja Economy 暫無資料。聯盟開始後自動更新。",
        })
    elif economy.get("status") == "partial":
        recs["alerts"].append({
            "type": "info",
            "msg":  f"部分物品類型取得失敗：{', '.join(economy.get('errors', [])[:2])}",
        })

    sw_count = builds.get("spirit_walker_count", 0)
    if sw_count > 50:
        recs["alerts"].append({
            "type": "success",
            "msg":  f"偵測到 {sw_count:,} 個 Spirit Walker 角色！開季熱度已起飛。",
        })

    reddit_sw = reddit.get("spirit_walker_mentions", 0)
    if reddit_sw > 20:
        recs["alerts"].append({
            "type": "info",
            "msg":  f"Reddit 本週 {reddit_sw} 則 Spirit Walker 相關討論，社群熱度上升中。",
        })

    return recs


def _signal_label(build_count: int, reddit_count: int) -> str:
    total = build_count * 2 + reddit_count
    if total >= 20:
        return "🔥 爆熱"
    if total >= 8:
        return "📈 上漲"
    if total >= 2:
        return "👀 觀察"
    return "⏳ 等待資料"
