from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.user import User, UserCreate, UserUpdate
from app.services.crud_user import CRUDUser
from app.utils.dependencies import get_user_service

router = APIRouter()

@router.get("/", response_model=List[User])
def get_users(user_service: CRUDUser = Depends(get_user_service)) -> List[User]:
    """
    Endpoint to retrieve all users.
    """
    # Call the `get_all` function from the `user_service` to retrieve all users
    users = user_service.get_all()
    # Return the list of users
    return users

@router.get("/{user_id}", response_model=User)
def get_user(user_service: CRUDUser = Depends(get_user_service), user_id: int = None) -> User:
    """
    Endpoint to retrieve a specific user by ID.
    """
    # Call the `get` function from the `user_service` to retrieve the user with the specified ID
    user = user_service.get(user_id)
    # If the user is not found, raise an HTTPException with status code 404
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # Return the user
    return user

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user_service: CRUDUser = Depends(get_user_service), user_in: UserCreate = None) -> User:
    """
    Endpoint to create a new user.
    """
    # Call the `create` function from the `user_service` to create a new user with the provided data
    new_user = user_service.create(user_in)
    # Return the newly created user
    return new_user

@router.put("/{user_id}", response_model=User)
def update_user(user_service: CRUDUser = Depends(get_user_service), user_id: int = None, user_in: UserUpdate = None) -> User:
    """
    Endpoint to update an existing user.
    """
    # Call the `get` function from the `user_service` to retrieve the user with the specified ID
    existing_user = user_service.get(user_id)
    # If the user is not found, raise an HTTPException with status code 404
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # Call the `update` function from the `user_service` to update the user with the provided data
    updated_user = user_service.update(existing_user, user_in)
    # Return the updated user
    return updated_user

@router.delete("/{user_id}", response_model=User)
def delete_user(user_service: CRUDUser = Depends(get_user_service), user_id: int = None) -> User:
    """
    Endpoint to delete a user.
    """
    # Call the `get` function from the `user_service` to retrieve the user with the specified ID
    existing_user = user_service.get(user_id)
    # If the user is not found, raise an HTTPException with status code 404
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # Call the `remove` function from the `user_service` to delete the user
    deleted_user = user_service.remove(existing_user)
    # Return the deleted user
    return deleted_user