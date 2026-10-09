// Behance Scraper by Data Gleaner: https://apify.com/datagleaner/behance-scraper
//
// Searches Behance projects by keyword and prints a few fields of each.
// Price: $0.002 per project ($2 per 1,000) and $0.003 per profile; this run of
// up to 10 projects costs about $0.02.
//
//   npm install apify-client
//   APIFY_TOKEN=... node behance-scraper.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/behance-scraper').call({
    searchQueries: ['packaging design'],
    sort: 'appreciations',
    maxItemsPerQuery: 10,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    console.log(`${item.title} | ${item.ownerName} | ${item.appreciations} appreciations | ${item.url}`);
}
