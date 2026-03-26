from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base


class SafetyLog(Base):
    __tablename__ = "safety_logs"

    id = Column(Integer, primary_key=True, index=True)
    rule_triggered = Column(String)
    original_output = Column(Text)
    modified_output = Column(Text)
    action_taken = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    message_id = Column(Integer, ForeignKey("messages.id"))
    message = relationship("Message", backref="safety_logs")