// Get the latest posts of a public Telegram channel with the Data Gleaner Telegram Channel Scraper.
//
// Store: https://apify.com/datagleaner/telegram-channel-scraper
// Price: $0.50 per 1,000 messages ($0.0005 per message) and $0.001 per channel info row.
// This run returns at most 10 messages and 1 channel row, so at most $0.006.
//
//   npm install apify-client
//   APIFY_TOKEN=... node telegram-channel-scraper.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/telegram-channel-scraper').call({
    channels: ['durov'],
    maxMessagesPerChannel: 10,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    if (item.type === 'channel') {
        console.log('Channel:', item.title, '-', item.subscribers, 'subscribers');
    } else {
        console.log(item.url, item.date, item.views, (item.text || '').slice(0, 80));
    }
}
