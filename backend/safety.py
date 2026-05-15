EMERGENCY_KEYWORDS = [
    "chest pain", "difficulty breathing", "severe bleeding",
    "unconscious", "stroke", "heart attack", "suicide",
    "seizure", "blood vomiting"
]

def check_emergency(user_input):
    text = user_input.lower()
    for keyword in EMERGENCY_KEYWORDS:
        if keyword in text:
            return True
    return False