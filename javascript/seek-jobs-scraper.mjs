// SEEK Job Scraper (Data Gleaner) - scrape SEEK Australia & New Zealand job listings.
//
// Store: https://apify.com/datagleaner/seek-jobs-scraper
// Price: $0.80 per 1,000 jobs ($0.0008 per job), full descriptions included.
// This example fetches at most 10 jobs, which costs under one cent.
//
// Run:
//   npm install apify-client
//   APIFY_TOKEN=your_token node seek-jobs-scraper.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/seek-jobs-scraper').call({
    keywords: ['registered nurse'],
    country: 'NZ',
    location: 'Auckland',
    maxJobsPerSearch: 10,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const job of items) {
    console.log([job.title, job.companyName, job.salaryLabel, job.location, job.url].join(' | '));
}
