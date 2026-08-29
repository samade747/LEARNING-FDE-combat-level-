"""Week 1, Hour 1 — send ONE request to Claude from Python and explain every part of the response.

Entry-contract check: "explain an API request/response". Track B auth decision = use the
claude-agent-sdk (bundled Claude Code CLI login), so this goes through `query()` rather than the
raw `anthropic` client + ANTHROPIC_API_KEY. The response *shape* is the same idea either way:
a stream of messages, each carrying typed content blocks, ending with a stop/terminal signal.

Run:  python week-01-foundations-sprint/hour1_messages_api_demo.py

What to watch in the output:
  - message TYPE           (SystemMessage / AssistantMessage / ResultMessage)
  - content BLOCK types    (TextBlock, ToolUseBlock, ...) — the API returns a LIST of blocks,
                             not a plain string
  - stop_reason            the protocol's own signal for "why did this turn end"
                             ('end_turn' = Claude is done; 'tool_use' = Claude wants a tool;
                              'max_tokens' = truncated; 'stop_sequence' = hit a stop string)
  - terminal_reason        SDK-level "why did the whole query end" ('completed', ...)
  - usage / cost           tokens in/out and USD, reported once at the end
"""
from __future__ import annotations

import asyncio
import sys

# Windows console defaults to cp1252 — Claude's replies contain em-dashes / non-latin text.
# Force UTF-8 so the output isn't mangled (repo-wide footgun, see loop-engineering iss-loop notes).
sys.stdout.reconfigure(encoding="utf-8")

from claude_agent_sdk import (
    AssistantMessage,
    ResultMessage,
    SystemMessage,
    TextBlock,
    ThinkingBlock,
    ToolUseBlock,
    query,
)

PROMPT = (
    "In two sentences, define the difference between an AI *workflow* and an AI *agent*, "
    "the way an architect would state it."
)


def describe_block(block) -> str:
    if isinstance(block, TextBlock):
        return f"TextBlock  -> {block.text!r}"
    if isinstance(block, ToolUseBlock):
        return f"ToolUseBlock -> name={block.name} input={block.input}"
    if isinstance(block, ThinkingBlock):
        return f"ThinkingBlock -> {len(block.thinking)} chars of reasoning"
    return f"{type(block).__name__} -> {block!r}"


async def main() -> None:
    print("=" * 70)
    print("REQUEST")
    print("=" * 70)
    print(f"prompt: {PROMPT}\n")

    print("=" * 70)
    print("RESPONSE (message by message)")
    print("=" * 70)

    async for message in query(prompt=PROMPT):
        kind = type(message).__name__

        if isinstance(message, SystemMessage):
            print(f"\n[{kind}] subtype={message.subtype!r}")
            print("   -> setup/handshake info from the CLI; not model output")

        elif isinstance(message, AssistantMessage):
            print(f"\n[{kind}] model={getattr(message, 'model', '?')} "
                  f"stop_reason={message.stop_reason!r}")
            print(f"   content is a list of {len(message.content)} block(s):")
            for i, block in enumerate(message.content):
                print(f"     [{i}] {describe_block(block)}")

        elif isinstance(message, ResultMessage):
            print(f"\n[{kind}]")
            print(f"   stop_reason      = {message.stop_reason!r}   "
                  "(protocol: why the last turn ended)")
            print(f"   terminal_reason  = {getattr(message, 'terminal_reason', None)!r}   "
                  "(SDK: why the whole query ended)")
            print(f"   is_error         = {message.is_error}")
            print(f"   num_turns        = {message.num_turns}")
            print(f"   duration_ms      = {message.duration_ms}")
            usage = message.usage or {}
            print(f"   usage            = in:{usage.get('input_tokens')} "
                  f"out:{usage.get('output_tokens')} "
                  f"cache_read:{usage.get('cache_read_input_tokens')}")
            print(f"   total_cost_usd   = {message.total_cost_usd}")

    print("\n" + "=" * 70)
    print("EXPLANATION — see hour1-notes.md for the written answer")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())
