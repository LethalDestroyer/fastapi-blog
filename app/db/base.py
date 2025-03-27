# app/db/base.py
# This will be useful later when importing all models in one place for creating tables.
from app.db.models import user, blog, comment
from app.db.session import Base


from app.db.models.user import User
from app.db.models.blog import Blog
from app.db.models.comment import Comment
