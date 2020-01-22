from flask_restful import Resource
from models.store import StoreModel 

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store is not None:
            return store.json()
            #ojo, el def json() que hemos creado en StoreModel también envía los items de esa store
        return {'message','store not found'},404 

    def post(self,name):
        if StoreModel.find_by_name(name) is not None:
            return {'message':'Store already exist'},400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message':'an error ocurred inserting this store'},500

        return store.json(),201

    def delete(self,name):
        store=StoreModel.find_by_name(name)
        if store is not None:
            store.delete_from_db()

        return{'message':'store deleted'}



class StoreList(Resource):
    #esta principalmente la meto en una class distinta porque va a estar en una ruta http diferente, por eso!!!!!!!!!!
    def get(self):
        return {'stores':[x.json() for x in StoreModel.query.all()]}
