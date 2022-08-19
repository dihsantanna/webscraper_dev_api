import json
from http import HTTPStatus as status

from flask import Response


def scraping_is_completed(data):
    if not data:
        return Response(
            response=json.dumps({"message": "Scraping order does not exist"}),
            status=status.NOT_FOUND,
        )
    elif not data["end"]:
        return Response(
            response=json.dumps({"message": "Scraping order is not completed"}), status=status.OK
        )
    else:
        return Response(
            response=json.dumps({"message": "Scraping order already completed"}), status=status.OK
        )
