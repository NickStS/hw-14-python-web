import pytest
import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_user(client):
    response = client.get('/users/1')
    assert response.status_code == 200