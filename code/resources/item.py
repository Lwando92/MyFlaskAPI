# import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('price', type=float,
                        required=True,
                        help="This field is required"
                        )

    parser.add_argument('store_id', type=int,
                        required=True,
                        help="This field is required"
                        )

    # @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': " Item not found"}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {
                'message': "An item with name '{}' already exists.".format(name)}

        data = Item.paser.parse_args()

        item = ItemModel(name, data['price'], data['stored_id'])
        try:
            ItemModel.insert()
        except BaseException:
            return {"message": " An error occurred while inserting"}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
                item.delete_from_db()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = " DELETE FROM items WHERE=?"
        # cursor.execute(query, (name,))

        # connection.commit()
        # connection.close()

        return {'message': 'Item Deleted'}

    def put(self, name):
        # data = request.get_json()
        data = Item.paser.parse_args()

        # item = ItemModel.find_by_name(name)
        # updated_item = ItemModel(name, data['price'])

        if item is None:
            # updated_item.insert()
            item =  ItemModel(name, data['price'], data['store_id'])
        else:

            item.price = data['price']
            item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items"

        # results = cursor.execute(query)
        # items = []
        # for row in results:
        #     items.append({'name': row[0], 'price': row[1]})

        # connection.close()

        # return {'items': items}
