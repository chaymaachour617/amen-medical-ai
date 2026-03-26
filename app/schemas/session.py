from pydantic import BaseModel
from datetime import datetime


class SessionBase(BaseModel):
    patient_id: int


class SessionCreate(SessionBase):
    pass


class SessionResponse(SessionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True