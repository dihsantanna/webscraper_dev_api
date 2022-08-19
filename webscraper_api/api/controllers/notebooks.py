import json

from flask import Response
from flask_restful import Resource
from webscraper_api.api.model.db import mongo


class Notebooks(Resource):
    def get(self):
        data = mongo.db.notebook_lenovo.find()
        return Response(json.dumps(data))
