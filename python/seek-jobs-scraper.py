"""SEEK Job Scraper (Data Gleaner) - scrape SEEK Australia & New Zealand job listings.

Store: https://apify.com/datagleaner/seek-jobs-scraper
Price: $0.80 per 1,000 jobs ($0.0008 per job), full descriptions included.
This example fetches at most 10 jobs, which costs under one cent.

Run:
    pip install apify-client
    APIFY_TOKEN=your_token python seek-jobs-scraper.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/seek-jobs-scraper").call(run_input={
    "keywords": ["data analyst"],
    "country": "AU",
    "location": "All Sydney NSW",
    "dateRange": "7",
    "maxJobsPerSearch": 10,
})
if run is None:
    raise SystemExit("The Actor run did not return.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(f'{item.get("title")} | {item.get("companyName")} | '
          f'{item.get("salaryLabel")} | {item.get("location")} | {item.get("url")}')
