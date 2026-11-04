# LangGraph Account Manager

A safe LangGraph starter for renewal opportunity workflows using **synthetic account data**. No Salesforce integration, LLM calls, outbound messages, or CRM changes yet.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
account-manager --account Example-Telecom
account-manager --account Example-HighRisk
pytest -q
```

## Workflow

`research → assess → plan → review/draft`

High-risk or high-value opportunities are routed to human review; low-risk opportunities produce a proposed briefing only. The graph is deterministic for safe learning and testing.

## Codex workflow

Open this repository in Codex and ask: *Follow AGENTS.md. On a feature branch, add an optional LLM-powered research node with structured output and mocked tests. Keep the default offline path and human approval gates. Open a pull request.*

CI runs pytest on pushes and pull requests. Never commit credentials or real customer data.
