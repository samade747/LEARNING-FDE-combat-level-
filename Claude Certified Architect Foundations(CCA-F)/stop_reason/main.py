"""Demo: how stop_reason works in the Claude Agent SDK, with a weather tool_use example.

Uses `claude_agent_sdk` (not the raw `anthropic` package) per plan.md's own constraint
("Must use the claude-agent-sdk"). Type definitions confirm both `AssistantMessage` and
`ResultMessage` carry a `stop_reason: str | None` field
(https://github.com/anthropics/claude-agent-sdk-python/blob/main/src/claude_agent_sdk/types.py).

**Tested 2026-08-29, real run, real tool call — one finding worth knowing before you rely on
this:** in that run, `AssistantMessage.stop_reason` was `None` on every message, including the
ones carrying a `ToolUseBlock`. Only `ResultMessage.stop_reason` (`'end_turn'`) and
`ResultMessage.terminal_reason` (`'completed'`) actually came through populated — once, at the
very end of the whole query, not per-turn. Whether that's version-specific SDK behavior or
something about how `query()` synthesizes messages internally isn't confirmed; this script logs
whatever it observes rather than assuming the type hint is what you'll see in practice — watch
your own run's log output for "AssistantMessage.stop_reason" lines to see current behavior.

Run: pip install claude-agent-sdk -q && python stop_reason/main.py
Needs Claude Code auth set up (ANTHROPIC_API_KEY, or a logged-in `claude` CLI session) — the SDK
bundles the Claude Code CLI itself, no separate Node/npm install required.
"""
from __future__ import annotations

import asyncio
import os
import sys
from typing import Any

# lib/sdk_parser lives one directory up from this file (CCA-F root), and this
# script is run directly (`python stop_reason/main.py`), not as a package —
# so the parent directory has to be added to sys.path before the import.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.sdk_parser import format_response_summary, logger  # noqa: E402

from claude_agent_sdk import (  # noqa: E402
    AssistantMessage,
    ClaudeAgentOptions,
    ResultMessage,
    TextBlock,
    ToolUseBlock,
    create_sdk_mcp_server,
    query,
    tool,
)


@tool("get_weather", "Get the current weather for a city.", {"city": str})
async def get_weather(args: dict[str, Any]) -> dict[str, Any]:
    """Fake weather lookup — no real weather API, just enough to make the tool_use round-trip real."""
    city = args["city"]
    return {"content": [{"type": "text", "text": f"{city}: sunny, 32C"}]}


weather_server = create_sdk_mcp_server(name="weather", version="1.0.0", tools=[get_weather])


def _block_summary(block) -> dict:
    if isinstance(block, ToolUseBlock):
        return {"type": "tool_use", "name": block.name}
    if isinstance(block, TextBlock):
        return {"type": "text"}
    return {"type": type(block).__name__}


async def main() -> None:
    options = ClaudeAgentOptions(
        mcp_servers={"weather": weather_server},
        allowed_tools=["mcp__weather__get_weather"],
    )

    async for message in query(prompt="What's the weather in Lahore?", options=options):
        if isinstance(message, AssistantMessage):
            format_response_summary(
                {"stop_reason": message.stop_reason, "content": [_block_summary(b) for b in message.content]}
            )
            logger.info(f"AssistantMessage.stop_reason = {message.stop_reason!r}")
            for block in message.content:
                if isinstance(block, TextBlock):
                    logger.info(f"Claude: {block.text}")
                elif isinstance(block, ToolUseBlock):
                    logger.info(f"Tool call: {block.name}({block.input})")

        elif isinstance(message, ResultMessage):
            logger.info(
                f"ResultMessage.stop_reason = {message.stop_reason!r}, "
                f"terminal_reason = {message.terminal_reason!r}"
            )


if __name__ == "__main__":
    asyncio.run(main())
