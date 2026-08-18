# Daily Triage Demo — Project 8 Capstone (Your Own Daily Loop)

**Loop Engineering, all 6 parts: heartbeat, worktree, skill, maker-checker, connector, spine.**

> **No official starter kit exists for this project** — the book says "pick one real, boring,
> recurring chore... build the full loop." This scaffold rehearses the exact shape from the book's
> own Part 5 worked example (`Loop-Engineering-Final-Prep.md` Section 6), but against local mock data
> so you can run a full beat with no live GitHub/CI/Slack needed.

## Kya Hai Is Mein

- `src/greeter.py` — ek **real bug** (off-by-one, last name drop hota hai) — safe fix candidate
- `tests/test_greeter.py` — checker, maine khud chala kar confirm kiya 2/3 tests fail hote hain
- `ISSUES.md` — 2 mock "open issues": ek safe fix (#1), ek jaan-boojh kar **risky** (#2 — public
  behaviour change) jo escalate hona chahiye
- `progress.md` — khaali spine template, ready to fill
- `.claude/skills/daily-triage/SKILL.md` — poora morning-triage procedure
- `.claude/agents/reviewer.md` + `.opencode/agents/reviewer.md` — reviewer jo issue #2 ko **hamesha**
  reject karta hai, chahe tests pass ho jayein

## Kaise Chalayein

1. Throwaway location par copy karo, apna git repo banao (`git init`)
2. `claude` chalao, folder trust karo
3. Type karo:
   ```text
   run the daily-triage skill
   ```
4. Dekho: agent `ISSUES.md` parhta hai, issue #1 (bug) fix karta hai apni branch par, reviewer se
   PASS leta hai, report karta hai ready-to-merge. Issue #2 (risky) ko **chhorta hai** aur
   `progress.md` ke "Open / needs a human" section mein likh deta hai
5. `progress.md` khol kar dekho — dono cheezein record hui hongi

## Done Jab (Book Ka Apna Capstone Criteria)

Book kehta hai: *"it has run unattended for a week and you trust what it ships because you read it."*
Is chote demo ke liye adapted version:

- [ ] Issue #1 PASS + ready-to-merge branch mein hai
- [ ] Issue #2 `progress.md` mein "needs a human" mein hai, **auto-fix nahi hua**
- [ ] `progress.md` "Done" section mein aaj ki date ke sath entry hai
- [ ] Doosri baar chalao — spine confirm karo ke woh issue #1 dobara "solve" karne ki koshish nahi
      karta (kyunki woh already "Done" mein hai)

## Real Duniya Mein Wire Karna (Aage Ka Kadam)

Yeh demo `ISSUES.md` se manually kaam parhta hai. Real production loop banane ke liye:

1. `ISSUES.md` ki jagah real GitHub issues/CI failures use karo (Concept 10 — connector)
2. Isay ek weekly/daily heartbeat do — Claude Code Routine ya `cron`/GitHub Actions
   (poori field guide: [`../08-routines-appendix.md`](../08-routines-appendix.md))
3. Har run ke pehle A6 checklist chalao ([`../08-routines-appendix.md#a6`](../08-routines-appendix.md))

## OpenCode Variant

```bash
opencode run "Run the daily-triage procedure: read progress.md, check ISSUES.md,
fix issue #1 on a new branch, invoke @reviewer to grade it, and escalate issue
#2 to progress.md without touching it. Update progress.md last."
```
