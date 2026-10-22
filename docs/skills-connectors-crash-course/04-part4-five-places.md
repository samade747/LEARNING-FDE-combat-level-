# 04 — Part 4: Same Skill, Paanch Jagah

Ek baar likhi skill portable hai. December 2025 mein Anthropic ne **Agent Skills open standard**
publish ki (agentskills.io) — format jo multiple tools ko same `SKILL.md` parhne deta. Mahino
mein doosre vendors ke tools (OpenAI's Codex CLI, Google's Gemini CLI — **CLI** = command-line
tool, typing se chalta) wo files parhne lage. Honest caveat: basic `SKILL.md` travel karta, par
har product apna install path, call-karne-ka-tareeqa, permissions, extra features add karta.
**Recipe tumne likhi ek kitchen mein, par har kitchen apne shelves alag arrange karti.**

> Same month Linux Foundation ne **Agentic AI Foundation** banaya — neutral, cross-vendor
> governance ke liye. MCP (jispar connectors chalte) uske founding projects mein se ek hai —
> isliye "portable" ek safe bet hai, kisi ek company ka promise nahi.

| Jagah | Kiske liye | Skill install | App connect | Khud banana |
|---|---|---|---|---|
| Claude.ai (web/mobile) | Sab ke liye, main tool | Directory se Install, ya zip upload | "+"→Connectors→pick→sign in | skill-creator likhta, Save skill click |
| Cowork/OpenWork (desktop) | Knowledge workers, non-coders | Same directory, enabled skills khud dikhti | Same flow + computer ki files already | Describe karo, agent folder mein save kar deta |
| Claude Code/OpenCode (terminal) | Code ke sath kaam karne wale | Skill folder `skills` directory mein daalo | Config file mein ek baar setup | Agent se "create a skill for..." pucho |

Har pair mein pehla tool commercial, doosra open-source hai — dono same `SKILL.md` parhte.
Non-programmers ke liye honest guidance: **Claude.ai mein shuru karo aur raho.**

## ChatGPT Aur Gemini Ka Kya?

2 cheezein saath true hain, marketing in ko blur karti.

**Skills par** — picture genuinely cross-vendor hai. Agent Skills open standard hone ki wajah se
OpenAI/Google ke CLI tools (Codex CLI, Gemini CLI) same `SKILL.md` files parhte, VS Code aur
Cursor bhi. **Skill is course ka ek hissa hai jo Claude-locked nahi.**

**"Teach it once" consumer chat apps ke andar** — har vendor ka apna version hai, koi travel nahi
karta:

- **Custom GPTs** — ChatGPT ke saved assistants, GPT Store se distribute, **sirf ChatGPT ke andar**
- **Gems** — Gemini ke saved assistants, **sirf Google ke apps ke andar**

Farq jo matter karta: **portability.** Ek hi tool use karte ho to koi bhi fine hai. Multiple
models ke sath strategy ho (jaisa yeh book argue karti) to **Skills future-proof choice hain.**

**Connectors par** — teeno ka equivalent hai. ChatGPT connectors+apps se, Gemini Workspace
integration+extensions se. MCP technology increasingly shared ho rahi. Principle identical:
**permissions grant karo, AI inherit karta, read-only se start karo.**

> **Is course ke liye:** Claude.ai mein seekho. Teach-once, connect-your-apps, automatic firing,
> scoped access har tool mein transfer hoti. Jahan feature Claude-specific hai, bata diya gaya.
