# Hermes with General Agents — Summary

**Hermes** aapka self-improving AI Employee hai — Nous Research ka open-source agent jo aapki apni infrastructure pe chalta hai. OpenClaw ne breadth pe bet lagai (har channel pe reach); Hermes ne depth pe bet lagai (seekho, compound karo). Personal Agent Harnesses section ka doosra/aakhri chapter.

## OpenClaw Se Farq

| | OpenClaw | Hermes |
| --- | --- | --- |
| Bet | Breadth | Depth (seekhna) |
| Memory | Deliberately commit | Khud commit, wall ke bagair |
| Skills | Install karte ho | Khud likhta hai |
| Model | Fixed | Swap, koi lock-in nahi |

Ehtiyat: "Self-improving" ki honest ceiling — memory/skills curate hoti hain, model retrain nahi hota. Asal risk **quiet drift** hai, isliye monthly audit zaroori.

## 00 — Install Aur Chat (Scenario 1)

- Wahi 5-step OpenClaw rhythm: sentence paste, AGENTS.md consult, plan approve, seam pe ruko, observable outcome pe done.
- Install se pehle 4 risks + guardrails: runaway spend (spending limits), prompt injection (draft-over-send), skills supply-chain risk (source parho, version pin), destructive actions/leaks (secrets `~/.hermes/.env` mein, chat mein kabhi paste nahi).
- Official skill install: `npx -y skills add nousresearch/hermes-agent`.
- Scenario 1: free Gemini key se install/setup (`hermes claw migrate --dry-run` OpenClaw se migrate ke liye), `hermes doctor` green verify, TUI mein real tool-fired task test.

## 01 — Phone Se Reach Aur Hard Task (Scenarios 2-3)

- Hermes ulta bana hai: "runs anywhere, lives where you do" — 20+ platforms se reachable (Telegram/Discord/Signal gateway).
- Scenario 3: **closed learning loop** — substantial task ke baad Hermes decide karta hai memory rakhni hai ya skill likhni hai `~/.hermes/skills/` mein. Deterministic lever agar khud na kare: task fix karo, "save that as the way you want this done" bolo. `description` field hi decide karti hai skill agli baar fire hogi ya nahi.

## 02 — Memory Aur Model-Swap (Scenarios 4-5)

- Scenario 4: OpenClaw ka wall (deliberately commit) Hermes mein khatam — khud memory curate karta hai, past-session full-text recall se, `/new` fresh session mein bhi yaad rakhta hai. Contrast: OpenClaw auditable (aap likhte ho), Hermes convenient (periodically `memories/` parhna zaroori).
- Scenario 5a: skill reuse — similar task pe pehle-likhi skill load hoti hai aur update hoti hai (live example: v0.1.0 → v1.0.0, raw curl se built-in web search tak).
- Scenario 5b: model swap — durable asset skill+memory layer hai, brain replaceable hai, ek command se switch. Ehtiyat: swap aasan hai, har model equal nahi — skill ko chhote model ke liye optimize karo.

## 03 — Automate Aur Voice (Scenarios 6-7)

- Scenario 6a: natural-language scheduled job (morning digest), leaner toolset by default (koi web search/messaging jab tak `enabled_toolsets` na set ho).
- Scenario 6b: worker backup — private Git repo (zip nahi) taake skill history + rollback mile.
- Scenario 7 (bonus): Telegram voice reply — free Edge TTS, non-interactive setup; bonus microphone loop bhi.

## 04 — Monthly Audit Aur Beyond

- **Monthly audit:** skills (khud likhi vs installed, stale hataao), memory (MEMORY.md/USER.md correct karo), supply chain (`hermes skills audit`).
- Real tools se connect: MCP servers ya Composio-jaisa aggregator — draft-over-send, sirf zaroori connect karo.
- **7-rung ladder:** Download &amp; go → It knows you → Commands &amp; model-agnostic → Integrator → Orchestration → Builder → One operating system.
- **3 complementary open layers:** OpenClaw (gateway/breadth), Hermes (learner/depth), Paperclip (orchestrator — teams/org charts/budget/audit). Zyada tar serious setups combine karte hain; Hermes ka official Paperclip adapter hai.
- Sensitive data pe real kaam se pehle governed wrapper (NVIDIA NemoClaw jaisa) ke peeche daalo.
