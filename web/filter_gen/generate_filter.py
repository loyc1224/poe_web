"""
POE2 即時經濟篩選器產生器。

用法（在 web/ 目錄下執行）：
    python -m filter_gen.generate_filter --league runesofaldur

只會在本機產生一份 .filter 純文字檔（web/filter_gen/output/），
不會建立任何網站頁面、不會被 Flask 路由到。
產生後把檔案內容貼到 pathofexile.tw 的 item-filters 頁面，
或直接複製到遊戲的篩選器資料夾使用。
"""
import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))  # 讓 `monitor` package 可被匯入

from monitor.config import LEAGUE_NAME  # noqa: E402
from monitor.ninja_client import fetch_economy  # noqa: E402

OUTPUT_DIR = Path(__file__).resolve().parent / "output"
TW_OVERRIDE_PATH = Path(__file__).resolve().parent / "tw_price_overrides.json"

# 遊戲透過「線上物品篩選器」訂閱同步下來的檔案，會被伺服器版本定期覆蓋，不能直接編輯
DEFAULT_BASE_FILTER = Path.home() / "Documents" / "My Games" / "Path of Exile 2" / "OnlineFilters" / "EQK0PTj"
# 合併後輸出到遊戲資料夾最上層（非 OnlineFilters），不受線上同步影響，可直接在遊戲內選用
DEFAULT_MERGED_OUTPUT = Path.home() / "Documents" / "My Games" / "Path of Exile 2" / "PoE2_LiveEconomy.filter"

MERGE_MARKER_START = "#===== [自動產生] 即時經濟通貨分級 開始 - 由 generate_filter.py 插入 ====="
MERGE_MARKER_END = "#===== [自動產生] 即時經濟通貨分級 結束 ====="


def load_tw_overrides() -> dict[str, float]:
    """讀取手動填寫的台服校正價（去掉 `_` 開頭的說明/範例欄位）。"""
    if not TW_OVERRIDE_PATH.exists():
        return {}
    raw = json.loads(TW_OVERRIDE_PATH.read_text(encoding="utf-8"))
    return {k: float(v) for k, v in raw.items() if not k.startswith("_")}

# 通貨等級門檻（單位：神聖石 divine）。由高到低比對，符合第一個就歸入該級。
TIERS = [
    # (最低神聖石價值, 標籤, 字級, 文字顏色,     邊框顏色,      背景顏色,        提示音,              地圖圖示,                     光柱效果 Beam)
    (20,   "S 神話級",  45, "255 255 255 255", "255 0 0 255", "0 0 0 255",     "PlayAlertSound 6 300", "MinimapIcon 0 Red Star",    "PlayEffect Red"),
    (5,    "A 極稀有",  42, "0 0 0 255",       "255 128 0 255", "255 200 0 255", "PlayAlertSound 3 300", "MinimapIcon 0 Yellow Star", "PlayEffect Yellow"),
    (1,    "B 稀有",    40, "0 0 0 255",       "0 200 255 255", "150 220 255 255", "PlayAlertSound 2 300", "MinimapIcon 1 Blue Diamond", "PlayEffect Blue Temp"),
    (0.2,  "C 有價值",  36, "0 0 0 255",       "0 170 0 255",   "200 255 200 255", "PlayAlertSound 1 200", "MinimapIcon 2 White Circle", None),
    (0.03, "D 一般",    32, "255 255 255 255", "120 120 120 200", "40 40 40 200", None,                   None,                         None),
]
# S/A 用永久光柱（沒有 Temp，會一直亮到你撿起來），B 用短暫光柱避免畫面太亂
# 低於最後一個門檻的通貨，仍然顯示但字最小、無音效（避免直接消失看不到雜項通貨）。
FALLBACK_FONT_SIZE = 18

CURRENCY_TYPES = {"Currency", "Delirium"}


