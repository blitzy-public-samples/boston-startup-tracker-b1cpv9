from pydantic import BaseModel

# Base schema for Founder, defining common fields
class FounderBase(BaseModel):
    name: str
    title: str
    linkedin_url: str

# Schema for creating a new Founder, inheriting from FounderBase
class FounderCreate(FounderBase):
    pass

# Schema for updating an existing Founder, inheriting from FounderBase
class FounderUpdate(FounderBase):
    pass

# Schema for Founder as stored in the database, inheriting from FounderBase
class FounderInDBBase(FounderBase):
    id: int
    startup_id: int

# Schema for a complete Founder object, inheriting from FounderInDBBase
class Founder(FounderInDBBase):
    pass