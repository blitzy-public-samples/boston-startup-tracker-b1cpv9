from pydantic import BaseModel
from datetime import date

# Base schema for Startup, defining common fields
class StartupBase(BaseModel):
    name: str
    website: str
    industry: str
    sub_sector: str
    employee_count: int
    local_employee_count: int
    headcount_growth: float
    total_funding: float
    last_funding_date: date
    funding_stage: str
    is_hiring: bool
    last_updated: date

# Schema for creating a new Startup, inheriting from StartupBase
class StartupCreate(StartupBase):
    pass

# Schema for updating an existing Startup, inheriting from StartupBase
class StartupUpdate(StartupBase):
    pass

# Schema for Startup as stored in the database, inheriting from StartupBase
class StartupInDBBase(StartupBase):
    id: int

# Schema for a complete Startup object, inheriting from StartupInDBBase
class Startup(StartupInDBBase):
    pass