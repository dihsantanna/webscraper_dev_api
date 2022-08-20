from bson import json_util
from flask import Response
from flask_restful import Resource
from webscraper_api.api.services.notebook import NotebookService


class Notebooks(Resource):
    def get(self):
        data = NotebookService().get_all_notebooks()
        return Response(json_util.dumps(data))
