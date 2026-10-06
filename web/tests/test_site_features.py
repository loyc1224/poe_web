import os
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import Mock, patch

import app as web_app


class SiteFeatureTests(unittest.TestCase):
    def setUp(self):
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        directory = Path(self.stack.enter_context(tempfile.TemporaryDirectory()))
        self.stack.enter_context(patch.object(web_app, "TRAFFIC_DB", directory / "traffic.db"))
        self.stack.enter_context(patch.object(web_app, "STASH_DB", directory / "stash.db"))
        self.stack.enter_context(patch.object(web_app, "STRATEGY_PASSWORD", "validation-password"))
        self.stack.enter_context(patch.dict(web_app.app.config, {"TESTING": True, "SECRET_KEY": "validation-session-key"}))
        self.stack.enter_context(patch.dict(web_app._strategy_login_attempts, {}, clear=True))
        self.stack.enter_context(patch.dict(os.environ, {"TW_CURRENCY_BUCKET": "", "FLASK_SECRET_KEY": "validation-session-key", "SECRET_KEY": ""}))
        self.stack.enter_context(patch("requests.get", side_effect=AssertionError("unexpected upstream GET")))
        self.stack.enter_context(patch("requests.post", side_effect=AssertionError("unexpected upstream POST")))
        self.client = web_app.app.test_client()

    def test_health_and_production_readiness_are_separate(self):
        self.assertEqual(self.client.get("/health").status_code, 200)
        self.assertEqual(self.client.get("/health/ready").status_code, 200)
        with patch.object(web_app, "STRATEGY_PASSWORD", ""):
            response = self.client.get("/health/ready")
            self.assertEqual(response.status_code, 503)
            self.assertFalse(response.json["checks"]["strategy_password"])
            self.assertEqual(self.client.post("/api/strategy/unlock", json={"password": "anything"}).status_code, 503)
        with patch.dict(os.environ, {"FLASK_SECRET_KEY": "", "SECRET_KEY": ""}):
            self.assertEqual(self.client.get("/health/ready").status_code, 503)

    def test_unused_filter_is_removed_and_beetle_is_a_protected_strategy_subcategory(self):
        with tempfile.TemporaryDirectory() as directory:
            content = Path(directory)
            for game, category, title in (("poe1", "beetle", "Private beetle"), ("poe1", "strategy", "Private strategy"), ("poe2", "fliter", "Unused filter"), ("poe2", "builds", "Public build")):
                folder = content / game / category
                folder.mkdir(parents=True)
                (folder / "article.md").write_text(f"# {title}\n- Summary\n{title} content", encoding="utf-8")
            with patch.object(web_app, "CONTENT_DIR", content):
                locked = web_app.load_games(include_strategies=False)
                unlocked = web_app.load_games(include_strategies=True)
                page = self.client.get("/").get_data(as_text=True)
                self.assertIn('data-strategy-subcategory="beetle"', page)
                self.assertNotIn('data-category-target="poe1-beetle"', page)
                self.assertNotIn('data-category-target="poe2-fliter"', page)
                self.assertNotIn("Private beetle content", page)
        categories = [category for game in locked for category in game["categories"]]
        self.assertFalse(any(category["name"] in ("beetle", "fliter", "filter") for category in categories))
        strategy = next(category for category in categories if category["id"] == "poe1-strategy")
        self.assertTrue(strategy["locked"])
        self.assertEqual(strategy["documents"], [])
        self.assertEqual(strategy["count"], 2)
        self.assertEqual(strategy["subcategories"][0]["id"], "beetle")
        documents = [document for game in unlocked for category in game["categories"] for document in category["documents"]]
        beetle = next(document for document in documents if document["subcategory"] == "beetle")
        self.assertEqual(beetle["category"], "strategy")
        self.assertEqual(beetle["id"], "poe1-beetle-article")

    def test_strategy_unlock_reload_lock_and_key_rotation(self):
        with patch.object(web_app, "load_games", wraps=web_app.load_games) as loader:
            self.client.get("/")
            loader.assert_called_with(include_strategies=False)
            response = self.client.post("/api/strategy/unlock", json={"password": "validation-password"})
            self.assertEqual(response.status_code, 200)
            self.client.get("/")
            loader.assert_called_with(include_strategies=True)
            self.client.get("/")
            loader.assert_called_with(include_strategies=True)
            with patch.dict(web_app.app.config, {"SECRET_KEY": "another-validation-key"}):
                self.client.get("/")
                loader.assert_called_with(include_strategies=False)
            self.assertEqual(self.client.post("/api/strategy/lock").status_code, 200)
            self.client.get("/")
            loader.assert_called_with(include_strategies=False)

    def test_strategy_wrong_password_invalid_payload_and_rate_limit(self):
        for payload in (["not-an-object"], "not-an-object", None):
            self.assertEqual(self.client.post("/api/strategy/unlock", json=payload).status_code, 400)
        for attempt in range(5):
            with self.subTest(attempt=attempt):
                self.assertEqual(self.client.post("/api/strategy/unlock", json={"password": "wrong"}).status_code, 401)
        self.assertEqual(self.client.post("/api/strategy/unlock", json={"password": "validation-password"}).status_code, 429)
        with patch.object(web_app.time, "time", return_value=10**12):
            self.assertEqual(self.client.post("/api/strategy/unlock", json={"password": "validation-password"}).status_code, 200)

    def test_unicode_strategy_password_is_supported(self):
        password = "\u7b56\u7565\u6e2c\u8a66"
        with patch.object(web_app, "STRATEGY_PASSWORD", password):
            self.assertEqual(self.client.post("/api/strategy/unlock", json={"password": password}).status_code, 200)

    def test_published_datasets_for_every_supported_game_and_kind(self):
        for game in ("poe1", "poe2"):
            for kind in ("currency", "unique", "gem", "beast"):
                if game == "poe2" and kind == "beast":
                    continue
                with self.subTest(game=game, kind=kind):
                    response = self.client.get(f"/api/tw-pricer/{kind}?game={game}")
                    self.assertEqual(response.status_code, 200)
                    self.assertEqual(response.json["game"], game)
                    self.assertEqual(response.json["kind"], kind)
                    self.assertIn(response.json["status"], ("ok", "unavailable"))
                    self.assertIsInstance(response.json["categories"], list)
                    self.assertIsInstance(response.json["items"], list)
                    if response.json["status"] == "ok":
                        self.assertTrue(response.json["items"])
        with patch.object(web_app, "refresh_all_tw_prices") as refresh:
            self.assertEqual(self.client.post("/api/tw-pricer/refresh").status_code, 403)
            refresh.assert_not_called()

    def test_price_pages_redirects_and_parameter_errors(self):
        for game in ("poe1", "poe2"):
            self.assertEqual(self.client.get(f"/pricer?game={game}").status_code, 200)
            response = self.client.get(f"/tw-pricer?game={game}")
            self.assertEqual(response.status_code, 302)
            self.assertIn(f"{game}-tw-currency", response.location)
        self.assertEqual(self.client.get("/api/pricer/currency?game=unknown").status_code, 400)
        self.assertEqual(self.client.get("/api/pricer/currency?league=%3Cscript%3E").status_code, 400)
        dataset = {"status": "ok", "items": [{"id": "test", "name": "Test", "zh": "Test"}]}
        for game, function in (("poe1", "fetch_poe1_economy"), ("poe2", "fetch_economy")):
            with patch.object(web_app, function, return_value=dataset):
                response = self.client.get(f"/api/pricer/currency?game={game}&league=Standard")
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json["game"], game)

    def test_oauth_configuration_callback_and_unauthorized_stash(self):
        with patch.object(web_app, "OAUTH_CLIENT_ID", ""):
            response = self.client.get("/api/pricer/oauth/start")
            self.assertEqual(response.status_code, 302)
            self.assertIn("missing+POE_TW_CLIENT_ID", response.location)
            state = self.client.get("/api/pricer/stash/state")
            self.assertFalse(state.json["oauth_configured"])
            self.assertFalse(state.json["oauth_connected"])
        with patch.object(web_app, "OAUTH_CLIENT_ID", "validation-client"), patch.object(web_app, "OAUTH_REDIRECT_URI", ""):
            response = self.client.get("/callback?state=invalid&code=invalid")
            self.assertIn("invalid+or+expired+state", response.location)
        self.assertEqual(self.client.post("/api/pricer/stash/sync", json={"game": "poe1"}).status_code, 401)
        self.assertEqual(self.client.post("/api/pricer/stash/sync", json={"game": "unknown"}).status_code, 400)
        self.assertEqual(self.client.get("/api/pricer/stash/resources").status_code, 404)
        self.assertEqual(self.client.get("/api/pricer/stash/resources?refresh=1").status_code, 401)

    def test_traffic_and_image_proxy_allowlist(self):
        self.assertEqual(self.client.get("/api/traffic").status_code, 200)
        self.assertEqual(self.client.get("/api/img-proxy?path=https://example.com/image.png").status_code, 400)
        upstream = Mock(content=b"image", headers={"Content-Type": "image/png"})
        with patch("requests.get", return_value=upstream) as fetch:
            response = self.client.get("/api/img-proxy?path=/gen/image/test.png")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "image/png")
        self.assertEqual(fetch.call_args.args[0], "https://web.poecdn.com/gen/image/test.png")


if __name__ == "__main__":
    unittest.main()