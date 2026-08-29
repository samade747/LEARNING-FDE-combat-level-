## Scope 
we are learning about Claude Agent SDK
and  


# Plan — stop_reason Handling
--Must use the claude-agent-sdk
--Python 
--must use lib


## Goal

we are creating a code examples to learn about stop_reason
we need to see stop_reason for tool_user
we need to see the stop reason for end_result
we need to see how the results is appended 
i want to use a weather tool_use example.
    
`lib/sdk_parser` ko extend karna taake yeh Claude Messages API ke `stop_reason` field ko sahi se
handle kare — `tool_use` ko `end_turn` se differentiate kar sake, aur loop ko batana ke agla step
kya hai (tool call continue karna, ya final response present karna).

## Non-Goals

- Raw `anthropic` client + `ANTHROPIC_API_KEY` — Track B auth decision = claude-agent-sdk. Loop
  mechanics ke liye offline `FakeClient` use karte hain.
- Poora agent framework rebuild — sirf stop_reason → loop-decision mapping.

## Approach

`lib/sdk_parser` mein ek naya `stop_reason.py` module — pure mapping, no network, testable bina key.
`classify_stop_reason(str)` ek loop-decision string deta hai; helpers `is_tool_turn()`,
`text_is_final()`, `next_step(response)`.

## Steps — DONE (2026-08-29, Week 2)

1. [x] `lib/sdk_parser/stop_reason.py` — `_DECISION` map (`end_turn`/`stop_sequence`→final,
   `tool_use`→call_tools, `max_tokens`→retry_truncated, `pause_turn`→continue, `refusal`→stop_refused),
   `None`/unknown → `"unknown"` with a warning.
2. [x] `__init__.py` re-exports the 4 helpers.
3. [x] `stop_reason/main.py` — real claude-agent-sdk run (weather tool_use example). Finding:
   per-turn `AssistantMessage.stop_reason` is `None`; only `ResultMessage.stop_reason` (`end_turn`)
   populated. `classify_stop_reason(None)` isi liye `"unknown"` + warning deta hai.
4. [x] `week-02-agentic-loop-by-hand/by_hand_loop.py` — offline 2-tool loop uses `classify_stop_reason`
   as its branch point. Real run: 3 turns, parallel weather calls + calculator + end_turn.
5. [x] `week-02-agentic-loop-by-hand/test_week2.py` — 6 offline tests, all pass.

**Status: complete.** stop_reason ab `tool_use` ko `end_turn` se differentiate karta hai aur loop ko
next step batata hai — plan.md ka Goal pura.
