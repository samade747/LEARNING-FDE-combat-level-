# 03 — Complete Worked Example: Weekly Digest

**Feature:** *"Weekly digest"* jo har user ko unke notes ka summary email kare har Monday. Kai files
touch karti hai (scheduled job, notes query, mailer) — Concept 8 ke right-sizing rule se **poori loop**
kamati hai. **2 dafa chalate hain:** pehle claude.ai mein (thinking visible), phir Claude Code mein
(real repo files).

## claude.ai Mein

**Phase 0 (already set):** Plain language, existing libraries prefer karo, har feature spec ship kare,
`published/` mat chhuo.

**Phase 1 — Research:**
```text
Research what's involved in a "weekly digest email"... Cover: how
we'd select which notes to include, scheduling options, email-sending
approaches, and main failure modes (no notes that week, send failures,
time zones).
```
Findings Artifact mein **time-zone question** ata hai jo aap ne socha nahi tha.

**Phase 2 — Specify:** Spec Artifact banti hai — achi hai, lekin kuch jagah generic.

**Phase 3 — Clarify:** Interview 3 unstated decisions nikalta hai: **local Monday, UTC nahi**; **zero
notes wale hafte mein email nahi jati**; **unsubscribed users skip hote hain.** *"Yehi lamha hai jahan
SDD apni keemat kamata hai — 3 future bugs abhi sentences ki tarah mar gaye."*

**Phase 4 — Build:** `plan.md` (existing mailer reuse karta hai, constitution match) → approve → task-
by-task implement. Jab task spec mein kuch chup dhoondti hai (email subject line), **pehle spec update
karo**, phir continue karo.

## Wahi Feature, Claude Code Mein

- **Research:** subagents, ek per area, findings `specs/weekly-digest/research.md` mein
- **Specify:** `Shift+Tab` plan mode mein — "abhi mat banao" rule ab tool enforce karta hai
- **Build:** Claude apni task list banati hai, aap har step review karte ho, har ek ke baad commit
  karte ho — `git log` task list jaisa parhta hai

**Asal farq:** spec kahan reh gayi — claude.ai mein Artifact mein, Claude Code mein `specs/` mein,
version-controlled.

## Artifacts Ki Shape (Trimmed)

```md
# spec.md — Weekly Digest
## Functional Requirements
FR-1 Digest sends on the user's local Monday at 8:00am.
FR-2 Include only notes created or edited in the prior 7 days.
FR-3 Zero qualifying notes → no email is sent.
FR-4 Unsubscribed users are skipped.
FR-5 A send failure is retried once, then logged.
```

```md
# plan.md — Weekly Digest
## Approach
Reuse the existing mailer service (constitution: prefer what exists).
A scheduled job runs hourly, selects users whose local time is Mon 08:00.
```

```md
# tasks.md — Weekly Digest
1. Note-selection query: notes per user from the last 7 days. [FR-2]
2. Eligibility check: local Monday 08:00 + subscribed. [FR-1, FR-4]
3. Digest builder: top 10 + "and N more"; skip if empty. [FR-3]
4. Wire to mailer with retry-once + logging. [FR-5]
5. Tests for each acceptance criterion. [Verify]
```

> **Notice karo:** Har task apna requirement cite karta hai, aakhri task verification hai — seedha
> acceptance criteria se derived.

---
[⬅ Three Ways](02-three-ways.md) · [Agla: Judgment ➡](04-judgment.md)
