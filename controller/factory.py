from flask import Flask
from flask_restful import Resource, Api
from controller.items import Items
from controller.objeto import Objeto


def create_app():

    app = Flask(__name__)
    api = Api(app)

    class WelcomeOllivanders(Resource):
        def get(self):
            return {"Hello": "Ollivanders"}

    api.add_resource(WelcomeOllivanders, "/")
    api.add_resource(Items, "/items/<name>")
    api.add_resource(Objeto, "/objeto/<name>")

    return app
