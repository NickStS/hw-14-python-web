from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import SessionLocal, get_db
from app.models import User
from app.schemas import UserBase
from app.hashing import verify_password
from app.jwt import create_access_token
from datetime import datetime, timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(db: SessionLocal = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user = verify_token(db, token)
    if user is None:
        raise credentials_exception

    return user

def verify_token(db: SessionLocal, token: str):
    user = db.query(User).filter(User.token == token).first()
    return user

def create_access_token_data(user: UserBase):
    access_token_expires = timedelta(minutes=15)
    expire = datetime.utcnow() + access_token_expires
    return {"sub": user.email, "exp": expire}

def create_access_token(user: UserBase):
    to_encode = create_access_token_data(user)
    encoded_jwt = create_access_token(to_encode)
    return encoded_jwt

def register_user(db: SessionLocal, user: UserBase):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_email(db: Session, email: str, token: str):
    user = db.query(User).filter(User.email == email, User.email_verification_token == token).first()
    if user:
        user.email_verified = True
        db.commit()
        return {"message": "Email verified"}
    else:
        raise HTTPException(status_code=400, detail="Email verification failed")
