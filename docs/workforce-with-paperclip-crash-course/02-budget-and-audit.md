# 02 — Scenarios 5-6: Budget Aur Audit Trail

## Scenario 5 — Budget, Aapka Safety Rail (~5 min)

Har agent ek spending cap carry karta hai. **Rule simple hai:** cap ke **80%** par Paperclip warn karta
hai, **100%** par agent **pause** ho jata hai — bug ya runaway loop ek bounded amount se zyada kharch
nahi kar sakta.

> **Honest catch:** Budget sirf woh spend count kar sakta hai jo **per-token billed** ho. Aapka keyless
> local runtime kuch bill nahi karta — Paperclip har token ko **$0** record karta hai. Rail aaj bite
> nahi karta kyunki bite karne ko kuch nahi. **Woh us din bite karega jab aap paid, per-token model par
> agent point karo — bilkul jab aapko chahiye.**

```text
Set a one-dollar cap on the CEO, then show me the spend Paperclip
actually recorded. Tell me plainly what it cost and why.
```

**Done jab:** Cap set ho, aap rule bata sako (80% warn, 100% pause), aur aap ne honest $0 khud dekha ho.

> **Warning:** Agar kabhi paid API key wire karo, shell mein export karo — kabhi file mein paste mat
> karo, na hi agent se likhwao. Key kahin ghalat jagah land ho to rotate karo.

## Scenario 6 — Audit Trail Ko CFO Ki Tarah Query Karo (~10 min)

Company ke operating system ka poora point yeh hai ke koi bahar ka banda (CFO, legal, compliance)
database se **seconds mein** dobara construct kar sake kya hua. Paperclip yeh history embedded Postgres
mein rakhta hai: **`activity_log`** (ek row per action) aur **`cost_events`** (dollar story).

```text
Time to play CFO. Connect to Paperclip's database and run two queries
for Northwind: first "what happened, in order"... then the total cost
so far in dollars.
```

**`actor_type` column** batata hai insaani decision (`user`) aur agent ka kaam (`agent`) mein farq —
yehi auditor use karta hai confirm karne ke liye ke aap ne decide kiya.

**Done jab:** History query poori ordered story de, cost query real number de, aur aap column
(`actor_type`) naam le sako jo human decision ko agent action se alag karti hai.

---
[⬅ Strategy Aur Team](01-strategy-and-team.md) · [⬆ Index](README.md) · [Agla: Workspace Aur Operating ➡](03-workspace-and-operating.md)
