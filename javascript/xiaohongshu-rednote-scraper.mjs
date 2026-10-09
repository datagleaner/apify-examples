// Xiaohongshu (RedNote) Scraper by Data Gleaner: 10 notes from the food feed.
//
// Store: https://apify.com/datagleaner/xiaohongshu-rednote-scraper
// Price: $0.003 per note (pay per event), so this run costs about $0.03.
//
//   npm install apify-client
//   APIFY_TOKEN=... node xiaohongshu-rednote-scraper.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/xiaohongshu-rednote-scraper').call({
    feedChannels: ['food'],
    maxItems: 10,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    console.log(`${item.title} | ${item.author?.nickname} | likes=${item.likes} | ${item.url}`);
}
