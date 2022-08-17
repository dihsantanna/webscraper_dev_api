from operator import itemgetter
from .crawlers.get_notebook_links import get_notebook_links
from .crawlers.get_notebooks_infos import get_notebooks_infos
from .helpers.json_handler import save_in_json


class Scraper:
    def __get_notebooks(self):
        note_links = get_notebook_links()
        notebooks_infos = get_notebooks_infos(note_links)
        filtered_by_price = sorted(notebooks_infos, key=itemgetter("price"))
        save_in_json(infos=filtered_by_price)

    def scrape(self):
        self.__get_notebooks()
