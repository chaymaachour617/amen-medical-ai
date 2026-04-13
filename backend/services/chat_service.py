from langdetect import detect
from app.assistant.prompt_builder import build_prompt
from app.services.llm_service import generate_response
def handle_chat(user_message: str):

    # 1️⃣ Detect language
    try:
        language = detect(user_message)
    except:
        language = "unknown"

    # 2️⃣ Build prompt
   prompt = build_prompt(user_message, patient_context, language)
    # 3️⃣ Call LLM
    response = generate_response(prompt)

    return response