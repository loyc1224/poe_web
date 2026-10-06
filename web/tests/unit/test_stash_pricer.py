import unittest
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

from monitor.stash.pricer import value_stashes
from monitor.stash.client import StashApiError, fetch_account_stashes
from monitor.stash.store import StashStore


class StashPricerTests(unittest.TestCase):
    def setUp(self):
        self.currency = {"game": "poe1", "league": "test-league", "status": "ok", "items": [
            {"name": "Divine", "price": {"unit": "divine", "buy": 1, "divinePer1": 1, "chaosPer1": 500}},
            {"name": "Chaos", "price": {"unit": "chaos", "buy": 1, "divinePer1": 0.002, "chaosPer1": 1}},
        ]}
        self.datasets = {"currency": self.currency}
        self.stashes = [{"id": "tab-1", "name": "Currency", "items": [
            {"id": "divines", "typeLine": "Divine", "stackSize": 10, "frameType": 5},
            {"id": "chaos", "typeLine": "Chaos", "stackSize": 500, "frameType": 5},
            {"id": "rare", "name": "Rare", "typeLine": "Belt", "rarity": "Rare"},
        ]}]

    def value(self, **arguments):
        return value_stashes(self.stashes, self.datasets, "poe1", "test-league", **arguments)

    def test_prices_real_stack_quantities_and_keeps_unknown_items_unpriced(self):
        result = self.value()
        self.assertEqual(result["total_divine"], 11)
        self.assertEqual(result["unpriced_count"], 1)
        self.assertIsNone(next(row for row in result["resources"] if row["name"] == "Rare")["value_divine"])

    def test_tab_and_item_selection_control_the_total(self):
        self.assertEqual(self.value(selected_tabs=[])["total_divine"], 0)
        result = self.value(excluded_items=["divines"])
        self.assertEqual(result["total_divine"], 1)
        self.assertEqual(next(row for row in result["resources"] if row["name"] == "Divine")["quantity"], 10)
        self.assertEqual(self.value(selected_tabs=[])["resources"], [])

    def test_gem_variants_are_matched_and_never_merged_by_name_alone(self):
        self.datasets["gem"] = {"game": "poe1", "league": "test-league", "status": "ok", "items": [
            {"name": "Gem", "level": 20, "quality": 0, "isCorrupted": False, "price": {"unit": "chaos", "amount": 500}},
            {"name": "Gem", "level": 21, "quality": 20, "isCorrupted": True, "price": None, "priceStatus": "unavailable", "medianChaos": 5000},
        ]}
        self.stashes = [{"id": "gems", "name": "Gems", "items": [
            {"id": "gem20", "typeLine": "Gem", "frameType": 4, "properties": [{"type": 5, "values": [["20", 0]]}, {"type": 6, "values": [["0%", 0]]}]},
            {"id": "gem21", "typeLine": "Gem", "frameType": 4, "corrupted": True, "properties": [{"type": 5, "values": [["21", 0]]}, {"type": 6, "values": [["20%", 0]]}]},
        ]}]
        result = self.value()
        self.assertEqual(result["total_divine"], 1)
        self.assertEqual(result["unpriced_count"], 1)
        self.assertEqual(len(result["resources"]), 2)

    def test_wrong_game_or_league_is_rejected(self):
        for field, value in (("game", "poe2"), ("league", "another-league")):
            self.currency[field] = value
            with self.assertRaises(ValueError):
                self.value()
            self.currency[field] = "poe1" if field == "game" else "test-league"

    def test_unavailable_history_is_not_used_and_rare_equipment_is_not_guessed(self):
        self.datasets["unique"] = {"game": "poe1", "league": "test-league", "status": "ok", "items": [{"name": "Unique", "price": None, "medianChaos": 5000, "lastPrice": {"unit": "divine", "amount": 10}, "priceStatus": "unavailable"}]}
        self.stashes[0]["items"].append({"id": "unique", "name": "Unique", "typeLine": "Belt", "rarity": "Unique", "identified": True})
        self.assertEqual(self.value()["total_divine"], 11)
        self.assertEqual(self.value()["unpriced_count"], 2)

    def test_nested_tabs_do_not_double_count_the_same_item(self):
        self.stashes.append({"id": "folder", "name": "Folder", "metadata": {"folder": True}, "children": [{"id": "tab-2", "name": "Child", "items": [self.stashes[0]["items"][0]]}]})
        self.assertEqual(self.value()["total_divine"], 11)

    def test_socketed_items_are_counted_once_with_stable_fallback_identifiers(self):
        self.stashes[0]["items"][2]["socketedItems"] = [{"typeLine": "Divine", "stackSize": 2, "frameType": 5}]
        result = self.value()
        self.assertEqual(result["total_divine"], 13)
        resource = next(row for row in result["resources"] if row["name"] == "Divine")
        self.assertIn("tab-1:3", resource["item_ids"])
        self.assertEqual(self.value(excluded_items=["tab-1:3"])["total_divine"], 11)

    def test_nullable_stack_size_counts_nonstackable_items_as_one(self):
        self.stashes[0]["items"][0]["stackSize"] = None
        self.assertEqual(self.value()["total_divine"], 2)


