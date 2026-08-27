"""fixed_loop.py — reference implementation with all five broken_loop.py bugs corrected.

Fixes: append full history every turn (BUG 1); always append tool_results back into messages
(BUG 2); check stop_reason, not "text present" (BUG 3); enforce MAX_TURNS as a real ceiling
(BUG 4); execute every tool_use block in a turn, not just the first (BUG 5).
"""
from __future__ import annotations

MODEL = "claude-haiku-4-5-20251001"
MAX_TURNS = 6


def agent_loop(client, user_message: str) -> dict:
    messages = [{"role": "user", "content": user_message}]
    for _ in range(MAX_TURNS):
        response = client.messages.create(model=MODEL, max_tokens=1024, messages=messages)
        messages.append({"role": "assistant", "content": response.content})  # fixes BUG 1

        if response.stop_reason == "end_turn":  # fixes BUG 3 — stop_reason decides, not "text present"
            return {"final_text": _text(response)}

        if response.stop_reason != "tool_use":
            return {"final_text": None, "stop_reason": response.stop_reason}

        tool_results = []
        for block in _tool_use_blocks(response):  # fixes BUG 5 — every block, not just [0]
            result = client.execute_tool(block.name, block.input)
            tool_results.append({"type": "tool_result", "tool_use_id": block.id, "content": str(result)})
        messages.append({"role": "user", "content": tool_results})  # fixes BUG 2

    return {"final_text": None, "error": "max turns exceeded"}  # fixes BUG 4 — a real ceiling


def _text(response) -> str:
    return "".join(b.text for b in response.content if getattr(b, "type", None) == "text")


def _tool_use_blocks(response):
    return [b for b in response.content if getattr(b, "type", None) == "tool_use"]


if __name__ == "__main__":
    import os

    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise SystemExit("Set ANTHROPIC_API_KEY to run live. Otherwise: pytest test_loop.py")

    import anthropic

    client = anthropic.Anthropic()
    print(agent_loop(client, "What's 2+2? Just answer directly, no tools needed."))
