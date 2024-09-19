from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create a database engine using the DATABASE_URL from settings
engine = create_engine(settings.DATABASE_URL)

# Create a sessionmaker instance bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Dependency function to provide a database session.
    
    Returns:
        Generator: A generator that yields a database session and closes it after use.
    """
    # Create a new database session
    db = SessionLocal()
    try:
        # Yield the session to the calling function
        yield db
    finally:
        # Close the session after the calling function has finished using it
        db.close()