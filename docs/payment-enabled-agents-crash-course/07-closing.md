# 07 — Part 7: Closing (Concept 19) + Cheat Sheet + Template + References

## Concept 19 — Layered Composition Ki Discipline

**Ek line mein:** Yeh poora course ek kaam tak simplify hota hai: use case parho, usay 4 layers mein
tor do, aur har layer par sahi protocol chuno.

Is course ke 19 Concepts aur 5 Decisions sab ek claim ke liye scaffolding hain: **2026 mein agent
commerce ek single protocol nahi, ek layered architecture hai**, aur aapka kaam har layer ke liye sahi
protocol chunna hai apne saamne wale use case ke liye.

**Yehi shape 3 scales par dikhti hai:**

- **Protocol scale par:** 4 headline protocols alag problems alag layers par solve karte hain — ACP
  Layer 3, AP2 Layer 2, x402 aur MPP Layer 4. **Unhe same layer par rivals treat karna sabse common
  architectural mistake hai.** Woh sirf wahan compete karte hain jahan unki layers overlap karti hain
- **System scale par:** production system har layer se ek protocol rakhta hai, OpenAI Agents SDK ke
  through wired universal client ki tarah. SDK khud protocol nahi hai — **orchestrator hai jo protocols
  ko cleanly compose karne deta hai**
- **Discipline scale par:** aapka kaam use case parhna, 4 layers mein todna, har ek par sahi protocol
  chunna, aur har choice ko use case ke real constraints ke against justify karna hai (transaction
  value, latency budget, dispute model, audit requirements). **Kaam "favorite protocol chuno" nahi
  hai. "Is use case ke liye, har layer kya demand karta hai" hai.**

**5 Decisions ki summary:** Decision 1 (consumer shopping) ACP + Stripe card rails par utri, kyunki
chargeback protection chahiye thi. Decision 2 (API-paying agent) x402-only par utri, kyunki machine-to-
machine ke liye Layers 2+4 collapse hoti hain. Decision 3 (enterprise procurement) sabse complex
composition (AP2 + ACP + MPP) tak pahunchi, audit aur recurrence needs ki wajah se. Decision 4
(multi-agent marketplace) AP2 + ERC-8004 + x402 par utri, bilateral-trust ki zaroorat kisi aur tareeqe
se poori nahi ho sakti thi. Decision 5 ne Decision 2 ko bilkul alag stack (Google ADK + Coinbase +
AP2 + x402) par rebuild kiya, wahi 4-layer shape mili — **prove karta hai architecture Stripe aur
OpenAI ka wrapper nahi hai.**

**Composition jo aap chunte ho use case se set hoti hai, taste se nahi.** Team jo "stablecoins future
hain" ki wajah se x402 chunti hai jabke consumer shopping experience bana rahi hai — galat composition
hai. Team jo "Stripe enterprise-grade hai" ki wajah se ACP chunti hai jabke $0.001/call API access ke
liye pay kar rahi hai — galat composition hai. **Use case ko choice drive karne do.**

**Protocols badalte rahenge.** Naye launch honge, aaj ke leaders zameen khoyenge, governance haath
badlegi. **Discipline sab se zyada zinda rehti hai:** 4 layers stable hain, aur use case ko unme parhna
woh skill hai jo agle 24 mahino mein jo bhi protocols jeetein unse survive karti hai.

## Cheat Sheet — Framework Ek Page Mein

**4 layers (yaad rakho):**
```
Layer 1: DISCOVERY      → "Kya khareedne ke liye available hai?"
Layer 2: AUTHORIZATION  → "Kya main yeh spend karne ka allowed hoon?"
Layer 3: COMMERCE       → "Poori purchase lifecycle kya hai?"
Layer 4: SETTLEMENT     → "Paisa asal mein kahan move hota hai?"
```

**Har layer par top picks (2026):**

| Layer | Top Picks | Kis Se Chuno |
| --- | --- | --- |
| Discovery | MCP, A2A, agent directories, AI shopping surfaces | Agent ki services asal mein kahan rehti hain |
| Authorization | AP2 mandates, ACP SPT, TAP, ERC-8004 | Trust model: audit-rigorous, Stripe-native, identity-only, ya multi-agent |
| Commerce | ACP, UCP, direct API (none) | Kya use case ko commerce lifecycle chahiye? |
| Settlement | x402, MPP, card rails, bank/Lightning | Economics: transaction value rail decide karti hai |

**4 canonical compositions:**

| Use Case | Stack |
| --- | --- |
| Consumer shopping | AI surface + ACP SPT + ACP + Stripe cards |
| API-paying agent | MCP/directory + EIP-3009 + (none) + x402 |
| Enterprise procurement | A2A/MCP + AP2 + ACP/UCP + MPP/cards |
| Multi-agent marketplace | A2A + AP2 + ERC-8004 + (none) + x402 |

