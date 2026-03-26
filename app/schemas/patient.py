from pydantic import BaseModel
from datetime import date
from typing import Optional


class PatientBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    medical_conditions: Optional[str] = None
    allergies: Optional[str] = None
class PatientCreate(PatientBase):
    pass


class PatientUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    date_of_birth: Optional[date]
    gender: Optional[str]
    medical_conditions: Optional[str]
    allergies: Optional[str]


class PatientResponse(PatientBase):
    id: int

    class Config:
        from_attributes = True