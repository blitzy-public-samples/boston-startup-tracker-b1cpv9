from pydantic import BaseModel
from datetime import date

# Base schema for NewsArticle, defining common fields
class NewsArticleBase(BaseModel):
    title: str
    url: str
    published_date: date

# Schema for creating a new NewsArticle, inheriting from NewsArticleBase
class NewsArticleCreate(NewsArticleBase):
    startup_id: int

# Schema for updating an existing NewsArticle, inheriting from NewsArticleBase
class NewsArticleUpdate(NewsArticleBase):
    pass

# Schema for NewsArticle as stored in the database, inheriting from NewsArticleBase
class NewsArticleInDBBase(NewsArticleBase):
    id: int
    startup_id: int

# Schema for a complete NewsArticle object, inheriting from NewsArticleInDBBase
class NewsArticle(NewsArticleInDBBase):
    pass