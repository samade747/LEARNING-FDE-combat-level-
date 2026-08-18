# 08 — Appendix: Hook Pipeline End-to-End

*Yeh ek field guide hai, spec nahi. Event names aur payloads mechanical layer hain — build karne se
pehle live docs se confirm karo.*

## Woh Lamhe Jo Matter Karte Hain

Hook pipeline barh kar do dozen se zyada events tak pahonch gaya hai, lekin **paanch lamhe** hi
zyada tar real use cover karte hain:

| Lamha | Claude Code Event | OpenCode Surface | Typical Kaam |
| --- | --- | --- | --- |
| Session shuru hota hai | `SessionStart` | plugin init | State load karo, din ka context print karo |
| Tool chalne se pehle | `PreToolUse` | `tool.execute.before` | Risky action check ya rewrite karo |
| Tool chalne ke baad | `PostToolUse` | `tool.execute.after` | Lint, format, log mein trace karo |
| Agent finish karne ki koshish kare | `Stop` | required CI check / pre-commit | Suite chalao, jhoota "done" block karo |
| Subagent finish ho | `SubagentStop` | `opencode run` exit par wrapper script | Typed verdict validate karo |

## Contract, Ek Paragraph Mein

Hook ek **command** hai. Claude Code mein event ki detail JSON ki shakal mein stdin par milti hai
(command ka input stream), apni khud ki wrappers mein arguments ki tarah. Jawab **exit code** se deta
hai. Zero pass hai. Gate events (`PreToolUse`, `Stop`) par, blocking code **`2`** action ya finish ko
rok deta hai. Koi bhi doosra non-zero code ek non-blocking error hai jo kuch nahi rokta. After-events
(`PostToolUse`) par action already chal chuka hota hai, isliye code usay undo nahi kar sakta. Lekin
exit `2` par, hook ne stderr par jo bhi print kiya wo agent ko wapas **uske agle input** ki tarah milta
hai. Yehi hissa design surface hai: hook jo print kare *"blocked: tests failing in test/auth: fix those
first"* — wo **ek** waqt mein guardrail bhi hai aur AX-grade error message bhi.

## Teen Drills

- **Drill 1 — Stream Dekho.** Ek hook (ya plugin) lagao jo har tool call ki ek line `trace.log` mein
  append kare. Ek normal beat chalao, phir log parho. Zyada tar log yeh dekh kar surprise hote hain ke
  ek beat kitne actions leti hai. Yehi surprise observability ka poora point hai.
- **Drill 2 — Jaan-Boojh Kar Block Karo.** `PreToolUse` check likho jo koi bhi Bash command block kare
  jismein `curl` ho, error mein allowed alternative ka naam ho. Agent se URL fetch karwao aur back-and-
  forth dekho: block hua, inform hua, redirect hua.
- **Drill 3 — Conditional Gate.** Test-suite wala `Stop` hook sirf tab chalao jab beat mein source
  files change hui hon (`if` condition, ya `git diff --name-only` check). Slow checks jo sirf tab
  chalein jab zaroorat ho — yehi wajah hai harness kaafi fast rehti hai use karne layak.

---
[⬅ Practice Projects](07-practice-projects.md) · [⬆ Index](README.md)
