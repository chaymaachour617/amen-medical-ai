from sqlalchemy import Column, Integer, String, Date, Text, DateTime
from app.db.base import Base
from datetime import datetime, timezone

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String, nullable=False)
    medical_conditions = Column(Text)
    allergies = Column(Text)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))