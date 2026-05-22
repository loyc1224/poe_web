# POE Flask 網站續聊交接檔

## 1) 專案目標
- 用 Flask 建一個 POE 知識庫網站。
- 內容以 Markdown 維護，網站自動掃描分類並顯示。
- 每次新增策略文件時，要同時處理：文件、圖片命名、靜態資源、部署。

## 2) 目前系統架構

### 應用程式
- 入口：app.py
- 框架：Flask + Markdown
- 邏輯：掃描 content 底下的分類資料夾，每個 md 都會變成一張文件卡與右側內容。

### 分類
- strategy = 策略
- crafting = 做裝
- beetle = 甲蟲

### 內容來源
- 網站內容來源：python_web/content/{category}/*.md
- 圖片來源：python_web/static/images/*
- Markdown 內圖片要用相對路徑 ./xxx.jpg 或 ./xxx.png

### 前端
- 模板：templates/index.html
- 版型：左分類 / 中文件卡 / 右內容
- 支援 Mermaid 流程圖

## 3) 實體資料夾對照
- 專案主目錄：c:/code/Keeps/web/poe_web/python_web
- 網站內容：c:/code/Keeps/web/poe_web/python_web/content
- 網站圖片：c:/code/Keeps/web/poe_web/python_web/static/images
- 本地備份（人工整理）：
  - c:/code/Keeps/web/poe_web/策略
  - c:/code/Keeps/web/poe_web/做裝
  - c:/code/Keeps/web/poe_web/甲蟲

## 4) 已完成狀態（截至本次）
- 甲蟲分類已建立且上線。
- 甲蟲文件已存在：poe-beetle-heist.md。
- 甲蟲文件已包含：
  - 運作邏輯
  - 甲蟲配置
  - 收益與估價
  - 優缺點
  - Mermaid 流程圖
  - 與圖天賦圖片段落
- 圖片已整理於 static/images：
  - beetle-stash-loot.jpg
  - beetle-heist-atlas-passive.png

## 5) 固定作業流程（之後每次都照這個）
1. 接收你提供的文字與圖片檔位置。
2. 幫你整理成一份可讀的 Markdown 文件（含標題、段落、表格、流程圖）。
3. 圖片做語義化命名，複製到 static/images。
4. 文件放到正確分類資料夾（content/strategy、content/crafting、content/beetle）。
5. 如有需要同步到本地備份資料夾（策略/做裝/甲蟲）。
6. 直接部署 Cloud Run 更新網站。

## 6) 下次對話直接貼這段（快速啟動模板）
請依照 SESSION_HANDOFF.md 的流程處理。

這次新增內容：
- 分類：{strategy | crafting | beetle}
- 文件標題：{標題}
- 原始內容：
{貼上你的草稿}

圖片：
- 圖片來源路徑：{例如 c:/code/Keeps/web/poe_web/甲蟲/xxx.png}
- 想要的新檔名：{例如 beetle-xxx.png}
- 要放在哪一段：{例如 與圖天賦}

要求：
- 幫我整理成完整 md
- 幫我改圖名並加入文件
- 幫我更新部署

## 7) 部署指令（固定）
在 c:/code/Keeps/web/poe_web/python_web 執行：
gcloud run deploy poe-python-web --source . --region asia-east1 --project udata-gcp-1 --allow-unauthenticated --platform managed --port 8080
