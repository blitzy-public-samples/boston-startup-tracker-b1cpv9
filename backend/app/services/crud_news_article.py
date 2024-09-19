from typing import TypeVar, Generic, List, Optional
from sqlalchemy.orm import Session
from app.db.base_class import Base
from app.models.news_article import NewsArticle
from app.schemas.news_article import NewsArticleCreate, NewsArticleUpdate
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDNewsArticle(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """Class providing CRUD operations for NewsArticle model."""

    def __init__(self):
        """Default constructor for CRUDNewsArticle class."""
        self.model = NewsArticle
        self.create_schema = NewsArticleCreate
        self.update_schema = NewsArticleUpdate

    def get(self, db: Session, id: int) -> Optional[NewsArticle]:
        """Retrieve a news article by ID."""
        # Query the database for a news article with the given ID
        return db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, db: Session, skip: int = 0, limit: int = 100) -> List[NewsArticle]:
        """Retrieve multiple news articles."""
        # Query the database for news articles, skipping `skip` records and limiting to `limit` records
        return db.query(self.model).offset(skip).limit(limit).all()

    def get_multi_by_startup(self, db: Session, startup_id: int) -> List[NewsArticle]:
        """Retrieve multiple news articles by startup ID."""
        # Query the database for news articles associated with the given startup ID
        return db.query(self.model).filter(self.model.startup_id == startup_id).all()

    def create(self, db: Session, obj_in: NewsArticleCreate) -> NewsArticle:
        """Create a new news article."""
        # Create a new news article object using data from `obj_in`
        db_obj = self.model(**obj_in.dict())
        # Add the news article object to the database session
        db.add(db_obj)
        # Commit the changes to the database
        db.commit()
        # Refresh the news article object to get the updated data (including ID)
        db.refresh(db_obj)
        # Return the created news article object
        return db_obj

    def update(self, db: Session, db_obj: NewsArticle, obj_in: NewsArticleUpdate) -> NewsArticle:
        """Update an existing news article."""
        # Update the news article object `db_obj` with data from `obj_in`
        update_data = obj_in.dict(exclude_unset=True)
        for field in update_data:
            setattr(db_obj, field, update_data[field])
        # Commit the changes to the database
        db.commit()
        # Refresh the news article object to get the updated data
        db.refresh(db_obj)
        # Return the updated news article object
        return db_obj

    def remove(self, db: Session, id: int) -> NewsArticle:
        """Delete a news article."""
        # Retrieve the news article object with the given ID from the database
        obj = db.query(self.model).get(id)
        # Delete the news article object from the database session
        db.delete(obj)
        # Commit the changes to the database
        db.commit()
        # Return the deleted news article object
        return obj