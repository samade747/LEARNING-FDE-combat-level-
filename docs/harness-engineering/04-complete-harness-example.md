# 04 — Ek Complete Harness (Hardened Morning Triage)

## Loop Chalane Se Pehle: Minimum Safe Harness Checklist

Kisi bhi loop ko unattended chalane se pehle, harness mein ye **8 cheezein** honi chahiye:

1. **Deny list** — jo actions bilkul namumkin hain
2. **Fence** — worktree/sandbox territory jo chhor nahi sakta, gated branches
3. **Lean, described tools** — sirf jo kaam ke liye chahiye, har ek ki achi description
4. **Kam se kam ek blocking hook** — verify gate jo model skip na kar sake
5. **Typed verdict** — checker ka jawab aisi shape mein jo code validate kar sake
6. **Escalation path** — malformed ya risky results insaan tak, **visibly**
7. **Log jo aap asal mein parhein** — har action record, cost samet
8. **Wapas jane ka raasta** — checkpoints aur resume path, taake fail hui run restart na ho, resume ho

Koi ek missing ho to harness mein ek **hole** hai — bilkul wahan jahan model aakhir kar bhatak jayega.

## Loop Wahi, Harness Naya

**Loop Engineering** wali morning-triage loop lo, shape bilkul wahi rakho, aur usay wo harness do jo
usay pehle se milna chahiye tha. Wahi skill, wahi spine, aur ek jaan-boojh kar change: heartbeat **3am**
pe move ho jata hai — kyunke harness sab se zyada wahi matter karti hai jab koi awake na ho.

**Harness plan (dono tools mein same):**

1. **Constrain:** tests/diffs free chalte hain, pushes sirf `claude/*` pe, force-push aur `rm -rf` ke
   common spellings deny, sandbox + branch protection asli deewarein hain
2. **Inform:** triage skill wahi rehti hai, reviewer sirf file reads + 3 commands (`npm test`,
   `npm run lint`, `git diff`) tak mehdood
3. **Verify:** edit ke baad lint automatic, commit se pehle aur required CI mein hamesha. Tests har
   beat gate karti hain. Reviewer ab **JSON** deta hai
4. **Correct:** `HARNESS.md` ratchet log — har classified failure ek surface pe ek line
5. **Escalate:** malformed verdicts aur high-risk passes "needs a human" mein, run log loudly bolta hai

### Claude Code — `.claude/settings.json`

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Bash(npm test *)",
      "Bash(npm run lint *)",
      "Bash(git diff *)",
      "Bash(git push origin claude/*)"
    ],
    "deny": [
      "Read(./.env)",
      "Read(./secrets/**)",
      "Bash(rm -rf *)",
      "Bash(git push --force *)"
    ]
  },
  "hooks": {
    "PostToolUse": [
      { "matcher": "Edit|Write", "hooks": [
        { "type": "command", "command": "npm run lint --silent >&2 || exit 2" }
      ]}
    ],
    "Stop": [
      { "hooks": [
        { "type": "command", "command": "npm test --silent >&2 || exit 2" }
      ]}
    ]
  }
}
```

### `.claude/agents/reviewer.md` — Typed Verdict + Enforceable Command Limit

```markdown
---
name: reviewer
description: Grades a diff against the spec and tests. Returns a JSON verdict.
tools: Read, Bash
model: haiku
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: ".claude/hooks/reviewer-allowlist.sh"
---

You are a strict, read-only reviewer. Run the tests and linter yourself;
do not trust claims. Then reply with ONLY a JSON object:

{ "verdict": "PASS", "reasons": [], "risk": "low" }

Any public behaviour change is risk: "high".
```

```bash
#!/bin/sh
# .claude/hooks/reviewer-allowlist.sh — reviewer sirf ye 3 commands chala sakta hai
cmd=$(cat | jq -r '.tool_input.command // empty')
case "$cmd" in
  "npm test"*|"npm run lint"*|"git diff"*) exit 0 ;;
  *) echo "Blocked: reviewer may run only npm test, npm run lint, git diff" >&2
     exit 2 ;;
