from playwright.sync_api import sync_playwright
from src.scraper.helpers.print_color import print_color

PAGE_URL = "https://webscraper.io/test-sites/e-commerce/allinone"


def get_notebook_links():
    print_color("Initializing data search...", color="GREEN")
    notebooks_hrefs = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(PAGE_URL)

            page.locator("xpath=/html/body/div[1]/div[2]/div/div/div/h1").wait_for()

            page.locator('xpath=//*[@id="side-menu"]/li[2]/a').click()

            page.locator("xpath=/html/body/div[1]/div[3]/div/div[2]/h1").wait_for()

            page.locator('xpath=//*[@id="side-menu"]/li[2]/ul/li[1]/a').click()

            page.locator("xpath=/html/body/div[1]/div[3]/div/div[2]/h1").wait_for()

            notebooks = page.locator('h4 a:has-text("Lenovo")')

            notebooks_hrefs.extend(notebooks.evaluate_all("(els) => els.map((el) => el.href)"))

            browser.close()

            return notebooks_hrefs
    except Exception as e:
        print_color(e, color="RED")
    finally:
        print_color(f"Found {len(notebooks_hrefs)} notebooks.", color="YELLOW")
