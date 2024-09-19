from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.sql.functions import func

@as_declarative()
class Base:
    """Base class for all database models."""

    # Primary key column for all models
    @declared_attr
    def id(cls) -> Any:
        # Define an Integer column named 'id'
        # Set the column as the primary key
        # Enable autoincrement for the column
        return Column(Integer, primary_key=True, autoincrement=True)

    # Column to store the creation timestamp for each record
    @declared_attr
    def created_at(cls) -> Any:
        # Define a DateTime column named 'created_at'
        # Set the default value of the column to the current timestamp using `func.now()`
        return Column(DateTime, default=func.now())

    # Generate the table name automatically based on the class name
    @declared_attr
    def __tablename__(cls) -> str:
        # Convert the class name to lowercase
        # Return the lowercase class name as the table name
        return cls.__name__.lower()