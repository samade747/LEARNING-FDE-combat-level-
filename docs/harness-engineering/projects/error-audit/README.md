# Harness Project 3 — The Error Audit

**Concept:** 7 (AX) · **Time:** 45-60 min · **Difficulty:** Medium

`connector_before.py` has 3 realistic errors — technically correct, useless to an agent reading
them cold (`401 Unauthorized`, `400 Bad Request: invalid input`, `429 Too Many Requests`).
`connector_after.py` shows the rewrite this project asks you to do yourself: each message names
**what to change next**, not just what went wrong.

## Setup

```bash
cp -r docs/harness-engineering/projects/error-audit /path/outside/this/repo/error-audit
cd /path/outside/this/repo/error-audit
git init && git add -A && git commit -m "start"
claude
```

## Steps

1. Trigger all 3 errors from `connector_before.py` (no api_key, bad `record_id`, `"rec_ratelimited"`)
   — read each message **as if you were the agent**, with no human to translate it.
2. Rewrite each one so it names the next step, without looking at `connector_after.py` first.
3. Compare your rewrite to `connector_after.py` — same idea is fine, exact wording doesn't need to
   match.
4. Have the agent call the fixed connector after hitting an error, and confirm it **self-heals** on
   the next attempt — no extra prompting from you.

## Done jab (self-check)

- [ ] Fail hui call agent ki agli koshish pe khud heal hui (aapki madad ke bina)
- [ ] Us beat ki taraf ishara kar sako jo pehle waste hoti thi (jab error se agent confuse hua)

---
[⬆ Harness Practice Log](../../11-practice-log.md) · [Poori list](../../07-practice-projects.md)
