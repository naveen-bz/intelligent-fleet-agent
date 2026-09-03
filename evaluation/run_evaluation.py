import json
from pathlib import Path
from app.graph import fleet_graph
from evaluation.evaluators import evaluate_keywords, evaluate_trace

dataset = json.loads(
    (Path(__file__).parent / "datasets" / "golden_cases.json").read_text()
)

for case in dataset:
    result = fleet_graph.invoke({
        "request_id": case["id"],
        "question": case["question"],
        "shipment_id": case["shipment_id"],
        "execution_trace": [],
    })
    keyword_eval = evaluate_keywords(result["final_answer"], case["expected_keywords"])
    trace_eval = evaluate_trace(result["execution_trace"], case["expected_agents"])

    print(f"\n{case['id']}")
    print("Keyword score:", keyword_eval["score"])
    print("Trace score:", trace_eval["score"])
