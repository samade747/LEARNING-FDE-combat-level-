# Week 1, Hour 1 — Entry-Skill Verification

## Part A — One request, explained

Script: [`hour1_messages_api_demo.py`](hour1_messages_api_demo.py) · run 2026-08-29, real call,
`model=claude-sonnet-5`.

### Request

Ek single user prompt bheja — architecture se "workflow vs agent" ka farq 2 jumलों mein maang.
claude-agent-sdk `query(prompt=...)` internally Claude Code CLI ko chalata hai jo auth handle karti
hai (koi `ANTHROPIC_API_KEY` env var nahi chahiye).

### Response — har field ka matlab

Response **ek string nahi** — yeh **typed messages ki ek stream** hai, aur har message ke andar
**content blocks ki ek list** hoti hai:

| Cheez | Is run mein aya | Matlab (architect ke liye) |
| --- | --- | --- |
| `SystemMessage(subtype='init')` | 1 | CLI/session handshake — model output nahi. Ignore for logic. |
| `AssistantMessage` → `ThinkingBlock` | 1 (0 chars) | Model ka internal reasoning channel. Yahan khaali tha (simple prompt). Kabhi kabhi yahan asli reasoning hota hai — usay final text se alag treat karo. |
| `AssistantMessage` → `TextBlock` | 1 | Asli jawab. **Content ek list hai** — ek turn mein text + tool_use dono blocks ho sakte hain. |
| `stop_reason` (AssistantMessage par) | `None` | ⚠️ **Finding:** claude-agent-sdk ke per-turn `AssistantMessage` par yeh populate nahi hota. (Wahi observation `stop_reason/main.py` mein bhi note hua.) |
| `stop_reason` (ResultMessage par) | `'end_turn'` | **Protocol ka apna signal** — "Claude ka turn kyun khatam hua". `end_turn` = model ne khud faisla kiya ke kaam ho gaya. Doosre values: `tool_use` (tool chahiye), `max_tokens` (truncate hua), `stop_sequence` (stop string mila). |
| `terminal_reason` | `'completed'` | SDK-level — "poori query kyun khatam hui". `completed` = normal end. |
| `is_error` | `False` | Turn error-free tha. |
| `num_turns` | `1` | Ek hi request/response turn hua (koi tool round-trip nahi). |
| `usage` | `in:2 out:158 cache_read:18596` | Token accounting. `cache_read` bada hai kyunki system prompt/context cached tha. |
| `total_cost_usd` | ~`$0.0063` | Is call ki asal keemat. Architect ke liye: har design choice ka ek dollar number hota hai. |

### Architect takeaway (exam-relevant, Task 1.1)

> **Completion protocol ke control signals se pata karo, prose parh kar nahi.** `stop_reason` /
> `tool_use` / `tool_result` / `tool_use_id` — yeh loop ki machinery hai. "Response mein text hai
> isliye kaam ho gaya" ya "text mein 'done' likha hai" — yeh galat hai aur Week 2 ka poora lab isi
> ghalti ke 5 variants diagnose karता hai.

### Model ka jawab (workflow vs agent) — reference ke liye

> An AI *workflow* is a system in which the control flow is **fixed at design time**: a human
> architect wires LLM calls and tools along predetermined paths, so the sequence of steps is known
> before the system runs. An AI *agent* hands that control flow **to the model itself**: given a
> goal, tools, and a feedback loop, the LLM decides at runtime which steps to take and when it is
> done, so the execution path is discovered rather than drawn.

---

## Part B — One Claude Code task + plan-vs-direct defense

**Task kiya:** is workspace ke andar Week 1 ke files (README, is script, notes) banaye — yeh khud ek
Claude Code task tha, direct execution mode mein (files banao, script chalao, output capture karo).

### Plan mode vs direct execution — kab kya

| Direct execution | Plan mode |
| --- | --- |
| Chhota, well-understood, isolated change | Architectural / multi-file / uncertain / multi-approach kaam |
| "Yeh function rename karo", "yeh test add karo" | "Is service ko event-driven banao", "auth flow redesign karo" |
| Rollback aasan, blast radius chhota | Pehle approach par agree karna zaroori — galat direction mehnga |
| Is script ko likhna + chalana | Poore practicum SoR ka architecture decide karna (P3) |

**Extra option:** verbose discovery (bara codebase samajhna) ke liye **Explore subagent + scratchpad**
— taake woh saara output main conversation ka context na khaye. (Yeh Week 6 ka topic hai.)

**Is task ke liye faisla:** direct execution — kaam mechanical tha (known file structure, ek script
jise chala kar verify kar sakte hain), koi architectural branch nahi tha. Agar poora 13-week
coursework structure ek saath design karna hota, plan mode behtar hota.
