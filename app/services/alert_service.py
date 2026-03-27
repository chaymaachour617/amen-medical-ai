from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.alert import Alert


def create_alert(db: Session, alert_data: dict):
    new_alert = Alert(**alert_data)
    db.add(new_alert)
    db.commit()
    db.refresh(new_alert)
    return new_alert


def get_all_alerts(db: Session):
    return db.query(Alert).all()


def get_alerts_by_session(db: Session, session_id: int):
    return db.query(Alert).filter(Alert.session_id == session_id).all()


def get_alert_by_id(db: Session, alert_id: int):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return alert


def delete_alert(db: Session, alert_id: int):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")

    db.delete(alert)
    db.commit()
    return {"message": "Alert deleted successfully"}