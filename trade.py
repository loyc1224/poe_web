# trade.py

import requests
import json

def main():
    # 1. 指定要查询的联赛
    league = "Standard"  # 请确认你在台服官网上看到的联赛名称是 Standard

    # 2. 台服 Search 端点
    search_url = f"https://pathofexile.tw/api/trade/search/{league}"

    # 3. 正确的 payload 结构：顶层要有 "query"（包含 status、filters 等）
    payload = {
        "query": {
            "status": {
                "option": "online"   # 只要“线上”出售的物品
            },
            # 这里必须写 "filters"（复数），而不是 "filter"
            "filters": {
                "trade_filters": {
                    "filters": {
                        # 3a. 物品类别过滤：武器 → 匕首
                        "type_filters": {
                            "filters": {
                                "category": {
                                    "option": "weapon"
                                },
                                "sub_category": {
                                    "option": "dagger"
                                }
                            }
                        },
                        # 3b. 稀有度过滤：只要 Rare（稀有）
                        "rarity_filters": {
                            "filters": {
                                "rarity": {
                                    "option": "rare"
                                }
                            }
                        },
                        # 3c. 价格过滤：最低 5 Chaos
                        "trade_filters": {
                            "filters": {
                                "price": {
                                    "min": 5    # 数字 5 表示最低 5 Chaos
                                },
                                "currency": {
                                    "option": "chaos"
                                }
                            }
                        }
                    }
                }
                # 如果后续还有其他 filters（如 misc_filters），也放在这里
            }
        },
        # 4. 排序：按价格从低到高
        "sort": {
            "price": "asc"
        }
    }

    # 5. 发起 POST 请求
    headers = {"Content-Type": "application/json"}
    resp = requests.post(search_url, headers=headers, json=payload)
    try:
        data = resp.json()
    except ValueError:
        print("回传内容不是合法 JSON，HTTP code：", resp.status_code)
        print("回传的纯文本：", resp.text)
        return

    # 6. 如果失败，打印错误并退出
    if resp.status_code != 200:
        print("搜尋失敗，HTTP code：", resp.status_code)
        # 大部分 invalid query 会在 resp.json() 里有类似 {'error': {'code':2,'message':'Invalid query'}}
        print("錯誤訊息：", data)
        return

    # 7. 拿到符合条件的 ID list 与 search_id
    result_ids = data.get("result", [])
    total_matches = data.get("total", 0)
    search_id = data.get("id")

    print(f"台服「{league}」聯盟搜尋結果共 {total_matches} 筆符合條件。")

    if not result_ids:
        print("目前沒有符合條件的物品。")
        return

    # 8. 示範拿前 10 筆 ID 来 Fetch
    top_n = 10
    to_fetch = result_ids[:top_n]
    id_str = ",".join(to_fetch)

    fetch_url = f"https://pathofexile.tw/api/trade/fetch/{id_str}?query={search_id}"
    fetch_resp = requests.get(fetch_url)
    try:
        items_data = fetch_resp.json()
    except ValueError:
        print("Fetch 回传内容不是合法 JSON，HTTP code：", fetch_resp.status_code)
        print("Fetch 回传的纯文本：", fetch_resp.text)
        return

    # 9. 逐笔列印物品关键信息
    for idx, item in enumerate(items_data.get("result", []), start=1):
        listing = item.get("listing", {})
        item_info = item.get("item", {})

        seller_account = listing.get("account", {}).get("name")
        price_amount = listing.get("price", {}).get("amount")
        price_currency = listing.get("price", {}).get("currency")
        raw_name = item_info.get("name") or item_info.get("typeLine")
        whisper_msg = listing.get("whisper")

        print(f"--- 第 {idx} 筆 ---")
        print(f"物品：{raw_name}")
        print(f"賣家：{seller_account}")
        print(f"價格：{price_amount} {price_currency}")
        print(f"聯絡 Whisper：{whisper_msg}")
        print()

if __name__ == "__main__":
    main()

