from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional

class UserBase(BaseModel):
    """
    Base Pydantic model for User data with common fields.
    """
    email: EmailStr = Field(..., example="user@example.com")
    
    @validator('email')
    def email_must_contain_at(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email format')
        return v.lower()

class UserCreate(UserBase):
    """
    Pydantic model for creating a new User, includes password.
    """
    password: str = Field(..., min_length=8, max_length=50, example="strongpassword")

class UserInDB(UserBase):
    """
    Pydantic model representing a User as stored in DB (includes hashed password).
    """
    id: int
    hashed_password: str
    is_active: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    """
    Pydantic model for JWT token response.
    """
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    """
    Pydantic model for data encoded in JWT token.
    """
    email: Optional[str] = None