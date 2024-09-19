from fastapi.testclient import TestClient

def test_search_startups(client: TestClient):
    # Define a test search query
    test_query = "tech"

    # Send a GET request to the `/search/` endpoint with the test query
    response = client.get(f"/search/?query={test_query}")

    # Assert that the response status code is 200 OK
    assert response.status_code == 200

    # Assert that the response contains a list of startups
    startups = response.json()
    assert isinstance(startups, list)
    assert len(startups) > 0

    # TODO: Human tasks
    # - Populate the database with test startup data.
    # - Add assertions to verify that the returned startups match the search query.