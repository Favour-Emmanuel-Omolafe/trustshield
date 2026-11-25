"""
TrustShield Core Scoring Engine (Starter Module)
Evaluates text and URL signals for scam, impersonation, and extortion indicators.
"""

from dataclasses import dataclass


@dataclass
class RiskAssessment:
    score: int
    level: str
    signals: list[str]


HIGH_RISK_KEYWORDS = {
    "urgent": 15,
    "suspended": 20,
    "verify": 15,
    "otp": 25,
    "pin": 25,
    "crypto": 20,
    "gift card": 25,
    "extort": 35,
    "blackmail": 35,
    "exposed": 20,
}


def assess_content(text: str, url: str = "") -> RiskAssessment:
    content = (text or "").lower()
    target_url = (url or "").lower()
    score = 0
    signals: list[str] = []

    for phrase, weight in HIGH_RISK_KEYWORDS.items():
        if phrase in content:
            score += weight
            signals.append(f"keyword:{phrase}")

    if any(short in target_url or short in content for short in ("bit.ly", "tinyurl", "t.co", "http://")):
        score += 20
        signals.append("link:suspicious_or_unencrypted")

    final_score = min(100, score)
    if final_score >= 50:
        level = "HIGH"
    elif final_score >= 25:
        level = "MEDIUM"
    else:
        level = "LOW"

    return RiskAssessment(score=final_score, level=level, signals=signals)
