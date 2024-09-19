from fastapi.testclient import TestClient

def test_get_investors(client: TestClient):
    # Send a GET request to the `/investors/` endpoint
    response = client.get("/investors/")
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains a list of investors
    assert isinstance(response.json(), list)
    
    # TODO: Add assertions to verify the structure and content of the investor data

def test_get_investor(client: TestClient):
    # TODO: Retrieve a valid investor ID from the database
    investor_id = "sample_investor_id"
    
    # Send a GET request to the `/investors/{investor_id}` endpoint
    response = client.get(f"/investors/{investor_id}")
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains the investor data for the specified ID
    assert response.json()["id"] == investor_id

def test_create_investor(client: TestClient):
    # Define test data for a new investor
    new_investor_data = {
        "name": "Test Investor",
        "email": "test@investor.com",
        "portfolio_size": 10
    }
    
    # Send a POST request to the `/investors/` endpoint with the test data
    response = client.post("/investors/", json=new_investor_data)
    
    # Assert that the response status code is 201 Created
    assert response.status_code == 201
    
    # Assert that the response contains the data for the newly created investor
    assert response.json()["name"] == new_investor_data["name"]
    assert response.json()["email"] == new_investor_data["email"]
    assert response.json()["portfolio_size"] == new_investor_data["portfolio_size"]
    
    # TODO: Add assertions to verify the structure and content of the created investor data

def test_update_investor(client: TestClient):
    # TODO: Retrieve a valid investor ID from the database
    investor_id = "sample_investor_id"
    
    # Define test data for updating the investor
    update_data = {
        "name": "Updated Investor Name",
        "portfolio_size": 15
    }
    
    # Send a PUT request to the `/investors/{investor_id}` endpoint with the test data
    response = client.put(f"/investors/{investor_id}", json=update_data)
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains the data for the updated investor
    assert response.json()["id"] == investor_id
    assert response.json()["name"] == update_data["name"]
    assert response.json()["portfolio_size"] == update_data["portfolio_size"]
    
    # TODO: Add assertions to verify the structure and content of the updated investor data

def test_delete_investor(client: TestClient):
    # TODO: Retrieve a valid investor ID from the database
    investor_id = "sample_investor_id"
    
    # Send a DELETE request to the `/investors/{investor_id}` endpoint
    response = client.delete(f"/investors/{investor_id}")
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains the data for the deleted investor
    assert response.json()["id"] == investor_id
    
    # Verify that the investor is no longer present in the database
    get_response = client.get(f"/investors/{investor_id}")
    assert get_response.status_code == 404

# TODO: Human tasks
# 1. Add assertions to verify the structure and content of the investor data in test_get_investors
# 2. Retrieve a valid investor ID from the database in test_get_investor
# 3. Add assertions to verify the structure and content of the created investor data in test_create_investor
# 4. Retrieve a valid investor ID from the database in test_update_investor
# 5. Add assertions to verify the structure and content of the updated investor data in test_update_investor
# 6. Retrieve a valid investor ID from the database in test_delete_investor