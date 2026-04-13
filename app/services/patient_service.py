from sqlalchemy.orm import Session
from app.models.patient import Patient
from datetime import date
from fastapi import HTTPException



def calculate_age(date_of_birth: date) -> int:
    today = date.today()
    return today.year - date_of_birth.year - (
        (today.month, today.day) < (date_of_birth.month, date_of_birth.day)
    )


def create_patient(db: Session, patient_data: dict):
    age = calculate_age(patient_data["date_of_birth"])
    if age < 18:
        raise HTTPException(status_code=400, detail="Le patient doit avoir au moins 18 ans.")

    patient = Patient(**patient_data)
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient


def get_all_patients(db: Session):
    return db.query(Patient).all()


def get_patient_by_id(db: Session, patient_id: int):
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient non trouvé")
    return patient


def update_patient(db: Session, patient_id: int, update_data: dict):
    patient = get_patient_by_id(db, patient_id)
    for key, value in update_data.items():
        setattr(patient, key, value)
    db.commit()
    db.refresh(patient)
    return patient


def delete_patient(db: Session, patient_id: int):
    patient = get_patient_by_id(db, patient_id)
    db.delete(patient)
    db.commit()
    return {"message": "Patient supprimé avec succès"}
