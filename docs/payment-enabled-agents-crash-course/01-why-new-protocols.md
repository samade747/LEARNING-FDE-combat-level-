# 01 — Part 1: Agent Commerce Ko Naye Protocols Kyun Chahiye (Concepts 1-3)

## Concept 1 — Woh Assumption Jo Tuti

**Ek line mein:** Payment systems assume karte the ke ek human "buy" click kar raha hai, aur agents
isay 3 tareeqon se ek sath tortay hain.

Payment systems ek khamosh assumption par bane the: human keyboard par hai, buy click kar raha hai.
Har screen, har fraud check, har dispute process log ke liye design hui thi. AI agents isay 3 tareeqon
se ek sath tortay hain:

**Break 1: agents ke email addresses nahi hote.** Consumer payment flows account maangte hain. Account
email/phone/naam maangta hai. Autonomous agent ke paas yeh nahi hote. Fake karo to entity ban jati hai
jo KYC fail karti hai fraud detection ke first look mein.

**Break 2: agents hazaron baar per second act karte hain.** Fraud detection rate, location, pattern se
odd behavior flag karti hai. Ek minute mein 1,000 API calls karne wala agent credential-stuffing
attack jaisa dikhta hai. Jo agent ke liye normal hai woh human ke liye alarm hai.

**Break 3: agents phone nahi utha sakte.** Dispute resolution assume karta hai buyer se contact ho
sakta hai: "kya aapne authorize kiya?" Ek agent jisne charge authorize kiya woh jawab nahi de sakta,
aur uske pichhe wala human ko pata bhi nahi hoga.

| Break | Human-Rail Fix Kya Nahi Kar Sakta | Agent-Rail Fix Kya Deta Hai |
| --- | --- | --- |
| No email/account | Agents ko fake accounts banwana | Cryptographic identity (TAP, ERC-8004) ya scoped tokens (ACP SPT, AP2 Mandate) |
| High-frequency behavior | Attack jaisi traffic block karna | HTTP-native per-request payment (x402) ya pre-authorized sessions (MPP) |
| No phone for disputes | Email disputes jo agent parh nahi sakta | Mandate-based authorization (AP2) non-repudiable audit trail ke sath |

"Purani payments ko bas nayi agent UX mein wrap kar do" raasta already fail ho chuka hai. 2024-2025
mein kai startups ne try kiya: agents ko human-like accounts made-up identity ke sath diye. Fraud
detection ne pakar liya, chargebacks jama ho gaye. **Protocol-level fixes zaroori nikle, optional nahi.**
Isi liye ACP, AP2, x402, aur MPP sab 12 mahino ke andar aye.

## Concept 2 — Ek Protocol Kyun Jeet Nahi Sakta

**Ek line mein:** 4 breaks 4 alag layers par 4 alag incumbents ke sath hote hain, isliye protocols kaam
layer ke hisab se split karte hain, ek sab kuch swallow nahi karta.

Ek unified protocol ko yeh sab specify karna parta:
1. Agents kaise merchants/services dhoondte hain — **discovery** layer
2. Agents kaise prove karte hain kaun hain aur human ne allow kiya — **authorization** layer
3. Agents poori purchase kaise chalate hain, disputes/refunds sameit — **commerce** layer
4. Paisa asal mein kaise move hota hai — **settlement** layer

Har layer ke paas already strong incumbents hain: discovery search engines/APIs ka hai, identity OAuth/
certificate authorities ka, commerce Stripe/Adyen/Shopify ka, settlement Visa/Mastercard/ACH plus naye
crypto rails ka. Unified protocol ko har layer ke har incumbent ko raazi karna parta — yeh kabhi nahi
hone wala tha.

**Jo hua: har protocol ne wahi ek layer li jahan uske sponsor ka sabse zyada leverage tha:**

| Protocol | Sponsor Ka Leverage Kahan Hai | Kaunsi Layer Li |
| --- | --- | --- |
| **ACP** | OpenAI ChatGPT ka shopping channel rakhta hai; Stripe merchant integration | Commerce, human-buyer-via-AI flows ke liye |
| **AP2** | Google ke paas Android wallets aur 60-partner coalition | Authorization, mandates as signed credentials |
| **x402** | Coinbase ke paas stablecoin infra; Cloudflare ke paas HTTP edge | Settlement, machine-to-machine micropayments |
| **MPP** | Stripe ke paas merchant relationships; Tempo ke paas blockchain | Settlement, enterprise aur multi-rail flows |

**Poore course ka core idea:** **Ek layer ke andar, ek protocol chuno. Layers ke across, kai compose
karo.** 4 protocols choose karne wale alternatives nahi, stack karne wale layers hain.

## Concept 3 — OpenAI Agents SDK Bataur Universal Client

**Ek line mein:** Aap 4 protocols 4 alag tareeqon se wire nahi karte. Har ek ek tool ban jata hai jo
agent call karta hai, aur SDK sabke peeche single client hai.

2026 mein jawab yeh hai ke agent ka framework universal client ban jata hai. Har protocol SDK ya HTTP
endpoint expose karta hai, aur framework usay tool ki tarah wire karta hai. Yeh OpenAI Agents SDK,
LangGraph, AutoGen, CrewAI sab mein hold karta hai.

**Har protocol integration ka same shape:** protocol ko ek ya zyada `@function_tool` functions mein
wrap karo, `Agent` ko hand karo, `Runner.run` loop chalaye.

```python
@function_tool
async def acp_checkout(merchant_id: str, items: list, max_amount: Decimal) -> PaymentToolResult:
    """ACP se merchant par checkout complete karo."""
    spt = stripe.PaymentTokens.create(amount=int(max_amount * 100), currency="usd",
                                        merchant_id=merchant_id, max_uses=1)
    response = await acp_post(merchant_id, items, spt.token)
    return PaymentToolResult(status="success" if response.status == "confirmed" else "failed",
                              details={"order_id": response.order_id})

@function_tool
async def x402_fetch(url: str, max_payment_usdc: Decimal) -> X402PaymentResult:
    """x402 payment ke sath ek URL fetch karo."""
    client = X402Client(wallet=agent_wallet, max_per_request=max_payment_usdc)
    response = await client.get(url)
    return X402PaymentResult(content=response.content, amount_paid_usdc=response.amount_paid_usdc)

shopping_agent = Agent(name="ShoppingAgent",
    instructions="Retail goods ke liye acp_checkout, paid APIs ke liye x402_fetch use karo.",
    tools=[acp_checkout, x402_fetch], model="gpt-5.5")
```

**Shape identical hai chaaron protocols ke across.** SDK universal client hai; har protocol sirf ek
tool hai jo agent reason karta hai aur zaroorat par call karta hai. **3 cheezein jo matter karti hain:**

1. **Typed return value payment results ke liye** — Pydantic model se agent ko clean type info milti
   hai kya succeed hua, kya fail hua
2. **`Runner.run(..., context=...)` payment context ke liye** — user identity, spending limits, wallet
   handle instructions mein bake karne ki jagah `context` parameter se pass karo — per-run, per-user
3. **`tool_input_guardrail` spend limits ke liye** — tool execute hone se **pehle** chalta hai aur
   call reject kar sakta hai. SDK-native tareeqa payment ko hone se pehle rokne ka — baad mein nahi.
   Agent-level `output_guardrail` yeh solve nahi karta, kyunki woh final reply par fire hota hai,
   payment ho chukne ke baad

---
[⬅ Overview](00-overview.md) · [⬆ Index](README.md) · [Agla: 4 Layers In Depth ➡](02-four-layers.md)
