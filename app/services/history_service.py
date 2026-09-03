from app.mock_data import HISTORY

def get_route_history(route_key: str) -> dict:
    if route_key not in HISTORY:
        raise ValueError(f"No historical data for route {route_key}")
    return dict(HISTORY[route_key])
