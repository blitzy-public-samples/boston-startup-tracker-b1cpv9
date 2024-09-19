from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.core.config import settings
from app.core.security import verify_password, create_access_token
from app.models.user import User
from app.schemas.token import Token

def authenticate_user(db: Session, email: str, password: str) -> User:
    """
    Authenticates a user based on email and password.
    """
    # Query the database for a user with the provided email
    user = db.query(User).filter(User.email == email).first()

    # If no user is found, return None
    if not user:
        return None

    # Verify the provided password against the user's hashed password
    if not verify_password(password, user.hashed_password):
        return None

    # Return the authenticated user
    return user

def create_access_token(user: User) -> Token:
    """
    Creates an access token for a user.
    """
    # Create the access token data payload with the user ID and expiry time
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token_data = {
        "sub": str(user.id),
        "exp": timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    }

    # Generate the access token using create_access_token
    access_token = create_access_token(access_token_data)

    # TODO: Implement refresh token generation logic
    refresh_token = "placeholder_refresh_token"

    # Return a Token object containing the access token and refresh token
    return Token(access_token=access_token, refresh_token=refresh_token)

# Human tasks:
# - Implement refresh token generation logic