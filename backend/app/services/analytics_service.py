from typing import List
from sqlalchemy.orm import Session
from app.models.startup import Startup
from app.models.funding_round import FundingRound

def get_funding_trends(db: Session) -> dict:
    """
    Calculates funding trends over time.
    
    :param db: SQLAlchemy database session
    :return: A dictionary containing funding trend data
    """
    # Query the database for funding round data grouped by year
    funding_data = db.query(
        FundingRound.year,
        db.func.sum(FundingRound.amount).label('total_funding')
    ).group_by(FundingRound.year).order_by(FundingRound.year).all()

    # Calculate the total funding amount for each year
    funding_trends = {
        'years': [],
        'amounts': []
    }
    for year, total_funding in funding_data:
        funding_trends['years'].append(year)
        funding_trends['amounts'].append(float(total_funding))

    # Format the data into a dictionary suitable for charting
    return funding_trends

def get_industry_breakdown(db: Session) -> dict:
    """
    Calculates the breakdown of startups by industry.
    
    :param db: SQLAlchemy database session
    :return: A dictionary containing industry breakdown data
    """
    # Query the database for the count of startups in each industry
    industry_data = db.query(
        Startup.industry,
        db.func.count(Startup.id).label('count')
    ).group_by(Startup.industry).all()

    # Format the data into a dictionary suitable for charting
    industry_breakdown = {
        'industries': [],
        'counts': []
    }
    for industry, count in industry_data:
        industry_breakdown['industries'].append(industry)
        industry_breakdown['counts'].append(count)

    return industry_breakdown

def get_headcount_growth(db: Session) -> dict:
    """
    Calculates headcount growth statistics.
    
    :param db: SQLAlchemy database session
    :return: A dictionary containing headcount growth data
    """
    # Query the database for startup headcount data
    headcount_data = db.query(Startup.initial_headcount, Startup.current_headcount).all()

    # Calculate growth rates
    growth_rates = []
    for initial, current in headcount_data:
        if initial > 0:
            growth_rate = (current - initial) / initial
            growth_rates.append(growth_rate)

    # Calculate average, median, and percentile headcount growth
    growth_rates.sort()
    num_startups = len(growth_rates)
    
    average_growth = sum(growth_rates) / num_startups if num_startups > 0 else 0
    median_growth = growth_rates[num_startups // 2] if num_startups > 0 else 0
    percentile_25 = growth_rates[int(num_startups * 0.25)] if num_startups > 0 else 0
    percentile_75 = growth_rates[int(num_startups * 0.75)] if num_startups > 0 else 0

    # Format the data into a dictionary suitable for presentation
    headcount_growth = {
        'average_growth': average_growth,
        'median_growth': median_growth,
        'percentile_25': percentile_25,
        'percentile_75': percentile_75
    }

    return headcount_growth

# Human tasks:
# - Implement logic to query and aggregate funding round data by year.
# - Implement logic to query and count startups by industry.
# - Implement logic to query headcount data and calculate growth statistics.