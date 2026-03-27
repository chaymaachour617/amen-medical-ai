from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.session import Session as ChatSession



def create_session(db: Session, session_data: dict):
    session = ChatSession(**session_data)
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


def get_all_sessions(db: Session):
    return db.query(ChatSession).all()


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