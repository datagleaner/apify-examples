"""Run the Data Gleaner China Brand Report and print the summary and a few posts.

Store page: https://apify.com/datagleaner/china-brand-report
Price: $4.99 per report, charged once when the report is saved (posts, CSV and
translations included; a run that finds no discussion is not charged). The small
limits below keep the run short, but the report price is the same.

    pip install apify-client
    APIFY_TOKEN=... python china-brand-report.py
"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagleaner/china-brand-report").call(
    run_input={
        "brand": "Starbucks",
        "keywords": ["星巴克"],
        "days": 1,
        "maxWeiboPosts": 50,
        "maxBilibiliVideos": 10,
    }
)
if run is None:
    raise SystemExit("The run did not return; check it in the Apify Console.")

items = client.dataset(run.default_dataset_id).iterate_items()
report = next(items, None)
if report is None:
    raise SystemExit("No output; check the run log in the Apify Console.")

print(f'{report.get("brand")}: {report.get("counts")}')
print(f'Weibo sentiment: {(report.get("sentiment") or {}).get("weibo")}')
print(f'Report: {report.get("reportUrl")}')
for post in report.get("topWeiboPosts") or []:
    print(f'  engagement={post.get("engagement")}  {(post.get("textEn") or post.get("text") or "")[:80]}')

for i, item in enumerate(items):
    if i == 10:
        break
    text = (item.get("text") or "").replace("\n", " ")[:60]
    print(f'{item.get("platform")}  {item.get("publishedAt")}  likes={item.get("likes")}  {text}')
    print(f'    {item.get("url")}')