def build_tier_blocks(items: list[dict], min_divine: float, tw_overrides: dict[str, float]) -> str:
    """依即時神聖石價值，把通貨切成幾個等級的 Show 區塊。"""
    buckets: dict[str, list[str]] = {label: [] for _, label, *_ in TIERS}
    fallback: list[str] = []

    for item in items:
        if item.get("type") not in CURRENCY_TYPES:
            continue
        name = item.get("name")
        if not name:
            continue
        if name in tw_overrides:  # 有手動填台服校正價就優先用，不用 poe.ninja 國際服估價
            value = tw_overrides[name]
        else:
            value = item.get("chaos", 0) or 0
            if item.get("unit") == "chaos":  # 極少數用混沌石計價，換算成約略神聖石值
                value = value / 200
        if value < min_divine:
            continue
        placed = False
        for threshold, label, *_ in TIERS:
            if value >= threshold:
                buckets[label].append(name)
                placed = True
                break
        if not placed:
            fallback.append(name)

    lines = ["#===== 即時經濟通貨分級（依 poe.ninja 神聖石價格自動產生）====="]
    for threshold, label, font, text_c, border_c, bg_c, sound, minimap, effect in TIERS:
        names = buckets[label]
        if not names:
            continue
        name_list = " ".join(f'"{n}"' for n in names)
        lines.append(f"Show # 通貨 - {label}（>= {threshold} divine）")
        lines.append('\tClass == "Stackable Currency"')
        lines.append(f"\tBaseType == {name_list}")
        lines.append(f"\tSetFontSize {font}")
        lines.append(f"\tSetTextColor {text_c}")
        lines.append(f"\tSetBorderColor {border_c}")
        lines.append(f"\tSetBackgroundColor {bg_c}")
        if effect:
            lines.append(f"\t{effect}")
        if sound:
            lines.append(f"\t{sound}")
        if minimap:
            lines.append(f"\t{minimap}")
        lines.append("")

    if fallback:
        name_list = " ".join(f'"{n}"' for n in fallback)
        lines.append("Show # 通貨 - 其餘（低價值，僅縮小顯示，不隱藏）")
        lines.append('\tClass == "Stackable Currency"')
        lines.append(f"\tBaseType == {name_list}")
        lines.append(f"\tSetFontSize {FALLBACK_FONT_SIZE}")
        lines.append("\tSetTextColor 200 200 200 255")
        lines.append("\tSetBorderColor 100 100 100 150")
        lines.append("")

    return "\n".join(lines)


BASELINE_RULES = """
#===== 基礎規則（簡化版，只為了讓其他物品也看得到，可自行換成完整版 NeverSink 骨架）=====

# 傳說（唯一）裝備 - 一律顯示，最醒目
Show # 傳說裝備
	Rarity Unique
	SetFontSize 45
	SetTextColor 175 96 37 255
	SetBorderColor 175 96 37 255
	SetBackgroundColor 60 30 0 255
	PlayAlertSound 3 300
	MinimapIcon 0 Yellow Star

# 稀有裝備 - 依地圖等級顯示，中高亮度
Show # 稀有裝備
	Rarity Rare
	AreaLevel >= 55
	SetFontSize 38
	SetTextColor 255 255 0 255
	SetBorderColor 255 255 0 255
	MinimapIcon 1 Yellow Diamond

Show # 稀有裝備（低階，字縮小）
	Rarity Rare
	SetFontSize 24
	SetTextColor 255 255 0 200
	SetBorderColor 255 255 0 120

# 命運卡
Show # 命運卡
	Class == "Divination Cards"
	SetFontSize 40
	SetTextColor 0 0 0 255
	SetBackgroundColor 0 240 190 255
	PlayAlertSound 2 300
	MinimapIcon 1 Yellow Triangle

# 符文 / 靈魂核心
Show # 符文與靈魂核心
	Class == "Runes" "Soul Cores"
	SetFontSize 38
	SetTextColor 255 255 255 255
	SetBorderColor 0 240 190 255
	MinimapIcon 1 Blue Circle

# 高階石板（Waystone）
Show # 高階石板
	Class == "Waystones"
	WaystoneTier >= 11
	SetFontSize 40
	SetTextColor 255 255 255 255
	SetBorderColor 255 0 0 255
	MinimapIcon 0 Red Square

Show # 一般石板
	Class == "Waystones"
	SetFontSize 30
	SetTextColor 200 200 200 255
	SetBorderColor 120 120 120 200

# 護符
Show # 護符
	Class == "Charms"
	SetFontSize 32
	SetTextColor 200 240 255 255
	SetBorderColor 0 170 255 255

# 技能寶石 / 未切割寶石
Show # 寶石
	Class == "Skill Gems" "Uncut Skill Gems" "Uncut Spirit Gems"
	SetFontSize 38
	SetTextColor 30 190 190 255
	SetBorderColor 40 130 130 255
	MinimapIcon 1 Green Triangle

# 保底規則：任何沒被上面規則接住的東西一律顯示（絕不隱藏未知物品，避免漏看新物品）
Show # 保底顯示 - 未知/其餘物品
	SetFontSize 32
"""


