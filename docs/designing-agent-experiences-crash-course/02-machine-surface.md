# 02 — Part 3: Machine Surface — Agents Ke Liye Design (Concepts 13-14)

## Concept 13 — Agent Experience (AX): Aapke Product Ke Robot Users Hain

Aapka product **agents** bhi use karte hain — aapke users ki taraf se act karne wale, aur aapke apne
workforce ke doosre Workers. Woh aapka careful layout nahi dekhte. **Woh structure parhte hain.**
Structure hostile ho to insan ka agent chupke se fail hota hai.

**4 cheezein decide karti hain agent aapke product ke sath kaamyab ho sakta hai ya nahi:**
- **Access** — kya agent prove kar sakta hai kiski authority ke under act kar raha hai (scoped, revocable
  credential)?
- **Context** — model asal mein samajh sakta hai aapka product kya karta hai?
- **Tools** — kya capabilities machine-readable, typed, discoverable hain?
- **Orchestration** — agents safely chain kar sakte hain (predictable contracts, idempotent actions)?

**Payoff:** Achha connector ya MCP server hi **achi AX hai.** `SKILL.md` jo agent ko sikhaye, MCP tool
jiski clear typed signature ho — yeh aapke product ki UX hai uske robot users ke liye.

**Machine surface jise agent trust kar sake:**
- **Tools ko action ke liye naam do**: `refund_order`, "process" nahi
- **Schemas narrow, typed, validated rakho**
- **Side effects aur khatra declare karo** — jo tools duniya badalte hain unhe mark karo
- **Structured, actionable errors return karo** — sirf code nahi, agla kya karna hai (retryable? `retry_after`?)
- **Actions idempotent banao** jahan mumkin ho
- **Provenance aur permission carry karo**
- **Agent ke liye docs likho** — examples, limits, failure modes
- **Contract test karo, sirf screen nahi**

> **MCP kya deta hai, kya nahi:** MCP standardize karta hai discovery, calling, authentication.
> Jaan-boojh kar 3 cheezein aapke liye chhodta hai: **orchestration**, **governance**, **state**.
> Protocol agent ko darwaze tak leta hai; andar kya kare (aur kaun dekh raha hai) abhi bhi aapka design
> hai.

## Concept 14 — Generative UI: Agents Jo Interfaces Wapis Dete Hain

**MCP Apps** ke sath, tool sirf text return nahi karta — normal text result (fallback) **aur** ek
interactive `ui://` resource (`_meta.ui.resourceUri` mein naam) bhi de sakta hai jo host support karne
par render hota hai, sandboxed iframe mein.

> **Ek line mein positioning:** MCP machine surface hai. MCP Apps interactive human surface hai. Milkar
> ek tool dono users (insan aur agent) ki khidmat karta hai.

**MCP Apps** — MCP ka pehla official UI extension, November 2025 mein propose hua, July 2026 spec mein
finalize hua. Claude, VS Code, Goose, Postman render karte hain.

**4 properties jo MCP App ko box mein web page se zyada banati hain:**
- **Context rakhta hai** — app conversation ke andar rehta hai
- **Dono taraf baat karta hai** — widget server ke tools call kar sakti hai
- **Host ki powers consent se borrow karta hai**
- **Safe by construction** — sandbox app ko host page se roke rakhta hai

**Widget kab jagah kamata hai:** complex data explore karna, kai options ek sath configure karna, rich
media, real-time monitoring, multi-step workflows. **Counter-rule:** agar plain text jawab kaafi hai,
text return karo. Widget ko jagah kamani parti hai, jaise nudge interruption kamati hai (Concept 10).

**Discipline jo aapko portable rakhti hai: progressive enhancement** — pehle open standard par banao,
phir jahan ek host extras de, feature-detect karo aur baaki jagah gracefully degrade karo.

---
[⬅ Human Surface](01-human-surface.md) · [⬆ Index](README.md) · [Agla: The New Craft ➡](03-new-craft.md)
