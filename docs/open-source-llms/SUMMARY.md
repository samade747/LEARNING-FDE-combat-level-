# Open Source LLMs — Summary

Har AI tool ke 2 parts: **Harness** (hands-on kaam) aur **Brain** (model). Harness brain ko ek **address**
pe reach karta hai — wahi address 3 jagah point kar sakta hai: laptop (Ollama), server (vLLM), cloud
(OpenRouter) — harness kabhi farq nahi janta. 2 deewarein har local setup face karti hai: **capability**
(sahi tool call — strong model se fix) aur **throughput** (fast reading — GPU se fix).

## 00 — Local Tier: Laptop Pe Model (Ollama)

- **Concept 1:** `ollama run gemma3:4b` — WiFi band karke bhi kaam karta hai, kuch bhi bahar nahi jata.
  `localhost` = "yehi computer."
- **Concept 2:** Brain sirf address hai (phone-number analogy) — local brain **alag** brain hai, pehle
  wale ki chhoti copy nahi.
- **Concept 3:** `ollama launch claude/opencode --model`. Claude Code = bare address (`ANTHROPIC_BASE_URL`,
  no `/v1`); OpenCode = `/v1` required in `opencode.json` provider config.
- **Concept 4:** Real task test — strong machine par clean change, plain laptop par ruk jata hai ya minutes
  leta hai.
- **Concept 5 — 2 Deewarein:** Capability (tool-use-trained model chahiye, hardware se fix nahi) vs
  Throughput (GPU chahiye, smarter/chhota model se fix nahi). Model guide: `llama3.2:3b` (tool calls
  mangle karta) < `qwen3:8b` (simple tasks OK) < `qwen3:30b-a3b` (best balance).
- **Concept 6:** Healthy tool call = structured JSON; kamzor model text bhejta hai, harness reject karta
  hai. Context window trap: default sirf 4,096 tokens (chup chaap trim) — `num_ctx` ko 64,000+ set karo.
- **Concept 7:** Brain own karna kab kaam ki — privacy, offline, cost (din-bhar-chalti loops ke liye
  sasta). Limit: sirf ek customer serve karta hai — Part 2 ka setup.

## 01 — Server Tier: Ek Machine, Kai Users (vLLM)

- **Concept 8:** `bench.py` se concurrency-1-vs-50 sweep — Ollama flat rehta hai (design choice, ek insaan
  ke laptop ke liye, restaurant ke liye nahi — `OLLAMA_NUM_PARALLEL`).
- **Concept 9:** vLLM = industrial kitchen, kai users ek saath. 2 tricks: continuous batching, PagedAttention.
  `vllm serve` + `--enable-auto-tool-choice` + parser flags (bagair inke coding agents chup chaap fail
  hoti hain). 16GB card → FP8 compressed build.
- **Concept 10:** Same sweep — Ollama flat, vLLM chadhti curve (GPU bharne tak). Self-check: vLLM ek user
  ke liye tez nahi karta, load ke neeche machine ko tez karta hai.
- **Concept 11:** Same wiring naya port (`:8000`), sharing warning — kam se kam `--api-key` set karo jab
  machine kisi aur ko serve kare.
- **Concept 12:** Kab kaam ki — team/classroom, din-bhar loops (per-token bill nahi rukta), team-scale
  privacy. Honest limit: **sirf throughput** wall move hoti hai, model utni hi smart — capability wall ke
  liye cloud tier chahiye.

## 02 — Cloud Tier: Frontier Models (OpenRouter)

- **Concept 13:** Open weights jo utha nahi sakte — Kimi K3 (2.8T params, performance, 64+ chips chahiye)
  vs DeepSeek V4 Pro (1.6T/~49B active, price-performance, MIT, 8-16 GPUs). "Open" 3 cheezein deta hai:
  no lock-in, choice of landlord, floor under future. OpenRouter = gateway (1 address/key/bill).
- **Concept 14:** Same wiring pattern (`ANTHROPIC_BASE_URL=openrouter.ai/api`). Ehtiyat: Claude Code sirf
  Anthropic models pe fully tested — OpenCode/CCR full-supported path hai non-Anthropic ke liye.
- **Concept 15:** Kimi K3 ($3 in/$15 out) vs DeepSeek V4 Pro ($0.44/$0.87, ~17x sasta output pe). Working
  rule: price-performance default, escalate sirf real-failure-se-trigger. Cached input zaroori (repeated
  prefix chhote fraction pe). 3 sawal order mein: data bahar ja sakta? → mid-size model reach mein? →
  frontier chahiye?
- **Concept 16:** Claude Code Router (CCR) — ek config file se request-by-request routing (default/
  background/think/longContext tiers). `ccr code`, `/model` mid-session switch. Honest notes: community
  project, add-only-when-zaroorat-ho.

## 03 — Appendix: Apna Mini LLM Cloud Banao

- **A1:** vLLM akela = kitchen, restaurant nahi (koi identity/spending-limit/records/multi-model
  awareness nahi). Inference engine (vLLM) vs Gateway (logon ko jaanta hai) ka farq.
- **A2:** LiteLLM (open-source proxy) — virtual keys, budgets+rate limits, ek address pe menu, spending
  records. Gateway = control tool, performance tool nahi.
- **A3:** 4-container stack (vLLM + LiteLLM + Postgres + Open WebUI), `litellm-config.yaml` example,
  `docker compose up`. **Security warning:** March 2026 LiteLLM supply-chain attack — exact version pin
  karo, `latest` track mat karo.
- **A4:** Keys generate karna — `user_id`, `models`, `max_budget`, `rpm_limit` (4 jaan-boojh-kar settings).
- **A5:** Teeno tiers ek darwaze ke peeche — model_list mein Tier 2 (apna GPU) + Tier 3 (rented frontier)
  + fallback policy (GPU-down → chup-chaap-cloud). OpenRouter key kabhi machine se bahar nahi jati.
- **A6:** Health metrics — queue depth, time-to-first-token, GPU memory in use.
- **A7:** Banao jab (multi-user+budget, data-must-stay-in, stable address, all-day loops); mat banao jab
  (akele ho, occasional traffic, koi owner nahi). Scale-up path: Docker Compose → vLLM production stack/
  KubeAI.
