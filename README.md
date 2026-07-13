# Backend Clone of a Social Media Application using FastAPI

This project is a production-ready REST API for a social media application built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**.

The API supports secure authentication, post management, user management, and a voting system.

---

# API Routes

## 1) Posts Route

Responsible for managing posts.

Features:

- Create Post
- Get All Posts
- Get Post by ID
- Update Post
- Delete Post
- Search Posts
- Pagination Support

---

## 2) Users Route

Responsible for user management.

Features:

- Register User
- Get User by ID

---

## 3) Authentication Route

Responsible for authentication.

Features:

- User Login
- JWT Token Generation
- OAuth2 Password Authentication

---

## 4) Votes Route

Responsible for the like/vote system.

Features:

- Vote on Posts
- Remove Vote
- Prevent Duplicate Votes

---

# Technologies Used

- FastAPI
- Python
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- JWT Authentication
- Passlib (bcrypt)
- Docker
- Pytest

---

# How to Run Locally

First clone the repository.

```bash
git clone https://github.com/MahekPatel-2403/SocialSphere-API.git
```

Then move into the project directory.

```bash
cd SocialSphere-API
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment.

### Linux/macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install the dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
uvicorn app.main:app --reload
```

Open Swagger Documentation.

```text
http://127.0.0.1:8000/docs
```

---

# Environment Variables

Create a **.env** file in the root directory and add the following variables.

```env
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=your_password
DATABASE_NAME=socialsphere
DATABASE_USERNAME=postgres

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Project Structure

```
SocialSphere-API
│
├── app
│   ├── routers
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── oauth2.py
│   ├── utils.py
│   ├── config.py
│   └── main.py
│
├── alembic
├── tests
├── requirements.txt
├── .env
└── README.md
```

---

# Future Improvements

- Comments on Posts
- User Profiles
- Image Uploads
- Refresh Tokens
- Email Verification
- Follow/Unfollow Users
- Notifications

---

## Author

**Mahek Patel**

GitHub: https://github.com/MahekPatel-2403
