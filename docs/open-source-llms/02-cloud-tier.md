# 02 — Cloud Tier: Frontier Models (OpenRouter)

## Concept 13: Open Weights Jo Aap Utha Nahi Sakte

Part 2 ka honest limit: capability wall sirf **bare brain** se clear hoti hai. Aaj ke sab se bare open
brains:

- **Kimi K3** (Moonshot AI) — **performance** ke liye. 2.8 trillion parameters, 1 million token context.
  Open-weight models mein top ranked
- **DeepSeek V4 Pro** (DeepSeek) — **price performance** ke liye. 1.6 trillion parameters (~49B active
  per token), MIT license, K3 se sasta

**Honest arithmetic:** "Open weights" ka matlab hai aap **chala sakte** ho. Ye matlab nahi ke aap
**waqai chala sakte** ho. K3 ko **64+ accelerator chips** chahiye. DeepSeek V4 Pro ko **8-16 datacenter
GPUs**. **Frontier open models ke liye, sab kiraye pe lete hain.**

**"Open" 3 cheezein deta hai:** No lock-in (koi company model chheen nahi sakti), choice of landlord
(kai hosts compete karte hain), a floor under your future (zaroorat pare to aap khud hardware khare kar
sakte ho).

**OpenRouter** ek **gateway** hai — ek address, ek key, ek bill, sainkron models ke liye.

> **Simple:** Part 1 ghar mein cooking thi. Part 2 apni industrial kitchen. Part 3 duniya ke great
> restaurants — 64 stoves wali kitchens jo aap kabhi ghar mein nahi banaoge. OpenRouter delivery app
> hai jismein sab restaurants ek menu pe hain.

## Concept 14: Frontier Brains Ko Wahi 2 Agents Se Chalao

```bash
export ANTHROPIC_BASE_URL=https://openrouter.ai/api
export ANTHROPIC_AUTH_TOKEN=sk-or-...
export ANTHROPIC_API_KEY=
claude --model moonshotai/kimi-k3
```

**OpenCode** OpenRouter ko out-of-box jaanta hai (`/connect`).

> **Ehtiyat:** Claude Code sirf Anthropic ke apne models pe fully test hota hai. Non-Anthropic models
> experimental hain. Full-supported path OpenCode hai, ya Claude Code Router (Concept 16).

**Feel farq:** koi queue nahi, koi crawl nahi, clean tool calls — frontier models **dono deewarein**
clear karti hain ek saath.

> **Trade:** Pehli dafa aapke lafz machine se **bahar** gaye, aur pehli dafa tokens **paisa** cost karte
> hain. **Private and free Part 1 thi. Ye powerful and metered hai.**

## Concept 15: Performance Ya Price

Roughly: **Kimi K3** $3/million input, $15/million output. **DeepSeek V4 Pro** $0.44 in, $0.87 out.
Output pe, price-performance pick **~17x sasta** hai.

**Working rule:** **Default price-performance model ko, escalate performance model tak jab sasta wala
insufficient prove ho** — real failures se trigger, vibes se nahi.

**Cached input zaroori hai:** Agent har turn wahi instructions/repo context resend karta hai — dono
providers repeated prefix pe **chhota fraction** charge karte hain jab cache hit ho.

**3 sawal, order mein:**
1. **Kya data bahar ja sakta hai?** Nahi → local ya server, kitne log serve karne hain uske hisaab se
2. **Kya task mid-size open model ke reach mein hai?** Haan → economics ka sawal hai
3. **Frontier brain chahiye?** Cloud tier — sasta default, mehnga proven-failure pe

### Self-Check
**Sawal:** Firm chahti hai agent jo confidential client contracts din bhar review kare. Tasks moderately
hard hain, mid-size model ke reach mein. Konsa tier?
**Jawab:** **Server tier.** Sawal 1 cloud ko rule out karta hai (confidential data bahar nahi ja sakti).
Laptop tier fail hota hai (all-day team loop throughput wall hit karti hai). vLLM machine firm ke network
ke andar throughput clear karti hai, data ghar rakhti hai, din-bhar loop sasti karti hai.

## Concept 16: Ek Router, Teeno Tiers — Claude Code Router

**Claude Code Router (CCR)** open source tool hai jo ek chhoti server chalata hai — Claude Code ki
native format ek taraf, kai providers doosri taraf. Config file decide karta hai **request by request**
kaunsa brain jawab de.

```json
{
  "Router": {
    "default": "openrouter,deepseek/deepseek-v4-pro",
    "background": "ollama,qwen3:8b",
    "think": "openrouter,moonshotai/kimi-k3",
    "longContext": "openrouter,moonshotai/kimi-k3",
    "longContextThreshold": 60000
  }
}
```

Ye Concept 15 ka rule **configuration ki tarah likha hua**: ordinary work → sasta frontier model. Cheap
background chores → apna laptop, free. Hard reasoning + huge contexts → Kimi K3.

```bash
ccr code                          # Router se Claude Code start karo
/model ollama,qwen3:8b            # session ke beech mein brain switch karo
```

> **2 honest notes:** CCR community project hai, koi vendor product nahi — update aur release notes
> parhte raho. Aur jahan zaroorat na ho wahan mat add karo — aapki vLLM server pehle se Claude Code ki
> format native boli bolti hai.

---
[⬅ Server Tier](01-server-tier.md) · [Agla: Appendix — Mini LLM Cloud ➡](03-appendix-mini-llm-cloud.md)
