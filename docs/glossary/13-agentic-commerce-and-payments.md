# 13 — 11. Agentic Commerce and Payments

Agents paisa kaise spend karte hain — ACP, AP2, x402, MPP jaisi payment protocols ki vocabulary.

---

_These terms describe how AI Workers become buyers — the trust infrastructure that lets them pay for compute, data, and services autonomously, within the authority envelope their human supervisor defines. Every term here traces back to the [Agents as Economic Actors](https://agentfactory.panaversity.org/docs/thesis#agents-as-economic-actors) section of the thesis._

### Agentic Commerce

The broad shift from humans clicking "buy" to AI agents executing purchases on their own behalf. Covers both agent-to-business transactions (an agent buying an API subscription for its company) and agent-to-agent transactions (one agent hiring another for a specialist task).

> 💡 **Analogy:** Online shopping turned retail into clicks. Agentic commerce turns clicks into autonomous transactions. A textile factory's procurement agent doesn't wait for a human to log in and order cotton; it watches inventory, negotiates with supplier agents, and places the order inside a pre-approved budget.

### Agents as Economic Actors

The thesis claim that AI Workers will stop being tools and start being participants in markets — discovering services, negotiating terms, making payments, and signing contracts within budgets their human supervisor sets. The next inflection after outcome-based pricing.

> 🔹 **Example:** A churn-reduction Digital FTE is given a Rs. 500,000 monthly budget and a goal: "Reduce customer churn by 15%." It autonomously purchases API credits for enrichment data, provisions a training cluster for a model, and buys SMS credits from JazzCash to run retention campaigns — all without human approval on each transaction, because the authority envelope already permits it.

### Authority Envelope

The set of rules that defines what an AI agent is allowed to do on a human's behalf — spending limits (per transaction, per day, per vendor), approved vendors, required approvals, audit requirements. The digital equivalent of a purchase authorization matrix for a human employee.

> 💡 **Analogy:** A company gives a purchasing manager a card with a Rs. 200,000 daily limit, approved vendor list, and a rule that anything over Rs. 50,000 needs a second signature. The authority envelope is that same rulebook, written in code, enforced automatically on every agent action.

### Trust Layer

The infrastructure that lets organizations safely delegate purchasing authority to agents: signed mandates, audit trails, dispute resolution, liability frameworks, and reconciliation. The payment rails already exist; the trust layer is the gap the industry is racing to fill in 2026.

> 🔹 **Example:** An agent places a Rs. 1,000,000 order with a supplier that never delivers. Who is liable — the agent's owner, the platform that hosted the agent, or the supplier? The trust layer is the legal, technical, and insurance infrastructure that answers this question before the transaction happens, not after.

### Signed Mandate

A cryptographically signed, verifiable statement that defines what an agent is authorized to do on its principal's behalf — what it can buy, how much it can spend, from whom, and under what conditions. Portable across platforms, verifiable by any merchant, revocable by the principal.

> 💡 **Analogy:** A notarized power of attorney document. A person signs a document saying "this lawyer can act on my behalf, but only for these matters, up to this amount, until this date." A signed mandate is the same thing, digital and machine-readable. AP2 is built entirely around this concept.

### ACP (Agentic Commerce Protocol)

An open standard co-developed by OpenAI and Stripe for standardizing checkout flows between AI agents and merchants. First deployed in ChatGPT's Instant Checkout, now extending through Shopify and PayPal. Operates at the checkout layer — how an agent actually completes a purchase on a merchant site.

> 🔹 **Example:** A Pakistani buyer asks an agent to order imported specialty flour. The agent searches, compares, and hits "buy" on a Shopify store using ACP. The store recognizes the request as agent-initiated, validates the mandate, processes the card, and returns a receipt — no human had to fill in a form.

### AP2 (Agent Payments Protocol)

An open standard developed by Google with 60+ partners for the authorization layer of agent payments. AP2 defines how mandates are signed, verified, and enforced across ecosystems. It doesn't move money itself — it decides whether a given agent is allowed to move money.

> 💡 **Analogy:** AP2 is the bouncer at the door, checking ID and the guest list. ACP is the bar inside taking the order. x402 and MPP are the payment terminals. Each does a different job; together they make agentic commerce work.

### x402

A protocol created by Coinbase that reuses the dormant HTTP 402 "Payment Required" status code to enable instant stablecoin payments over HTTP. Purpose-built for machine-to-machine microtransactions — an agent calling a paid API pays per call, settled on-chain in USDC. V2 launched December 2025; Stripe integrated it on Base in February 2026; Cloudflare supports x402 transactions natively.

> 🔹 **Example:** An agent needs one lookup against a premium data API that charges $0.02 per call. Instead of signing up for a monthly subscription, it hits the API endpoint, gets a `402 Payment Required` response, pays $0.02 in USDC, retries with the payment receipt, and gets the data. Total elapsed time: under a second.

### MPP (Machine Payments Protocol)

An open standard co-developed by Stripe and Tempo, launched March 18, 2026. MPP shares x402's HTTP 402 mechanism but is payment-method agnostic — supporting stablecoins, cards, wallets, and Stripe's Shared Payment Tokens. Introduces a "sessions" model that lets an agent pre-authorize a spending limit and stream micropayments within it, rather than authorizing each transaction individually.

> 💡 **Analogy:** A prepaid Easypaisa wallet with a daily limit. Once you've loaded it and set the ceiling, you can make dozens of small payments without re-authorizing each one. MPP sessions work the same way for agents — one authorization, many streamed payments, auto-cutoff at the limit.

---

---
[⬅ Prev](12-security-safety-and-enterprise-terms.md) · [Next ➡](14-monitoring-quality-and-llmops.md)
