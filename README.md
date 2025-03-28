# Blog API with FastAPI

A secure blog application built with FastAPI following MVC architecture, featuring JWT authentication, post management, and MySQL database integration.

## Features

- ✅ JWT Authentication (Signup/Login)
- 📝 Create, Read, Delete blog posts
- 🔒 Token-based authorization
- 🚀 Optimized database operations
- ⚡ Response caching for posts
- 📊 MySQL database with SQLAlchemy ORM

## Tech Stack

- **Python 3.12**
- **FastAPI** (Web framework)
- **SQLAlchemy** (ORM)
- **MySQL** (Database)
- **Pydantic** (Data validation)
- **Redis** (Caching)
- **Uvicorn** (ASGI server)

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/blog-api-fastapi.git
cd blog-api-fastapi
```

### 2. Set up environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment
Create `.env` file:
```ini
DATABASE_URL=mysql+mysqlconnector://username:password@localhost/blog_db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REDIS_URL=redis://localhost:6379
```

### 5. Database setup
```sql
CREATE DATABASE blog_db;
GRANT ALL PRIVILEGES ON blog_db.* TO 'username'@'localhost';
```

## Running the Application

```bash
uvicorn main:app --reload
```

Access the API at:  
🔗 http://localhost:8000

## API Documentation

Interactive docs available at:  
📚 http://localhost:8000/docs  
📚 http://localhost:8000/redoc

## Endpoints

| Method | Endpoint          | Description                     | Auth Required |
|--------|-------------------|---------------------------------|---------------|
| POST   | /auth/signup      | Register new user               | No            |
| POST   | /auth/login       | Login and get access token      | No            |
| POST   | /posts/           | Create new post                 | Yes           |
| GET    | /posts/           | Get all user's posts            | Yes           |
| DELETE | /posts/{post_id}  | Delete a post                   | Yes           |

## Testing

### Manual Testing with cURL

1. **Signup**
```bash
curl -X POST "http://localhost:8000/auth/signup" \
-H "Content-Type: application/json" \
-d '{"email":"test@example.com","password":"securepassword"}'
```

2. **Login** (Save the token)
```bash
curl -X POST "http://localhost:8000/auth/login" \
-H "Content-Type: application/json" \
-d '{"username":"test@example.com","password":"securepassword"}'
```

3. **Create Post**
```bash
curl -X POST "http://localhost:8000/posts/" \
-H "Authorization: Bearer YOUR_TOKEN" \
-H "Content-Type: application/json" \
-d '{"text":"My first post"}'
```

### Automated Tests
Run the test suite:
```bash
pytest tests/
```

## Project Structure

```
blog-api/
├── app/
│   ├── controllers/      # Route handlers
│   ├── models/           # Database models
│   ├── schemas/          # Pydantic models  
│   ├── services/         # Business logic
│   ├── database/         # DB configuration
│   └── config.py         # App settings
├── main.py               # App entry point
└── requirements.txt      # Dependencies
```

## Deployment

For production deployment:
1. Set up MySQL and Redis servers
2. Configure proper CORS origins
3. Use Gunicorn with Uvicorn workers:
```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

## License

MIT License - See [LICENSE](LICENSE) for details