from bson import ObjectId
from webscraper_api.api.model.db import mongo
from webscraper_api.scraper.scraper import Scraper


class ScrapeService:
    def get_scrape_order_by_id(self, order_id):
        try:
            return mongo.db.scrape_order.find_one({"_id": ObjectId(order_id)})
        except Exception:
            return None

    def post_scrape_order(self):
        order_id = Scraper().scrape_order()
        return order_id
