import pytest

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert '¡Hola Mundo!'.encode('utf-8') in response.data

def test_status(client):
    response = client.get('/')
    assert response.status_code == 200