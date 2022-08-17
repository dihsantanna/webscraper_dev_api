from playwright.sync_api import sync_playwright

PAGE_URL = "https://webscraper.io/test-sites/e-commerce/allinone"


def get_notebook_links():
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

        notebooks_hrefs = notebooks.evaluate_all("(els) => els.map((el) => el.href)")

        browser.close()

        return notebooks_hrefs
