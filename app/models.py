from __future__ import annotations
from typing import Any, Annotated, TypedDict
from operator import add
from pydantic import BaseModel, Field

class AskRequest(BaseModel):
    question: str = Field(min_length=3)
    shipment_id: str = "SH123"

class AskResponse(BaseModel):
    request_id: str
    answer: str
    risk_level: str
    findings: dict[str, Any]
    execution_trace: list[str]

class FleetState(TypedDict, total=False):
    request_id: str
    question: str
    shipment_id: str
    required_agents: list[str]
    next_agent_index: int
    findings: dict[str, Any]
    execution_trace: Annotated[list[str], add]
    final_answer: str
    risk_level: str
