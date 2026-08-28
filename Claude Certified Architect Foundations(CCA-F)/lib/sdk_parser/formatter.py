"""Formats a parsed Claude Messages API response into a short, human-readable summary line.

Starter module — extend as the parser grows. Kept intentionally small: one function, no
external dependencies, so it can be tested without a real API call.
"""
from __future__ import annotations

from .logger import logger


def format_response_summary(response: dict) -> str:
    """response is a dict shaped like a Messages API response: {"stop_reason": ..., "content": [...]}."""
    stop_reason = response.get("stop_reason", "unknown")
    content = response.get("content", [])
    block_types = [block.get("type", "?") for block in content]
    summary = f"stop_reason={stop_reason} blocks={block_types}"
    logger.info(summary)
    return summary
