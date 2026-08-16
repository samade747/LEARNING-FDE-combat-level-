# 00 — Overview: 4 Invariants, Server Kya Hai

## Server Aur MCP Server

**Server** ek computer hai jo hamesha ek fixed address par on rehta hai, doosre computers ke sawal ka
intezar karta hai aur jawab deta hai. Har phone app kisi na kisi server se baat kar rahi hai. Ek shop
ka front counter socho: hamesha khula, khud kuch nahi karta, lekin customer ke ate hi ek kaam karta hai
aur result wapis deta hai — yehi aapka server hai.

**MCP server** ek khaas kism ka server hai jo **MCP** follow karta hai — ek shared standard (AI ke liye
USB port jaisa, ek plug jo har assistant mein fit ho) taake koi bhi AI koi custom wiring ke bina isay
use kar sake.

## 4 Non-Negotiables

Poora course inhi 4 cheezon ka build hai:

1. **Ek gateway.** AI aapse ek hi connector par milta hai, tools naam se grouped uske peeche. (Free
   account sirf **ek** custom connector add kar sakta hai — yeh limit hai, preference nahi.)
2. **Sirf Tools.** Aap AI se sirf **tools** ke zariye baat karte ho — functions jo model apni reasoning
   ke beech mein call kar sakta hai — resources ya prompts ke zariye nahi jo insan ko haath se pick karna
   parte.
3. **Prove karo, trust mat karo.** Aapka customer ek aisa dimagh hai jo bina bad-niyati ke bhi ghalat
   person ki identity de sakta hai. Identity hamesha ek verified sign-in se aati hai, AI ke bataye kuch
   se nahi — waisa hi jaise hotel desk aapka mail passport dekh kar deta hai, kisi ki baat par nahi.
4. **Fail closed.** Jab server missing ya broken ho, AI chup nahi hota — woh **improvise** karta hai,
   jawab bana leta hai, person ka saved data khud invent kar leta hai. Aapke server ko usay rokna hai
   aur saaf kehna hai — jaise ATM jo bank tak na pahunche to "temporarily unavailable" dikhata hai, balance
   guess kar ke cash nahi de deta.

Do invariants **shape** describe karte hain (ek gateway, sirf tools). Doosre do **jobs hain jo server ko
karni hain kyunki AI trust nahi kiya ja sakta** (identity prove karna, fail closed).

## Prerequisites

1. Typed Python parh sakte ho ([Python in the AI Era](../python-crash-course/README.md))
2. [Agentic Coding Crash Course](../agentic-coding/README.md) kar chuke ho
3. Bahar se ek connector use kar chuke ho (Skills & Connectors course)
4. **Build AI Agents pehle zaroori nahi** — yahan aap agent nahi, wahi server banate ho jise agent call
   karta hai

## Kaise Banate Ho: Plan → Review → Execute → Verify

Aap yeh server **haath se nahi likhte.** Har Manufacturing-track course ki tarah: **aapka coding agent
code likhta hai; aapka kaam spec dena aur output verify karna hai.** Plan karo, review karo, chalao,
check karo.

**Base download karo:** `connector-native-apps-base.zip` — ismein `auth.py` aur `session.py` **GIVEN**
(complete) hain, kabhi rewrite nahi karte, sirf parhte/wire karte ho. Baqi sab (`server.py`, `db.py`,
`config_store.py`) aap concept-by-concept apne agent ke sath banate ho.

**Do tracks:** **Beginner track** bundled `mock_auth/` use karta hai — local sign-in, koi account nahi
chahiye. **Standard track** real hosted sign-in service use karta hai (AI Identity course mein sikhoge).
Pehle Beginner track par poora build karo, phir `.env` ki 3 values badal kar switch karo.

---
[⬆ Index](README.md) · [Agla: The Shape ➡](01-the-shape.md)
