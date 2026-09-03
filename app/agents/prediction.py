from app.models import FleetState
from app.services.history_service import get_route_history

def prediction_agent(state: FleetState) -> dict:
    shipment = state["findings"]["shipment"]
    history = get_route_history(shipment["route_key"])
    weather = state["findings"].get("weather", {})

    live_weather_delay = float(weather.get("estimated_delay_hours", 0))
    historical_delay = float(history["typical_weather_delay_hours"])
    probability = float(history["weather_delay_probability"])

    predicted_delay = max(live_weather_delay, historical_delay if probability >= 0.20 else 0)

    if predicted_delay >= 3 or probability >= 0.30:
        risk_level = "HIGH"
    elif predicted_delay >= 1 or probability >= 0.15:
        risk_level = "MODERATE"
    else:
        risk_level = "LOW"

    return {
        "findings": {
            "prediction": {
                "predicted_delay_hours": predicted_delay,
                "delay_probability": probability,
                "risk_level": risk_level,
                "historical": history,
            }
        },
        "execution_trace": ["prediction_agent: generated delay prediction"],
    }
