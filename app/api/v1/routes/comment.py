# app/api/v1/routes/comment.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db import dependency
from app.db.models.comment import Comment
from app.db.models.blog import Blog
from app.db.models.user import User
from app.db.schemas.comment import CommentCreate, CommentResponse
from app.api.v1.routes.auth import oauth2_scheme, get_user_by_username
from app.core.security import decode_access_token

router = APIRouter(prefix="/comments", tags=["Comments"])

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(dependency.get_db)) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    username = payload.get("sub")
    user = get_user_by_username(db, username=username)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user


@router.post("/{blog_id}", response_model=CommentResponse)
def add_comment(blog_id: int, comment: CommentCreate, db: Session = Depends(dependency.get_db), current_user: User = Depends(get_current_user)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    new_comment = Comment(content=comment.content, user_id=current_user.id, blog_id=blog_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


@router.get("/{blog_id}", response_model=List[CommentResponse])
def get_comments(blog_id: int, db: Session = Depends(dependency.get_db)):
    return db.query(Comment).filter(Comment.blog_id == blog_id).all()
