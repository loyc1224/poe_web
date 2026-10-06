import argparse
import atexit
import json
import os
import re
import tempfile
import threading
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

from dotenv import load_dotenv
from playwright.sync_api import expect, sync_playwright


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def check_images(page, selector):
    images = page.locator(selector)
    for image in images.all():
        if not image.is_visible():
            continue
        require(bool(image.get_attribute("src")), "Visible image has no source")
        image.scroll_into_view_if_needed()
        image.evaluate("image => image.decode()")
        require(image.evaluate("image => image.naturalWidth > 0 && image.naturalHeight > 0"), "Image failed to decode")


def check_strategy(page, password):
    button = page.locator('[data-strategy-subcategory="beetle"]').first
    if not button.count():
        button = page.locator('[data-category-locked="true"]').first
    require(button.count() > 0, "Strategy articles are not locked for a new visitor")
    button.click()
    expect(page.locator("#strategyPassword")).to_be_visible()
    page.locator("#strategyPassword").fill("validation-intentionally-wrong-password")
    page.locator("#strategySubmit").click()
    expect(page.locator("#strategyError")).not_to_be_empty()
    require(bool(password), "STRATEGY_PASSWORD is required for successful unlock validation")
    page.locator("#strategyPassword").fill(password)
    with page.expect_navigation(wait_until="domcontentloaded"):
        page.locator("#strategySubmit").click()
    require(page.locator('[data-category-locked="true"]').count() == 0, "Strategy did not unlock")
    if page.locator('[data-strategy-subcategory="beetle"]').count():
        expect(page.locator('.doc-card.active')).to_have_attribute('data-doc-subcategory', 'beetle')
    page.reload(wait_until="domcontentloaded")
    require(page.locator('[data-category-locked="true"]').count() == 0, "Session was lost after reload")
    strategy_buttons = page.locator('[data-category-target$="-strategy"]')
    for button in strategy_buttons.all():
        button.click()
        require(page.locator('.category-panel.active .doc-card').count() > 0, "Unlocked strategy has no articles")
    check_documents(page)
    strategy_buttons.last.click()
    with page.expect_navigation(wait_until="domcontentloaded"):
        page.locator('[data-lock-strategy]:visible').first.click()
    require(page.locator('[data-category-locked="true"]').count() > 0, "Strategy did not lock again")


def check_documents(page):
    targets = page.locator('.doc-card').evaluate_all("buttons => buttons.map(button => ({id: button.dataset.docTarget, category: button.dataset.docCategory}))")
    require(bool(targets), "No public documents found")
    for target in targets:
        page.locator(f'[data-category-target="{target["category"]}"]').click()
        page.locator(f'.doc-card[data-doc-target="{target["id"]}"]').click()
        panel = page.locator(f'.doc-panel[data-doc-panel="{target["id"]}"]')
        expect(panel).to_be_visible()
        require(bool(panel.inner_text().strip()), "Document is empty")
        check_images(page, f'.doc-panel[data-doc-panel="{target["id"]}"] img')


def check_navigation(page):
    require(page.locator('[data-category-target$="-filter"], [data-category-target$="-fliter"], [data-category-target$="-beetle"]').count() == 0, "Unused filter or top-level beetle category remains")
    require(page.locator('.strategy-subcategories [data-strategy-parent="poe1-strategy"][data-strategy-subcategory="beetle"]').count() == 1, "Beetle must be a strategy submenu")


