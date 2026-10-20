import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from monitor.economy import ninja_client


class EconomyCacheTests(unittest.TestCase):
    def test_empty_upstream_keeps_last_valid_prices(self):
        cases = (
            ("poe2", ninja_client.fetch_economy, "economy_test-league"),
            ("poe1", ninja_client.fetch_poe1_economy, "poe1_economy_test-league"),
        )
        previous = {
            "status": "ok",
            "league": "test-league",
            "fetched_at": 123,
            "errors": [],
            "items": [{"name": "Divine Orb", "chaos": 1}],
        }

        for game, fetch, cache_key in cases:
            with self.subTest(game=game), tempfile.TemporaryDirectory() as temp_dir:
                with patch.object(ninja_client, "CACHE_DIR", Path(temp_dir)):
                    ninja_client._save_cache(cache_key, previous)
                    cache_path = Path(temp_dir) / f"{cache_key}.json"
                    original_cache = cache_path.read_bytes()

                    with patch.object(ninja_client, "_get", return_value={"items": [], "lines": []}):
                        result = fetch("test-league", force=True)

                    self.assertEqual(result["items"], previous["items"])
                    self.assertEqual(result["status"], "unavailable")
                    self.assertTrue(result["stale"])
                    self.assertEqual(cache_path.read_bytes(), original_cache)

                    ninja_client._save_cache(cache_key, {**previous, "items": []})
                    with patch.object(ninja_client, "_get", return_value={"items": [], "lines": []}) as upstream:
                        empty_result = fetch("test-league", force=False)

                    upstream.assert_called()
                    self.assertEqual(empty_result["items"], [])
                    self.assertEqual(empty_result["status"], "unavailable")


if __name__ == "__main__":
    unittest.main()