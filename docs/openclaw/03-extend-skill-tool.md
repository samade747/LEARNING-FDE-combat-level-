# 03 — Skill Aur Tool Se Extend Karna (Scenario 5)

**2 alag tareeqe** capabilities add karne ke:

- **Skill** — folder jismein `SKILL.md` hai: **expertise** jo agent khud invoke karta hai jab task match
  kare. Cross-runtime spec follow karti hai (agentskills.io) — same folder OpenClaw, Claude Code,
  OpenCode, 50+ mein chalta hai. Registries: [skills.sh](https://skills.sh), [ClawHub](https://clawhub.ai)
- **MCP tool** — **capability** jo agent call kar sakta hai: external service jo functions expose karta
  hai MCP se (time, database, calendar)

**Shape same hai:** install/configure → gateway restart → verify loaded → phone se test.

## 5a: Ek Skill Add Karo Jo Aap Waqai Karte Ho

> **Ehtiyat:** Installed skill jo fire nahi hoti, **almost hamesha description mismatch** hoti hai —
> install kaam kar gayi, message sirf skill ki trigger description se match nahi hua.

**Prompt 1 — discover:**
```text
Check whether the find-skills skill is already installed. If it
isn't, install it with Global scope. Use it to search skills.sh
against my USER.md and propose two or three real skills that fit
how I work. Don't install yet.
```

**Prompt 2 — install + verify:**
```text
Install [your pick] with Global scope, restart the gateway. List
the SKILL.md description back to me so I know exactly what to send
to trigger it.
```

**Done jab:** Agent ne confirm kiya skill installed hai, **aur** test input ne skill-specific format wala
reply diya (generic answer nahi).

## 5b: Ek External Tool Connect Karo (Bina Credentials)

`mcp-server-time` — canonical hello-world MCP. Koi API key nahi, 2 tools (`get_current_time`,
`convert_time`).

> **Ehtiyat: MCP chup chaap fail hoti hai.** Misconfigured server chat mein koi error nahi deta — agent
> ko bas tool nahi milta. **Gateway log hi diagnostic hai.**

```text
Set up the standard mcp-server-time example (no API key needed).
After the gateway restart, prove `time` is registered with 2 tools.
```

Phone se real time question poocho:
> *"Agar main ye proposal abhi [client ka city] bhejoon, unka local time kya hai? Reasonable hour hai
> email karne ke liye?"*

**Done jab:** `time` server 2 tools ke sath registered hai, **aur** real time question ka specific live
jawab mila, **aur** dashboard mein `get_current_time` tool badge dikhi (proof ke agent ne tool call kiya,
hallucinate nahi kiya).

## Activation Dance

Har OpenClaw extension (skills, plugins, MCP servers, channels, hooks) **isi 4-step pattern** se guzarti
hai: **exists → disabled by default → enabled → configured (restart).** Ek dafa pattern dekh lo, har
naya feature familiar lagega, broken-on-first-try nahi.

> **Scenario 6 ke liye carry-forward:** Skill aur MCP tool `USER.md` mein add karwao taake scheduled
> jobs unhe jaanein, phir backup repo mein push karo.

---
[⬅ Identity Customize Karna](02-customize-identity.md) · [Agla: Automate + Audit ➡](04-automate-audit.md)
