"""List the page URLs in a website's sitemaps with the Data Gleaner Sitemap URL Extractor.

Store: https://apify.com/datagleaner/sitemap-extractor
Price: $0.20 per 1,000 URLs ($0.0002 per URL). This run returns at most 10 URLs, so at most $0.002.

    pip install apify-client
    APIFY_TOKEN=... python sitemap-extractor.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/sitemap-extractor").call(run_input={
    "websites": ["stripe.com"],
    "maxUrlsPerSite": 10,
})
if run is None:
    raise SystemExit("The Actor run did not start.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item["url"], item.get("lastmod"), item.get("priority"), item.get("sitemapUrl"))
