from pydantic import BaseModel, EmailStr

# Base schema for User, defining common fields
class UserBase(BaseModel):
    email: EmailStr
    role: str
    is_active: bool

# Schema for creating a new User, inheriting from UserBase
class UserCreate(UserBase):
    password: str

# Schema for updating an existing User, inheriting from UserBase
class UserUpdate(UserBase):
    pass

# Schema for User as stored in the database, inheriting from UserBase
class UserInDBBase(UserBase):
    id: int
    hashed_password: str

# Schema for a complete User object, inheriting from UserInDBBase
class User(UserInDBBase):
    pass