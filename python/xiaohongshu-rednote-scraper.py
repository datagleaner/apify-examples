"""Xiaohongshu (RedNote) Scraper by Data Gleaner: 10 notes from the food feed.

Store: https://apify.com/datagleaner/xiaohongshu-rednote-scraper
Price: $0.003 per note (pay per event), so this run costs about $0.03.

    pip install apify-client
    APIFY_TOKEN=... python xiaohongshu-rednote-scraper.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/xiaohongshu-rednote-scraper").call(
    run_input={"feedChannels": ["food"], "maxItems": 10}
)
if run is None:
    raise SystemExit("The run did not start.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    author = (item.get("author") or {}).get("nickname")
    print(f"{item.get('title')} | {author} | likes={item.get('likes')} | {item.get('url')}")
