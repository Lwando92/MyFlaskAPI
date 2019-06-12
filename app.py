import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secret"
api = Api(app)

# @app.before_first_request
# def create_tables():
#     db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)


# stores = [
#     {
#         'name': 'My lovely Store',
#         'items':
#     }
# ]


# @app.route("/")
# def home():
#     return render_template('index.html')
# # POST /store data:{name}
# @app.route('/store', methods=['POST'])
# def create_store():
#     request_data = request.get_json()
#     new_store = {
#         'name': request_data['name'],
#         'items': []
#     }
#     stores.append(new_store)
#     return jsonify(new_store)


# # GET /store/<string: name>
# @app.route('/store/<string:name>')
# def get_store(name):
#     for store in stores:
#         if store['name'] == name:
#             return jsonify(store)
#         return jsonify({'message':' Store not found'})


# # GET /store
# @app.route('/store')
# def get_stores():
#     return jsonify({'stores': stores })

# # POST /stroe/<string: name>/item
# @app.route('/store/<string:name>/item', methods=['POST'])
# def create_item_in_store(name):
#     request_data = request.get_json()
#     for store in stores:
#         if store['name'] == name:
#             new_item = {
#                 'name':request_data['name'],
#                 'price': request_data['price']
#             }
#         store['items'].append(new_item)
#         return jsonify(new_item)
#     return jsonify({'message':"Store not found"})

# # GET /store/<string:name>/item
# @app.route('/store/<string:name>/item')
# def get_item_in_store(name):

#     for store in stores:
#         if store['name'] == name:
#              return jsonify({'items':store['items']})
