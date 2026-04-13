from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session as DBSession
from app.db.database import SessionLocal
from app.schemas.session import SessionCreate, SessionResponse
from app.services import session_service

router = APIRouter(prefix="/sessions", tags=["Sessions"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=SessionResponse)
def create_session(session: SessionCreate, db: DBSession = Depends(get_db)):
    return session_service.create_session(db, session.model_dump())


@router.get("/", response_model=list[SessionResponse])
def get_sessions(db: DBSession = Depends(get_db)):
    return session_service.get_all_sessions(db)


@router.get("/{session_id}", response_model=SessionResponse)
def get_session(session_id: int, db: DBSession = Depends(get_db)):
    return session_service.get_session_by_id(db, session_id)


@router.delete("/{session_id}")
def delete_session(session_id: int, db: DBSession = Depends(get_db)):
    return session_service.delete_session(db, session_id)