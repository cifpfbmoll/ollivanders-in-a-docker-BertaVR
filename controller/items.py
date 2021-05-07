from flask import Flask
from flask_restful import Resource, Api
from services.service_mock import Service
import json


class Items(Resource):

    # /item/<name>

    def get(self, name):
        # curl http://localhost:5000/items/name/"Aged+Brie"
        #  El 200 queda comentado porque dificultaba los test y nos ha parecido
        # prescindible ya que es el código por defecto
        return Service.get_item(name)  # , 200
