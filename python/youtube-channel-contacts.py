"""YouTube Channel Email Scraper and Influencer Contact Finder (Data Gleaner).

Store: https://apify.com/datagleaner/youtube-channel-contacts
Price: $0.015 per channel where a public email was found; channels with no email are free.
This run takes at most 5 channels from one keyword search, so it costs at most $0.075.

Run:
    pip install apify-client
    APIFY_TOKEN=... python youtube-channel-contacts.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/youtube-channel-contacts").call(run_input={
    "searchKeywords": ["fitness coach"],
    "maxChannelsPerKeyword": 5,
    "followLinks": True,
})
if run is None:
    raise SystemExit("The run did not return.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    if item.get("status") != "ok":
        print("error:", item.get("input"), item.get("error"))
        continue
    emails = [e["email"] for e in item.get("emails", [])]
    print(f'{item.get("title")} ({item.get("handle")}), {item.get("subscribers")} subscribers')
    print("  emails: ", ", ".join(emails) or "-")
    print("  website:", item.get("website") or "-")
    print("  socials:", ", ".join(f"{k}={v}" for k, v in (item.get("socials") or {}).items()) or "-")
