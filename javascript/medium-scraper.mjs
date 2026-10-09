// Medium Scraper by Data Gleaner: https://apify.com/datagleaner/medium-scraper
//
// Fetches the top Medium articles for one tag and prints a few fields of each.
// Price: $0.003 per article ($3 per 1,000) and $0.0005 per response; this run of
// up to 10 articles costs about $0.03.
//
//   npm install apify-client
//   APIFY_TOKEN=... node medium-scraper.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/medium-scraper').call({
    tags: ['machine-learning'],
    tagSort: 'top',
    maxArticlesPerTag: 10,
    includeContent: false,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    console.log(`${item.title} | ${item.author?.name} | ${item.claps} claps | ${item.readingTimeMinutes} min | ${item.url}`);
}
