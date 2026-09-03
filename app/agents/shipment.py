from app.models import FleetState
from app.services.shipment_service import get_shipment

def shipment_agent(state: FleetState) -> dict:
    shipment = get_shipment(state["shipment_id"])
    return {
        "findings": {"shipment": shipment},
        "execution_trace": [f"shipment_agent: loaded {shipment['shipment_id']}"],
    }
