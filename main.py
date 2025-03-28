from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from app.controllers import auth_controller, post_controller
from app.database.database import engine, Base
from app.config import REDIS_URL, ENVIRONMENT

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blog API",
    description="A simple blog API with authentication",
    version="1.0.0",
    docs_url="/docs" if ENVIRONMENT != "production" else None,
    redoc_url=None
)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_controller.router)
app.include_router(post_controller.router)

@app.on_event("startup")
async def startup():
    """
    Initialize Redis cache on application startup.
    """
    redis = aioredis.from_url(REDIS_URL)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

@app.get("/")
def read_root():
    """
    Root endpoint returning a simple message.
    """
    return {"message": "Blog API is running"}