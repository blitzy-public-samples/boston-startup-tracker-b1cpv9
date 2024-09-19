from fastapi import APIRouter, Depends
from app.services.analytics_service import AnalyticsService
from app.utils.dependencies import get_analytics_service

# Create a router for analytics endpoints
router = APIRouter()

@router.get("/funding-trends", response_model=dict)
async def get_funding_trends(
    analytics_service: AnalyticsService = Depends(get_analytics_service)
) -> dict:
    """
    Endpoint to retrieve funding trends over time.
    """
    # Call the get_funding_trends function from the analytics_service
    funding_trends = await analytics_service.get_funding_trends()
    
    # Return the funding trend data
    return funding_trends

@router.get("/industry-breakdown", response_model=dict)
async def get_industry_breakdown(
    analytics_service: AnalyticsService = Depends(get_analytics_service)
) -> dict:
    """
    Endpoint to retrieve the breakdown of startups by industry.
    """
    # Call the get_industry_breakdown function from the analytics_service
    industry_breakdown = await analytics_service.get_industry_breakdown()
    
    # Return the industry breakdown data
    return industry_breakdown

@router.get("/headcount-growth", response_model=dict)
async def get_headcount_growth(
    analytics_service: AnalyticsService = Depends(get_analytics_service)
) -> dict:
    """
    Endpoint to retrieve headcount growth statistics.
    """
    # Call the get_headcount_growth function from the analytics_service
    headcount_growth = await analytics_service.get_headcount_growth()
    
    # Return the headcount growth data
    return headcount_growth