def build_prompt(user_message: str, patient_context: dict):

    base_instruction = """
You are a medical assistant.
You must provide safe, non-diagnostic guidance.
Never prescribe medication.
Encourage professional consultation when necessary.
"""

    context_section = f"""
Patient Information:
Age: {patient_context.get("age")}
Medical Conditions: {patient_context.get("conditions")}
Allergies: {patient_context.get("allergies")}
"""

    final_prompt = f"""
{base_instruction}

{context_section}

User Question:
{user_message}

Assistant:
"""

    return final_prompt
