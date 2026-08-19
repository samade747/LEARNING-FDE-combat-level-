# Agent Factory System of Record — Summary

Sabse chota lekin sabse foundational chapter — khud woh cheez jis par Ecosystem Concept aur FDE AF Model poori theory khadi karte hain. Sabse zaroori line: **Grounded, guessing nahi.** Jab source unreachable ho, yeh **fail closed** hota hai — "nahi bata sakta" kehta hai, kuch banata nahi.

## Chapter Overview
- Book ko chunk, embed, aur MCP ke zariye serve kar diya gaya hai — koi bhi AI agent/worker (Claude, ChatGPT, Claude Code, Cowork, ya custom SDK agent) connect ho kar grounded jawab pa sakta hai. Yehi source Zia Tutor AI aur Zia Developer AI khud parhte hain.
- FDE AF Model ki zabaan mein: yeh **Layer 1 ka pehla instance** hai — SoR kernel. **Ek component, kai corpora** — aage har vertical ka corpus (accounting standards, clinical protocols, regulations) isi component se serve hoga.

## 00 — Connect Karo: Steps Aur Design Ke Peeche Ki Soch
- **4 design properties** jo isay "search over docs" se alag banate hain: (1) koi bhi MCP-speaking agent/host connect ho sakta hai; (2) **grounded, guessing nahi** — exact section cite karta hai, fail closed jab source unreachable; (3) book ke saath **live rehta hai** — naya version publish hote hi record dobara parh leta hai, drift nahi hota; (4) book ka apna stack (Postgres+pgvector, read-only MCP tools) — "humne ise usi method se banaya jo hum sikhate hain."
- **Connect kaise karein (claude.ai Custom Connector), Beta 1:** Connectors → Add custom connector → Name: `Agent Factory System of Record`, MCP Server URL: `https://sor.panaversity.org/mcp` → Advanced settings mein OAuth Client ID: `zia-tutor-ai` (Client Secret khaali chhodo) → Add → Connect → access approve → test karo: *"Use the Agent Factory System of Record and explain what AI actually is."* Yeh **read-only** hai, core content serve karta hai (About se Glossary tak, ~80% value path).
- FDE AF Model mein fit: Layer 1 ka pehla live instance — apni content ke saath isi component ko run karke apna khud ka governed SoR (Accounting/Core Banking SoR) ban sakta hai; poora method [Designing the Vertical System of Record] mein hai.
