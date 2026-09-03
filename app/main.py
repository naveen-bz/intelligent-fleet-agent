from uuid import uuid4
from fastapi import FastAPI, HTTPException
from app.models import AskRequest, AskResponse
from app.graph import fleet_graph

app = FastAPI(
    title="Intelligent Fleet Agent",
    version="1.0.0",
    description="Multi-agent transportation operations assistant using mock data.",
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/api/v1/ask", response_model=AskResponse)
def ask(request: AskRequest):
    request_id = str(uuid4())

    try:
        result = fleet_graph.invoke({
            "request_id": request_id,
            "question": request.question,
            "shipment_id": request.shipment_id,
            "execution_trace": [],
        })
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))

    return AskResponse(
        request_id=request_id,
        answer=result["final_answer"],
        risk_level=result["risk_level"],
        findings=result["findings"],
        execution_trace=result["execution_trace"],
    )
