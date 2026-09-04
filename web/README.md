# Python Web（Flask）

## 1) 建立虛擬環境
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## 2) 安裝套件
```powershell
pip install -r requirements.txt
```

## 3) 啟動網站
```powershell
python app.py
```

## 3-0) 一鍵啟動（含 OAuth 參數）

如果要測試通貨查價頁的 OAuth 登入流程，可使用：

```powershell
.\start_local.ps1 -ClientId "你的 OAuth Client ID"
```

說明：
- `-ClientId` 必填，會寫入 `POE_TW_CLIENT_ID`
- `-RedirectUri` 選填，未提供時會自動使用目前啟動位址（例如 `http://127.0.0.1:5000/callback`）
- 若改埠號可這樣執行：`.\start_local.ps1 -ClientId "你的 OAuth Client ID" -Port 5001`

開啟：`http://127.0.0.1:5000`

健康檢查：`http://127.0.0.1:5000/health`

## 3-1) 商店篩選設定（文件化）

- 設定檔：`content/shop_filters.json`
- POE2 商店篩選與換界石篩選會從這個檔案讀取並產生前端按鈕
- 商店正則可直接維持英文（例如：`bow|mov|[egdl] da.* to a`）

相關說明文件：
- `content/poe2/strategy/poe2-regex-filter-spec.md`

## 4) 部署到 Google Cloud Run（同專案 ID）

預設使用：
- Project ID：`udata-gcp-1`
- Region：`asia-east1`
- Service：`poe-python-web`

PowerShell 一鍵部署：
```powershell
.\deploy.ps1
```

或直接命令：
```powershell
gcloud run deploy poe-python-web --source . --region asia-east1 --project udata-gcp-1 --allow-unauthenticated --platform managed --port 8080
```
