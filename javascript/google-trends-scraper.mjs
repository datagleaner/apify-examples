// Google Trends Scraper by Data Gleaner: interest over time for a batch of keywords.
//
// Store page: https://apify.com/datagleaner/google-trends-scraper
// Price: $1.50 per 1,000 results ($0.0015 per result). This run returns 5 results (about $0.0075).
//
// Usage:
//   npm install apify-client
//   APIFY_TOKEN=your_token node google-trends-scraper.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/google-trends-scraper').call({
    mode: 'search',
    searchTerms: ['python', 'javascript', 'rust', 'go', 'kotlin'],
    geo: ['US'],
    timeRange: 'today 12-m',
    outputs: ['interestOverTime'],
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    console.log(`${item.searchTerm} (${item.geo}) | average ${item.average} | peak ${item.peakValue} on ${item.peakDate} | latest ${item.latestValue}`);
}
