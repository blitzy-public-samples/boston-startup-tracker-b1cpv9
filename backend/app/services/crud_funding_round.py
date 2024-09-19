from typing import TypeVar, Generic, List, Optional
from sqlalchemy.orm import Session
from app.db.base_class import Base
from app.models.funding_round import FundingRound
from app.schemas.funding_round import FundingRoundCreate, FundingRoundUpdate

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDFundingRound(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self):
        self.model = FundingRound

    def get(self, db: Session, id: int) -> Optional[FundingRound]:
        # Query the database for a funding round with the given ID
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> List[FundingRound]:
        # Query the database for funding rounds, skipping `skip` records and limiting to `limit` records
        return db.query(self.model).offset(skip).limit(limit).all()

    def get_multi_by_startup(self, db: Session, startup_id: int) -> List[FundingRound]:
        # Query the database for funding rounds associated with the given startup ID
        return db.query(self.model).filter(self.model.startup_id == startup_id).all()

    def create(self, db: Session, obj_in: FundingRoundCreate) -> FundingRound:
        # Create a new funding round object using data from `obj_in`
        db_obj = self.model(**obj_in.dict())
        # Add the funding round object to the database session
        db.add(db_obj)
        # Commit the changes to the database
        db.commit()
        # Refresh the funding round object to get the updated data (including ID)
        db.refresh(db_obj)
        # Return the created funding round object
        return db_obj

    def update(self, db: Session, db_obj: FundingRound, obj_in: FundingRoundUpdate) -> FundingRound:
        # Update the funding round object `db_obj` with data from `obj_in`
        obj_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            setattr(db_obj, field, obj_data[field])
        # Commit the changes to the database
        db.commit()
        # Refresh the funding round object to get the updated data
        db.refresh(db_obj)
        # Return the updated funding round object
        return db_obj

    def remove(self, db: Session, id: int) -> FundingRound:
        # Retrieve the funding round object with the given ID from the database
        obj = db.query(self.model).get(id)
        # Delete the funding round object from the database session
        db.delete(obj)
        # Commit the changes to the database
        db.commit()
        # Return the deleted funding round object
        return obj

funding_round = CRUDFundingRound()