from db import db
import sqlite3


class StoreModel(db.Model):

    __tablename__='stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items=db.relationship('ItemModel', lazy='dynamic')
    #Creo una variable llamadsa item que dentro de StoreModel que establece una relación
    #con la clase ItemModel
    #pongo aquí lazy dynamic para que no me cree un objeto para todos los items....
    #esta operacion no hace falta que la haga en la clase ItemModel ya que por cada item solo 
    #hay una store mientras que en este caso de StoreModel tengo que poner el LAZY ya que para cada
    #store puede haber muichísimos items 
    

    def __init__(self,name):
        self.name=name
        

    def json(self):
        return {'name':self.name,'items':[x.json() for x in self.items.all()]}
        #.all() lo pongo debido al lazy de L12 
        #el json que aplico en la segunda key es el de ItemModel, ed,
        #al hacer la L12 puedo utilizar también sus __init__ siempre y cuando lo halla
        #invocado antes ya que en x.json() for x in self.items  realmente 
        #primero se está invocando con el self.items y luego se aplica el x.json()
        # de la class ItemModel 


        #AQUÍ LLAMO A LA VARIABLE CREADA ITEMS.
        #Ojo, se la llama com self.items ya que está creada dentro de la clase aunqie no este
        #definita en el def__init__ como name que si que lo está 
    
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