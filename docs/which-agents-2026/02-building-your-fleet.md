# 02 — Apna Fleet Banana

## General Agents (Jo Tum *Use* Karte Ho)

### Cowork: Enterprise AI Employee

Cowork Anthropic ka AI employee hai business professionals ke liye jo terminal mein kaam nahi karte.
Claude Desktop app ke andar chalta hai (macOS aur Windows).

**Socho isay:** ek knowledgeable coworker jo wo kaam karta hai jiske liye tumhare paas kabhi time nahi
hota — reports banana, documents analyze karna, files organize karna, presentations draft karna, aur
recurring tasks manage karna. Workplace tools se connect hota hai (mail, drive, chat, calendar,
e-signature, spreadsheets, slides). Anthropic ne major enterprise upgrade shipped kiya hai: private
plugin marketplaces, department-specific plugins (HR, finance, engineering, legal, operations), aur
`/schedule` command jo tasks automatically chalata hai (jaise har Monday competitor analysis).

### Claude Code: All-Purpose General Agent

Anthropic ne banaya, tumhare computer par chalta hai. Naam ke bawajood, sirf code se bohat zyada karta
hai — Anthropic ne apna framework "Claude Code SDK" se **Claude Agent SDK** rename kiya kyunke teams
research, video production, data analysis, note-taking, aur non-coding tasks ke liye use kar rahi thi.

**Socho isay:** general-purpose agent jo computer par wo sab kar sakta hai jo tum kar sakte ho, bas
tez. Skills system (reusable SKILL.md files) aur specialized sub-employees ko delegate karne ki ability
Agent Factory method ke building blocks hain.

### Codex: Power Engineering AI Employee

OpenAI ka AI general agent hard engineering problems ke liye. Do modes mein chalta hai: cloud mode
(isolated environment mein khud se, kuch minutes se half-hour tak) aur local CLI tool.

**Socho isay:** specialist jo hardest jobs ke liye call karte ho. Jab Claude Code everyday handle karta
hai, Codex complex reasoning ke liye bana hai — system architectures jo deep thinking maangte hain.

## Personal AI Employees (Jo Tum *Banate Aur Deploy* Karte Ho)

### OpenClaw: Personal AI Employee

Peter Steinberger ne banaya, major sponsors (OpenAI, Vercel included) backed. GitHub par most-starred
software project ban gaya launch ke mahino mein.

**Socho isay:** tireless personal assistant jo tumhare messaging apps se connect hota hai — email sort
karta hai, calendar manage karta hai, flights book karta hai, insurance paperwork handle karta hai, aur
jo bhi daily tasks tum sikhao. WhatsApp, Telegram, Discord, Slack, Signal, iMessage — sab se.

Fully open source (MIT license). Apni machine par chalate ho, apna AI model choose karte ho (Claude,
GPT, DeepSeek), aur ClawHub marketplace se hazaron community-built skills se extend karte ho. Iska
persona ek Markdown prompt file (SOUL.md) se shape hota hai.

### NanoClaw: Secure AI Employee

Lightweight, security-first alternative to OpenClaw. OpenClaw ke paas ~half-million lines of code
hain; NanoClaw wahi core experience deta hai codebase mein jo parh kar samjha ja sake.

**Socho isay:** OpenClaw with a locked door. Har AI employee apne container mein chalta hai — walled-off
environment jahan sirf wo files dekh sakta hai jo tum explicitly allow karo, koi internet access nahi
bina grant ke. Isolation real hai, sirf software setting nahi.

## Tumhari Journey Is Kitaab Mein

| Book Section | Kya Seekh Rahe Ho | Primary AI Employee | Supporting |
| --- | --- | --- | --- |
| **Part 1**: Foundations | AI employees kya hain, kaise kaam karte ho | Claude Code | OpenClaw |
| **Part 2**: Workflow Primitives | File processing, data extraction, version control | Claude Code | None |
| **Part 3**: Business Domains | Finance, legal, marketing, operations workflows | Claude Cowork | Claude Code |
| **Part 4**: Natural Language Programming | TypeScript, Python development, testing, debugging | Claude Code | Codex |
| **Part 5**: Building OpenClaw Apps | Apna OpenClaw-based app banana aur ship karna | OpenClaw | Claude Code |
| **Part 6**: Building Agent Factories | Frameworks, tool protocols, databases, evaluation | Claude Code | NanoClaw |

## The Big Picture: Tumhara Agent Fleet

Koi bhi ek hi AI employee use nahi karta. 2026 ka most effective setup ek **fleet** hai: General Agents
roz-marra ka kaam handle karte hain, Personal AI Employees tumhare messaging apps aur business
workflows mein autonomously chalte hain.

Fleet ka matlab har tool roz use karna nahi. Practically, zyada tar logon ke paas ek daily-driver aur
ek specialist hota hai — jaise Claude Code + OpenClaw, ya Cowork + NanoClaw, ya Claude Code + Codex.
Goal tool-collection nahi, **coverage** hai: ek agent apne default workflow ke liye, ek agent un jobs ke
liye jo default tool nahi karta.

**General Agents wo hain jo tum *use* karte ho. Personal AI Employees wo hain jo tum *banate aur
deploy* karte ho** — aur aakhir mein bechte ho. Yeh kitaab dono sides sikhati hai: Claude Code, Cowork,
aur Codex se maximum leverage lena, aur OpenClaw/NanoClaw se apne Digital FTEs banana jo doosre log pay
kar ke use karein.

## Migration & Fleet Evolution

Common timeline: **Day 1** — OpenClaw + Claude Code ya Cowork. **Month 3** — Codex add karo tough
engineering ke liye. **Month 6** — NanoClaw introduce karo sensitive tasks ke liye, ya SKILL.md/SOUL.md
se custom agents banana shuru karo.

**Migration tips:** SKILL.md patterns agents ke across export/import karo; ClawHub community skills ko
bridge ki tarah use karo; token spend weekly monitor karo. Tool sprawl se bacho — chaar-paanch core
tools pe cap rakho jab tak clients ke liye nahi bana rahe.

## Beyond the Core Fleet

Claude Code, Cowork, aur NanoClaw strong foundation hain, lekin 2026 ka agent landscape bohat diverse
hai. Open-source frameworks (Gemini CLI, Qwen Code, OpenAI Agents SDK, Claude Agent SDK) multi-agent
fleets power karte hain, often lower cost pe jab DeepSeek/Qwen models ke sath pair ho. No-code builders
(Vellum, Microsoft Copilot Studio, Zapier Central, Salesforce Agentforce) non-technical teams ko agents
deploy karne dete hain bina SDKs/terminals ke. Pure open-model fans ke liye: Llama, DeepSeek, Mistral,
ya Gemma par bane tools fully local/self-hosted options dete hain, zero cloud dependency.

*Last updated: March 2026*

---
[⬅ Fleet Economics & Trade-offs](01-fleet-economics-and-tradeoffs.md) · [Agla: Test Your Understanding ➡](03-test-your-understanding.md)
