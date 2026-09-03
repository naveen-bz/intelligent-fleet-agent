from app.mock_data import WEATHER

def get_route_weather(route_key: str) -> dict:
    if route_key not in WEATHER:
        raise ValueError(f"No weather data for route {route_key}")
    return dict(WEATHER[route_key])
