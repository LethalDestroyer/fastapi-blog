# 📝 FastAPI Blog Application

This is a blog application built with **FastAPI**, providing a set of RESTful APIs for managing users, blogs, and comments. It uses **OAuth2 with JWT** for authentication.

## 🚀 Features

- ✅ User Signup & Login (OAuth2 + JWT)
- ✅ Create Blog Posts
- ✅ View All Blogs
- ✅ View My Blogs
- ✅ Comment on Blogs
- ✅ View Comments on a Blog Post
- ✅ Secure Routes with JWT Tokens
- ✅ Clean, Scalable Project Structure


### 1. Clone the repo

https://github.com/LethalDestroyer/fastapi-blog.git
cd fastapi-blog

2. Set up a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Run the application

uvicorn app.main:app --reload


🔐 Authentication Flow
Signup → /auth/signup

Login → /auth/login
Use token in Authorize in Swagger
Use token to access secured endpoints like:
/blogs/
/blogs/me
/comments/{blog_id}

🧪 Sample APIs

🔐 Auth
POST /auth/signup — Register a new user
POST /auth/login — Login and receive JWT token

📚 Blogs
POST /blogs/ — Create a blog post (JWT required)
GET /blogs/ — View all blogs (public)
GET /blogs/me — View blogs created by you (JWT required)

💬 Comments
POST /comments/{blog_id} — Add comment (JWT required)
GET /comments/{blog_id} — View all comments on a blog

👨‍💻 Author
Shubham Harne