import re


URGENCY_WORDS = [
    "urgent",
    "immediately",
    "now",
    "today",
    "within 10 minutes",
    "last chance",
    "act fast",
    "तुरंत",
    "अभी",
    "आज",
    "जल्दी"
]

AUTHORITY_WORDS = [
    "electricity department",
    "bank officer",
    "police",
    "government",
    "rbi",
    "official",
    "electricity board",
    "बिजली विभाग",
    "पुलिस",
    "सरकार"
]

PAYMENT_WORDS = [
    "pay",
    "payment",
    "upi",
    "transfer",
    "refund",
    "verification",
    "₹",
    "rs",
    "रिफंड",
    "भुगतान"
]

DANGER_WORDS = [
    "otp",
    "pin",
    "mpin",
    "password",
    "disconnect",
    "blocked",
    "suspended",
    "disconnection",
    "ओटीपी",
    "बंद",
    "डिस्कनेक्ट"
]


def detect_scam(message):

    text = message.lower()

    detected = []
    score = 0

    # Urgency
    urgency_found = [
        word for word in URGENCY_WORDS
        if word in text
    ]

    if urgency_found:
        score += 25
        detected.append("Urgency / Pressure")

    # Authority
    authority_found = [
        word for word in AUTHORITY_WORDS
        if word in text
    ]

    if authority_found:
        score += 20
        detected.append("Authority Claim")

    # Payment
    payment_found = [
        word for word in PAYMENT_WORDS
        if word in text
    ]

    if payment_found:
        score += 25
        detected.append("Payment / Refund Request")

    # OTP / threat
    danger_found = [
        word for word in DANGER_WORDS
        if word in text
    ]

    if danger_found:
        score += 30
        detected.append("Sensitive Information / Threat")

    score = min(score, 100)

    if score >= 70:
        level = "HIGH RISK"
    elif score >= 40:
        level = "MEDIUM RISK"
    else:
        level = "LOW RISK"

    return {
        "score": score,
        "level": level,
        "detected": detected
    }