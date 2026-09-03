def evaluate_keywords(answer: str, expected_keywords: list[str]) -> dict:
    text = answer.lower()
    matched = [k for k in expected_keywords if k.lower() in text]
    return {
        "score": len(matched) / len(expected_keywords) if expected_keywords else 1.0,
        "matched": matched,
        "missing": [k for k in expected_keywords if k not in matched],
    }

def evaluate_trace(trace: list[str], expected_agents: list[str]) -> dict:
    text = " ".join(trace).lower()
    matched = [agent for agent in expected_agents if f"{agent}_agent" in text]
    return {
        "score": len(matched) / len(expected_agents) if expected_agents else 1.0,
        "matched": matched,
        "missing": [a for a in expected_agents if a not in matched],
    }
