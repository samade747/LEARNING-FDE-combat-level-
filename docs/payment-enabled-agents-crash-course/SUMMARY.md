# Payment-Enabled Agents — Summary

Mode 2's aakhri chapter (9/9). 4 protocols (ACP, AP2, x402, MPP) jo OpenAI Agents SDK systems ko paisa
spend karne dete hain — **rivals nahi, layers hain**. Core discipline: use case parho, 4 layers mein tor
do, har layer par sahi protocol stack karo. 19 concepts, 5 worked decisions, 4 learning tracks.

## 00 — Overview: 4 Protocols, 4 Layers

- **4 headline protocols:** ACP (OpenAI+Stripe, consumer checkout, ChatGPT Instant Checkout), AP2 (Google+
  60 partners, signed mandates, paisa khud move nahi karta), x402 (Coinbase→Linux Foundation, HTTP 402
  revive, stablecoin, 1-2 sec), MPP (Stripe+Tempo, prepaid-session settlement, multi-rail).
- **4 layers:** Discovery (kya khareed sakta hai — MCP/A2A/directories) → Authorization (allowed hoon? —
  AP2/ACP SPT/TAP/ERC-8004) → Commerce (poori purchase lifecycle — ACP/UCP/none) → Settlement (paisa
  kahan move — x402/MPP/card rails). Har use case sab 4 touch karta hai, alag protocol har layer par,
  kuch layers poori skip.
- **4 Learning Tracks:** Reader (2-3h, read-only) → Beginner (~1 din, +x402/ACP test txn) → Intermediate
  (2-3 din, +compose ACP+x402+AP2) → Advanced (4-5 din, +Inngest durable system, spend limits, dispute cycle).
- Vocabulary: Mandate (AP2 — Intent/Cart/Payment), SPT (ACP one-time token), Stablecoin/USDC, HTTP 402,
  Facilitator (x402), Merchant of Record (MoR), `tool_input_guardrail` (course ki spine — payment-blocking
  SDK-native mechanism).

## 01 — Part 1: Naye Protocols Kyun Chahiye (Concepts 1-3)

- **Concept 1 — Assumption jo tuti:** Payment systems assume karte human "buy" click kar raha hai. 3
  breaks: no email/account (agents ke paas nahi), high-frequency (1000 calls/min = attack jaisa dikhta
  hai), no phone for disputes (agent jawab nahi de sakta). Fix table: cryptographic identity/scoped tokens,
  HTTP-native/pre-authorized sessions, mandate-based non-repudiable audit trail.
- **Concept 2 — Ek protocol kyun jeet nahi sakta:** 4 layers, 4 alag incumbents (search/OAuth/Stripe-
  Shopify/Visa-crypto), har naya protocol wahi ek layer li jahan sponsor ka leverage tha (ACP↔Commerce,
  AP2↔Authorization, x402/MPP↔Settlement). **Core rule: ek layer ke andar ek protocol, layers ke across
  kai compose.**
- **Concept 3 — SDK bataur universal client:** Har protocol ek `@function_tool` ban jata hai, framework
  single client hai (Agent+Runner.run). 3 zaroori cheezein: typed Pydantic return values, `context=`
  param (per-run/per-user state), `tool_input_guardrail` (payment ko **hone se pehle** rokna — `output_
  guardrail` bohat late fire hota hai, payment ho chuka hota hai).

## 02 — Part 2: The Four Layers In Depth (Concepts 4-7)

- **Concept 4 (Discovery):** MCP (developer-wired, dominant), A2A (multi-agent), agent directories
  (runtime-discovered), AI shopping surfaces (consumer). Mutually exclusive nahi — real agent kai use
  karta hai.
- **Concept 5 (Authorization):** AP2 Mandates (audit-heavy), ACP SPT (Stripe-native consumer), TAP
  (identity-only, add-on), ERC-8004 (on-chain reputation, no-prior-trust). 2 sawal: human authorized? +
  agent-woh-hi-hai? `tool_input_guardrail` code example (`block_over_user_cap`) — payment safety ke liye
  yehi guardrail type chahiye, sabse common mistake output guardrail use karna hai.
- **Concept 6 (Commerce):** ACP vs UCP compete karte hain; "direct API" iss layer ki **absence** hai, 3rd
  competitor nahi. Sabse underestimate: refunds/disputes — ACP merchant-as-MoR se existing dispute
  machinery inherit karta hai.
- **Concept 7 (Settlement):** x402 (sub-cent, high-frequency), MPP (multi-rail, sessions), card rails
  (~2.9%+$0.30, chargeback cover), bank/Lightning (large/cross-border). Decision tree by transaction size.
  **Tool-level check UX hai; real safety wallet ke on-chain caps hain.**

## 03 — Part 3: The Four Protocols In Depth (Concepts 8-11)

- Pydantic contract layer rule: **Decimal money ke liye hamesha, `float` kabhi nahi**.
- **Concept 8 (ACP):** OpenAI+Stripe, Sep 2025, ChatGPT Instant Checkout powers. SPT (one-time, scoped) +
  optional Cart Mandate. Merchant = MoR. Common mistake: user-confirmation step skip karna — cart-confirm
  default rakho pehle mahine.
