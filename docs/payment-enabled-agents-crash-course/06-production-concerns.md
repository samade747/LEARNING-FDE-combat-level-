# 06 — Part 6: Production Concerns — Jo Cheezein System Live Hone Par Marti Hain (Concepts 15-18)

## Concept 15 — Spend-Limit Enforcement 3 Architectural Levels Par

**Ek line mein:** Agent ko overspend karne se rokne ke liye limit ko 3 independent jagahon par enforce
karo, taake ek jagah ki bug baqi 2 se pakri jaye.

Sabse bara tareeqa jispar agent-commerce system badly fail karta hai: **agent allowed se zyada spend
karta hai.** Stuck agent loop seconds mein wallet drain kar sakta hai. Har protocol ka apna cap hai
(ACP SPT amount, MPP session cap, x402 per-request max), lekin **koi bhi akela kaafi nahi hai.**

**Level 1: Wallet aur payment-method limits.** Yeh cap hai jo asal mein protect karta hai. Agent ki
smart-contract wallet (x402 ke liye) ya Stripe customer account (ACP/MPP ke liye) infrastructure level
par spend caps rakhti hai. Chain ya Stripe unhe enforce karti hai chahe agent code kuch bhi kare. **Yeh
akela level hai jo hold karta hai jab agent loop poori tarah fail ho jaye.**

```python
wallet_spend_limits = {
    "max_per_transaction_usdc": Decimal("10.00"),
    "max_per_day_usdc": Decimal("100.00"),
    "max_per_merchant_usdc": Decimal("50.00"),
}
```

**Level 2: SDK tool guardrails.** `tool_input_guardrail` har payment tool se pehle chalta hai aur call
reject kar sakti hai. **SDK-native tareeqa payment ko hone se pehle rokne ka.** Yeh course ka canonical
guardrail block hai — `enforce_per_run_spend_cap` (input) aur `verify_receipt_integrity` (output)
dono ek payment tool ke sath attach hoti hain.

> **Sahi guardrail family use karo:** input guardrails user ke pehle message par, output guardrails
> final reply par, tool guardrails har custom tool call par chalte hain. **Payment safety ke liye
> `tool_input_guardrail` chahiye specifically** — sabse common mistake agent-commerce code mein
> `output_guardrail` ko spend control ke liye reach karna hai. Jab tak yeh fire hoti hai, paisa ja chuka
> hota hai.

**Level 3: Application aur business-logic limits.** Aapka apna code user-specific rules enforce karta
hai — per-user daily caps, per-category caps, allowed merchants. "Yeh user $500/din kisi bhi merchant
par spend kar sakta hai, lekin unverified merchants par sirf $50/din" — yeh rule yahan rehta hai,
protocol mein nahi.

**Har level alag infrastructure mein rehta hai.** Level 1 chain/Stripe mein, Level 2 agent SDK mein,
Level 3 aapke application code mein. **Ek jagah ki bug baqi 2 se pakri jati hai.** Level 1 skip karo,
ek agent-loop bug poori wallet drain kar sakti hai. Level 2 skip karo, run ko mid-flight abort karne
ki power kho dete ho. Level 3 skip karo, per-user/per-category policy enforce nahi kar sakte.

**Trap:** sirf protocol caps par trust karna. ACP SPT cap, MPP session cap, x402 per-request max —
protocol-level limits hain. Specific protocol abuse rokti hain, lekin **protocols ke across add nahi
hoti.** $50 cap wale 100 SPTs lagatar mint karne se koi protection nahi — total $5,000.

## Concept 16 — Agent Identity Hygiene: Keys, Wallets, Aur Audit Logs

**Ek line mein:** Agent ki signing key hi authorized spending aur fraud ke darmiyan khadi hoti hai —
isay guard karo: ek agent ek key, schedule par rotate, har spend durable storage mein logged.

**4 habits:**

**1. Per-agent wallet separation.** Har agent (ya agent class) ki apni wallet/payment handle honi
chahiye. **Alag jobs wale agents ke darmiyan signing keys kabhi share mat karo.** Shopping agent aur
procurement agent ek wallet share karein to ek compromise dono drain karti hai.

