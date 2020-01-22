from db import db
import sqlite3


class ItemModel(db.Model):

    __tablename__='items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id=db.Column(db.Integer, db.ForeignKey('stores.id'))
    #aquí estamos definiendo cual va a ser el elemento que comparten las tablas de 
    #items y de stores donde store.id señala el nombre de la tabla y la comlumna a la que afecta
    #IMPORTANTE... ESTA CONEXION LA TENGO QUE CREAR DONDE EL PARÁMETRO COMPARTIDO NO SEA LA PRIMARY KEY (ed, definirlo donde sea la foreign key)
    #ED, COMO EL ELEMENTO COMPARTIDO ES EL ID DE LAS STORES (ID PRIMARY KEY EN StoreModel class)    
    #LA CREO AQÍ LA CONEXION
    
    store=db.relationship('StoreModel')
    #creo una variable que se llama stores dentro de ItemModel que establece una relacion con 
    #la clase StoreModel

    def __init__(self,name,price,store_id):
        self.name=name
        self.price=price
        self.store_id=store_id

    def json(self):
        return {'name':self.name,'price':self.price}
    
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()
        #es importante poner el return cls.query.. etc. ya que esto es una classmethod, es decir, me va a devolver un objeto
        #con lo cual ese objeto que quiero que me devuelva será ItemModel(name, price) siendo name y price filtrados por sqlalchemy
        # con lo cualñ, ItemModel(name,price) es lo mismo que cls(name,price)
       
        
    def save_to_db(self):
        
        db.session.add(self)
        db.session.commit()

    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

