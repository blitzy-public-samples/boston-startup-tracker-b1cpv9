from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.job_posting import JobPosting, JobPostingCreate, JobPostingUpdate
from app.services.crud_job_posting import CRUDJobPosting
from app.utils.dependencies import get_job_posting_service

router = APIRouter()

@router.get("/", response_model=List[JobPosting])
def get_job_postings(
    job_posting_service: CRUDJobPosting = Depends(get_job_posting_service)
) -> List[JobPosting]:
    """
    Endpoint to retrieve all job postings.
    """
    # Call the `get_all` function from the `job_posting_service` to retrieve all job postings
    job_postings = job_posting_service.get_all()
    
    # Return the list of job postings
    return job_postings

@router.get("/{job_posting_id}", response_model=JobPosting)
def get_job_posting(
    job_posting_id: int,
    job_posting_service: CRUDJobPosting = Depends(get_job_posting_service)
) -> JobPosting:
    """
    Endpoint to retrieve a specific job posting by ID.
    """
    # Call the `get` function from the `job_posting_service` to retrieve the job posting with the specified ID
    job_posting = job_posting_service.get(job_posting_id)
    
    # If the job posting is not found, raise an HTTPException with status code 404
    if job_posting is None:
        raise HTTPException(status_code=404, detail="Job posting not found")
    
    # Return the job posting
    return job_posting

@router.post("/", response_model=JobPosting, status_code=status.HTTP_201_CREATED)
def create_job_posting(
    job_posting_in: JobPostingCreate,
    job_posting_service: CRUDJobPosting = Depends(get_job_posting_service)
) -> JobPosting:
    """
    Endpoint to create a new job posting.
    """
    # Call the `create` function from the `job_posting_service` to create a new job posting with the provided data
    new_job_posting = job_posting_service.create(job_posting_in)
    
    # Return the newly created job posting
    return new_job_posting

@router.put("/{job_posting_id}", response_model=JobPosting)
def update_job_posting(
    job_posting_id: int,
    job_posting_in: JobPostingUpdate,
    job_posting_service: CRUDJobPosting = Depends(get_job_posting_service)
) -> JobPosting:
    """
    Endpoint to update an existing job posting.
    """
    # Call the `get` function from the `job_posting_service` to retrieve the job posting with the specified ID
    existing_job_posting = job_posting_service.get(job_posting_id)
    
    # If the job posting is not found, raise an HTTPException with status code 404
    if existing_job_posting is None:
        raise HTTPException(status_code=404, detail="Job posting not found")
    
    # Call the `update` function from the `job_posting_service` to update the job posting with the provided data
    updated_job_posting = job_posting_service.update(job_posting_id, job_posting_in)
    
    # Return the updated job posting
    return updated_job_posting

@router.delete("/{job_posting_id}", response_model=JobPosting)
def delete_job_posting(
    job_posting_id: int,
    job_posting_service: CRUDJobPosting = Depends(get_job_posting_service)
) -> JobPosting:
    """
    Endpoint to delete a job posting.
    """
    # Call the `get` function from the `job_posting_service` to retrieve the job posting with the specified ID
    existing_job_posting = job_posting_service.get(job_posting_id)
    
    # If the job posting is not found, raise an HTTPException with status code 404
    if existing_job_posting is None:
        raise HTTPException(status_code=404, detail="Job posting not found")
    
    # Call the `remove` function from the `job_posting_service` to delete the job posting
    deleted_job_posting = job_posting_service.remove(job_posting_id)
    
    # Return the deleted job posting
    return deleted_job_posting