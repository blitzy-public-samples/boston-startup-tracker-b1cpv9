from typing import TypeVar, Generic, List, Optional
from sqlalchemy.orm import Session
from app.db.base_class import Base
from app.models.job_posting import JobPosting
from app.schemas.job_posting import JobPostingCreate, JobPostingUpdate
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDJobPosting(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """Class providing CRUD operations for JobPosting model."""

    def __init__(self):
        """Default constructor for CRUDJobPosting class."""
        self.model = JobPosting
        self.create_schema = JobPostingCreate
        self.update_schema = JobPostingUpdate

    def get(self, db: Session, id: int) -> Optional[JobPosting]:
        """Retrieve a job posting by ID."""
        # Query the database for a job posting with the given ID
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> List[JobPosting]:
        """Retrieve multiple job postings."""
        # Query the database for job postings, skipping `skip` records and limiting to `limit` records
        return db.query(self.model).offset(skip).limit(limit).all()

    def get_multi_by_startup(self, db: Session, startup_id: int) -> List[JobPosting]:
        """Retrieve multiple job postings by startup ID."""
        # Query the database for job postings associated with the given startup ID
        return db.query(self.model).filter(self.model.startup_id == startup_id).all()

    def create(self, db: Session, obj_in: JobPostingCreate) -> JobPosting:
        """Create a new job posting."""
        # Create a new job posting object using data from `obj_in`
        db_obj = self.model(**obj_in.dict())
        # Add the job posting object to the database session
        db.add(db_obj)
        # Commit the changes to the database
        db.commit()
        # Refresh the job posting object to get the updated data (including ID)
        db.refresh(db_obj)
        # Return the created job posting object
        return db_obj

    def update(self, db: Session, db_obj: JobPosting, obj_in: JobPostingUpdate) -> JobPosting:
        """Update an existing job posting."""
        # Update the job posting object `db_obj` with data from `obj_in`
        update_data = obj_in.dict(exclude_unset=True)
        for field in update_data:
            setattr(db_obj, field, update_data[field])
        # Commit the changes to the database
        db.commit()
        # Refresh the job posting object to get the updated data
        db.refresh(db_obj)
        # Return the updated job posting object
        return db_obj

    def remove(self, db: Session, id: int) -> JobPosting:
        """Delete a job posting."""
        # Retrieve the job posting object with the given ID from the database
        obj = db.query(self.model).get(id)
        # Delete the job posting object from the database session
        db.delete(obj)
        # Commit the changes to the database
        db.commit()
        # Return the deleted job posting object
        return obj