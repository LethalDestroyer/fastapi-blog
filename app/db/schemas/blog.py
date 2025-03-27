# app/db/schemas/blog.py

from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from app.db.schemas.comment import CommentResponse
from app.db.schemas.user import UserResponse

class BlogCreate(BaseModel):
    title: str
    content: str

class BlogResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    owner: UserResponse
    comments: List[CommentResponse] = []

    class Config:
        orm_mode = True
