from app import app

db.init_app(app)

#ponemos un decorador que afecta al method justo de debajo
#el decorador hace que se ejecute siempre antes que el primer request que se haga a la API, se acual sea
@app.before_first_request
def create_tables():
    db.create_all()
    #crea todas las tablas, si no existen, que hallamos 
    # definidos en los Models mediante db.Model __tablename__
    #  etc...