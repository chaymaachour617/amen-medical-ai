from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.exam_schema import ExamCreate, ExamUpdate, ExamResponse
from app.services import exam_service

router = APIRouter(prefix="/exams", tags=["Exams"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=ExamResponse)
def create_exam(exam: ExamCreate, db: Session = Depends(get_db)):
    return exam_service.create_exam(db, exam.model_dump())


@router.get("/", response_model=list[ExamResponse])
def get_exams(db: Session = Depends(get_db)):
    return exam_service.get_all_exams(db)


@router.get("/{exam_id}", response_model=ExamResponse)
def get_exam(exam_id: int, db: Session = Depends(get_db)):
    return exam_service.get_exam_by_id(db, exam_id)


@router.put("/{exam_id}", response_model=ExamResponse)
def update_exam(exam_id: int, exam: ExamUpdate, db: Session = Depends(get_db)):
    return exam_service.update_exam(
        db, exam_id, exam.model_dump(exclude_unset=True)
    )


@router.delete("/{exam_id}")
def delete_exam(exam_id: int, db: Session = Depends(get_db)):
    return exam_service.delete_exam(db, exam_id)
