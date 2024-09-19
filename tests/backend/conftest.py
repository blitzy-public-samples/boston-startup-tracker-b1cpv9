from typing import Generator
import pytest
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.main import app
from fastapi.testclient import TestClient

def override_get_db() -> Generator[Session, None, None]:
    # Create a new database session using SessionLocal()
    db = SessionLocal()
    try:
        # Yield the session to the calling test function
        yield db
    finally:
        # Close the session after the test function has finished
        db.close()

@pytest.fixture(scope="module")
def client(override_get_db: Generator[Session, None, None]) -> Generator[TestClient, None, None]:
    # Create a FastAPI test client using TestClient(app)
    test_client = TestClient(app)
    
    # Override the get_db dependency in the application with the override_get_db fixture
    app.dependency_overrides[SessionLocal] = override_get_db
    
    try:
        # Yield the test client to the calling test function
        yield test_client
    finally:
        # Clean up the test client after the test function has finished
        app.dependency_overrides.clear()