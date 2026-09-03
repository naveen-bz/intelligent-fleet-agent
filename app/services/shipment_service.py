from app.mock_data import SHIPMENTS

def get_shipment(shipment_id: str) -> dict:
    if shipment_id not in SHIPMENTS:
        raise ValueError(f"Shipment {shipment_id} was not found")
    return dict(SHIPMENTS[shipment_id])
