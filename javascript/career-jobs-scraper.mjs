// Career Site Jobs Scraper (Data Gleaner) - Node.js example.
//
// Store: https://apify.com/datagleaner/career-jobs-scraper
// Price: $0.0015 per job returned (pay per event). This run returns at most
// 10 jobs, so it costs at most $0.015.
//
// Run:
//   npm install apify-client
//   APIFY_TOKEN=... node career-jobs-scraper.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/career-jobs-scraper').call({
    companies: ['https://jobs.lever.co/spotify', 'https://jobs.ashbyhq.com/openai'],
    titleKeywords: ['data'],
    maxJobsPerCompany: 5,
    maxItems: 10,
    includeDescription: false,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const job of items) {
    const pay = job.salary ? `${job.salary.min}-${job.salary.max} ${job.salary.currency}` : 'n/a';
    console.log([job.company, job.title, (job.locations || []).join(', '), pay, job.jobUrl].join(' | '));
}
