"""Google Ads Transparency Center Scraper (Data Gleaner) - Python example.

Store: https://apify.com/datagleaner/google-ads-transparency-scraper
Price: $1.50 per 1,000 ads ($0.0015 per ad). This run is capped at 10 ads, about $0.015.

    pip install apify-client
    APIFY_TOKEN=your_token python google-ads-transparency-scraper.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/google-ads-transparency-scraper").call(
    run_input={"domains": ["nike.com"], "region": "US", "maxAdsPerAdvertiser": 10}
)
if run is None:
    raise SystemExit("The run did not start.")
for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item.get("advertiserName"), "|", item.get("format"), "|", item.get("lastShown"), "|", item.get("adUrl"))
