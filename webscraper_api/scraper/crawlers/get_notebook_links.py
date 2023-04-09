from playwright.sync_api import sync_playwright
from webscraper_api.scraper.helpers.print_color import print_color

PAGE_URL = "https://webscraper.io/test-sites/e-commerce/allinone"


def get_notebook_links():
    print_color("Initializing data search...", color="GREEN")
    notebooks_hrefs = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(PAGE_URL)

            computer_btn = page.get_by_role("link", name="Computers")

            computer_btn.wait_for()

            computer_btn.click()

            laptop_btn = page.get_by_role("link", name="Laptops")
            
            laptop_btn.wait_for()

            laptop_btn.click()

            page.locator('.page-header', has_text="Computers / Laptops").wait_for()

            notebooks = page.locator('h4 a:has-text("Lenovo")')

            notebooks_hrefs.extend(notebooks.evaluate_all("(els) => els.map((el) => el.href)"))

            browser.close()

            return notebooks_hrefs
    except Exception as e:
        print_color(str(e), color="RED")
    finally:
        print_color(f"Found {len(notebooks_hrefs)} notebooks.", color="YELLOW")
