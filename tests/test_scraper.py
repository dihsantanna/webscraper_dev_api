from webscraper_api.scraper.crawlers.get_notebook_links import get_notebook_links
from webscraper_api.scraper.crawlers.get_notebooks_infos import get_notebooks_infos

from tests.mocks.notebooks_hrefs import notebooks_hrefs


def test_get_notebook_links():
    notebooks_hrefs = get_notebook_links()
    assert len(notebooks_hrefs) > 0
    assert type(notebooks_hrefs) == list


def test_get_notebooks_infos():
    notebooks_infos = get_notebooks_infos(notebooks_hrefs)
    assert len(notebooks_infos) == 5
    assert type(notebooks_infos) == list
