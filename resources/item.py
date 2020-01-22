from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help="El nombre del campo al cual se le quiere cambiar el valor no coincide con el nombre original del dato")
    parser.add_argument('store_id',type=int,required=True,help="Every item need a store_id number")




    @jwt_required()
    def get(self,name):
        
        item=ItemModel.find_by_name(name)
                    
        if item is not None:
            return item.json()
                     
        else:
            return {'message':'The item does not exist'}
               
    def post(self,name):

        if ItemModel.find_by_name(name) is not None:
            return {'message':f'The item {name} already exist'},400
                    
        data=Item.parser.parse_args()

        item=ItemModel(name,data['price'],data['store_id'])
        # item=ItemModel(name,**data)
        try:
            item.save_to_db()
            
        except:
            return {'message':'Ha ocurrido un error'},500
                    
        return item.json(), 201
    
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item is not None:
            item.delete_from_db()
        return {'message':'item deleted correctly'}
        
    def put(self,name):
                
        data=Item.parser.parse_args()  
        
        item=ItemModel.find_by_name(name)
               
        
        if item is None:
            item = ItemModel(name,data['price'], data['store_id'])
          
        else:
            item.price=data['price']

        item.save_to_db()
            
        return item.json()

class ItemList(Resource):
    def get (self):
        return {'items':[x.json() for x in ItemModel.query.all()]}
        #ed, da un diccionario con una sola key llamada items con un valor de 
        # una lista que aplica x.json a un bucle
        #es lo mismo que:
        # return {'items': List(map(lambda x:x.json(),ItemModel.query.all())}
        #lambda aplica a x la formula x.json()
        #map aplica lambda a todas las x de ItemModel.query.all()
        #Lista transforma todo ello en una lista 

        #importante.... si solo usamos python no usar el map, mejor el codigo de L62 antes que el de L66
        #se usa map si usamos además otros lenguajes como java etc. Si no es mejor usar el código que está puesto