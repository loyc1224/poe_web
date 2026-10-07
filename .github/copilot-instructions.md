# Copilot 專案指示

所有變更先閱讀並遵循根目錄 `PROJECT_RULES.md` 與 `AGENTS.md`。

## 功能驗證

- 一般網站變更依 `PROJECT_RULES.md` CORE-002 與 `web/docs/VALIDATION.md` 按風險分級、合併相鄰小修改後驗收；不要每個微小編輯都重跑完整測試／瀏覽器矩陣。完整 Cloud Run 部署前後仍必須執行全部離線測試與 `web/scripts/validate_site.py` 桌機／手機矩陣，逐項檢查首次載入 icon、圖片解碼、策略解鎖／重整／鎖回及使用者控制項；只測首頁或 `/health` 不算部署驗收。
- 新發現的缺陷必須補回歸測試／閘門並更新共用驗證文件與記憶。回報 PASS／FAIL／BLOCKED；沒有真實 OAuth client／授權時不得把 fixture 成功當成登入或倉庫同步成功。
- 部署必要設定包含策略密碼與固定 session key；缺少時停止部署，機密不得寫入回報、文件或倉庫。

## Cloud Run 部署授權

- 使用者當次明確要求「部署／佈署到 Cloud Run」，或在 Cloud Run 部署上下文中說「部署／佈署」，就代表該次部署已取得 OK。電腦與手機 GitHub Copilot 都適用，不再要求使用者重複說 OK。
- 預設目標沿用 `web/scripts/deploy.ps1`：專案 `udata-gcp-1`、區域 `asia-east1`、服務 `poe-python-web`。未獲明確要求不得改部署目標。
- 部署前由實作者執行受影響測試、啟動服務並驗證 `/health`；失敗時停止部署並回報原因。
- 不把當次授權解讀成每次修改、push 或 PR 都可自動上線；Cloud Scheduler 變更須另取得明確授權。
- GitHub 雲端代理不能沿用使用者電腦上的 `gcloud` 登入。必須先確認可用的遠端部署流程及其 Google Cloud 身分授權。
- 手機／GitHub 雲端代理收到明確部署要求時，更新 `.github/cloud-run-deploy-request.json`，內容為 `{"request_id":"當次唯一的 UTC 時間字串","target":"udata-gcp-1/asia-east1/poe-python-web"}`，與本次程式變更放在同一 PR。只在收到明確部署要求時建立或更新此檔。
- 使用者將部署請求合併至 `main` 後，`.github/workflows/deploy-cloud-run.yml` 會測試、建置、驗證並部署；也可由有權限的使用者在 Actions 手動執行該工作流程。不得自行合併 PR 或規避 GitHub 核准要求；建立部署請求不等於已完成部署。
- 不將長效憑證、token 或私鑰寫入倉庫或對話；不繞過 GitHub 工作流程限制、分支保護或環境核准。
- 區分「已修改部署設定」、「已觸發部署」與「Cloud Run 已部署且驗證成功」。缺少權限、遠端流程或使用者需完成的核准時，回報實際阻礙，不宣稱已完成部署。