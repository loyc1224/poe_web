# Python Web（Flask）

本專案所有建構需遵循倉庫根目錄 [`PROJECT_RULES.md`](../PROJECT_RULES.md)；該文件是資料集、驗收、目錄與文件的核心規範。

## 目標

提供 PoE1／PoE2 繁體中文知識庫、工具與台服物價。行情由更新器同步成 JSON，網站只讀資料集，不在使用者查詢時連線抓取來源。

## 服務與模組

| 模組 | 責任 |
|---|---|
| Flask 首頁 | 分類導覽、Markdown 文件、PoE 工具與右側面板 |
| 台服物價更新器 | 同步通貨／傳奇資料、分類與兌換幣圖示，驗證後發布 JSON |
| 台服物價 API | 依遊戲與類別讀取 JSON，不呼叫行情上游 |
| Cloud Scheduler | 每小時觸發受保護的資料刷新端點 |

主要入口：`app.py`。共用 economy 來源 client 與台服資料集更新器集中在 `monitor/`，Jinja 頁面位於 `templates/`。

## 功能

- 首頁三欄知識庫，支援 POE1／POE2 分類、文章與策略密碼保護。
- 左側 POE1／POE2「物價」可折疊，分類有通貨、傳奇、寶石；POE1 另有野獸。各類依來源分類顯示圖示、中文名稱與筆數，選取後右側原地篩選。
- 價格以基準通貨圖示 → 物品圖示表示，另顯示趨勢、掛單數或信心資訊。
- 每筆價格旁提供另開的台服官方交易搜尋連結。
- 更新器產生 POE1／POE2 × 通貨／傳奇／寶石，以及 POE1 野獸共七份 JSON；Cloud Run 多實例可共用私有 Cloud Storage。
- OAuth 倉庫同步、商店篩選及知識文件管理。
- POE2 傳奇／寶石來源目前回傳空清單，狀態會顯示 unavailable；野獸行情目前只有 POE1 endpoint，不以其他遊戲或聯盟價格代替。

## 技術堆疊

- Python 3.11+、Flask、Jinja、Python-Markdown、Requests。
- JSON／本機 cache；Cloud Run 部署可使用 Google Cloud Storage 與 Cloud Scheduler。
- 自動化驗證使用 Python `unittest`。

## 架構與資料流程

### 系統架構

```mermaid
graph TB
	subgraph Client[使用者端]
		Browser[瀏覽器 / Jinja UI]
	end
	subgraph Web[Flask Web]
		Home[首頁與面板]
		PriceAPI[台服物價唯讀 API]
		OtherAPI[OAuth / 工具 API]
	end
	subgraph Data[資料與內容]
		Dataset[通貨／傳奇／寶石／野獸 JSON]
		Content[Markdown / 靜態資源]
		Shared[(Cloud Storage，可選)]
	end
	subgraph Refresh[更新流程]
		Scheduler[Cloud Scheduler]
		RefreshAPI[受保護刷新端點]
		Collector[資料更新器與分類驗證]
		Source[POE Pricer TW API]
	end
	Browser --> Home
	Browser --> PriceAPI
	Browser --> OtherAPI
	Home --> Content
	PriceAPI --> Dataset
	Dataset --- Shared
	Scheduler --> RefreshAPI
	RefreshAPI --> Collector
	Collector --> Source
	Collector --> Dataset
```

### 台服物價同步時序

```mermaid
sequenceDiagram
	participant Scheduler as Cloud Scheduler
	participant Flask as Flask Refresh API
	participant Collector as 更新器
	participant Source as POE Pricer TW
	participant Store as JSON / Cloud Storage
	participant Browser as 網頁
	Scheduler->>Flask: 每小時 POST + refresh token
	Flask->>Collector: 驗證授權後執行更新
	Collector->>Source: 抓取聯盟、分類、通貨／傳奇／寶石／野獸
	Source-->>Collector: 原始 JSON
	Collector->>Collector: 分類、驗證、建立 unit_icons
	Collector->>Store: 原子發布遊戲與類別資料集
	Browser->>Flask: GET 遊戲與物價類別
	Flask->>Store: 唯讀載入 JSON
	Store-->>Flask: 分類 metadata 與行情 items
	Flask-->>Browser: 回傳資料集
```

## 專案結構

```text
web/
  app.py                  Flask routes / application assembly
	monitor/                economy clients and synchronized price datasets
  cache/                  generated JSON / local database cache
  content/<game>/<type>/  structured Markdown knowledge
  templates/              Jinja pages and panels
  static/                 images and static assets
  tests/                  offline unit / contract tests
```

完整目錄責任與資料契約見根目錄 `PROJECT_RULES.md`。

## 快速開始

在 `web/` 目錄執行：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

開啟 `http://127.0.0.1:5000`；健康檢查為 `/health`。

OAuth 本機測試：

```powershell
.\start_local.ps1 -ClientId "你的 OAuth Client ID"
```

`-RedirectUri` 可選，預設使用目前 host／port 的 callback；如需改埠號加上 `-Port 5001`。

更新台服行情 JSON：

```powershell
python refresh_tw_currency.py
python -m unittest discover -s tests -v
```

每小時 Cloud Scheduler 與共享 Cloud Storage 設定：

```powershell
.\setup_tw_currency_scheduler.ps1 -BucketName "你的唯一 bucket 名稱" -RuntimeServiceAccount "Cloud Run 服務帳號"
```

此設定會修改線上 GCP 資源；依核心規範，須先取得使用者明確 OK 才能執行。部署 Cloud Run 同樣必須先本機驗證並取得明確 OK。

## 文件索引

- 核心規範：[`../PROJECT_RULES.md`](../PROJECT_RULES.md)
- 延續作業摘要：`SESSION_HANDOFF.md`
- PoE2 篩選規格：`content/poe2/strategy/poe2-regex-filter-spec.md`
- POE1／POE2 物價資料 API：`/api/tw-pricer/<kind>?game=poe1|poe2`，kind 為 `currency`、`unique`、`gem`；`beast` 僅限 POE1

## Change Log

| 版本 | 日期 | 變更 |
|---|---|---|
| 1.2.0 | 2026-10-05 | 新增寶石與野獸 JSON 分類、放大側欄圖示、每筆台服交易搜尋連結，並擴充更新器與契約測試。 |
| 1.3.0 | 2026-10-05 | 移除開季監控頁／API 及 POE1／POE2 快速交易面板，保留物價與倉庫查價流程。 |
