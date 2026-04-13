from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ExamBase(BaseModel):
    exam_type: str
    exam_date: datetime
    preparation_type: Optional[str] = None
    status: Optional[str] = None
    patient_id: int


class ExamCreate(ExamBase):
    pass


class ExamUpdate(BaseModel):
    exam_type: Optional[str]
    exam_date: Optional[datetime]
    preparation_type: Optional[str]
    status: Optional[str]


class ExamResponse(ExamBase):
    id: int

    class Config:
        from_attributes = True
