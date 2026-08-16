# 02 — Part 2: The Four Layers In Depth (Concepts 4-7)

## Concept 4 — Layer 1: Discovery

**Ek line mein:** Discovery woh jagah hai jahan agent pata karta hai kya khareeda ja sakta hai; sahi
mechanism iss par depend karta hai ke services asal mein kahan rehte hain.

**4 serious options, 2026 mein:**

| Protocol | Kaise Kaam Karta Hai | Kis Ke Liye Best |
| --- | --- | --- |
| **MCP** (Anthropic) | Tool servers callable functions expose karte hain; agent connect karta hai, tools list karta hai | Developer-wired specific services; high-volume agent work; dominant agent-tooling discovery layer |
| **A2A** (Google) | Agents standard envelopes mein apna offer publish karte hain; doosre agents discover karte hain | Multi-agent ecosystems; AP2 jis layer ko extend karta hai |
| **Agent directories** (Agent.market, lobster.cash, Tenzro) | Public marketplaces jo paid APIs/services list karti hain | Runtime par discovered third-party services — "Yellow Pages" |
| **AI shopping surfaces** (ChatGPT Instant Checkout, Google AI Mode) | Consumer AI products, product discovery + ACP checkout built-in | Consumer flows jahan user AI se baat kar raha ho |

**Choice "MCP vs A2A vs directories" nahi hai. Yeh hai: mere agent ki services asal mein kahan rehti
hain?** Aapke org ke internal — MCP. Partner agents ke network across — A2A. Runtime par discovered
third-party APIs — directories. Consumer products — AI shopping surface + ACP. **Yeh mutually
exclusive nahi hain; real agent aksar kai use karta hai.**

## Concept 5 — Layer 2: Identity Aur Authorization

**Ek line mein:** Authorization woh jagah hai jahan agent prove karta hai human ne yeh spending allow
ki, aur agent woh hi hai jo claim karta hai — paisa move hone se pehle.

Paisa move hone se pehle 2 cheezein sach honi chahiyein: agent woh hai jo claim karta hai, human ne yeh
spending authorize ki. Yeh Layer 2 skip karo to 2 failures milti hain: **fraud** (koi bhi agent kisi ka
bhi paisa spend kar sakta hai) ya **paralysis** (har transaction ko human confirm click chahiye).

**4 options, 4 philosophies:**

| Protocol | Kaise Kaam Karta Hai | Sabse Strong Kahan |
| --- | --- | --- |
| **AP2 Mandates** (Google) | Signed credentials: Intent → Cart → Payment Mandate | Audit-heavy flows, non-repudiable proof of consent; multi-agent flows jahan merchant ne buyer ka agent kabhi nahi dekha |
| **ACP SPT** (OpenAI + Stripe) | Stripe ek Shared Payment Token mint karta hai, merchant/amount/time-window scoped | Consumer shopping jahan Stripe processor hai |
| **TAP** (Visa + Cloudflare) | Agent ki identity signature HTTP headers mein rides, merchants Visa ki directory se verify karte hain | Identity verification specifically (authorization nahi); usually doosre auth protocol ke sath add hota hai |
| **ERC-8004 + on-chain reputation** | On-chain registry agent identities + transaction history ki, reputation score | Pure multi-agent flows, no prior trust |

**2 sawal jo Layer 2 ko jawab dene hain:**
1. **"Kya human ne yeh authorize kiya?"** AP2 → mandate. ACP → SPT (Stripe ne account-level authorize
   hone ke baad hi mint kiya). TAP → jawab nahi deta (identity-only). ERC-8004 → signed on-chain
   transactions
2. **"Kya agent woh hai jo claim karta hai?"** AP2 → signing key. ACP → merchant-scoped SPT. TAP →
   Visa directory lookup. ERC-8004 → on-chain identity record

**SDK 2 integration points deta hai:** tool input guardrail (payment tool se pehle) aur run context
(per-user state dono mein carry hota hai).

