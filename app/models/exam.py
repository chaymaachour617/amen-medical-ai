from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, index=True)
    exam_type = Column(String, nullable=False)
    exam_date = Column(DateTime, nullable=False)
    preparation_type = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    patient_id = Column(Integer, ForeignKey("patients.id"))
    patient = relationship("Patient", backref="exams")