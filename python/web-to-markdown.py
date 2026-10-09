"""Convert web pages to clean, LLM-ready Markdown with the Data Gleaner Web to Markdown Actor.

Store: https://apify.com/datagleaner/web-to-markdown
Price: $1 per 1,000 pages ($0.001 per page that returns content; failed URLs are free).
This run fetches 3 URLs plus at most 2 search results, so at most 5 pages and $0.005.

    pip install apify-client
    APIFY_TOKEN=... python web-to-markdown.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/web-to-markdown").call(run_input={
    "urls": [
        "https://en.wikipedia.org/wiki/Markdown",
        "https://docs.python.org/3/tutorial/introduction.html",
        "https://www.paulgraham.com/greatwork.html",
    ],
    "query": "model context protocol",
    "maxResults": 2,
    "maxCharsPerPage": 2000,
})
if run is None:
    raise SystemExit("The Actor run did not start.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    if item.get("error"):
        print(item["url"], "ERROR:", item["error"])
        continue
    print(item["url"], "|", item.get("title"), "|", item.get("wordCount"), "words via", item.get("fetchedVia"))
    print((item.get("markdown") or "")[:200].replace("\n", " "))
    print()
