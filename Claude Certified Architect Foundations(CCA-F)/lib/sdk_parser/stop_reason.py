"""stop_reason handling — turn a Claude Messages API `stop_reason` into a loop decision.

Built for Track B Week 2 (The Agentic Loop by Hand). The whole point of the week: the loop must
branch on the protocol's own signal, not on whether the response happens to contain text.

Offline, no network, no API key — pure mapping + validation.
"""
from __future__ import annotations

from .logger import logger

# stop_reason value -> what the loop should do next
_DECISION = {
    "end_turn": "final",            # model decided it is done -> present final text, break
    "stop_sequence": "final",       # hit a configured stop string -> treat as done
    "tool_use": "call_tools",       # model wants tools -> run every tool_use block, append results
    "pause_turn": "continue",       # long-running server tool -> send response back unchanged
    "max_tokens": "retry_truncated",  # response was cut off -> retry with more budget, do NOT parse
    "refusal": "stop_refused",      # model declined -> stop, surface to caller
}

# stop_reason values for which a text block IS the deliverable
_TEXT_IS_FINAL = {"end_turn", "stop_sequence"}


def classify_stop_reason(stop_reason: str | None) -> str:
    """Map a stop_reason to one of:
    'final' | 'call_tools' | 'continue' | 'retry_truncated' | 'stop_refused' | 'unknown'.
    """
    if stop_reason is None:
        logger.warning("stop_reason is None - SDK per-turn messages often omit it; "
                       "read it off the ResultMessage / final response instead")
        return "unknown"
    decision = _DECISION.get(stop_reason)
    if decision is None:
        logger.warning("unrecognised stop_reason %r — treating as 'unknown'", stop_reason)
        return "unknown"
    return decision


def is_tool_turn(stop_reason: str | None) -> bool:
    """True when the loop must execute tool calls before continuing."""
    return stop_reason == "tool_use"


def text_is_final(stop_reason: str | None) -> bool:
    """True when a text block in this response is the answer to return (not mid-reasoning prose)."""
    return stop_reason in _TEXT_IS_FINAL


def next_step(response) -> str:
    """Convenience: classify straight from a response-like object with a `.stop_reason` attr
    or a dict with a 'stop_reason' key."""
    sr = getattr(response, "stop_reason", None)
    if sr is None and isinstance(response, dict):
        sr = response.get("stop_reason")
    return classify_stop_reason(sr)
