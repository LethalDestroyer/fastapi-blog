# app/db/models/comment.py

from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    blog_id = Column(Integer, ForeignKey("blogs.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    blog = relationship("Blog", back_populates="comments")
    user = relationship("User", back_populates="comments")
