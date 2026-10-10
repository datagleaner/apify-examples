// App Developer Email Finder for Google Play, the App Store, Steam and the Chrome Web Store (Data Gleaner).
//
// Store: https://apify.com/datagleaner/app-developer-email-finder
// Price: $0.0015 per app whose developer has a public email; apps without one are free.
// This run takes at most 5 Google Play apps for one keyword, so it costs at most $0.0075.
//
// Run:
//   npm install apify-client
//   APIFY_TOKEN=... node app-developer-email-finder.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/app-developer-email-finder').call({
    searchKeywords: ['habit tracker'],
    stores: ['googlePlay'],
    maxAppsPerKeyword: 5,
    onlyWithEmail: true,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();

for (const item of items) {
    console.log(`${item.appName} (${item.store}) by ${item.developerName}`);
    console.log('  email:  ', item.developerEmail || '-');
    console.log('  website:', item.developerWebsite || '-');
    console.log('  privacy:', item.privacyPolicyUrl || '-');
}
