from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from webscraper_api.api.controllers.notebooks import Notebooks
from webscraper_api.api.controllers.scrape import Scrape
from webscraper_api.api.model.db import mongo

load_dotenv()

from os import environ  # noqa: E402


def create_app(db_uri=environ.get("MONGODB_URI")):
    app = Flask(__name__)
    api = Api(app)
    CORS(app)
    app.config["MONGO_URI"] = db_uri
    mongo.init_app(app)
    api.add_resource(Notebooks, "/notebooks")
    api.add_resource(Scrape, "/scrape")
    return app
