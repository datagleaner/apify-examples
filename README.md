# Data Gleaner Apify examples: Python and JavaScript

Runnable code for every [Data Gleaner](https://apify.com/datagleaner) scraper on the Apify Store: Weibo, Bilibili, Xiaohongshu (RedNote), WeChat articles, Google Hotels, Google Trends, Google News, the Google Ads Transparency Center, website contact details, YouTube channel emails, sitemaps, web pages to Markdown, Medium, Behance, Telegram channels and job boards.

Each scraper is pay-per-result: you pay only for the items it returns, with no subscription. Each example uses a small input, so a run costs cents.

## Quick start

Get an API token from [Apify Console > Settings > API & Integrations](https://console.apify.com/settings/integrations), then run either version.

**Python:**

```bash
pip install -r requirements.txt
export APIFY_TOKEN=your_token
python python/weibo-scraper.py
```

**JavaScript (Node.js 18+):**

```bash
npm install
export APIFY_TOKEN=your_token
node javascript/weibo-scraper.mjs
```

The Python examples use apify-client 3.x, where `call()` returns a run object, so the dataset ID is `run.default_dataset_id` (the old `run["defaultDatasetId"]` raises a TypeError). The JavaScript examples use `run.defaultDatasetId`.

## Examples

| Scraper | What it returns | Python | JavaScript |
|---|---|---|---|
| [Website Contact Details Scraper](https://apify.com/datagleaner/website-contact-details-scraper) | Emails, phones, own social accounts and contact pages of company websites | [python](python/website-contact-details-scraper.py) | [js](javascript/website-contact-details-scraper.mjs) |
| [Sitemap URL Extractor](https://apify.com/datagleaner/sitemap-extractor) | Every page URL in a site's sitemaps, with lastmod | [python](python/sitemap-extractor.py) | [js](javascript/sitemap-extractor.mjs) |
| [Google Hotels Scraper](https://apify.com/datagleaner/google-hotels-scraper) | Hotel prices for your dates, ratings and offers | [python](python/google-hotels-scraper.py) | [js](javascript/google-hotels-scraper.mjs) |
| [Weibo Scraper](https://apify.com/datagleaner/weibo-scraper) | Sina Weibo posts by keyword or user, no login | [python](python/weibo-scraper.py) | [js](javascript/weibo-scraper.mjs) |
| [Bilibili Scraper](https://apify.com/datagleaner/bilibili-scraper) | Bilibili videos, comments and danmaku | [python](python/bilibili-scraper.py) | [js](javascript/bilibili-scraper.mjs) |
| YouTube Channel Contacts | YouTube channel emails and influencer contacts | [python](python/youtube-channel-contacts.py) | [js](javascript/youtube-channel-contacts.mjs) |
| Xiaohongshu (RedNote) Scraper | Xiaohongshu notes with stats | [python](python/xiaohongshu-rednote-scraper.py) | [js](javascript/xiaohongshu-rednote-scraper.mjs) |
| WeChat Articles | Public WeChat official account articles as text and Markdown | [python](python/wechat-articles.py) | [js](javascript/wechat-articles.mjs) |
| China Brand Report | What Chinese social media says about a brand | [python](python/china-brand-report.py) | [js](javascript/china-brand-report.mjs) |
| Google Trends Scraper | Interest over time and Trending Now | [python](python/google-trends-scraper.py) | [js](javascript/google-trends-scraper.mjs) |
| Google News Scraper | Google News articles with resolved publisher URLs | [python](python/google-news-scraper.py) | [js](javascript/google-news-scraper.mjs) |
| Google Ads Transparency Scraper | Ads an advertiser runs, from the Ads Transparency Center | [python](python/google-ads-transparency-scraper.py) | [js](javascript/google-ads-transparency-scraper.mjs) |
| Web to Markdown | Web pages as clean, LLM-ready Markdown | [python](python/web-to-markdown.py) | [js](javascript/web-to-markdown.mjs) |
| Medium Scraper | Medium articles by tag, author or publication | [python](python/medium-scraper.py) | [js](javascript/medium-scraper.mjs) |
| Behance Scraper | Behance projects and creatives | [python](python/behance-scraper.py) | [js](javascript/behance-scraper.mjs) |
| Telegram Channel Scraper | Posts of public Telegram channels | [python](python/telegram-channel-scraper.py) | [js](javascript/telegram-channel-scraper.mjs) |
| Career Site Jobs Scraper | Jobs from company career sites (Greenhouse, Lever, Workday and more) | [python](python/career-jobs-scraper.py) | [js](javascript/career-jobs-scraper.mjs) |
| SEEK Jobs Scraper | SEEK Australia and New Zealand job listings | [python](python/seek-jobs-scraper.py) | [js](javascript/seek-jobs-scraper.mjs) |

Scrapers without a link are publishing to the Store this week; until then, see [apify.com/datagleaner](https://apify.com/datagleaner).

## Use with AI agents (MCP)

Any MCP client (Claude, Cursor, VS Code and others) can call these scrapers through Apify's hosted MCP server. Add it to Claude Code with one Actor preloaded as a tool:

```bash
claude mcp add --transport http apify "https://mcp.apify.com?tools=datagleaner/website-contact-details-scraper"
```

Then ask, for example: "Find the contact emails for stripe.com and plausible.io." Without `?tools=`, the agent can still find our Actors with the server's `search-actors` tool and run them with `call-actor`.

## Guides

Step-by-step guides, with code that works without our tools too, are at [datagleaner.github.io](https://datagleaner.github.io).

## License

MIT. Use the code however you like.
