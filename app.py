from db import db #Esto quiere decir del archivo db.py importa todo db.py 
from flask import Flask
from flask_restful import Api, reqparse
from flask_jwt import jwt_required, JWT

from security import authenticate, identify
from models.user import UserModel
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from models.store import StoreModel 
 

app=Flask(__name__)
#La siguiente linea es la que me crea el esquema.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'ruben'
api = Api(app)
db.init_app(app)

#ponemos un decorador que afecta al method justo de debajo
#el decorador hace que se ejecute siempre antes que el primer request que se haga a la API, se acual sea
@app.before_first_request
def create_tables():
    db.create_all()
    #crea todas las tablas, si no existen, que hallamos definidos en los Models mediante db.Model __tablename__ etc...

jwt=JWT(app, authenticate, identify)


api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister, '/register')



if __name__=='__main__':
    
    app.run(port=5000, debug=True)



