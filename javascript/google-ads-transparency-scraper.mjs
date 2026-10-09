// Google Ads Transparency Center Scraper (Data Gleaner) - JavaScript example.
//
// Store: https://apify.com/datagleaner/google-ads-transparency-scraper
// Price: $1.50 per 1,000 ads ($0.0015 per ad). This run is capped at 10 ads, about $0.015.
//
//   npm install apify-client
//   APIFY_TOKEN=your_token node google-ads-transparency-scraper.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/google-ads-transparency-scraper').call({
    domains: ['nike.com'],
    region: 'US',
    maxAdsPerAdvertiser: 10,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const ad of items) {
    console.log(`${ad.advertiserName} | ${ad.format} | ${ad.lastShown} | ${ad.adUrl}`);
}
