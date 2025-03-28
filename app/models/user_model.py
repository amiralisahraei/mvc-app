from sqlalchemy import Column, Integer, String, Boolean
"""
This module defines the `User` model for the application.

Classes:
    User: Represents a user in the system.

Attributes:
    id (int): The primary key for the user.
    email (str): The email address of the user. Must be unique and not null.
    hashed_password (str): The hashed password of the user. Cannot be null.
    is_active (bool): Indicates whether the user is active. Defaults to True.
    posts (relationship): A relationship to the `Post` model, representing the posts owned by the user.
"""
from sqlalchemy.orm import relationship
from app.database.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)

    # Use string literals for the relationship
    posts = relationship("Post", back_populates="owner")