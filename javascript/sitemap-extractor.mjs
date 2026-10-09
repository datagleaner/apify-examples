// List the page URLs in a website's sitemaps with the Data Gleaner Sitemap URL Extractor.
//
// Store: https://apify.com/datagleaner/sitemap-extractor
// Price: $0.20 per 1,000 URLs ($0.0002 per URL). This run returns at most 10 URLs, so at most $0.002.
//
//   npm install apify-client
//   APIFY_TOKEN=... node sitemap-extractor.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/sitemap-extractor').call({
    websites: ['stripe.com'],
    maxUrlsPerSite: 10,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    console.log(item.url, item.lastmod, item.priority, item.sitemapUrl);
}
