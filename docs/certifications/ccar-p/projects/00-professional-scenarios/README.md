# CCAR-P — Professional Scenarios (3 Official Sample Questions)

*Official exam guide, Section 8 — see [`../../03-how-to-prepare-and-sample-questions.md`](../../03-how-to-prepare-and-sample-questions.md). CCAR-P builds on CCAR-F (see [`01-domain-blueprint.md`](../../01-domain-blueprint.md) "CCAR-F Se Farq") with two new domains — Governance/Safety/Risk (14%) and Stakeholder Communication/Lifecycle (14%) — plus a wider-scope Integration domain (19%, the heaviest). This project implements all 3 sample questions, from Domains 3, 2, and 4.*

Three independent decision-logic modules, each built directly around one official sample question:
least-privilege tool configuration, prompt-caching-aware ordering, and RAG-regression diagnosis. No
real API calls — pure decision logic, fully testable offline.

## Files

- `least_privilege.py` — **Sample 1** (Domain 3, Integration): `enforce_least_privilege()` removes
  tools a role doesn't need, rather than adding logging/confirmation on top of an over-permissioned
  config.
- `prompt_ordering.py` — **Sample 2** (Domain 2, Prompting & Context): `build_cached_prompt()`
  orders stable content before varying content and marks it cacheable; `is_cache_effective()`
  catches the broken case where dynamic content is placed before the stable prefix.
- `rag_diagnostics.py` — **Sample 3** (Domain 4, Evaluation & Optimization):
  `diagnose_rag_regression()` isolates retrieval/indexing as the likely cause when the symptom
  pattern (document refresh, model + latency unchanged) matches the official scenario.
- `test_professional_scenarios.py` — 6 offline pytest tests, covering each sample's correct answer
  and a case that should NOT trigger the same conclusion.

## Kaise Chalayein

```bash
pip install pytest
pytest test_professional_scenarios.py -v
```

## Done Jab (3 Sample Questions, Self-Check)

- [x] Least privilege removes unneeded tools entirely (not just logs/confirms them) —
      `pytest::test_sample1_support_staff_loses_refund_and_delete_tools`
- [x] Cache-aware ordering puts stable content first, marked cacheable —
      `pytest::test_sample2_static_content_ordered_before_dynamic_and_marked_cacheable`
- [x] RAG regression correctly isolates retrieval as the cause when the symptom pattern matches —
      `pytest::test_sample3_document_refresh_with_stable_model_points_at_retrieval`

## Exam Connection

Domain 3 (Integration, 19%) is CCAR-P's heaviest domain — wider in scope than CCAR-F's "Tool Design
& MCP" (18%): RAG pipeline design, observability at scale, and protocol selection (MCP vs API/CLI vs
agent-to-agent) are all explicit objectives here, not just tool descriptions and structured errors.

---
[⬅ CCAR-P Projects Index](../README.md)
