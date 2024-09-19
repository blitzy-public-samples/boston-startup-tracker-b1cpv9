from fastapi.testclient import TestClient

def test_get_funding_rounds(client: TestClient):
    # Send a GET request to the `/funding-rounds/` endpoint
    response = client.get("/funding-rounds/")
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains a list of funding rounds
    assert isinstance(response.json(), list)
    
    # TODO: Add assertions to verify the structure and content of the funding round data

def test_get_funding_round(client: TestClient):
    # TODO: Retrieve a valid funding round ID from the database
    funding_round_id = "sample_id"  # Replace with actual ID
    
    # Send a GET request to the `/funding-rounds/{funding_round_id}` endpoint
    response = client.get(f"/funding-rounds/{funding_round_id}")
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains the funding round data for the specified ID
    assert response.json()["id"] == funding_round_id

def test_create_funding_round(client: TestClient):
    # Define test data for a new funding round
    new_funding_round = {
        "startup_id": "sample_startup_id",
        "round_type": "Seed",
        "amount": 1000000,
        "date": "2023-05-01"
    }
    
    # Send a POST request to the `/funding-rounds/` endpoint with the test data
    response = client.post("/funding-rounds/", json=new_funding_round)
    
    # Assert that the response status code is 201 Created
    assert response.status_code == 201
    
    # Assert that the response contains the data for the newly created funding round
    assert response.json()["startup_id"] == new_funding_round["startup_id"]
    assert response.json()["round_type"] == new_funding_round["round_type"]
    assert response.json()["amount"] == new_funding_round["amount"]
    assert response.json()["date"] == new_funding_round["date"]
    
    # TODO: Add assertions to verify the structure and content of the created funding round data

def test_update_funding_round(client: TestClient):
    # TODO: Retrieve a valid funding round ID from the database
    funding_round_id = "sample_id"  # Replace with actual ID
    
    # Define test data for updating the funding round
    updated_data = {
        "amount": 2000000,
        "date": "2023-06-01"
    }
    
    # Send a PUT request to the `/funding-rounds/{funding_round_id}` endpoint with the test data
    response = client.put(f"/funding-rounds/{funding_round_id}", json=updated_data)
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains the data for the updated funding round
    assert response.json()["id"] == funding_round_id
    assert response.json()["amount"] == updated_data["amount"]
    assert response.json()["date"] == updated_data["date"]
    
    # TODO: Add assertions to verify the structure and content of the updated funding round data

def test_delete_funding_round(client: TestClient):
    # TODO: Retrieve a valid funding round ID from the database
    funding_round_id = "sample_id"  # Replace with actual ID
    
    # Send a DELETE request to the `/funding-rounds/{funding_round_id}` endpoint
    response = client.delete(f"/funding-rounds/{funding_round_id}")
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains the data for the deleted funding round
    assert response.json()["id"] == funding_round_id
    
    # Verify that the funding round is no longer present in the database
    get_response = client.get(f"/funding-rounds/{funding_round_id}")
    assert get_response.status_code == 404

# Human tasks:
# TODO: Retrieve a valid funding round ID from the database
# TODO: Add assertions to verify the structure and content of the funding round data
# TODO: Add assertions to verify the structure and content of the created funding round data
# TODO: Add assertions to verify the structure and content of the updated funding round data