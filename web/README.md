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
