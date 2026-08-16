# 04 — Part 4: Composition Rules — Kab Kaunse Protocols Use Karein (Concepts 12-14)

## Concept 12 — Minimum Viable Agent-Payment Stack

**Ek line mein:** Sahi stack woh sabse chota protocols ka set hai jo ek use case ke liye value ship
kare, har layer par sab 4 protocols nahi.

Kuch bhi compose karne se pehle ek sawal pucho: **yahan sabse chota stack kya hai jo value ship kare?**
Jawab almost kabhi "sab 4 protocols, har layer" nahi hota.

**Har common use case ke liye sabse chota stack:**

| Use Case | Discovery | Auth | Commerce | Settlement | MVP Kyun |
| --- | --- | --- | --- | --- | --- |
| **Consumer shopping** | AI shopping surface / MCP catalog | ACP SPT (ya regulated fields mein AP2) | ACP | Card rails via Stripe | Zyada tar buyers chargeback cover chahte hain |
| **API-paying agent** | MCP + x402 support / Agent.market | EIP-3009 signature | None (direct API call) | x402 (Base/Solana) | Machine-to-machine ke liye Layers 2+4 collapse ho jate hain |
| **Enterprise procurement** | A2A discovery partner network mein | AP2 Intent Mandate (audit ke liye required) | ACP/UCP catalog suppliers, direct API service buys | MPP sessions recurring, ACP SPT one-off | Audit trail skip nahi ho sakta |
| **Multi-agent marketplace** | A2A / agent directory | AP2 mandate + ERC-8004 reputation | None (direct agent-to-agent) | x402 (usually), ya MPP Stripe already wired ho to | Trust dono directions mein chalta hai |

**Composition rule:** har layer par woh protocol chuno jo use case demand kare. Jo layers use case
touch hi nahi karta unpar protocols add mat karo. Pure API-paying agent ko ACP nahi chahiye. Consumer-
shopping agent ko $50 t-shirt ke liye x402 nahi pakarna chahiye — card ki chargeback cover 2.9% fee
worth hai.

**Trap:** kuch teams ACP, AP2, x402, MPP sab ek sath wire karti hain "flexibility ke liye." 4x
integration surface milta hai aur "kaunsa protocol kab fire hota hai" ka koi clear jawab nahi. **Ek
stack chuno. Ship karo. Doosra stack tab add karo jab doosra use case usay demand kare.**

## Concept 13 — Protocols Kab Layers Ke Across Compose Hote Hain, Kab Ek Layer Ke Andar Compete Karte

**Ek line mein:** 2 alag layers wale protocols sath stack hote hain; 2 same layer wale ek doosre ko
replace karte hain. **Kisi bhi pair ke baare mein sirf ek sawal poochna hai: kya woh same layer par hain?**

**Layers ke across, compose hone ke liye banaye:**

| Composition | Layer Mapping | Kahan Ship Hota Hai |
| --- | --- | --- |
| AP2 + ACP | AP2 Layer 2 (audit-grade auth), ACP Layer 3 (commerce) | Regulated fields jahan ACP ke normal flow ko extra audit chahiye |
| AP2 + x402 | AP2 Layer 2 (mandate auth), x402 Layer 4 (stablecoin settlement) | Crypto-native flows jinhe audit bhi chahiye, `a2a-x402` extension se |
| ACP + x402 | ACP Layer 3, x402 Layer 4 machine-to-machine sub-flows ke liye | Hybrid platforms — consumer buy mein kuch API spend shamil |
| MCP + x402 (`withX402Client`) | MCP Layer 1, x402 Layer 4 | Cloudflare ka standard pattern paid MCP tools ke liye |

**Ek layer ke andar, compete karne ke liye banaye:**

| Competition | Layer | Kaun Jeetta Hai |
| --- | --- | --- |
| AP2 vs ACP SPT vs TAP | Layer 2 | AP2 audit-grade flows; ACP SPT Stripe-wired consumer flows; TAP identity-only |
| ACP vs UCP | Layer 3 | ACP ChatGPT reach; UCP Gemini reach; dono cross-surface sellers ke liye |
| x402 vs MPP | Layer 4 | x402 one-off micropayments/pure stablecoin; MPP sessions/subscriptions/multi-rail |

**Test:** jab 2 protocols ke darmiyan fasein, ek sawal pucho: kya woh same layer par hain? Haan to ek
chuno (ya dono support karo alag sub-flows ke liye). Nahi to probably compose hote hain.

**Worked composition — AP2 + x402 stack** (crypto-native pattern, B2B/agent-to-agent flows mein
common):
```
Layer 1 (Discovery): A2A directory partner network ke andar
Layer 2 (Auth):      AP2 Intent + Cart + Payment Mandates
Layer 3 (Commerce):  Often none, ya ACP catalog ke liye
Layer 4 (Settlement): x402, a2a-x402 extension ke through
```

## Concept 14 — Cost Aur Latency: Kya Choice Force Karti Hai

**Ek line mein:** Transaction size aur acceptable wait settlement protocol decide karte hain — card
fees chote payments ko crush karte hain, slow checkouts tight loops tor dete hain.

**Composition ke hisab se cost per transaction:**

| Composition | Typical Cost | Typical Latency |
| --- | --- | --- |
| ACP + card rails | 2.9% + $0.30 | 5-30 seconds |
| ACP + MPP sessions | 2.9% cards, ~0.5% Tempo stablecoin | 1-3 sec per metered call |
| AP2 + x402 | Sub-cent gas, zero protocol fees | 2-5 sec (mandate signing +1-3) |
| x402 only | Sub-cent gas, zero fees | 1-2 sec |
| MPP sessions only | Near-zero Tempo, Stripe rate cards | 50-500 ms per metered call |

**Paisa kya force karta hai:** ~5% se zyada fees problem hain. $0.05 API call jo 2.9%+$0.30 card fees
pay kare, call se zyada fees mein kharch karta hai — x402/MPP stablecoin ki taraf clear signal. $5-$10
wahan line hai jahan card rails maane nahi rakhte — neeche machine-payment rails jeetein, upar
chargeback cover fee worth hai.

**Latency kya force karti hai:** user-facing step par 5 second se zyada wait problem hai. AP2 mandate
signing 1-3 sec add karti hai, human signature wait kare to bohat zyada. Agent-to-agent flows (no
human) ke liye budget aur tight hai, often sub-second — x402 on Base aur MPP on Tempo default hain.

**Decision tree, compressed:**
```
Transaction value?
├── Sub-dollar → x402 only, ya MPP sessions
├── $1-$10 → x402/MPP, AP2 audit chahiye ho to
├── $10-$1,000 → ACP + card rails (chargeback cover fee worth hai)
└── $1,000+ → AP2 + ACP/UCP + MPP sessions, ya bank rails

Latency budget?
├── Sub-second → MPP on Tempo, ya x402 on Base
├── 1-5 sec → x402/MPP; AP2 sirf pre-signed mandates ke sath
└── 5+ sec → Poora ACP checkout kaam karta hai
```

---
[⬅ 4 Protocols In Depth](03-four-protocols.md) · [⬆ Index](README.md) · [Agla: Decision Lab ➡](05-decision-lab.md)
