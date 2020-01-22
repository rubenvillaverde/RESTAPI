from db import db
import sqlite3



class UserModel(db.Model):
    #con esto estamos diciendo que la clase UserModel que no es resource, se basa en la clase db.Model
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self,username,password):
        #como sabemos no hay que especificar id ya que es automático (anterior mas uno)
        #podriamos utilizar tambien en lugar de id los UUID universisal unique id
        self.username=username
        self.password=password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
        #es una class methos ergo me da un objeto de esta misma clase, por lo tanto ha de devolver cls(parametros filtrados)
        # #que es lo mismo que UserModel(parámetros filtrados)
        # #
        #  hasta query es como SELECT * FROM
        # .filter_by= es como WHERE USERNAME=USERNAME
        # .first() ES COMO FECTHONE()
        # ED, me da toda la fila (filter By) del primer resultado que coincide (first()) 
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
        #el nombre de la tabla lo definimos al principio de la clase 

        #importante .... relacionar cada clase con una tabla deistinta en base de datos 
       
