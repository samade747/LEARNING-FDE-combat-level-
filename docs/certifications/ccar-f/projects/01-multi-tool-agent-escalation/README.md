# CCAR-F Exercise 1 — Multi-Tool Agent with Escalation Logic

*Official exam guide, Section 8, Exercise 1 (see [`../../03-how-to-prepare-and-sample-questions.md`](../../03-how-to-prepare-and-sample-questions.md)). Also Track B syllabus's **Required Architect Project 2** (Week 5). Domains reinforced: 1 (Agentic Architecture & Orchestration), 2 (Tool Design & MCP Integration), 5 (Context Management & Reliability).*

Hand-rolled agentic loop (raw Messages API — no Claude Agent SDK, that course is still unpublished, see `docs/certifications/07-practice-log.md`). Four tools over a fake in-memory CRM, structured tool errors, and one thing the exam's own Q1 sample question is built around: **a programmatic hook that verifies the customer before any order-touching tool runs**, because prompt wording alone lets that slip in production.

## Files

- `tools.py` — 4 tools (`get_customer`, `lookup_order`, `process_refund`, `update_shipping_address`), each raising a structured `ToolError(errorCategory, isRetryable, message)` on failure.
- `hooks.py` — the PreToolUse-style gate: blocks any order tool until `get_customer` has verified a `customer_id`, and blocks refunds above `$500` regardless of verification (auto-escalate).
- `agent.py` — the loop itself. Reads `stop_reason`, never guesses completion from prose. Handles multiple `tool_use` blocks in one turn (multi-concern requests).
- `test_agent.py` — offline verification via a `FakeClient` that plays back scripted API responses.

## Kaise Chalayein

**Offline (no API key, no cost) — the actual verification:**
```bash
pip install -r requirements.txt
pytest test_agent.py -v
```

**Live (needs your own `ANTHROPIC_API_KEY` from console.anthropic.com — separate from Claude Code login):**
```bash
export ANTHROPIC_API_KEY=sk-ant-...
python agent.py
```

## Done Jab (Official Exercise's 5 Steps, Self-Check)

- [x] 4 tools, 2 of them similar-shaped (`lookup_order`/`update_shipping_address` both take `customer_id`+`order_id`) — descriptions differentiate them
- [x] Loop checks `stop_reason` (`tool_use` vs `end_turn`), not prose parsing
- [x] Structured errors: `errorCategory` (transient/validation/business/permission) + `isRetryable`
- [x] Programmatic hook blocks a business rule (verify-before-touch) and redirects to escalation — `pytest::test_hook_blocks_unverified_order_touch_and_escalates`
- [x] Multi-concern message (refund + address update in one ask) → both tool calls happen in one turn — `pytest::test_verified_customer_can_touch_orders_and_multi_tool_turn_works`

## Exam Connection

This is the exact shape of Sample Question 1 in [`03-how-to-prepare-and-sample-questions.md`](../../03-how-to-prepare-and-sample-questions.md): production data shows 12% of cases skip verification. The correct fix (**A** in that question) is a programmatic prerequisite gate — `hooks.py::enforce_prerequisites` is that gate, built and tested.

---
[⬅ CCAR-F Projects Index](../README.md)
