# 網站功能驗證與共用範本

遵循 [核心規範 CORE-005](../../PROJECT_RULES.md)。本文件提供可重跑的驗證程序、覆蓋範圍與驗收報告範本，不能以首頁或健康端點的 HTTP 200 代替逐項驗收。

## 執行程序

在 `web/` 安裝一次驗證工具；正式容器只安裝 `requirements.txt`，不包含瀏覽器：

```powershell
python -m pip install -r requirements.txt -r requirements-validation.txt
python -m playwright install chromium
python -m unittest discover -s tests -v
python scripts/validate_site.py --report "$env:TEMP\poe-site-validation-local.json"
```

未指定 URL 時，程序自動在隨機本機埠啟動測試站並於結束時關閉。從未追蹤的 `.env` 或環境讀取策略密碼；若沒有固定 session key，只為本機測試設定一個測試值，**不會替正式環境設定機密**。

本機自動驗證站的流量與 OAuth SQLite 使用暫存目錄，不修改正式本機資料庫。策略密碼由 `STRATEGY_PASSWORD` 環境設定提供，本機放未追蹤的 `.env`，正式環境應透過 Secret Manager 注入；**策略密碼不存 SQLite**。SQLite 的用途是流量、OAuth 狀態／token 與倉庫資料。

正式站部署後必須另跑，不可把本機結果當成線上結果：

```powershell
python scripts/validate_site.py --base-url "https://你的正式站" --report "$env:TEMP\poe-site-validation-live.json"
```

價格／查價缺陷回歸與實際官方公開掛單抽查：

```powershell
python scripts/refresh_tw_currency.py --trade-metadata-only
python scripts/validate_site.py --verify-official-trade --report "$env:TEMP\poe-site-validation-official-trade.json"
```

`--verify-official-trade` 使用瀏覽器 DOM 產生的 query 呼叫台服 search/fetch，驗證兩顆回報寶石及魔血、獵首、漢恩的蔑視，每件抽查最多三筆公開掛單。寶石核對完整名稱、Lv21、品質20%、腐化；裝備核對 unique 名稱、基底、已鑑定、官方 rarity 與價格單位，保留貼膜狀態。不輸出賣家帳號、不使用登入憑證。它是明確的管理驗證操作，不是網頁 GET 的即時抓價。官方登入／限流／無資料造成受阻時保留錯誤並停止，不能假稱查到正確物品。

正式策略密碼須已安全放在執行者的環境或 `.env`，且與正式站一致；不得透過聊天傳送或放在命令列參數。報告會遮蔽策略密碼，僅記錄非機密狀態。

## 功能矩陣

