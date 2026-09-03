from langgraph.graph import StateGraph, END

from app.models import FleetState
from app.agents.shipment import shipment_agent
from app.agents.weather import weather_agent
from app.agents.safety import safety_agent
from app.agents.prediction import prediction_agent
from app.agents.synthesizer import synthesizer_agent

def supervisor(state: FleetState) -> dict:
    query = state["question"].lower()
    agents = ["shipment"]

    if any(word in query for word in ["weather", "storm", "rain", "wind", "route"]):
        agents.append("weather")

    if any(word in query for word in ["driver", "safety", "telematics", "braking", "speeding"]):
        agents.append("safety")

    if any(word in query for word in ["delay", "eta", "predict", "prediction", "historical"]):
        agents.append("prediction")

    # Delay prediction requires live weather in this reference implementation.
    if "prediction" in agents and "weather" not in agents:
        agents.insert(1, "weather")

    return {
        "required_agents": agents,
        "next_agent_index": 0,
        "findings": {},
        "execution_trace": [f"supervisor: selected agents={agents}"],
    }

def choose_next(state: FleetState) -> str:
    index = state.get("next_agent_index", 0)
    agents = state["required_agents"]
    if index >= len(agents):
        return "synthesizer"
    return agents[index]

def advance(state: FleetState) -> dict:
    return {"next_agent_index": state.get("next_agent_index", 0) + 1}

def build_graph():
    workflow = StateGraph(FleetState)

    workflow.add_node("supervisor", supervisor)
    workflow.add_node("shipment", shipment_agent)
    workflow.add_node("weather", weather_agent)
    workflow.add_node("safety", safety_agent)
    workflow.add_node("prediction", prediction_agent)
    workflow.add_node("advance", advance)
    workflow.add_node("synthesizer", synthesizer_agent)

    workflow.set_entry_point("supervisor")

    routes = {
        "shipment": "shipment",
        "weather": "weather",
        "safety": "safety",
        "prediction": "prediction",
        "synthesizer": "synthesizer",
    }

    workflow.add_conditional_edges("supervisor", choose_next, routes)

    for node in ["shipment", "weather", "safety", "prediction"]:
        workflow.add_edge(node, "advance")

    workflow.add_conditional_edges("advance", choose_next, routes)
    workflow.add_edge("synthesizer", END)

    return workflow.compile()

fleet_graph = build_graph()
