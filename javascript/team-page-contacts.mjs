// Company Leadership and Team Page Scraper (Data Gleaner).
//
// Store: https://apify.com/datagleaner/team-page-contacts
// Price: $0.002 per named person found on a company's own site; domains with no team page are free.
// This run takes at most 5 people from each of 2 domains, so it costs at most $0.02.
//
// Run:
//   npm install apify-client
//   APIFY_TOKEN=... node team-page-contacts.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/team-page-contacts').call({
    domains: ['baremetrics.com', 'mongodb.com'],
    maxPeoplePerDomain: 5,
    seniority: ['founder', 'c-level'],
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();

for (const item of items) {
    console.log(`${item.companyName}: ${item.personName}, ${item.jobTitle} (${item.seniority})`);
    console.log('  linkedin:', item.linkedinUrl || '-');
    console.log('  email:   ', item.email || '-');
    console.log('  source:  ', item.sourceUrl);
}
