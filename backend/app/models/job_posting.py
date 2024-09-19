from sqlalchemy import Column, ForeignKey, Integer, String, Date
from app.db.base_class import Base

class JobPosting(Base):
    """Model representing a job posting by a startup company."""

    # Define the table name
    __tablename__ = "job_postings"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Foreign key to link the job posting to a startup
    startup_id = Column(Integer, ForeignKey("startups.id"), nullable=False)

    # Job posting details
    title = Column(String, nullable=False)
    department = Column(String, nullable=False)
    description = Column(String, nullable=False)
    posted_date = Column(Date, nullable=False)

    # TODO: Add relationships if needed (e.g., to Startup model)
    # TODO: Add any additional methods or properties as required