**Spend-limit enforcement, 3 levels (required):**
```
Level 1: Wallet/payment-method limits  (smart-contract caps YA Stripe customer caps)
Level 2: SDK tool guardrails           (tool_input_guardrail har payment tool par)
Level 3: Application business logic    (per-user, per-category, per-merchant policies)
```

**Economic threshold:**
```
Transaction value
├── < $5         → x402 ya MPP stablecoin (card fees transaction se zyada)
├── $5-$1,000    → ACP + card rails (chargeback protection worth hai)
└── > $1,000     → AP2 + composed stack
```

**Dispute model (often sabse strong constraint):**
```
Chargeback protection chahiye?  Yes → ACP + card rails      No → x402 acceptable
Audit evidence chahiye?         Yes → AP2 Layer 2            No → SPT/EIP-3009 kaafi
```

**Production Checklist:**
- [ ] Wallet/payment-method spend limits Level 1 par configured
- [ ] SDK `tool_input_guardrail` har payment-authorizing tool par (Level 2)
- [ ] Application per-user/per-category/per-merchant caps enforce kare (Level 3)
- [ ] Signing keys key vault mein, kabhi env vars mein nahi
- [ ] Per-agent wallet separation
- [ ] Key rotation schedule (90-day baseline)
- [ ] Audit logs durable storage mein, agent runtime se independent
- [ ] OpenTelemetry traces SDK/httpx/Inngest/FastAPI ke across span karein, ek trace ID per transaction
- [ ] Pydantic models har boundary par; `Decimal` money ke liye hamesha
- [ ] Stripe webhook handler signature verify kare, Inngest event fire kare (thin handler)
- [ ] AP2 mandate-signed callback signature verify kare, `step.wait_for_event` resume kare
- [ ] x402 seller-side middleware configured (paid APIs expose karte ho to)
- [ ] Inngest `idempotency` key har webhook-triggered function par
- [ ] Dispute/refund mechanism har protocol ke liye documented
- [ ] Human-in-the-loop confirmation gate pehle 30 din production ke
- [ ] Cart-accuracy metric measured confirmation gate relax karne se pehle

## Design-Review Template (Chunay Hue Sawal)

**Architecture:** Kaunsa use case serve ho raha hai? 4 layers explicitly walk karo — kaunsa protocol
kis layer par? Har layer ka choice use case ke against justify karo. Kisi layer par protocol overlap
hai?

**Economic:** Transaction value distribution kya hai? Latency budget kya hai? Expected volume par cost
per transaction kya hai?

**Operational:** Sab 3 levels par spend-limit enforcement? Identity hygiene (wallet separation, key
rotation, audit logs, traces)? Dispute/refund mechanics use case ke actual disputes handle karte hain?
Operational envelope (Inngest) long-running flows handle karta hai? Human-in-the-loop gates?

**Webhook/async-callback:** Stripe webhook handler thin hai? AP2 signing callback signatures verify
karta hai? x402 seller-side middleware configured hai? Inngest idempotency keys har jagah? Pydantic
models har boundary par?

**Failure-mode:** Sabse likely production failure mode kya hai? Mitigation kya hai?

**Track-readiness:** Team kaunse learning track se operate kar rahi hai? Agent misbehave kare to
rollback plan kya hai (wallet kill switch? SPT revocation?)?

## References (Chunay Hue)

- **ACP:** `github.com/agentic-commerce-protocol/agentic-commerce-protocol`, `agenticcommerce.dev`
  (OpenAI + Stripe)
- **AP2:** `github.com/google-agentic-commerce/AP2`, `ap2-protocol.org` (Google + 60+ partners)
- **x402:** `github.com/coinbase/x402`, `x402.gitbook.io`, `x402.org` (Coinbase, ab Linux Foundation)
- **MPP:** `mpp.dev` (Stripe + Tempo, launch March 18, 2026)
- **Adjacent:** A2A (`github.com/google-a2a/A2A`), MCP (`modelcontextprotocol.io`), UCP (Google), TAP
  (Visa + Cloudflare), ERC-8004
- **OpenAI Agents SDK:** `pip install openai-agents`, `openai.github.io/openai-agents-python`
- [Build AI Agents](../build-agents-crash-course/README.md), [Production Worker with Nervous System](../ai-agent-nervous-system-crash-course/README.md), [Eval-Driven Development](../eval-driven-development-crash-course/README.md), [Choosing Agentic Architectures](../choosing-agentic-architectures-crash-course/README.md)

---

*"Aapke paas ab poora framework hai: 4 layers, 4 protocols, unhe compose karne ke rules, 5 worked
decisions, production concerns jo decide karte hain system survive karta hai ya nahi. Protocols badalte
rahenge. 4-layer discipline nahi badlegi. Layers se banao, aur jab protocol naam badlein tab bhi sahi
rahoge."*

---
[⬅ Production Concerns](06-production-concerns.md) · [⬆ Index](README.md)
