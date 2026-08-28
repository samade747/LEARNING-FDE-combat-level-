"""Sample Question 3 (Domain 4 — Evaluation, Testing & Optimization): diagnosing a RAG regression.

Official guide's own scenario: a RAG system starts giving confident-but-incorrect answers right
after a document refresh, while latency and model version are unchanged. The most likely place to
investigate first is retrieval/indexing (stale or irrelevant chunks) — not model weights (nothing
suggests a silent model change), not temperature (unrelated to a document-refresh trigger), and not
the context window (nothing suggests it shrank).
"""
from __future__ import annotations


def diagnose_rag_regression(
    trigger_event: str,
    model_version_changed: bool,
    latency_changed: bool,
) -> dict:
    """Returns the most likely root cause given the observed symptoms. Mirrors the official
    guide's own diagnostic reasoning: a document-refresh trigger with an unchanged model and
    unchanged latency points at retrieval/indexing, not the model or its runtime settings."""
    if trigger_event == "document_refresh" and not model_version_changed and not latency_changed:
        return {
            "most_likely_cause": "retrieval_or_indexing",
            "reason": (
                "Confident-but-wrong answers right after a document refresh, with the model and "
                "latency unchanged, points at the retrieval step returning stale or irrelevant "
                "chunks (a broken re-index or mismatched embeddings) — not the model itself."
            ),
        }
    return {
        "most_likely_cause": "insufficient_evidence",
        "reason": "The document-refresh + unchanged-model/latency pattern is what isolates retrieval as the cause.",
    }
