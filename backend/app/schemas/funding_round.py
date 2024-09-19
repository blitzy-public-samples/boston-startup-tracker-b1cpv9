from pydantic import BaseModel
from datetime import date

# Base schema for FundingRound, defining common fields
class FundingRoundBase(BaseModel):
    amount: float
    date: date
    round_type: str

# Schema for creating a new FundingRound, inheriting from FundingRoundBase
class FundingRoundCreate(FundingRoundBase):
    startup_id: int

# Schema for updating an existing FundingRound, inheriting from FundingRoundBase
class FundingRoundUpdate(FundingRoundBase):
    pass

# Schema for FundingRound as stored in the database, inheriting from FundingRoundBase
class FundingRoundInDBBase(FundingRoundBase):
    id: int
    startup_id: int

# Schema for a complete FundingRound object, inheriting from FundingRoundInDBBase
class FundingRound(FundingRoundInDBBase):
    pass