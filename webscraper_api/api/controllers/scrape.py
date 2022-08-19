import json

from bson import ObjectId
from flask import Response, request
from flask_restful import Resource
from webscraper_api.api.model.db import mongo
from webscraper_api.api.validations.scraping_is_completed import scraping_is_completed
from webscraper_api.scraper.scraper import Scraper


class Scrape(Resource):
    def get(self):
        order_id = request.args.get("orderId", type=str)
        if order_id is None:
            return Response(
                response=json.dumps({"message": "Query orderId is required"}),
                status=400,
            )
        data = mongo.db.scrape_order.find_one({"_id": ObjectId(order_id)})
        return scraping_is_completed(data)

    def post(self):
        scraper = Scraper()
        order_id = scraper.scrape_order()
        return Response(
            response=json.dumps({"message": "Scrape order created!", "order_id": str(order_id)}),
            mimetype="application/json",
            status=201,
        )
