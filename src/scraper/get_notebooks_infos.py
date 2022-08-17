from playwright.sync_api import sync_playwright

PAGE_URI = "https://webscraper.io"


def get_notebooks_infos(note_links):
    note_infos = []
    for link in note_links:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(link)
            page.locator("xpath=/html/body/div[1]/div[2]/div/div/div/h1").wait_for()

            title = page.locator(
                "xpath=/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[2]"
            ).inner_text()

            description = page.locator("div.caption .description").inner_text()

            imgSrc = page.locator(
                "xpath=/html/body/div[1]/div[3]/div/div[2]/div/div/div[1]/img"
            ).get_attribute("src")

            price = page.locator("div.caption .price").inner_text()

            hdd_content = page.locator(
                "xpath=/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[2]"
            )

            hdd = hdd_content.locator("role=button[disabled=false]").evaluate_all(
                "(els) => els.filter(el => !el.className.includes('disabled')).map(el => el.innerText)"
            )

            rating = page.locator(
                "xpath=/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[3]"
            )

            qty_reviews = rating.locator("p").inner_text()

            qty_starts = rating.locator("span.glyphicon-star").evaluate_all(
                "(stars) => stars.length"
            )

            note_info = {
                "title": title,
                "description": description,
                "imgSrc": PAGE_URI + imgSrc,
                "price": float(price.replace("$", "")),
                "hdd": hdd,
                "rating": {
                    "qty_reviews": int(qty_reviews.strip(" reviews")),
                    "qty_starts": int(qty_starts),
                },
            }

            note_infos.append(note_info)

            browser.close()

    return note_infos
