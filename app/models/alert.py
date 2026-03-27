from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    alert_type = Column(String)
    alert_message = Column(Text)
    severity = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    session_id = Column(Integer, ForeignKey("sessions.id"))
    session = relationship("Session", backref="alerts")