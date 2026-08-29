# Week 2 — Homework

> **Explain what the Claude Agent SDK will now do for you that you just implemented by hand.**

By-hand loop (`by_hand_loop.py`) mein hum ne 5 cheezein manually banayi. Agent SDK (`query()` /
`ClaudeSDKClient`) inhe internal kar deta hai:

| By hand (Week 2) | SDK ab karta hai |
| --- | --- |
| `messages.append({"role": "assistant", ...})` har turn | Session state — poori conversation history khud maintain, stateless API calls ke beech |
| `tool_use` block detect → tool run → `tool_result` block append with matching `tool_use_id` | Tool dispatch loop — registered tools / MCP servers ko khud call karta hai, results wapas plumb karta hai |
| `if stop_reason == "end_turn"` vs `"tool_use"` branch | Loop control — `stop_reason` khud read karke decide karta hai continue ya done |
| `for _ in range(MAX_TURNS)` ceiling | Bounded execution — `max_turns` option, exhaustion par clean stop |
| Har `tool_use` block par iterate (parallel calls) | Parallel tool execution built-in |
| — | Permission system (`allowed_tools`, `can_use_tool`, hooks), built-in tools (Read/Grep/Glob/Edit), MCP server wiring, subagents |

## Lekin architect ko andar ka pata kyun ho

1. **Exam Task 1.1** seedha in mechanics ko test karта hai — SDK abstraction ke neeche kya hai.
2. **Debugging:** jab SDK-based agent "loop repeat karta hai" ya "tool call miss karta hai", diagnosis
   wahi 5 root causes hain — bas ab woh SDK ke andar hain. Symptom pehchano to fix jaldi milta hai.
3. **When NOT to use the SDK:** agar aapko custom loop control chahiye (jaise har turn ke baad ek
   external gate), by-hand loop ya lower-level client behtar. SDK opinionated hai.

## Ek line

> SDK ne loop ki plumbing le li — history, tool round-trip, stop_reason branching, ceiling, parallel
> execution. Architect ka kaam ab "loop kaise likhoon" nahi, "yeh loop is problem ke liye sahi shape
> hai ya nahi" hai.
