"""Fetch both Taiwan currency datasets for a scheduled refresh run."""
import sys
import argparse
from pathlib import Path

from dotenv import load_dotenv

WEB_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WEB_DIR))
load_dotenv(WEB_DIR / ".env")

from monitor.tw_pricer.tw_pricer_source import refresh_all_tw_prices, refresh_trade_metadata


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--trade-metadata-only", action="store_true")
    arguments = parser.parse_args()
    try:
        refreshed = {game: {"trade": refresh_trade_metadata(game)} for game in ("poe1", "poe2")} if arguments.trade_metadata_only else refresh_all_tw_prices()
    except Exception as error:
        print(error, file=sys.stderr)
        raise SystemExit(1) from error

    for game, datasets in refreshed.items():
        for kind, data in datasets.items():
            print(f"{game} {kind}: {data['league']} ({len(data['items'])} items; {data['status']})")