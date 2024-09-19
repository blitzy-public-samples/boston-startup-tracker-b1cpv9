from fastapi.testclient import TestClient

def test_get_job_postings(client: TestClient):
    # Send a GET request to the `/jobs/` endpoint
    response = client.get("/jobs/")
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains a list of job postings
    assert isinstance(response.json(), list)
    
    # TODO: Add assertions to verify the structure and content of the job posting data

def test_get_job_posting(client: TestClient):
    # TODO: Retrieve a valid job posting ID from the database
    job_posting_id = "sample_id"  # Replace with actual ID
    
    # Send a GET request to the `/jobs/{job_posting_id}` endpoint
    response = client.get(f"/jobs/{job_posting_id}")
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains the job posting data for the specified ID
    assert response.json()["id"] == job_posting_id

def test_create_job_posting(client: TestClient):
    # Define test data for a new job posting
    new_job_posting = {
        "title": "Software Engineer",
        "company": "Tech Startup Inc.",
        "description": "We're looking for a talented software engineer...",
        "salary": 100000,
        "location": "Boston, MA"
    }
    
    # Send a POST request to the `/jobs/` endpoint with the test data
    response = client.post("/jobs/", json=new_job_posting)
    
    # Assert that the response status code is 201 Created
    assert response.status_code == 201
    
    # Assert that the response contains the data for the newly created job posting
    assert response.json()["title"] == new_job_posting["title"]
    assert response.json()["company"] == new_job_posting["company"]
    
    # TODO: Add assertions to verify the structure and content of the created job posting data

def test_update_job_posting(client: TestClient):
    # TODO: Retrieve a valid job posting ID from the database
    job_posting_id = "sample_id"  # Replace with actual ID
    
    # Define test data for updating the job posting
    updated_job_posting = {
        "title": "Senior Software Engineer",
        "salary": 120000
    }
    
    # Send a PUT request to the `/jobs/{job_posting_id}` endpoint with the test data
    response = client.put(f"/jobs/{job_posting_id}", json=updated_job_posting)
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains the data for the updated job posting
    assert response.json()["id"] == job_posting_id
    assert response.json()["title"] == updated_job_posting["title"]
    assert response.json()["salary"] == updated_job_posting["salary"]
    
    # TODO: Add assertions to verify the structure and content of the updated job posting data

def test_delete_job_posting(client: TestClient):
    # TODO: Retrieve a valid job posting ID from the database
    job_posting_id = "sample_id"  # Replace with actual ID
    
    # Send a DELETE request to the `/jobs/{job_posting_id}` endpoint
    response = client.delete(f"/jobs/{job_posting_id}")
    
    # Assert that the response status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response contains the data for the deleted job posting
    assert response.json()["id"] == job_posting_id
    
    # Verify that the job posting is no longer present in the database
    get_response = client.get(f"/jobs/{job_posting_id}")
    assert get_response.status_code == 404

# TODO: Human tasks
# 1. Add assertions to verify the structure and content of the job posting data in test_get_job_postings
# 2. Retrieve a valid job posting ID from the database in test_get_job_posting
# 3. Add assertions to verify the structure and content of the created job posting data in test_create_job_posting
# 4. Retrieve a valid job posting ID from the database in test_update_job_posting
# 5. Add assertions to verify the structure and content of the updated job posting data in test_update_job_posting
# 6. Retrieve a valid job posting ID from the database in test_delete_job_posting