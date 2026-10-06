"""Read and write the scheduled Taiwan currency JSON datasets."""
import json
import os
import unicodedata
from pathlib import Path
from urllib.parse import urlsplit


DATA_DIR = Path(__file__).resolve().parents[2] / "cache"
DATA_DIR.mkdir(exist_ok=True)


def price_dataset_icon(data: dict) -> str:
    for entry in [*data.get("categories", []), *data.get("items", [])]:
        for field in ("imageUrl", "image"):
            image = entry.get(field)
            if not isinstance(image, str):
                continue
            try:
                parsed = urlsplit(image)
            except ValueError:
                continue
            if (
                parsed.scheme == "https"
                and parsed.netloc in ("web.poecdn.com", "webtw.poecdn.com")
                and parsed.path.startswith(("/image/", "/gen/image/"))
            ):
                return image
    return ""


def load_tw_price_navigation_icons() -> dict:
    icons = {}
    for game in ("poe1", "poe2"):
        for kind in ("currency", "unique", "gem", "beast"):
            if game == "poe2" and kind == "beast":
                continue
            try:
                icons[f"{game}-{kind}"] = price_dataset_icon(load_tw_price_dataset(game, kind))
            except (FileNotFoundError, ValueError, OSError):
                icons[f"{game}-{kind}"] = ""
        icons[game] = next(
            (icons[f"{game}-{kind}"] for kind in ("currency", "unique", "gem") if icons[f"{game}-{kind}"]),
            "",
        )
    return icons


def _dataset_name(game: str, kind: str) -> str:
    if game not in ("poe1", "poe2"):
        raise ValueError("game must be poe1 or poe2")
    if kind not in ("currency", "unique", "gem", "beast", "trade"):
        raise ValueError("unsupported Taiwan price category")
    if kind == "beast" and game != "poe1":
        raise ValueError("beast dataset is only available for poe1")
    return f"tw_{kind}_{game}.json"


def trade_identity_index(items: list) -> dict:
    index = {}
    for entry in items:
        if not isinstance(entry, dict) or not isinstance(entry.get("type"), str):
            continue
        for alias in (entry.get("text") or entry.get("name") or entry["type"], entry.get("name")):
            if isinstance(alias, str) and alias.strip():
                key = unicodedata.normalize("NFKC", " ".join(alias.split())).casefold()
                index.setdefault(key, []).append(entry)
    return index


def resolve_trade_identity(item: dict, kind: str, index: dict) -> dict | None:
    identity_options = []
    for field in ("zhName", "name", "enName", "code"):
        name = item.get(field)
        if not isinstance(name, str) or not name.strip():
            continue
        key = unicodedata.normalize("NFKC", " ".join(name.split())).casefold()
        identity_options = index.get(key, [])
        if identity_options:
            break
    identities = {}
    for entry in identity_options:
        if kind == "gem" and entry.get("category_id") != "gem":
            continue
        if kind == "beast" and entry.get("category_id") != "monster":
            continue
        if kind == "unique" and not entry.get("flags", {}).get("unique"):
            continue
        base_type = item.get("baseType") or item.get("base_type")
        if base_type and entry["type"] != base_type:
            continue
        identity = {"type": entry["type"]}
        if entry.get("name"):
            identity["name"] = entry["name"]
        if entry.get("disc"):
            identity["discriminator"] = entry["disc"]
        identities[tuple(sorted(identity.items()))] = identity
    return next(iter(identities.values())) if len(identities) == 1 else None


def load_tw_price_dataset(game: str, kind: str) -> dict:
    """Load a published dataset without making any upstream network request."""
    dataset_name = _dataset_name(game, kind)
    bucket_name = os.getenv("TW_CURRENCY_BUCKET", "").strip()

    if bucket_name:
        from google.cloud import storage

        blob = storage.Client().bucket(bucket_name).blob(f"tw-currency/{dataset_name}")
        if not blob.exists():
            raise FileNotFoundError(f"尚無 {game} 台服通貨資料集")
        payload = blob.download_as_text(encoding="utf-8")
    else:
        dataset_path = DATA_DIR / dataset_name
        if not dataset_path.exists():
            raise FileNotFoundError(f"尚無 {game} 台服通貨資料集")
        payload = dataset_path.read_text(encoding="utf-8")

    data = json.loads(payload)
    required_fields = ("schema_version", "status", "category", "league", "source", "items", "categories")
    if (
        data.get("game") != game
        or data.get("kind") != kind
        or data.get("category") != kind
        or data.get("schema_version") != 1
        or any(field not in data for field in required_fields)
        or not isinstance(data.get("items"), list)
        or not isinstance(data.get("categories"), list)
    ):
        raise ValueError("台服通貨資料集格式錯誤")
    if kind != "trade":
        try:
            metadata = load_tw_price_dataset(game, "trade")
            index = trade_identity_index(metadata["items"])
        except (FileNotFoundError, ValueError, OSError):
            index = {}
        data["trade_metadata_status"] = "ok" if index else "unavailable"
        data["items"] = [
            {**item, "trade_identity": resolve_trade_identity(item, kind, index)}
            for item in data["items"]
        ]
    return data


def save_tw_price_dataset(game: str, kind: str, data: dict) -> None:
    """Publish a complete dataset atomically to local disk or Cloud Storage."""
    dataset_name = _dataset_name(game, kind)
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    bucket_name = os.getenv("TW_CURRENCY_BUCKET", "").strip()

    if bucket_name:
        from google.cloud import storage

        blob = storage.Client().bucket(bucket_name).blob(f"tw-currency/{dataset_name}")
        blob.upload_from_string(payload, content_type="application/json; charset=utf-8")
        return

    dataset_path = DATA_DIR / dataset_name
    temporary_path = dataset_path.with_suffix(".json.tmp")
    temporary_path.write_text(payload, encoding="utf-8")
    temporary_path.replace(dataset_path)