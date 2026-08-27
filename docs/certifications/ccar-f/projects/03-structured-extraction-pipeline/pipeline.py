"""pipeline.py — Exercise 3: Structured Data Extraction Pipeline (steps 2, 4, 5).

Step 1 (schema with required/optional/nullable fields, "other"+detail enum pattern) lives in
schemas.py. Step 3 (few-shot examples for structural variety) is documented as data below — a real
system embeds these in the extraction prompt, so there is no separate "step 3 function."
"""
from __future__ import annotations

from schemas import validate_extraction

MAX_RETRIES = 2

# Step 3 — few-shot examples spanning structurally different document formats (narrative prose vs
# a table). A real prompt embeds these; kept here as data so "verify structural-variety handling
# improved" (the exercise's own step 3 check) has something concrete to point evaluation at.
PROMPT_EXAMPLES = [
    {"format": "narrative", "excerpt": "Payment of $450.00 is due via bank transfer by March 3rd."},
    {"format": "table", "excerpt": "| Total | $450.00 |\n| Due | 2026-03-03 |\n| Method | Bank Transfer |"},
]


def extract_with_retry(client, document: dict, max_retries: int = MAX_RETRIES) -> dict:
    """Step 2 — a validation-retry loop. On a validation failure, the follow-up call receives the
    document, the failed extraction, and the specific validation error (per the exercise's own
    step 2 wording), so a format mismatch can genuinely self-correct. Returns
    {"fields", "attempts", "resolved_by_retry"} on success, or {"fields": None, "attempts",
    "error"} once retries are exhausted."""
    prior_fields = None
    prior_error = None
    for attempt in range(1, max_retries + 2):  # first try + max_retries follow-ups
        response = client.extract(document, prior_fields=prior_fields, prior_error=prior_error)
        fields = response["fields"]
        errors = validate_extraction(fields)
        if not errors:
            return {"fields": fields, "attempts": attempt, "resolved_by_retry": attempt > 1}
        prior_fields, prior_error = fields, "; ".join(errors)
    return {"fields": None, "attempts": max_retries + 1, "error": prior_error}


def run_batch(client, documents: list[dict]) -> dict:
    """Step 4 — a batch-processing strategy: one `custom_id` per document, failures resubmitted
    once with a modification (chunking an oversized document). `client.submit_batch` returns
    {custom_id: {"status": "succeeded" | "failed", ...}}."""
    batch_request = [{"custom_id": doc["id"], "document": doc} for doc in documents]
    results = client.submit_batch(batch_request)

    resubmit = []
    for custom_id, result in results.items():
        if result["status"] == "failed" and result.get("reason") == "oversized":
            original = next(d for d in documents if d["id"] == custom_id)
            resubmit.append({"custom_id": custom_id, "document": _chunk(original)})

    resubmit_results = client.submit_batch(resubmit) if resubmit else {}

    final = dict(results)
    final.update(resubmit_results)
    succeeded = {k: v for k, v in final.items() if v["status"] == "succeeded"}
    failed = {k: v for k, v in final.items() if v["status"] != "succeeded"}
    return {"succeeded": succeeded, "failed": failed, "resubmitted": list(resubmit_results.keys())}


def _chunk(document: dict) -> dict:
    """Stand-in chunking strategy for an oversized document — splits at the midpoint. Real
    chunking would respect document structure; this exercise only needs the resubmission path."""
    text = document["text"]
    return {**document, "text": text[: len(text) // 2], "chunked": True}


def route_by_confidence(extractions: list[dict], threshold: float = 0.7) -> dict:
    """Step 5 — routes low-confidence field-level extractions to human review, and aggregates
    which fields are weakest so document-type/field accuracy can be analyzed for consistency."""
    auto_accept = []
    human_review = []
    low_confidence_by_field: dict[str, int] = {}

    for extraction in extractions:
        low_fields = [f for f, c in extraction["confidence"].items() if c < threshold]
        if low_fields:
            human_review.append({"doc_id": extraction["doc_id"], "low_confidence_fields": low_fields})
            for f in low_fields:
                low_confidence_by_field[f] = low_confidence_by_field.get(f, 0) + 1
        else:
            auto_accept.append(extraction["doc_id"])

    return {
        "auto_accept": auto_accept,
        "human_review": human_review,
        "low_confidence_by_field": low_confidence_by_field,
    }
