"""Run the Data Gleaner Weibo Scraper and print a few fields of each post.

Store page: https://apify.com/datagleaner/weibo-scraper
Price: $3 per 1,000 posts ($0.003 per post). This run fetches at most 10 posts, so about $0.03.

    pip install apify-client
    APIFY_TOKEN=... python weibo-scraper.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/weibo-scraper").call(
    run_input={"searchQueries": ["瑞幸"], "maxItemsPerQuery": 10}
)
if run is None:
    raise SystemExit("The run did not return; check it in the Apify Console.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    author = (item.get("author") or {}).get("screenName")
    text = (item.get("text") or "").replace("\n", " ")[:80]
    print(f'{item.get("createdAt")}  likes={item.get("likesCount")}  @{author}  {text}')
    print(f'    {item.get("url")}')
