# 05 — Part 5: The Decision Lab (5 Worked Examples)

Har Decision: use case, 4 layers walk (kaunsa protocol kis layer par, kyun), implementation shape, sabse
likely production failure + fix. **Pehle 4 matrix ke rows cover karte hain; 5wan ek ko bilkul alag
toolchain mein rebuild karta hai framework prove karne ke liye ke woh kisi ek vendor tak tied nahi hai.**

## Decision 1 — Consumer Shopping Agent (ChatGPT Instant Checkout Pattern)

**Use case:** ACP-enabled merchants (Walmart, Etsy, Shopify sellers) par shopping agent. User batata
hai kya chahiye; agent catalogs search karta hai, options dikhata hai, confirm hone par checkout karta
hai. $5-$500 per order, refunds/chargebacks required.

**4 Layers Walk:**
- **Discovery:** AI shopping surface (ChatGPT Shopping) — discovery work already ho chuka hai, million
  catalogs khud wire karna viable nahi
- **Auth:** ACP SPT, Stripe se mint, ek merchant/amount/10-minute window scoped
- **Commerce:** ACP — poori lifecycle matter karti hai (cart, checkout, fulfillment, disputes, refunds)
- **Settlement:** Card rails via Stripe — $5-$500 card-rail sweet spot mein hai, chargeback cover
  worth hai

**Sabse likely production failure:** cart mismatches ("red maanga, pink mila"). **Fix:** SPT mint hone
se pehle user cart confirm kare, cart-accuracy log karo, accuracy 95% se neeche jaye to instructions
tune karo.

**Inngest:** `step.wait_for_event` cart-confirmation gate ke liye, per-user concurrency cap.

> **Yeh pehle chuno.** Yehi live use case hai aaj — ChatGPT Instant Checkout, ACP ecosystem, har
> ACP-enabled Shopify merchant. Ek composition ship kar sakte ho to yehi ship karo.

## Decision 2 — API-Paying Research Agent (x402-Only Pattern)

**Use case:** third-party APIs (financial feeds, news, specialized search) pay karne wala research
agent. Runtime par Agent.market se paid APIs discover karta hai. High-frequency micropayments $0.001-
$0.50, task shuru hone ke baad koi human nahi, koi commerce lifecycle nahi.

**4 Layers Walk:**
- **Discovery:** Agent.market + MCP-via-Cloudflare — runtime discovery + pre-wired fallback set
- **Auth + Settlement (collapsed):** Task shuru hone ke baad koi human nahi. Wallet ke on-chain caps
  per-transaction bound karte hain, user-level caps SDK `tool_input_guardrail` se. EIP-3009 signature
  dono authorization aur settlement hai. **x402 on Base, koi separate mandate protocol nahi**
- **Commerce:** None — "purchase" sirf ek API call hai

**Sabse likely production failure:** stuck loop se runaway spend — agent same data re-fetch karta
rehta hai budget khatam hone tak. **Fix:** wallet ke on-chain caps (real safety), SDK session-spend
guardrails, dedup cache identical fetches dubara pay na karein.

**Inngest:** `step.run` memoization pay off hoti hai — session ke beech crash ho to retry sirf baqi
data ke liye pay karta hai.

> **Pure machine-to-machine.** Layers 2 aur 4 ek signature mein collapse hoti hain, Layer 3 khaali
> hai. Decision 1 se structurally simpler hai: kam protocols, kam integration points, kam cost per
> call. Trade: koi chargeback cover nahi, koi commerce semantics nahi — jo theek hai kyunki use case ko
> dono chahiye nahi.

## Decision 3 — Enterprise Procurement Agent (AP2 + Composed-Stack Pattern)

**Use case:** regulated enterprise (financial services) ke liye procurement agent. Buyers tasks
delegate karte hain: "50 ergonomic keyboards approved suppliers se, $5,000 se neeche, Friday tak."
Audit trail legally required, spend caps multiple levels par, suppliers pre-approved (runtime discovery
nahi).

**4 Layers Walk:**
- **Discovery:** Internal MCP server supplier catalogs ke sath — scope bounded hai
- **Auth:** AP2 — Intent Mandate task creation par, Cart Mandate checkout se pehle, Payment Mandate
  settlement par, har ek procurement officer sign karta hai. **Non-repudiable audit trail** skip nahi
  ho sakta
- **Commerce:** ACP ACP-enabled suppliers ke liye, direct B2B API baqi ke liye
- **Settlement:** MPP sessions recurring suppliers, ACP SPT + card rails one-off buys (supplier
  history se pick hota hai)

**Sabse likely production failure:** Intent Mandate scope mismatches — officer mandate sign karta hai,
agent kaam karta hai, phir cart mandate fit nahi karta. **Fix:** agent shopping shuru karne se pehle
mandate scope validate karo (Intent Mandates pehle banao), scope se bare tasks reject karo.

**Inngest:** AP2 mandate signing `step.wait_for_event` ka natural fit. Multi-stage tasks per-stage
`step.run`, per-user concurrency cap.

