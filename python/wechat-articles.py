"""WeChat Articles Scraper (Data Gleaner) - public 微信公众号 articles as text and Markdown.

Store: https://apify.com/datagleaner/wechat-articles
Price: $5 per 1,000 articles (pay per event). This run fetches at most 5, about $0.025.

Run:  pip install apify-client
      APIFY_TOKEN=... python wechat-articles.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/wechat-articles").call(run_input={
    "searchKeywords": ["新能源汽车"],
    "maxArticles": 5,
    "includeContent": ["markdown"],
})
if run is None:
    raise SystemExit("Run did not start")

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(item.get("publishedAt"), "|", item.get("accountName"), "|", item.get("title"))
    print("  ", item.get("url"))
    print("  ", (item.get("contentMarkdown") or "")[:200].replace("\n", " "))
