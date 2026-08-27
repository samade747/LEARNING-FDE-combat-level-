"""broken_loop.py — Track B Required Project 1: Agentic Loop, No Framework.

Root syllabus: "the instructor introduces missing history, a lost tool result, incorrect stop
handling, repeated tool calls, and premature termination. Students diagnose each failure from its
symptoms." Five isolated loop variants below, each correct except for ONE injected bug — compare
each to fixed_loop.agent_loop, the reference implementation with all five bugs fixed.
"""
from __future__ import annotations

MODEL = "claude-haiku-4-5-20251001"
MAX_TURNS = 6


def loop_bug1_missing_history(client, user_message: str) -> dict:
    """BUG 1 — missing history: the assistant's own turn is never appended to `messages`, so
    the next API call is missing the model's own prior reasoning/tool_use block. The model
    effectively re-answers each turn half-blind to what it just did."""
    messages = [{"role": "user", "content": user_message}]
    for _ in range(MAX_TURNS):
        response = client.messages.create(model=MODEL, max_tokens=1024, messages=messages)
        # missing: messages.append({"role": "assistant", "content": response.content})
        if response.stop_reason == "end_turn":
            return {"final_text": _text(response)}
        tool_results = []
        for block in _tool_use_blocks(response):
            result = client.execute_tool(block.name, block.input)
            tool_results.append({"type": "tool_result", "tool_use_id": block.id, "content": str(result)})
        messages.append({"role": "user", "content": tool_results})
    return {"final_text": None, "error": "max turns exceeded"}


def loop_bug2_lost_tool_result(client, user_message: str) -> dict:
    """BUG 2 — lost tool result: the tool executes and its result is computed, but the result
    is never appended back into `messages`. The next model call has no idea the tool ever ran."""
    messages = [{"role": "user", "content": user_message}]
    for _ in range(MAX_TURNS):
        response = client.messages.create(model=MODEL, max_tokens=1024, messages=messages)
        messages.append({"role": "assistant", "content": response.content})
        if response.stop_reason == "end_turn":
            return {"final_text": _text(response)}
        for block in _tool_use_blocks(response):
            client.execute_tool(block.name, block.input)  # result computed, then discarded
        # missing: messages.append({"role": "user", "content": tool_results})
    return {"final_text": None, "error": "max turns exceeded"}


def loop_bug3_incorrect_stop_handling(client, user_message: str) -> dict:
    """BUG 3 — incorrect stop handling: stops the instant ANY text block is present, instead of
    checking `stop_reason == "end_turn"`. A turn that reasons in prose AND calls a tool
    (stop_reason is still "tool_use") gets treated as final — the tool call is silently dropped."""
    messages = [{"role": "user", "content": user_message}]
    for _ in range(MAX_TURNS):
        response = client.messages.create(model=MODEL, max_tokens=1024, messages=messages)
        messages.append({"role": "assistant", "content": response.content})
        if any(getattr(b, "type", None) == "text" for b in response.content):
            return {"final_text": _text(response)}
        for block in _tool_use_blocks(response):
            client.execute_tool(block.name, block.input)
    return {"final_text": None, "error": "max turns exceeded"}


def loop_bug4_repeated_tool_calls(client, user_message: str) -> dict:
    """BUG 4 — repeated tool calls: no turn ceiling at all, so a model that keeps re-requesting
    the same call (for instance because it never received a result — see BUG 2) runs forever
    instead of failing loudly with a bounded, diagnosable error."""
    messages = [{"role": "user", "content": user_message}]
    while True:  # missing: `for _ in range(MAX_TURNS)` or any other ceiling
        response = client.messages.create(model=MODEL, max_tokens=1024, messages=messages)
        messages.append({"role": "assistant", "content": response.content})
        if response.stop_reason == "end_turn":
            return {"final_text": _text(response)}
        tool_results = []
        for block in _tool_use_blocks(response):
            result = client.execute_tool(block.name, block.input)
            tool_results.append({"type": "tool_result", "tool_use_id": block.id, "content": str(result)})
        messages.append({"role": "user", "content": tool_results})


def loop_bug5_premature_termination(client, user_message: str) -> dict:
    """BUG 5 — premature termination: only the FIRST tool_use block in a multi-tool turn is
    executed; any additional tool calls in the same turn are silently dropped."""
    messages = [{"role": "user", "content": user_message}]
    for _ in range(MAX_TURNS):
        response = client.messages.create(model=MODEL, max_tokens=1024, messages=messages)
        messages.append({"role": "assistant", "content": response.content})
        if response.stop_reason == "end_turn":
            return {"final_text": _text(response)}
        blocks = _tool_use_blocks(response)
        block = blocks[0]  # rest of `blocks` silently ignored
        result = client.execute_tool(block.name, block.input)
        messages.append({"role": "user", "content": [
            {"type": "tool_result", "tool_use_id": block.id, "content": str(result)}
        ]})
    return {"final_text": None, "error": "max turns exceeded"}


def _text(response) -> str:
    return "".join(b.text for b in response.content if getattr(b, "type", None) == "text")


def _tool_use_blocks(response):
    return [b for b in response.content if getattr(b, "type", None) == "tool_use"]
