"""Career Site Jobs Scraper (Data Gleaner) - Python example.

Store: https://apify.com/datagleaner/career-jobs-scraper
Price: $0.0015 per job returned (pay per event). This run returns at most
10 jobs, so it costs at most $0.015.

Run:
    pip install apify-client
    APIFY_TOKEN=... python career-jobs-scraper.py
"""
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/career-jobs-scraper").call(run_input={
    "companies": ["https://boards.greenhouse.io/stripe", "https://jobs.ashbyhq.com/openai"],
    "titleKeywords": ["engineer"],
    "maxJobsPerCompany": 5,
    "maxItems": 10,
    "includeDescription": False,
})
if run is None:
    sys.exit("[ERROR] The Actor run did not return.")

for job in client.dataset(run.default_dataset_id).iterate_items():
    salary = job.get("salary") or {}
    pay = f"{salary.get('min')}-{salary.get('max')} {salary.get('currency')}" if salary else "n/a"
    print(f"{job['company']} | {job['title']} | {', '.join(job.get('locations') or [])} | {pay} | {job['jobUrl']}")
