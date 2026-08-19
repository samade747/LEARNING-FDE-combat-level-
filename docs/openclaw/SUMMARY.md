# OpenClaw with General Agents — Summary

OpenClaw ko apna **Personal AI Employee** banana: WhatsApp/Telegram/Discord se reply karne wala open-
source assistant, jo aap apne general agent (Claude Code/OpenCode) se install/configure karte ho — agent
sab kaam karta hai, aap sirf wo faislay lete ho jo sirf aap le sakte ho.

## Collaboration Pattern (Poore Course Mein Repeat Hota Hai)

5-step rhythm har scenario mein: (1) aap ek sentence paste karte ho, (2) agent `AGENTS.md` consult karta
hai aur plan propose karta hai, (3) aap approve karte ho aur dekhte ho, (4) agent **seam** pe rukta hai
(sirf aap kar sakte ho — QR scan, API key, OAuth), (5) aap "done" ho jab ek observable cheez hoti hai.

## 00 — Collaboration Pattern + Install (Scenario 1)

- 3 actors: aap, general agent, OpenClaw. Universal recovery move: gateway log parho, plain-language
  problem+fix propose karo.
- Download: `openclaw-with-general-agents.zip` — 2 files (`AGENTS.md` ~600-line operational reference,
  `CLAUDE.md` = `@AGENTS.md`). Confirm brief loaded: "What can you do for OpenClaw?"
- **Scenario 1:** OpenClaw laptop pe, Gemini free tier, dashboard reply. Plan → approve step-by-step →
  agent apna end-to-end check karta hai + browser dashboard bhi. Done: CLI aur browser dono reply dein,
  footer `gemini-3.5-flash` dikhaye. ~5 underlying commands (`npm install -g openclaw`, `onboard
  --install-daemon`, `gateway status`, `dashboard`, `doctor`) — sab `~/.openclaw/` mein (config, key,
  workspace/brain).

## 01 — Channel Pair Aur Delegate (Scenarios 2-3)

- **Scenario 2:** Phone se pairing — WhatsApp preferred (doosra number + Business account, personal nahi —
  library unofficial hai), Telegram (BotFather), Discord (Developer Portal + 3 privacy intents). Agent QR/
  token step khud render nahi kar sakta — ruk kar naya terminal window bolta hai. Phone ab ek
  **authenticated path** hai — credential ki tarah treat karo.
- **Scenario 3:** Real task delegate karna proves "AI Employee" chatbot se alag hai — **agent loop**.
  6-line log shape: inbound message → model call → tool call → tool result → doosri model call → outbound
  message. Yehi loop hai; agli scenarios sirf isi loop mein tools/triggers add karti hain.

## 02 — Voice Aur Memory Customize Karna (Scenario 4)

- Behavior `~/.openclaw/workspace/` markdown files se: **SOUL.md** (personality/tone), **IDENTITY.md**
  (naam/role), **USER.md** (aapke baare mein), **MEMORY.md** (durable, channels ke aar-paar facts). Har
  file lean rakho, churn mat karo (context cost). Edit ke baad `/reset` zaroori (nahi to cached system
  prompt reh jata hai).
- **4a SOUL.md:** tone change → `/reset` → verify diff visible. **4b IDENTITY.md:** naam do → verify.
  **4c USER.md:** context sikhao → verify factor mein ata hai. **4d MEMORY.md** (alag hai — sirf main
  session mein load): 4-step test — paired channel remembers (session/channel automatic), dashboard alag
  session **nahi** janta (wall — per-channel, shared nahi), "commit to long-term memory" bolne se
  `MEMORY.md` banti hai, dashboard `/reset` ke baad ab janta hai (wall cross ho gayi).
- **4e Backup:** workspace = poori identity, laptop mar jaye to sab kho jata hai — private GitHub repo
  mein backup + recovery one-liner save karo. Identity ab laptop-wipe survive kar sakti hai.

## 03 — Skill Aur Tool Se Extend Karna (Scenario 5)

- **Skill** (folder + `SKILL.md`, agent khud invoke karta hai jab task match kare, cross-runtime spec —
  50+ tools mein chalti hai, registries: skills.sh, ClawHub) vs **MCP tool** (external service ki
  capability, agent call kar sakta hai).
- **5a:** find-skills se discover karo (`USER.md` ke against propose), phir install+restart+verify —
  install-worked-but-trigger-mismatch sabse common failure hai (description mismatch).
- **5b:** `mcp-server-time` (no API key, 2 tools) connect karo. **MCP chup chaap fail hoti hai** — gateway
  log hi diagnostic hai. Real time-question test karo, dashboard tool-badge se prove karo hallucinate
  nahi hua.
- **Activation Dance (4-step, sab extensions ke liye):** exists → disabled by default → enabled →
  configured (restart).

## 04 — Automate Karna Aur Monthly Audit (Scenarios 6-7)

- **Scenario 6:** Schedules ulta karti hain — agent clock/interval pe act karta hai. 3 flavors: cron
  (most-used, precise times), heartbeat (ambient checks fixed cadence), hooks (event triggers, out of
  scope). **6a:** 5-min demo heartbeat dekho phir band karo. **6b:** ek real schedule chuno (USER.md se
  suggested options), setup + backup repo mein commit — isay on chhoro.
- **Scenario 7 (Monthly Audit):** AI Employee waqt ke sath accumulate hota hai (skills, credentials, tools,
  memory, autonomous calls) — har addition chhota approved decision hai, chain opaquely compound hoti hai.
  Defense: install-time vigilance nahi, **fixed-cadence 10-min review**. Kam se kam ek decision lo (delete/
  revoke/prune/uninstall), agle mahine calendar mark karo.

## 05 — NemoClaw Se Sandbox Karna (Scenario 8)

- Problem: Employee jo poora computer + koi bhi website reach kar sakta hai safe hai **sirf jab tak sirf
  aap** message karte ho. Doosron ke messages handle karte hi (support inbox) power khatra ban jati hai —
  **prompt injection** (buri instruction normal-lagne wale message mein chhupi).
- Solution: sandbox — locked cage (1 folder + chhoti allow-list). **NemoClaw** (NVIDIA) OpenClaw ko
  **OpenShell** cage ke andar chalata hai. Pairing controls **kaun** message kar sakta hai; sandboxing
  controls **wo jo parhe uske sath kya kar sakta hai** — dono chahiye.
- **4 Layers:** Foundation (Linux container/Docker/WSL2), Guard (NemoClaw — deewaron ke bahar, provider
  key rakhta hai, sirf yehi dial-out karta hai), Prison (OpenShell — asal deewarein), Employee (OpenClaw,
  ab prison ke andar).
- "Sirf Aap Kar Sakte Ho" table: admin pop-ups/restart, sandbox login, wizard answers, provider API key —
  agent OS-security-prompts approve nahi kar sakta.
- 4 setup prompts (goal → foundation → NemoClaw+wizard → dashboard+prove), OpenRouter provider key
  example. Common issues: silent-429 (free-tier limit), `127.0.0.1` vs `172.x` dashboard link, file-must-
  be-in-cage-workspace, memory-warning-refuse (Linux layer needs more memory).
- **Full-system table (post-Scenario-6):** background service, channel pairing, 7 workspace files, GitHub
  backup, 1 skill, 1 external tool, 1 scheduled task — 7 artifacts jo "kal zaroori" banate hain.
