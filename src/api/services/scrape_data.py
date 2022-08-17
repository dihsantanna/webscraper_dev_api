from http import HTTPStatus as status
from scraper.scraper import Scraper

STARTED_MSG = "Scraper started."


def scrape_data():
    try:
        scraper = Scraper()
        scraper.scrape()
        return {"message": STARTED_MSG}, status.ACCEPTED
    except Exception:
        return {"message": "Internal server error"}, status.INTERNAL_SERVER_ERROR
