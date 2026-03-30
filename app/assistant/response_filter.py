def filter_response(response: str):

    forbidden_phrases = [
        "take this medication",
        "increase your dose"
    ]

    for phrase in forbidden_phrases:
        if phrase in response.lower():
            return "⚠️ Please consult a healthcare professional."

    return response