import math
import re
import unicodedata


def _number(value):
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    return number if math.isfinite(number) and number >= 0 else None


def _name(value):
    return unicodedata.normalize("NFKC", str(value or "").strip()).casefold()


def _property(item, property_type):
    for property_value in item.get("properties") or []:
        if property_value.get("type") != property_type:
            continue
        values = property_value.get("values", [])
        if values:
            match = re.search(r"\d+", str(values[0][0]))
            if match:
                return int(match.group())
    return None


def flatten_stash_items(items):
    for item in items or []:
        if not isinstance(item, dict):
            raise ValueError("Invalid official stash item")
        yield item
        yield from flatten_stash_items(item.get("socketedItems"))


def value_stashes(stashes, datasets, game, league, selected_tabs=None, excluded_items=None):
    excluded_items = set(excluded_items or [])
    selected_tabs = None if selected_tabs is None else set(selected_tabs)
    for dataset in datasets.values():
        if dataset.get("game") != game or dataset.get("league") != league:
            raise ValueError("Stash prices must match the exact game and league")

    currency = datasets.get("currency", {})
    divine_rate = next(
        (_number(item.get("price", {}).get("chaosPer1")) for item in currency.get("items", []) if item.get("price") and item["price"].get("divinePer1") == 1),
        None,
    )
    index = {}
    for kind, dataset in datasets.items():
        if dataset.get("status") != "ok":
            continue
        for item in dataset.get("items", []):
            index.setdefault(_name(item.get("zhName") or item.get("name")), []).append((kind, item))

    tabs = []
    resources = {}
    seen = set()

    def visit(tab, parent_name=""):
        tab_id = str(tab.get("id") or "")
        tab_name = str(tab.get("name") or parent_name or tab_id)
        for child in tab.get("children") or []:
            visit(child, tab_name)
        if tab.get("metadata", {}).get("folder"):
            return
        included = selected_tabs is None or tab_id in selected_tabs
        tab_total = 0.0
        tab_unknown = 0
        for position, item in enumerate(flatten_stash_items(tab.get("items"))):
            item_id = str(item.get("id") or f"{tab_id}:{position}")
            if item_id in seen:
                continue
            seen.add(item_id)
            quantity = _number(1 if item.get("stackSize") is None else item["stackSize"])
            if quantity is None or quantity == 0:
                continue
            display_name = item.get("name") or item.get("typeLine") or item.get("baseType") or "Unknown"
            candidates = index.get(_name(display_name), [])
            if item.get("rarity") == "Rare" or item.get("frameType") == 2:
                candidates = []
            if item.get("rarity") == "Unique" or item.get("frameType") in (3, 9, 10):
                candidates = [(kind, row) for kind, row in candidates if kind == "unique" and item.get("identified") is True]
            if item.get("frameType") == 4 or _property(item, 5) is not None:
                level, quality = _property(item, 5), _property(item, 6)
                candidates = [(kind, row) for kind, row in candidates if kind == "gem" and row.get("level") == level and row.get("quality") == (quality if quality is not None else 0) and row.get("isCorrupted") is bool(item.get("corrupted", False))]
            unit_value = None
            category = "unpriced"
            if len(candidates) == 1:
                kind, row = candidates[0]
                category = row.get("category_id") or row.get("category") or kind
                price = row.get("price")
                if isinstance(price, dict) and row.get("priceStatus") != "unavailable":
                    if kind == "currency":
                        unit_value = _number(price.get("divinePer1"))
                    if unit_value is None:
                        amount = _number(price.get("amount", price.get("buy")))
                        if price.get("unit") == "divine":
                            unit_value = amount
                        elif price.get("unit") == "chaos" and divine_rate and amount is not None:
                            unit_value = amount / divine_rate
            counted = included and item_id not in excluded_items
            value = _number(quantity * unit_value) if unit_value is not None else None
            if counted:
                if value is None:
                    tab_unknown += 1
                else:
                    tab_total += value
            variant = (_property(item, 5), _property(item, 6), bool(item.get("corrupted", False)))
            key = (display_name, category, unit_value, variant)
            resource = resources.setdefault(key, {"name": display_name, "category": category, "icon": item.get("icon", ""), "quantity": 0, "value_divine": 0.0 if unit_value is not None else None, "unit_value_divine": unit_value, "level": variant[0], "quality": variant[1], "corrupted": variant[2], "item_ids": [], "tabs": [], "included": counted})
            if included:
                resource["quantity"] += quantity
            if counted:
                if value is not None:
                    resource["value_divine"] += value
            resource["item_ids"].append(item_id)
            if tab_name not in resource["tabs"]:
                resource["tabs"].append(tab_name)
            resource["included"] = resource["included"] or counted
        tabs.append({"id": tab_id, "name": tab_name, "type": tab.get("type", ""), "colour": tab.get("metadata", {}).get("colour", ""), "included": included, "value_divine": tab_total, "unpriced_count": tab_unknown})

    for tab in stashes:
        visit(tab)
    rows = sorted((row for row in resources.values() if row["quantity"] > 0), key=lambda row: row["value_divine"] if row["value_divine"] is not None else -1, reverse=True)
    categories = {}
    for row in rows:
        if row["included"] and row["value_divine"] is not None:
            categories[row["category"]] = categories.get(row["category"], 0.0) + row["value_divine"]
    return {"game": game, "league": league, "tabs": tabs, "resources": rows, "total_divine": sum(tab["value_divine"] for tab in tabs), "unpriced_count": sum(tab["unpriced_count"] for tab in tabs), "categories": [{"id": category, "value_divine": value} for category, value in sorted(categories.items(), key=lambda entry: entry[1], reverse=True)]}