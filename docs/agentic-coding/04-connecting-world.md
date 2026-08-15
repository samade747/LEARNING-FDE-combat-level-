# 04 — Connecting to the World: MCP

## Concept 12: MCP, Honestly

Ab tak AI aapke computer ke **ek folder** tak mehdood tha. Real kaam wahan nahi hota — order status
database mein hai, bug ticketing system mein hai. **MCP (Model Context Protocol)** AI ko in services se
connect karta hai — Slack, Google Docs, Notion, GitHub, databases.

**"Kya ye sirf ek API nahi hai?"** Almost. MCP APIs ke upar ek **standard wrapper** hai — glue code
(auth, request shaping) pehle se ho chuka hota hai. Asal sawal kabhi "MCP ya API" nahi hota — **"kya ye
standing connection ke qabil hai, ya agent seedha call kar sakta hai?"**

**Setup:**
- **Claude Code:** `claude mcp add --transport http <name> <url>` (ya `--scope project` shareable
  `.mcp.json` ke liye). `/mcp` se status check
- **OpenCode:** `opencode.json` mein `mcp` block, `"type": "remote"` ya `"local"`

**Zaroori use case: system of record connect karna.** System of record wo authoritative jagah hai jahan
data ki truth rehti hai — database, CRM, ticketing system. MCP agent ko **live, authoritative data** se
jodta hai, stale paste se nahi. *"Order 4471 ka status kya hai?"* — agent asal database query karta hai.

**Ehtiyat: sab kuch connect mat karo.** Har MCP connection conversation mein space leti hai, chahe use
na ho. GitHub MCP server bohat tokens add karta hai. **Claude Code** tool definitions ko defer karta hai
(sirf use hone pe load), **OpenCode** upfront load karta hai — isliye OpenCode pe zyada selective raho.

**Kab MCP use karo, kab skip karo:**
- **Use karo:** service ko login/connected rehna zaroori ho (Calendar, database with password)
- **Skip karo:** AI simple terminal command se wahi result de sake (`gh issue list` vs GitHub MCP)

**1-2 connections se shuru karo jo waqai chahiye — 10 nahi jo available hain.**

## Ek Zaroori Safety Habit: Context Darwaza Hai

**Model jo bhi parhta hai, wo usay steer kar sakta hai — chahe likha kisi ne bhi ho.** Fetched web page,
GitHub issue, tool description — model ke liye ye sab **same tarah ka text** hai. Window sab kuch ek
stream mein flatten kar deta hai. Isay **prompt injection** kehte hain.

**3 aadatein jo zyada tar risk band karti hain:**
- **Fetched content sirf inform karti hai. Sirf aapki apni files instruct karti hain** — kisi ajnabi ka
  text kabhi rules file ya skill mein paste mat karo
- **Kisi bhi cheez ko poori tarah trust na karo to subagent se parhwao** (Concept 11) — planted line
  us disposable window mein hi reh jati hai, kabhi aapki conversation mein nahi ati
- **Jab AI ka behavior kuch parhne ke turant baad ajeeb ho jaye, us cheez pe shak karo**

> **Honest limit:** Ye aadatein exposure kam karti hain, lekin fooled model ko namumkin nahi banatin —
> text text hai. Rules jinse AI ko talk out nahi kiya ja sakta, aur fences jo limit karein AI kya reach
> kar sakta hai — ye alag engineering hai, **Harness Engineering course** deewarein banati hai.

> **Ek line mein:** **Trust har piece of context ki property hai, aur low-trust text ko kabhi standing
> surface nahi milni chahiye.**

---
[⬅ Personalizing](03-personalizing.md) · [Agla: Complete Worked Example ➡](05-worked-example.md)
