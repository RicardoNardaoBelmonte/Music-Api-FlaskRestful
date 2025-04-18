from flask import Flask
from flask_restful import Api
from config import Config # importing class config
from database import configure_bdd
from resources import MusicResource, MusicListResource
from flask_migrate import Migrate 
from database import db

app = Flask(__name__)
app.config.from_object(Config) # setting the configuration of the app(bdd)
configure_bdd(app) #configuring the database( is calling the function to create the tables in bdd)
migrate = Migrate(app, db)# creating the migration object to manage the migrations of the database

api = Api(app) 
api.add_resource(MusicResource, '/music', '/music/<int:music_id>') # ading the resource to api
api.add_resource(MusicListResource, '/musics') #adding the resource to api get_all

if __name__ == '__main__':
    app.run(debug=True)