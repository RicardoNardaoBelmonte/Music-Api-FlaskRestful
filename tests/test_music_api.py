
def test_create_music(test_client, sample_music_data):
    # creating test for post method 
    response = test_client.post('/music', json=sample_music_data)
    assert response.status_code==201
    assert 'id' in response.json #check if the id is in the response

    for key in sample_music_data:
        assert response.json[key] == sample_music_data[key]#this is a cool way to check if the data is correct in response

    
def test_get_music(test_client, created_music_id):
    #testing get method with existent id
    response = test_client.get(f'/music/{created_music_id}')
    assert response.status_code==200
    assert response.json['id'] == created_music_id #check if the id is the same as the one created in de function created_music_id

def test_get_nonexistent_music(test_client):
    #testing get method with non-existent id
    response = test_client.get('/music/999')
    assert response.status_code==404

def test_update_music (test_client, created_music_id):
    #testing put method
    update_data = {
        'artist': 'Eminem',
        'genre': 'rap',
        'year': 2000
    }

    response = test_client.put(''
        f'/music/{created_music_id}',
        json=update_data
    )
    
    assert response.status_code == 200
    update_music = response.json
    for key in update_data:
        assert update_music[key] == update_data[key]#comparing data

def test_delete_music(test_client, created_music_id):
    #this is a test for delete music
    #first we make sure the id exist
    get_response = test_client.get(f'/music/{created_music_id}')
    assert get_response.status_code == 200

    #doing the delete
    delete_response = test_client.delete(f'/music/{created_music_id}')
    assert delete_response.status_code == 204

    get_response = test_client.get(f'/music/{created_music_id}')
    assert get_response.status_code == 404#and here we are trying to return again the id to make sure it was deleted

def test_get_all_musics(test_client, created_music_id):
    #testing get all musics
    response = test_client.get('/musics')

    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0
    assert any(music['id'] == created_music_id for music in response.json)# this is a very cool way to verify if the response are right with comparing the ids 