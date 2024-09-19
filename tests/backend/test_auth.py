from fastapi.testclient import TestClient
from app.core.security import verify_password

def test_login_for_access_token(client: TestClient):
    # Define test user credentials
    test_username = "test_user"
    test_password = "test_password"

    # Send a POST request to the `/auth/token` endpoint with the test credentials
    response = client.post(
        "/auth/token",
        data={"username": test_username, "password": test_password}
    )

    # Assert that the response status code is 200 OK
    assert response.status_code == 200

    # Assert that the response contains an access token and a refresh token
    json_response = response.json()
    assert "access_token" in json_response
    assert "refresh_token" in json_response

def test_login_for_access_token_incorrect_credentials(client: TestClient):
    # Define incorrect test user credentials
    incorrect_username = "wrong_user"
    incorrect_password = "wrong_password"

    # Send a POST request to the `/auth/token` endpoint with the incorrect credentials
    response = client.post(
        "/auth/token",
        data={"username": incorrect_username, "password": incorrect_password}
    )

    # Assert that the response status code is 401 Unauthorized
    assert response.status_code == 401

    # Assert that the response contains an error message indicating invalid credentials
    json_response = response.json()
    assert "detail" in json_response
    assert json_response["detail"] == "Incorrect username or password"

# Human tasks:
# 1. Retrieve a test user from the database or create one if it doesn't exist.
# 2. Replace the placeholder test credentials with the actual test user's credentials.