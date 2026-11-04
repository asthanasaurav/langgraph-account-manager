# Codex instructions

- Python 3.11+, LangGraph StateGraph, synthetic data only.
- Keep deterministic offline behavior by default.
- Never commit credentials, customer data, or `.env` files.
- Do not send customer communications or modify CRM without explicit human approval.
- Add mocked tests for LLM or API integrations; run `pytest -q`.
- Work on feature branches and open PRs.
