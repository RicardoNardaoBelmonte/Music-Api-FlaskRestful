
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

