SHIPMENTS = {
    "SH123": {
        "shipment_id": "SH123",
        "origin": "Denver, CO",
        "destination": "Chicago, IL",
        "status": "IN_TRANSIT",
        "current_eta_hours": 19,
        "driver_id": "DRV77",
        "route_key": "DEN-CHI",
    },
    "SH456": {
        "shipment_id": "SH456",
        "origin": "Denver, CO",
        "destination": "Dallas, TX",
        "status": "IN_TRANSIT",
        "current_eta_hours": 11,
        "driver_id": "DRV88",
        "route_key": "DEN-DAL",
    },
    "SH789": {
        "shipment_id": "SH789",
        "origin": "Denver, CO",
        "destination": "Phoenix, AZ",
        "status": "ON_TIME",
        "current_eta_hours": 13,
        "driver_id": "DRV99",
        "route_key": "DEN-PHX",
    },
}

WEATHER = {
    "DEN-CHI": {
        "risk_level": "HIGH",
        "conditions": ["Severe thunderstorms near Omaha", "Heavy rain near Chicago"],
        "estimated_delay_hours": 3.0,
    },
    "DEN-DAL": {
        "risk_level": "MODERATE",
        "conditions": ["Strong crosswinds in Kansas"],
        "estimated_delay_hours": 1.0,
    },
    "DEN-PHX": {
        "risk_level": "LOW",
        "conditions": ["Clear driving conditions"],
        "estimated_delay_hours": 0.0,
    },
}

TELEMATICS = {
    "DRV77": {"hard_braking_events": 2, "speeding_events": 1, "fatigue_indicator": False},
    "DRV88": {"hard_braking_events": 5, "speeding_events": 4, "fatigue_indicator": True},
    "DRV99": {"hard_braking_events": 0, "speeding_events": 0, "fatigue_indicator": False},
}

HISTORY = {
    "DEN-CHI": {
        "average_transit_hours": 18.0,
        "weather_delay_probability": 0.32,
        "typical_weather_delay_hours": 2.5,
        "sample_size": 420,
    },
    "DEN-DAL": {
        "average_transit_hours": 10.5,
        "weather_delay_probability": 0.18,
        "typical_weather_delay_hours": 1.0,
        "sample_size": 350,
    },
    "DEN-PHX": {
        "average_transit_hours": 12.5,
        "weather_delay_probability": 0.08,
        "typical_weather_delay_hours": 0.5,
        "sample_size": 510,
    },
}
