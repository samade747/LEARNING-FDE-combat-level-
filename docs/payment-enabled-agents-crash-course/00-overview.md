# 00 — Overview: 4 Protocols, 4 Layers

## Ek Idea, Poora Course

Yeh course un 4 protocols par hai jo OpenAI Agents SDK systems ko paisa spend karne dete hain:
merchants par, APIs ke against, doosre agents ke sath, poori open economy mein. **19 concepts, 5
worked decisions, 4 learning tracks.**

**Poora course jispar khara hai:** **4 protocols rivals nahi hain. Layers hain.** Zyada tar articles
poochte hain "ACP ya x402?" — yeh sawal galat hai. 2026 ki real system ek sath kai use karti hai,
kyunki har ek same problem ki alag layer solve karta hai. API-paying agent x402 se settle karta hai
aur kuch aur chahiye nahi; shopping agent ko checkout run karne ke liye ACP chahiye **aur** paisa move
karne ke liye card rails. **Aapka kaam use case parhna hai aur har layer par sahi protocol stack
karna hai.**

## 4 Headline Protocols

- **ACP (Agentic Commerce Protocol)** — consumer-shopping protocol, OpenAI aur Stripe ne banaya. Agent
  ka real merchant par checkout complete karna. ChatGPT Instant Checkout power karta hai. Commerce
  layer mein rehta hai
- **AP2 (Agent Payments Protocol)** — authorization protocol, Google + 60 partners. Signed "mandates"
  produce karta hai jo prove karte hain human ne agent ko spend karne diya. Khud paisa move nahi karta
- **x402** — HTTP-native settlement protocol, Coinbase ne banaya, ab Linux Foundation govern karta hai.
  Unused HTTP 402 "Payment Required" status code revive karta hai — agent API call ke liye 1-2
  seconds mein stablecoin se pay kar sakta hai
- **MPP (Machine Payments Protocol)** — Stripe aur Tempo ka settlement protocol. Trick "session" hai:
  agent spending cap pre-approve karta hai, phir uske against kai chote payments stream karta hai.
  Multi-rail (stablecoin, Lightning, cards)

## 4 Layers, Poore Course Ki Spine

1. **Discovery layer** — agent kya khareed sakta hai dhoondta hai (MCP, A2A, agent directories, AI
   shopping surfaces)
2. **Authorization layer** — paisa move hone se pehle 2 cheezein prove hoti hain: human ne allow kiya,
   aur agent woh hi hai jo claim karta hai (AP2 Mandates, ACP SPT, TAP, ERC-8004)
3. **Commerce layer** — poori purchase lifecycle chalati hai: cart, checkout, fulfillment, dispute,
   refund (ACP, UCP; plain API calls isay poori tarah skip karte hain)
4. **Settlement layer** — jahan paisa asal mein hath badalta hai (x402, MPP, card rails, bank
   transfer/Lightning)

**Har use case sab 4 layers touch karta hai, lekin har ek alag protocol compose karta hai har layer
par, kuch layer poori tarah skip karte hain.** Consumer shopping agent poora stack chalata hai: MCP
discovery, ACP token authorization, ACP commerce, card rails settlement. API-paying agent commerce
poori tarah skip karta hai, discovery + x402 settlement tak collapse ho jata hai.

## 4 Learning Tracks

| Track | Waqt | Kya Karte Ho |
| --- | --- | --- |
| **Reader** | 2-3 ghante | Sab Concepts/Decisions parho, code chalana skip karo |
| **Beginner** | ~1 din | Reader + x402 client examples chalao + 1 ACP test transaction (Stripe test mode) |
| **Intermediate** | 2-3 din | Beginner + agent banao jo ACP ek transaction ke liye aur x402 doosre ke liye use kare, AP2 Intent Mandate checks wire karo |
| **Advanced** | 4-5 din | Intermediate + poora composed system Inngest envelope mein durably chalao, spend limits + human-approval gates wire karo, trace/cost/dispute metrics measure karo, ek poora refund cycle handle karo |

**Self-check:** *"Mere use case ke liye, sabse chota protocol composition kaunsa value ship karta
hai?"* Part 4 ke baad iska jawab de sako to track sirf itna sawal hai ke aap "smallest composition" se
"production-grade composition" tak kitna aage jana chahte ho.

## Vocabulary Snapshot

- **Mandate (AP2)** — signed digital proof human ne specific spending authorize ki. 3 hain: Intent
  ("shoes under $120"), Cart ("yeh exact items"), Payment ("yeh exact payment authorize karo")
- **SPT (Shared Payment Token, ACP)** — payment processor (Stripe) se one-time token, ek merchant, ek
  amount cap, ek short time window tak locked
- **Stablecoin/USDC** — dollar-pegged cryptocurrency, agents "$0.05 payment" ko 5 cents ki tarah rakhte
  hain sending aur settling ke darmiyan
- **HTTP 402 Payment Required** — 1997 se reserved status code, x402 ne revive kiya
- **Facilitator (x402)** — optional third party jo signature check karke on-chain payment submit karti
  hai, merchant ko apni blockchain plumbing nahi chalani parti
- **Merchant of Record (MoR)** — business jo transaction ke liye legally responsible hai. ACP mein
  merchant hi MoR rehta hai; plain machine-to-machine x402 calls mein often koi MoR nahi hota
- **`tool_input_guardrail`** — SDK guardrail jo tool execute hone se **pehle** chalta hai aur call
  reject kar sakta hai — payment rokne ka SDK-native tareeqa. Poore course ki spine (7 payment tools
  mein appear hota hai)

---
[⬆ Index](README.md) · [Agla: Kyun Naye Protocols Chahiye ➡](01-why-new-protocols.md)
