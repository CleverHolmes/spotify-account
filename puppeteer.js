import puppeteer from 'puppeteer';

// const browser = await puppeteer.launch();
// const browser = await puppeteer.launch({headless: true});
// const browser = await puppeteer.launch({headless: 'new'});
const browser = await puppeteer.launch({ headless: false });
const page = await browser.newPage();

// // Navigate the page to a URL
await page.goto('https://www.spotify.com/signup');

// // Set screen size
// await page.setViewport({ width: 1080, height: 1024 });

// // Type into search box
// await page.type('.search-box__input', 'automate beyond recorder');

const email = 'your_emasdfsdfxcvxcvil@gmail.com';
const password = 'your_password';
const username = 'your_username';
const birthMonth = '2'; // Replace with the desired month
const birthYear = '1990'; // Replace with the desired year
const gender = '1'; // Replace with 'male' or 'female'

// Fill out the form
await page.type('#username', email);
console.log('Input email');

await page.click('button[data-testid="submit"]');
console.log('Next');
await page.waitForTimeout(1000);

await page.type('#password', password);
console.log('Input password');
await page.click('button[data-testid="submit"]');
console.log('Next');
await page.waitForTimeout(1000);

await page.type('input[name="displayName"]', username);
console.log('Input username');

await page.select('select[name="birthMonth"]', birthMonth);
await page.type('input[name="birthYear"]', birthYear);
console.log('Input birth month and year');

await page.click(`label[for="${gender}"]`);
console.log('Input gender');

await page.click('button[data-testid="submit"]');
console.log('Next');
await page.waitForTimeout(1000);

await page.click('button[data-testid="submit"]');
console.log('Next');

// Wait for the page to load (replace the URL with the correct URL)
while (page.url() === 'https://www.spotify.com/us/signup#step=3') {
    await page.waitForTimeout(2000);
}

await page.waitForTimeout(5000); // Wait for 5 seconds