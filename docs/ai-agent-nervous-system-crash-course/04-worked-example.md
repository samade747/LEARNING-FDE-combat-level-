# 04 — Part 4: Poora Worked Example — Customer Support AI Worker

Yeh course ki spine hai. Chota customer-support worker banao, phir usay nervous system do — ek layer
ek prompt. Worker code D0 ke baad kabhi nahi badalta; har layer nervous system hai, **bahar se add** hui.

## The Brief

Worker Neon `customers` table se apne sample customers parhta hai, incoming email ka warm reply draft
karta hai, refund sirf human approval ke sath issue kar sakta hai, aur har action ke liye `audit_log`
mein row likhta hai (chota fixed action-names set se).

## 7 Decisions

**D0 — Worker banao, standalone.**
```text
Build me a minimal customer-support agent with the OpenAI Agents SDK...
It reads sample customers from Neon customers table, drafts a warm
reply, and can issue a refund, but the refund tool needs human
approval before it runs.
```
**Zaroori rule:** Worker ka apna code kabhi `inngest` import nahi karta. Agent aur nervous system alag
rehte hain — yehi Inngest ko baad mein Temporal/Restate se swap karne deta hai.

```python
@function_tool(needs_approval=True)
def issue_refund(order_id: str, amount_cents: int, reason: str) -> str:
    ...
```
`needs_approval=True` agent ko **pause** karwata hai — D5 ka keystone yahin hook hota hai.

**D1 — Agent run ko durable banao.**
```text
Wrap the agent run in an Inngest durable function... The whole agent
call goes inside a single step.run so it is memoized.
```
Agent call sabse mehnga hissa hai — `step.run` ke andar iska result memoized hai, retry par dobara nahi
chalta.

**D2 — Event par trigger karo.**
```text
Make the worker wake on a customer/email.received event instead of
being run by hand. Add an ingress audit step before the agent and a
reply audit step after it.
```
**2 alag steps kyun:** Har audit write apna `step.run` hai, apna memoized. Reply step fail ho aur retry
ho, ingress row dobara nahi likhi jati.

**D3 — Daily cron jo fan-out kare.**
```text
Add a daily cron that fans out one customer/health_check.requested
event per Pro and Enterprise customer, each one idempotency-keyed.
```
**Loop nahi, fan-out kyun:** Parent khud customers process nahi karta — N events bhejta hai, return
karta hai. Har child apna run hai, isolated, independently retryable.

**D4 — Flow control.**
```text
Add flow control: a global concurrency cap, a per-customer
concurrency key, and a throttle to protect the OpenAI rate limit.
```
3 knobs 3 kaam karte hain: global cap (ek waqt kitne chalein), per-customer key (ek noisy customer baaki
ko starve na kare), throttle (OpenAI rate limit protect kare).

**D5 — Durable human-approval gate refunds par (keystone).**

Yeh poori idea code se pehle: agent decide karta hai refund warranted hai, lekin insan "haan" bole us
se pehle issue nahi karta.

```text
Make the pause survive [a crash]: when the agent stops for approval,
save where it stopped, then wait up to four hours for a human's
approve-or-reject.
```

```python
decision = await ctx.step.wait_for_event(
    "await-refund-approval",
    event="refund/approval.decided",
    timeout=datetime.timedelta(hours=4),
    if_exp=f"async.data.customer_id == '{customer_id}'",
)
```

**3 cheezein jo galat ho sakti hain:**
1. `if_exp` sirf **is customer** ke liye correlate karo — 2 refunds parallel hon to unique `request_id`
   use karo
2. Resume par agent ko **saved state** do, nayi conversation nahi — warna woh loop mein phas jayega
3. **Agents SDK custom context save nahi karta** — resume par `context_override` se khud wapis do, warna
   approved refund tool bina context ke chalta hai aur chupke se koi row nahi likhta

**Done jab:** Approval par exactly **ek** `refund_issued` row. Rejection par `refund_blocked` row, koi
refund nahi.

**D6 — Prove karo durability broken step survive karti hai.**
```text
Deliberately break the agent step so it fails, fire an event, and
show me Inngest retrying it while the earlier audit step stays
memoized.
```
**Proof:** Failing run mein ingress audit step **1 attempt** par khara, agent step **kai attempts**
accrue karta hai backoff ke sath. **Yeh Concept 7 ka memoization hai, aapke apne Worker mein.**

> **Surprising lekin correct:** Recovery (fix ke baad re-fire) ek **naya run** hai — apni **khud ki**
> ingress row likhta hai. Break-then-recover ke baad customer ki legitimately **2** ingress rows hoti
> hain. Memoization within-run guarantee hai, 2 alag runs ke paar nahi.

## Kya Hua

Worker ka internal code D0 ke baad kabhi nahi badla — same `SandboxAgent`, same 2 tools. **Jo badla
uske around sab kuch:** ab event aur daily cron par jagta hai, durably chalta hai, flow control follow
karta hai, refunds durable human approval par gate hote hain, aur bad deploy se replay se recover hota
hai.

**Yeh woh line hai jo opening ne khinchi thi** — ek agent jo aap operate karte ho, aur ek FTE jo khud
operate karta hai. Aap ne abhi is line ke paar bana diya.

---
[⬅ Balance Aur Recovery](03-balance-and-recovery.md) · [⬆ Index](README.md) · [Agla: Where This Leaves Off ➡](05-where-this-leaves-off.md)
