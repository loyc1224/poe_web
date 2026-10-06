import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import app as web_app
from monitor.tw_pricer import tw_pricer_client, tw_pricer_source


def make_response(payload):
    response = Mock()
    response.json.return_value = payload
    response.raise_for_status.return_value = None
    return response


class PriceDatasetClientTests(unittest.TestCase):
    def test_trade_identity_uses_official_base_type_and_discriminator_for_full_gem_name(self):
        entries = [
            {"category_id": "gem", "type": "霜漣之瞬", "text": "霜漣之瞬．寒風", "disc": "alt_x"},
            {"category_id": "gem", "type": "元素打擊", "text": "元素打擊．光譜", "disc": "alt_x"},
        ]
        index = tw_pricer_client.trade_identity_index(entries)
        for entry in entries:
            with self.subTest(name=entry["text"]):
                identity = tw_pricer_client.resolve_trade_identity({"name": entry["text"]}, "gem", index)
                self.assertEqual(identity, {"type": entry["type"], "discriminator": "alt_x"})

    def test_trade_identity_separates_unique_name_from_base_type_and_rejects_unknown_names(self):
        entry = {"category_id": "accessory", "name": "魔血", "type": "重革腰帶", "text": "魔血\n重革腰帶", "flags": {"unique": True}}
        index = tw_pricer_client.trade_identity_index([entry])
        self.assertEqual(tw_pricer_client.resolve_trade_identity({"name": "魔血"}, "unique", index), {"name": "魔血", "type": "重革腰帶"})
        self.assertIsNone(tw_pricer_client.resolve_trade_identity({"name": "Unknown"}, "unique", index))
        self.assertIsNone(tw_pricer_client.resolve_trade_identity({"name": "魔血"}, "gem", index))

    def test_trade_identity_does_not_guess_ambiguous_item_variants(self):
        entries = [{"category_id": "accessory", "name": "Same name", "type": base, "flags": {"unique": True}} for base in ("Base A", "Base B")]
        index = tw_pricer_client.trade_identity_index(entries)
        self.assertIsNone(tw_pricer_client.resolve_trade_identity({"name": "Same name"}, "unique", index))
        self.assertEqual(tw_pricer_client.resolve_trade_identity({"name": "Same name", "baseType": "Base B"}, "unique", index), {"name": "Same name", "type": "Base B"})

    def test_read_api_preserves_unavailable_price_and_uses_published_official_identity(self):
        fields = {"schema_version": 1, "status": "ok", "game": "poe1", "league": "test-league", "source": "fixture", "fetched_at": 1, "categories": []}
        gem = {"id": 30792, "name": "霜漣之瞬．寒風", "level": 21, "quality": 20, "isCorrupted": True, "price": None, "priceStatus": "unavailable", "medianChaos": 3500, "lastPrice": {"unit": "divine", "amount": 6.86}}
        metadata = {"category_id": "gem", "type": "霜漣之瞬", "text": "霜漣之瞬．寒風", "disc": "alt_x"}
        with tempfile.TemporaryDirectory() as directory, patch.dict(os.environ, {"TW_CURRENCY_BUCKET": ""}), patch.object(tw_pricer_client, "DATA_DIR", Path(directory)):
            tw_pricer_client.save_tw_price_dataset("poe1", "gem", {**fields, "kind": "gem", "category": "gem", "items": [gem]})
            tw_pricer_client.save_tw_price_dataset("poe1", "trade", {**fields, "kind": "trade", "category": "trade", "items": [metadata]})
            with patch("requests.get", side_effect=AssertionError("unexpected upstream request")):
                response = web_app.app.test_client().get("/api/tw-pricer/gem?game=poe1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["trade_metadata_status"], "ok")
        item = response.json["items"][0]
        self.assertIsNone(item["price"])
        self.assertEqual(item["priceStatus"], "unavailable")
        self.assertEqual(item["lastPrice"], gem["lastPrice"])
        self.assertEqual(item["trade_identity"], {"type": "霜漣之瞬", "discriminator": "alt_x"})

    def test_navigation_icon_prefers_source_category_metadata(self):
        image = "https://web.poecdn.com/image/Art/2DItems/Currency/CurrencyRerollRare.png"
        dataset = {
            "categories": [{"id": "Currency", "image": image}],
            "items": [{"imageUrl": "https://webtw.poecdn.com/gen/image/item.png"}],
        }
        self.assertEqual(tw_pricer_client.price_dataset_icon(dataset), image)

    def test_navigation_icon_falls_back_to_real_item_without_inventing_an_image(self):
        image = "https://webtw.poecdn.com/gen/image/item.png"
        self.assertEqual(tw_pricer_client.price_dataset_icon({"categories": [], "items": [{"imageUrl": image}]}), image)
        self.assertEqual(tw_pricer_client.price_dataset_icon({"categories": [], "items": []}), "")

    def test_navigation_icon_rejects_untrusted_and_malformed_urls(self):
        for image in ("https://web.poecdn.com.evil.example/image/item.png", "http://web.poecdn.com/image/item.png", "https://web.poecdn.com/other/item.png", "https://[invalid/image/item.png", None):
            with self.subTest(image=image):
                self.assertEqual(tw_pricer_client.price_dataset_icon({"categories": [{"image": image}], "items": []}), "")

    def test_navigation_icons_handle_missing_datasets_without_upstream_fetches(self):
        with patch.object(tw_pricer_client, "load_tw_price_dataset", side_effect=FileNotFoundError) as loader:
            with patch("requests.get", side_effect=AssertionError("unexpected upstream request")):
                icons = tw_pricer_client.load_tw_price_navigation_icons()
        self.assertEqual(loader.call_count, 7)
        self.assertEqual(icons["poe1"], "")
        self.assertEqual(icons["poe2"], "")
        self.assertNotIn("poe2-beast", icons)

    def test_home_renders_navigation_icons_before_any_panel_is_opened(self):
        from html.parser import HTMLParser

        class NavigationImages(HTMLParser):
            def __init__(self):
                super().__init__()
                self.images = {}

            def handle_starttag(self, tag, attrs):
                attributes = dict(attrs)
                if tag == "img" and "data-price-kind-icon" in attributes:
                    self.images[attributes["data-price-kind-icon"]] = attributes

        image = "https://web.poecdn.com/image/Art/2DItems/Currency/CurrencyRerollRare.png"
        with patch.object(web_app, "load_tw_price_navigation_icons", return_value={"poe1-currency": image}), patch.object(web_app, "record_home_visit", return_value={"total_views": 0, "daily_uniques": 0, "day": "2026-10-06"}):
            with patch("requests.get", side_effect=AssertionError("unexpected upstream request")):
                response = web_app.app.test_client().get("/")
        self.assertEqual(response.status_code, 200)
        parser = NavigationImages()
        parser.feed(response.get_data(as_text=True))
        self.assertEqual(parser.images["poe1-currency"]["src"], image)
        self.assertNotIn("hidden", parser.images["poe1-currency"])
        self.assertIn("hidden", parser.images["poe2-unique"])
        self.assertNotIn("src", parser.images["poe2-unique"])

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
    def test_trade_metadata_is_published_with_game_specific_official_identity(self):
        payload = {"result": [{"id": "gem", "label": "技能寶石", "entries": [{"type": "霜漣之瞬", "text": "霜漣之瞬．寒風", "disc": "alt_x"}]}]}
        for game, endpoint in (("poe1", "trade"), ("poe2", "trade2")):
            with self.subTest(game=game), patch.object(tw_pricer_source.requests, "get", return_value=make_response(payload)) as fetch, patch.object(tw_pricer_source, "save_tw_price_dataset") as save:
                dataset = tw_pricer_source.refresh_trade_metadata(game)
                self.assertEqual(dataset["game"], game)
                self.assertEqual(dataset["kind"], "trade")
                self.assertEqual(dataset["items"][0]["disc"], "alt_x")
                self.assertEqual(dataset["items"][0]["category_id"], "gem")
                self.assertEqual(fetch.call_args.args[0], f"https://pathofexile.tw/api/{endpoint}/data/items")
                save.assert_called_once_with(game, "trade", dataset)

    def test_empty_trade_metadata_does_not_replace_previous_dataset(self):
        with patch.object(tw_pricer_source.requests, "get", return_value=make_response({"result": []})), patch.object(tw_pricer_source, "save_tw_price_dataset") as save:
            with self.assertRaises(ValueError):
                tw_pricer_source.refresh_trade_metadata("poe1")
            save.assert_not_called()

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