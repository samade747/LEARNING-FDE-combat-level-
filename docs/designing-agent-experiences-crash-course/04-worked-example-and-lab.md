# 04 — Worked Example + Hands-On Lab + Projects

## Worked Example: Support Worker Ki 2 Surfaces

**Human surface:** Support lead console kholta hai. Default view: *"Refunded order #4021, $38,
confidence: high."* (Layer 1). Ek tap se plan dikhta hai. $38 Worker ki limit ke andar hai (autonomy
stop 3, act within limits). $900 chargeback dispute limit se upar hai, Worker rukta hai (stop 2,
in-the-loop). Har refund 24-ghante ka undo carry karta hai. 9 doosron ke sath chalte waqt, fleet view
$900 wala dispute surface karti hai, clean refunds log mein rehte hain.

**Machine surface:** Wahi Worker payment provider ke liye khud ek agent hai. Refund capability ek typed
MCP tool hai (**tools**), scoped revocable credential present karta hai (**access**), tool description
model ko batati hai kab refund valid hai (**context**), refund idempotent hai (**orchestration**). Yeh
sab human surface par kabhi nahi dikhta, lekin iske bina poora system collapse ho jata hai.

**Stakes barhein to:** Refunds ki jagah **vendor payments** — bheja hua paisa wapis nahi ata. Undo
safety net nahi rehta, design weight **recovery se prevention** ki taraf shift hota hai. Intent preview
mandatory ban jata hai. Autonomy dial "act within limits" se upar kabhi nahi jati, limit chhoti hoti hai,
bara payment hamesha in-the-loop. Safety surface zyada load uthati hai — dusra human approver optional
nahi rehta.

## Hands-On Lab: Apna Pehla MCP App Banao

**Step 1 — `create-mcp-app` skill install karo:**
```bash
npx skills add modelcontextprotocol/ext-apps
```

**Step 2 — 10-Minute Loop: Scaffold, Build, Serve:**
```text
Create an MCP App that displays a color picker
```
```bash
npm install && npm run build && npm run serve
```

**Step 3 — Render dekho:**
- **Option A (free):** Local test host — `ext-apps/examples/basic-host` clone karo, chalao
- **Option B:** Claude mein — Cloudflare tunnel se apna local server expose karo, custom connector add
  karo

**Step 4 — Jo bana usay parho.** Server par ek **tool** jiska metadata UI ki taraf point kare, aur ek
**resource** jo woh UI serve kare:
```typescript
const resourceUri = "ui://get-time/mcp-app.html";
registerAppTool(server, "get-time", {
  _meta: { ui: { resourceUri } },  // yehi line tool ko App banati hai
}, async () => ({ content: [{ type: "text", text: new Date().toISOString() }] }));
```

**Step 5 — Real Build: Refund Approval Card.**
```text
Using the create-mcp-app skill, build an MCP App called refund-approval.
Tool: review_refund(order_id, amount, confidence).
1. Show one plain line with word confidence (never color)
2. Approve/Escalate buttons, keyboard reachable
3. On Approve: 24h undo available
4. If amount > 50: disable Approve, only Escalate
5. approve_refund/undo_refund idempotent
```

**Design Pass Checklist:**
| Check | Concept |
| --- | --- |
| Fallback text decision carry karta hai? | 14 |
| Confidence word hai, color nahi? | 7, 5 |
| Approve → Undo ek click hai, 2x click safe hai? | 11, 13 |
| $900 refund card refuse karta hai, human route karta hai? | 8 |
| Keyboard se poori card reach hoti hai? | 5 |
| Tools action ke liye named hain? | 13 |

## Projects

1. **Ek agent audit karo** jo aap use karte ho — 11 anti-patterns ke against score karo
2. **Dial draw karo** — apne Worker ke 5 autonomy stops likho, kaunse hamesha in-the-loop
3. **Nudge budget design karo** — sirf woh events rakho jo real mein insan chahiye
4. **Machine surface likho** — apne Worker ki ek capability ko MCP tool ki tarah likho
5. **Fleet view design karo** — 5 Workers ek sath, kya glance mein dikhta hai
6. **Poora brief (capstone)** — 11-section Agent Experience Brief ek Digital FTE ke liye
7. **Widget ship karo** — Hands-On Lab Step 5 tak complete karo

---
[⬅ The New Craft](03-new-craft.md) · [⬆ Index](README.md)
