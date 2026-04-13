from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MessageBase(BaseModel):
    content: str
    role: str
    session_id: int
    sender: Optional[str] = None


class MessageCreate(MessageBase):
    pass


class MessageResponse(MessageBase):
    id: int
    timestamp: datetime
    llm_model: Optional[str] = None
    was_modified: bool = False   

    class Config:
        from_attributes = True
