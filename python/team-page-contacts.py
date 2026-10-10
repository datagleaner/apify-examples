"""Company Leadership and Team Page Scraper (Data Gleaner).

Store: https://apify.com/datagleaner/team-page-contacts
Price: $0.002 per named person found on a company's own site; domains with no team page are free.
This run takes at most 5 people from each of 2 domains, so it costs at most $0.02.

Run:
    pip install apify-client
    APIFY_TOKEN=... python team-page-contacts.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/team-page-contacts").call(run_input={
    "domains": ["baremetrics.com", "mongodb.com"],
    "maxPeoplePerDomain": 5,
    "seniority": ["founder", "c-level"],
})
if run is None:
    raise SystemExit("The run did not return.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(f'{item.get("companyName")}: {item.get("personName")}, {item.get("jobTitle")} ({item.get("seniority")})')
    print("  linkedin:", item.get("linkedinUrl") or "-")
    print("  email:   ", item.get("email") or "-")
    print("  source:  ", item.get("sourceUrl"))
