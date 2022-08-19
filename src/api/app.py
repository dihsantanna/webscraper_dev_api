from bson import ObjectId, json_util
from dotenv import load_dotenv
from flask import Flask, Response, request
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_restful import Api, Resource
from src.api.validations.scraping_completed import scraping_completed
from src.scraper.scraper import Scraper

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
        return Response(json_util.dumps(data))


class Scrape(Resource):
    def get(self):
        order_id = request.args.get("orderId", type=str)
        if order_id is None:
            return Response(
                response=json_util.dumps({"message": "Query orderId is required"}),
                status=400,
            )
        data = mongo.db.scrape_order.find_one({"_id": ObjectId(order_id)})
        return scraping_completed(data)

    def post(self):
        scraper = Scraper()
        order_id = scraper.scrape_order()
        return Response(
            response=json_util.dumps(
                {"message": "Scrape order created!", "order_id": str(order_id)}
            ),
            mimetype="application/json",
            status=201,
        )


api.add_resource(Notebooks, "/notebooks")
api.add_resource(Scrape, "/scrape")
