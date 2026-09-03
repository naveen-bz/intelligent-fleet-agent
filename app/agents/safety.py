from app.models import FleetState
from app.services.telematics_service import (
    get_driver_telematics,
    calculate_safety_score,
    safety_band,
)

def safety_agent(state: FleetState) -> dict:
    shipment = state["findings"]["shipment"]
    telemetry = get_driver_telematics(shipment["driver_id"])
    score = calculate_safety_score(telemetry)
    return {
        "findings": {
            "safety": {
                "score": score,
                "risk_level": safety_band(score),
                "telemetry": telemetry,
            }
        },
        "execution_trace": ["safety_agent: calculated driver safety risk"],
    }
