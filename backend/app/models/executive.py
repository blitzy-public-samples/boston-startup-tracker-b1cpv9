from sqlalchemy import Column, ForeignKey, Integer, String
from app.db.base_class import Base

class Executive(Base):
    """Model representing an executive of a startup company."""

    # Define the table name
    __tablename__ = "executives"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Foreign key to link the executive to a startup
    startup_id = Column(Integer, ForeignKey("startups.id"), nullable=False)

    # Executive's name
    name = Column(String, nullable=False)

    # Executive's title or position
    title = Column(String, nullable=False)

    # LinkedIn profile URL of the executive
    linkedin_url = Column(String)

    def __init__(self, **kwargs):
        """Default constructor for the Executive class."""
        super().__init__(**kwargs)

    def __repr__(self):
        """Return a string representation of the Executive instance."""
        return f"<Executive(id={self.id}, name='{self.name}', title='{self.title}')>"