// Run the Data Gleaner Google News Scraper and print a few fields of each article.
//
// Store page: https://apify.com/datagleaner/google-news-scraper
// Price: $1.50 per 1,000 articles ($0.0015 per article). This run fetches at most 10 articles, so about $0.015.
//
//   npm install apify-client
//   APIFY_TOKEN=... node google-news-scraper.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/google-news-scraper').call({
    queries: ['openai'],
    timeframe: '1d',
    maxArticlesPerQuery: 10,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    console.log(`${item.publishedAt}  ${item.source}  ${item.title}`);
    console.log(`    ${item.articleUrl || item.googleNewsUrl}`);
}
