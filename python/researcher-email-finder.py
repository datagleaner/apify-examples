"""Researcher Email Finder: PubMed authors by topic (Data Gleaner).

Store: https://apify.com/datagleaner/researcher-email-finder
Price: $0.005 per researcher returned with a published email; researchers without one are free.
This run returns at most 10 researchers, so it costs at most $0.05.

Run:
    pip install apify-client
    APIFY_TOKEN=... python researcher-email-finder.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/researcher-email-finder").call(run_input={
    "queries": ["crispr base editing"],
    "yearFrom": 2024,
    "maxResearchers": 10,
})
if run is None:
    raise SystemExit("The run did not return.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(f'{item.get("name")}, {item.get("institution") or "-"} ({item.get("country") or "-"})')
    print("  email:", item.get("email"))
    print("  orcid:", item.get("orcidUrl") or "-")
