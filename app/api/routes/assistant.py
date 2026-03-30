from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.assistant.llm_client import query_gemini
from app.assistant.prompt_builder import build_prompt
from app.assistant.safety_layer import pre_check
from app.assistant.response_filter import filter_response

router = APIRouter(prefix="/assistant", tags=["Assistant"])


@router.post("/chat")
def chat(user_message: str, db: Session = Depends(get_db)):

    if not pre_check(user_message):
        return {"response": "🚨 Emergency detected. Please seek immediate medical attention."}

    patient_context = {
        "age": 30,
        "conditions": "None",
        "allergies": "Penicillin"
    }

    prompt = build_prompt(user_message, patient_context)

    llm_response = query_gemini(prompt)

    safe_response = filter_response(llm_response)

    return {"response": safe_response}