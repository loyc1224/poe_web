# POE2 即時經濟物品篩選器產生器

## 這是做什麼的？

用你網站已經在抓的 poe.ninja 經濟資料（`web/cache/economy_*.json`），
自動產生一份「官方支援」的 `.filter` 篩選器檔案。

- 通貨（Currency / Delirium 等）會依照**目前真實神聖石價格**分成幾個等級，
  越貴的顏色越亮、字越大、有提示音、地圖圖示越明顯。
- 每次重新執行就會依照最新價格重新產生，等於「經濟驅動的篩選器」，
  跟 NeverSink 每 4 小時自動更新的原理一樣（只是我們是手動/排程觸發）。

## 為什麼安全，不會被鎖號？

`.filter` 純文字檔是遊戲客戶端官方支援的機制
（設定 → 介面 → 物品篩選器），只會改變**已經在地上的物品**的顏色、大小、
音效、地圖圖示，不會讀取遊戲記憶體、不會在畫面上疊加額外圖層，
跟你貼的截圖那種「即時浮動報價文字」是不同技術。

> 截圖那種效果通常是像 **Awakened PoE Trade** 那類工具，做法是玩家手動
> `Ctrl+C` 複製物品文字後去查官方交易 API，官方預設允許、目前沒有停權
> 案例。如果是「讀取遊戲記憶體、自動在畫面上疊字」的工具，官方明文禁止，
> 有機會被鎖號，不建議使用。

## 使用方式

```powershell
cd web
python -m filter_gen.generate_filter --league Standard --force
```

預設行為（推薦）：

- 會自動讀取你電腦上「線上物品篩選器」同步下來的完整版官方 NeverSink 篩選器
  （`%USERPROFILE%\Documents\My Games\Path of Exile 2\OnlineFilters\EQK0PTj`），
  在最前面插入一段即時經濟通貨分級，其餘裝備/地圖/寶石規則完全保留原樣。
- 輸出到 `%USERPROFILE%\Documents\My Games\Path of Exile 2\PoE2_LiveEconomy.filter`
  （注意：不在 `OnlineFilters` 資料夾內，所以不會被線上訂閱同步覆蓋掉）。
- 遊戲內 設定(Options) → UI → 物品篩選器(Item Filter) → 選 `PoE2_LiveEconomy`。

## 參數

- `--league`：對應 `web/monitor/config.py` 裡 `POE2_LEAGUES` 的 slug（例如 `runesofaldur`、`standard`）。
- `--force`：忽略快取，強制重新向 poe.ninja 要最新價格（預設會用現有快取，30 分鐘內有效）。
- `--min-divine`：最低顯示門檻（低於這個神聖石價值的雜物直接 Hide，預設 `0`，即全部顯示但字很小）。
- `--base-filter`：要合併的完整版篩選器路徑（預設是上面那份 OnlineFilters 同步檔）。
- `--no-base`：不合併任何完整版，只輸出簡化版基礎規則（舊行為，寫到 `filter_gen/output/`）。
- `--output`：自訂輸出路徑。

## 篩選器只能做「顏色分級」，不能顯示價格數字

`.filter` 語法只能控制顏色、字體大小、外框、提示音、地圖圖示，**沒辦法在物品上
顯示「0.79 神聖石」這種文字**。目前這個腳本能做到的是：越貴的通貨字越大、顏色
越亮、掉落有提示音/光柱，讓你一眼分辨貴賤，但看不到確切數字。

另外實測過，poe.ninja PoE2 的 economy API 目前**只有 `Currency` 和 `Delirium`
兩種類別有資料**（`Omen`、`Essence`、`Rune` 等查詢都回傳空值），所以本工具能
分級的範圍已經是目前資料源的上限，其餘品項（Omen、地圖、精華等）沿用原版
 NeverSink 篩選器內建的固定分級。

### 想要看到真正的價格數字：Awakened PoE Trade

若想要滑鼠移到物品上就查到實際估價數字，需要另外搭配官方允許、無停權案例的
免費工具 **Awakened PoE Trade**（下載：
https://snosme.github.io/awakened-poe-trade/download ）：

1. 安裝並啟動，遊戲內用「視窗全螢幕」或「無邊框視窗」模式（不能用獨佔全螢幕，
   否則疊加視窗無法顯示）。
2. 滑鼠移到物品上，按下預設快捷鍵（通常是 `Ctrl+D`），它會複製物品文字並自動
   查詢官方交易 API，跳出一個顯示估價的小視窗。
3. 這個做法只用複製貼上、查官方公開 API，不讀記憶體、不自動疊加畫面，是目前
   社群公認最安全的價格查詢方式。

## 之後可以怎麼擴充

- 排程（Windows 工作排程器）每 30 分鐘重新執行一次，自動覆蓋
  `PoE2_LiveEconomy.filter`，等於你自己的「迷你版 FilterBlade」。
- 若之後更新了線上篩選器（改了 hash），記得同步更新
  `generate_filter.py` 裡的 `DEFAULT_BASE_FILTER` 路徑，或改用
  `--base-filter` 參數指定新路徑。
