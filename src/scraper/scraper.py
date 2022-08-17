from get_notebook_links import get_notebook_links
from get_notebooks_infos import get_notebooks_infos
from json_handler import save_in_json
from helpers.set_interval import set_interval

PATH = "data/notebooks_infos.json"
FIVE_MINUTES = 300


class Scraper:
    def __init__(self):
        self.started = False

    def __get_notebooks(self):
        note_links = get_notebook_links()
        notebooks_infos = get_notebooks_infos(note_links)
        filtered_by_price = sorted(notebooks_infos, key="price")
        save_in_json(infos=filtered_by_price, path=PATH)

    def start(self):
        if not self.started:
            timer = set_interval(self.__get_notebooks, FIVE_MINUTES)
            self.timer = timer
            self.started = True
            print("Scraper started")
        else:
            print("Scraper is already started")

    def stop(self):
        if self.started:
            self.timer.cancel()
            self.started = False
            print("Scraper stopped")
        else:
            print("Scraper is not started")
