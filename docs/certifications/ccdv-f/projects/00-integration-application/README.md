# CCDV-F — Integration Application (How to Prepare + 3 Sample Questions)

*Official exam guide, Section 7 (How to Prepare) + Section 8 (Sample Questions) — see [`../../03-how-to-prepare-and-sample-questions.md`](../../03-how-to-prepare-and-sample-questions.md). Unlike CCAR-F, the CCDV-F guide does not define 4 numbered exercises — it recommends building "at least one Claude application that exercises the API, integrates 1+ tools, applies basic prompt/context engineering, and includes simple security + evaluation practices," then gives 3 illustrative sample questions (Domains 2, 7, 8). This project is that one application, built directly around those 3 samples.*

A small integration app covering the guide's 3 sample-question domains: a batch-vs-realtime
processing decision (Domain 2), an untrusted-content / prompt-injection guardrail (Domain 7), and
an MCP-server-shaped, reusable inventory tool (Domain 8). No real API calls — every piece is pure
decision logic, fully testable offline.

## Files

- `mode_selector.py` — **Sample 1** (Applications and Integration): `choose_processing_mode()`
  implements the guide's own tradeoff — large, latency-tolerant, cost-sensitive workloads go to
  batch; anything else stays realtime.
- `content_guard.py` — **Sample 2** (Security and Safety): `UntrustedContent` wraps retrieved text
  so it is only ever read as data; `privileged_tool_call()` is a hard gate that rejects any action
  whose instruction source isn't the trusted system prompt.
- `inventory_mcp_tool.py` — **Sample 3** (Tools and MCPs): `InventoryMCPServer`, one server instance
  reused across multiple named "apps" instead of duplicated per-app logic.
- `test_integration_application.py` — 8 offline pytest tests, covering each sample question's own
  correct answer and its named wrong alternatives.

## Kaise Chalayein

```bash
pip install pytest
pytest test_integration_application.py -v
```

## Done Jab (How to Prepare Checklist, Self-Check)

- [x] Kam se kam ek "application" jo API-shaped decision logic exercise kare — `mode_selector.py`
- [x] Kam se kam 1 tool integrate hua — `inventory_mcp_tool.py::TOOL_DEF` + `InventoryMCPServer`
- [x] Basic security practice — `content_guard.py`'s untrusted-content isolation +
      privileged-action gate
- [x] Sample 1 (batch vs realtime) — `pytest::test_sample1_large_non_urgent_cost_sensitive_workload_chooses_batch`
- [x] Sample 2 (prompt injection) — `pytest::test_sample2_injected_instruction_is_flagged_and_never_obeyed` +
      `pytest::test_sample2_untrusted_source_cannot_trigger_a_privileged_action`
- [x] Sample 3 (reusable MCP tool) — `pytest::test_sample3_mcp_server_reused_across_multiple_apps`

## Exam Connection

Each sample question names a plausible-sounding wrong answer, and the tests here are built to fail
against a naive implementation of each one — a `mode_selector` that always picks realtime "for
speed," a `content_guard` that trusts retrieved text, an inventory lookup hard-coded per app. The
guide's own correct answers are the only implementations that pass.

---
[⬅ CCDV-F Projects Index](../README.md)
