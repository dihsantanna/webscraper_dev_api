from pymongo import MongoClient

MONGO_URI = f"mongodb://localhost:27017"


def save_scraped_data(data):
    with MongoClient(MONGO_URI) as client:
        db = client["webscraper"]

        db.drop_collection("notebook_lenovo")

        collection = db["notebook_lenovo"]
        collection.insert_many(data)
