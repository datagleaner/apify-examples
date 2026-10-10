"""App Developer Email Finder for Google Play, the App Store, Steam and the Chrome Web Store (Data Gleaner).

Store: https://apify.com/datagleaner/app-developer-email-finder
Price: $0.0015 per app whose developer has a public email; apps without one are free.
This run takes at most 5 Google Play apps for one keyword, so it costs at most $0.0075.

Run:
    pip install apify-client
    APIFY_TOKEN=... python app-developer-email-finder.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/app-developer-email-finder").call(run_input={
    "searchKeywords": ["habit tracker"],
    "stores": ["googlePlay"],
    "maxAppsPerKeyword": 5,
    "onlyWithEmail": True,
})
if run is None:
    raise SystemExit("The run did not return.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(f'{item.get("appName")} ({item.get("store")}) by {item.get("developerName")}')
    print("  email:  ", item.get("developerEmail") or "-")
    print("  website:", item.get("developerWebsite") or "-")
    print("  privacy:", item.get("privacyPolicyUrl") or "-")
