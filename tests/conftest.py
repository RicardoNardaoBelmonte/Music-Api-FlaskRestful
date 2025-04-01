import json
import pytest
from models import Music
from database import db
from app import app

@pytest.fixture(scope='module')#execute for all tests in the module
def test_client():
    #create a test for database
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"

    with app.test_client() as client:
        with app.app_context():
            db.create_all()# create all the tables in the databaseq
        yield client #return the test client
        with app.app_context():
            db.drop_all()# drop all the tables in the database after the tests are done

@pytest.fixture
def sample_music_data():
    #returns the fields of the music
    return {'artist': 'Test Artist', 'genre': 'Teste Genre', 'year': '2025'}

@pytest.fixture
def created_music_id(test_client, sample_music_data):
    #create a music in the database and returns the id of the music created
    #request = {'artist': 'Test Artist', 'genre': 'Teste Genre', 'year': '2025'} thats is a other way to create the request to post too
    response = test_client.post('/music', json=sample_music_data)
    return json.loads(response.data)['id']