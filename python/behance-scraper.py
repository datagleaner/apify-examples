"""Behance Scraper by Data Gleaner: https://apify.com/datagleaner/behance-scraper

Searches Behance projects by keyword and prints a few fields of each.
Price: $0.002 per project ($2 per 1,000) and $0.003 per profile; this run of
up to 10 projects costs about $0.02.

    pip install apify-client
    APIFY_TOKEN=... python behance-scraper.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/behance-scraper").call(
    run_input={
        "searchQueries": ["packaging design"],
        "sort": "appreciations",
        "maxItemsPerQuery": 10,
    }
)
if run is None:
    raise SystemExit("The run did not start.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(f'{item.get("title")} | {item.get("ownerName")} | {item.get("appreciations")} appreciations | {item.get("url")}')
