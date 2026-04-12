def build_prompt(user_message: str, patient_context: dict, language: str):

    # 🎯 SYSTEM LANGUAGE RULES
    if language == "ar":
        system_prompt = """
أنت AMEN مساعد طبي للتحضير الطبي.
أجب باللغة العربية.
كن مطمئناً وواضحاً.
لا تقدم تشخيصاً.
قدم إرشادات عامة وآمنة فقط.
"""
    else:
        system_prompt = """
You are AMEN, a medical preparation assistant.
Speak in the same language as the patient.
Be warm, reassuring, and clear.
Do NOT diagnose.
Give safe general medical guidance only.
Keep answers concise.
"""

    base_instruction = """
You are a medical assistant.
You must provide safe, non-diagnostic guidance.
Never prescribe medication.
Encourage professional consultation when necessary.
If appropriate, suggest reminders for important actions like taking medication or follow-up appointments.
If you suggest a reminder, include it in your response as [REMINDER: reminder message].
"""


    context_section = f"""
Patient Information:
Age: {patient_context.get("age")}
Medical Conditions: {patient_context.get("conditions")}
Allergies: {patient_context.get("allergies")}
"""
    final_prompt = f"""
{system_prompt}

{base_instruction}

{context_section}

User Question:
{user_message}

Assistant:
"""
    return final_prompt