# 10 — Commands Cheat Sheet (Sab Ek Jagah)

Yeh ek **single-page quick-reference** hai — har command jo is chapter mein kahin bhi use hua, ek jagah.
Poori explanation ke liye peeche wale concept files dekho ([01](01-heartbeats.md),
[02](02-body.md), [08](08-routines-appendix.md)); yahan sirf **command + ek line context**.

## Claude Code — Sab Commands

| Command | Kaam | Concept |
| --- | --- | --- |
| `/loop 5m <prompt>` | In-session loop — timer par prompt dobara chalata hai, jab tak session khula hai | 4 |
| `show my running loops` | Chalti hui in-session loops dikhao | 4 |
| `cancel the <name> loop` | Ek chalti hui in-session loop rok do | 4 |
| `/loop 5m <prompt> --bg` | In-session loop background session mein (terminal band ho tab bhi chalta hai, machine on chahiye) | 4 |
| `/goal <success condition>` | Run-until-done — chhota alag checker-model har turn ke baad "done hain?" puchta hai | 5 |
| `/schedule every weekday at 9am, <prompt>` | Naya cloud Routine banao (scheduled heartbeat) | 6 |
| `/schedule list` | Sab apni Routines dekho | 6 |
| `/schedule run the <name> routine now` | Ek Routine ko turant, one-off fire karo | 6 |
| `/schedule update the <name> routine to <new timing>` | Routine ki schedule badlo | 6 |
| `--worktree` (session flag) | Apni isolated git checkout mein session kholo | 8 |
| `isolation: worktree` (subagent field) | Har subagent ko fresh, khud-saaf-hone-wala checkout do | 8 |

**Subagent define karna** — `.claude/agents/<name>.md` (frontmatter: `name`, `description`, optional
`tools`, `model`) — detail [02-body.md](02-body.md#concept-11-maker-checker--subagents) mein.

**Skill define karna** — `.claude/skills/<name>/SKILL.md` (frontmatter: `name`, `description`, optional
`allowed-tools`) — detail [02-body.md](02-body.md#concept-9-knowledge--skills) mein.

## OpenCode — Equivalent Shell Patterns

Koi built-in `/loop`/`/goal`/`/schedule` nahi — scheduler/trigger khud lagana parta hai. **Shape same
hai, sirf commands alag.**

```bash
# In-session (Concept 4) — Claude Code /loop ka equivalent
while true; do
  opencode run "check if the deployment finished; if it did, say DONE"
  sleep 300   # 5 minutes
done

# Run-until-done (Concept 5) — Claude Code /goal ka equivalent
for i in $(seq 1 8); do          # tries ki hadd — kabhi hamesha ke liye loop na karo
  opencode run "Make the tests in test/auth pass and fix any lint errors."
  if npm test -- test/auth && npm run lint; then
    echo "Condition met on try $i"; break
  fi
done

# Scheduled (Concept 6) — cron, koi vendor cloud zaroori nahi
0 9 * * 1-5 cd /path/to/repo && opencode run "check the CI dashboard and summarize any failures"

# Worktree isolation (Concept 8) — git ke apne worktrees
git worktree add ../wt-feature-a feature-a
git worktree add ../wt-feature-b feature-b
( cd ../wt-feature-a && opencode run "implement feature A" ) &
( cd ../wt-feature-b && opencode run "implement feature B" ) &
wait
```

**Subagent** — `.opencode/agents/<name>.md` (frontmatter: `mode: subagent`, `model`, `description`,
optional `permission` block) — built-in read-only subagents: `general`, `explore`, `scout`.

## Routine API Trigger (Appendix A3)

```bash
curl -X POST https://api.anthropic.com/v1/claude_code/routines/<routine-id>/fire \
  -H "Authorization: Bearer <routine-token>" \
  -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"text": "Sentry alert SEN-4521 fired in prod. Stack trace attached."}'
```
Token ek dafa dikhta hai — turant store karo. Koi built-in dedup nahi (webhooks retry karte hain) —
sender par deduplicate karo, prompt **safe-to-repeat** likho. Full field guide: [08-routines-appendix.md](08-routines-appendix.md).

## Decision Table: Konsa Command Chuno

| Sawal | Jawab | Command |
| --- | --- | --- |
| Kaam khatam hota hai, command prove kar sakti hai? | Conditional loop | `/goal` |
| Kaam repeat hota hai, waqt par? | Schedule | `/schedule` |
| Kaam repeat hota hai, event par (PR, message, webhook)? | Event-driven | Routine + trigger (GitHub/API) |
| Sirf abhi, session khule rehte, kuch "watch" karna hai? | In-session | `/loop` |
| Kaam ek dafa hota hai? | Koi loop nahi | Simple session |
| Laptop band hone par bhi chalna zaroori hai? | Cloud Routine chahiye | `/schedule` ya Routines UI |
| 1-hour se zyada frequent chahiye? | Schedule floor se niklo | API trigger + apna scheduler |

## Save Karne Se Pehle — Minimum Checklist

Poori detail [04-complete-loop-example.md](04-complete-loop-example.md#loop-chalane-se-pehle-minimum-safe-loop-checklist)
aur [08-routines-appendix.md#a6](08-routines-appendix.md#a6--routine-checklist-save-karne-se-pehle) mein.

```
[ ] Success condition — kaam khatam hone ka pata kaise chalega
[ ] Limit — max tries/minutes/spend
[ ] Isolated branch/worktree
[ ] Read-only checker (alag agent/model)
[ ] State file (spine)
[ ] Human gate — risky/fail seedha main pe nahi
[ ] Log/notification — chup chaap fail na ho
```

---
[⬅ Routine Drills + Dreaming](09-routine-drills-and-dreaming.md) · [⬆ Index](README.md) · [Agla: Practice Log ➡](11-practice-log.md)
