# 03 — Part 3: Balance Aur Recovery — Production Scale (Concepts 11-15)

Parts 1-2 ne Worker ko chalaya aur crashes se survive karwaya. Part 3 real scale par chalane ke baare
mein hai: ek busy Worker ko har cheez overwhelm karne se rokna, aur jab kuch bulk mein ghalat ho to
tezi se recover karna.

## Concept 11 — Concurrency Aur Throttling

**Concurrency** — kitne runs **ek sath** execute ho sakte hain. **Throttling** — kitni tezi se naye runs
**start** ho sakte hain.

```python
@inngest_client.create_function(
    fn_id="customer-support-conversation",
    trigger=inngest.TriggerEvent(event="customer/email.received"),
    concurrency=[inngest.Concurrency(limit=10)],
    throttle=inngest.Throttle(limit=100, period=timedelta(minutes=1)),
)
```

**Dono kyun chahiye:** Concurrency downstream systems ko **ek waqt** mein bohat zyada calls se bachata
hai. Throttle **burst** se bachata hai — 500 emails 9 baje sharp aayein, throttle starts ko phaila deta
hai.

**Subtle part:** Concurrency sirf **in-flight** runs limit karta hai, start-rate nahi. Fast runs mein,
`concurrency=10` bhi ek second mein hundreds of starts launch kar sakta hai. **Count limit** (database
pool) ke liye concurrency chahiye; **rate limit** (OpenAI 30/min) ke liye throttle chahiye.

**Per-key concurrency:**
```python
concurrency=[
    inngest.Concurrency(limit=10),  # global cap
    inngest.Concurrency(limit=2, key="event.data.customer_id"),  # per-customer cap
],
```
Ek customer 100 emails bhejein, sirf 2 ek sath process hote hain — baqi 98 queue mein, lekin **doosre
customers block nahi hote.**

## Concept 12 — Priority Aur Fairness

**Priority** — har event par ek expression evaluate hoti hai; high priority wale runs queue mein aage
jate hain. Priority concurrency/throttle ko override nahi karti — sirf decide karti hai **kaunsa** run
agla free slot pata hai.

**Fair-share scheduling** — `key` parameter ke sath sizing:
```python
concurrency=[
    inngest.Concurrency(limit=50),
    inngest.Concurrency(limit=3, key="event.data.tenant_id"),
],
```
Har tenant ko guaranteed slice milta hai — koi tenant baaki sab ko block nahi kar sakta.

> **Caution:** Local dev server sirf **concurrency** observable hai. Throttle, priority, fair-share
> sustained multi-tenant contention chahiye jo local test mein nahi banti — Cloud mein confirm karo.

## Concept 13 — Batching

Kuch kaam naturally batched hote hain — 10,000 embeddings ek ek kar ke nahi, 50 ke batch mein. Inngest
ka batch trigger events accumulate karta hai:

```python
batch_events=inngest.Batch(
    max_size=50,
    timeout=timedelta(seconds=30),  # jo pehle ho
),
async def batch_embed_resolved_tickets(ctx: inngest.Context):
    ticket_ids = [e.data["ticket_id"] for e in ctx.events]  # plural
```

**Batching sahi hai jab** kaam naturally bulkable ho aur timeout jitni latency afford ho. **Ghalat hai
jab** interactive response chahiye ho.

## Concept 14 — Replay Aur Bulk Cancellation

**2 farq jo confuse karta hai:**

- **Automatic retry** (same run ke andar) — memo-preserving, complete steps memo se aate hain, sirf
  fail hua step dobara chalta hai
- **Replay/Rerun** (dashboard button, across runs) — **bilkul naya run top se**, har step dobara
  execute hota hai. **Naye run ka memo old run se nahi milta.**

> **Caution:** Replay har step dobara chalata hai — memo save nahi karta. Jo cheez duplicate side effect
> (dobara refund) rokti hai woh memo nahi, **idempotency key** hai (Concept 4).

**Bulk cancellation** ulta hai — "yeh kaam queued tha lekin ab nahi chahiye." Matching runs cleanly
terminate hote hain — `step.sleep`/`step.wait_for_event` resume nahi hote, in-flight runs step boundary
par exit hote hain (torn writes nahi hotin).

**Faisla:** *"Yeh kaam succeed hona chahiye ya nahi hona chahiye?"* Succeed → replay. Na ho → cancel.

## Concept 15 — HITL Gates `step.wait_for_event` Se

Kuch actions itni important hain ke agent ko akele nahi lene diye jate — $500 refund, legal notice.
**Approval gate** hi woh jagah hai jahan Worker rukta hai aur kisi ka wait karta hai. (Yeh Invariant 1
hai — human principal hai.)

```python
approval = await ctx.step.wait_for_event(
    "wait-for-human-approval",
    event="refund/approval.decided",
    timeout=timedelta(hours=24),
    if_exp=f"async.data.request_id == '{request_id}'",
)
if approval is None:
    # timeout: escalate
elif not approval.data["approved"]:
    # rejected
else:
    # approved: refund issue karo
```

**Weekend mein koi active function run nahi hota.** Function **suspended** hai — Inngest state store
karta hai, memory se page-out karta hai. Inngest suspended time bill nahi karta. **HITL workflows ki
economics polling-based queues se dramatically different hain.**

> Yeh D5 ka keystone hai (Part 4 ka worked example) — refund approval, durable bana hua.

---
[⬅ The Reflexes](02-the-reflexes.md) · [⬆ Index](README.md) · [Agla: Worked Example ➡](04-worked-example.md)
