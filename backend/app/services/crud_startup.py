from typing import TypeVar, Generic, List, Optional
from sqlalchemy.orm import Session
from app.db.base_class import Base
from app.models.startup import Startup
from app.schemas.startup import StartupCreate, StartupUpdate
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDStartup(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self):
        self.model = Startup

    def get(self, db: Session, id: int) -> Optional[Startup]:
        # Query the database for a startup with the given ID
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> List[Startup]:
        # Query the database for startups, skipping `skip` records and limiting to `limit` records
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: StartupCreate) -> Startup:
        # Create a new startup object using data from `obj_in`
        db_obj = self.model(**obj_in.dict())
        # Add the startup object to the database session
        db.add(db_obj)
        # Commit the changes to the database
        db.commit()
        # Refresh the startup object to get the updated data (including ID)
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: Startup, obj_in: StartupUpdate) -> Startup:
        # Update the startup object `db_obj` with data from `obj_in`
        obj_data = obj_in.dict(exclude_unset=True)
        for key, value in obj_data.items():
            setattr(db_obj, key, value)
        # Commit the changes to the database
        db.commit()
        # Refresh the startup object to get the updated data
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, id: int) -> Startup:
        # Retrieve the startup object with the given ID from the database
        obj = db.query(self.model).get(id)
        # Delete the startup object from the database session
        db.delete(obj)
        # Commit the changes to the database
        db.commit()
        return obj

crud_startup = CRUDStartup()