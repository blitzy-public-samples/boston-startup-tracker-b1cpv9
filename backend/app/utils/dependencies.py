from typing import Generator
from fastapi import Depends
from app.db.session import SessionLocal
from app.services.crud_startup import CRUDStartup
from app.services.crud_user import CRUDUser
from app.services.crud_founder import CRUDFounder
from app.services.crud_executive import CRUDExecutive
from app.services.crud_investor import CRUDInvestor
from app.services.crud_funding_round import CRUDFundingRound
from app.services.crud_job_posting import CRUDJobPosting
from app.services.crud_news_article import CRUDNewsArticle
from app.services.auth_service import AuthService
from app.services.analytics_service import AnalyticsService
from app.services.search_service import SearchService

@Depends
def get_db() -> Generator[SessionLocal, None, None]:
    # Create a new database session
    db = SessionLocal()
    try:
        # Yield the session to the calling function
        yield db
    finally:
        # Close the session after the calling function has finished using it
        db.close()

@Depends
def get_startup_service(db: SessionLocal = Depends(get_db)) -> CRUDStartup:
    # Create an instance of the CRUDStartup service with the database session
    return CRUDStartup(db)

@Depends
def get_user_service(db: SessionLocal = Depends(get_db)) -> CRUDUser:
    # Create an instance of the CRUDUser service with the database session
    return CRUDUser(db)

@Depends
def get_founder_service(db: SessionLocal = Depends(get_db)) -> CRUDFounder:
    # Create an instance of the CRUDFounder service with the database session
    return CRUDFounder(db)

@Depends
def get_executive_service(db: SessionLocal = Depends(get_db)) -> CRUDExecutive:
    # Create an instance of the CRUDExecutive service with the database session
    return CRUDExecutive(db)

@Depends
def get_investor_service(db: SessionLocal = Depends(get_db)) -> CRUDInvestor:
    # Create an instance of the CRUDInvestor service with the database session
    return CRUDInvestor(db)

@Depends
def get_funding_round_service(db: SessionLocal = Depends(get_db)) -> CRUDFundingRound:
    # Create an instance of the CRUDFundingRound service with the database session
    return CRUDFundingRound(db)

@Depends
def get_job_posting_service(db: SessionLocal = Depends(get_db)) -> CRUDJobPosting:
    # Create an instance of the CRUDJobPosting service with the database session
    return CRUDJobPosting(db)

@Depends
def get_news_article_service(db: SessionLocal = Depends(get_db)) -> CRUDNewsArticle:
    # Create an instance of the CRUDNewsArticle service with the database session
    return CRUDNewsArticle(db)

@Depends
def get_auth_service(db: SessionLocal = Depends(get_db)) -> AuthService:
    # Create an instance of the AuthService with the database session
    return AuthService(db)

@Depends
def get_analytics_service(db: SessionLocal = Depends(get_db)) -> AnalyticsService:
    # Create an instance of the AnalyticsService with the database session
    return AnalyticsService(db)

@Depends
def get_search_service() -> SearchService:
    # Create an instance of the SearchService
    # TODO: Pass necessary dependencies (e.g., Elasticsearch client) to the SearchService constructor
    return SearchService()

# Human tasks:
# - Pass necessary dependencies (e.g., Elasticsearch client) to the SearchService constructor.