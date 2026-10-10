"""Shopify Partner and Agency Contacts (Data Gleaner).

Store: https://apify.com/datagleaner/shopify-partner-contacts
Price: $0.005 per partner with a public email or phone; partners with neither are free.
This run takes at most 10 partners in Germany, so it costs at most $0.05.

Run:
    pip install apify-client
    APIFY_TOKEN=... python shopify-partner-contacts.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/shopify-partner-contacts").call(run_input={
    "countries": ["de"],
    "maxPartners": 10,
})
if run is None:
    raise SystemExit("The run did not return.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(f'{item.get("partnerName")} ({item.get("city")}, {item.get("country")}), tier {item.get("partnerTier") or "-"}')
    print("  email:  ", item.get("email") or "-")
    print("  phone:  ", item.get("phone") or "-")
    print("  website:", item.get("website") or "-")
