from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class PostBase(BaseModel):
    """
    Base Pydantic model for Post data.
    """
    text: str = Field(..., min_length=1, max_length=10000, example="This is a blog post")

class PostCreate(PostBase):
    """
    Pydantic model for creating a new Post.
    """
    pass

class Post(PostBase):
    """
    Pydantic model representing a Post with all fields including relationships.
    """
    id: int
    owner_id: int
    created_at: datetime
    
    class Config:
        orm_mode = True