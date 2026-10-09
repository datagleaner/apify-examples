// Convert web pages to clean, LLM-ready Markdown with the Data Gleaner Web to Markdown Actor.
//
// Store: https://apify.com/datagleaner/web-to-markdown
// Price: $1 per 1,000 pages ($0.001 per page that returns content; failed URLs are free).
// This run fetches 3 URLs plus at most 2 search results, so at most 5 pages and $0.005.
//
//   npm install apify-client
//   APIFY_TOKEN=... node web-to-markdown.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/web-to-markdown').call({
    urls: [
        'https://en.wikipedia.org/wiki/Markdown',
        'https://docs.python.org/3/tutorial/introduction.html',
        'https://www.paulgraham.com/greatwork.html',
    ],
    query: 'model context protocol',
    maxResults: 2,
    maxCharsPerPage: 2000,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    if (item.error) {
        console.log(item.url, 'ERROR:', item.error);
        continue;
    }
    console.log(item.url, '|', item.title, '|', item.wordCount, 'words via', item.fetchedVia);
    console.log((item.markdown || '').slice(0, 200).replace(/\n/g, ' '));
    console.log();
}
