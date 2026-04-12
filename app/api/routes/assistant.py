from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.assistant.llm_client import query_gemini
from app.assistant.prompt_builder import build_prompt
from app.assistant.safety_layer import pre_check
from app.assistant.response_filter import filter_response
from app.models.session import Session as DBSession
from app.services.patient_service import get_patient_by_id, calculate_age
from app.services.alert_service import create_alert
from app.schemas.alert_schema import AlertCreate
from langdetect import detect
import re

router = APIRouter(prefix="/assistant", tags=["Assistant"])


@router.post("/chat")
def chat(user_message: str, session_id: int, db: Session = Depends(get_db)):

    if not pre_check(user_message):
        return {"response": "🚨 Emergency detected. Please seek immediate medical attention."}

    # Detect language
    try:
        language = detect(user_message)
    except:
        language = "unknown"

    # Get session and patient
    session = db.query(DBSession).filter(DBSession.id == session_id).first()
    if not session:
        return {"error": "Session not found"}
    patient = get_patient_by_id(db, session.patient_id)
    if not patient:
        return {"error": "Patient not found"}

    patient_context = {
        "age": calculate_age(patient.date_of_birth),
        "conditions": patient.medical_conditions,
        "allergies": patient.allergies
    }

    prompt = build_prompt(user_message, patient_context, language)

    llm_response = query_gemini(prompt)

    safe_response = filter_response(llm_response)

    # Check for reminders
    reminder_match = re.search(r'\[REMINDER: (.*?)\]', safe_response)
    if reminder_match:
        reminder_message = reminder_match.group(1)
        alert_data = AlertCreate(
            session_id=session_id,
            alert_type="reminder",
            message=reminder_message,
            severity="medium"
        )
        create_alert(db, alert_data.model_dump())
        # Remove the marker from response
        safe_response = re.sub(r'\[REMINDER: .*?\]', '', safe_response).strip()

    return {"response": safe_response}