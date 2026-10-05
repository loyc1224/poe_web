import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import app as web_app
from monitor import tw_pricer_client, tw_pricer_source


def make_response(payload):
    response = Mock()
    response.json.return_value = payload
    response.raise_for_status.return_value = None
    return response


class PriceDatasetClientTests(unittest.TestCase):
    def test_local_dataset_round_trip_preserves_categories_and_unit_icons(self):
        dataset = {
            "schema_version": 1,
            "status": "ok",
            "game": "poe1",
            "kind": "currency",
            "category": "currency",
            "league": "測試聯盟",
            "fetched_at": 1,
            "source": "test",
            "categories": [{"id": "Scarabs", "label": "聖甲蟲"}],
            "unit_icons": {"chaos": "https://web.poecdn.com/chaos.png"},
            "items": [{"category_id": "Scarabs", "name": "測試聖甲蟲"}],
        }
        with tempfile.TemporaryDirectory() as temp_dir, patch.dict(os.environ, {"TW_CURRENCY_BUCKET": ""}):
            with patch.object(tw_pricer_client, "DATA_DIR", Path(temp_dir)):
                tw_pricer_client.save_tw_price_dataset("poe1", "currency", dataset)
                loaded = tw_pricer_client.load_tw_price_dataset("poe1", "currency")

        self.assertEqual(loaded["categories"], dataset["categories"])
        self.assertEqual(loaded["unit_icons"], dataset["unit_icons"])
        self.assertEqual(loaded["items"][0]["category_id"], "Scarabs")

    def test_invalid_dataset_schema_is_rejected(self):
        invalid_dataset = {"game": "poe1", "kind": "currency", "items": []}
        with tempfile.TemporaryDirectory() as temp_dir, patch.dict(os.environ, {"TW_CURRENCY_BUCKET": ""}):
            with patch.object(tw_pricer_client, "DATA_DIR", Path(temp_dir)):
                (Path(temp_dir) / "tw_currency_poe1.json").write_text(
                    json.dumps(invalid_dataset), encoding="utf-8"
                )
                with self.assertRaises(ValueError):
                    tw_pricer_client.load_tw_price_dataset("poe1", "currency")


