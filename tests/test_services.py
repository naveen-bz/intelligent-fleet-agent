import pytest
from app.services.shipment_service import get_shipment
from app.services.telematics_service import calculate_safety_score

def test_shipment_exists():
    assert get_shipment("SH123")["destination"] == "Chicago, IL"

def test_unknown_shipment():
    with pytest.raises(ValueError):
        get_shipment("UNKNOWN")

def test_safety_score():
    assert calculate_safety_score({
        "hard_braking_events": 2,
        "speeding_events": 1,
        "fatigue_indicator": False,
    }) == 86
