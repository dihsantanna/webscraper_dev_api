import _thread

from bson import json_util
from dotenv import load_dotenv
from flask import Flask, Response
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_restful import Api, Resource
from scraper.scraper import Scraper

load_dotenv()

from os import environ

app = Flask(__name__)
api = Api(app)
CORS(app)
app.config["MONGO_URI"] = environ["MONGODB_URI"]
mongo = PyMongo(app)


class Notebooks(Resource):
    def get(self):
        data = mongo.db.notebook_lenovo.find()
        return Response(json_util.dumps(data), mimetype="application/json")


class Scrape(Resource):
    def put(self):
        scraper = Scraper()
        _thread.start_new_thread(scraper.scrape, ())
        return {"message": "Scraping started!"}, 202


api.add_resource(Notebooks, "/notebooks")
api.add_resource(Scrape, "/scrape")
