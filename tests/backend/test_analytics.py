from fastapi.testclient import TestClient

def test_get_funding_trends(client: TestClient):
    # Send a GET request to the `/analytics/funding-trends` endpoint
    response = client.get("/analytics/funding-trends")
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains funding trend data
    data = response.json()
    assert "funding_trends" in data
    assert isinstance(data["funding_trends"], list)
    
    # TODO: Add assertions to verify the structure and content of the funding trend data

def test_get_industry_breakdown(client: TestClient):
    # Send a GET request to the `/analytics/industry-breakdown` endpoint
    response = client.get("/analytics/industry-breakdown")
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains industry breakdown data
    data = response.json()
    assert "industry_breakdown" in data
    assert isinstance(data["industry_breakdown"], dict)
    
    # TODO: Add assertions to verify the structure and content of the industry breakdown data

def test_get_headcount_growth(client: TestClient):
    # Send a GET request to the `/analytics/headcount-growth` endpoint
    response = client.get("/analytics/headcount-growth")
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains headcount growth data
    data = response.json()
    assert "headcount_growth" in data
    assert isinstance(data["headcount_growth"], list)
    
    # TODO: Add assertions to verify the structure and content of the headcount growth data

# Human tasks:
# - Add assertions to verify the structure and content of the funding trend data.
# - Add assertions to verify the structure and content of the industry breakdown data.
# - Add assertions to verify the structure and content of the headcount growth data.