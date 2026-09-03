from app.mock_data import TELEMATICS

def get_driver_telematics(driver_id: str) -> dict:
    if driver_id not in TELEMATICS:
        raise ValueError(f"No telematics data for driver {driver_id}")
    return dict(TELEMATICS[driver_id])

def calculate_safety_score(data: dict) -> int:
    score = 100
    score -= data["hard_braking_events"] * 5
    score -= data["speeding_events"] * 4
    if data["fatigue_indicator"]:
        score -= 20
    return max(score, 0)

def safety_band(score: int) -> str:
    if score >= 90:
        return "LOW"
    if score >= 70:
        return "MODERATE"
    return "HIGH"
