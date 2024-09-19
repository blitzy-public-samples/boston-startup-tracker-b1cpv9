from sqlalchemy import Column, Integer, String
from app.db.base_class import Base

class Investor(Base):
    """Model representing an investor."""

    # Define the table name
    __tablename__ = "investors"

    # Define the columns
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    website = Column(String)

    # Default constructor is automatically provided by SQLAlchemy