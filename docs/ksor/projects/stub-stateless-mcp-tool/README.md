# KSoR Project 2 — Stub Stateless MCP Tool

**Concept:** Section 10 (Agent Surface — MCP), Section 5 (Abstention Is a Feature) · **Time:** 30-45 min ·
**Difficulty:** Easy-Medium

Ek minimal Python "MCP-shaped" tool-call handler — no real MCP SDK, no server — jo `search` aur
`retrieve` requests ko stateless tarike se handle karta hai (har call corpus disk se reload karta
hai, koi session/history nahi rakhta), aur **abstain karta hai jab koi match na ho**, guess nahi
karta.

## Files

- `corpus.json` — 3-document fixture corpus (2 authority, 1 orientation)
- `mcp_tool.py` — `handle_request(request: dict) -> dict`, tool shapes `search` aur `retrieve`
- `test_client.py` — 5 scripted calls jo hit/abstain/statelessness verify karte hain

## Kaise Chalayein

```bash
python test_client.py
```

## Trip Karo (jaan-boojh kar break karo)

`mcp_tool.py` mein `search`'s "no hits" branch ko badal do taake woh koi bhi random document return
kare (guess) instead of abstain karna. Phir `test_client.py` chalao — dekho `r2` ka check fail hota
hai, kyunke ab handler guess kar raha hai jahan usay "yeh maloom nahi" kehna chahiye tha.

## Done Jab (Self-Check)

- [ ] `test_client.py` clean pass karta hai (5/5 checks)
- [ ] `search` sirf `authority_class: "authority"` documents ko hits mein return karta hai, `about-001`
      (orientation) kabhi hit nahi hota
- [ ] Guess-fallback jaan-boojh kar add kar ke dekha — test suite ne pakra
- [ ] Farq bata sako: yeh "retrieval" hai (RAG jaisa), lekin KSoR khud RAG nahi — `docs/ksor/02-architecture-and-tooling.md`
      ka "Retrieval Asal Product Nahi Hai" section dekho kyun

---
[⬆ KSoR Practice Projects](../README.md) · [⬆ KSoR Index](../../README.md)
