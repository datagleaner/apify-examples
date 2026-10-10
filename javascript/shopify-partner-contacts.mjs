// Shopify Partner and Agency Contacts (Data Gleaner).
//
// Store: https://apify.com/datagleaner/shopify-partner-contacts
// Price: $0.005 per partner with a public email or phone; partners with neither are free.
// This run takes at most 10 partners in Germany, so it costs at most $0.05.
//
// Run:
//   npm install apify-client
//   APIFY_TOKEN=... node shopify-partner-contacts.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/shopify-partner-contacts').call({
    countries: ['de'],
    maxPartners: 10,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();

for (const item of items) {
    console.log(`${item.partnerName} (${item.city}, ${item.country}), tier ${item.partnerTier || '-'}`);
    console.log('  email:  ', item.email || '-');
    console.log('  phone:  ', item.phone || '-');
    console.log('  website:', item.website || '-');
}
