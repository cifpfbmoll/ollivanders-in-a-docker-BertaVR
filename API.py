from flask import Flask, request, flash, redirect, url_for, jsonify, request
from flask_restful import Resource, Api
import os
from flask_sqlalchemy import SQLAlchemy
from controller.items import Items
from controller.objeto import Objeto
from repository import db_inicializar
from services.services import Services

app = Flask(__name__)
api = Api(app)
db_inicializar.init_app(app)


@app.route('/items/delete/<itemName>/')
def delete_item(itemName):
    return Services.delete_item(itemName)

@app.route('/item/' , methods=['POST']) #faltan las claves valor (ruta) libro flask
def post_item():
    return Services.post()

@app.route('/items/')
def show_items():
    return Services.get_items()
    
@app.route('/item/<itemName>')
def show_item(itemName):
    return Services.get_item(itemName)





class WelcomeOllivanders(Resource):
    def get(self):
        return {"Hello": "Ollivanders"}


api.add_resource(WelcomeOllivanders, "/")
# api.add_resource(Items, "/item")
#api.add_resource(Objeto, "/objeto/<name>")

if __name__ == "__main__":
    app.run(debug=True)
