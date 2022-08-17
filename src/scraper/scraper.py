from operator import itemgetter
from .crawlers.get_notebook_links import get_notebook_links
from .crawlers.get_notebooks_infos import get_notebooks_infos
from .helpers.json_handler import save_in_json
from .helpers.set_interval import set_interval

FIVE_MINUTES = 300


class Scraper:
    def __init__(self):
        self.__started = False

    def __get_notebooks(self):
        note_links = get_notebook_links()
        notebooks_infos = get_notebooks_infos(note_links)
        filtered_by_price = sorted(notebooks_infos, key=itemgetter("price"))
        save_in_json(infos=filtered_by_price)

    def start(self):
        if not self.__started:
            timer = set_interval(self.__get_notebooks, FIVE_MINUTES)
            self.timer = timer
            self.__started = True
            print("Scraper started")
        else:
            print("Scraper is already started")

    def stop(self):
        if self.__started:
            self.timer.cancel()
            self.__started = False
            print("Scraper stopped")
        else:
            print("Scraper is not started")

    def is_started(self):
        return self.__started
