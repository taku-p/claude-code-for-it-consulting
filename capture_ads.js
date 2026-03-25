const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch({
    args: ['--force-color-profile=srgb']
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 480, deviceScaleFactor: 2 });

  const filePath = path.resolve(__dirname, 'cover_ads.html');
  await page.goto(`file://${filePath}`, { waitUntil: 'networkidle0' });

  await page.screenshot({
    path: path.resolve(__dirname, 'cover_ads.png'),
    fullPage: false
  });

  console.log('cover_ads.png を生成しました');
  await browser.close();
})();
