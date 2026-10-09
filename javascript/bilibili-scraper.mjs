// Bilibili Scraper by Data Gleaner: search Bilibili videos by keyword.
//
// Store: https://apify.com/datagleaner/bilibili-scraper
// Price (pay per event): $8 per 1,000 videos, $2 per 1,000 comments,
// $0.50 per 1,000 danmaku. This run fetches 5 videos, about $0.04.
//
// Usage:
//   npm install apify-client
//   APIFY_TOKEN=... node bilibili-scraper.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/bilibili-scraper').call({
    searchKeywords: ['python 教程'],
    searchOrder: 'click',
    maxItems: 5,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    if (item.type !== 'video') continue;
    console.log(`${item.title} | ${item.stats?.views} views | ${item.owner?.name} | ${item.url}`);
}
