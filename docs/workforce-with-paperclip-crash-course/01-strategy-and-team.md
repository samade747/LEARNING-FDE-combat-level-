# 01 — Scenarios 3-4: Strategy Aur Team

## Scenario 3 — CEO Strategy Propose Karta Hai; Aap Approve Karte Ho (~15 min)

**Heartbeat** agent ka scheduled kaam-karne-ka-waqt hai — jagta hai, kaam ka hissa karta hai, agli
heartbeat tak log off. **Pehli** heartbeat par CEO ek cheez karta hai: goal parhta hai, strategy draft
karta hai task board ke pehle item ki tarah, phir usay **`in_review`** mein move karta hai. **Kuch aage
nahi badhta jab tak aap sign-off na karo.**

```text
Fire the CEO's first heartbeat and let it think. When it has drafted
its strategy and put it up for my review, show it to me.
```

Phir:
```text
I have read the strategy. I will sign off on it as is... Move it
forward to done, show me the activity-log row that proves I, the
board, decided it.
```

**Done jab:** Strategy `in_review` se `done` mein move ho, activity-log row `actor_type = user` (aap,
decider) dikhaye.

## Scenario 4 — CEO Board Banata Hai Aur Pehla Teammate Hire Karta Hai (~20 min)

**Task** ek work unit hai (Jira ticket jaisa), lekin assignee ek agent hai.

```text
backlog → todo → in_progress → in_review → done
```

Approved strategy ke sath, CEO goal ko tasks mein todta hai, phir assign/delegate karta hai. **Yahin
company "workforce" banti hai, akela CEO nahi.**

```text
Let the CEO act on the approved strategy. Fire a few heartbeats and
show me what it does... it will decide it needs a specialist and file
a hire request.
```

> **Sharp CEO tasks banane se pehle hire request file karta hai** — marketing tasks banane se pehle
> koi marketer honi chahiye jo unhe own kare.

Hire aapke inbox mein **approval** ki tarah ata hai. Approve/reject karne ke baad:

```text
I approve the hire. Bring the specialist on board reporting to the
CEO, then fire one CEO heartbeat so it breaks the approved strategy
into tasks and hands them to the new teammate.
```

Ek dafa hire approve ho jaye, CEO baaki khud karta hai — agli heartbeat par strategy ko sub-tasks mein
todta hai aur naye teammate ko assign karta hai. **Yehi payoff hai: team, CEO nahi, kaam karti hai.**

> **Specialist approve hone ke baad, CEO ki heartbeat pause karo** — **autonomy ek grant hai, wapis le
> sakte ho.**

**Done jab:** Company ke paas kam az kam 2 agents hon (CEO + specialist), CEO ne delegate kiya hua task
specialist ne complete kiya ho (comment thread teammate ka real kaam dikhaye, CEO ka nahi), aur aap task
ko company goal tak trace kar sako.

---
[⬅ Setup Aur Company](00-setup-and-company.md) · [⬆ Index](README.md) · [Agla: Budget Aur Audit ➡](02-budget-and-audit.md)
