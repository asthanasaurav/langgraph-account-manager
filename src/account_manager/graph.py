from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict, total=False):
    account: str
    renewal_days: int
    contract_value: int
    escalations: int
    risk: str
    recommendation: str
    requires_review: bool
    status: str

ACCOUNTS = {
    "Example-Telecom": {"renewal_days": 90, "contract_value": 12000, "escalations": 0},
    "Example-HighRisk": {"renewal_days": 20, "contract_value": 85000, "escalations": 3},
}

def research(state: State) -> State:
    if state["account"] not in ACCOUNTS:
        raise ValueError("Unknown synthetic account")
    return dict(ACCOUNTS[state["account"]])

def assess(state: State) -> State:
    return {"risk": "high" if state["renewal_days"] <= 30 or state["escalations"] >= 2 else "low"}

def plan(state: State) -> State:
    review = state["risk"] == "high" or state["contract_value"] >= 50000
    return {"requires_review": review, "recommendation": "Escalate for account owner review" if review else "Prepare renewal briefing"}

def route(state: State) -> str:
    return "review" if state["requires_review"] else "draft"

def review(state: State) -> State:
    return {"status": "awaiting_human_review"}

def draft(state: State) -> State:
    return {"status": "draft_ready_no_external_action"}

def build_graph():
    g = StateGraph(State)
    for name, fn in [("research", research), ("assess", assess), ("plan", plan), ("review", review), ("draft", draft)]:
        g.add_node(name, fn)
    g.add_edge(START, "research")
    g.add_edge("research", "assess")
    g.add_edge("assess", "plan")
    g.add_conditional_edges("plan", route)
    g.add_edge("review", END)
    g.add_edge("draft", END)
    return g.compile()
