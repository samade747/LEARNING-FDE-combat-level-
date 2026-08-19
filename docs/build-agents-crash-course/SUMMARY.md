# Build AI Agents with the OpenAI Agents SDK — Summary

Mode 2 Phase 2, Chapter 1/3. **16 Concepts, 80% real use.** Poore course ka rule: **har agent bug ya
state bug hai, ya trust bug.** 3 build: local chat agent, sandboxed version, cost-controlled version.

## 00 — Foundations (Concepts 1-3)

1. **Agent kya hai**: chat completion = 1 request→1 response; function-calling LLM = aap loop chalate
   ho; **Agent = SDK loop chalata hai** (model→tools→results→model...). `Agent` = LLM+instructions+
   tools; `Runner` loop chalata hai.
2. **3 Primitives**: `Agent`, `Runner` (`run_sync`/`run`/`run_streamed`), `@function_tool` (type hints+
   docstring→JSON schema, SDK validation error before your function runs). `result.final_output` =
   wrapped jawab (2 model calls: tool-choose + compose). Default model `gpt-5.4-mini`.
3. **Agent Loop concrete**: `max_turns` cap, `MaxTurnsExceeded` exception. Aap loop mein nahi ho —
   control points upstream (instructions/tools/guardrails) aur downstream (result). Rule: ~2 turns per
   tool budget karo.

## 01 — Local Chat App (Concepts 4-9)

4. `uv` = Python ka npm/Cargo.
5. Chat loop bug: `Runner.run_sync` **stateless** — turn 2 turn 1 bhoolta nahi, milta hi nahi hai
   (classic state bug).
6. **Sessions** fix karti hain: `SQLiteSession` (in-memory/persistent). Cost consequence: har turn
   poori history re-bill hoti hai. `OpenAIResponsesCompactionSession` lambi conversations ke liye.
7. **Streaming**: `run_streamed` + `stream_events()` — live UI, lekin debugging mehngi (aadha-print
   failure). Pehle plain version, phir streaming add karo.
8. **Function Tools**: type hints = model documentation (`Literal[...]` exact values force karta hai),
   docstring = tool description (kab na call karo bhi likho), tools strings/chote JSON return karein.
9. **Handoffs**: control transfer specialist agent ko — jab instructions/tools genuinely diverge karein.
   Decision table diya. Cost: har handoff ≥1 extra model call (3 calls vs single-agent 1).

## 02 — Safety, Observability, Model Routing (Concepts 10-13)

10. **Guardrails** — input/output/tool kisms. Parallel (default, low latency, possible wasted tokens)
    vs Blocking (`run_in_parallel=False`, no side-effects on trip). `InputGuardrailTripwireTriggered`
    catch karo. Tool guardrail content **reject** kar ke loop continue rakh sakta hai.
11. **Tracing** — model/tool/handoff calls record, flame graph. 3 wajah critical: production debugging,
    per-turn cost, latency budget. Non-OpenAI models: per-run `tracing_disabled=True`. Din 1 se hi
    trace karo — microsecond overhead vs hours of blind debugging.
12. **Model Routing** — economy vs frontier tier table. Base-URL swap pattern (DeepSeek); LiteLLM for
    Anthropic/Gemini/Bedrock. Cost gap 10x+.
13. **Human Approval** — `needs_approval=True` on tool. `Runner.run` returns `interruptions`; tool body
    tab tak nahi chalti jab tak `state.approve()`. Dynamically approve (callable, e.g. $100+ threshold).
    **Approval sandboxing ka substitute nahi, sandboxing approval ka nahi** — dono chahiye.

## 03 — Sandbox Deploy Karna (Concepts 14-16)

14. **`SandboxAgent`** — model reliable safety boundary nahi hai (usually refuse karta hai, hamesha
    nahi). Trap: sirf **built-in capabilities** sandbox hoti hain, aapke `@function_tool` bodies nahi
    (woh aapke Python process mein chalti hain). Sandbox clients table: Unix-local (no isolation) vs
    Docker/E2B/Cloudflare (real isolation).
15. **Cloudflare Sandbox** — bridge pattern (Worker + Sandbox API + Client). Local dev (free) vs
    production (Workers Paid $5/mo+). **R2 mount** — durable storage; gotchas: key `"data"` not
    `"/data"`, `read_only=False` (default True silently no-ops writes), `mount_strategy` required.
16. **R2 Persistence** — sandbox container tez marta hai (idle timeout). `/workspace/data` (mounted)
    survives; rest dies. `Compaction()` capability — long runs summarize purane turns. `Session`
    (conversation history) vs `Memory()` (distilled cross-run lessons) — confuse mat karo.

## 04 — Poora Worked Example

Stage A (local, 6 decisions): AGENTS.md brief + rules (D1), architecture section (D2, push back on
giant tool lists/wrong model tiers), 5-min SDK probe (D2.5), scaffold 3 files (D3), streaming+sessions+
CLI wiring (D4 — DeepSeek+streaming+@function_tool = HTTP 400 bug; active-agent threading for handoffs),
guardrail (D5), tracing (D6, string-only metadata). Stage B (`SandboxAgent` challenge, ~60 lines): only
triage swaps to sandbox, billing tools stay host-side, `@function_tool` bodies always host-side, session
DB stays host-side, `/workspace` intentionally ephemeral.

## 05 — Cost Discipline + Get Good At This

Every turn re-bills full session history. 3 numbers: output tokens 2-5x costlier, cache hits (stable
prefix) 80-90% discount, subagents/guardrails = token multipliers. 2-tier routing (plan-frontier/
implement-economy; default-economy/escalate-on-failure). 5 cost-failure modes table (bill 3x→wrong
default model; spike→loop abuse; ever-costlier turns→unbounded context; over-explaining→terse
instructions; cache hits drop→unstable prefix). 3 DeepSeek gotchas (streaming+tools fails, strict JSON
schema 400s, tracing exports rejected). Realistic cost: low-single-digits/month moderate, $15-30 heavy.
Debugging cheat-sheet (7 symptoms→concept). Golden rule: safety primitives add on problem-hit, except
tracing (day 1). Portable shape: agent loops/tools/sessions/guardrails/approvals/tracing/sandboxes.
