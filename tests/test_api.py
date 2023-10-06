import json
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal

client = TestClient(app)

def create_sample_contacts(db):
    contacts = [
        {"name": "John Doe", "email": "john@example.com"},
        {"name": "Jane Smith", "email": "jane@example.com"},
    ]
    for contact in contacts:
        db.execute(
            "INSERT INTO contacts (name, email) VALUES (:name, :email)",
            {"name": contact["name"], "email": contact["email"]},
        )
    db.commit()

def test_create_contact():
    with TestClient(app) as client:
        db = SessionLocal()
        db.execute("DELETE FROM contacts")
        db.commit()

        response = client.post(
            "/contacts/",
            json={"name": "Alice Johnson", "email": "alice@example.com"},
        )

        assert response.status_code == 200

        db = SessionLocal()
        contact = db.execute("SELECT * FROM contacts WHERE name = 'Alice Johnson'").fetchone()
        db.commit()
        assert contact is not None

