def pre_check(message: str):

    emergency_keywords = [
        "suicide",
        "heart attack",
        "cannot breathe",
        "overdose"
    ]

    for word in emergency_keywords:
        if word in message.lower():
            return False

    return True