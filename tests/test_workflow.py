from app.graph import fleet_graph

def run(question, shipment_id):
    return fleet_graph.invoke({
        "request_id": "test",
        "question": question,
        "shipment_id": shipment_id,
        "execution_trace": [],
    })

def test_delay_workflow():
    result = run(
        "Will shipment SH123 be delayed? Check weather and route history.",
        "SH123",
    )
    trace = " ".join(result["execution_trace"])
    assert "shipment_agent" in trace
    assert "weather_agent" in trace
    assert "prediction_agent" in trace
    assert result["risk_level"] == "HIGH"

def test_safety_workflow():
    result = run("Check driver safety for shipment SH456.", "SH456")
    assert "safety_agent" in " ".join(result["execution_trace"])
    assert result["risk_level"] == "HIGH"

def test_basic_shipment_query():
    result = run("Tell me about shipment SH789.", "SH789")
    assert "Shipment SH789" in result["final_answer"]
    assert "weather_agent" not in " ".join(result["execution_trace"])