def merge_into_base(base_text: str, tier_section: str) -> str:
    """把即時經濟區塊插入完整版篩選器的最前面（第一條 Show/Hide 規則之前）。

    PoE 篩選器由上而下比對，第一個符合的規則生效，所以放最前面才會蓋過
    base 檔裡原本針對通貨的規則，其餘規則（裝備/地圖/寶石...）維持原樣。
    """
    lines = base_text.splitlines()
    insert_at = len(lines)
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("Show") or stripped.startswith("Hide"):
            insert_at = i
            break
    block = [MERGE_MARKER_START, *tier_section.splitlines(), MERGE_MARKER_END, ""]
    merged = lines[:insert_at] + block + lines[insert_at:]
    return "\n".join(merged)


def generate(league: str, force: bool, min_divine: float, base_filter, output) -> Path:
    econ = fetch_economy(league=league, force=force)
    items = econ.get("items", [])
    tw_overrides = load_tw_overrides()

    note = f"""# ===============================================================
# POE2 即時經濟區塊 - 由 generate_filter.py 自動產生並插入
# 聯盟：{league}
# 資料時間：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(econ.get('fetched_at', time.time())))}
# 資料來源：poe.ninja 國際服估價（僅供相對貴賤參考，非台服官方成交價！）
#           pathofexile.tw 為官方獨立台服經濟圈，poe.ninja 沒有台服數據。
#           已手動校正 {len(tw_overrides)} 項通貨（見 tw_price_overrides.json），
#           其餘項目仍是國際服估價，請自行斟酌。
# 狀態：{econ.get('status')}  已抓取物品數：{len(items)}
# 重新產生：cd web && python -m filter_gen.generate_filter --force
# ===============================================================
"""
    tier_section = note + "\n" + build_tier_blocks(items, min_divine, tw_overrides)

    if base_filter and base_filter.exists():
        base_text = base_filter.read_text(encoding="utf-8")
        content = merge_into_base(base_text, tier_section)
        out_path = output or DEFAULT_MERGED_OUTPUT
    else:
        content = tier_section + "\n" + BASELINE_RULES
        out_path = output or (OUTPUT_DIR / "PoE2_LiveEconomy.filter")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(content, encoding="utf-8")
    return out_path


def main():
    parser = argparse.ArgumentParser(description="產生 POE2 即時經濟篩選器")
    parser.add_argument("--league", default=LEAGUE_NAME, help="poe.ninja 聯盟 slug，如 runesofaldur / standard")
    parser.add_argument("--force", action="store_true", help="忽略快取，強制重新抓取 poe.ninja 最新價格")
    parser.add_argument("--min-divine", type=float, default=0.0, help="低於此神聖石價值的通貨直接不列入分級（仍會落入保底規則）")
    parser.add_argument("--base-filter", type=Path, default=None, help="要合併的完整版篩選器路徑（預設抓 OnlineFilters 下載的那份，若存在）")
    parser.add_argument("--no-base", action="store_true", help="不合併任何完整版，只輸出簡化版基礎規則")
    parser.add_argument("--output", type=Path, default=None, help="輸出檔案路徑（預設寫到遊戲資料夾最上層，不會被線上同步覆蓋）")
    args = parser.parse_args()

    base_filter = None if args.no_base else (args.base_filter or DEFAULT_BASE_FILTER)
    out_path = generate(args.league, args.force, args.min_divine, base_filter, args.output)
    print(f"已產生：{out_path}")
    if base_filter and base_filter.exists() and not args.no_base:
        print(f"（已以完整版篩選器為骨架合併：{base_filter}）")
        print("這是獨立本機檔案，不在 OnlineFilters 資料夾內，不會被線上同步覆蓋。")
    print("遊戲內：Options -> UI -> Item Filter -> 選這個檔案即可。")


if __name__ == "__main__":
    main()
