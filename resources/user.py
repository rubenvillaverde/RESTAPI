


import sqlite3
from flask_restful import reqparse, Resource
from models.user import UserModel


class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument(
        'username',type=str,required=True,help="This field can not be blank"
    )
    parser.add_argument(
        'password',type=str,required=True,help="This field can not be blank"
    )

    def post(self):    
        
        data=UserRegister.parser.parse_args()
        

        if UserModel.find_by_username(data['username']) is not None:
            return {'message':'El usuario ya existe con ese nombre'},400

        user= UserModel(**data)
        #esto el lo mismo que user=UserModel(data['username'],data['password'])
        #es decir, **data convierte los valores asociado a unaq key en una tuple

        #ed, pasa de data={'username':valor1,'password':valor2}
        # a (valor1,valor2)
        user.save_to_db()


        return {"message":"user created correctly"},201

    


