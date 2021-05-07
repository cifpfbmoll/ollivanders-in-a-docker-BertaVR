
import click
from flask import g, current_app as app
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from repository.db_conexion import db
from repository.db_models import Item
from repository.db_sql import DB_sql

def get_DB():
    if db not in g:
        app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:pomeranian@localhost/guildedrose"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   
        db.init_app(app)
        g.db = db
        g.Item = Item
    return g.db


@click.command("inicializar_DB")
@with_appcontext
def init_db_command():
    initDB()
    click.echo('OK, habéis inicializado la DB.')

def init_app(app):
    app.teardown_appcontext(desconectar_db)
    app.cli.add_command(init_db_command)

def initDB():
    db = get_DB()
    db.drop_all()
    db.create_all()
    inventario = DB_sql.inventario
    for item in inventario:
        db.session.add(item)
    db.session.commit()


def desconectar_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.session.close()

