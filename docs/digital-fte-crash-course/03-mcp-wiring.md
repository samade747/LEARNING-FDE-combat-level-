# 03 — Part 3: MCP — Agent Ko System of Record Se Wire Karna (Concepts 11-15)

Part 1 ne Skills library di. Part 2 ne Postgres system of record diya. **Part 3 dono ko Model Context
Protocol se jodta hai** — open standard agent ke external state aur capability tak pahunchne ka.

## Concept 11 — MCP Kya Hai, Aur Kya Nahi

**Model Context Protocol** ek open client/server protocol hai. "USB-C for AI tools" — ek protocol, kai
implementations.

**3 Primitives:**
1. **Tools** — functions jo model invoke kar sakta hai (sabse zyada use hota hai)
2. **Resources** — read-only data jo agent fetch kar sakta hai
3. **Prompts** — reusable templates jo server deta hai (kam use hota hai)

**3 Transports:**

| Transport | Kab | Status |
| --- | --- | --- |
| `stdio` | Local subprocess | Mature, local tools default |
| `Streamable HTTP` | Remote server | **Naye remote work ke liye recommended** |
| `SSE` | Purana remote | Legacy |

**Stateless vs Stateful HTTP:** Stateless (default) — har call independent, load balancer ke peeche
scale hota hai. Stateful — live session khula rehta hai (streaming ke liye chahiye), lekin ek server
instance se bandha rehta hai.

**MCP kya NAHI hai:**
- **Framework nahi** — protocol hai
- **Service nahi** — koi "MCP cloud" nahi, yeh programs hain jo chalte hain
- **Security boundary nahi** — MCP transport/protocol define karta hai, server khud decide karta hai
  kya expose karna hai
- **`@function_tool` ka replacement nahi** — dono ki jagah hai

## Concept 12 — Neon MCP Server: Development Plane, Runtime Nahi

Neon MCP server Neon ki **management** API expose karta hai — **development tool hai, production nahi.**
Neon ke apne docs saaf kehte hain: *"Never connect MCP agents to production databases."*

**Wajah:** `run_sql` tool koi bhi SQL chala deta hai jo model likhe. Build karte waqt yeh poora point hai.
Live database par point karo to yeh ek **door** ban jata hai — koi bhi jo Worker mein instructions
smuggle kar sake (customer ka clever message) poora database parh sakta hai.

**Development mein use karo:** schema/migrations, apna data explore karna, connection strings dhoondna.

**Finished Worker ko chahiye:** customer orders lookup, refund policy check, refund issue karna, audit
row likhna — **in sab ke liye alag tareeqa** — ya toh **custom MCP server** (Concept 14) ya direct
connection. Live Worker ko kabhi `run_sql`-style tool nahi milna chahiye.

## Concept 13 — MCP Ko Agents SDK Se Connect Karna

SDK ka built-in MCP client — local (stdio), remote (streamable HTTP), legacy (SSE). Aap connection
kholte ho, agent ko dete ho, SDK baaki karta hai: server se poochta hai tools kya hain, model ke
saamne `@function_tool`s ke sath rakh deta hai. **Model MCP tool aur local function tool mein farq nahi
kar sakta — yehi poora point hai.**

**4 zaroori cheezein:**
- **Connection clean kholo, clean band karo**
- **Production mein tool list cache karo** — default har run par "kya tools hain" dobara poochta hai
- **Servers stack hote hain** — ek agent ko kai MCP servers de sakte ho
- **Dangerous tools ko approval ke peeche gate karo**

## Concept 14 — Custom MCP Servers: Kab Apna Banao

Neon MCP server **generic** hai — development ke liye strength, runtime ke liye weakness. **Custom MCP
server ulta karta hai:** narrow surface, koi general `run_sql` nahi, sirf specific operations jo Worker
ko chahiye.

**Decision Table:**

| Aap Kya Expose Karna Chahte Ho | Use Karo | Kyun |
| --- | --- | --- |
| Ek function, ek agent | `@function_tool` | Protocol overhead ki zaroorat nahi |
| Kai functions agent code se tightly coupled | `@function_tool` | Same repo mein rehte hain |
| Kai agents/deployments use karenge | Custom MCP server | Protocol hi reusability deta hai |
| Agent process se lamba chalna chahiye | Custom MCP server | Long-running connections |
| Vendor-provided (Neon, GitHub) | Vendor ka MCP server | Jo ban chuka usay dobara mat banao |
| Sensitive operations, narrow scope chahiye | Custom MCP server | Exact tools define karo, kuch aur nahi |

**Custom server kya deta hai jo `@function_tool` nahi deta:**
1. **Process isolation** — server crash agent crash nahi karta
2. **Scope** — sirf jo tools define kiye, kuch aur nahi (`run_sql` nahi)
3. **Reusability** — doosra agent same server use kar sakta hai

**Trade-off real hai:** Custom MCP server operational complexity add karta hai — ek aur process, logs,
network hop. **Ek server tab banao jab reuse hona ho, scoping matter kare, ya isolation safety de.**

**Rule:** MCP ki value uske banaye boundary ki value ke sath barhti hai. Jo boundary chahiye nahi, woh
overhead hai.

## Concept 15 — MCP Under Load

Ek agent, ek server wala demo kaam karta hai. Real traffic 3 pressures add karta hai:

1. **Agent aur server ke beech ka wire** — local subprocess ek machine ke liye theek hai; ek se zyada
   agents share karein ya server apni hardware par jaye, to remote transport (streamable HTTP) par
   switch karo
2. **Setup cost baar baar mat do** — server boot par ek dafa connect karo, tool list cache karo, database
   connections ka pool rakho
3. **Har cheez par ceiling lagao, trace ko poora rakho** — steps cap karo, retries limited rakho,
   rate-limit karo, MCP boundary ke paar trace follow kare

---
[⬅ System of Record](02-system-of-record.md) · [⬆ Index](README.md) · [Agla: Worked Example ➡](04-worked-example.md)
