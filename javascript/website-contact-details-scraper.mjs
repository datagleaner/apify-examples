// Extract emails, phones and social profiles from websites with Data Gleaner's
// Website Contact Details Scraper: https://apify.com/datagleaner/website-contact-details-scraper
//
// Price: US$4.00 per 1,000 websites with contacts (US$0.004 each); sites with no
// contacts are free. The Actor returns one item per input website, so the 3-site
// list below caps the run at 3 items and costs at most about US$0.012.
//
// Run: npm install apify-client && APIFY_TOKEN=... node website-contact-details-scraper.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/website-contact-details-scraper').call({
    websites: ['https://www.appier.com', 'stripe.com', 'https://www.sakura.ad.jp'],
    maxPagesPerSite: 5,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    console.log(`${item.website} -> ${item.status}`);
    console.log('  company: ', item.companyName);
    console.log('  emails:  ', (item.emails || []).map((e) => e.value));
    console.log('  phones:  ', (item.phones || []).map((p) => p.value));
    console.log('  linkedin:', ((item.socials || {}).linkedin || []).map((s) => s.url));
}
