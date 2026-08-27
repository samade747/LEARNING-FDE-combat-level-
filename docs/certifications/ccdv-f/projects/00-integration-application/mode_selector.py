"""Sample Question 1 (Domain 2 — Applications and Integration): batch vs realtime.

Official guide's own scenario: 10,000 documents, non-urgent, cost is the primary concern, results
needed by next morning. The correct move is the Message Batches API — latency-tolerant, high-volume,
reduced cost within a 24h window — not synchronous parallel calls, not shrinking max_tokens, and not
blindly downsizing the model.
"""
from __future__ import annotations


def choose_processing_mode(volume: int, deadline_hours: float, cost_sensitive: bool) -> dict:
    """Returns {"mode": "batch"|"realtime", "reason": ...}. Batch wins when the workload is large,
    latency-tolerant, and cost matters more than per-item speed. Realtime wins when a user is
    waiting right now — that is the whole tradeoff the sample question is testing."""
    if deadline_hours >= 12 and cost_sensitive and volume >= 100:
        return {
            "mode": "batch",
            "reason": (
                f"{volume} items, {deadline_hours}h deadline, cost-sensitive — Message Batches API "
                "trades latency tolerance for reduced per-item cost; no user is waiting synchronously."
            ),
        }
    return {
        "mode": "realtime",
        "reason": "Either the deadline is tight, the volume is small, or cost isn't the binding constraint.",
    }
