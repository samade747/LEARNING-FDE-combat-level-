# 03 — Part 3: The Four Protocols In Depth (Concepts 8-11)

> **Pydantic contract layer:** poore course ke code samples Pydantic models use karte hain, plain dicts
> nahi — protocol payloads, tool returns, FastAPI bodies, Inngest events sab ke liye. 4 boundaries
> cross hoti hain ek typical flow mein (tool return → protocol endpoint → response wapis → webhook
> FastAPI handler tak). **Untyped dict har boundary par chupke se fields khoti hai; Pydantic models
> exact field point karti hain.** **Decimal hamesha money ke liye, `float` kabhi nahi** — floating-point
> math precision khoti hai jo hazaron micropayments ke across compound hoti hai.

## Concept 8 — ACP (Agentic Commerce Protocol): Consumer-Shopping Protocol

**Ek line mein:** ACP woh hai jispar agent real merchant par asal checkout complete karta hai kisi
insaan ki taraf se, merchant hi sale ke liye responsible rehte hue.

**Kya hai:** OpenAI + Stripe ka open spec, September 29, 2025 ko Etsy/Shopify launch partners ke sath
launch hua. Early 2026 tak ChatGPT Instant Checkout power karta hai. Apache 2.0, beta spec.

**Kahan Rehta Hai:** mostly Layer 3 (Commerce), Layer 2 (Authorization) tak apne token mechanism se
reach karta hai. Cart formation, checkout, order management, fulfillment status, refund mechanics
cover karta hai. **Merchant hi Merchant of Record rehta hai** — chargebacks, returns, customer service
sab merchant ke existing systems se flow karte hain.

**2 important primitives:**
1. **Shared Payment Token (SPT)** — payment processor (Stripe) se one-time token, ek merchant/amount
   cap/short time window/usually single use tak locked. Agent $50 cleared ho aur $1,000 spend try kare
   to SPT protocol level par hi fail ho jati hai
2. **Cart Mandate (AP2 extension ke through)** — extra audit rigor ke liye, user Cart Mandate sign
   karta hai SPT submit hone se pehle. ACP mein optional hai, regulated flows mein increasingly common

**SDK integration shape:** `verify_user_can_spend` tool input guardrail (`tool_arguments` se
`max_total_usd` check, user session ke `can_spend()` ke against). `acp_browse_merchant` (catalog
search), `acp_create_cart_and_checkout` (guardrail-protected, SPT mint karta hai, checkout submit
karta hai), `acp_check_order`, `acp_refund` — sab `@function_tool` decorated. Har checkout tool ke sath
guardrail attach hoti hai.

**Harness (yeh baseline har protocol par apply hoti hai):** plain cloud harness, extra kuch nahi.
Stripe SDK FastAPI handler ke andar chalta hai, ACP calls outbound HTTPS hain. **Ek rule: Stripe API
keys secret store (key vault) mein rakho, environment variables mein kabhi nahi**, Stripe ke schedule
par rotate karo. **Koi sandbox nahi chahiye** (ACP koi code nahi chalata), **koi special storage nahi**
(orders Stripe aur merchant system mein persist hote hain).

**Inngest durability:** ACP transactions short hain (5-30 seconds), `step.run` blocks mein fit hote
hain. `step.wait_for_event` tab kaam karta hai jab agent user ko cart confirm karne ke liye pause kare
(cart creation aur checkout ke darmiyan, human-in-the-loop pattern).

**Jahan teams galti karte hain:** user-confirmation step skip karna. ACP dono support karta hai — "user
har cart confirm kare" aur "user is type ki purchase pre-authorized kar chuka hai." Teams speed ke liye
doosra chunte hain, phir dekhte hain SPT ki chhoti misconfiguration agent ko slightly-wrong items khareedne
deti hai bina recover karne ke tareeqe ke. **Production ke pehle mahine cart confirm karna default
rakho.**

## Concept 9 — AP2 (Agent Payments Protocol): Authorization Layer

**Ek line mein:** AP2 signed proofs produce karta hai ke human ne spending allow ki; khud paisa move
nahi karta, sirf prove karta hai move hone diya gaya tha.

**Kya hai:** Google ka open spec, 60+ partners ke sath, September 2025 launch (latest v0.2.0, April
2026). Apache 2.0. **Authorization layer hai, commerce ya settlement nahi.** Signed mandates produce
karta hai jo prove karte hain agent spend karne ke liye authorized hai, settlement kisi bhi rail par
chorta hai (cards, bank, ya x402 through `a2a-x402` extension).

