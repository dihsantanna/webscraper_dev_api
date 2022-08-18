from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource

from .services.get_notebooks import get_notebooks

app = Flask(__name__)
api = Api(app)
CORS(app)


class Notebooks(Resource):
    def get(self):
        data = get_notebooks()
        return data


api.add_resource(Notebooks, "/notebooks")