def check_prices(page, verify_official=False, official_results=None):
    pairs = page.locator('[data-price-kind]').evaluate_all("buttons => buttons.map(button => ({game: button.dataset.game, kind: button.dataset.priceKind}))")
    require(len(pairs) == 7, "Expected all seven supported price panels")
    for pair in pairs:
        game, kind = pair["game"], pair["kind"]
        response = page.request.get(f"/api/tw-pricer/{kind}?game={game}")
        require(response.status == 200, f"{game}/{kind} dataset HTTP {response.status}")
        data = response.json()
        require(data.get("game") == game and data.get("kind") == kind, "Dataset game/kind mismatch")
        require(data.get("status") in ("ok", "unavailable"), "Invalid dataset status")
        if data["status"] == "ok":
            require(bool(data.get("items")), "Successful dataset is empty")
        toggle = page.locator(f'[data-price-kind="{kind}"][data-game="{game}"]')
        toggle.click()
        panel = page.locator(f'[data-direct-category="{game}-tw-{kind}"]')
        expect(panel).to_have_attribute("data-loaded", "true")
        expect(panel.locator('[data-currency-error]')).to_be_empty()
        search = panel.locator('[data-currency-search]')
        search.fill("validation-no-such-item-97d0e90")
        require(panel.locator('.tw-trade-link').count() == 0, "Search did not filter rows")
        search.fill("")
        sort = panel.locator('[data-currency-sort]')
        values = sort.locator("option").evaluate_all("options => options.map(option => option.value)")
        for value in values:
            sort.select_option(value)
        if data["status"] == "ok":
            links = panel.locator('.tw-trade-link')
            require(links.count() > 0, "Missing trade links")
            link = links.first
            trade_path = '/trade2/search/poe2/' if game == 'poe2' else '/trade/search/'
            require(link.get_attribute("href").startswith("https://pathofexile.tw" + trade_path), "Invalid game-specific trade link")
            require(link.get_attribute("target") == "_blank" and "noopener" in link.get_attribute("rel"), "Unsafe trade link")
            check_images(page, f'[data-direct-category="{game}-tw-{kind}"] tr:first-child img')
            expected_items = {str(item.get('id', item.get('code', item.get('key', item.get('zhName') or item.get('name') or item.get('enName') or '')))): item for item in data['items']}
            anchors = links.evaluate_all("anchors => anchors.map(anchor => ({id: anchor.dataset.tradeItemId, href: anchor.href}))")
            equipment_names = {'\u9b54\u8840', '\u7375\u9996', '\u6f22\u6069\u7684\u8511\u8996'}
            verified_equipment = set()
            for anchor in anchors:
                item = expected_items.get(anchor['id'])
                require(item is not None, "Trade link has no corresponding published item")
                payload = json.loads(parse_qs(urlsplit(anchor['href']).query)['q'][0])
                query = payload['query']
                identity = item.get('trade_identity')
                require(bool(identity), "Trade link has no verified official identity")
                expected_type = {'option': identity['type'], 'discriminator': identity['discriminator']} if identity.get('discriminator') else identity['type']
                require(query['type'] == expected_type and query.get('name') == identity.get('name'), "Trade query does not match the official full item identity")
                if kind == 'unique':
                    filters = query['filters']
                    require(filters['type_filters']['filters']['rarity'] == {'option': 'unique'}, 'Equipment query must constrain unique rarity')
                    require(filters['misc_filters']['filters']['identified'] == {'option': 'true'}, 'Equipment query must exclude unidentified listings')
                if kind == 'gem':
                    filters = query['filters']['misc_filters']['filters']
                    for field, value in (('gem_level', item.get('level')), ('quality', item.get('quality'))):
                        if isinstance(value, (int, float)):
                            require(filters.get(field) == {'min': value, 'max': value}, "Gem trade query lost level/quality variant")
                    if isinstance(item.get('isCorrupted'), bool):
                        require(filters.get('corrupted') == {'option': str(item['isCorrupted']).lower()}, "Gem trade query lost corrupted/uncorrupted variant")
                if verify_official and game == 'poe1' and kind == 'unique' and identity.get('name') in equipment_names:
                    if identity['name'] not in verified_equipment:
                        official_results.append(check_official_equipment_search(data['league'], identity, payload))
                        verified_equipment.add(identity['name'])
            if verify_official and game == 'poe1' and kind == 'unique':
                require(verified_equipment == equipment_names, 'Required equipment cases are missing; official verification cannot be skipped')
        if kind in ('gem', 'unique', 'currency'):
            for item in data.get('items', []):
                if item.get('priceStatus') == 'unavailable' or not item.get('price'):
                    continue
                if item.get('name'):
                    search.fill(item['name'])
                    require(panel.locator('.tw-price-ratio .tw-price-unit').count() > 0, "Current prices must include a visible unit")
                    search.fill('')
                    break
        if game == 'poe1' and kind == 'gem':
            for name in ('\u971c\u6f23\u4e4b\u77ac\uff0e\u5bd2\u98a8', '\u5143\u7d20\u6253\u64ca\uff0e\u5149\u8b5c'):
                variants = [item for item in data.get('items', []) if item.get('name') == name and item.get('level') == 21 and item.get('quality') == 20 and item.get('isCorrupted') is True]
                if verify_official:
                    require(bool(variants), 'Reported gem variant is missing; official verification cannot be skipped')
                for item in variants:
                    search.fill(name)
                    row = panel.locator('tr').filter(has=page.get_by_text(item.get('variantLabel', ''), exact=True)).first
                    if item.get('price') is None or item.get('priceStatus') == 'unavailable':
                        expect(row.locator('.tw-price-empty')).to_have_text('\u66ab\u7121\u6709\u6548\u884c\u60c5')
                        require(row.locator('.tw-price-ratio').count() == 0, "Historical medians must not be shown as current prices")
                    if verify_official:
                        href = row.locator('.tw-trade-link').get_attribute('href')
                        payload = json.loads(parse_qs(urlsplit(href).query)['q'][0])
                        result = check_official_gem_search(page, data['league'], name, payload)
                        official_results.append(result)
            search.fill('')
        categories = page.locator(f'[data-price-category-list="{game}-{kind}"] [data-price-category]')
        if categories.count() > 1:
            categories.nth(1).click()
            categories.first.click()
        with page.expect_response(lambda response: f"/api/tw-pricer/{kind}?game={game}" in response.url):
            panel.locator('[data-currency-refresh]').click()
        expect(panel.locator('[data-currency-refresh]')).to_be_enabled()
        check_images(page, f'[data-price-category-list="{game}-{kind}"] img')


