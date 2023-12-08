import asyncio
from pyppeteer import launch


const puppeteer = require('puppeteer');

async function htmlToPdf(htmlFilePath, pdfFilePath) {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    page.on('console', message => console.log('Browser console:', message.text()));

    await page.goto(`file://${htmlFilePath}`, {waitUntil: 'networkidle0'});
    await page.screenshot({ path: 'screenshot.png' }); // For debugging
    await page.pdf({ path: pdfFilePath, format: 'A4' });

    await browser.close();
}


# List of HTML files
html_files = [
    r"F:\PlannerGenerator\PlannerGenHTML\chatgpt\cover.html",
    r"F:\PlannerGenerator\PlannerGenHTML\chatgpt\index.html",
    r"F:\PlannerGenerator\PlannerGenHTML\chatgpt\year_1.html",
]

# Output PDF file
output_pdf = r"F:\PlannerGenerator\PlannerGenHTML\chatgpt\pyppeteeroutput.pdf"

asyncio.get_event_loop().run_until_complete(html_to_pdf(html_files, output_pdf))
