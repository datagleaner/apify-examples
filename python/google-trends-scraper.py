"""Google Trends Scraper by Data Gleaner: interest over time for a batch of keywords.

Store page: https://apify.com/datagleaner/google-trends-scraper
Price: $1.50 per 1,000 results ($0.0015 per result). This run returns 5 results (about $0.0075).

Usage:
    pip install apify-client
    APIFY_TOKEN=your_token python google-trends-scraper.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/google-trends-scraper").call(run_input={
    "mode": "search",
    "searchTerms": ["python", "javascript", "rust", "go", "kotlin"],
    "geo": ["US"],
    "timeRange": "today 12-m",
    "outputs": ["interestOverTime"],
})
if run is None:
    raise SystemExit("[ERROR] The Actor run did not return.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(f'{item.get("searchTerm")} ({item.get("geo")}) | average {item.get("average")} | '
          f'peak {item.get("peakValue")} on {item.get("peakDate")} | latest {item.get("latestValue")}')