def fetch_official_trade_samples(league, payload):
    import requests

    with requests.Session() as session:
        response = session.post(f'https://pathofexile.tw/api/trade/search/{league}', json=payload, timeout=20)
        response.raise_for_status()
        search = response.json()
        identifiers = search.get('result', [])[:3]
        require(bool(identifiers), 'Official search returned no listings for the requested item')
        response = session.get('https://pathofexile.tw/api/trade/fetch/' + ','.join(identifiers), params={'query': search['id']}, timeout=20)
        response.raise_for_status()
        records = response.json().get('result', [])
    require(bool(records), 'Official fetch returned no listings')
    return search, records


def check_official_equipment_search(league, identity, payload):
    search, records = fetch_official_trade_samples(league, payload)
    samples = []
    for record in records:
        item = record['item']
        require(item.get('identified') is True, 'Unidentified equipment cannot be verified by its full unique name')
        require(item.get('name') == identity['name'], 'Official search returned a different equipment name')
        require(item.get('baseType', item.get('typeLine')) == identity['type'], 'Official search returned a different equipment base type')
        require(item.get('rarity') == 'Unique' or (item.get('rarity') is None and item.get('frameType') == 3), 'Official search returned non-unique equipment')
        price = record.get('listing', {}).get('price') or {}
        require(isinstance(price.get('amount'), (int, float)) and bool(price.get('currency')), 'Equipment asking price is missing its currency')
        samples.append({'name': item['name'], 'base_type': identity['type'], 'rarity': 'unique', 'identified': True, 'foil_variation': item.get('foilVariation'), 'asking_price': price})
    return {'equipment_name': identity['name'], 'base_type': identity['type'], 'matched_count': len(search['result']), 'samples': samples, 'scope': 'unique name/base type only; public asking prices, not sales, rare modifiers or exact unique rolls'}


def check_official_gem_search(page, league, name, payload):
    search, records = fetch_official_trade_samples(league, payload)
    samples = []
    for record in records:
        item = record['item']
        require(item.get('typeLine') == name, 'Official search returned a different full gem name')
        require(item.get('corrupted') is True, 'Official search returned an uncorrupted gem')
        properties = {prop.get('type'): prop for prop in item.get('properties', [])}
        for property_type, expected in ((5, 21), (6, 20)):
            values = properties.get(property_type, {}).get('values', [])
            require(bool(values), 'Official listing is missing gem level/quality')
            number = re.search(r'\d+', values[0][0])
            require(number is not None and int(number.group()) == expected, 'Official listing has the wrong gem level/quality')
        price = record.get('listing', {}).get('price') or {}
        require(isinstance(price.get('amount'), (int, float)) and bool(price.get('currency')), 'Official asking price is missing its currency')
        samples.append({'full_name': name, 'level': 21, 'quality': 20, 'corrupted': True, 'asking_price': price})
    return {'full_name': name, 'matched_count': len(search['result']), 'samples': samples, 'scope': 'public asking prices, not completed sales or source estimates'}


