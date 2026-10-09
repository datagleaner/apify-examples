"""Run the Data Gleaner Google News Scraper and print a few fields of each article.

Store page: https://apify.com/datagleaner/google-news-scraper
Price: $1.50 per 1,000 articles ($0.0015 per article). This run fetches at most 10 articles, so about $0.015.

    pip install apify-client
    APIFY_TOKEN=... python google-news-scraper.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/google-news-scraper").call(
    run_input={"queries": ["openai"], "timeframe": "1d", "maxArticlesPerQuery": 10}
)
if run is None:
    raise SystemExit("The run did not return; check it in the Apify Console.")

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(f'{item.get("publishedAt")}  {item.get("source")}  {item.get("title")}')
    print(f'    {item.get("articleUrl") or item.get("googleNewsUrl")}')
