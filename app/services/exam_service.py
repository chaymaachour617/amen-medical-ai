from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.exam import Exam



def create_exam(db: Session, exam_data: dict):
    exam = Exam(**exam_data)
    db.add(exam)
    db.commit()
    db.refresh(exam)
    return exam


def get_all_exams(db: Session):
    return db.query(Exam).all()


def get_exam_by_id(db: Session, exam_id: int):
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise HTTPException(status_code=404, detail="Examen non trouvé")
    return exam


def update_exam(db: Session, exam_id: int, update_data: dict):
    exam = get_exam_by_id(db, exam_id)
    for key, value in update_data.items():
        setattr(exam, key, value)
    db.commit()
    db.refresh(exam)
    return exam


def delete_exam(db: Session, exam_id: int):
    exam = get_exam_by_id(db, exam_id)
    db.delete(exam)
    db.commit()
    return {"message": "Examen supprimé avec succès"}
