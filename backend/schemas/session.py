from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SessionBase(BaseModel):
    patient_id: int


class SessionCreate(SessionBase):
    pass


class SessionResponse(SessionBase):
    id: int
    started_at: datetime
    ended_at: Optional[datetime] = None
    session_status: Optional[str] = None

    class Config:
        from_attributes = True
