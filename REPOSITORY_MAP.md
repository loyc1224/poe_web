# 倉庫目錄與功能查找索引

依 [`PROJECT_RULES.md`](PROJECT_RULES.md) CORE-003／CORE-006 維護；此文件是導航索引，不是另一份核心規則。

## 目錄分類

```text
poe_web/
  PROJECT_RULES.md          核心規範與驗收要求
  AGENTS.md                Agent入口，引用核心規範
  ARCHITECTURE.md           架構圖、分層原因與可重用專案骨架
  REPOSITORY_MAP.md         目錄／功能查找索引
  .github/                 Copilot指示與CI／部署工作流程
  web/
    app.py                 Flask組裝、HTTP與授權協調
    README.md              專案入口與文件索引
    Dockerfile             正式runtime映像
    requirements*.txt      正式依賴與驗證依賴
    monitor/
      __init__.py          舊 economy 頂層匯入的相容出口
      economy/             poe.ninja economy 與共用聯盟設定／翻譯
        config.py
        ninja_client.py
        translations.py
      stash/               個人倉庫領域
        client.py          官方私人倉庫讀取
        pricer.py          資料集估值、選取與去重
        store.py           個人連線的加密SQLite／GCS
      tw_pricer/           台服行情資料集與官方名稱表
        tw_pricer_client.py 讀寫已發布資料集
        tw_pricer_source.py 上游更新與驗證發布
    templates/             index／pricer／stash頁面
    static/                公開圖片／前端資產，新功能按領域分類
    content/<game>/        人工遊戲文章，不放程式／帳號資料
    cache/                 產生的公共資料集；私有DB不追蹤
    tests/
      unit/                領域邏輯、資料契約與隔離儲存測試
      integration/         Flask路由及跨層功能測試
    docs/                   專用操作／功能文件
      STASH.md              倉庫API、估值、安全與OAuth接入
      VALIDATION.md         共用驗證程序／功能矩陣／缺陷紀錄
      SESSION_HANDOFF.md    延續作業摘要
    scripts/                執行、部署與資料更新CLI
      deploy.ps1            Windows部署與驗證閘門
      deploy.sh             既有Linux部署入口
      refresh_tw_currency.py 明確行情／metadata更新CLI
      setup_tw_currency_scheduler.ps1 排程設定CLI
      start_local.ps1       本機啟動CLI
      validate_site.py      桌機／手機瀏覽器驗證CLI
    drop_checker/          桌面OCR查價工具（獨立功能）
    filter_gen/            遊戲濾鏡產生器（獨立功能）
  joycon-setup/            獨立控制器設定，不混入網站
```

## 功能查找表

| 要找的功能 | 入口／模組 | 介面／資料 | 測試／操作文件 |
|---|---|---|---|
| 首頁與文章／策略密碼 | `web/app.py` 的 home／load_games／strategy API | `templates/index.html`、`content/poe1/`／`poe2/`；密碼為私有env／Secret | `tests/integration/test_site_features.py`、`docs/VALIDATION.md` |
| 台服行情、完整查價名稱 | `monitor/tw_pricer/tw_pricer_client.py`／`tw_pricer_source.py`、`scripts/refresh_tw_currency.py` | `templates/index.html`、`cache/tw_<kind>_<game>.json` | `tests/unit/test_tw_price_datasets.py`、`README.md`／`docs/VALIDATION.md` |
| 倉庫帳號連線與API | `web/app.py` 的 OAuth／session／stash API、`monitor/stash/client.py` | `templates/stash.html`；瀏覽器 cookie 為私有連線ID；OAuth token／opt-in POESESSID 只存加密store | `tests/integration/test_site_features.py`、`tests/unit/test_stash_pricer.py`、`docs/STASH.md` |
| 倉庫物品估值／勾選／快照 | `monitor/stash/pricer.py`、`monitor/stash/store.py` | 公開行情JSON＋按連線隔離加密的 OAuth/session 私有資料 | `tests/unit/test_stash_pricer.py`、`docs/STASH.md` |
| 舊通貨查價 | `monitor/economy/ninja_client.py`、pricer API | `templates/pricer.html`、`cache/economy_*.json` | `tests/integration/test_site_features.py`／`scripts/validate_site.py`；外部來源另驗 |
| 裝備／拓荒篩選工具 | `templates/index.html` 的filter工具、`load_shop_filters` | `content/shop_filters.json` | `scripts/validate_site.py`／`docs/VALIDATION.md` |
| 部署與全功能驗收 | `scripts/deploy.ps1`／GitHub workflow、`scripts/validate_site.py` | `requirements-validation.txt`；報告與截圖放TEMP | `docs/VALIDATION.md`；只測HTTP200不算通過 |

表內省略 `web/` 前綴的路徑均相對於 `web/`。

## 新增／修改功能檢查單

1. 先定位現有責任模組；已有合適位置就追加，不複製第二套。
2. 一個領域的來源、計算與儲存放在同一套件，使用client／pricer／store等角色名稱，不以任務時間命名。
3. 分清公共資料集、私人帳號資料、人工文章、前端資產與測試fixture；機密與私人倉庫不得放Git。
4. 更新本索引與README文件連結，補功能／資料契約與驗證矩陣。
5. 搬移範圍只限受影響領域；同步import、mock、圖片路徑與Docker／discovery，驗證後才移除原路徑。

## 相容期與範圍

功能套件依責任分為 `monitor/economy/`、`monitor/stash/`、`monitor/tw_pricer/`；操作CLI集中於 `scripts/`，專用手冊集中於 `docs/`，README、Flask入口、Dockerfile與依賴檔保留根目錄。行情快取、遊戲文章、模板與圖片保持既有資料契約路徑。測試分為 `tests/unit/` 與 `tests/integration/`。倉庫 OAuth／session-cookie／路由協調仍在 `app.py`，不宣稱所有既有程式已重構。

舊 `content/poe2/fliter/` 文件不在網站分類中載入，保留原檔。POE1 `beetle/` 文章在UI屬策略子項，讀取端已整合，不能因搬目錄破壞密碼保護與舊doc ID。這些legacy位置只為相容，新增內容不得使用錯字／混亂分類。

## 變更紀錄

| 版本 | 日期 | 內容 |
|---|---|---|
| 1.0.0 | 2026-10-06 | 建立功能目錄分類、查找表與漸進搬移規範，歸類倉庫領域模組。 |
| 1.0.1 | 2026-10-06 | 將 economy／台服行情分入各自套件，測試分 unit／integration，更新功能查找路徑。 |
| 1.1.0 | 2026-10-06 | Web操作腳本歸入scripts/、專用文件歸入docs/，保留Flask／Docker必要根入口並更新所有引用。 |
| 1.2.0 | 2026-10-06 | 加入根目錄架構說明及 Mermaid 圖，連結專案層級文件並說明可供其他專案套用的目錄原則。 |
| 1.2.1 | 2026-10-07 | 倉庫查找表同步列出 OAuth／POESESSID session-cookie 連線與加密儲存。 |