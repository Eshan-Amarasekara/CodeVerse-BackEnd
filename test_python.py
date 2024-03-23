import pytest
import json
from server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_main_page(client):
    response = client.get('/')
    assert b'Homepage' in response.data

def test_upload_file(client):
    # Test uploading a valid file
    with open('imagecheck1.png', 'rb') as f:
        data = {'file': (f, 'imagecheck1.png')}
        response = client.post('/upload', data=data, content_type='multipart/form-data')
        assert response.status_code == 201
        assert b'File successfully uploaded' in response.data

def test_get_bot_response(client):
    response = client.get('/get?msg=How%20are%20you?')
    assert response.status_code == 200
    expected_response = b"I'm here and ready to assist you with any questions or help you may need. How can I assist you today?"
    assert expected_response in response.data  # Adjust this assertion based on your expected response
 # Adjust this assertion based on your expected response

def test_me_endpoint(client):
    response = client.get('/me')
    assert response.status_code == 200
    assert b'me' in response.data  # Adjust this assertion based on your expected response

def test_user_input(client):
    data = {'data': 'test input data'}
    response = client.post('/userinput', json=data)
    assert response.status_code == 200
    assert b'JSON data saved successfully' in response.data

def test_business_endpoint(client):
    response = client.get('/business')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data  # Adjust this assertion based on your expected HTML response
