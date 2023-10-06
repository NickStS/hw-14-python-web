from sqlalchemy.orm import Session
from .models import Contact
from .schemas import ContactCreate, ContactUpdate, UserCreate

from app.models import User

def create_contact(db: Session, contact: ContactCreate):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def get_contacts(db: Session, skip: int = 0, limit: int = 100):
    contacts = db.query(Contact).offset(skip).limit(limit).all()
    return contacts

def get_contact_by_id(db: Session, contact_id: int):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    return contact

def update_contact(db: Session, contact_id: int, contact_data: ContactUpdate):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        for key, value in contact_data.dict().items():
            setattr(contact, key, value)
        db.commit()
        db.refresh(contact)
    return contact

def delete_contact(db: Session, contact_id: int):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user