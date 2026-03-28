from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AlertBase(BaseModel):
    session_id: int
    alert_type: str
    message: str
    severity: str


class AlertCreate(AlertBase):
    pass


class AlertResponse(AlertBase):
    id: int
    created_at: datetime

class Config:
        from_attributes = True