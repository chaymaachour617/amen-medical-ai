from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.alert_schema import AlertCreate, AlertResponse
from app.services import alert_service

router = APIRouter(prefix="/alerts", tags=["Alerts"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AlertResponse)
def create_alert(alert: AlertCreate, db: Session = Depends(get_db)):
    return alert_service.create_alert(db, alert.model_dump())


@router.get("/", response_model=list[AlertResponse])
def get_alerts(db: Session = Depends(get_db)):
    return alert_service.get_all_alerts(db)


@router.get("/session/{session_id}", response_model=list[AlertResponse])
def get_alerts_by_session(session_id: int, db: Session = Depends(get_db)):
    return alert_service.get_alerts_by_session(db, session_id)


@router.get("/{alert_id}", response_model=AlertResponse)
def get_alert(alert_id: int, db: Session = Depends(get_db)):
    return alert_service.get_alert_by_id(db, alert_id)


@router.delete("/{alert_id}")
def delete_alert(alert_id: int, db: Session = Depends(get_db)):
    return alert_service.delete_alert(db, alert_id)