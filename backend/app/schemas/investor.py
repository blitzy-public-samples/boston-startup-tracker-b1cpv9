from pydantic import BaseModel

# Base schema for Investor, defining common fields
class InvestorBase(BaseModel):
    name: str
    type: str
    website: str

# Schema for creating a new Investor, inheriting from InvestorBase
class InvestorCreate(InvestorBase):
    pass

# Schema for updating an existing Investor, inheriting from InvestorBase
class InvestorUpdate(InvestorBase):
    pass

# Schema for Investor as stored in the database, inheriting from InvestorBase
class InvestorInDBBase(InvestorBase):
    id: int

# Schema for a complete Investor object, inheriting from InvestorInDBBase
class Investor(InvestorInDBBase):
    pass