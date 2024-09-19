from pydantic import BaseModel
from datetime import date

# Base schema for JobPosting, defining common fields
class JobPostingBase(BaseModel):
    title: str
    department: str
    description: str
    posted_date: date

# Schema for creating a new JobPosting, inheriting from JobPostingBase
class JobPostingCreate(JobPostingBase):
    startup_id: int

# Schema for updating an existing JobPosting, inheriting from JobPostingBase
class JobPostingUpdate(JobPostingBase):
    pass

# Schema for JobPosting as stored in the database, inheriting from JobPostingBase
class JobPostingInDBBase(JobPostingBase):
    id: int
    startup_id: int

# Schema for a complete JobPosting object, inheriting from JobPostingInDBBase
class JobPosting(JobPostingInDBBase):
    pass