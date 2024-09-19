from typing import TypeVar, Generic, List, Optional
from sqlalchemy.orm import Session
from app.db.base_class import Base
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDUser(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self):
        self.model = User

    def get(self, db: Session, id: int) -> Optional[User]:
        # Query the database for a user with the given ID
        return db.query(self.model).filter(self.model.id == id).first()

    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        # Query the database for a user with the given email
        return db.query(self.model).filter(self.model.email == email).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        # Query the database for users, skipping `skip` records and limiting to `limit` records
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: UserCreate) -> User:
        # Hash the user's password using `get_password_hash`
        hashed_password = get_password_hash(obj_in.password)
        
        # Create a new user object using data from `obj_in` and the hashed password
        db_obj = User(
            email=obj_in.email,
            hashed_password=hashed_password,
            full_name=obj_in.full_name,
            is_superuser=obj_in.is_superuser,
        )
        
        # Add the user object to the database session
        db.add(db_obj)
        
        # Commit the changes to the database
        db.commit()
        
        # Refresh the user object to get the updated data (including ID)
        db.refresh(db_obj)
        
        # Return the created user object
        return db_obj

    def update(self, db: Session, db_obj: User, obj_in: UserUpdate) -> User:
        # Update the user object `db_obj` with data from `obj_in`
        update_data = obj_in.dict(exclude_unset=True)
        if update_data.get("password"):
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        
        # Commit the changes to the database
        db.add(db_obj)
        db.commit()
        
        # Refresh the user object to get the updated data
        db.refresh(db_obj)
        
        # Return the updated user object
        return db_obj

    def remove(self, db: Session, id: int) -> User:
        # Retrieve the user object with the given ID from the database
        obj = db.query(self.model).get(id)
        
        # Delete the user object from the database session
        db.delete(obj)
        
        # Commit the changes to the database
        db.commit()
        
        # Return the deleted user object
        return obj

user = CRUDUser()