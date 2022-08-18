from operator import itemgetter

from scraper.model_mongo import save_scraped_data

from .crawlers.get_notebook_links import get_notebook_links
from .crawlers.get_notebooks_infos import get_notebooks_infos


class Scraper:
    def __get_notebooks(self):
        note_links = get_notebook_links()
        notebooks_infos = get_notebooks_infos(note_links)
        filtered_by_price = sorted(notebooks_infos, key=itemgetter("price"))
        save_scraped_data(filtered_by_price)

    def scrape(self):
        self.__get_notebooks()
