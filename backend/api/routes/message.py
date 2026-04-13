from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.message import MessageCreate, MessageResponse
from app.services import message_service

router = APIRouter(prefix="/messages", tags=["Messages"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=MessageResponse)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    return message_service.create_message(db, message.model_dump())


@router.get("/session/{session_id}", response_model=list[MessageResponse])
def get_messages_by_session(session_id: int, db: Session = Depends(get_db)):
    return message_service.get_messages_by_session(db, session_id)


@router.delete("/{message_id}")
def delete_message(message_id: int, db: Session = Depends(get_db)):
    return message_service.delete_message(db, message_id)