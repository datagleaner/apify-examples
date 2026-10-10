// Researcher Email Finder: PubMed authors by topic (Data Gleaner).
//
// Store: https://apify.com/datagleaner/researcher-email-finder
// Price: $0.005 per researcher returned with a published email; researchers without one are free.
// This run returns at most 10 researchers, so it costs at most $0.05.
//
// Run:
//   npm install apify-client
//   APIFY_TOKEN=... node researcher-email-finder.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/researcher-email-finder').call({
    queries: ['crispr base editing'],
    yearFrom: 2024,
    maxResearchers: 10,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();

for (const item of items) {
    console.log(`${item.name}, ${item.institution || '-'} (${item.country || '-'})`);
    console.log('  email:', item.email);
    console.log('  orcid:', item.orcidUrl || '-');
}
