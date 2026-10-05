"""Fetch both Taiwan currency datasets for a scheduled refresh run."""
import sys
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

from monitor.tw_pricer_source import refresh_all_tw_prices


if __name__ == "__main__":
    try:
        refreshed = refresh_all_tw_prices()
    except Exception as error:
        print(error, file=sys.stderr)
        raise SystemExit(1) from error

    for game, datasets in refreshed.items():
        for kind, data in datasets.items():
            print(f"{game} {kind}: {data['league']} ({len(data['items'])} items; {data['status']})")