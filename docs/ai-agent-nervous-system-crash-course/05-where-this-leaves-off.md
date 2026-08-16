# 05 — Part 5: Yeh Course Kahan Chhodta Hai + Quick Reference

## Cost Shape

**2 cost surfaces:** infrastructure cost (Inngest, store, compute) aur inference cost (model tokens).
**Infrastructure roughly flat rehti hai; inference linearly scale karta hai.**

**Inngest pricing:** Hobby tier $0 — 50,000 executions/month, 5 concurrent steps, koi card nahi.
Execution = ek function run + har step-level retry.

**Hobby-tier ceilings:** 5-concurrent-step cap (code mein `limit=10` likhne ke bawajood platform 5 par
rok deta hai). `step.sleep` 7 din tak free tier par.

**Inference cost hi hawi hai.** Typical customer-support run kuch hazar se 10,000 tokens use karta hai.
**Yehi optimize karo.** 2 sabse zyada value wale levers: stable cached prompt prefix, aasan turns cheap
model par route karo.

**3 Inngest-specific levers:** Pure functions ko `step.run` mein mat wrap karo (side effects ke liye
bachao). Bulk paths ke liye `batch_events` use karo. `step.sleep`/`step.wait_for_event` se sasta
suspend karo — suspended time bill nahi hoti.

## Swap Guide: Nervous System Invariant Hai, Platform Nahi

| Concept | Inngest | Alternatives |
| --- | --- | --- |
| Trigger surface | Events | Temporal signals, Restate handlers, AWS EventBridge |
| Durable execution | `step.run` | Temporal activities, Restate handlers, custom Postgres state machines |
| HITL primitive | `step.wait_for_event` | Temporal signals, Restate awakeables, custom queues |
| Cron | `TriggerCron` | Kubernetes CronJobs, GitHub Actions schedules |
| Flow control | concurrency + throttle | Temporal task queues, Redis rate limiters |

**Dapr Agents** production scale ka open companion hai (CNCF-governed, `DurableAgent` class). Inngest
seekhne ke liye behtar hai (dashboard model visible banata hai); Dapr scale ke liye behtar hai jab
Kubernetes-native, polyglot deployment chahiye.

## Yeh Course Abhi Kya Cover Nahi Karta

Worker 4 Invariants satisfy karta hai (Engine, System of Record, World Calls the System, Human as
Principal partial). Baaki 3:

- **Invariant 2** — Har insan ko delegate chahiye (OpenClaw)
- **Invariant 3** — Workforce ko manager chahiye (Paperclip)
- **Invariant 6** — Workforce policy ke under expandable hai (Claude Managed Agents)

## How to Actually Get Good At This

- "Function event arrive hone par fire kyun nahi hota" → event name typo (Concept 3)
- "Function same logical event ke liye 2 baar fire kyun hua" → missing idempotency key (Concept 4)
- "Deploy ke baad kaam kyun gaya" → code `step.run` ke bahar (Concept 7)
- "Customer 2 baar charge kyun hua" → Stripe call `step.run` ke bahar, ya step name unique nahi
- "9am peak par OpenAI 429 kyun deta hai" → missing throttle (Concept 11)
- "Ek customer ka burst doosron ko starve kyun karta hai" → missing per-key concurrency (Concept 12)
- "HITL gate weekend mein chup chaap fire kyun hua" → missing timeout handler jo audit likhe (Concept 15)

**Architecture ek waqt mein ek piece banao.** Isliye Part 4 saat prompts hai, ek nahi.

## Quick Reference

**Trigger surface choose karo:**
- External HTTP request → **Webhook trigger**
- Schedule → **Cron trigger** (`TriggerCron`)
- Doosra Inngest function ne event emit kiya → **Event trigger** (`TriggerEvent`)
- Interactive user wait kar raha hai → Inngest trigger nahi, normal request/response

**Step primitive choose karo:**
- Side-effecting call → `ctx.step.run(...)` (default)
- Long-running serverless OpenAI call → `ctx.step.ai.infer(...)`
- Fixed duration wait → `ctx.step.sleep(...)`
- External event wait → `ctx.step.wait_for_event(...)`
- Pure computation → sirf code likho, `step.run` ki zaroorat nahi

**File layout:**
```text
ai-agent-nervous-system/
├── db.py                 # Neon Postgres access (D0)
├── worker.py              # SandboxAgent + 2 tools (D0)
├── inngest_app.py          # Inngest functions + FastAPI host (D1-D5)
├── .env
└── AGENTS.md
```

**Golden rule:** Worker code kabhi `inngest` import nahi karta; ek hi file nervous system wire karti hai.

## 15 Concepts, Ek Line Mein

1. Events vs requests — request sync hai koi wait karta hai; event async hai duniya aage badh chuki
2. Cron triggers — `TriggerCron(cron="0 9 * * *")`
3. Webhook triggers — inbound HTTP payload named event ban jata hai
4. Idempotency — event IDs + step names duplicate ko no-op banate hain
5. Fan-out — ek event, N subscribing functions; ya parent N child events fire kare
6. `step.run` — har step ek checkpoint hai
7. Memoization — complete steps stored output return karte hain
8. `step.sleep`/`step.wait_for_event` — dono durably suspend karte hain
9. Retries — automatic backoff, N tries ke baad dead-letter
10. Python mein `step.run` AI calls ke liye — `step.ai.wrap` TypeScript-only hai
11. Concurrency/throttling — active runs cap karo, starts-per-second cap karo
12. Priority/fairness — priority queue order karta hai, per-key concurrency fair share deta hai
13. Batching — events accumulate ho ke ek batched call banate hain
14. Replay/bulk cancellation — replay naye code se, bulk-cancel jo nahi chahiye
15. HITL gates — function insan ke approve karne tak suspend hota hai

---
[⬅ Worked Example](04-worked-example.md) · [⬆ Index](README.md)
