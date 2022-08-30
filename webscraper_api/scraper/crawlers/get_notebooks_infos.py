from playwright.sync_api import sync_playwright

from ..helpers.print_color import print_color

PAGE_URI = "https://webscraper.io"


def get_notebooks_infos(note_links):
    note_infos = []
    qty_notebooks = len(note_links)
    print_color("Searching for information from found notebooks...", color="GREEN")
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            for i, link in enumerate(note_links):
                page.goto(link)
                page.locator("xpath=/html/body/div[1]/div[2]/div/div/div/h1").wait_for()

                title = page.locator(
                    "xpath=/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[2]"
                ).inner_text()

                description = page.locator("div.caption .description").inner_text()

                img_src = page.locator(
                    "xpath=/html/body/div[1]/div[3]/div/div[2]/div/div/div[1]/img"
                ).get_attribute("src")

                rating = page.locator(
                    "xpath=/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[3]"
                )

                qty_reviews = rating.locator("p").inner_text()

                qty_stars = rating.locator("span.glyphicon-star").evaluate_all(
                    "(stars) => stars.length"
                )

                hdds_size = page.locator("div.swatches > button.swatch").all_inner_texts()

                price_for_hdd = dict()

                for hddBtnText in hdds_size:
                    hddBtn = page.locator("div.swatches > button.swatch", has_text=hddBtnText)
                    if hddBtn.evaluate("(el) => el.className.includes('disabled')"):
                        continue

                    hddBtn.click()
                    price = page.locator("div.caption .price").text_content()
                    price_for_hdd[hddBtnText] = {"price": float(price.replace("$", ""))}

                note_info = {
                    "title": title,
                    "description": description,
                    "img_src": PAGE_URI + img_src,
                    "price_for_hdd": price_for_hdd,
                    "rating": {
                        "qty_reviews": int(qty_reviews.strip(" reviews")),
                        "qty_stars": int(qty_stars),
                    },
                }

                note_infos.append(note_info)

                print_color(
                    f"Notebook {i + 1} of {qty_notebooks} scraped.",
                    color="YELLOW",
                )

            browser.close()

        print_color("Scraping completed!", color="GREEN")

        return note_infos
    except Exception as e:
        print_color(str(e), color="RED")
