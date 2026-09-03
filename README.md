# Intelligent Fleet Agent — Full Working Mock Solution

A runnable multi-agent reference application for transportation operations.

## Features

- FastAPI backend
- LangGraph multi-agent orchestration
- Mock shipment, weather, telematics, and historical-route services
- Supervisor that selects agents based on the user question
- Shipment Agent
- Weather Agent
- Safety Agent
- Prediction Agent
- Evidence-based response synthesizer
- Request tracing
- Golden evaluation dataset
- Pytest unit, API, and workflow tests
- Docker support

## Architecture

```text
                           +------------------+
                           | Backoffice User  |
                           +--------+---------+
                                    |
                                    v
                           +------------------+
                           | FastAPI API      |
                           +--------+---------+
                                    |
                                    v
                           +------------------+
                           | LangGraph        |
                           | Supervisor       |
                           +--------+---------+
                                    |
                  +-----------------+------------------+
                  |                 |                  |
                  v                 v                  v
          Shipment Agent      Weather Agent       Safety Agent
                  |                 |                  |
                  +-----------------+------------------+
                                    |
                                    v
                           Prediction Agent
                                    |
                                    v
                           Response Synthesizer
                                    |
                                    v
                           API Response + Trace
```

## Quick Start

### Option 1: Run locally

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app.main:app --reload
```

Open:

- API documentation: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/health`

### Run the CLI demo

```bash
python -m app.demo
```

### Run tests

```bash
pytest -q
```

## Example API Request

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/ask" \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Will shipment SH123 be delayed? Check weather, route history, and driver safety.\",\"shipment_id\":\"SH123\"}"
```

## Example Response

```json
{
  "request_id": "...",
  "answer": "Shipment SH123 is currently IN_TRANSIT...",
  "risk_level": "HIGH",
  "findings": {},
  "execution_trace": []
}
```

## Mock Data

The application ships with:

| Dataset | Examples |
|---|---|
| Shipments | SH123, SH456, SH789 |
| Weather | Denver→Chicago, Denver→Dallas, Denver→Phoenix |
| Telematics | DRV77, DRV88, DRV99 |
| Route history | Multiple mock corridors |

No external API keys are required.

## Agent Selection

The supervisor uses deterministic routing in this version:

- Always starts with `shipment`
- Weather-related questions add `weather`
- Driver/safety questions add `safety`
- ETA/delay/history questions add `prediction`
- Prediction automatically includes weather because live weather contributes to delay prediction

This is intentional for a reliable, testable mock implementation. In production, the supervisor can be replaced with an LLM planner while keeping policy checks deterministic.

## Evaluation

Golden cases are stored in:

```text
evaluation/datasets/golden_cases.json
```

The project evaluates:

- Required agent execution
- Required answer keywords
- Deterministic safety score calculation
- Tool lookup behavior
- API response behavior

## Production Extension Points

Replace the files under `app/services/` with:

- MCP clients
- Enterprise shipment APIs
- Weather APIs
- Telematics systems
- Routing systems
- RAG/vector retrieval
- Historical data warehouse queries

Recommended control path:

```text
Agent -> Tool/MCP Client -> Policy Layer -> Enterprise System
```

Do not allow an LLM alone to make authorization decisions.

## Project Layout

```text
app/
  api/
  agents/
  services/
  graph.py
  models.py
  main.py
  demo.py
evaluation/
  datasets/
  evaluators.py
  run_evaluation.py
tests/
Dockerfile
docker-compose.yml
requirements.txt
```
