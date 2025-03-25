from flask_sqlalchemy import SQLAlchemy 
from flask import Flask

db = SQLAlchemy() # creates db object instantiated from SQLAlchemy class

def configure(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db' #name of bdd (caminho)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # disable track modifications off (rastreamente de modificações)


    db.init_app(app)
    with app.app_context():
        db.create_all() #create tables to database
        
app = Flask(__name__)

configure(app)#configure the app(bdd)

if __name__ == '__main__':
    app.run(debug=True)