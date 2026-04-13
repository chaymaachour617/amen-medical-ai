from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.session import Session as ChatSession
from app.models.patient import Patient

def create_session(db: Session, session_data: dict):
    try:
        patient = db.query(Patient).filter(Patient.id == session_data["patient_id"]).first()
        if not patient:
            raise HTTPException(status_code=404, detail="Patient non trouvé")
        
        allowed_fields = {"patient_id", "session_status", "ended_at"}
        filtered_data = {k: v for k, v in session_data.items() if k in allowed_fields}
        
        new_session = ChatSession(**filtered_data)
        db.add(new_session)
        db.commit()
        db.refresh(new_session)
        return new_session

    except Exception as e:
        db.rollback()  
        print("ERROR SESSION:", e)
        raise HTTPException(status_code=500, detail=str(e))


def get_all_sessions(db: Session):
    try:
        return db.query(ChatSession).all()
    except Exception as e:
        print("ERROR GET SESSIONS:", e)
        raise HTTPException(status_code=500, detail=str(e))


def get_session_by_id(db: Session, session_id: int):
    session = db.query(ChatSession).filter(ChatSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session non trouvée")
    return session


def delete_session(db: Session, session_id: int):
    session = get_session_by_id(db, session_id)
    db.delete(session)
    db.commit()
    return {"message": "Session supprimée avec succès"}
