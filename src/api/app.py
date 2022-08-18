from bson import json_util
from dotenv import load_dotenv
from flask import Flask, Response
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_restful import Api, Resource

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


api.add_resource(Notebooks, "/notebooks")
