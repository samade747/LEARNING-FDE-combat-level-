"""Exercise 1 — Multi-Tool Agent with Escalation Logic.

A hand-rolled agentic loop against the raw Messages API (no Claude Agent SDK — that course is
still unpublished per docs/certifications/07-practice-log.md, and Track B Week 2 "The Loop by
Hand" builds exactly this shape by hand anyway). Implements every step of the official exercise:

1. 3-4 well-described tools with two similar ones (lookup_order/update_shipping_address both take
   customer_id+order_id) — see tools.py.
2. A loop that reads `stop_reason` to decide whether to keep calling tools or stop.
3. Structured tool errors (errorCategory/isRetryable) — see tools.py's ToolError.
4. A programmatic hook enforcing a business rule (verify-before-touch, refund threshold) — hooks.py.
5. Multi-concern requests: one turn can contain several tool_use blocks; all are executed and all
   results returned before the next model call.

Run for real: set ANTHROPIC_API_KEY and `python agent.py`.
Run offline (no API key, no cost): `pytest test_agent.py -v` — it drives this same loop against a
FakeClient with canned responses.
"""
from __future__ import annotations

import os

from hooks import Escalate, enforce_prerequisites, record_verification
from tools import TOOLS, ANTHROPIC_TOOL_DEFS, ToolError

MODEL = "claude-haiku-4-5-20251001"
MAX_TURNS = 8

SYSTEM_PROMPT = (
    "You are a customer-support agent for an online store. You have four tools: get_customer, "
    "lookup_order, process_refund, update_shipping_address. Always verify the customer with "
    "get_customer before calling any tool that touches an order. If a tool call is blocked or "
    "escalated, explain to the user that this needs human review — do not retry it yourself."
)


def run_turn(client, tool_name: str, tool_input: dict, session_state: dict) -> dict:
    """Execute one tool call through the hook gate. Returns an Anthropic tool_result content block."""
    try:
        enforce_prerequisites(tool_name, tool_input, session_state)
        result = TOOLS[tool_name].fn(**tool_input)
        record_verification(tool_name, result, session_state)
        return {"type": "tool_result", "tool_use_id": None, "content": str(result)}
    except Escalate as e:
        session_state["escalated"] = True
        return {
            "type": "tool_result",
            "tool_use_id": None,
            "is_error": True,
            "content": str({"errorCategory": "permission", "isRetryable": False, "message": e.reason}),
        }
    except ToolError as e:
        return {
            "type": "tool_result",
            "tool_use_id": None,
            "is_error": True,
            "content": str(e.to_dict()),
        }


def agent_loop(client, user_message: str, session_state: dict | None = None) -> dict:
    """The loop itself: `stop_reason` decides everything, never "does the reply contain text"."""
    session_state = session_state if session_state is not None else {}
    messages = [{"role": "user", "content": user_message}]

    for _ in range(MAX_TURNS):
        response = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            tools=ANTHROPIC_TOOL_DEFS,
            messages=messages,
        )
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            final_text = "".join(b.text for b in response.content if getattr(b, "type", None) == "text")
            return {"final_text": final_text, "escalated": session_state.get("escalated", False)}

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if getattr(block, "type", None) != "tool_use":
                    continue
                result_block = run_turn(client, block.name, block.input, session_state)
                result_block["tool_use_id"] = block.id
                tool_results.append(result_block)
            messages.append({"role": "user", "content": tool_results})
            continue

        # Any other stop_reason (max_tokens, refusal, ...) — stop rather than loop blindly.
        return {"final_text": None, "escalated": session_state.get("escalated", False),
                "stop_reason": response.stop_reason}

    return {"final_text": None, "escalated": session_state.get("escalated", False), "error": "max turns exceeded"}


if __name__ == "__main__":
    import anthropic

    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise SystemExit("Set ANTHROPIC_API_KEY to run live. Otherwise: pytest test_agent.py")

    live_client = anthropic.Anthropic()
    outcome = agent_loop(live_client, "Hi, I'm Amina Raza. Please refund order ord_100 and also "
                                       "update its shipping address to '12 Garden Town, Lahore'.")
    print(outcome)
