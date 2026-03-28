from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db.base import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    alert_type = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    severity = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    session_id = Column(Integer, ForeignKey("sessions.id"),nullable=False)
    session = relationship("Session", backref="alerts")