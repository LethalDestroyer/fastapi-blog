# app/main.py

from fastapi import FastAPI
from app.db.session import engine
from app.db import base
from app.api.v1.routes import auth, blog, comment

app = FastAPI(title="Blog API", version="1.0.0")

# Create DB tables on startup
base.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(comment.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Blog API!"}