| 功能 | 實際驗證 | 限制 |
|---|---|---|
| 健康／設定 | `/health` 存活；`/health/ready` 檢查策略密碼與固定 session key | readiness 只回傳布林，不回傳密碼 |
| 首次導覽 icon | 全新瀏覽器狀態、有效 src、可見圖逐一 decode、naturalWidth／Height | 沒有來源圖片的類別應隱藏空圖，不假造來源圖片 |
| 導覽分類 | 舊 Filter 入口不存在；甲蟲位於策略子項，未解鎖不傳送文章，子項解鎖後開啟甲蟲文章 | 保留裝備／拓荒篩選工具；原始 Filter 文件保留但不載入網站分類 |
| 文章 | 公開與解鎖後策略文章逐一開啟、內容非空、圖片解碼 | 不把文章內容或密碼寫入測試報告 |
| 策略 | 錯誤密碼、成功解鎖、重新整理後仍解鎖、兩版策略文章、鎖回 | 離線另測設定缺漏、錯誤 JSON、Unicode 密碼、限流與 session key 變更 |
| 台服物價 | POE1 四類／POE2 三類、game／kind／status、搜尋、排序、分類、重新讀取、現價／歷史價區隔、文字單位與代表物品圖 | unavailable 不可回退到 medianChaos／lastPrice；UI 刷新只重讀 JSON |
| 台服查價 | 逐一解碼 DOM query，核對已發布官方 type/name/discriminator、遊戲專屬路径、gem_level／quality／corrupted；零品質與 false 不丟失 | canonical 名稱表需精確 match；未知／歧義名稱停用，不能把全名直接塞 type |
| 傳奇裝備查价 | unique 完整名稱＋基底、rarity=unique、identified=true；官方掛單抽查魔血／重革腰帶、獵首／皮革腰帶、漢恩的蔑視／領主戰冠 | 不驗稀有詞綴或特定 unique rolls；貼膜仍是 Unique，不能只看 frameType=3 |
| 篩選 | POE1 裝備、POE2 商店／換界石，選取、清除、換界石重置、POE1 tabs | 每組工具有獨立 selector，空選取與剪貼簿權限分開測試 |
| 複製 | 剪貼簿拒絕有錯誤狀態；允許時逐字比對已複製字串 | 無未處理 Promise／pageerror |
| 舊查價頁 | 兩版切換、搜尋、排序、強制刷新參數，以 deterministic fixture 驗 UI | **不代表外部 poe.ninja 真實刷新或價格正確性已驗證** |
| OAuth／倉庫 | 離線驗設定缺漏、無效 callback、未登入的 state／sync／resources 邊界 | 真實登入與成功同步需正式 client、callback 及使用者授權；目前 BLOCKED |
| 新倉庫統計 | 未登入總值—／停用同步，fixture分頁／物品選取、搜尋排序、分類占比、歷史圖、空分頁、圖片解碼與JS錯誤 | fixture不是真實帳號資產；台服OAuth與Cloud Run私有持久儲存仍BLOCKED，詳見STASH.md |
| 連結帳號 | 主動作保持可點，走官方OAuth後端；獨立齒輪顯示缺設定；unit驗真正302官方URL／PKCE／scope／回呼／Secret不出URL，缺設定與交換失敗回原倉庫頁 | 註冊client缺漏時不能真實授權，不攔截成診斷也不借用他站client；不是解除按鈕灰色就算登入成功 |
| 流量／圖片代理 | 離線驗 API 回應、代理路徑白名單、來源與回應型別 | 無上游連線的離線測試不代表所有遠端圖片一定可用 |
| 桌機／手機 | 1440×1000、390×844，各項操作、JS 錯誤與截圖 | 實作者須看截圖，不能只確認產生了檔案 |

瀏覽器報告以 FAIL 回傳非零退出碼；BLOCKED 仍會寫入報告，預設不阻擋核心功能部署，但不得宣稱全功能通過。要求所有外部流程都必須通過時，加 `--require-oauth`；目前真實 OAuth 仍未自動化，會以非零退出碼停止。

## 部署閘門

- `scripts/deploy.ps1` 先跑全部離線測試、自動本機瀏覽器驗證與正式設定存在檢查；任何失敗立即停止。部署後跑正式 readiness 與相同瀏覽器程序。
- GitHub Actions 在實際容器設定**僅供測試**的策略密碼與固定 session key，再跑同一程序；測試密碼不會設定到 Cloud Run。
- GitHub 正式部署前檢查既有服務是否設定策略密碼與固定 session key；部署後檢查 `/health/ready`。Actions 目前不具備正式密碼讀取權限，因此完整線上解鎖驗收仍由安全持有密碼的執行者跑上述正式站程序。
- 需要人工核准、OAuth 或正式 Secret 設定時，停止並回報實際阻礙，不繞過權限，不把機密放進 artifacts。正式 Secret 建立／IAM／部署仍依當次授權執行。
- `.dockerignore` 與 `.gcloudignore` 都排除 `.env`、憑證與本機 OAuth SQLite 檔案，避免映像或 source upload 包含登入資料。

## 本次發現與回歸