- **Concept 9 (AP2):** Google, 60+ partners, khud paisa move nahi karta — sirf prove karta hai. 3 mandates
  chain (Intent→Cart→Payment) = non-repudiable audit trail, regulated industries fit. Mistake: mandate
  creation ko checkout-time treat karna — Intent Mandate pehle banao.
- **Concept 10 (x402):** Coinbase→Linux Foundation, HTTP 402 + EIP-3009 + optional Facilitator. 1-2 sec,
  no account/session/human. Wallet on-chain cap = real safety, per-request max nahi.
- **Concept 11 (MPP):** Stripe+Tempo, March 2026. `charge` (one-off) vs `session` (pre-authorized cap +
  metered stream). x402 vs MPP compared (per-request vs per-session, stablecoin-only vs multi-rail).
  Mistake: sessions bohat bare/lambe — session cap = loss limit.

## 04 — Part 4: Composition Rules (Concepts 12-14)

- **Concept 12:** Sabse chota stack jo value ship kare — 4 use-case-to-MVP-stack table (consumer shopping,
  API-paying, enterprise procurement, multi-agent marketplace). Trap: "flexibility ke liye" sab 4 wire
  karna.
- **Concept 13:** Layers-ke-across compose vs same-layer-compete — test: "kya woh same layer par hain?"
  Composition examples (AP2+ACP, AP2+x402, ACP+x402, MCP+x402) vs competition examples (Layer 2/3/4 ke
  andar).
- **Concept 14:** Cost+latency composition table. Decision tree: sub-dollar→x402/MPP; $1-$1,000→ACP+cards;
  $1,000+→AP2+composed. Latency: sub-second→MPP/x402; 5+sec→poora ACP checkout theek hai.

## 05 — Part 5: The Decision Lab (5 Worked Examples)

5 full walkthroughs (use case → 4-layer walk → implementation → likely failure+fix → Inngest pattern):
(1) **Consumer Shopping** (ACP+cards, cart-mismatch failure); (2) **API-Paying Research Agent** (x402-
only, Layers 2+4 collapse, runaway-spend failure); (3) **Enterprise Procurement** (AP2+ACP+MPP, audit-
forced, mandate-scope-mismatch failure); (4) **Multi-Agent Marketplace** (AP2+x402+ERC-8004, gamed-
reputation failure); (5) **Non-Stripe/Non-OpenAI rebuild** — Decision 2 ko Google ADK + Coinbase wallet
par rebuild karke prove karta hai architecture koi ek vendor tak tied nahi (line-by-line translation
table).

## 06 — Part 6: Production Concerns (Concepts 15-18)

- **Concept 15:** Spend-limit **3 independent levels**: (1) Wallet/payment-method limits (asal protection,
  agent-code-fail-hone-par-bhi-hold-karta-hai), (2) SDK `tool_input_guardrail` (per-tool-call, pre-payment),
  (3) Application business logic (per-user/category/merchant). Trap: sirf protocol caps par trust karna
  (caps across-protocols add nahi hote — 100× $50-SPT = $5,000).
- **Concept 16 (Identity Hygiene):** per-agent wallet separation, key rotation (90-day baseline), audit
  logs (crash-survive, payment-se-pehle-logged), distributed traces (OpenTelemetry, ek trace ID). Mistake:
  wallet address ko identity samajhna — **private signing key hi identity hai**, vault mein rakho, env
  vars mein kabhi nahi.
- **Concept 17 (Disputes):** ACP (card-network chargeback, MoR advantage), AP2 (mandate chain = evidence,
  underlying rail replace nahi karta), x402 (**no formal dispute — sabse bari limit**, softeners: escrow/
  AP2-compose/seller-guarantees), MPP (Stripe dispute machinery inherited). Dispute model aksar cost se
  zyada composition drive karta hai.
- **Concept 18 (Webhook Plumbing):** FastAPI thin handler + Inngest durable workflow, 3 patterns (Stripe
  dispute webhook, AP2 mandate-signing callback, x402 seller-side middleware). 3 recurring failures:
  business-logic-inline-in-webhook (double-charge), missing-idempotency, missing-callback-signature-check.

## 07 — Part 7: Closing (Concept 19) + Cheat Sheet + Template + References

- **Concept 19:** Discipline works at 3 scales — protocol (4 protocols, alag layers, treat-as-rivals =
  common mistake), system (SDK = orchestrator jo cleanly compose karne deta hai), discipline (use-case-
  read → 4-layers-split → per-layer-choice → justify-against-real-constraints). 5 Decisions summarized;
  composition **use case se set hoti hai, taste se nahi**.
- **Cheat Sheet (1-page):** 4 layers recap, top picks per layer, 4 canonical compositions table, 3-level
  spend-limit enforcement, economic threshold tree, dispute-model tree.
- **Production Checklist:** 16-item checklist (spend limits 3 levels, keys in vault, wallet separation,
  key rotation, audit logs, OTel traces, Pydantic+Decimal, thin webhook handlers, signature verification,
  idempotency keys, dispute docs, human-in-loop first 30 days, cart-accuracy metric).
- **Design-Review Template:** 6 question categories (Architecture, Economic, Operational, Webhook/async,
  Failure-mode, Track-readiness).
- **References:** ACP/AP2/x402/MPP repos+sites, adjacent (A2A/MCP/UCP/TAP/ERC-8004), OpenAI Agents SDK,
  links to Build Agents / Nervous System / Eval-Driven Development / Choosing Architectures chapters.
