from datetime import datetime
from typing import List
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.post_model import Post
from app.schemas.post_schema import PostCreate, Post
from app.database.database import get_db
from fastapi_cache.decorator import cache

class PostService:
    """
    Service class handling post related operations.
    """
    
    @staticmethod
    def create_post(db: Session, post: PostCreate, owner_id: int) -> Post:
        """
        Create a new post for the given user.
        
        Args:
            db: Database session
            post: Post creation data
            owner_id: ID of the post owner
            
        Returns:
            Post: The created post object
        """
        db_post = Post(text=post.text, owner_id=owner_id)
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post

    @staticmethod
    @cache(expire=300)  # Cache for 5 minutes
    def get_user_posts(db: Session, owner_id: int) -> List[Post]:
        """
        Get all posts for a specific user with caching.
        
        Args:
            db: Database session
            owner_id: ID of the user whose posts to retrieve
            
        Returns:
            List[Post]: List of posts belonging to the user
        """
        return db.query(Post).filter(Post.owner_id == owner_id).all()

    @staticmethod
    def delete_post(db: Session, post_id: int, owner_id: int) -> bool:
        """
        Delete a post if it belongs to the given user.
        
        Args:
            db: Database session
            post_id: ID of the post to delete
            owner_id: ID of the user attempting deletion
            
        Returns:
            bool: True if deletion was successful, False otherwise
            
        Raises:
            HTTPException: If post not found or not owned by user
        """
        post = db.query(Post).filter(Post.id == post_id).first()
        if not post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found"
            )
        if post.owner_id != owner_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to delete this post"
            )
        db.delete(post)
        db.commit()
        return True