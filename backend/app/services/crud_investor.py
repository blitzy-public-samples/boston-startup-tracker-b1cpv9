from typing import TypeVar, Generic, List, Optional
from sqlalchemy.orm import Session
from app.db.base_class import Base
from app.models.investor import Investor
from app.schemas.investor import InvestorCreate, InvestorUpdate
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDInvestor(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self):
        self.model = Investor

    def get(self, db: Session, id: int) -> Optional[Investor]:
        # Query the database for an investor with the given ID.
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> List[Investor]:
        # Query the database for investors, skipping `skip` records and limiting to `limit` records.
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: InvestorCreate) -> Investor:
        # Create a new investor object using data from `obj_in`.
        db_obj = self.model(**obj_in.dict())
        # Add the investor object to the database session.
        db.add(db_obj)
        # Commit the changes to the database.
        db.commit()
        # Refresh the investor object to get the updated data (including ID).
        db.refresh(db_obj)
        # Return the created investor object.
        return db_obj

    def update(self, db: Session, db_obj: Investor, obj_in: InvestorUpdate) -> Investor:
        # Update the investor object `db_obj` with data from `obj_in`.
        obj_data = obj_in.dict(exclude_unset=True)
        for key, value in obj_data.items():
            setattr(db_obj, key, value)
        # Commit the changes to the database.
        db.commit()
        # Refresh the investor object to get the updated data.
        db.refresh(db_obj)
        # Return the updated investor object.
        return db_obj

    def remove(self, db: Session, id: int) -> Investor:
        # Retrieve the investor object with the given ID from the database.
        obj = db.query(self.model).get(id)
        # Delete the investor object from the database session.
        db.delete(obj)
        # Commit the changes to the database.
        db.commit()
        # Return the deleted investor object.
        return obj