class StashConnectionTests(unittest.TestCase):
    def test_storage_is_encrypted_and_isolated_by_connection(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "stash.db"
            store = StashStore(path, "fixture-secret-key")
            store.save("owner_a_01234567890123456789", {"tokens": {"access_token": "private-fixture-token"}, "account_name": "Account A"})
            self.assertEqual(store.load("owner_a_01234567890123456789")["account_name"], "Account A")
            self.assertEqual(store.load("owner_b_01234567890123456789"), {})
            self.assertNotIn(b"private-fixture-token", path.read_bytes())
            store.delete("owner_a_01234567890123456789")
            self.assertEqual(store.load("owner_a_01234567890123456789"), {})

    def test_client_uses_documented_private_stash_endpoints(self):
        payloads = [{"name": "Account A"}, {"stashes": [{"id": "tab-1", "name": "Currency", "type": "CurrencyStash"}]}, {"stash": {"id": "tab-1", "items": [{"id": "item-1", "typeLine": "Divine"}]}}]
        responses = [Mock(ok=True, status_code=200, json=Mock(return_value=payload)) for payload in payloads]
        with patch("monitor.stash.client.requests.get", side_effect=responses) as get:
            result = fetch_account_stashes("fixture-token", "poe1", "test league")
        self.assertEqual(result["account_name"], "Account A")
        self.assertEqual([call.args[0] for call in get.call_args_list], ["https://api.pathofexile.com/profile", "https://api.pathofexile.com/stash/test%20league", "https://api.pathofexile.com/stash/test%20league/tab-1"])
        self.assertEqual(len(result["tabs"][0]["items"]), 1)

    def test_poe2_is_not_misrepresented_as_supported(self):
        with patch("monitor.stash.client.requests.get") as get:
            with self.assertRaises(StashApiError) as error:
                fetch_account_stashes("fixture-token", "poe2", "test-league")
        self.assertEqual(error.exception.status, 409)
        get.assert_not_called()

    def test_authorization_and_rate_limits_are_reported_without_tokens(self):
        for status in (401, 403, 429):
            with self.subTest(status=status), patch("monitor.stash.client.requests.get", return_value=Mock(status_code=status, ok=False)):
                with self.assertRaises(StashApiError) as error:
                    fetch_account_stashes("private-fixture-token", "poe1", "test-league")
                self.assertEqual(error.exception.status, status)
                self.assertNotIn("private-fixture-token", str(error.exception))

    def test_wrong_league_in_official_items_is_rejected(self):
        payloads = [{"name": "Account A"}, {"stashes": [{"id": "tab-1"}]}, {"stash": {"id": "tab-1", "items": [{"id": "item-1", "league": "another-league"}]}}]
        responses = [Mock(ok=True, status_code=200, json=Mock(return_value=payload)) for payload in payloads]
        with patch("monitor.stash.client.requests.get", side_effect=responses):
            with self.assertRaises(StashApiError) as error:
                fetch_account_stashes("fixture-token", "poe1", "test-league")
        self.assertEqual(error.exception.status, 409)

    def test_nullable_official_children_and_items_are_treated_as_empty(self):
        payloads = [{"name": "Account A"}, {"stashes": [{"id": "tab-1", "children": None}]}, {"stash": {"id": "tab-1", "items": None}}]
        responses = [Mock(ok=True, status_code=200, json=Mock(return_value=payload)) for payload in payloads]
        with patch("monitor.stash.client.requests.get", side_effect=responses):
            result = fetch_account_stashes("fixture-token", "poe1", "test-league")
        self.assertEqual(result["tabs"][0]["items"], [])


if __name__ == "__main__":
    unittest.main()