| 日期 | 發現／根因 | 回歸方法／目前狀態 |
|---|---|---|
| 2026-10-06 | HTTP 200 掩蓋功能故障 | 新增 CORE-005、功能矩陣與瀏覽器閘門 |
| 2026-10-06 | 首次首頁 icon 無 src，僅點進分類後才初始化 | 首頁從已發布 JSON 預先提供來源圖；HTML 與冷啟動 decode 測試 |
| 2026-10-06 | 全域 img 樣式讓 hidden 的無圖 icon 仍可見 | 專用 hidden CSS；桌機／手機可見圖測試 |
| 2026-10-06 | Cloud Run 未設定策略密碼與固定 session key | 新增 `/health/ready` 與部署前設定閘門；已依當次授權設定 Secret Manager 參照並於新 revision 驗證 |
| 2026-10-06 | Unicode 密碼被拒絕、非 JSON 物件可能造成錯誤 | UTF-8 constant-time 比較與 JSON 型別檢查；離線邊界測試 |
| 2026-10-06 | 複製被拒絕造成未處理 Promise | 統一複製錯誤處理；拒絕／成功與字串比對 |
| 2026-10-06 | SQLite with context 只提交交易、未關閉連線，Windows 清理失敗 | closing + transaction context；每個功能測試都清理暫存資料庫 |
| 2026-10-06 | 舊 Filter 未使用、甲蟲應屬策略子項 | 排除舊分類、整合甲蟲至受密碼保護的策略；保留原始文件及 doc ID，加入子項與冷啟動解鎖回歸 |
| 2026-10-06 | 寒風／光譜 Lv21 品質20 腐化，price=null 卻顯示歷史 medianChaos 3500／3120，且無單位 | 停止歷史 fallback、排除現價排序、始終顯示文字單位；來源 JSON 未改價，保留 lastPrice 僅供歷史分析 |
| 2026-10-06 | 變異寶石全名誤作 type、沒有限制等級／品質／腐化，POE2 路徑沿用 POE1 | 官方 metadata 確認兩者是基底型別＋alt_x；唯讀 API 附加 identity，DOM query 逐一比對，實際官方 search/fetch 抽查 |
| 2026-10-06 | 裝備查價包含未鑑定掛單，無法用官方回應的空 name 驗證完整傳奇名 | 裝備 query 限制已鑑定傳奇；DOM 與官方 response 都驗 identified=true，不把未知名稱當精確驗收 |
| 2026-10-06 | 貼膜魔血 frameType=10，但官方 rarity=Unique；驗證只接受 frameType=3 誤報失敗 | 優先驗官方 rarity，舊 API 無 rarity 時才接受 frameType=3，保留 foilVariation 證據 |
| 2026-10-06 | 舊倉庫程式猜端點、假設遊戲已提供value、全站共用token／資料 | 換官方文档端點與PoE1限制；個人加密連線／PKCE隔離，不讀舊共用紀錄，純資料集估值與未估價狀態 |
| 2026-10-06 | 新頁圖表括號錯誤未初始化，舊JS閘門跑在新頁之前 | 修正圖表結構，所有頁面完成後才檢查pageerror；桌機／手機fixture回歸 |
| 2026-10-06 | 分頁／物品選取改變可能造成假歷史漲跌，插槽物品可能漏算 | 快照依相同選取範圍過濾；官方物品ID去重，socketedItems／null stackSize與缺ID勾選回歸 |
| 2026-10-06 | 連結帳號被前端攔截成診斷、授權失敗跳舊查價頁；倉庫模組平鋪難定位 | 正常連結走官方OAuth，診斷拆齒輪，返回原頁；倉庫模組歸到monitor/stash/，更新import／mock、CORE-006與根查找索引 |
| 2026-10-06 | 未先確認官方受理狀態就把註冊client當成可立即完成，後又把國際服公告直接套用台服 | 國際服Getting Started暫停新申請，但台服政策尚未確認；使用者授權紀錄證明既有台服應用存在。需台服官方確認本站核發途徑／回呼／API，不能推論既有應用是最近核發或借用其client |
| 2026-10-06 | economy／台服行情模組與測試平鋪，新增功能難依責任定位 | 模組歸類至 `monitor/economy/`、`monitor/tw_pricer/`；測試分 `tests/unit/`、`tests/integration/`；全量 unittest discovery 48 PASS、舊路徑搜尋無殘留，桌機／手機各 10 項 PASS |
| 2026-10-06 | Web根目錄散落部署／更新／驗證腳本與多份操作Markdown | 腳本移至 `scripts/`、專用手冊移至 `docs/`；修正 CI／命令／匯入根路徑；CLI `--help`、PowerShell parser、完整測試與瀏覽器矩陣做提交前驗證 |
| 2026-10-06 | 架構文件與目錄整理提交後依使用者要求部署 | commit `d784208` 部署至 `poe-python-web-00044-gd4`，Ready／100%流量；48 tests PASS，正式站桌機／手機20 checks PASS，真實 OAuth 各 1 BLOCKED；readiness PASS，未修改排程 |

