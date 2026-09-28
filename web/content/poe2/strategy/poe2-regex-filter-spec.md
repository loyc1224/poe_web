# 【POE2】商店正則與篩選文件規格

- 目的：讓網站直接從文件生成篩選按鈕，不用再改前端模板
- 設定檔位置：`content/shop_filters.json`
- 套用頁面：首頁「商店篩選工具」與「換界石篩選」

---

## 檔案結構（JSON）

```json
{
  "poe2": {
    "shop_defaults": ["bow", "quiver", "movement speed"],
    "shop_groups": [
      {
        "title": "🏹 冰霜射擊商店正則 (EN)",
        "keywords": [
          { "label": "Vendor Regex (Guide)", "kw": "bow|mov|[egdl] da.* to a" },
          { "label": "Bow", "kw": "bow" }
        ]
      }
    ],
    "waystone_defaults": ["物品稀有度.*([4-9][0-9]|[1-9][0-9]{2})"],
    "waystone_keywords": [
      { "label": "稀有度 >=40%", "kw": "物品稀有度.*([4-9][0-9]|[1-9][0-9]{2})" }
    ]
  }
}
```

---

## 欄位說明

- `shop_defaults`
- 首次載入時，預設會被勾選並組成篩選字串的 `kw` 清單

- `shop_groups`
- 商店篩選的分組顯示內容
- 每組包含：
- `title`: 分組標題
- `keywords`: 詞條陣列

- `keywords[].label`
- 畫面顯示文字（可中文或英文）

- `keywords[].kw`
- 實際複製到剪貼簿的字串（可為正則）
- 這個欄位就是網站組合篩選字串時使用的內容

- `waystone_defaults` / `waystone_keywords`
- 換界石篩選專用，規則同上

---

## 英文正則規範（你目前需求）

- 商店正則保留英文，請直接寫在 `kw`
- 推薦保留這條基礎式：

```text
bow|mov|[egdl] da.* to a
```

說明：

- `bow`: 找弓
- `mov`: 比對移動速度相關字串
- `[egdl] da.* to a`: 比對附加傷害類型（常見於 `adds ... damage to attacks`）

---

## 維護流程

1. 修改 `content/shop_filters.json`
2. 重新整理網頁
3. 進入「商店篩選工具」確認新詞條與預設是否正確
4. 點「複製」驗證輸出字串

---

## 常見注意事項

- 正則中的 `|` 是 OR，前端會再用 `|` 把多個關鍵字串起來
- 若 `kw` 本身已經是完整正則（例如 `bow|mov|...`），建議單獨放一顆按鈕，避免再與其他片段重複疊加造成太寬鬆
- 若你使用中文客戶端，部分英文關鍵字可能命中率下降；此時可保留英文正則，另外補一組中文對照詞條
