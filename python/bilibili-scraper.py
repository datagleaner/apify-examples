"""Bilibili Scraper by Data Gleaner: search Bilibili videos by keyword.

Store: https://apify.com/datagleaner/bilibili-scraper
Price (pay per event): $8 per 1,000 videos, $2 per 1,000 comments,
$0.50 per 1,000 danmaku. This run fetches 5 videos, about $0.04.

Usage:
    pip install apify-client
    APIFY_TOKEN=... python bilibili-scraper.py
"""
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/bilibili-scraper").call(
    run_input={
        "searchKeywords": ["python 教程"],
        "searchOrder": "click",
        "maxItems": 5,
    }
)
if run is None:
    sys.exit("Run did not return.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    if item.get("type") != "video":
        continue
    stats = item.get("stats") or {}
    owner = item.get("owner") or {}
    print(f'{item["title"]} | {stats.get("views")} views | {owner.get("name")} | {item["url"]}')
