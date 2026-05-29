# ── 聯盟設定 ─────────────────────────────────────────────────────────────────
# 0.5 正式上線後，把 LEAGUE_NAME 改成實際聯盟名稱（例如 "Dawn" 或 GGG 公告的名字）
LEAGUE_NAME = "Dawn"

# 目前仍在進行中的聯盟（0.5 開季前的聯盟），用於「現有聯盟物價表」分頁
# poe.ninja PoE2 可用聯盟：Standard、Mercenaries 等
CURRENT_LEAGUE_NAME = "Standard"

# ── Spirit Walker 抓寵目標 ────────────────────────────────────────────────────
BEAST_TARGETS = [
    {
        "id": "silverfist",
        "zh": "銀拳",
        "en": "Mighty Silverfist",
        "location": "Act 3，叢林遺跡",
        "priority": "高",
        "stage": "前期",
        "stage_order": 1,
        "keywords": ["silverfist", "mighty silverfist"],
        "description": "白毛大猩猩，官方展示 Spirit Walker 時用來示範抓寵，最早可抓到的強力寵物。",
    },
    {
        "id": "yama",
        "zh": "白色山魔",
        "en": "Yama the White",
        "location": "Act 4，Halls of the Dead",
        "priority": "中高",
        "stage": "前期",
        "stage_order": 2,
        "keywords": ["yama", "yama the white"],
        "description": "白毛猴王，會衝鋒，前期過渡寵，比銀拳晚遇到。",
    },
    {
        "id": "scourge",
        "zh": "天空災厄",
        "en": "Scourge of the Skies",
        "location": "Act 4，Shrike Island",
        "priority": "高",
        "stage": "中期",
        "stage_order": 3,
        "keywords": ["scourge of the skies", "scourge skies"],
        "description": "大型鳥王，風暴/龍捲風技能，理論清圖能力強，Act 4 後換寵重點。",
    },
    {
        "id": "chetza",
        "zh": "切特札",
        "en": "Chetza, the Feathered Plague",
        "location": "Trial of Chaos 第 4 層",
        "priority": "極高",
        "stage": "試煉",
        "stage_order": 4,
        "keywords": ["chetza", "feathered plague"],
        "description": "黑色瘟疫鳥，身上多紅眼睛，龍捲風技能，開季第一波熱門神獸最強候選。",
    },
    {
        "id": "bahlak",
        "zh": "巴拉克",
        "en": "Bahlak, the Sky Seer",
        "location": "Trial of Chaos 第 4 層",
        "priority": "中高",
        "stage": "試煉",
        "stage_order": 5,
        "keywords": ["bahlak", "sky seer"],
        "description": "貓頭鷹風格，風暴系技能多，切特札替代方案，需實測 AI 穩定性。",
    },
    {
        "id": "morvak",
        "zh": "莫瓦克",
        "en": "Morvak, the Infernal",
        "location": "Endgame 地圖 Boss",
        "priority": "高",
        "stage": "後期",
        "stage_order": 6,
        "keywords": ["morvak", "infernal morvak"],
        "description": "高血量高傷倍，偏打王型，Endgame 後期打王寵物主力。",
    },
]

# ── Reddit 搜尋設定 ────────────────────────────────────────────────────────────
# 每次只取最重要的幾組，減少 rate-limit 壓力
REDDIT_QUERIES = [
    ("pathofexile2", "spirit walker tame beast"),
    ("pathofexile2", "chetza bahlak silverfist scourge morvak"),
    ("pathofexile", "poe2 spirit walker companion beast"),
]

# ── poe.ninja Economy 監控品項 ────────────────────────────────────────────────
ECONOMY_TYPES = [
    # poe.ninja PoE2 Currency Exchange API — type 對應路徑
    # 格式：(type_param, 顯示標籤)
    ("Currency",  "通貨"),
    ("Delirium",  "狂亂物品"),
]

# poe.ninja PoE2 可用聯盟 slug（網址中的 league 名稱）
# Active: Standard, Hardcore
# Previous: Fate of the Vaal (vaal), HC Fate of the Vaal (vaalhc)
POE2_LEAGUES = [
    ("Standard",        "Standard"),
    ("Hardcore",        "Hardcore"),
    ("Fate of the Vaal", "vaal"),
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
    "builds":  900,   # 15 分鐘
    "economy": 1800,  # 30 分鐘
    "reddit":  300,   # 5 分鐘
}
