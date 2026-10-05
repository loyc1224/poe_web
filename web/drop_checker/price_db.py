"""
PoE2 物價與名稱字典管理模組
支援從 poe.ninja 抓取最新價格，以及載入本地快取與中英文對照。
"""
import json
import logging
import difflib
from pathlib import Path
import requests

logger = logging.getLogger(__name__)

CACHE_DIR = Path(__file__).resolve().parent.parent / "cache"

# 常見 POE2 中英文對照與別名字典
DICTIONARY_ZH_EN = {
    # 通貨 (Currency)
    "神聖石": "Divine Orb",
    "崇高石": "Exalted Orb",
    "混沌石": "Chaos Orb",
    "點金石": "Orb of Alchemy",
    "鍊金石": "Orb of Alchemy",
    "富豪石": "Regal Orb",
    "帝王石": "Regal Orb",
    "瓦爾石": "Vaal Orb",
    "機會石": "Orb of Chance",
    "廢除石": "Orb of Annulment",
    "卡蘭德鏡": "Mirror of Kalandra",
    "鏡子": "Mirror of Kalandra",
    "希內科拉之鎖": "Hinekora's Lock",
    "鎖": "Hinekora's Lock",
    "磨石": "Blacksmith's Whetstone",
    "鍛造磨石": "Blacksmith's Whetstone",
    "鎧甲碎片": "Armourer's Scrap",
    "護甲片": "Armourer's Scrap",
    "玻璃球": "Glassblower's Bauble",
    "智識捲軸": "Scroll of Wisdom",
    "鑑定捲軸": "Scroll of Wisdom",
    "幻變石": "Orb of Transmutation",
    "強化石": "Orb of Augmentation",
    "工匠石": "Artificer's Orb",
    "裂化石": "Fracturing Orb",
    "寶石匠的稜鏡": "Gemcutter's Prism",
    "寶石匠稜鏡": "Gemcutter's Prism",
    "增幅石": "Orb of Augmentation",
    "蛻變石": "Orb of Transmutation",
    "重鑄石": "Orb of Scouring",
    "祝福石": "Blessed Orb",
    "神品石": "Divine Orb",

    # 完美 / 大系列
    "完美崇高石": "Perfect Exalted Orb",
    "完美混沌石": "Perfect Chaos Orb",
    "完美帝王石": "Perfect Regal Orb",
    "完美富豪石": "Perfect Regal Orb",
    "完美珠寶師石": "Perfect Jeweller's Orb",
    "大崇高石": "Greater Exalted Orb",
    "大混沌石": "Greater Chaos Orb",
    "大帝王石": "Greater Regal Orb",
    "大富豪石": "Greater Regal Orb",

    # 預兆 / 改善之兆 (Omen)
    "改善之兆": "Omen of Amelioration",
    "洗鍊之兆": "Omen of Whittling",
    "機會之兆": "Omen of Chance",
    "光明之兆": "Omen of Light",
    "滅絕之兆": "Omen of Annulment",

    # 精華 (Essence) & 符文 (Rune)
    "活力符文": "Rune of Vitality",
    "冰川符文": "Glacial Rune",
    "終點符文": "Rune of Culmination",
    "爆裂符文": "Rune of the Blossom",
}

class PriceDatabase:
    def __init__(self, league: str = "Standard"):
        self.league = league
        self.item_prices: dict[str, dict] = {}  # {canonical_name_lowercase: {name, zh, chaos, divine}}
        self.name_map: dict[str, str] = {}       # {zh_or_alias_lowercase: canonical_name_lowercase}
        self.load_database()

    def load_database(self):
        """讀取本地快取並向 poe.ninja 更新。"""
        self.item_prices.clear()
        self.name_map.clear()

        # 預載預設字典 mapping
        for zh, en in DICTIONARY_ZH_EN.items():
            en_lower = en.lower()
            zh_lower = zh.lower()
            self.name_map[zh_lower] = en_lower
            self.name_map[en_lower] = en_lower

        # 讀取本地快取檔案
        for cache_name in [f"economy_{self.league}.json", "economy_runesofaldur.json", "economy_Standard.json"]:
            path = CACHE_DIR / cache_name
            if path.exists():
                try:
                    data = json.loads(path.read_text(encoding="utf-8"))
                    items = data.get("items", [])
                    for item in items:
                        name = item.get("name", "")
                        zh = item.get("zh", "")
                        chaos = item.get("chaos", 0.0) or 0.0
                        unit = item.get("unit", "chaos")

                        if not name:
                            continue

                        en_lower = name.lower()
                        self.item_prices[en_lower] = {
                            "name": name,
                            "zh": zh,
                            "chaos": round(chaos, 2),
                            "unit": unit
                        }
                        self.name_map[en_lower] = en_lower
                        if zh:
                            self.name_map[zh.lower()] = en_lower
                except Exception as e:
                    logger.warning(f"讀取快取 {path} 失敗: {e}")

        # 手動加補常見熱門與基礎通貨預設價格 (若 poe.ninja 未回傳)
        defaults = {
            "Regal Orb": {"name": "Regal Orb", "zh": "富豪石", "chaos": 0.01, "unit": "divine"},
            "Orb of Scouring": {"name": "Orb of Scouring", "zh": "重鑄石", "chaos": 0.02, "unit": "divine"},
            "Orb of Alchemy": {"name": "Orb of Alchemy", "zh": "點金石", "chaos": 0.01, "unit": "divine"},
            "Chaos Orb": {"name": "Chaos Orb", "zh": "混沌石", "chaos": 0.005, "unit": "divine"},
            "Divine Orb": {"name": "Divine Orb", "zh": "神聖石", "chaos": 1.0, "unit": "divine"},
            "Exalted Orb": {"name": "Exalted Orb", "zh": "崇高石", "chaos": 0.01, "unit": "divine"},
            "Vaal Orb": {"name": "Vaal Orb", "zh": "瓦爾石", "chaos": 0.02, "unit": "divine"},
            "Orb of Chance": {"name": "Orb of Chance", "zh": "機會石", "chaos": 0.01, "unit": "divine"},
            "Orb of Annulment": {"name": "Orb of Annulment", "zh": "廢除石", "chaos": 0.15, "unit": "divine"},
            "Omen of Amelioration": {"name": "Omen of Amelioration", "zh": "改善之兆", "chaos": 15.0, "unit": "divine"},
        }
        for en, info in defaults.items():
            en_lower = en.lower()
            if en_lower not in self.item_prices:
                self.item_prices[en_lower] = info
            if info["zh"]:
                self.name_map[info["zh"].lower()] = en_lower

    def get_price(self, query: str) -> dict | None:
        """根據搜尋詞（中文、英文、別名）查詢價格，支援模糊匹配。"""
        if not query:
            return None

        q_lower = query.strip().lower()

        # 1. 精確匹配
        canonical = self.name_map.get(q_lower)
        if canonical and canonical in self.item_prices:
            return self.item_prices[canonical]

        # 2. 部分子字串匹配 (Substring Match)
        for key, canonical_key in self.name_map.items():
            if len(q_lower) >= 2 and (q_lower in key or key in q_lower):
                if canonical_key in self.item_prices:
                    return self.item_prices[canonical_key]

        # 3. 模糊匹配 (Fuzzy Match / Levenshtein Distance)
        all_keys = list(self.name_map.keys())
        matches = difflib.get_close_matches(q_lower, all_keys, n=1, cutoff=0.5)
        if matches:
            matched_key = matches[0]
            canonical_key = self.name_map[matched_key]
            if canonical_key in self.item_prices:
                return self.item_prices[canonical_key]

        return None
