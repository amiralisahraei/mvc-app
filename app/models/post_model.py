from sqlalchemy import Column, Integer, Text, ForeignKey
"""
This module defines the `Post` model for the application.

Classes:
    Post: Represents a post in the application, associated with a user.

Attributes:
    id (int): The primary key of the post.
    text (str): The content of the post. Cannot be null.
    owner_id (int): The foreign key referencing the ID of the user who owns the post. Cannot be null.
    owner (User): The relationship to the `User` model, representing the owner of the post.
"""
from sqlalchemy.orm import relationship
from app.database.database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Use string literals
    owner = relationship("User", back_populates="posts")