"""Medium Scraper by Data Gleaner: https://apify.com/datagleaner/medium-scraper

Fetches the top Medium articles for one tag and prints a few fields of each.
Price: $0.003 per article ($3 per 1,000) and $0.0005 per response; this run of
up to 10 articles costs about $0.03.

    pip install apify-client
    APIFY_TOKEN=... python medium-scraper.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/medium-scraper").call(
    run_input={
        "tags": ["machine-learning"],
        "tagSort": "top",
        "maxArticlesPerTag": 10,
        "includeContent": False,
    }
)
if run is None:
    raise SystemExit("The run did not start.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    author = (item.get("author") or {}).get("name")
    print(f'{item.get("title")} | {author} | {item.get("claps")} claps | {item.get("readingTimeMinutes")} min | {item.get("url")}')
