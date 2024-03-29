from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message":"Store not found"}, 404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {"message":"A store with name '{}' alread exists".fomart(name)}, 400

        store = StoreModel(name)
        
        try:
            store.save_to_db()
        except:
            return {"message": "An error occured during creation of store"}, 500

    def delete(self, name):
        sotore = StoreModel(name)

        if store:
            store.delete_from_db()
        
        return {"message": "Store deleted"}


class StoreList(Resource):
    def get(self):
        return{'store': [store.json() for store in StoreModel.query.all()]}
