from app.models import FleetState

RISK_ORDER = {"LOW": 1, "MODERATE": 2, "HIGH": 3}

def synthesizer_agent(state: FleetState) -> dict:
    findings = state["findings"]
    shipment = findings["shipment"]
    weather = findings.get("weather")
    safety = findings.get("safety")
    prediction = findings.get("prediction")

    risks = []
    if weather:
        risks.append(weather["risk_level"])
    if safety:
        risks.append(safety["risk_level"])
    if prediction:
        risks.append(prediction["risk_level"])
    overall = max(risks, key=lambda x: RISK_ORDER[x]) if risks else "LOW"

    lines = [
        f"Shipment {shipment['shipment_id']} is currently {shipment['status']}.",
        f"Current ETA is approximately {shipment['current_eta_hours']} hours.",
        f"Overall operational risk: {overall}.",
    ]

    if weather:
        lines.append(
            f"Weather risk is {weather['risk_level']} with conditions: "
            + "; ".join(weather["conditions"]) + "."
        )
        lines.append(f"Estimated weather-related delay: {weather['estimated_delay_hours']} hours.")

    if prediction:
        lines.append(
            f"Historical delay probability is {prediction['delay_probability']:.0%}; "
            f"predicted additional delay is {prediction['predicted_delay_hours']} hours."
        )

    if safety:
        lines.append(
            f"Driver safety score is {safety['score']}/100 "
            f"with {safety['risk_level']} safety risk."
        )

    if overall == "HIGH":
        action = "Recommended action: proactively notify operations and monitor the shipment for escalation."
    elif overall == "MODERATE":
        action = "Recommended action: continue active monitoring and prepare the receiving operation for a possible delay."
    else:
        action = "Recommended action: continue normal monitoring."

    lines.append(action)

    return {
        "final_answer": "
".join(lines),
        "risk_level": overall,
        "execution_trace": ["synthesizer_agent: created final operational recommendation"],
    }
