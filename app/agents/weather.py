from app.models import FleetState
from app.services.weather_service import get_route_weather

def weather_agent(state: FleetState) -> dict:
    shipment = state["findings"]["shipment"]
    weather = get_route_weather(shipment["route_key"])
    return {
        "findings": {"weather": weather},
        "execution_trace": [f"weather_agent: analyzed {shipment['route_key']}"],
    }
