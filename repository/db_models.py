from repository.db_conexion import db

class Item(db.Model):
    __tablename__ = 'Inventario'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False)
    sell_in = db.Column(db.Integer, nullable=False)
    quality = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return '<User %r>' % self.name

    def __init__(self, name,  sell_in, quality):

        self.name = name
        self.sell_in = sell_in
        self.quality = quality