```python
@tool_input_guardrail
def block_over_user_cap(data: ToolInputGuardrailData) -> ToolGuardrailFunctionOutput:
    """Reject karo agar request user ke per-run cap se zyada ho."""
    args = json.loads(data.context.tool_arguments or "{}")
    requested = Decimal(str(args.get("max_amount_usd", 0)))
    ctx = data.context.context
    user_cap = Decimal(str(ctx["user_session"].per_run_spend_cap_usd))
    run_spent = Decimal(str(ctx.get("run_spend_usd", 0)))
    if run_spent + requested > user_cap:
        return ToolGuardrailFunctionOutput.reject_content(f"Cap exceed hoga: ${run_spent + requested}")
    return ToolGuardrailFunctionOutput.allow()

@function_tool(tool_input_guardrails=[block_over_user_cap])
async def purchase_with_acp(ctx: RunContextWrapper, merchant_id: str, items: list,
                              max_amount_usd: Decimal) -> PaymentToolResult:
    """Guardrail already verify kar chuka hai spend bounds ke andar hai."""
    ...
```

> **Kaunsa guardrail payment rokta hai:** SDK ke 3 guardrail types alag moments par fire hote hain.
> `input_guardrail` pehle agent ke initial input par chalta hai. `output_guardrail` **final** response
> par chalta hai. `tool_input_guardrail`/`tool_output_guardrail` **har** function-tool call par chalte
> hain, execute hone se pehle/baad. **Payment safety ke liye tool input guardrail chahiye** — output
> guardrail bohat late fire hota hai payment rokne ke liye. Yeh sabse common mistake hai.

**Choice aapke trust model par depend karti hai.** User signed-in hai aur Stripe se SPTs mint kar sakte
ho — ACP sabse production-ready story deta hai. Non-repudiable audit trails chahiye (regulated
industries, B2B procurement) — AP2 mandates fit karte hain. Cryptographic identity alag se chahiye —
TAP add karo. Pure multi-agent, no shared trust — ERC-8004 gap fill karta hai.

## Concept 6 — Layer 3: Commerce

**Ek line mein:** Commerce woh sab kuch hai jo authorization ya settlement nahi hai: cart, order,
fulfillment, dispute, refund — aur plain API call isay poori tarah skip karta hai.

**3 meaningfully different options:**

| Protocol | Kya Karta Hai | Sabse Best |
| --- | --- | --- |
| **ACP** (OpenAI + Stripe) | Structured flow: cart, order confirmation, fulfillment, dispute escalation, refunds. Merchant hi MoR rehta hai | Consumer shopping: retail goods, subscriptions. ChatGPT Instant Checkout power karta hai |
| **UCP** (Google) | Similar lifecycle, Google shopping surfaces (Gemini, AI Mode) ke around | Google Shopping merchants; Google AI surfaces ke agents |
| **Direct API** (machine-to-machine) | Koi commerce protocol nahi, bas HTTP API. x402/MPP se payment. No cart, no disputes, no refunds | API access, compute, data feeds |

**ACP aur UCP compete karte hain; "direct API" iss layer ki absence hai, teesra competitor nahi.**

**Sabse zyada underestimate hone wali cheez: refunds aur disputes.** ACP isay sahi karta hai merchant
ko MoR rakh kar — existing dispute machinery (Stripe chargebacks, retailer ki return policy) bas kaam
karti hai. Direct-API approaches isay galat karte hain — often koi refund path hi nahi hota, jo $0.0001
API call ke liye fine hai lekin $500 API credits ke liye galat.

```python
@function_tool
async def acp_create_cart(merchant_id: str, items: list[CartItem]) -> PaymentToolResult:
    """Cart banao ACP merchant par. Abhi charge NAHI karta."""
    ...

@function_tool
async def acp_checkout(cart_id: str, spt_token: str) -> OrderResult:
    """Pehle se bane cart ke liye checkout complete karo."""
    ...

@function_tool
async def acp_initiate_refund(order_id: str, reason: str) -> RefundResult:
    """Order ke liye refund shuru karo."""
    ...
```