**2. Key rotation, schedule par aur demand par.** Signing keys 90-din baseline par rotate karo (Stripe
ki advice API keys ke liye). Turant rotate karo jab operator team chore, deployment signing surface
touch kare, ya kuch galat lage. **Rotation ki habit exact number of days se zyada matter karti hai.**

**3. Audit logs jo crash survive karein.** Har authorization decision durable storage mein log hoti
hai jo agent ke runtime se alag rehti hai — har SPT mint, har mandate sign, har x402 signature, har MPP
session. **Decision payment se pehle log hoti hai, action complete hone se pehle:**

```python
audit_id = str(uuid4())
await neon_client.audit_log.insert({"audit_id": audit_id, "action": "acp_create_cart_and_checkout",
    "merchant_id": merchant_id, "status": "initiated", ...})
try:
    result = await _actually_complete_checkout(...)
    await neon_client.audit_log.update(audit_id, {"status": "completed", ...})
    return result
except Exception as e:
    await neon_client.audit_log.update(audit_id, {"status": "failed", "error": str(e)})
    raise
```

**4. Distributed traces poori transaction ke across.** Audit log batata hai kya succeed hua. Traces
batate hain kya hua — fail/retry/stall hone wale calls sameit. Ek user request ek SDK run, 5-10 tool
calls, 2-3 protocol HTTP requests, ek baad mein ane wala Stripe webhook, aur hours baad resume hone
wala Inngest function mein fan-out hoti hai. **Bina ek trace ID ke jo sab jorde, post-mortem impossible
hai.** OpenTelemetry (`tracer.start_as_current_span`) real, stable API hai isi liye.

