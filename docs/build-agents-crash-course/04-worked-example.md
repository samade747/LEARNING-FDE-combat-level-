# 04 — Part 5: Poora Worked Example

Ab tak coding agent har concept ke liye one-off code likhta raha. Part 5 sab kuch ek `chat-agent` build
mein collapse karta hai. **Stage A** local build hai (6 decisions), **Stage B** ek challenge brief hai
jo `Agent` ko `SandboxAgent` se swap karta hai wahi role topology par.

## Setup: Brief `AGENTS.md` Mein Likhna

Pehle project init karo, `.env` likho, phir **brief** `AGENTS.md` mein append karo — kya banana hai:
streaming chat agent jo session yaad rakhe, 2 local-CLI tools (`search_docs`, `summarize_url`), 2
HTTPS-shaped billing tools (`get_billing_invoice`, `issue_refund` with `needs_approval=True`),
`BillingSpecialist` ko handoff, jailbreak guardrail cheap tier par, tracing wired.

## Stage A: Local Build (6 Decisions)

**Decision 1 — Project rules `AGENTS.md` mein append karo.** Brief batata hai **kya** banana hai; rules
batate hain **kya na todo.** Har rule ke sath "prevents X" hona chahiye — nahi to woh camouflage hai,
discipline nahi.

**Decision 2 — Architecture section add karo.** Plan mode mein, har agent ka model/tools/handoffs,
guardrail, session strategy, Stage A (local) aur Stage B (sandbox) deployment topology. **Push back**
agar agent giant tool list proposes kare, ya "triage important hai" bol kar `gpt-5.5` de de — triage
high-volume hai, high-stakes nahi.

**Decision 2.5 — SDK probe karo (5 minute).** SDK weekly ship hoti hai; names/signatures move karte
hain. Ek introspection script chalao Decisions 3-6 se pehle — 5 minute yahan 30 minute ki debugging
bachate hain.

**Decision 3 — Code scaffold karo.** Architecture section 3 Python files ban jata hai: `models.py`,
`tools.py`, `agents.py`. Sab typed, `issue_refund` mein `needs_approval=True`, koi `Agent(...)` mein
`max_turns=` nahi (yeh Runner-level hai).

**Decision 4 — Streaming, sessions, CLI wire karo.**

> **Zaroori:** DeepSeek + streaming + `@function_tool` = HTTP 400 bug. Worked example isliye OpenAI par
> chalta hai. DeepSeek chahiye to `Runner.run` (non-streaming) use karo, `result.new_items` se markers
> lo.

> **Active-agent threading:** `result.last_agent` ko turns ke across track karo, `/reset` par
> `triage_agent` par reset karo. Skip karo to CLI kabhi kabhi handoff ke baad turn 2 par crash hota hai —
> model aisi tool call karta hai jo current agent ke paas nahi hai.

**Decision 5 — Guardrail add karo.** Cheap-tier classifier `JailbreakCheck` (Pydantic) return karta hai,
SDK validate karta hai aapke code se pehle.

**Decision 6 — Tracing wire karo.** `workflow_name="chat-agent"`, per-turn `trace_metadata` (strings
hi, koi bare int nahi — 400 error deta hai).

**Stage A complete:** Streaming, memory, guardrail, handoff, approval-gated refund, model routing,
tracing — sab kaam karta hai. Moderate use = single-digit dollars/month.

## Stage B: `SandboxAgent` (Challenge)

Koi step-by-step nahi — ek rich brief, ek done-when, gotchas ki list, planning ki autonomy.

**5 behavioral requirements:**
1. `SandboxAgent` sirf triage ke liye swap hota hai, `Capabilities.default()` ke sath, filesystem-style
   tools drop
2. Billing tools HTTPS-shaped rehte hain (host-side)
3. Guardrail, tracing, active-agent threading unchanged transfer
4. `SQLiteSession` host-side rehta hai; `/workspace` ephemeral, persistent state backend-specific mount
   ke peeche
5. Migration chota hai (~60 lines)

**Gotchas:**
- `@function_tool` bodies **hamesha** host-side chalti hain, `SandboxAgent` par bhi
- Session DB harness mein rehti hai, container mein nahi
- Streamed path par OpenAI use karo, DeepSeek nahi
- Resume karte waqt `session=` **aur** `run_config=` dono do
- `/workspace` jaan-boojh kar ephemeral hai — persist ke liye backend ka mount use karo

**Done jab:** Sandboxed CLI 2 dafa chale — doosri baar pichli conversation yaad rahe (host-side
`SQLiteSession`) lekin `/workspace/page.html` gaya ho (sandbox-side ephemeral). **Yehi two-tier
behavior architectural win hai.**

---
[⬅ Sandbox Deploy](03-sandbox-deployment.md) · [⬆ Index](README.md) · [Agla: Cost Discipline ➡](05-cost-discipline.md)
