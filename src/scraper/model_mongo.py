from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

from os import environ


def save_scraped_data(data):
    with MongoClient(environ["MONGODB_URI"]) as client:
        db = client["webscraper"]

        db.drop_collection("notebook_lenovo")

        collection = db["notebook_lenovo"]
        collection.insert_many(data)
