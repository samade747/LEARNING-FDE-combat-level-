# 02 — Part 2: The Reflexes — Jab Kuch Toote (Concepts 6-10)

Part 1 tha kaam Worker tak kaise pahunchta hai. Part 2 hai jab woh kaam beech mein toot jaye to kya
hota hai.

> **Durability ka matlab:** jab kuch beech mein fail ho, jo steps khatam ho chuke woh khatam rahen, aur
> Worker wahin se uthaye jahan toota — poora dobara na kare. Nervous-system tasveer mein, **yeh reflex
> hai.**

## Concept 6 — `step.run` Aur Durable Function Model

Normal Python function ek dafa top se bottom chalta hai. Beech mein crash ho to top se dobara.

Inngest function **durable** hai. Har operation jise checkpoint karna hai `step.run(name, fn, ...)` mein
wrap hota hai. Engine aapke function ko **ek step ek waqt** chalata hai: top se handler chalata hai,
jahan tak pahunche steps ke saved outputs milte hain (execute nahi hote), agla naya step chalata hai.

```text
ENGINE                                YOUR FUNCTION (host)
  | call: run from the top ------->   step 1 tak chalta hai, karta hai
  | <-------------------------------   step 1 ka result wapis
result 1 store hota hai
  | dobara call --------------->   step 1 memo se, step 2 chalata hai
  ...har step ke liye ek call
```

**Yeh 2 alag programs hain isliye:** Engine aur function alag programs hain. Ek program doosre ke code
ke beech mein pause nahi kar sakta. Engine aapke function ko web ke through, ek step ka result store kar
ke, dobara call karta hai.

**`step.run` ka ek rule:** step **re-run ke liye safe** hona chahiye. Pure functions safe hain.
Idempotent API calls safe hain. Non-deterministic kaam bhi safe hai (bas retry par alag result mil
sakta hai) — jahan exact value stable chahiye, usay seed karo ya alag step mein generate karo.

## Concept 7 — Memoization: Neeche Ka Mechanism

Jab `await ctx.step.run("load-customer", ...)` call karte ho, Inngest ek memo store rakhta hai
`(run_id, step_name)` se keyed. **Pehli baar:** memo khali, function chalta hai, result save hota hai.
**Har baad wali replay:** memo bhara hua hai, function **nahi** chalta, saved value milliseconds mein
wapis ata hai.

> **Trap jo naye users ko surprise karta hai:** `step.run` ke **bahar** wala code har baar chalta hai
> jab bhi Inngest handler mein dobara enter kare — sirf retries par nahi, **har step par.**

```python
# ANTI-PATTERN: yeh har step advance par dobara chalta hai
expensive_thing = await fetch_expensive_data(ctx.event.data["id"])
await ctx.step.run("do-something", do_something_with, expensive_thing)
```

Fix: expensive cheez ko apne step mein wrap karo:
```python
expensive_thing = await ctx.step.run("fetch-expensive-data", fetch_expensive_data, ctx.event.data["id"])
```

**Step name hi memo key hai.** Python SDK duplicate naam auto-number karta hai (`load-customer:1`), lekin
inpar rely mat karo — stable, data-derived naam do (`f"load-customer-{customer_id}"`).

> **Jo bhi re-execute na hona chahiye usay `step.run` mein wrap karo.** Yeh optional nahi hai.

## Concept 8 — `step.sleep` Aur `step.wait_for_event`: Waqt Ke Zariye Durability

Normal Python function mein "3 din wait karo" matlab process 3 din khula rakhna — untenable hai.
Inngest mein yeh **ek line** hai:

```python
await ctx.step.sleep("wait-three-days", timedelta(days=3))
```

Function suspend hota hai; Inngest resume time store karta hai; **kuch bhi compute consume nahi hota**
jab tak wait karte ho. `step.sleep` paid plans par 1 saal tak, free Hobby plan par 7 din tak wait kar
sakta hai.

**Zyada powerful sibling: `step.wait_for_event`.** Waqt ki jagah **doosre event** ka wait karta hai:

```python
approval = await ctx.step.wait_for_event(
    "wait-for-approval",
    event="refund/approval.decided",
    timeout=timedelta(hours=24),
    if_exp=f"async.data.request_id == '{request_id}'",
)
if approval is None or not approval.data.get("approved"):
    return {"status": "rejected_or_timeout"}
```

`if_exp` hi decide karta hai kaunsa waiting run wake ho — sirf **is** request ka.

## Concept 9 — Retries, Error Handling, Dead-Letter

Default: ~4 retries exponential backoff ke sath. Aakhri retry ke baad run **failed** state mein jata
hai, inspection/replay ke liye rehta hai.

**3 Patterns:**
1. **Transient vs permanent failures** — declined card dobara declined hoga. `NonRetriableError` raise
   karo taake Inngest retry skip kare
2. **Step-level vs function-level errors** — step fail ho retry hota hai; function ko survive karwana ho
   to `step.run` ko `try/except` mein wrap karo
3. **Dead-letter aur replay** — poori tarah fail hui function gayab nahi hoti — dashboard ke "failed
   runs" view mein rehti hai, **Replay** button ke sath

## Concept 10 — Python Mein AI Calls Ke Liye `step.run`

**Zaroori:** `step.ai.wrap` sirf TypeScript mein hai. Python mein **hamesha `ctx.step.run` use karo** —
poore agent run ko wrap karo, bare model call nahi:

```python
result = await ctx.step.run("run-agent", lambda: run_support_agent(thread=thread))
```

Dashboard `load-thread` phir `run-agent` dikhata hai, har ek apna input/output ke sath.

> **Poora agent run ek step hai.** Beech mein fail ho aur retry ho, **poora agent dobara chalta hai** —
> tokens dobara kharch hote hain. Usually theek hai (draft dobara banana sasta hai). Agar ek run costly
> ho, kaam ko chote pieces mein todo.

> **Step traces aur customer data:** `step.run` inputs/outputs Inngest ke observability store mein save
> hote hain. PII, secrets, regulated content **raw** step mein mat pass karo — reference (customer_id)
> pass karo, sensitive content step ke **andar** apne authoritative store se load karo.

`step.ai.infer` (Python-supported lekin niche): sirf serverless platforms par jo in-flight time bill
karte hain, ya lambe inferences ke liye useful hai.

---
[⬅ The Senses](01-the-senses.md) · [⬆ Index](README.md) · [Agla: Balance Aur Recovery ➡](03-balance-and-recovery.md)
