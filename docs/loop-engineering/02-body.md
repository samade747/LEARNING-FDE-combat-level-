# 02 — Body: Loop Har Run Mein Kya Karta Hai

Heartbeat loop **start** karta hai. Ye 4 parts wo hain jo loop **har beat pe karta hai** — jab koi
insaan dekh nahi raha, tab ye asal mein matter karte hain.

## Concept 8: Isolation — Worktrees

Jaise hi loop ek se zyada agent ek saath chalata hai, wo ek dusre ki files overwrite karna shuru kar
dete hain — bilkul waisay jaise do log ek hi lines edit karein bina batayen. **Git worktree** isko fix
karta hai: alag working folder, apni branch pe, lekin same repo history share karte hue. Ek agent ke
edits doosre ke checkout ko touch nahi kar sakte.

**Claude Code:** `--worktree` flag se apni checkout mein session khulti hai. Subagent pe
`isolation: worktree` set karo — har helper ko fresh, khud-saaf-hone-wala checkout milta hai.

**OpenCode:** Koi single flag nahi — git ke apne worktrees use karo:
```bash
git worktree add ../wt-feature-a feature-a
git worktree add ../wt-feature-b feature-b
( cd ../wt-feature-a && opencode run "implement feature A" ) &
( cd ../wt-feature-b && opencode run "implement feature B" ) &
wait
```

## Concept 9: Knowledge — Skills

Loop har baar **fresh session** se start hota hai — matlab project ki aadaton ki koi memory nahi. Bina
madad ke, har beat pe apna setup guess karta hai — tokens waste, ghaltiyan invite. **Skill** yehi
knowledge hai jo ek dafa `SKILL.md` mein likh di jati hai, jo agent har run pe parhta hai.

**Rule:** Jo bhi cheez aap har run pe dobara explain karte, wo skill mein honi chahiye — triage steps,
project ki aadatein, "hum ye tareeqa is liye nahi karte kyunke pehle ek dafa problem hui thi" — sab.

> Loop prompt ko chhota rakho: schedule ka prompt sirf ek line ho — *"run the daily-triage skill"* —
> aur skill sara detail sambhale. Kam tokens, aasan updates.

## Concept 10: Action — Connectors (MCP)

Loop jo sirf files parh sakta hai, wo sirf **baat** kar sakta hai. Connectors (MCP pe bane) usay **karne**
dete hain — PR kholna, Linear ticket update karna, Slack pe post karna, database query karna. Farq: ek
loop kehta hai "ye raha fix", doosra loop PR khol deta hai, ticket link karta hai, aur CI green hote hi
channel pe post kar deta hai.

### Loop Mein Connector Ki 3 Zaroori Baatein

Loop retry karta hai aur tools **khud** chunta hai — is se acha tool set ka matlab badal jata hai:

1. **Kam, focused tools > bohat saare overlapping tools** — Model har beat pe tool choose karta hai,
   koi dekh nahi raha. 100 overlapping tools dedo, wo confuse ho jayega. Rule of thumb: agar ek human
   engineer confidently na keh sake konsa tool fit hai, to agent bhi nahi keh sakta.
2. **Writes dobara chalane pe safe hon** — Agar loop retry karta hai aur wahi write dobara call hoti
   hai, to duplicate record ban sakta hai (jaise dobara customer create ho jana). "Update-or-create"
   jaisi operations behtar hain blind "create" se.
3. **Error messages batayen agla step kya hai** — Loop mein, error message hi agle beat ka input hota
   hai. *"Permission denied: request the repo scope"* khud fix ho jata hai agli try mein. *"Error 403"*
   ek beat waste kar deta hai.

## Concept 11: Maker-Checker — Subagents

**Loop ka sab se important decision:** jo agent kaam **banata** hai, wo apna kaam khud **approve** nahi
kar sakta. Model apne aap ko zyada aasani se pass kar deta hai. Doosra agent — alag instructions, kabhi
alag model — wo galtiyan pakar sakta hai jo pehle wale ne miss ki. Isay **LLM-as-judge** bhi kehte hain.

**Claude Code:** `.claude/agents/` mein subagents define karo — ek explore karta hai, ek implement karta
hai, ek spec/tests ke against check karta hai.

