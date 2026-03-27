from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.message import Message



def create_message(db: Session, message_data: dict):
    message = Message(**message_data)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def get_messages_by_session(db: Session, session_id: int):
    return db.query(Message).filter(Message.session_id == session_id).all()


def delete_message(db: Session, message_id: int):
    message = db.query(Message).filter(Message.id == message_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message non trouvé")
    db.delete(message)
    db.commit()
    return {"message": "Message supprimé avec succès"}