本機與 Python 3.11 實際部署映像完成：20 項離線測試；桌機／手機共 18 項瀏覽器檢查通過，真實 OAuth／授權倉庫同步各有 1 項 BLOCKED。舊查價頁 UI 使用 fixture。

2026-10-06 正式驗收：`poe-python-web-00042-6qn` Ready、100% 流量，正式 `/health/ready` 回報策略密碼與固定 session key 均已設定。對正式 URL 執行相同程序，18 項核心檢查 PASS；策略成功解鎖、重新整理、鎖回及甲蟲子項都以實際設定驗證，桌機／手機截圖已檢查。真實 OAuth／授權倉庫同步仍為 BLOCKED，不能宣稱全外部功能成功。

正式策略密碼與 session key 透過 `poe-web-strategy-password:1`、`poe-web-session-key:1` 的 Secret Manager 参照注入既有 runtime；值不在文件、版控、映像或 SQLite。映像固定 digest 為 `sha256:314ed37a87bb93c0f095b37d84d8bcafb63e9043091adba5e2716c3df36f152f`；正式驗收 JSON／截圖保存於系統 TEMP 的 `poe-site-validation-production.json`／`poe-site-validation-production/`。此為本機合法 gcloud 身分直接部署，並未驗證 GitHub OIDC 端到端流程，也未合併 PR 或修改排程。

2026-10-06 架構文件與目錄整理 commit `d784208a853c392db5227e8163c746459a6c0e6c` 已部署至 `poe-python-web-00044-gd4`，Ready／100%流量；部署前48項 unittest PASS，正式站 20 項桌機／手機功能檢查 PASS，OAuth真實登入／倉庫同步各 1 項 BLOCKED。正式 `/health/ready` PASS；未建立或修改線上排程。報告位於 TEMP 的 `poe-web-predeploy-validation.json` 與 `poe-web-postdeploy-validation.json`。此部署使用本機 gcloud，不代表 GitHub OIDC 流程已驗證。

## 共用報告範本

本次價格／查價修正的本機與部署映像驗證：26 項離線測試；18 項桌機／手機核心檢查 PASS，OAuth／倉庫各 1 項 BLOCKED。`--verify-official-trade` 實際 API 搜尋寒風／光譜分別查到 5／7 筆，各前三筆的全名、Lv21、品質20% 與腐化皆符合。當時公開開價為寒風 10／12／15 神聖石、光譜 7／8／10 神聖石，**不是成交價或本站的新估價**；結果可能隨市場改變。JSON／截圖在 TEMP 的 `poe-site-validation-official-trade.json`／同名目錄。

