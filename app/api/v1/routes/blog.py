# app/api/v1/routes/blog.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db import dependency
from app.db.models.blog import Blog
from app.db.models.user import User
from app.db.schemas.blog import BlogCreate, BlogResponse
from app.api.v1.routes.auth import oauth2_scheme, get_user_by_username
from app.core.security import decode_access_token

router = APIRouter(prefix="/blogs", tags=["Blogs"])

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(dependency.get_db)) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    username = payload.get("sub")
    user = get_user_by_username(db, username=username)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user


@router.post("/", response_model=BlogResponse)
def create_blog(blog: BlogCreate, db: Session = Depends(dependency.get_db), current_user: User = Depends(get_current_user)):
    db_blog = Blog(title=blog.title, content=blog.content, owner_id=current_user.id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


@router.get("/", response_model=List[BlogResponse])
def get_all_blogs(db: Session = Depends(dependency.get_db)):
    return db.query(Blog).all()


@router.get("/me", response_model=List[BlogResponse])
def get_my_blogs(db: Session = Depends(dependency.get_db), current_user: User = Depends(get_current_user)):
    return db.query(Blog).filter(Blog.owner_id == current_user.id).all()
