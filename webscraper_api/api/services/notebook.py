from webscraper_api.api.model.db import mongo


class NotebookService:
    def get_all_notebooks(self):
        return mongo.db.notebook_lenovo.find()
