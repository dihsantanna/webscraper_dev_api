from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

from .services.scrape_data import scrape_data
from .services.get_notebooks import get_notebooks

app = Flask(__name__)
api = Api(app)
CORS(app)


class Notebooks(Resource):
    def get(self):
        data = get_notebooks()
        return data


class Scrape(Resource):
    def put(self):
        return scrape_data()


api.add_resource(Notebooks, "/notebooks")
api.add_resource(Scrape, "/scrape")
