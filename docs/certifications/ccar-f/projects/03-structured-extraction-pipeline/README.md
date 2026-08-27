# CCAR-F Exercise 3 — Build a Structured Data Extraction Pipeline

*Official exam guide, Section 8, Exercise 3 (see [`../../03-how-to-prepare-and-sample-questions.md`](../../03-how-to-prepare-and-sample-questions.md)). Also Track B syllabus's **Required Architect Project 3** (Week 10). Domains reinforced: 4 (Prompt Engineering & Structured Output), 5 (Context Management & Reliability).*

An invoice-extraction pipeline covering the exercise's full 5-step shape: a nullable-field JSON
schema (`tool_use`), a validation-retry loop, few-shot examples for structural variety, Message-
Batches-style batch processing with `custom_id` + resubmission, and confidence-routed human review.
No real API calls — everything is driven by a `FakeExtractionClient` so the pipeline's *control
flow* is fully testable offline.

## Files

- `schemas.py` — the extraction tool's JSON schema: required + nullable fields, an "other" +
  `payment_method_detail` enum pattern, and `validate_extraction()`, a dependency-free stand-in for
  a Pydantic/JSON-schema validator.
- `pipeline.py` — `extract_with_retry` (step 2: validation-retry loop with the specific error fed
  back), `PROMPT_EXAMPLES` (step 3: few-shot data for structurally different document formats),
  `run_batch` (step 4: `custom_id`-per-document batch + resubmission of oversized documents),
  `route_by_confidence` (step 5: low-confidence fields routed to human review).
- `test_pipeline.py` — 5 offline pytest tests covering each step's own success condition.

## Kaise Chalayein

```bash
pip install pytest
pytest test_pipeline.py -v
```

## Done Jab (Official Exercise's 5 Steps, Self-Check)

- [x] Nullable-field schema + "other"+detail enum pattern — `schemas.py::EXTRACTION_TOOL_DEF`
- [x] Missing info returns `null`, not a fabricated value — `pytest::test_missing_info_returns_null_not_fabricated`
- [x] Validation-retry loop resolves a format mismatch, and exhausts cleanly on a persistent one —
      `pytest::test_validation_retry_resolves_a_format_mismatch` +
      `pytest::test_validation_retry_exhausts_on_a_persistent_error`
- [x] Few-shot examples for structural variety (narrative vs table) — `pipeline.py::PROMPT_EXAMPLES`
- [x] Batch strategy: `custom_id` per document, oversized documents chunked + resubmitted —
      `pytest::test_batch_resubmits_oversized_documents`
- [x] Confidence-routed human review, aggregated by field — `pytest::test_confidence_routing_separates_low_confidence_fields`

## Exam Connection

The exercise's own step 1 names the trap directly: a model asked to extract a field that is not in
the document should return `null`, never a plausible-looking guess. `schemas.py::validate_extraction`
treats a present-but-null field as **valid** (not an error) — that is the whole point. What *is* an
error is a value outside the declared enum, which is exactly what the validation-retry loop exists
to catch and correct.

---
[⬅ CCAR-F Projects Index](../README.md)
