from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy() # creates db object instantiated from SQLAlchemy class

def configure_bdd(app):
    db.init_app(app)    
    with app.app_context():
        db.create_all() #create tables to database