"""Get the latest posts of a public Telegram channel with the Data Gleaner Telegram Channel Scraper.

Store: https://apify.com/datagleaner/telegram-channel-scraper
Price: $0.50 per 1,000 messages ($0.0005 per message) and $0.001 per channel info row.
This run returns at most 10 messages and 1 channel row, so at most $0.006.

    pip install apify-client
    APIFY_TOKEN=... python telegram-channel-scraper.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/telegram-channel-scraper").call(run_input={
    "channels": ["durov"],
    "maxMessagesPerChannel": 10,
})
if run is None:
    raise SystemExit("The Actor run did not start.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    if item["type"] == "channel":
        print("Channel:", item.get("title"), "-", item.get("subscribers"), "subscribers")
    else:
        print(item["url"], item.get("date"), item.get("views"), (item.get("text") or "")[:80])