**Kahan Rehta Hai:** Layer 2 (Identity aur Authorization). 2 protocols par build hota hai neeche:
A2A (agent-to-agent messaging) aur MCP (tool exposure). AP2 mandate A2A ke over ya MCP tool call ke
sath attached signed credential ki tarah travel karta hai.

**3 primitives — 3 mandate types:**

| Mandate | Kab Banti Hai | Kya Prove Karti Hai |
| --- | --- | --- |
| **Intent Mandate** | Task shuru mein, user apni UI mein sign karta hai | User ne agent ko set rules ke andar act karne diya (price limits, time windows, allowed merchants) |
| **Cart Mandate** | Agent ne specific cart banane ke baad, checkout se pehle user sign karta hai | User ne yeh exact cart is exact price par approve kiya |
| **Payment Mandate** | Payment ke waqt, user sign karta hai ya Intent Mandate ke against auto-generate hoti hai | User ne yeh exact payment is exact rail par authorize ki |

**Audit trail:** 3 mandates ek chain banati hain jise signer baad mein deny nahi kar sakta — Intent
("shoes under $120") → Cart ("$110 wale yeh shoes") → Payment ("is stablecoin wallet ko charge karo").
**Non-repudiable** — "maine kabhi authorize nahi kiya" user ki apni signature ke against nahi tikta.
Isi liye AP2 regulated industries (healthcare, financial services) fit karta hai.

**SDK ke liye kya badalta hai:** AP2 ki OpenAI Agents SDK mein first-class jagah nahi hai; reference
builds Google ADK use karti hain. Aap isay `@function_tool` functions ki tarah wire karte ho jo
mandates create/sign/validate/dispatch karte hain. `require_intent_mandate` guardrail Cart Mandate se
pehle Intent Mandate hone confirm karti hai. `ap2_create_intent_mandate` (user signing UI, block until
sign/reject), `ap2_create_cart_mandate` (Intent Mandate rules ke against check karta hai), `ap2_settle_via_x402`
(`a2a-x402` extension se stablecoin settle karta hai).

**Harness mein kya add hota hai:** signing surface (user mandates sign kare — web/mobile/notification-
based), aur signed mandates ke liye durable storage jo dispute windows jitni lambi ho (7-year retention
financial mandates ke liye standard hai).

**Inngest durability:** mandate signing `step.wait_for_event` ka textbook use hai — "signing requested"
event fire hoti hai, function suspend hota hai, user UI mein sign karta hai jo "signing signed" fire
karta hai, function resume hota hai. Zero compute waiting ke doran.

**Jahan teams galti karte hain:** mandate creation ko checkout-time concern treat karna aur mandate
sign karna agent ka bohat kaam kar chukne ke baad. **Intent Mandate pehle banao**, agent ke shop karne
se pehle — scope mismatch jaldi pakarta hai (user shoes chahta tha, Intent sirf office supplies allow
karta hai) us cart par compute waste karne se pehle jo kabhi fund nahi ho sakega.

## Concept 10 — x402: HTTP-Native Settlement Protocol

**Ek line mein:** x402 agent ko 1-2 seconds mein API call ke liye stablecoin se pay karne deta hai,
purani HTTP 402 "Payment Required" status code revive karke.

**Kya hai:** Coinbase ne banaya (May 2025), V2 December 2025 mein launch hui, ab Linux Foundation ka
x402 Foundation govern karta hai (April 2026), Cloudflare/Stripe/AWS/Google members. Apache 2.0. Early
2026 tak 100 million+ payments Base aur Solana ke across.

**Kahan Rehta Hai:** mostly Layer 4 (Settlement) machine-to-machine flows ke liye, Layer 1 (Agent.market
directories) aur Layer 3 (full commerce layer plain API access ke liye jahan real purchase lifecycle
nahi hai) tak bhi reach karta hai.

**4 primitives:**
1. **HTTP 402 status code** — unpaid client paid resource maange, server `402 Payment Required` +
   header (scheme, network CAIP-2 form mein jaise `eip155:8453` matlab "Base", asset USDC, recipient,
   max amount, expiry) return karta hai
2. **Payment authorization header** — client signed payment authorization ke sath retry karta hai,
   signature off-chain hoti hai, buyer koi gas fee nahi deta
3. **EIP-3009 (transferWithAuthorization)** — Ethereum standard jispar x402 bana hai, buyer off-chain
   sign karta hai, koi aur on-chain submit karta hai