def check_filters(page, context):
    for target, display, copy_id, clear_id in (
        ("poe1-tools", "#p1FilterDisplay", "#copyP1FilterBtn", "#clearP1FilterBtn"),
        ("poe2-tools", "#filterDisplay", "#copyFilterBtn", "#clearFilterBtn"),
        ("poe2-tools", "#wsFilterDisplay", "#copyWsFilterBtn", "#clearWsFilterBtn"),
    ):
        page.locator(f'[data-category-target="{target}"]').click()
        if display == "#wsFilterDisplay" and not page.locator(display).is_visible():
            page.locator('details:has(#wsFilterDisplay) > summary').click()
        panel = page.locator(f'[data-doc-panel="{target}"]')
        if not panel.count():
            panel = page.locator('.doc-panel.active')
        expect(page.locator(display)).to_be_visible()
        chip_selector = {
            '#p1FilterDisplay': '.kw-chip-p1 .chip-label',
            '#filterDisplay': '.kw-chip:not(.kw-chip-ws) .chip-label',
            '#wsFilterDisplay': '.kw-chip-ws .chip-label',
        }[display]
        chip = panel.locator(chip_selector).first
        require(chip.count() > 0, "Missing filter keyword controls")
        before = page.locator(display).inner_text()
        chip.click()
        require(page.locator(display).inner_text() != before, f"{display}: filter selection did not change output")
        if 'empty-display' in (page.locator(display).get_attribute('class') or ''):
            chip.click()
        context.clear_permissions()
        page.locator(copy_id).click()
        expect(page.locator('#copyToast')).to_have_text('\u7121\u6cd5\u5b58\u53d6\u526a\u8cbc\u7c3f')
        context.grant_permissions(['clipboard-read', 'clipboard-write'])
        page.locator(copy_id).click()
        expect(page.locator('#copyToast')).not_to_have_text('\u7121\u6cd5\u5b58\u53d6\u526a\u8cbc\u7c3f')
        require(page.evaluate('navigator.clipboard.readText()') == page.locator(display).inner_text(), "Copied filter differs from displayed output")
        page.locator(clear_id).click()
        require(not page.locator(display).inner_text().count('|'), "Clear filter did not clear output")
        if display == "#wsFilterDisplay":
            page.locator('#resetWsFilterBtn').click()
            require(page.locator(display).inner_text().count('|') > 0, "Waystone reset did not restore defaults")
    page.locator('[data-category-target="poe1-tools"]').click()
    for tab in page.locator('.p1-tab').all():
        tab.click()
        expect(tab).to_have_class('p1-tab active')


