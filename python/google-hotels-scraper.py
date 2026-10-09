"""Google Hotels Scraper by Data Gleaner: hotel prices for your exact dates.

Store page: https://apify.com/datagleaner/google-hotels-scraper
Price: $3.00 per 1,000 hotels ($0.003 per hotel). This run returns at most 10 hotels (about $0.03).

Usage:
    pip install apify-client
    APIFY_TOKEN=your_token python google-hotels-scraper.py
"""
import os
from datetime import date, timedelta

from apify_client import ApifyClient

check_in = date.today() + timedelta(days=30)
check_out = check_in + timedelta(days=2)

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/google-hotels-scraper").call(run_input={
    "locations": ["Tokyo"],
    "checkIn": check_in.isoformat(),
    "checkOut": check_out.isoformat(),
    "adults": 2,
    "currency": "USD",
    "maxHotelsPerLocation": 10,
})
if run is None:
    raise SystemExit("[ERROR] The Actor run did not return.")

for hotel in client.dataset(run.default_dataset_id).iterate_items():
    offers = hotel.get("offers") or []
    cheapest = offers[0]["provider"] if offers else "-"
    print(f'{hotel.get("name")} | rating {hotel.get("rating")} | '
          f'{hotel.get("lowestPrice")} {hotel.get("currency")}/night | first offer: {cheapest}')
