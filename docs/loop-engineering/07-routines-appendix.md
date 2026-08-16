# 07 — Routines Appendix: Field Guide (A1-A6)

Yeh appendix book ka sabse "mechanical" hissa hai — Claude Code cloud **Routines** ke har field, teeno
triggers, secrets kahan jate hain, aur woh common galtiyan jo real hours barbaad karti hain. Isay tab
padho jab ek real Routine banane wale ho, memorize karne ki zaroorat nahi.

**Ek sentence orientation:** Routine ek **saved Claude Code configuration** hai — prompt + repo(s) +
cloud environment + connectors, ek dafa package hui aur Anthropic ke servers par automatically chalti
hai. Yeh Concept 6 ka heartbeat hai, ek product ki tarah. Loop design aap late ho; scheduler, machine,
plumbing platform deta hai.

## Quick-Reference Table

| Default/Behavior | Risk | Fix |
| --- | --- | --- |
| "Local" option New-routine dialog mein | Desktop task ko Routine samajh baithna | Remote = cloud routine, Local = Desktop task (A1) |
| Sab connectors included, writes allowed | Unattended agent har linked tool mein act kar sakta hai | Zaroorat se zyada har connector hatao (A2) |
| `.env` gitignored, cloud clone tak nahi pahunchta | Routine credentials na paye, fail ya improvise kare | Secrets env-variables panel mein, prompt mein bhi bata do (A4) |
| Fresh clone, fresh environment, har run | Loop apna pehla step forever repeat kare | Committed context/progress file, ya external board (A4) |
| Schedule floor 1 hour | Design 15-minute fires assume kare | API trigger + apna scheduler higher frequency ke liye (A3) |
| API bearer token ek baar dikhta hai, endpoint dedupe nahi karta | Lost token, webhook retries se duplicate runs | Turant store karo, prompt safe-to-repeat likho (A3) |
| GitHub events hourly capped, overflow **dropped** | Event-heavy loop chupke se kaam miss kare | Nightly reconciliation sweep, schedule trigger par (A3) |
| `matches regex` poora field test karti hai | `hotfix` "urgent hotfix for auth" match nahi karega | `.*hotfix.*`, ya `contains` use karo (A3) |
| Runs **aapki** identity carry karte hain, koi mid-run approval nahi | External actions ship hote hain aapke naam se, unreviewed | Two-routine gate: draft, phir human approve, phir API-fired executor (A4) |
| Green status = koi infra error nahi | Failed tasks successful lagti hain | Har baar run transcript parho (A5) |

## A1 — Local Session ≠ Cloud Routine

Desktop app ke **New routine** button mein 2 options: **Remote** (cloud routine — isi appendix ka
topic) aur **Local** ([Desktop scheduled task](https://code.claude.com/docs/en/desktop-scheduled-tasks)
— apni machine par, real files/unsaved changes ke sath, sirf machine on hone tak). Rule: local files
chahiye → Desktop task. Laptop-closed guarantee ya connectors/API/GitHub triggers chahiye → cloud
routine. Achha pehla step: prompt ko Desktop task ya one-off run ki tarah prove karo, phir scheduled
cloud routine mein move karo.

## A2 — Creation Form, Field By Field

Routine `claude.ai/code/routines` par, Desktop app mein, ya `/schedule` se plain language mein banti
hai. Sab ek hi account tak jati hain.

- **Prompt** — self-contained hona zaroori hai (koi permission prompt, koi puchne wala mid-run nahi).
  Skill ko point karo, routine ka apna text chota rakho.
- **Repositories** — har run fresh clone hoti hai. Default: sirf `claude/*` branches par push. **Allow
  unrestricted branch pushes** toggle isay hatati hai — sirf jaan-boojh kar, ek repo par.
- **Environment** — network access, env variables, setup script (cached). **Default** = Trusted
  allowlist. Kuch aur chahiye → **Custom**, sirf woh domain allow karo.
- **Connectors** — **default: sab connected connectors included, writes allowed, bina puche.** Yeh
  sabse zaroori cheez hai har baar badalne ki — jo routine ko zaroorat nahi hai usay hatao.

## A3 — Teen Triggers

**Schedule** — presets: hourly/daily/weekdays/weekly. **1-hour floor hai.** Higher frequency chahiye →
API trigger + apna scheduler. One-off runs daily cap mein count nahi hote.

**API** — `/fire` endpoint + bearer token (ek baar dikhta hai, turant store karo):
```bash
curl -X POST https://api.anthropic.com/v1/claude_code/routines/<routine-id>/fire \
  -H "Authorization: Bearer <routine-token>" \
  -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"text": "Sentry alert SEN-4521 fired in prod. Stack trace attached."}'
```
> **Warning:** `/fire` endpoint mein koi built-in deduplication nahi hai, webhooks default se retry
> karte hain. Sender par deduplicate/rate-limit karo, prompt ko safe-to-repeat likho.

**GitHub events** — pull request + release events. `matches regex` **poora field** test karta hai
(`hotfix` matlab exactly `hotfix`, `.*hotfix.*` likho). **Per-routine/account hourly caps, overflow
dropped** (queued nahi) — event-heavy design ko nightly reconciliation sweep chahiye.

## A4 — Secrets, State, Identity

- **Secrets env-variables panel mein, `.env` mein kabhi nahi** — `.env` gitignored hai, cloud clone tak
  kabhi nahi pahunchta
- **Har run zero se shuru hota hai** — fresh clone, fresh environment. Yaad rakhne wali har cheez
  machine se pehle nikalni zaroori hai: repo mein push, external system mein write
- **Routines aap ki tarah act karti hain** — commits/PRs/Slack posts sab aapki identity carry karte hain
- **Koi mid-run approval nahi** — gate **routines ke darmiyan** banao: Routine A draft karti hai,
  **human** review karta hai, approval Routine B ko API trigger se fire karta hai jo action leta hai

## A5 — Runs Parhna

**"Green status matlab session bina infrastructure error ke khatam hui — yeh iska proof nahi ke task
succeed hua."** Blocked network requests, missing connector tools, task failures sab transcript mein
hain, status column mein nahi. **Har baar transcript parho.**

## A6 — Routine Checklist (Save Karne Se Pehle)

```
[ ] Repositories: sirf sahi repo, unrestricted pushes OFF
[ ] Prompt: self-contained, success condition + limit shamil
[ ] Connectors: jo zaroorat nahi unhe hatao
[ ] Environment: secrets variables panel mein, network access narrow
[ ] Trigger: jaan-boojh kar chuna, no accidental high-frequency
[ ] State: committed progress/context file ya external board
[ ] Human gate: draft PRs/branches/messages, no direct merge/deploy/payment
[ ] Test run: one-off/Run now se fire karo, TRANSCRIPT parho, status color nahi
```

---
[⬅ Practice Projects](06-practice-projects.md) · [⬆ Index](README.md) · [Agla: Routine Drills + Dreaming Capstone ➡](08-routine-drills-and-dreaming.md)
