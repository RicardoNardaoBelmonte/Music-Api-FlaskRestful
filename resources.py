from flask_restful import Resource, reqparse, fields, marshal_with
from sqlalchemy import Select
from models import Music
from database import db

#defining the arguments expected in the request
music_args = reqparse.RequestParser()
music_args.add_argument("artist", type=str, required=True, help='The field Artist is required')
music_args.add_argument("genre", type=str, required=True, help='The field Genre is required')
music_args.add_argument("year", type=int, required=False, help="The field year is not required it's optional")

#defining the structure of the response
resource_fields = {
    "id": fields.Integer,
    "artist": fields.String,
    "genre": fields.String,
    "year": fields.Integer
}

class MusicResource(Resource):
    @marshal_with(resource_fields)
    def get(self, music_id):
        music = db.session.get(Music, music_id)
        if not music:
            return {"massage": "Music not found"}, 404
        return music, 200
    
    @marshal_with(resource_fields)
    def post(self):
        data = music_args.parse_args()
        music = Music(artist=data['artist'], genre=data['genre'], year=data['year'])
        db.session.add(music)
        db.session.commit()
        return music, 201


    def delete(self, music_id):
        music = db.session.get(Music, music_id)
        if not music:
            return {"message": "Music not Found"}, 404
        db.session.delete(music)
        db.session.commit()
        return {"message": "Music deleted"}, 204

    @marshal_with(resource_fields)
    def put(self, music_id):
        data = music_args.parse_args() 
        music = db.session.get(Music, music_id)
        if not music:
            return {"message": "Music not found"},404
        
        music.artist = data['artist']
        music.genre = data['genre']
        music.year = data['year']
        db.session.commit()
        return  music, 200

class MusicListResource(Resource):
    @marshal_with(resource_fields)
    def get(self):#get_all
        musics = db.session.scalars(Select(Music)).all() #new standard for selecting all the data from the table
        if not musics:
            return {"message": "No musics Found"}, 404
        return musics, 200