from app.graph import fleet_graph

questions = [
    ("Will shipment SH123 be delayed? Check weather, route history, and driver safety.", "SH123"),
    ("What is the driver safety risk for shipment SH456?", "SH456"),
    ("Give me the current ETA for shipment SH789.", "SH789"),
]

for question, shipment_id in questions:
    print("=" * 80)
    print("QUESTION:", question)
    result = fleet_graph.invoke({
        "request_id": "demo",
        "question": question,
        "shipment_id": shipment_id,
        "execution_trace": [],
    })
    print("\nANSWER:\n", result["final_answer"])
    print("\nTRACE:")
    for item in result["execution_trace"]:
        print(" -", item)
