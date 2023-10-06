import unittest
from fastapi.testclient import TestClient
from app.main import app
from app.crud import get_contacts, create_contact, update_contact, delete_contact
from app.database import SessionLocal
from app.models import Contact, User
from sqlalchemy.orm import Session

class TestRepository(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)
        self.db = SessionLocal()

    def tearDown(self):
        self.db.close()

    def test_create_contact(self):
        user = User(username="testuser")
        contact_data = {"name": "John Doe", "email": "johndoe@example.com"}
        contact = create_contact(db=self.db, user=user, contact=contact_data)
        self.assertIsInstance(contact, Contact)
        self.assertEqual(contact.name, "John Doe")
        self.assertEqual(contact.email, "johndoe@example.com")

    def test_get_contact(self):
        user = User(username="testuser")
        contact_data = {"name": "Jane Smith", "email": "janesmith@example.com"}
        contact = create_contact(db=self.db, user=user, contact=contact_data)

        fetched_contact = get_contacts(db=self.db, user=user, contact_id=contact.id)
        self.assertEqual(contact.id, fetched_contact.id)

    def test_update_contact(self):
        user = User(username="testuser")
        contact_data = {"name": "Michael Johnson", "email": "michaeljohnson@example.com"}
        contact = create_contact(db=self.db, user=user, contact=contact_data)

        updated_data = {"name": "Updated Name", "email": "updated@example.com"}
        updated_contact = update_contact(db=self.db, user=user, contact_id=contact.id, contact=updated_data)
        self.assertEqual(updated_contact.name, "Updated Name")
        self.assertEqual(updated_contact.email, "updated@example.com")

    def test_delete_contact(self):
        user = User(username="testuser")
        contact_data = {"name": "Alice Brown", "email": "alicebrown@example.com"}
        contact = create_contact(db=self.db, user=user, contact=contact_data)

        deleted_contact = delete_contact(db=self.db, user=user, contact_id=contact.id)
        self.assertIsNone(deleted_contact)

if __name__ == '__main__':
    unittest.main()