4. **Facilitator** — optional third party jo signature check karke on-chain payment submit karti hai
   (Coinbase, Cloudflare dono facilitators chalate hain)

**Poori transaction 1-2 seconds leti hai. Koi account creation, API key, session, ya human in the loop
nahi.**

**SDK ke liye kya badalta hai:** x402 ki sabse simple story hai 4 mein se. `x402_fetch` tool
(`enforce_x402_session_cap` guardrail ke sath — session spend track karti hai), `x402_search_agent_market`
(Agent.market search). MCP server ko `withX402Client` se wrap kiya ja sakta hai (Cloudflare pattern).

**Harness mein kya add hota hai:** almost kuch nahi. Agent ki smart-contract wallet chain par address
rakhti hai (usually Base), signing key key vault mein, buyer-side library signing + HTTP retry handle
karti hai.

> **Wallet cap hi asal safety hai.** Trap yeh hai agent ko credit card ki tarah treat karna. Real
> safety **wallet ka on-chain spend limit** hai, per-request `max_payment_usdc` nahi. On-chain limit
> skip karo aur no-cap hot wallet use karo, ek stuck agent loop poori wallet drain kar sakta hai. Per
> agent identity, per session, per merchant — 3 independent layers configure karo.

**Inngest durability:** x402 calls short (1-2 sec) aur idempotent hain — same request/signature same
outcome dete hain. 5 of 10 API calls pay ke baad crash ho to memoized 5 calls dubara pay nahi hoti,
sirf baqi 5.

## Concept 11 — MPP (Machine Payments Protocol): Sessions-Based Settlement

**Ek line mein:** MPP agent ko ek "prepaid tab" open karne deta hai spending cap ke sath, phir uske
against kai chote payments stream karta hai jab tak tab close na ho.

**Kya hai:** Stripe + Tempo, March 2026 launch. Tempo Stripe/Paradigm ka layer-1 blockchain hai
high-frequency machine payments ke liye. Apache 2.0. **MPP x402 ka settlement-layer jawab hai — same
use case, alag philosophy.**

**Kahan Rehta Hai:** Layer 4 (Settlement), x402 se directly compete karta hai. **Key difference: MPP
multi-rail hai aur per-charge + session-based dono support karta hai, x402 stablecoin-only aur
per-request hai.**

**HTTP shape:** x402 402 code + custom headers use karta hai; MPP standard HTTP authentication par
payment layer karta hai — server `WWW-Authenticate: Payment` return karta hai, client `Authorization:
Payment <signed-payload>` se retry karta hai, server `Payment-Receipt` reply karta hai.

**2 intent types:**

| Intent | Lifecycle | Best For |
| --- | --- | --- |
| **`charge`** | One-off transfer, ek round-trip mein authorized+settled | Single purchases, one-time API access |
| **`session`** | Cap+duration pre-authorize, phir metered micropayments stream, close hone tak | High-frequency micropayments, recurring subscriptions |

**x402 vs MPP trade:**

| Dimension | x402 | MPP |
| --- | --- | --- |
| Authorization frequency | Per request | Per charge/session |
| Rails | Stablecoin only | Multi-rail (stablecoin, Lightning, cards, ACH) |
| Fees | Zero protocol fee + sub-cent gas | Stripe fees on cards, near-zero Tempo stablecoin |
| Recurring support | Limited | Native via `session` intent |
| Best fit | One-off API calls | Recurring subscriptions, enterprise, fiat fallback needed |

**SDK ke liye kya badalta hai:** `mpp_create_session` (`verify_mpp_session_authorized` guardrail ke
sath), `mpp_metered_call` (active session ke andar), `mpp_close_session` (total charged + rail
breakdown return karta hai).

**Harness mein kya add hota hai:** ek configuration step — Stripe account par MPP enable karna. Tempo
integration Stripe ka MPP server handle karta hai, agent Tempo se seedha touch nahi karta.

**Jahan teams galti karte hain:** sessions bohat bare ya lambe banana. **Session cap aapka loss limit
hai agar kuch galat ho.** "Convenience ke liye" $1,000 session $1,000 ke agent-loop-gone-wrong losses
ka exposure create karta hai. Sessions ko actual expected work ke hisab se right-size karo.

---
[⬅ 4 Layers In Depth](02-four-layers.md) · [⬆ Index](README.md) · [Agla: Composition Rules ➡](04-composition-rules.md)
