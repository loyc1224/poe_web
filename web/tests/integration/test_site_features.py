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
        from urllib.parse import parse_qs, urlsplit

        with patch.object(web_app, "OAUTH_CLIENT_ID", ""):
            response = self.client.get("/api/pricer/oauth/start")
            self.assertEqual(response.status_code, 302)
            self.assertEqual(parse_qs(urlsplit(response.location).query)["message"], ["missing+POE_TW_CLIENT_ID"])
            state = self.client.get("/api/pricer/stash/state")
            self.assertFalse(state.json["oauth_configured"])
            self.assertFalse(state.json["oauth_connected"])
        with patch.object(web_app, "OAUTH_CLIENT_ID", "validation-client"), patch.object(web_app, "OAUTH_CLIENT_SECRET", "fixture-client-secret"), patch.object(web_app, "OAUTH_REDIRECT_URI", ""):
            response = self.client.get("/callback?state=invalid&code=invalid")
            self.assertIn("invalid+or+expired+state", response.location)
        self.assertEqual(self.client.post("/api/pricer/stash/sync", json={"game": "poe1"}).status_code, 401)
        self.assertEqual(self.client.post("/api/pricer/stash/sync", json={"game": "unknown"}).status_code, 400)
        self.assertEqual(self.client.get("/api/pricer/stash/resources").status_code, 404)
        self.assertEqual(self.client.get("/api/pricer/stash/resources?refresh=1").status_code, 401)

    def test_connect_account_redirects_to_official_authorization_with_pkce(self):
        from urllib.parse import parse_qs, urlsplit

        with patch.object(web_app, "OAUTH_CLIENT_ID", "registered-fixture-client"), patch.object(web_app, "OAUTH_CLIENT_SECRET", "fixture-server-secret"), patch.object(web_app, "OAUTH_REDIRECT_URI", "https://example.org/callback"):
            response = self.client.get("/api/pricer/oauth/start?return_to=stash", base_url="https://example.org")
        self.assertEqual(response.status_code, 302)
        destination = urlsplit(response.location)
        expected = urlsplit(web_app.OAUTH_AUTHORIZE_URL)
        self.assertEqual((destination.scheme, destination.netloc, destination.path), (expected.scheme, expected.netloc, expected.path))
        parameters = parse_qs(destination.query)
        self.assertEqual(parameters["client_id"], ["registered-fixture-client"])
        self.assertEqual(parameters["redirect_uri"], ["https://example.org/callback"])
        self.assertEqual(parameters["response_type"], ["code"])
        self.assertEqual(parameters["scope"], ["account:profile account:stashes"])
        self.assertEqual(parameters["code_challenge_method"], ["S256"])
        self.assertTrue(parameters["code_challenge"][0])
        self.assertNotIn("client_secret", parameters)
        with self.client.session_transaction(base_url="https://example.org") as connection:
            self.assertEqual(connection["oauth_state"], parameters["state"][0])
            self.assertNotIn("oauth_code_verifier", connection)
            self.assertEqual(connection["oauth_return_path"], "/stash")

    def test_missing_stash_oauth_configuration_returns_to_stash_without_fake_authorization(self):
        with patch.object(web_app, "OAUTH_CLIENT_ID", ""):
            response = self.client.get("/api/pricer/oauth/start?return_to=stash")
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.location.startswith("/stash?oauth=error&"))
        self.assertNotIn("pathofexile.tw/oauth/authorize", response.location)
        page = self.client.get(response.location)
        self.assertIn("未開啟官方授權：本站尚未設定已註冊的 OAuth client ID。", page.get_data(as_text=True))

    def test_poepricer_client_cannot_be_reused_for_this_site(self):
        from urllib.parse import parse_qs, urlsplit

        with patch.object(web_app, "OAUTH_CLIENT_ID", "poetwpricer"), patch.object(web_app, "OAUTH_CLIENT_SECRET", "fixture-client-secret"), patch.object(web_app, "OAUTH_REDIRECT_URI", "https://example.org/callback"):
            response = self.client.get("/api/pricer/oauth/start?return_to=stash", base_url="https://example.org")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(parse_qs(urlsplit(response.location).query)["message"], ["client_redirect_mismatch+poetwpricer"])
        self.assertEqual(urlsplit(response.location).path, "/stash")
        self.assertNotIn("pathofexile.tw/oauth/authorize", response.location)
        self.assertIn("授權只適用於該網站", self.client.get("/stash").get_data(as_text=True))

    def test_failed_oauth_token_exchange_returns_to_originating_stash_page(self):
        from urllib.parse import parse_qs, urlsplit

        with patch.object(web_app, "OAUTH_CLIENT_ID", "registered-fixture-client"), patch.object(web_app, "OAUTH_CLIENT_SECRET", "fixture-server-secret"), patch.object(web_app, "OAUTH_REDIRECT_URI", "https://example.org/callback"):
            start = self.client.get("/api/pricer/oauth/start?return_to=stash", base_url="https://example.org")
            state = parse_qs(urlsplit(start.location).query)["state"][0]
            with patch("requests.post", return_value=Mock(status_code=400)):
                response = self.client.get("/callback", query_string={"state": state, "code": "fixture-code"}, base_url="https://example.org")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlsplit(response.location).path, "/stash")
        self.assertEqual(parse_qs(urlsplit(response.location).query)["message"], ["token exchange failed 400"])

    def test_successful_oauth_callback_exchanges_pkce_code_with_requested_scope(self):
        from urllib.parse import parse_qs, urlsplit

        token_payload = {"access_token": "fixture-access-token", "refresh_token": "fixture-refresh-token", "expires_in": 3600, "sub": "fixture-account"}
        with patch.object(web_app, "OAUTH_CLIENT_ID", "registered-fixture-client"), patch.object(web_app, "OAUTH_CLIENT_SECRET", "fixture-server-secret"), patch.object(web_app, "OAUTH_REDIRECT_URI", "https://example.org/callback"):
            start = self.client.get("/api/pricer/oauth/start?return_to=stash", base_url="https://example.org")
            state = parse_qs(urlsplit(start.location).query)["state"][0]
            with patch("requests.post", return_value=Mock(status_code=200, json=Mock(return_value=token_payload))) as exchange:
                response = self.client.get("/callback", query_string={"state": state, "code": "fixture-code"}, base_url="https://example.org")
        self.assertEqual(urlsplit(response.location).path, "/stash")
        self.assertEqual(parse_qs(urlsplit(response.location).query), {"oauth": ["connected"]})
        request_data = exchange.call_args.kwargs["data"]
        self.assertEqual(request_data["client_id"], "registered-fixture-client")
        self.assertEqual(request_data["client_secret"], "fixture-server-secret")
        self.assertEqual(request_data["code"], "fixture-code")
        self.assertEqual(request_data["redirect_uri"], "https://example.org/callback")
        self.assertEqual(request_data["scope"], "account:profile account:stashes")
        self.assertTrue(request_data["code_verifier"])
        self.assertTrue(exchange.call_args.kwargs["headers"]["User-Agent"].startswith("OAuth registered-fixture-client/1.0.0 (contact: "))
        state_response = self.client.get("/api/stash/state", base_url="https://example.org")
        self.assertTrue(state_response.json["oauth_connected"])
        self.assertNotIn("fixture-access-token", state_response.get_data(as_text=True))

    def test_refresh_oauth_token_uses_registered_client_and_user_agent(self):
        token_payload = {"access_token": "fixture-refreshed-token", "refresh_token": "fixture-next-refresh-token", "expires_in": 3600, "sub": "fixture-account"}
        with patch.object(web_app, "OAUTH_CLIENT_ID", "registered-fixture-client"), patch.object(web_app, "OAUTH_CLIENT_SECRET", "fixture-server-secret"):
            with patch("requests.post", return_value=Mock(status_code=200, json=Mock(return_value=token_payload))) as refresh:
                with web_app.app.test_request_context():
                    result = web_app._refresh_access_token("fixture-refresh-token")
        self.assertEqual(result["access_token"], "fixture-refreshed-token")
        request_data = refresh.call_args.kwargs["data"]
        self.assertEqual(request_data["grant_type"], "refresh_token")
        self.assertEqual(request_data["client_id"], "registered-fixture-client")
        self.assertEqual(request_data["client_secret"], "fixture-server-secret")
        self.assertEqual(request_data["refresh_token"], "fixture-refresh-token")
        self.assertTrue(refresh.call_args.kwargs["headers"]["User-Agent"].startswith("OAuth registered-fixture-client/1.0.0 (contact: "))

    def test_stash_dashboard_is_private_and_does_not_expose_legacy_global_tokens(self):
        page = self.client.get("/stash")
        self.assertEqual(page.status_code, 200)
        self.assertIn('id="total"', page.get_data(as_text=True))
        self.assertIn('data-stash-navigation', self.client.get("/").get_data(as_text=True))
        web_app._save_stash_state("Other account", "poe1", "test-league", [], "fixture", raw_payload={"tabs": []})
        response = self.client.get("/api/stash/state")
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.json["valuation"])
        self.assertEqual(response.json["account_name"], "")
        self.assertIn("no-store", response.headers["Cache-Control"])
        self.assertIsInstance(response.json["connection_setup"]["client_id"], bool)
        self.assertIsInstance(response.json["connection_setup"]["client_secret"], bool)
        self.assertEqual(self.client.post("/api/stash/sync", json={"game": "poe1", "league": "test-league"}).status_code, 401)
        self.assertEqual(self.client.post("/api/stash/sync", json={"game": "poe2", "league": "test-league"}).status_code, 409)
        self.assertEqual(self.client.post("/api/stash/selection", json={"selected_tabs": []}).status_code, 409)
        self.assertEqual(self.client.post("/api/stash/disconnect", json={}, headers={"Origin": "https://another.example"}).status_code, 403)

    def test_stash_connections_and_oauth_states_cannot_cross_browsers(self):
        with self.client.session_transaction() as connection:
            connection["stash_connection_id"] = "owner_a_01234567890123456789"
        store = web_app._stash_store()
        store.save("owner_a_01234567890123456789", {"tokens": {"access_token": "private-token", "expires_at": 10**12}, "pkce": {"state": "private-state", "verifier": "private-verifier", "created_at": web_app.time.time()}})
        self.assertTrue(self.client.get("/api/stash/state").json["oauth_connected"])
        other = web_app.app.test_client()
        self.assertFalse(other.get("/api/stash/state").json["oauth_connected"])
        with web_app.app.test_request_context():
            self.assertIsNone(web_app._pop_pkce_verifier("private-state"))
        self.assertNotIn("private-token", self.client.get("/api/stash/state").get_data(as_text=True))

    def test_authorized_stash_sync_selection_history_and_failure_preservation(self):
        owner = "owner_a_01234567890123456789"
        with self.client.session_transaction() as connection:
            connection["stash_connection_id"] = owner
        web_app._stash_store().save(owner, {"tokens": {"access_token": "fixture-token", "expires_at": 10**12}})
        dataset = {"game": "poe1", "league": "test-league", "status": "ok", "items": [{"name": "Divine", "price": {"unit": "divine", "divinePer1": 1, "chaosPer1": 500}}]}
        fetched = {"account_name": "Account A", "game": "poe1", "league": "test-league", "tabs": [{"id": "tab-1", "name": "Currency", "items": [{"id": "item-1", "typeLine": "Divine", "stackSize": 10, "frameType": 5}]}]}
        with patch.object(web_app, "fetch_account_stashes", return_value=fetched), patch.object(web_app, "_stash_datasets", return_value={"currency": dataset}):
            response = self.client.post("/api/stash/sync", json={"game": "poe1", "league": "test-league"})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["stash"]["total_divine"], 10)
            resources = self.client.get("/api/pricer/stash/resources")
            self.assertEqual(resources.status_code, 200)
            self.assertEqual(resources.json["resources"][0]["value_divine"], 10)
            with patch.object(web_app, "fetch_account_stashes", side_effect=AssertionError("GET must not synchronize upstream")):
                self.assertEqual(self.client.get("/api/pricer/stash/resources?refresh=1").status_code, 200)
            self.assertEqual(len(self.client.get("/api/stash/state").json["history"]), 1)
            response = self.client.post("/api/stash/selection", json={"selected_tabs": [], "excluded_items": []})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json["valuation"]["total_divine"], 0)
            self.assertEqual(self.client.get("/api/stash/state").json["history"], [])
            self.assertEqual(self.client.post("/api/stash/selection", json={"selected_tabs": ["foreign-tab"]}).status_code, 400)
        with patch.object(web_app, "fetch_account_stashes", side_effect=web_app.StashApiError(429, "rate limit")):
            self.assertEqual(self.client.post("/api/stash/sync", json={"game": "poe1", "league": "test-league"}).status_code, 429)
        self.assertEqual(len(web_app._stash_store().load(owner)["history"]), 1)
        self.assertEqual(self.client.post("/api/stash/disconnect", json={}).status_code, 200)
        self.assertIsNone(self.client.get("/api/stash/state").json["valuation"])

    def test_session_cookie_connection_requires_consent_encrypts_and_disconnects(self):
        session_cookie = "a" * 32
        dataset = {"game": "poe1", "league": "test-league", "status": "ok", "items": [{"name": "Divine Orb", "price": {"unit": "divine", "amount": 1}}]}
        fetched = {"account_name": "Account A", "game": "poe1", "league": "test-league", "tabs": [{"id": "tab-1", "name": "Currency", "items": [{"id": "item-1", "typeLine": "Divine Orb", "stackSize": 2}]}]}
        payload = {"account_name": "Account A", "poe_session": session_cookie, "game": "poe1", "league": "test-league"}
        self.assertEqual(self.client.post("/api/stash/session/connect", json=payload).status_code, 400)
        with patch.object(web_app, "fetch_account_stashes_with_session", return_value=fetched) as fetch_session, patch.object(web_app, "_stash_datasets", return_value={"currency": dataset}):
            connected = self.client.post("/api/stash/session/connect", json={**payload, "accepted_risk": True})
            self.assertEqual(connected.status_code, 200)
            self.assertEqual(connected.json["stash"]["source"], "session-cookie")
            self.assertEqual(fetch_session.call_args.args, (session_cookie, "Account A", "poe1", "test-league"))
            state = self.client.get("/api/stash/state")
            self.assertTrue(state.json["session_connected"])
            self.assertEqual(state.json["connection_mode"], "session-cookie")
            self.assertNotIn(session_cookie, state.get_data(as_text=True))
            self.assertNotIn(session_cookie.encode(), web_app.STASH_DB.read_bytes())
            synced = self.client.post("/api/stash/sync", json={"game": "poe1", "league": "test-league"})
            self.assertEqual(synced.status_code, 200)
            self.assertEqual(fetch_session.call_count, 2)
            self.assertEqual(self.client.post("/api/stash/disconnect", json={}).status_code, 200)
        self.assertFalse(self.client.get("/api/stash/state").json["session_connected"])
        self.assertNotIn(session_cookie.encode(), web_app.STASH_DB.read_bytes())

    def test_connecting_a_different_account_clears_the_previous_account_snapshot(self):
        owner = "owner_a_01234567890123456789"
        web_app._stash_store().save(owner, {"subject": "account-a", "account_name": "Account A", "valuation": {"total_divine": 100}})
        with web_app.app.test_request_context():
            web_app.session["stash_connection_id"] = owner
            web_app._save_tokens({"sub": "account-b", "access_token": "fixture-account-b", "expires_in": 3600})
        stored = web_app._stash_store().load(owner)
        self.assertEqual(stored["subject"], "account-b")
        self.assertNotIn("valuation", stored)
        self.assertNotIn("account_name", stored)
        web_app._stash_store().save(owner, {"account_name": "Unknown previous owner", "valuation": {"total_divine": 999}})
        with web_app.app.test_request_context():
            web_app.session["stash_connection_id"] = owner
            web_app._save_tokens({"sub": "account-b", "access_token": "fixture-account-b", "expires_in": 3600}, initial_authorization=True)
        self.assertNotIn("valuation", web_app._stash_store().load(owner))

    def test_real_oauth_configuration_requires_same_origin_https_callback(self):
        with patch.object(web_app, "OAUTH_CLIENT_ID", "registered-fixture-client"), patch.object(web_app, "OAUTH_CLIENT_SECRET", "fixture-secret"), patch.dict(web_app.app.config, {"TESTING": False}):
            for callback, expected in (("http://example.org/callback", "invalid+POE_TW_REDIRECT_URI"), ("https://foreign.example/callback", "invalid+POE_TW_REDIRECT_URI"), ("https://example.org/callback", None)):
                with self.subTest(callback=callback), patch.object(web_app, "OAUTH_REDIRECT_URI", callback):
                    response = self.client.get("/api/stash/state", base_url="https://example.org")
                    self.assertEqual(response.json["config_error"], expected)

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