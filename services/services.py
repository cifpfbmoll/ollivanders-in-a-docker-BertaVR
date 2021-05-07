from repository.db_inicializar import get_DB
from repository.db_models import Item
from flask_restful import abort, reqparse
from flask.json import jsonify
from flask import g

class Services():
    @staticmethod
    def get_items():
        db = get_DB()
        items = db.session.query(Item).all()
        inventario = []
        for item in items:
            item_json = {'name': item.name,
                         'sell_in': item.sell_in, 'quality': item.quality}
            inventario.append(item_json)
        return {'items': inventario}

    # @staticmethod
    # def updateQuality():
    #     db = g.db
    #     for item in g.Item.objects():
    #         item_object = Item(
    #             [item.name, item.sell_in, item.quality])
    #         item_object.update_quality()
    #         item.sell_in = item_object.sell_in
    #         item.quality = item_object.quality
    #         item.save()
    #     return Item

    @staticmethod
    def get_item(itemName):
        db = get_DB()
        if not itemName:
            abort(404, description="Es necesario el nombre del item")
        item = Item.query.filter_by(name=itemName).first()
        if not item:
            abort(404, description="El item {} no existe".format(itemName))
        return jsonify(name=item.name, quality=item.quality, sell_in=item.sell_in)

    @staticmethod
    def delete_item(itemName):
        db = get_DB()
        if not itemName:
            abort(404, description="Es necesario el nombre del item")
        item = db.session.query(Item).filter_by(name=itemName).first() ##id, vale vamos al ORM y le decimos que borre este item (en base al id)
        if not item:
            abort(404, description="El item {} no existe".format(itemName))
        db.session.query(Item).filter_by(id=item.id).delete() ##mejor usar el ORM         
        db.session.commit()
        return 'Objeto borrado'

    @staticmethod
    def postItem(args):
        db = get_DB()
        item = g.Item(name = args['name'], sell_in = args['sell_in'], quality = args['quality'])
        db.session.add(item)
        db.session.commit()
        
    @staticmethod
    def post(self):
        # curl -d name="Conjured Mana Cake" -d sell_in=3 -d quality=6
        # http://127.0.0.1:5000/items -X POST
        args_content = self.parseRequest()
        self.postItem(args_content)
        return 'Éxito', 201

    def delete(self):
        # curl -d name="Conjured Mana Cake" -d sell_in=3 -d quality=6
        # http://127.0.0.1:5000/items -X DELETE
        args_content = self.parseRequest()
        Services.deleteItem(args_content)
        return 'Borrado', 204

    def parseRequest(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("name", type=str, required=True,
                            help='name requerido')
        parser.add_argument("sell_in", type=int, required=True,
                            help='sellIn requerido')
        parser.add_argument("quality", type=int, required=True,
                            help='quality requerido')

        return parser.parse_args()
