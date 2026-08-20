# Proposal Loop — Bonus Project (Two-Persona State Machine Over Real Gmail)

**Loop Engineering, bonus/DIY project** — inspired by a shared example ("AI Multi-Agent Marriage
Proposal Loop") that used two real people's names and inboxes plus Gemini. This version rebuilds
the same *mechanism* — an OODA-style state machine that drives a multi-turn email exchange to a
terminal state — with **fictional personas and a single real mailbox**, using **Claude** (this
session's own reasoning) instead of a separate LLM API call.

> 🧩 **Sabse aasan zaban mein:** socho do dost chit likh kar ek doosre ko baat bhej rahe hain, aur
> beech mein ek teesra banda (loop) har chit padh kar decide karta hai "kya jawab positive hai ya
> mana hai, aur agla chit kya likhna hai" — jab tak koi final jawab (haan ya na) na aa jaye. Yahan
> woh "chit" real Gmail email hai, aur "teesra banda" khud Claude hai jo dono personas ki taraf se
> likh raha hai.

## Why fictional personas, why one mailbox

The original example sent real emails between two real people's real inboxes. Reusing that would
mean publishing private individuals' names and addresses into a repo that gets pushed to GitHub —
not something to do without consent. So this version:

- Uses **invented personas** (Rayan, Meher) — not real people.
- Runs entirely inside **one real, authenticated mailbox** (`samad.x747@gmail.com`), which plays
  both sides of the conversation. Every email is genuinely sent and received over real Gmail — the
  loop is real, the "two people" are not.

## What actually ran

This was executed **live, in-session**, using the Gmail MCP connector already authenticated to
this chat (not a standalone Python script — Claude Code itself made the tool calls, playing both
personas and classifying which state to move to next). Two independent threads, two terminal
states:

| Path | Messages | Terminal state |
| --- | --- | --- |
| Hard Rejection | 5/5 sent | `REJECTED_HARD` |
| Joyful Acceptance | 5/5 sent | `ACCEPTED` |

**State machine (both paths):**

```
PROPOSED
   -> WAITING_REFLECTION            (recipient asks for time)
   -> WAITING_REFLECTION            (proposer agrees, no pressure)
   -> [ACCEPTED | REJECTED_HARD]    (recipient's real answer — terminal)
   -> ACK_SENT                      (proposer's closing message, terminal)
```

Every message after the first was sent as a **real Gmail reply** (`create_draft` with
`replyToMessageId` set to the previous message's id, then `send_message` with that draft's id) —
not just a new email with a similar subject. That is what keeps both threads properly threaded in
the inbox, the same way a real reply chain would look.

## Real run log

**Path 1 — Hard Rejection** (thread `1a020f37da20e9d4`):

1. Rayan → Meher, proposal — msg `1a020f37da20e9d4`
2. Meher → Rayan, "need time" — msg `1a020f3a9e77e73d`
3. Rayan → Meher, "no rush" — msg `1a020f3d493538cb`
4. Meher → Rayan, final "no" — msg `1a020f3ff446080d`
5. Rayan → Meher, gracious ack — msg `1a020f427804bb74` — **terminal: `REJECTED_HARD`**

**Path 2 — Joyful Acceptance** (thread `1a020f446cc84542`):

1. Rayan → Meher, proposal — msg `1a020f446cc84542`
2. Meher → Rayan, "need reflection" — msg `1a020f46cffe8d69`
3. Rayan → Meher, "waiting patiently" — msg `1a020f49ea41e979`
4. Meher → Rayan, "yes!" — msg `1a020f4c6a8e0d8c` — **terminal decision reached here**
5. Rayan → Meher, "thrilled & confirmed" — msg `1a020f4ee49d5a0b` — **terminal: `ACCEPTED`**

## What this borrows from the course

- **State machine / OODA loop** (Loop Engineering concept: observe → orient → decide → act, repeat
  until a terminal state) — same shape as the daily-triage capstone's PASS/escalate branch, just
  applied to a conversation instead of a code fix.
- **Spine discipline** — this README *is* the spine: it is the permanent record of what ran, since
  there was no `progress.md`-style file updated turn-by-turn (the loop ran in one continuous
  session, not across separate scheduled beats).
- **Real tool calls, not simulation** — same principle as every other project in this course: the
  ISS project fetches a real position, the doorbell posts a real PR review, and this one sends
  real, threaded Gmail messages. A "fake" version would have just printed text to a file.

## Gotcha: Gmail threading

`send_message` alone does **not** thread replies — each call with a fresh `to`/`subject` starts an
unrelated message even if the subject looks like a reply. Real threading requires:

1. `create_draft(..., replyToMessageId=<previous message id>)` — this sets the proper
   `In-Reply-To`/`References` headers and returns a `threadId` that should match the original.
2. `send_message(draftId=<that draft's id>)` — sends the draft as-is.

Confirm the thread stuck by checking the returned `threadId` matches the first message's id.

---
[⬆ Poori Project List](../../README.md#runnable-projects-poore-12-har-ek-ki-real-jagah) ·
[Practice Log](../../10-practice-log.md)
