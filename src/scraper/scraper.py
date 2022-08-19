import _thread
from operator import itemgetter

from src.scraper.crawlers.get_notebook_links import get_notebook_links
from src.scraper.crawlers.get_notebooks_infos import get_notebooks_infos
from src.scraper.model_mongo import save_order, save_scraped_data, update_order


class Scraper:
    def __get_notebooks(self):
        note_links = get_notebook_links()
        notebooks_infos = get_notebooks_infos(note_links)
        filtered_by_price = sorted(notebooks_infos, key=itemgetter("price"))
        save_scraped_data(filtered_by_price)

    def __save_order(self):
        return save_order()

    def __update_order(self, order_id):
        return update_order(order_id)

    def scrape(self):
        self.__get_notebooks()

    def scrape_order(self):
        order_id = self.__save_order()
        
        def handler_scrape_order():
            self.__get_notebooks()
            self.__update_order(order_id)

        _thread.start_new_thread(handler_scrape_order, ())
        return order_id
