from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import List

from app.schemas.post_schema import Post, PostCreate
from app.models.user_model import User
from app.services.post_service import PostService
from app.services.auth_service import AuthService
from app.database.database import get_db

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

@router.post("/", response_model=Post)
def create_post(
    post: PostCreate,
    request: Request,
    current_user: User = Depends(AuthService.get_current_user),
    db: Session = Depends(get_db)
):
    """
    Endpoint for creating a new post.
    
    Args:
        post: Post creation data (text content)
        request: FastAPI request object for size validation
        current_user: Authenticated user from JWT token
        db: Database session
        
    Returns:
        Post: The created post object
        
    Raises:
        HTTPException: If payload size exceeds 1MB
    """
    # Check payload size (limit to 1MB)
    if request.headers.get("content-length") and int(request.headers["content-length"]) > 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="Payload too large (max 1MB)"
        )
    
    return PostService.create_post(db=db, post=post, owner_id=current_user.id)

@router.get("/", response_model=List[Post])
def read_posts(
    current_user: User = Depends(AuthService.get_current_user),
    db: Session = Depends(get_db)
):
    """
    Endpoint for retrieving all posts of the current user with caching.
    
    Args:
        current_user: Authenticated user from JWT token
        db: Database session
        
    Returns:
        List[Post]: List of posts belonging to the current user
    """
    return PostService.get_user_posts(db=db, owner_id=current_user.id)

@router.delete("/{post_id}")
def delete_post(
    post_id: int,
    current_user: User = Depends(AuthService.get_current_user),
    db: Session = Depends(get_db)
):
    """
    Endpoint for deleting a post.
    
    Args:
        post_id: ID of the post to delete
        current_user: Authenticated user from JWT token
        db: Database session
        
    Returns:
        dict: Success message
        
    Raises:
        HTTPException: If post not found or not owned by user
    """
    PostService.delete_post(db=db, post_id=post_id, owner_id=current_user.id)
    return {"message": "Post deleted successfully"}