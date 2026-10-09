// Google Hotels Scraper by Data Gleaner: hotel prices for your exact dates.
//
// Store page: https://apify.com/datagleaner/google-hotels-scraper
// Price: $3.00 per 1,000 hotels ($0.003 per hotel). This run returns at most 10 hotels (about $0.03).
//
// Usage:
//   npm install apify-client
//   APIFY_TOKEN=your_token node google-hotels-scraper.mjs
import { ApifyClient } from 'apify-client';

const day = 24 * 60 * 60 * 1000;
const checkIn = new Date(Date.now() + 30 * day).toISOString().slice(0, 10);
const checkOut = new Date(Date.now() + 32 * day).toISOString().slice(0, 10);

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('datagleaner/google-hotels-scraper').call({
    locations: ['Tokyo'],
    checkIn,
    checkOut,
    adults: 2,
    currency: 'USD',
    maxHotelsPerLocation: 10,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const hotel of items) {
    const firstOffer = hotel.offers?.[0]?.provider ?? '-';
    console.log(`${hotel.name} | rating ${hotel.rating} | ${hotel.lowestPrice} ${hotel.currency}/night | first offer: ${firstOffer}`);
}
