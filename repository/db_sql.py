from flask import Flask, json, jsonify, Response
from flask_restful import Resource, Api, marshal_with, abort, fields
import os
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from flask import g
from repository.db_models import Item


resource_fields = {
    'name': fields.String,
    'sell_in': fields.Integer,
    'quality': fields.Integer

}

class DB_sql:

    inventario = [Item(name="Aged Brie",sell_in=3, quality=4),
                  Item(name="Backstage", sell_in=2, quality=6),
                  Item(name="Sulfuras", sell_in=80,  quality=0),
                  Item(name="Conjured Mana Cake", sell_in=4, quality=2),
                  Item(name="Sulfuras", sell_in=80, quality= 0),
                  Item(name="Sulfuras", sell_in=80, quality=0), 
                  Item(name="Conjured Mana Cake", sell_in=5,  quality=3),
                  Item(name="Aged Brie", sell_in=-3, quality=5)]
