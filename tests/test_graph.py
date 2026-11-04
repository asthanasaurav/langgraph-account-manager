import pytest
from account_manager.graph import build_graph

def test_low_risk():
    result = build_graph().invoke({"account": "Example-Telecom"})
    assert result["risk"] == "low"
    assert result["status"] == "draft_ready_no_external_action"

def test_high_risk():
    result = build_graph().invoke({"account": "Example-HighRisk"})
    assert result["requires_review"] is True
    assert result["status"] == "awaiting_human_review"

def test_unknown_account():
    with pytest.raises(ValueError):
        build_graph().invoke({"account": "Unknown"})
