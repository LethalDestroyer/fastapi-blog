# app/db/schemas/comment.py

from pydantic import BaseModel
from datetime import datetime
from app.db.schemas.user import UserResponse

class CommentCreate(BaseModel):
    content: str

class CommentResponse(BaseModel):
    id: int
    content: str
    created_at: datetime
    user: UserResponse

    class Config:
        orm_mode = True
