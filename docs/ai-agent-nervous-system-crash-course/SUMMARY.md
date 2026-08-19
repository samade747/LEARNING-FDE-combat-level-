# Give Your AI Agent a Nervous System — Summary

Mode 2 Phase 2, aakhri chapter. **15 Concepts, ~80% real use.** Agent already sochta/act karta hai —
missing cheez **nervous system** hai jo bina insan ke loop khud band karti hai (event pe jagna, reflex
se react karna, insan ka wait karte hue apni jagah rakhna). Setup: Inngest engine (aap nahi likhte,
retries/waits/memory/dashboard deta hai) + aapka agent (aap likhte ho).

## 00 — 15-Minute Quick Win

- Setup: base download, AGENTS.md se skills install, Neon DB (`customers`,`audit_log`), Inngest dev
  server (`npx inngest-cli@latest dev`, dashboard 8288).
- Pehla durable function: greeting → `step.sleep(15s)` → farewell (2 `step.run`). Trigger karo, dekho
  15s tak **zero compute** use hota hai (sleep step).
- Farewell step todo → dashboard mein greeting 1 attempt, farewell kai attempts backoff ke sath —
  **completed step ek dafa pay hota hai, retry pe nahi**.
- Hardcoded greeting ko real OpenAI Agents SDK agent se replace karo, same `step.run` ke andar.

## 01 — The Senses (Concepts 1-5)

1. **Events vs Requests** — request sync (caller wait karta), event async (fire-and-forget, zero/ek/
   kai functions react karte). Events → durability/scale almost free.
2. **Cron Triggers** — `TriggerCron(cron="0 9 * * *")`. Service down ho to Inngest durably retry karta
   hai, run miss nahi hoti.
3. **Webhook Triggers** — route chota (POST → event → 200 fast reply). 2 doors: webhook (data ke liye)
   vs `/api/inngest` (code chalane ke liye) — seedha baat nahi karte, sirf event se connect.
4. **Idempotency** — senders at-least-once deliver karte hain. Layer 1: stable event `id`. Layer 2:
   step-level (crash ho to completed steps memo se return, dobara nahi chalte). Note: Stripe jaisi
   provider ki apni idempotency key bhi chahiye.
5. **Fan-Out** — same event ko kai `@create_function` subscribe karein, ya parent N child events fire
   kare (dynamic fan-out, stable id se dedup). Sub-agent delegation = fan-out ka special case.

## 02 — The Reflexes (Concepts 6-10)

6. **`step.run`** — har operation checkpoint. Engine function ko ek step ek waqt chalata hai (2 alag
   programs). Rule: step re-run-safe hona chahiye.
7. **Memoization** — `(run_id, step_name)` keyed memo store. Trap: `step.run` ke **bahar** wala code
   har replay pe chalta hai — expensive kaam apne step mein wrap karo. Step naam stable/data-derived do.
8. **`step.sleep`/`step.wait_for_event`** — waqt/event ke zariye durability, zero compute jab wait.
   Sleep 1 saal (paid) / 7 din (Hobby). `wait_for_event` ka `if_exp` specific run wake karta hai.
9. **Retries, Errors, Dead-Letter** — ~4 retries exponential backoff. `NonRetriableError` permanent
   failures ke liye. Failed run dashboard mein "Replay" button ke sath rehti hai.
10. **Python AI Calls** — `step.ai.wrap` sirf TypeScript-only; Python mein hamesha `ctx.step.run` poore
    agent run ko wrap karo. Retry pe poora agent dobara chalta hai (tokens dobara). PII/secrets raw
    step mein mat pass karo — reference pass karo.

## 03 — Balance Aur Recovery (Concepts 11-15)

11. **Concurrency vs Throttling** — concurrency = in-flight cap; throttle = start-rate cap. Per-key
    concurrency (`key="event.data.customer_id"`) ek customer ko doosron ko block karne se rokta hai.
12. **Priority/Fairness** — priority expression queue order decide karti hai; fair-share per-key
    concurrency se guaranteed slice deta hai. Local dev sirf concurrency observable hai.
13. **Batching** — `batch_events(max_size, timeout)` bulk kaam ke liye; interactive response ke liye
    ghalat hai.
14. **Replay/Bulk Cancellation** — automatic retry (memo-preserving) vs Replay (naya run top se, memo
    nahi milta — duplicate side-effects idempotency key se roko, memo se nahi). Cancel = "hona hi nahi
    chahiye".
15. **HITL Gates** — `step.wait_for_event` se approval gate ($500 refund jaisi actions). Suspended
    function weekend mein bill nahi hoti (state store, page-out).

## 04 — Poora Worked Example: Customer Support AI Worker

7 Decisions (D0-D6): D0 standalone worker (`needs_approval=True` refund tool) — worker kabhi `inngest`
import nahi karta. D1 agent run ko `step.run` mein durable banao. D2 event-trigger + 2 alag audit
steps. D3 daily cron fan-out (loop nahi). D4 flow control (global cap + per-customer key + throttle).
D5 **keystone**: durable human-approval gate refunds par (`step.wait_for_event`, 4hr timeout,
`if_exp` unique request_id se, resume par saved context dena zaroori — Agents SDK custom context save
nahi karta). D6 broken step se durability prove karo (ingress 1 attempt, agent step kai attempts).
Recovery = naya run, apni ingress row.

## 05 — Where This Leaves Off + Quick Reference

- Cost: 2 surfaces — infra (Inngest, flat) vs inference (linear). Hobby tier free (50K exec/mo, 5
  concurrent steps cap, 7-day sleep). Inference cost hawi — stable cached prompt prefix + cheap model
  routing 2 sabse zyada value levers.
- **Swap guide**: nervous system invariant hai, platform nahi — Temporal, Restate, AWS EventBridge,
  K8s CronJobs sab alternatives. Dapr Agents production/Kubernetes-native companion hai.
- Course kya cover nahi karta: Invariant 2 (delegate per human — OpenClaw), 3 (manager — Paperclip),
  6 (policy-expandable — Claude Managed Agents).
- Debugging cheat-sheet (7 symptoms → fix), Quick Reference (trigger/step-primitive choice tables),
  file layout, golden rule (worker kabhi inngest import nahi karta), 15-concept one-liner recap.
