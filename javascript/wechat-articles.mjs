// WeChat Articles Scraper (Data Gleaner) - public 微信公众号 articles as text and Markdown.
//
// Store: https://apify.com/datagleaner/wechat-articles
// Price: $5 per 1,000 articles (pay per event). This run fetches at most 5, about $0.025.
//
// Run:  npm install apify-client
//       APIFY_TOKEN=... node wechat-articles.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/wechat-articles').call({
    searchKeywords: ['新能源汽车'],
    maxArticles: 5,
    includeContent: ['markdown'],
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    console.log(`${item.publishedAt} | ${item.accountName} | ${item.title}`);
    console.log(`   ${item.url}`);
    console.log(`   ${(item.contentMarkdown || '').slice(0, 200).replace(/\n/g, ' ')}`);
}
