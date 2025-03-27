# app/db/schemas/user.py

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
