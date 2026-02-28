import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        grand_total = 0
        
        seeds = range(86, 96)
        for seed in seeds:
            url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
            print(f"Scraping seed {seed}...")
            await page.goto(url)
            
            # Wait for the table to actually appear on the screen
            await page.wait_for_selector('td')
            
            # Find all table cells and grab the numbers inside them
            cells = await page.query_selector_all('td')
            for cell in cells:
                text = await cell.inner_text()
                try:
                    # Clean the text and convert to a number
                    num = float(text.strip())
                    grand_total += num
                except ValueError:
                    continue
                    
        print(f"\nFINAL GRAND TOTAL: {int(grand_total)}")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())

