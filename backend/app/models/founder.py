from sqlalchemy import Column, ForeignKey, Integer, String
from app.db.base_class import Base

class Founder(Base):
    """Model representing a founder of a startup company."""

    # Define the table name
    __tablename__ = "founders"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Foreign key to link the founder to a startup
    startup_id = Column(Integer, ForeignKey("startups.id"))

    # Founder's name
    name = Column(String, index=True)

    # Founder's title or position in the startup
    title = Column(String)

    # Founder's LinkedIn profile URL
    linkedin_url = Column(String)

    # TODO: Add relationships if needed (e.g., relationship to Startup model)
    # TODO: Add any additional methods or properties as required