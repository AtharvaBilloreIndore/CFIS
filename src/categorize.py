def categorize_feedback(text: str) -> str:
    text = text.lower()

    if any(word in text for word in ["please", "add", "feature", "enable", "support"]):
        return "Feature Request"

    if any(word in text for word in ["not working", "slow", "late", "crash", "delay", "issue", "problem"]):
        return "Complaint"

    if any(word in text for word in ["love", "great", "excellent", "amazing", "helpful"]):
        return "Praise"

    return "Other"
