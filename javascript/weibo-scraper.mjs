// Run the Data Gleaner Weibo Scraper and print a few fields of each post.
//
// Store page: https://apify.com/datagleaner/weibo-scraper
// Price: $3 per 1,000 posts ($0.003 per post). This run fetches at most 10 posts, so about $0.03.
//
//   npm install apify-client
//   APIFY_TOKEN=... node weibo-scraper.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/weibo-scraper').call({
    searchQueries: ['瑞幸'],
    maxItemsPerQuery: 10,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();

for (const item of items) {
    const author = item.author?.screenName;
    const text = (item.text ?? '').replace(/\n/g, ' ').slice(0, 80);
    console.log(`${item.createdAt}  likes=${item.likesCount}  @${author}  ${text}`);
    console.log(`    ${item.url}`);
}
