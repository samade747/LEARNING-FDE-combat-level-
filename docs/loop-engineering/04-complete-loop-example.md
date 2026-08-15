# 04 — Ek Complete Loop (Morning Triage Example)

## Loop Chalane Se Pehle: Minimum Safe Loop Checklist

Kisi bhi loop ko khud chalane dene se pehle, ye **7 cheezein** honi chahiye:

1. **Success condition** — kaam khatam hone ka pata kaise chalega
2. **Limit** — max tries/minutes/spend
3. **Isolated branch/worktree** — parallel kaam takrayega nahi
4. **Read-only checker** — alag agent jo grade kare, edit na kare
5. **State file** — spine, taake yaad rahe
6. **Human gate** — risky ya fail kaam seedha `main` pe nahi jata
7. **Log/notification** — overnight failure chup chaap na ho

Koi bhi ek missing ho, to loop **unsafe, bhulakkar, ya invisible** hai.

## Loop Ka Shape (Dono Tools Mein Same)

Ek **morning maintenance loop**: overnight CI failures dekhta hai, safe fixes draft karta hai, check
karwata hai, safe ones ke liye PR kholta hai, baaki flag karta hai.

1. **Heartbeat:** har weekday 9am
2. **Skill:** `daily-triage` skill sara steps sambhalti hai, prompt sirf 1 line
3. **Spine:** `progress.md` shuru mein parhna, end mein update karna
4. **Worktree:** har fix apni checkout mein
5. **Maker-checker:** implementer draft karta hai, alag reviewer PASS/FAIL deta hai
6. **Connector:** PASS pe PR khulta hai. FAIL/risky pe "needs a human" likh kar ruk jata hai

## Shared Skill (Dono Tools Mein Ek Jaisi)

Save karo `.claude/skills/daily-triage/SKILL.md` (Claude Code) ya `.opencode/skills/daily-triage/SKILL.md`
(OpenCode):

```markdown
---
name: daily-triage
description: >-
  Runs the morning maintenance pass. Reads the progress file, gathers overnight
  CI failures, open issues, and new audit advisories, drafts safe fixes (each
  one checked by a separate reviewer agent), opens pull requests for what passes,
  and writes anything risky to the progress file for a human.
---

# Daily triage

You are the morning maintenance loop. Work through these steps in order.
Do not skip the progress file. It is your only memory between runs.

## 1. Read your memory first
- Open `progress.md`. Read "In progress" and "Open / needs a human".
- Do not redo anything already listed under "Done".

## 2. Find the work
Gather candidates in this order, and stop once you have at most 5:
1. CI runs that failed since the last entry in `progress.md`.
2. Open issues labelled `bug` or `maintenance`.
3. New advisories from `npm audit`.

## 3. Work each candidate
- Create an isolated checkout: a git worktree, or a branch named `claude/<short-slug>`.
- Draft the smallest fix that solves the one problem.
- Send the diff to the reviewer agent. Wait for its verdict.

## 4. Decide from the verdict
- PASS + low risk (no public API change, no data migration, no deletion): open a PR.
- FAIL, or risky: do NOT open a PR. Add an entry to "Open / needs a human".

## 5. Update your memory last
- Move finished items to "Done" with today's date. Save `progress.md`.

## Rules
- Never open more than 5 pull requests in one run.
- Never change `main` directly. Only `claude/*` branches.
- When in doubt, escalate.
```

## Reviewer (Checker) — Dono Files Zaroori Hain

**Claude Code** — `.claude/agents/reviewer.md`:
```markdown
---
name: reviewer
description: Reviews a diff against the spec and the test results. Replies PASS or FAIL with reasons.
tools: Read, Bash
model: claude-haiku-4-5-20251001
---

You are a strict, read-only code reviewer. You never edit files.

1. Run the tests and the linter. Read the output yourself. Do not trust a claim that they pass.
2. Check the change against project conventions in `CLAUDE.md` and the relevant spec.
3. Look for bugs, missing edge cases, security risks, and any change to public behaviour.

Reply with exactly one of:
- `PASS` — followed by one line saying what you verified.
- `FAIL` — followed by the specific reasons, one per line.
```

**OpenCode** — `.opencode/agents/reviewer.md`:
```markdown
---
mode: subagent
model: anthropic/claude-haiku-4-5-20251001
description: Reviews a diff against the spec and tests. Replies PASS or FAIL with reasons. Read-only.
permission:
  edit: deny
  bash:
    "*": deny
    "npm test*": allow
    "npm run lint*": allow
    "git diff*": allow
---

You are a strict, read-only code reviewer. You never edit files.
[... same steps as above ...]
```

## Heartbeat Wire Karna

**Claude Code — Routine** (`claude.ai/code/routines`, weekday 9am, repo + GitHub/Slack connectors):
```text
Run the daily-triage skill.
Start by reading progress.md; finish by updating it.
For each fix: draft it in an isolated worktree, have the reviewer subagent grade it,
open a PR only on PASS, and append anything risky to the "needs a human" section.
```

**OpenCode — GitHub Actions workflow:**
```yaml
name: morning-maintenance
on:
  schedule:
    - cron: "0 9 * * 1-5"
jobs:
  triage:
    runs-on: ubuntu-latest
    permissions: { contents: write, pull-requests: write, issues: write }
    steps:
      - uses: actions/checkout@v6
        with: { persist-credentials: false }
      - uses: anomalyco/opencode/github@latest
        env: { ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }} }
        with:
          model: anthropic/claude-sonnet-5
          prompt: |
            Run the daily-triage skill. Read progress.md first; update it last.
            For each candidate fix: draft it on a new branch, then invoke the
            @reviewer subagent to grade it. Open a PR only when PASS.
```

## Ek Real Subah Kaisi Dikhti Hai

```text
[09:00] daily-triage fires
  → reads progress.md: 1 item "in progress" (lodash bump), nothing new flagged
  → finds: 2 CI failures overnight, 1 new npm-audit advisory
  → CI failure #1 (flaky auth test):
        drafts fix on branch claude/fix-auth-retry
        reviewer → PASS (tests green; retries on token refresh)
        → opens PR #142, links the issue
  → CI failure #2 (type error in report.ts):
        drafts fix on branch claude/fix-report-types
        reviewer → PASS → opens PR #143
  → advisory (image library):
        the safe fix changes the output format
        reviewer → FAIL (public behaviour change)
        → writes it to "Open / needs a human" in progress.md
  → updates progress.md, exits
[you, 09:30] two PRs to review, one flagged item to decide on. You typed nothing.
```

**Kya hua isme:** Loop ne kaam dhoonda, draft kiya, check karwaya, safe hisse ko ship kiya, aur sirf wo
ek decision aapko diya jo waqai insaan ko chahiye. Dono tools mein sirf **heartbeat aur "kahan chalta
hai" farq hai** — beech mein skill, spine, worktree, maker-checker, connector — sab same design.

### Self-Check
**Sawal:** Kya cheez raat mein galat fix ko merge hone se rokti hai?
**Jawab:** 3 cheezein sath: reviewer ko **PASS** lazmi dena, sirf low-risk changes PR khol sakti hain,
aur **human gate** risky/failed kaam ko `main` ki bajaye "needs a human" note mein bhejta hai. Har run
capped aur logged bhi hoti hai.

---
[⬅ Spine](03-spine.md) · [Agla: Human Control ➡](05-human-control.md)