**Poochne wala sawal:** kya use case ko commerce lifecycle chahiye bhi ya nahi? Chahiye (cart, refund,
dispute) to ACP ya UCP chuno. Nahi chahiye to yeh layer skip karo, authorization se seedha settlement
tak jao.

## Concept 7 — Layer 4: Settlement

**Ek line mein:** Settlement woh jagah hai jahan dollars asal mein custody badalte hain, aur pick
mostly transaction ki economics ke baare mein hai.

**4 serious options:**

| Protocol | Kaise Kaam Karta Hai | Economics | Sabse Best |
| --- | --- | --- | --- |
| **x402** | HTTP-native, stablecoin transfer Base/Solana/EVM par, EIP-3009 se signed | Sub-cent gas, 1-2 second finality, no protocol fees | Machine-to-machine micropayments, high-frequency low-value |
| **MPP** | Sessions: cap pre-authorize, metered payments stream. Multi-rail | Stripe fees card rails par, near-zero stablecoin par | Enterprise/multi-rail flows, recurring subscriptions |
| **Card rails** (Stripe/Adyen) | Visa/Mastercard/Amex via Stripe, SPT/Payment Mandate present hoti hai | ~2.9% + $0.30, established dispute machinery | Consumer flows, chargeback exposure |
| **Bank transfer/Lightning** | ACH, SEPA, Bitcoin Lightning | ACH ~$0.25 fixed, Lightning sub-cent | High-value flows, cross-border micropayments |

**Settlement pick mostly paisa ke baare mein hai.** Sub-dollar payments → x402. Consumer purchases
~$1,000 tak → card rails via ACP. Recurring subscriptions → MPP sessions. Large B2B transfers → bank
rails/Lightning. **Upar wali layers usually pick force karti hain:** ACP commerce mein matlab card
rails settlement mein; x402-paywalled MCP server discovery mein matlab x402 settlement mein.

> **Headline-number trap se bacho.** Sahi sawal "kiske paas sabse zyada volume hai?" nahi hai. "Kya is
> transaction ki economics ke sath fit karta hai?" hai. $0.001 API call card rails par settle karna
> call se zyada fees mein kharch karta hai. $5,000 procurement x402 stablecoin par settle karna
> chargeback protection phenk deta hai.

```python
@function_tool
async def x402_fetch(ctx: RunContextWrapper, url: str, max_payment_usdc: Decimal):
    """Paid URL x402 se fetch karo. Settlement automatic hai agar cost <= max_payment_usdc."""
    spent_so_far = Decimal(str(ctx.context.get("session_x402_spend_usdc", Decimal(0))))
    session_cap = ctx.context["user_session"].x402_session_cap_usdc
    if spent_so_far + max_payment_usdc > session_cap:
        return PaymentToolResult(status="rejected", error="Session spend cap exceed hoga")
    response = await x402_client.get(url, max_payment_usdc=max_payment_usdc)
    ctx.context["session_x402_spend_usdc"] = spent_so_far + response.amount_paid_usdc
    return X402PaymentResult(content=response.content, amount_paid_usdc=response.amount_paid_usdc)
```

**Ek cheez clear rakhni hai:** `if spent_so_far + ...` check ek soft guard hai tool body ke andar —
fast, friendly failure ke liye useful, lekin **real safety nahi hai**. Real safety agent ki **smart-
contract wallet** hai. In-tool check delete bhi kar do to wallet caps on-chain transfer reject kar
denge. **Tool ka check UX ke liye hai; wallet caps safety hain.**

---
[⬅ Kyun Naye Protocols Chahiye](01-why-new-protocols.md) · [⬆ Index](README.md)

*(Baqi parts — 4 Protocols SDK Deep Dive, Composition Rules, Decision Lab, Production Concerns,
Closing — likhe ja rahe hain.)*
