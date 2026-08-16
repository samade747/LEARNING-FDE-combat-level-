# 00 — Scenarios 1-2: Setup Aur Company

## Scenario 1 — Paperclip Khada Karo Aur Apni Company Banao (~15 min)

**Company** ek self-contained AI organisation hai: ek goal, agents ki team, task board, budget.

```text
I would like to get Paperclip running on my laptop. Before you change
anything, check what is already on my machine, then walk me through
your plan.
```

Phir:
```text
Plan looks good, go ahead step by step... When Paperclip is up, create
my company: call it Northwind, goal "Launch a weekly AI newsletter and
reach 1,000 subscribers in 90 days"... Set a small monthly budget
ceiling, twenty dollars... Require my sign-off before the company
hires any new agent.
```

**Done jab:** Dashboard render ho, "Northwind" company dikhaye, goal registered ho (CEO isay parh kar
plan kar sake, sirf tagline nahi), budget ceiling ho, naye hires approval maangein.

## Scenario 2 — Apna CEO Hire Karo (~10 min)

**Agent** ek AI employee hai: role, manager jise report karta hai, budget. **CEO** pehla agent hai jo
hire karte ho, aur ek jiska koi manager nahi — woh aapko, board ko, report karta hai.

```text
I want to hire my CEO... Run it on whatever coding agent I have logged
in locally... through Paperclip's matching local adapter, so no
separate API key.
```

Phir:
```text
Looks good. File the CEO as a hire and bring it to me to approve. Once
I approve, confirm it in the dashboard.
```

> **Zaroori:** Jo gate aap ne Scenario 1 mein arm ki thi, pehli hire par bhi lagti hai — **khud CEO ko
> bhi aap approve karte ho.** Yehi poora point hai.

**Done jab:** Approve karne ke baad, dashboard ek CEO agent dikhaye, idle, aapko report karta hua,
heartbeat enabled.

---
[⬆ Index](README.md) · [Agla: Strategy Aur Team ➡](01-strategy-and-team.md)
