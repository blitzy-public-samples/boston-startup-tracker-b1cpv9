from typing import List
from elasticsearch import Elasticsearch
from app.models.startup import Startup
from app.schemas.startup import Startup as StartupSchema

def search(es: Elasticsearch, query: str) -> List[StartupSchema]:
    """
    Searches for startups based on a query string.

    Args:
        es (Elasticsearch): The Elasticsearch client.
        query (str): The search query string.

    Returns:
        List[StartupSchema]: A list of startups that match the search query.
    """
    # Perform a search query on the Elasticsearch index using the provided query string.
    # TODO: Implement Elasticsearch query logic.
    search_results = es.search(index="startups", body={"query": {"match": {"_all": query}}})

    # Retrieve the startup IDs from the search results.
    startup_ids = [hit["_id"] for hit in search_results["hits"]["hits"]]

    # Fetch the corresponding startup data from the database.
    # TODO: Implement database lookup to retrieve startup data by ID.
    startups = Startup.query.filter(Startup.id.in_(startup_ids)).all()

    # Return the list of matching startups.
    return [StartupSchema.from_orm(startup) for startup in startups]

# Human tasks:
# TODO: Implement Elasticsearch query logic.
# TODO: Implement database lookup to retrieve startup data by ID.