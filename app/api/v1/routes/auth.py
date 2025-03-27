# app/api/v1/routes/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.core import security
from app.db import dependency
from app.db.models.user import User
from app.db.schemas.user import UserResponse
from app.db.schemas.user import UserCreate
from app.db.session import SessionLocal

router = APIRouter(prefix="/auth", tags=["Auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(dependency.get_db)):
    existing_user = db.query(User).filter((User.username == user.username) | (User.email == user.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")

    hashed_password = security.get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(dependency.get_db)):
    user = get_user_by_username(db, form_data.username)
    if not user or not security.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = security.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