> **Regulated industry.** Audit rules AP2 ko Layer 2 par force karti hain; kai suppliers ACP + direct
> APIs ko Layer 3 par sath force karte hain; recurring vs one-off MPP + cards ko Layer 4 par sath force
> karta hai. Decisions 1-2 se heavier composition, audit requirement isay justify karti hai.

## Decision 4 — Multi-Agent Marketplace (AP2 + x402 + ERC-8004 Pattern)

**Use case:** platform jahan agents doosre agents hire karte hain. Agent A ko research chahiye, Agent B
research x402 service ki tarah bechta hai. Koi ek doosre par abhi trust nahi karta, transactions
verifiable honi chahiyein, payment pure crypto-native (no cards). $0.10-$100 per transaction, dono
sides ko verifiable identity chahiye.

**4 Layers Walk:**
- **Discovery:** A2A — Agent B apni capability publish karta hai, Agent A discover karta hai
- **Auth:** AP2 + ERC-8004 — AP2 mandates user consent prove karte hain; ERC-8004 Agent B ko on-chain
  reputation deta hai jo Agent A pehle check kar sake. **Composed for full bilateral verification**
- **Commerce:** None — sirf "yeh task karo aur report do"
- **Settlement:** x402 `a2a-x402` extension se — crypto-native, sub-second, koi chargeback cover nahi
  chahiye

**Sabse likely production failure:** gamed reputation trust karna — ERC-8004 scores auditable hain
lekin operator chote successful jobs se inflate kar sakta hai. **Fix:** reputation ko doosre signals ke
sath combine karo (operator identity, transaction-volume thresholds, dispute history), first-time
counterparties ke liye ek amount ke upar human review add karo.

**Inngest:** kai specialists hire karte waqt fan-out, har result ke liye `step.wait_for_event`,
per-stage `step.run`. **Yeh decision har Inngest primitive touch karti hai.**

> **Pure multi-agent economy.** Transaction time par koi human nahi, dono agents pre-authorized scopes
> ke andar act karte hain. Sabse zyada failure modes wali shape — no-prior-relationship bilateral trust
> mushkil hai aur protocol stack sirf partially solve karta hai.

## Decision 5 — Non-Stripe, Non-OpenAI Stack (Prove Karta Hai Framework Travel Karta Hai)

Ab tak sab code samples `stripe.PaymentTokens.create(...)` aur OpenAI Agents SDK use karte the. Yeh
Decision 2 (API-paying research agent) ko **bilkul alag toolchain** par rebuild karta hai: Google's
Agent Development Kit (ADK) runtime ke liye, Coinbase smart-contract wallet on-chain identity ke liye,
AP2 mandates authorization ke liye, direct x402 settlement ke liye. **Zero Stripe, zero OpenAI.**

Use case Decision 2 wala hi hai. Architecture bhi wahi: x402 Layers 2+4 collapse karta hai, koi
commerce layer nahi, MCP discovery ke liye. **Sirf library badalti hai.**

**Line-by-line translation:**

| Decision 2 (OpenAI + Stripe) | Decision 5 (Google ADK + Coinbase) | Same Concept |
| --- | --- | --- |
| `from agents import Agent, function_tool` | `from google.adk import Agent` + tools import | Agent runtime |
| `@function_tool` (OpenAI Agents SDK) | `@function_tool` (Google ADK) | Tool decorator |
| `RunContextWrapper` | `context={...}` kwarg to `run_async` | Per-run state |
| `stripe.Customer.modify(...)` caps ke liye | `SmartWalletProvider(spend_limits={...})` | Spend caps, chain-native |
| `tool_input_guardrail` decorator | in-tool check + wallet caps | Pre-execution validation |
| `Runner.run(agent, ...)` | `agent.run_async(...)` | Agent execution |

**Kya identical rehta hai:** Architecture — Layer 1 MCP/directory, Layer 2 mandate + wallet caps,
Layer 3 none, Layer 4 x402. Primitives — Intent Mandate, EIP-3009 signatures, 402 responses, on-chain
spend caps.

**2 real operational differences:**
1. **Google ADK ke paas first-class tool input guardrail nahi hai (mid-2026 tak).** Workaround: in-tool
   validation, wallet ke on-chain caps se backed. Caps phir bhi protect karte hain, in-tool check sirf
   faster fail hota hai
2. **AP2 mandate signing yahan zyada native hai** — Google ne AP2 banaya, ADK ecosystem mandate-signing
   UI flows achi tarah integrate karta hai

**Poore Decision 5 ka point:** architecture library swap survive kar gaya, sirf imports badle. **Yeh
kisi bhi agent-commerce framework ka real test hai:** agar sirf ek vendor ke stack mein express ho
sakta hai, yeh ek library tutorial hai costume mein. Yeh nahi hai.

---
[⬅ Composition Rules](04-composition-rules.md) · [⬆ Index](README.md) · [Agla: Production Concerns ➡](06-production-concerns.md)
