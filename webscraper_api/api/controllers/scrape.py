from bson import json_util
from flask import Response, request
from flask_restful import Resource
from webscraper_api.api.services.scrape import ScrapeService
from webscraper_api.api.validations.scraping_is_completed import scraping_is_completed


class Scrape(Resource):
    def get(self):
        order_id = request.args.get("orderId", type=str)
        if order_id is None:
            return Response(
                response=json_util.dumps({"message": "Query orderId is required"}),
                status=400,
            )
        data = ScrapeService().get_scrape_order_by_id(order_id)
        return scraping_is_completed(data)

    def post(self):
        order_id = ScrapeService().post_scrape_order()
        return Response(
            response=json_util.dumps(
                {"message": "Scrape order created!", "order_id": str(order_id)}
            ),
            mimetype="application/json",
            status=201,
        )
