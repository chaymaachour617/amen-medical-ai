from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.patient_schema import PatientCreate, PatientUpdate, PatientResponse
from app.services import patient_service

router = APIRouter(prefix="/patients", tags=["Patients"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=PatientResponse)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    return patient_service.create_patient(db, patient.model_dump())


@router.get("/", response_model=list[PatientResponse])
def get_patients(db: Session = Depends(get_db)):
    return patient_service.get_all_patients(db)


@router.get("/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    return patient_service.get_patient_by_id(db, patient_id)


@router.put("/{patient_id}", response_model=PatientResponse)
def update_patient(patient_id: int, patient: PatientUpdate, db: Session = Depends(get_db)):
    return patient_service.update_patient(db, patient_id, patient.model_dump(exclude_unset=True))


@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    return patient_service.delete_patient(db, patient_id)
