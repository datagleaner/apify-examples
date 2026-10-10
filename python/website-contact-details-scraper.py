"""Extract emails, phones and social profiles from websites with Data Gleaner's
Website Contact Details Scraper: https://apify.com/datagleaner/website-contact-details-scraper

Price: US$2.00 per 1,000 websites with an email (US$0.002 each); every other
site, including sites with only phones or socials, is free. The Actor returns one item per input website, so the 3-site
list below caps the run at 3 items and costs at most about US$0.006.

Run: pip install apify-client && APIFY_TOKEN=... python website-contact-details-scraper.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/website-contact-details-scraper").call(
    run_input={
        "websites": ["https://www.appier.com", "stripe.com", "https://www.sakura.ad.jp"],
        "maxPagesPerSite": 5,
    }
)
if run is None:
    raise SystemExit("The run did not return.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["website"], "->", item["status"])
    print("  company: ", item.get("companyName"))
    print("  emails:  ", [e["value"] for e in item.get("emails") or []])
    print("  phones:  ", [p["value"] for p in item.get("phones") or []])
    print("  linkedin:", [s["url"] for s in (item.get("socials") or {}).get("linkedin", [])])
