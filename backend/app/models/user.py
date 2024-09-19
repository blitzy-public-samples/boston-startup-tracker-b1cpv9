from sqlalchemy import Column, Integer, String, Boolean
from app.db.base_class import Base

class User(Base):
    """Model representing a user of the application."""

    # Define the table name
    __tablename__ = "users"

    # Define columns
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    # Note: SQLAlchemy automatically creates a constructor that accepts keyword arguments
    # for all columns, so we don't need to explicitly define one.

    # Additional methods can be added here as needed, such as:
    # - Password hashing and verification
    # - Role-based permissions
    # - User profile information