// YouTube Channel Email Scraper and Influencer Contact Finder (Data Gleaner).
//
// Store: https://apify.com/datagleaner/youtube-channel-contacts
// Price: $0.015 per channel where a public email was found; channels with no email are free.
// This run takes at most 5 channels from one keyword search, so it costs at most $0.075.
//
// Run:
//   npm install apify-client
//   APIFY_TOKEN=... node youtube-channel-contacts.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/youtube-channel-contacts').call({
    searchKeywords: ['fitness coach'],
    maxChannelsPerKeyword: 5,
    followLinks: true,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();

for (const item of items) {
    if (item.status !== 'ok') {
        console.log('error:', item.input, item.error);
        continue;
    }
    const emails = (item.emails || []).map((e) => e.email);
    console.log(`${item.title} (${item.handle}), ${item.subscribers} subscribers`);
    console.log('  emails: ', emails.join(', ') || '-');
    console.log('  website:', item.website || '-');
    console.log('  socials:', Object.entries(item.socials || {}).map(([k, v]) => `${k}=${v}`).join(', ') || '-');
}
