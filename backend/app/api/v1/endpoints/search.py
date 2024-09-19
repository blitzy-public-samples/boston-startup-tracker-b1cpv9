from fastapi import APIRouter, Depends
from typing import List
from app.schemas.startup import Startup
from app.services.search_service import SearchService
from app.utils.dependencies import get_search_service

router = APIRouter()

@router.get("/", response_model=List[Startup])
async def search_startups(
    search_service: SearchService = Depends(get_search_service),
    query: str = ""
) -> List[Startup]:
    """
    Endpoint to search for startups based on a query string.

    Args:
        search_service (SearchService): Injected search service.
        query (str): The search query string.

    Returns:
        List[Startup]: A list of startups that match the search query.
    """
    # Call the `search` function from the `search_service` with the provided query string
    startups = await search_service.search(query)

    # Return the list of startups returned by the search service
    return startups