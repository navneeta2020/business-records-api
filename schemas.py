
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


# Schema for creating a business record
class BusinessRecordCreate(BaseModel):
    business_name: str = Field(min_length=2, max_length=100)
    contact_person: str = Field(min_length=2, max_length=100)
    email: str = Field(min_length=5, max_length=150)
    phone: Optional[str] = None
    description: Optional[str] = None


# Schema for updating a business record
class BusinessRecordUpdate(BaseModel):
    business_name: Optional[str] = None
    contact_person: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    description: Optional[str] = None


# Schema for returning a business record
class BusinessRecordResponse(BusinessRecordCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