def check_legacy_pricer(page):
    fixture_requests = []

    def fixture(route):
        parameters = parse_qs(urlsplit(route.request.url).query)
        fixture_requests.append(parameters)
        route.fulfill(json={
            "status": "ok", "game": parameters.get("game", ["poe2"])[0],
            "league": parameters.get("league", ["Standard"])[0], "fetched_at": 1, "errors": [],
            "items": [{"id": "validation", "name": "Validation item", "zh": "Validation item", "category": "\u901a\u8ca8", "divine_value": 1, "chaos_value": 10}],
        })

    page.route('**/api/pricer/currency?**', fixture)
    page.goto('/pricer', wait_until='domcontentloaded')
    expect(page.locator('#statusText')).to_have_text('ok')
    for game in ('poe1', 'poe2'):
        page.locator(f'#btn-{game}').click()
        expect(page.locator('#statusText')).to_have_text('ok')
        page.locator('#searchInput').fill('validation-no-such-item')
        require(page.locator('#tbody tr').count() <= 1, "Legacy price search did not filter")
        page.locator('#searchInput').fill('')
        for header in page.locator('th[data-sort]').all():
            header.click()
        page.locator('#refreshBtn').click()
        expect(page.locator('#statusText')).to_have_text('ok')
    require(any(request.get('force') == ['1'] for request in fixture_requests), "Legacy refresh did not request forced update")
    page.unroute('**/api/pricer/currency?**', fixture)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url")
    parser.add_argument("--report", type=Path)
    parser.add_argument("--artifacts-dir", type=Path)
    parser.add_argument("--require-oauth", action="store_true")
    parser.add_argument("--verify-official-trade", action="store_true")
    args = parser.parse_args()
    load_dotenv(Path(__file__).with_name(".env"))
    if not args.base_url:
        from werkzeug.serving import make_server

        os.environ.setdefault("FLASK_SECRET_KEY", "local-validation-session-key-not-production")
        from app import app

        database_directory = tempfile.TemporaryDirectory(prefix="poe-validation-databases-")
        app_module = __import__("app")
        app_module.TRAFFIC_DB = Path(database_directory.name) / "traffic.db"
        app_module.STASH_DB = Path(database_directory.name) / "stash.db"
        server = make_server("127.0.0.1", 0, app, threaded=True)
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()

        def close_local_server():
            server.shutdown()
            worker.join()
            server.server_close()
            database_directory.cleanup()

        atexit.register(close_local_server)
        args.base_url = f"http://127.0.0.1:{server.server_port}"
    password = os.getenv("STRATEGY_PASSWORD", "")
    artifacts = args.artifacts_dir or Path(tempfile.mkdtemp(prefix="poe-site-validation-"))
    artifacts.mkdir(parents=True, exist_ok=True)
    results = []
    official_results = []

    def run(name, operation):
        try:
            operation()
            results.append({"feature": name, "status": "PASS"})
        except Exception as error:
            message = str(error)
            if password:
                message = message.replace(password, "[REDACTED]")
            results.append({"feature": name, "status": "FAIL", "detail": message[:1200]})
        print(f'{results[-1]["status"]}: {name}')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        for name, width, height in (("desktop", 1440, 1000), ("mobile", 390, 844)):
            context = browser.new_context(base_url=args.base_url, viewport={"width": width, "height": height})
            page = context.new_page()
            page.set_default_timeout(20000)
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto("/", wait_until="domcontentloaded")
            run(f"{name}: production readiness", lambda: require(page.request.get("/health/ready").status == 200, "Production readiness failed: required configuration is missing"))
            run(f"{name}: initial navigation icons", lambda: check_images(page, '[data-price-nav-icon], [data-price-kind-icon]'))
            run(f"{name}: removed filter and protected beetle submenu", lambda: check_navigation(page))
            run(f"{name}: strategy unlock, reload and lock", lambda: check_strategy(page, password))
            if page.locator("#strategyDialog").is_visible():
                page.locator("#strategyCancel").click()
            run(f"{name}: documents and images", lambda: check_documents(page))
            run(f"{name}: seven price panels, exact trade queries and current prices", lambda: check_prices(page, args.verify_official_trade and name == 'desktop', official_results))
            run(f"{name}: equipment/shop/waystone filters and clipboard permissions", lambda: check_filters(page, context))
            run(f"{name}: browser JavaScript errors", lambda: require(not errors, "Browser JavaScript errors: " + "; ".join(errors)))
            page.screenshot(path=str(artifacts / f"{name}.png"), full_page=True)
            run(f"{name}: legacy pricer controls (deterministic fixture)", lambda: check_legacy_pricer(page))
            state = page.request.get("/api/pricer/stash/state").json()
            results.append({"feature": f"{name}: real OAuth login and authorized stash sync", "status": "BLOCKED", "detail": "Requires a registered OAuth client and an interactive account authorization; not simulated as a successful login", "oauth_configured": state.get("oauth_configured", False)})
            context.close()
        browser.close()
    report = {"checked_at": datetime.now(timezone.utc).isoformat(), "base_url": args.base_url, "artifacts": str(artifacts), "results": results, "official_trade_samples": official_results}
    if args.report:
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    failed = any(result["status"] == "FAIL" or (args.require_oauth and result["status"] == "BLOCKED") for result in results)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())