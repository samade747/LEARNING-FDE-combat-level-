"""Sample Question 2 (Domain 2 — Models, Prompting & Context Engineering): prompt-caching-aware
ordering.

Official guide's own scenario: an application sends the same 8,000-token system prompt + policy
document on every request, followed by a small, varying user message. Latency AND cost are both
concerns. The fix is ordering stable content first and enabling prompt caching — not truncating the
policy (loses required content), not blindly downsizing the model, and not relocating the policy
into a few-shot block (that doesn't create a reusable cacheable prefix).
"""
from __future__ import annotations


def build_cached_prompt(static_system_prompt: str, static_policy: str, dynamic_user_message: str) -> dict:
    """Returns the blocks in cache-correct order: everything stable and shared across requests
    comes first (and is marked cacheable), the varying part comes last."""
    return {
        "blocks": [
            {"content": static_system_prompt, "cache_control": {"type": "ephemeral"}},
            {"content": static_policy, "cache_control": {"type": "ephemeral"}},
            {"content": dynamic_user_message, "cache_control": None},
        ],
        "cacheable_prefix_tokens_estimate": len(static_system_prompt) + len(static_policy),
    }


def is_cache_effective(blocks: list[dict]) -> bool:
    """A cached prefix only helps if the stable blocks come BEFORE the varying one — caching a
    prefix that changes every request (because the varying content was placed first) provides no
    reuse benefit at all."""
    seen_dynamic = False
    for block in blocks:
        if block["cache_control"] is None:
            seen_dynamic = True
        elif seen_dynamic:
            return False  # a cacheable block appears AFTER a dynamic one — prefix isn't stable
    return True
