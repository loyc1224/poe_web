# ── 聯盟設定 ─────────────────────────────────────────────────────────────────
# POE2 當前開季聯盟（2026-05）- poe.ninja API 使用小寫 slug
LEAGUE_NAME = "runesofaldur"  # Runes of Aldur

# 目前仍在進行中的聯盟（0.5 開季前的聯盟），用於「現有聯盟物價表」分頁
# 注意：API 使用大寫開頭的聯盟名稱
CURRENT_LEAGUE_NAME = "Standard"  # Standard（大寫）

# ── poe.ninja Economy 類型 ────────────────────────────────────────────────────
ECONOMY_TYPES = [
    # poe.ninja PoE2 Currency Exchange API — type 對應路徑
    # 格式：(type_param, 顯示標籤)
    ("Currency",  "通貨"),
    ("Delirium",  "狂亂物品"),
]

# poe.ninja PoE2 可用聯盟 slug（網址中的 league 名稱）
# Active: Runes of Aldur (2026-05)
# Previous: Fate of the Vaal (vaal), HC Fate of the Vaal (vaalhc)
POE2_LEAGUES = [
    ("Runes of Aldur",     "runesofaldur"),
    ("HC Runes of Aldur",  "runesofaldurhc"),
    ("Standard",           "standard"),
    ("Hardcore",           "hardcore"),
    ("Fate of the Vaal",   "vaal"),
    ("HC Fate of the Vaal", "vaalhc"),
]

# ── PoE1 設定 ─────────────────────────────────────────────────────────────────
POE1_LEAGUE   = "Mirage"    # 目前 PoE1 聯盟（2026-05）
POE1_STANDARD = "Standard"  # PoE1 Standard 聯盟

# PoE1 economy 類型（格式：(type_param, 標籤)，皆用 exchange API）
POE1_ECONOMY_TYPES = [
    ("Currency",      "通貨"),
    ("Fragment",      "碎片"),
    ("Scarab",        "聖甲蟲"),
    ("Essence",       "精華"),
    ("DivinationCard","命運卡"),
    ("Oil",           "油"),
]

# ── 快取 TTL（秒）─────────────────────────────────────────────────────────────
CACHE_TTL = {
    "economy": 1800,  # 30 分鐘
}
