from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_ask():
    response = client.post(
        "/api/v1/ask",
        json={
            "question": "Will shipment SH123 be delayed because of weather?",
            "shipment_id": "SH123",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["risk_level"] == "HIGH"
    assert "Shipment SH123" in data["answer"]

def test_unknown_shipment():
    response = client.post(
        "/api/v1/ask",
        json={"question": "Check this shipment", "shipment_id": "UNKNOWN"},
    )
    assert response.status_code == 404
