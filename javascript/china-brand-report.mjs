// Run the Data Gleaner China Brand Report and print the summary and a few posts.
//
// Store page: https://apify.com/datagleaner/china-brand-report
// Price: $4.99 per report, charged once when the report is saved (posts, CSV and
// translations included; a run that finds no discussion is not charged). The small
// limits below keep the run short, but the report price is the same.
//
//   npm install apify-client
//   APIFY_TOKEN=... node china-brand-report.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/china-brand-report').call({
    brand: 'Starbucks',
    keywords: ['星巴克'],
    days: 1,
    maxWeiboPosts: 50,
    maxBilibiliVideos: 10,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
const [report, ...posts] = items;
if (!report) throw new Error('No output; check the run log in the Apify Console.');

console.log(`${report.brand}:`, report.counts);
console.log('Weibo sentiment:', report.sentiment?.weibo);
console.log(`Report: ${report.reportUrl}`);
for (const post of report.topWeiboPosts ?? []) {
    console.log(`  engagement=${post.engagement}  ${(post.textEn ?? post.text ?? '').slice(0, 80)}`);
}

for (const item of posts.slice(0, 10)) {
    const text = (item.text ?? '').replace(/\n/g, ' ').slice(0, 60);
    console.log(`${item.platform}  ${item.publishedAt}  likes=${item.likes}  ${text}`);
    console.log(`    ${item.url}`);
}
