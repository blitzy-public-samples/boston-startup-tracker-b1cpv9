from sqlalchemy import Column, Integer, String, Float, Boolean, Date
from app.db.base_class import Base

class Startup(Base):
    """Model representing a startup company."""

    # Define table name
    __tablename__ = "startups"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Basic information
    name = Column(String, index=True)
    website = Column(String)
    industry = Column(String, index=True)
    sub_sector = Column(String)

    # Employee information
    employee_count = Column(Integer)
    local_employee_count = Column(Integer)
    headcount_growth = Column(Float)

    # Funding information
    total_funding = Column(Float)
    last_funding_date = Column(Date)
    funding_stage = Column(String)

    # Additional information
    is_hiring = Column(Boolean, default=False)
    last_updated = Column(Date)

    def __repr__(self):
        """Return a string representation of the Startup instance."""
        return f"<Startup(name={self.name}, industry={self.industry}, funding_stage={self.funding_stage})>"