import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

# Application settings
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

# Database settings
password = "@Amir12345"  # Your actual password
encoded_password = quote_plus(password)  # Becomes "%40Amir12345"
DATABASE_URL = "mysql+mysqlconnector://amir:Amir12345@localhost/blog_db"

# Redis settings
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")