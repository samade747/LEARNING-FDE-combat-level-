"""Week 2, Hour 2 — a correct two-tool agentic loop, NO agent framework.

Runs fully offline against a scripted FakeClient (Track B auth = claude-agent-sdk, no raw API key;
the point of this lab is the LOOP MECHANICS, not live model calls). The message shapes are exactly
the raw Messages API shapes: content is a list of typed blocks, the round-trip is
tool_use -> tool_result keyed by tool_use_id, and the branch point is stop_reason.

The loop here is the reference-correct version. The 5-bug diagnostic exercise lives in
../../docs/certifications/ccar-f/projects/00-agentic-loop-no-framework/ (run its test_loop.py).

Run:  python week-02-agentic-loop-by-hand/by_hand_loop.py
"""
from __future__ import annotations

import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

# CCA-F root (one dir up from this week folder) — for `lib.sdk_parser`
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.sdk_parser import classify_stop_reason, format_response_summary  # noqa: E402

MAX_TURNS = 6


# --------------------------------------------------------------------------------------
# Raw-shaped message primitives
# --------------------------------------------------------------------------------------
class Block:
    def __init__(self, type_, **kw):
        self.type = type_
        self.__dict__.update(kw)


class Response:
    def __init__(self, stop_reason, content):
        self.stop_reason = stop_reason
        self.content = content


# --------------------------------------------------------------------------------------
# Tools (deterministic, offline)
# --------------------------------------------------------------------------------------
def get_weather(city: str) -> str:
    table = {"Lahore": "37C, sunny", "Karachi": "31C, humid"}
    return table.get(city, f"no data for {city}")


def calculator(expression: str) -> str:
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:
        return "error: unsupported characters"
    return str(eval(expression))  # offline, character-whitelisted


TOOLS = {"get_weather": lambda i: get_weather(i["city"]),
         "calculator": lambda i: calculator(i["expression"])}


# --------------------------------------------------------------------------------------
# Scripted fake model — simulates a 3-turn agentic exchange
# --------------------------------------------------------------------------------------
class FakeClient:
    """Returns a canned sequence: parallel weather calls -> calculator -> final answer."""

    def __init__(self):
        self._turn = 0

    class _Messages:
        def __init__(self, outer):
            self.outer = outer

        def create(self, model, max_tokens, messages, **kw):
            self.outer._turn += 1
            t = self.outer._turn
            if t == 1:
                return Response("tool_use", [
                    Block("text", text="I'll check both cities."),
                    Block("tool_use", id="w1", name="get_weather", input={"city": "Lahore"}),
                    Block("tool_use", id="w2", name="get_weather", input={"city": "Karachi"}),
                ])
            if t == 2:
                return Response("tool_use", [
                    Block("tool_use", id="c1", name="calculator", input={"expression": "37 - 31"}),
                ])
            return Response("end_turn", [
                Block("text", text="Lahore is 37C, Karachi is 31C — a 6 degree difference."),
            ])

    @property
    def messages(self):
        return self._Messages(self)

    def execute_tool(self, name, tool_input):
        return TOOLS[name](tool_input)


# --------------------------------------------------------------------------------------
# The loop
# --------------------------------------------------------------------------------------
def agent_loop(client, user_message: str) -> dict:
    messages = [{"role": "user", "content": user_message}]

    for turn in range(1, MAX_TURNS + 1):
        response = client.messages.create(model="fake", max_tokens=1024, messages=messages)

        print(f"\n--- turn {turn} ---")
        format_response_summary({
            "stop_reason": response.stop_reason,
            "content": [{"type": b.type} for b in response.content],
        })

        # BUG 1 fix: append the assistant's OWN turn (incl. tool_use blocks) to history
        messages.append({"role": "assistant", "content": response.content})

        decision = classify_stop_reason(response.stop_reason)
        print(f"    classify_stop_reason -> {decision}")

        # BUG 3 fix: branch on stop_reason, never on "is there a text block"
        if decision == "final":
            text = "".join(b.text for b in response.content if b.type == "text")
            return {"final_text": text, "turns": turn}
        if decision != "call_tools":
            return {"final_text": None, "stop_reason": response.stop_reason, "turns": turn}

        # BUG 5 fix: execute EVERY tool_use block, not just [0]
        tool_results = []
        for block in (b for b in response.content if b.type == "tool_use"):
            result = client.execute_tool(block.name, block.input)
            print(f"    tool {block.name}({block.input}) -> {result}")
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,   # exact-match key back to the call
                "content": str(result),
            })

        # BUG 2 fix: always send the results back as a user turn
        messages.append({"role": "user", "content": tool_results})

    # BUG 4 fix: a real ceiling, with a diagnosable error
    return {"final_text": None, "error": "max turns exceeded", "turns": MAX_TURNS}


if __name__ == "__main__":
    result = agent_loop(FakeClient(), "Compare the weather in Lahore and Karachi.")
    print("\n=== RESULT ===")
    print(result)
    assert result["final_text"] == "Lahore is 37C, Karachi is 31C — a 6 degree difference."
    assert result["turns"] == 3
    print("OK — loop handled parallel tools, the tool_result round-trip, and the end_turn stop.")
