"""Read and write the scheduled Taiwan currency JSON datasets."""
import json
import os
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "cache"
DATA_DIR.mkdir(exist_ok=True)


def _dataset_name(game: str, kind: str) -> str:
    if game not in ("poe1", "poe2"):
        raise ValueError("game must be poe1 or poe2")
    if kind not in ("currency", "unique", "gem", "beast"):
        raise ValueError("unsupported Taiwan price category")
    if kind == "beast" and game != "poe1":
        raise ValueError("beast dataset is only available for poe1")
    return f"tw_{kind}_{game}.json"


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