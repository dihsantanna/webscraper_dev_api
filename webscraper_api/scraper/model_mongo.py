from datetime import datetime

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

from os import environ  # noqa: E402


def save_scraped_data(data):
    with MongoClient(environ["MONGODB_URI"]) as client:
        db = client["webscraper"]

        db.drop_collection("notebook_lenovo")

        collection = db["notebook_lenovo"]
        collection.insert_many(data)


def save_order():
    with MongoClient(environ["MONGODB_URI"]) as client:
        db = client["webscraper"]

        collection = db["scrape_order"]
        result = collection.insert_one({"start": datetime.utcnow(), "end": None})
        return result.inserted_id


def update_order(order_id):
    with MongoClient(environ["MONGODB_URI"]) as client:
        db = client["webscraper"]

        collection = db["scrape_order"]
        collection.update_one({"_id": order_id}, {"$set": {"end": datetime.utcnow()}})