class PriceDatasetSourceTests(unittest.TestCase):
    def test_refresh_preserves_all_currency_categories_and_base_icons(self):
        currency_items = [
            {
                "name": "混沌石",
                "category_id": "Currency",
                "category_label": "通貨",
                "image": "https://web.poecdn.com/chaos.png",
                "price": {"unit": "chaos", "buy": 1},
            },
            {
                "name": "聖甲蟲：測試",
                "category_id": "Scarabs",
                "category_label": "聖甲蟲",
                "image": "https://web.poecdn.com/scarab.png",
                "price": {"unit": "chaos", "buy": 4},
            },
        ]
        unique_items = [
            {
                "id": 7,
                "name": "測試傳奇",
                "category": "weapon",
                "imageUrl": "https://web.poecdn.com/unique.png",
                "price": {"unit": "chaos", "amount": 12, "chaosEquivalent": 12},
                "listingCount": 5,
            }
        ]
        gem_item = {
            "id": 8,
            "name": "測試技能寶石",
            "level": 20,
            "imageUrl": "https://web.poecdn.com/gem.png",
            "price": {"unit": "chaos", "amount": 5, "chaosEquivalent": 5},
            "listingCount": 3,
        }
        beast_item = {
            "key": "Test_Beast",
            "zhName": "測試野獸",
            "enName": "Test Beast",
            "beastType": "red",
            "imageUrl": "https://web.poecdn.com/beast.png",
            "medianChaos": 10,
            "medianDivine": 0.02,
            "accountCount": 4,
        }
        responses = [
            make_response({"league": "測試聯盟"}),
            make_response(currency_items),
            make_response({"categories": [{"id": "Currency", "label": "通貨", "image": "https://web.poecdn.com/currency-category.png"}]}),
            make_response(unique_items),
            make_response({"categories": [{"id": "weapon", "label": "武器"}]}),
            make_response({"categories": [{"id": "skill", "label": "技能寶石"}]}),
            make_response([gem_item]),
            make_response({"league": "測試聯盟", "items": [beast_item]}),
        ]

        with patch.object(tw_pricer_source.requests, "get", side_effect=responses), patch.object(
            tw_pricer_source, "save_tw_price_dataset"
        ) as save_dataset:
            datasets = tw_pricer_source.refresh_tw_prices("poe1")

        currency = datasets["currency"]
        self.assertEqual(len(currency["items"]), 2)
        self.assertEqual(currency["unit_icons"]["chaos"], "https://web.poecdn.com/chaos.png")
        self.assertEqual({category["id"] for category in currency["categories"]}, {"Currency", "Scarabs"})
        currency_categories = {category["id"]: category for category in currency["categories"]}
        self.assertEqual(currency_categories["Currency"]["imageUrl"], "https://web.poecdn.com/currency-category.png")
        self.assertEqual(currency_categories["Scarabs"]["imageUrl"], "https://web.poecdn.com/scarab.png")
        self.assertEqual(datasets["unique"]["categories"][0]["label"], "武器")
        self.assertEqual(datasets["unique"]["unit_icons"]["chaos"], "https://web.poecdn.com/chaos.png")
        self.assertEqual(datasets["gem"]["items"][0]["category_id"], "skill")
        self.assertEqual(datasets["beast"]["categories"][0]["label"], "紅色野獸")
        self.assertEqual(len(datasets["beast"]["items"]), 1)
        self.assertEqual(save_dataset.call_count, 4)

    def test_empty_unique_source_is_published_as_unavailable(self):
        responses = [
            make_response({"league": "測試聯盟"}),
            make_response([{"name": "混沌石", "category_id": "Currency", "image": "https://web.poecdn.com/chaos.png", "price": {"unit": "chaos", "buy": 1}}]),
            make_response({"categories": [{"id": "Currency", "label": "通貨"}]}),
            make_response([]),
            make_response({"categories": []}),
            make_response({"categories": []}),
        ]

        with patch.object(tw_pricer_source.requests, "get", side_effect=responses), patch.object(
            tw_pricer_source, "save_tw_price_dataset"
        ) as save_dataset:
            datasets = tw_pricer_source.refresh_tw_prices("poe2")

        self.assertEqual(datasets["unique"]["status"], "unavailable")
        self.assertEqual(datasets["unique"]["items"], [])
        self.assertEqual(datasets["unique"]["message"], "此遊戲目前沒有可用的傳奇行情資料")
        self.assertEqual(save_dataset.call_count, 3)


class PriceDatasetApiTests(unittest.TestCase):
    def setUp(self):
        self.client = web_app.app.test_client()

    def test_read_api_returns_category_metadata_without_fetching_source(self):
        dataset = {
            "schema_version": 1,
            "status": "ok",
            "game": "poe1",
            "kind": "currency",
            "category": "currency",
            "league": "測試聯盟",
            "fetched_at": 1,
            "source": "test",
            "categories": [{"id": "Scarabs", "label": "聖甲蟲"}],
            "unit_icons": {"chaos": "https://web.poecdn.com/chaos.png"},
            "items": [{"category_id": "Scarabs", "name": "測試聖甲蟲"}],
        }
        with patch.object(web_app, "load_tw_price_dataset", return_value=dataset) as load_dataset:
            response = self.client.get("/api/tw-pricer/currency?game=poe1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["categories"][0]["id"], "Scarabs")
        self.assertEqual(response.json["unit_icons"]["chaos"], "https://web.poecdn.com/chaos.png")
        load_dataset.assert_called_once_with("poe1", "currency")

    def test_invalid_game_and_kind_are_rejected(self):
        self.assertEqual(self.client.get("/api/tw-pricer/currency?game=unknown").status_code, 400)
        self.assertEqual(self.client.get("/api/tw-pricer/unknown?game=poe1").status_code, 404)
        self.assertEqual(self.client.get("/api/tw-pricer/beast?game=poe2").status_code, 404)


if __name__ == "__main__":
    unittest.main()