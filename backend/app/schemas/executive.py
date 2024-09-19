from pydantic import BaseModel

# Base schema for Executive, defining common fields
class ExecutiveBase(BaseModel):
    name: str
    title: str
    linkedin_url: str

# Schema for creating a new Executive, inheriting from ExecutiveBase
class ExecutiveCreate(ExecutiveBase):
    pass

# Schema for updating an existing Executive, inheriting from ExecutiveBase
class ExecutiveUpdate(ExecutiveBase):
    pass

# Schema for Executive as stored in the database, inheriting from ExecutiveBase
class ExecutiveInDBBase(ExecutiveBase):
    id: int
    startup_id: int

# Schema for a complete Executive object, inheriting from ExecutiveInDBBase
class Executive(ExecutiveInDBBase):
    pass