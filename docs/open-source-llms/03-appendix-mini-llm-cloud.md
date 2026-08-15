# 03 — Appendix: Apna Mini LLM Cloud Banao

Part 2 ne industrial kitchen di. **Kitchen restaurant nahi hoti.** Ye appendix front door, menu, table
numbers, aur bill add karti hai.

## A1: Kitchen Restaurant Nahi Hai

Bare vLLM server: koi bhi jo port reach kare, use kar sakta hai — free, hamesha ke liye.

| Zaroorat | vLLM Karta Hai? |
| --- | --- |
| Tokens tez serve karna | **Haan** |
| Kaun call kar raha hai jaanna | Nahi |
| Spending limit pe kaat dena | Nahi |
| Har user ka record rakhna | Nahi |
| Ek address pe multiple models | Nahi |

**Inference engine** (vLLM) tokens serve karta hai. **Gateway** logon ko jaanta hai: kaun, kya use kar
sakta hai, kitne ka.

## A2: Gateway — Ek Address, Kai Brains, Real Users

**LiteLLM** — open source proxy jo OpenAI-compatible shape users ko deta hai, aur bahar providers ko
translate karta hai.

**4 zaroori cheezein:**
- **Virtual keys** — har student ki apni key
- **Budgets + rate limits** — spending cap + per-minute limit
- **Ek address pe menu** — local + cloud models saath
- **Records** — kis ne kya spend kiya

> Gateway **control tool** hai, **performance tool nahi**.

## A3: Poora Stack Ek File Mein

**4 containers:** vLLM (tokens serve), LiteLLM (gateway), Postgres (keys/spending survive restart),
Open WebUI (chat page).

```yaml
# litellm-config.yaml
model_list:
  - model_name: qwen3-8b
    litellm_params:
      model: hosted_vllm/Qwen/Qwen3-8B
      api_base: http://vllm:8000/v1
general_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
  database_url: os.environ/DATABASE_URL
```

```bash
docker compose up -d
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -d '{"model": "qwen3-8b", "messages": [{"role": "user", "content": "Say hello"}]}'
```

> **Zaroori security warning:** March 2026 mein LiteLLM package supply-chain attack ka shikar hua.
> **Exact version pin karo, `latest` track mat karo.** Gateway aapki poori cloud ki keys rakhta hai —
> sab se high-value target.

## A4: Keys Do — Budgets, Limits, Kisne Kya Kharch Kiya

```bash
curl -X POST http://localhost:4000/key/generate \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -d '{"user_id": "student-0417", "models": ["qwen3-8b"], "max_budget": 2.00, "budget_duration": "30d", "rpm_limit": 20}'
```

**4 settings, har ek jaan-boojh kar:** `user_id` (har dollar ek insaan se linked), `models` (menu jo ye
key order kar sakti hai), `max_budget` (cap — runaway loop khud ruk jati hai), `rpm_limit` (ek student
sab ke liye queue na bhar de).

Student aapki cloud ko **bilkul waisay** use karta hai jaise Part 3 OpenRouter use karta tha — sirf naya
address.

## A5: Teeno Tiers Ek Darwaze Ke Peeche

```yaml
model_list:
  - model_name: qwen3-8b       # Tier 2, apna GPU
    litellm_params:
      model: hosted_vllm/Qwen/Qwen3-8B
  - model_name: frontier       # Tier 3, rented
    litellm_params:
      model: openrouter/moonshotai/kimi-k3
      api_key: os.environ/OPENROUTER_API_KEY
router_settings:
  fallbacks:
    - qwen3-8b: ["frontier-cheap"]
```

**3 zaroori cheezein:** Aapki OpenRouter key **kabhi machine se bahar nahi jati** — students aapki
gateway key use karte hain. **Tier choice ek model name ban gaya** — `frontier` type karo, hard task ke
liye. **Fallback line ek policy hai** — GPU down ho to chup chaap cloud pe switch, availability money se
kharidi.

## A6: Watch Karo — 3 Numbers Jo Health Batate Hain

- **Queue depth** — kitni requests wait kar rahi hain (near-zero = coasting, climbing = GPU khatam)
- **Time to first token** — user kitna wait karta hai pehla token dekhne ke liye
- **GPU memory in use** — memory compute se pehle bharti hai

> **Simple:** Queue depth darwaze ki line hai. Time to first token har diner ka wait hai. GPU memory
> kitchen kitni bhari hai.

## A7: Kab Kaam Ki Hai, Kab Graduate Karein

**Banao jab:** kai users + ek budget (classroom, department), data bahar nahi jani chahiye, ek stable
address chahiye badalti duniya ke aage, loops din bhar chalti hain.

**Mat banao jab:** aap akele ho (seedha vLLM use karo), traffic chhoti/occasional hai (Part 3 rent karo,
weekends bacha lo), **koi ise own nahi karta** (service ko koi responsible chahiye jab wo toote).

**Docker Compose se aage kab jayein:** Jab load justify kare, **vLLM production stack** (Helm chart) ya
**KubeAI** pe move karo — same pieces, bigger scale. Gateway layer wahi rehta hai.

> **Appendix ek line mein:** Inference engine tokens serve karta hai, gateway logon ko serve karta hai.
> Mini LLM cloud sirf ye 2 programs + keys rakhne ki jagah hai. **Jo bhi aapke address pe point kare
> uske liye, aap ab cloud hain.**

---
[⬅ Cloud Tier](02-cloud-tier.md) · [⬆ Index](README.md)
