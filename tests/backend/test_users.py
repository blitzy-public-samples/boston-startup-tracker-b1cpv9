from fastapi.testclient import TestClient
from app.core.security import verify_password
from app.schemas.user import UserCreate

def test_get_users(client: TestClient):
    # Send a GET request to the `/users/` endpoint
    response = client.get("/users/")
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains a list of users
    assert isinstance(response.json(), list)
    
    # TODO: Add assertions to verify the structure and content of the user data
    # TODO: Populate the database with test user data

def test_get_user(client: TestClient):
    # TODO: Retrieve a valid user ID from the database
    user_id = 1  # Replace with a valid user ID
    
    # Send a GET request to the `/users/{user_id}` endpoint
    response = client.get(f"/users/{user_id}")
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains the user data for the specified ID
    assert response.json()["id"] == user_id

def test_create_user(client: TestClient):
    # Define test data for a new user using the `UserCreate` schema
    new_user_data = UserCreate(
        email="test@example.com",
        password="testpassword",
        full_name="Test User"
    )
    
    # Send a POST request to the `/users/` endpoint with the test data
    response = client.post("/users/", json=new_user_data.dict())
    
    # Assert that the response status code is 201 Created
    assert response.status_code == 201
    
    # Assert that the response contains the data for the newly created user
    created_user = response.json()
    assert created_user["email"] == new_user_data.email
    assert created_user["full_name"] == new_user_data.full_name
    
    # TODO: Add assertions to verify the structure and content of the created user data

def test_update_user(client: TestClient):
    # TODO: Retrieve a valid user ID from the database
    user_id = 1  # Replace with a valid user ID
    
    # Define test data for updating the user
    update_data = {
        "full_name": "Updated User Name",
        "email": "updated@example.com"
    }
    
    # Send a PUT request to the `/users/{user_id}` endpoint with the test data
    response = client.put(f"/users/{user_id}", json=update_data)
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains the data for the updated user
    updated_user = response.json()
    assert updated_user["id"] == user_id
    assert updated_user["full_name"] == update_data["full_name"]
    assert updated_user["email"] == update_data["email"]
    
    # TODO: Add assertions to verify the structure and content of the updated user data

def test_delete_user(client: TestClient):
    # TODO: Retrieve a valid user ID from the database
    user_id = 1  # Replace with a valid user ID
    
    # Send a DELETE request to the `/users/{user_id}` endpoint
    response = client.delete(f"/users/{user_id}")
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains the data for the deleted user
    deleted_user = response.json()
    assert deleted_user["id"] == user_id
    
    # Verify that the user is no longer present in the database
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404

# Human tasks:
# - Add assertions to verify the structure and content of the user data in test_get_users
# - Populate the database with test user data for test_get_users
# - Retrieve a valid user ID from the database for test_get_user, test_update_user, and test_delete_user
# - Add assertions to verify the structure and content of the created user data in test_create_user
# - Add assertions to verify the structure and content of the updated user data in test_update_user