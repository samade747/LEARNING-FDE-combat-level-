# 01 — Part 1: The Senses — Duniya Worker Tak Kaise Pahunchti Hai (Concepts 1-5)

## Concept 1 — Events Vs Requests

**Request** synchronous conversation hai — koi call karta hai, aap handle karte ho, return karte ho,
woh wait kar raha hota hai. Crash ho to caller ko error milta hai.

**Event** asynchronous message hai — duniya mein kuch hua, originator uska naamzad record emit karta
hai. **Zero, ek, ya kai** functions independently react karte hain. Koi connection khula nahi rehta.
Originator nahi jaanta kaun sun raha hai, wait nahi karta.

```python
# Request: main yahan hoon, wait kar raha hoon
result = await agent.handle_customer_message(text=user_input)

# Event: main fire-and-forget karta hoon
await inngest_client.send(events=[
    inngest.Event(name="customer/email.received", data={...}),
])
```

**Yeh shift chota lagta hai. Nahi hai.** Ek dafa events mein sochna shuru karo, durability aur scale
almost free mein aati hain:
- Producer consumer se slow nahi hota
- Consumer crash/restart kar sakta hai bina kaam khoye
- Naye consumers add ho sakte hain bina producers badle
- Backpressure ek flow-control policy hai, code change nahi

> **Events aapko kaam ki timing own karna band karwate hain.**

## Concept 2 — Cron Triggers

Sabse simple trigger clock hai:

```python
@inngest_client.create_function(
    fn_id="daily-customer-health-check",
    trigger=inngest.TriggerCron(cron="0 9 * * *"),  # 09:00 UTC daily
)
async def daily_health_check(ctx: inngest.Context) -> dict[str, int]:
    customers = await ctx.step.run("fetch-pro-customers", fetch_pro_customer_ids)
    events = [inngest.Event(name="customer/health_check.requested", data={"customer_id": cid}) for cid in customers]
    await ctx.step.send_event("fan-out", events)
    return {"customers_scheduled": len(customers)}
```

**3 zaroori cheezein:** Schedule standard cron syntax hai (UTC default). Function shape identical rehta
hai chahe cron ho ya event trigger. Cron output normal Inngest run hai — dashboard, trace, replay sab
milta hai.

**Agar service down ho jab cron fire ho?** Inngest cron runs ko durably record karta hai. Endpoint
unreachable ho to backoff ke sath retry karta hai — run "miss" nahi hoti.

## Concept 3 — Webhook Triggers

Pehla trigger clock tha. Doosra HTTP hai — bahar se koi (Stripe, email provider) worker tak pahunchna
chahta hai. **POST receive karna aasan hai. Uske baad wala hard hai:** queue karna, retry karna, crash
survive karna, duplicate refuse karna, agent chalana, 4-ghante ki approval hold karna. **Yeh kitchen
Inngest hai.**

Route chota rehta hai — bas POST receive kare, event Inngest ko de, `200` fast reply kare.

**2 doors, opposite directions:**
```text
DOOR 1: webhook door (aap likhte ho) — Stripe yahan knock karta hai DATA ke sath
DOOR 2: /api/inngest (auto) — ENGINE yahan knock karta hai CODE CHALANE ke liye
```

Yeh 2 doors seedha baat nahi karte — sirf event ke through connect hote hain.

```python
@app.post("/webhooks/stripe")
async def stripe_webhook(request: fastapi.Request):
    payload = await request.json()
    await inngest_client.send(
        inngest.Event(name="stripe/charge.refund.failed", data=reshape(payload)),
    )
    return {"ok": True}
```

**Local dev mein koi URL nahi hota** — aap khud webhook ka role nibhate ho `send_event` se.

## Concept 4 — Idempotency: Jab Same Event 2 Baar Aaye

Woh sabse common bug hai, rare edge case nahi. Senders **at-least-once** deliver karte hain, kabhi
exactly-once nahi. **Idempotent** matlab: 2 baar chalao, result same jitna 1 baar chalane se.

**Layer 1 — Event ID source par seed hota hai:**
```python
await inngest_client.send(events=[
    inngest.Event(
        name="customer/refund.requested",
        data={"order_id": "o-4429"},
        id=f"refund-request-{order_id}",  # stable, har duplicate par same
    ),
])
```

**Layer 2 — Step-level idempotency.** Har `step.run` apne naam se identify hota hai. Function crash ho
step 3-4 ke beech, retry code top se dobara chalata hai, lekin steps 1-3 **stored outputs** return karte
hain — dobara execute nahi hote. **Yehi durability hai.**

> **Zaroori note:** Memoization function ke andar exactly-once deta hai. Lekin agar Stripe charge ho
> jaye process crash hone se **pehle** ke Inngest result record kare, retry Stripe ko dobara call karega.
> Fix: `step.run` memoization + **provider ki apni idempotency key** dono sath.

## Concept 5 — Fan-Out Aur Sub-Agent Delegation

Ek event ko kai jagah kaam trigger karna hota hai. **Pattern: kai functions ko same event subscribe
karwao.** Fan-out code nahi chahiye — bas kai `@create_function` decorators same `TriggerEvent` ke sath.
Har function independently chalta hai, apna retry, apna trace, apni failure.

```python
@inngest_client.create_function(fn_id="refund-failed-notify-support", trigger=inngest.TriggerEvent(event="stripe/charge.refund.failed"))
async def notify_support(ctx): ...

@inngest_client.create_function(fn_id="refund-failed-update-risk-score", trigger=inngest.TriggerEvent(event="stripe/charge.refund.failed"))
async def update_risk_score(ctx): ...
```

**Doosra pattern: parent N children fire karta hai** (dynamic fan-out — daily cron 500-5000 customers
ke liye events bhejta hai). Stable `id` (retry par same) dedup ensure karta hai.

**Sub-agent delegation** fan-out ka special case hai — `ctx.step.send_event(...)` se doosre worker
types ko sub-tasks delegate karte ho. Parent wait nahi karta jab tak `step.invoke` use na karo.

> **Isolation ka farq:** Alag functions kabhi ek doosre ko block nahi karte. Lekin ek function ke
> hazaron runs (same function ke) concurrency cap ke peeche apni baari ka wait kar sakte hain
> (Concept 11).

---
[⬅ Quick Win](00-quick-win.md) · [⬆ Index](README.md) · [Agla: The Reflexes ➡](02-the-reflexes.md)