**Audit logs aur traces alag sawal jawab dete hain aur dono chahiye.** Audit logs business sawal
("Tuesday ko user ne kitna spend kiya?"), traces debugging sawal ("order abc123 ka checkout kyun fail
hua?"). Audit log sirf successful path record karta hai — retry ya stall karne wali call kabhi capture
nahi karta.

**Sabse common identity mistake:** wallet ke address ko agent ki identity treat karna. Address public
hai. **Private signing key hi identity hai.** Signing keys environment variables (ya source code) mein
rakhne wali teams ne agent ki identity un sab ko de di jinki secrets tak access hai. **Keys vault mein,
kabhi env vars mein nahi.**

## Concept 17 — Dispute Aur Refund Mechanics 4 Protocols Ke Across

**Ek line mein:** Har protocol disputes aur refunds alag tareeqe se handle karta hai, aur aapke use
case ko chahiye dispute model often sabse strong cheez hai jo decide karti hai aap kaunse protocols
compose karte ho.

**ACP: card network se disputes.** Merchant MoR rehta hai, isliye standard card-network dispute path
kaam karta hai — buyer ki bank chargeback shuru karti hai, Stripe merchant ki defense handle karta hai,
merchant apni existing refund policy follow karta hai. **Yeh ACP ka sabse bara practical advantage hai.**

**AP2: audit trail se disputes settle hote hain.** AP2 ka contribution mandate chain hai (Intent →
Cart → Payment). Dispute ate hi, yeh chain evidence hai user ne kya authorize kiya, legally hold karti
hai. **Underlying rail ka dispute path replace nahi karta** — mandate ne agar card payment authorize
kiya, Stripe ka dispute process phir bhi apply hota hai. AP2 sirf proof add karta hai.

**x402: koi formal dispute mechanism nahi.** Pure x402 payments design se non-refundable hain. Payment
on-chain 1-2 seconds mein settle hoti hai; koi chargeback nahi. **Yeh x402 ki sabse bari practical
limit hai.** $0.001 API call ke liye fine hai, kisi bhi jagah jahan buyer fairly refund chahe wahan
galat hai.

*3 tareeqe x402 ki no-refund property soften karne ke:*
- **Escrow** — higher-value x402 payments ke liye smart-contract escrow jo funds buyer acceptance tak
  hold kare
- **AP2 + alag rail ke sath compose** — x402 ki speed chahiye lekin dispute support bhi, mandate chain
  evidence deti hai, settlement phir bhi non-reversible
- **Seller guarantees** — off-chain enforced refund rules (reputable sellers ke liye kaam karta hai,
  anonymous ke sath tootta hai)

**MPP: Stripe se disputes.** Card rails par settled MPP sessions ACP jaisi standard Stripe dispute
machinery inherit karte hain. Stablecoin/Lightning par settled bhi Stripe ke seller-side dispute
resolution se guzarte hain.

**Dispute model aksar composition ko cost/latency se zyada drive karta hai.** Consumer-shopping platform
ko chargebacks chahiye → ACP fit karta hai. Pure machine-to-machine API marketplace ko koi disputes
nahi chahiye → x402 fit karta hai. Enterprise procurement ko audit-grade evidence chahiye → AP2 kisi
bhi settlement rail ke sath fit karta hai.

## Concept 18 — FastAPI Aur Inngest Webhook Plumbing: Request-Response Loop Close Karna

**Ek line mein:** Kuch payment events apne schedule par ate hain: disputes, mandate signatures,
seller-side payment requests. Ek thin FastAPI handler har ek pakarta hai aur Inngest event fire karta
hai jo kaam ko durable workflow tak le jata hai.

Agent commerce **dono directions mein chalta hai.** Stripe `charge.dispute.created` webhooks bhejta
hai. AP2 mandate signing user ke device par off-server hoti hai, baad mein post-back karti hai. x402
sellers ko server-side middleware chahiye jo `402 Payment Required` return kare. **Yeh sab ek
`Runner.run()` call ke andar fit nahi hote** — FastAPI handlers HTTP boundary ki tarah aur Inngest
events durable workflows tak bridge ki tarah chahiye.

**Pattern 1 — Stripe webhook suspended Inngest function tak flow karta hai.** Chargeback file hone par,
Stripe `charge.dispute.created` bhejta hai — order ke 5 minute baad ya 60 din baad. FastAPI handler
webhook ko Inngest event mein badalta hai, Inngest function pick karta hai aur dispute defense agent
chalata hai. **Handler thin rehta hai** (verify → event fire), **Inngest function durable** (idempotency
`raw_event_id` se, retries, step memoization). Agent ki reasoning kabhi webhook handler ke andar nahi
hoti — Stripe ~5 second mein 2xx maangta hai, agent run 30+ second le sakta hai.

**Pattern 2 — AP2 mandate-signing callback suspended `step.wait_for_event` resume karta hai.** User
apne phone par mandate approve karta hai, signed mandate post-back hoti hai. FastAPI callback signature
verify karta hai (registered public key ke against), mandate 7-year retention ke sath persist karta
hai, Inngest event fire karta hai jo suspended workflow resume karta hai (`if_exp` se mandate_id
correlate hota hai, `timeout=timedelta(hours=24)`, timeout par `None` return hoti hai).

**Pattern 3 — x402 seller-side middleware** (jab aap paid API expose karte ho, sirf consume nahi).
Multi-agent marketplace mein aapka agent kabhi buyer, kabhi seller hota hai. Seller side ko middleware
chahiye jo `402 Payment Required` return kare, `X-PAYMENT` headers check kare, resource sirf facilitator
verify karne ke baad serve kare.

**3 failures jo production mein recur hoti hain:**
1. **Webhook handlers business logic inline chalate hain** — agent ko webhook response ke andar chalane
   se Stripe ka 5-second timeout blow past ho jata hai, Stripe retry karta hai, agent 2 baar chalta hai,
   user double-charge hota hai. Handler thin rakho
2. **Webhook idempotency bhoolna** — Stripe same `event.id` se retry karta hai. `idempotency` key ke
   bina, har retry duplicate banata hai
3. **Callbacks par signature check nahi** — AP2 mandate-signed callbacks user ki signature registered
   public key ke against verify karni chahiye, warna koi bhi mandate-signed events forge kar sakta hai

---
[⬅ Decision Lab](05-decision-lab.md) · [⬆ Index](README.md) · [Agla: Closing ➡](07-closing.md)
