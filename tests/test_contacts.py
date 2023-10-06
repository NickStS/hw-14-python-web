from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal

client = TestClient(app)

# Ініціалізація бази даних перед початком тестів
def setup_module(module):
    pass

# Завершення роботи з базою даних після завершення тестів
def teardown_module(module):
    db = SessionLocal()
    db.close()

def test_create_contact():
    response = client.post("/contacts/", json={"name": "John Doe", "email": "johndoe@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "email" in data

def test_list_contacts():
    response = client.get("/contacts/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_read_contact():
    response = client.get("/contacts/1")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "email" in data

def test_update_contact():
    response = client.put("/contacts/1", json={"name": "Updated Name"})
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert data["name"] == "Updated Name"

def test_delete_contact():
    response = client.delete("/contacts/1")
    assert response.status_code == 200
    data = response.json()
    assert "name" in data
    assert "email" in data
