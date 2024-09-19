from datetime import datetime, timedelta
from typing import Any, Union
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from app.models.user import User

# Initialize password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Initialize OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict, expires_delta: Union[timedelta, None]) -> str:
    """
    Generates a JWT access token.
    """
    # Determine the token expiry time based on the provided `expires_delta`
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    # Add the expiry time to the `data` dictionary
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    
    # Encode the `data` dictionary as a JWT using the application's secret key
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    # Return the encoded JWT
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain password against a hashed password.
    """
    # Use the `pwd_context` to verify the plain password against the hashed password
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Hashes a plain password using bcrypt.
    """
    # Use the `pwd_context` to hash the password using bcrypt
    return pwd_context.hash(password)

def get_current_user(token: str) -> Any:
    """
    Retrieves the currently authenticated user from the JWT token.
    """
    try:
        # Decode the JWT token using the application's secret key
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        
        # Extract the user ID from the decoded token
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Retrieve the user from the database based on the user ID
    # TODO: Implement database lookup to retrieve user by ID
    user = None  # Replace this with actual database lookup
    
    # If the user is not found or the token is invalid, raise an HTTPException
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Return the user object
    return user

# Human tasks:
# TODO: Implement database lookup to retrieve user by ID