**OpenCode:** `general`, `explore`, `scout` (read-only) built-in subagents. Checker ko apna **model** do
— sasta, read-only.

```markdown
---
mode: subagent
model: anthropic/claude-haiku-4-5-20251001
description: Reviews a diff against the spec and tests. Replies PASS or FAIL with reasons.
---

You are a strict code reviewer. You do not make changes.
Check the diff against the spec and the test results, then reply PASS or FAIL with the reasons.
```

> Subagent chalane mein zyada tokens lagte hain — ye ek trustworthy checker ki keemat hai. Isay wahan
> use karo jahan doosri opinion matter karti hai (jo bhi loop aapki gairhaziri mein commit karega).
> Throwaway, read-only chores ke liye skip kar sakte ho.

---

## Interlude: Body Ko "Codify" Karna — Dynamic Workflows

Ab tak beat ka body (kaam dhoondo, fix draft karo, alag agent se grade karwao) agent turn-by-turn banata
tha. Claude Code ab poori orchestration ko **ek re-runnable script** likhne deta hai — isay **dynamic
workflow** kehte hain. Aap task describe karo, Claude script likhta hai jo kaam kai subagents mein
baant deta hai, aur background mein chalta hai.

**Zaroori warning:** Workflow ek **beat ka body** hai, **loop nahi**. Ye ek baar chalta hai aur khatam
hone pe sab bhool jata hai — na heartbeat, na spine. Loop teeno ka combo hai: **heartbeat** (Routine,
`/loop`, ya cron) jo beat fire karta hai, **workflow** jo body chalata hai, aur **progress file** jo
agli firing ke liye spine ka kaam karti hai.

> Yaad rakhne ka tareeqa: workflow engine hai, Routine chabi ghumati hai, aur `progress.md` agli trip ke
> liye information carry karta hai.

---

## Interlude: Checker Ko "Codify" Karna — Verification Skills

Ye **checker** ko codify karne ke baare mein hai. Anthropic isay **verification loop** kehte hain: agent
apna kaam check karta hai aur fix karne ki koshish karta hai, baar baar, jab tak check pass na ho jaye.

**Konse checks likhne chahiye:** Jo bhi cheez aap **har dafa haath se** correct karte ho, jab agent kaam
khatam kare — wahi likhne ke qabil hai. Jaise "error logs mein request body kabhi na ho, sirf request ID
ho" — ye ek fixed rule hai jo koi general linter kabhi include nahi karega, kyunke ye **aapki** hai.

```markdown
# .claude/skills/verify-log-hygiene/SKILL.md
---
name: verify-log-hygiene
description: Check that error logs include the request ID and never
  include the request body. Use when the diff touches error handling
  or logging.
allowed-tools: [Read, Edit, Grep]
---

Read the error-handling paths in the current diff.
For each log call on an error path, confirm it includes the request ID
and does not pass the request body, headers, or any user-supplied payload.
Report each violation with file:line, then fix it.
```

### Ek Check Ke 4 Ghar (Homes) — Har Ek Alag Heartbeat

1. **Standalone** — Aap khud invoke karte ho (aap hi heartbeat ho). Un checks ke liye jo har change pe
   apply nahi hote — security scan, licence sweep.
2. **Embedded** — Check us skill ke end mein chipka diya jata hai jo kaam banati hai, taake bina puche
   chal jaye. Sirf un skills pe kaam karta hai jo **aap edit kar sakte ho**.
3. **Chained** — Ek skill doosri ko end pe call karti hai. *"Main hamesha check chalata hoon"* ki aadat
   ab *"skill hamesha check chalati hai"* ka contract ban jati hai. `/code-review` → `/simplify` →
   `/verify` jaisi chain.
4. **Har PR pe** — Chain jab aapke liye theek chal jaye, to wahi checks har PR pe (event heartbeat se)
   chalne lagte hain. Yahan check **personal** se **team** infrastructure ban jata hai.

**Graduation rule:** Home 4 se shuru mat karo. Jab aap khud ko har dafa check chalate hue pakro, tab
embed/chain karo. Aur jab tak chain khud badal rahi ho, PR-wide gate mat lagao — kyunke ek dafa team ka
gate ban jaye, to har change sab ko dikhti hai.

---
[⬅ Heartbeats](01-heartbeats.md) · [Agla: Spine ➡](03-spine.md)