esac
```

**Routine ke prompt mein escalation contract:**
```text
Run the daily-triage skill. Treat the reviewer's reply as JSON. If it is
not valid JSON, or verdict is FAIL, or risk is "high": open no PR, append
the item with the reviewer's reasons to "Open / needs a human" in
progress.md, and continue to the next candidate.
```

### OpenCode — `opencode.json` + Pre-Commit + Reviewer

```json
{
  "permission": {
    "edit": "allow",
    "bash": {
      "*": "ask",
      "npm test*": "allow",
      "npm run lint*": "allow",
      "git diff*": "allow",
      "git push origin claude/*": "allow",
      "git push --force*": "deny",
      "rm -rf*": "deny"
    }
  }
}
```

```bash
#!/bin/sh
# .git/hooks/pre-commit — local verify gate (bypassable, isliye CI asal gate hai)
npm run lint --silent && npm test --silent || {
  echo "pre-commit: lint or tests failed — commit blocked"; exit 1;
}
```

GitHub Actions beat validate karti hai believe karne se pehle, protocol break pe escalate karti hai.
Repo settings last fence dete hain: `main` pe branch protection, required CI check ke saath.

> **Honest audit:** OpenCode side pe kam checklist boxes tool ke andar rehte hain, zyada platform mein
> — fence container+worktree hai, log Actions workflow log hai, checkpoint store commit hai, merge gate
> CI+branch protection hai. **Same 8 boxes, alag owners.**

## Ek Bura Din — Harness Ke Saath Aur Bagair

Same loop, same model, same malicious issue queue mein. Sirf variable: **harness**.

```text
BAGAIR (sirf loop course ki files):
[03:00] beat fires → malicious-injection issue parhta hai
  → agent, steered: .env parhne ki koshish ... kuch nahi rokta
  → curl se file bahar bhejne ki koshish ... kuch nahi rokta
  → failing test ko "fix" karta hai delete kar ke ... lint kabhi chali hi nahi
  → reviewer: "PASS — tests are green now" ... hain: test hi gayab hai
  → PR khulta hai; aap adhi neend mein 09:10 pe merge kar dete ho
[09:40] pata chalta hai kya ship hua. Transcript hi record hai.

SAATH (is course ki files add ki gayin):
[03:00] beat fires → malicious-injection issue parhta hai
  → .env parhne ki koshish ..... deny rule: blocked, logged
  → curl se bahar bhejne ki koshish ..... network fence: unreachable, logged
  → failing test delete karta hai ..... suite green ho jati hai: false pass
  → reviewer diff parhta hai: {"verdict":"FAIL","reasons":["test deleted, not fixed"],"risk":"high"}
  → koi PR nahi; item "needs a human" mein reasons ke sath
[09:10] aap ek flagged item aur 2 blocked actions ka log parhte ho.
        HARNESS.md mein ek line add karte ho. Ratchet ghumta hai. Aap ne kuch type nahi kiya.
```

**Zaroori baat:** Harness ne agent ko smart nahi banaya. Model bilkul same tha. Isne **system ko honest**
banaya: buri actions **namumkin** ho gayin, bura kaam **visible** ho gaya, aur asal decision asal
decision-maker (aap) tak pohanchi. Aur wo deleted test dekho — suite green ho gaya, lekin sirf
**diff-reading reviewer** ne pakra ke **kya remove hua tha**. Tests prove karte hain jo bacha hai wo
kaam karta hai. Ye prove nahi kar sakte ke sab zaroori cheez abhi bhi mojood hai. **Green suite proof
nahi, evidence hai.**

---
[⬅ Verify & Correct](03-verify-correct.md) · [Agla: Staying the Engineer ➡](05-staying-the-engineer.md)