2026-10-06 使用者明確要求部署後，價格與裝備查價修正已上線至 `poe-python-web-00043-fpx`，Ready／100% 流量，沿用既有 Secret 參照與排程。正式 URL 執行 `validate_site.py --verify-official-trade`：18 核心 checks PASS、OAuth／倉庫各 1 BLOCKED；三件已鑑定傳奇與兩顆指定寶石各前三筆實際官方掛單的名称、基底／變體條件與價格單位皆通過，桌機／手機截圖已檢查。正式證據為 TEMP 的 `poe-site-validation-trade-production.json`／同名截圖目錄。映像 digest `sha256:9f540afa3762b469b46dd50ba9f47b1933a4d51434e2ad267a661572e7cf33de`。本次直接 gcloud 部署，程式／文件未自動 commit/push，也未驗證 GitHub OIDC 部署流程。

装備補驗：`poe-site-validation-equipment.json` 的三件傳奇各前三筆均符合已鑑定、完整名稱與基底。當時魔血開價33／40／40神聖石（後兩筆為貼膜）、獵首15／15／15神聖石、漢恩的蔑視各1幻色石；只是公開開價，不能當成交價、來源估價或相同配值。官方回傳的掛單清單可能截斷，因此報告 matched_count 是回傳列表筆數，不保證總數。稀有裝備詞綴、插槽、腐化狀態與特定傳奇配值尚未驗證。

```text
版本／commit：
驗證環境／URL／revision：
日期／實作者：
離線測試：PASS / FAIL，項目數與命令
桌機／手機：尺寸、功能矩陣與截圖檢查
首次 icon／圖片解碼：
策略：拒絕、成功、重新整理、鎖回
物價／搜尋／排序／分類／刷新／交易連結：
篩選／清除／重置／剪貼簿拒絕與成功：
OAuth／倉庫：PASS / FAIL / BLOCKED，真實或 fixture
新發現：根因、修正位置、回歸案例
未驗證／受阻項目：原因、必要權限或依賴
正式部署：未觸發 / 已觸發 / 已部署且驗證
報告／截圖位置：
```

## 變更紀錄

| 版本 | 日期 | 內容 |
|---|---|---|
| 1.0.0 | 2026-10-06 | 建立逐項驗收程序、部署閘門、icon／策略／複製／SQLite 缺陷回歸紀錄與共用報告範本。 |
| 1.0.1 | 2026-10-06 | 新增 Filter 移除、策略甲蟲子項與密碼儲存說明；隔離驗證資料庫，覆蓋子項解鎖流程。 |
| 1.0.2 | 2026-10-06 | 記錄正式 Secret 配置、revision 與逐項線上驗收結果；保留 OAuth BLOCKED 與 fixture 限制。 |
| 1.0.3 | 2026-10-06 | 新增 unavailable 現價與單位回歸、canonical 名稱／寶石變體精確查詢，以及官方公開掛單的可重跑驗證與結果限制。 |
| 1.0.4 | 2026-10-06 | 新增三件傳奇裝備的真實掛單回歸、已鑑定限制與貼膜 rarity 邊界，說明不包含稀有詞綴／特定配值估價。 |
| 1.0.5 | 2026-10-06 | 記錄價格／裝備查價修正的正式 revision、固定映像與完整線上查詢驗收，保留外部授權限制。 |
| 1.1.0 | 2026-10-06 | 新增倉庫安全／估值回歸，本機與容器45 tests／20 UI checks PASS，真實台服OAuth與持久儲存仍BLOCKED，未部署此功能。 |
| 1.1.1 | 2026-10-06 | 帳號按鈕與官方OAuth導覽／失敗返回回歸、功能套件歸類；本機48 tests／20 UI checks PASS，真實client授權仍BLOCKED。 |
| 1.1.2 | 2026-10-06 | 記錄官方暫停新client核發的外部阻礙與Cloud Run回呼驗證，禁止以假值冒充OAuth接通。 |