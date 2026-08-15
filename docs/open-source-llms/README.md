# Open Source LLMs — Notes (Roman Urdu + English)

Ye notes **"Open Source LLMs: Your Laptop, Your Server/Cluster, the Cloud"** chapter ka easy explainer
hain (position #2), Panaversity ke **The AI Agent Factory** book se (Zia Tutor AI connector ke zariye).

Source: https://agentfactory.panaversity.org/docs/using-open-source-llms

## Index

1. [00 — Local Tier: Laptop Pe Model (Ollama)](00-local-tier.md)
2. [01 — Server Tier: Ek Machine, Kai Users (vLLM)](01-server-tier.md)
3. [02 — Cloud Tier: Frontier Models (OpenRouter)](02-cloud-tier.md)
4. [03 — Appendix: Apna Mini LLM Cloud Banao](03-appendix-mini-llm-cloud.md)

## Ek Line Mein Poori Cheez

> **Har AI tool ke 2 parts hain: Harness (jo hands-on kaam karta hai) aur Brain (model, jo sochta hai).**
> Harness brain ko ek **address** pe reach karta hai. Ye course sikhati hai ke wahi address 3 alag jagah
> point kar sakta hai — **aapka laptop** (Ollama), **aapki machine** (vLLM), ya **cloud** (OpenRouter) —
> aur **harness kabhi farq nahi janta.**

## 3 Tiers

| Tier | Serving Layer | Scale | Address |
| --- | --- | --- | --- |
| **Local** | Ollama | 1 banda, 1 laptop | `localhost:11434` |
| **Server** | vLLM | Kai users, 1 machine | `localhost:8000` |
| **Cloud** | OpenRouter | Frontier models jo koi self-host nahi kar sakta | `openrouter.ai` |

## 2 Deewarein Jo Har Local Setup Face Karti Hain

- **Capability wall** — sahi tool call likhna (strong model se fix hoti hai)
- **Throughput wall** — lambi instruction jaldi parhna (GPU se fix hoti hai)
