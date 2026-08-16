# 03 — Part 4: Routing Aur Citing (Concepts 12-15)

> **Aasan lafzon mein:** Ek customer sawal aksar kai professional sawal chhupaye hote hain. Yeh part
> Worker ko sikhata hai unhe alag karna, har ek ko governing record tak bhejna, aur jo wapis aaye usay
> label karna. Aur sabse mushkil habit: jab do sources disagree karein, **dono dikhao.** Ek comfortable
> sentence mein blend mat karo.

## Concept 12 — Authority Routing: Kaunsa Record Governs Karta Hai

Zyada tar evidence requests 3 shapes mein reduce hote hain:

| Sawal | Source | Path | Kya Wapis Ata Hai |
| --- | --- | --- | --- |
| Rule kya hai? | System of Record | Discovery, phir confirmation | Governed truth |
| Number kya hai? | System jo owns karta hai | Typed query | Ek exact, timestamped value |
| Is case ke baare mein kya kaha gaya? | Working context | Permission-aware retrieval | Evidence, kabhi rule nahi |

Ek aur step: pehle decide hota hai **kaunsi profession** is sawal ko own karti hai, phir kaunsa source
uske andar.

**Map likho prompt likhne se pehle** (`governance/authority-map.yaml`):

```yaml
routes:
  accounting.implementation_revenue:
    questions: [revenue recognition, implementation acceptance]
    governing_source: VERTICAL-ACCOUNTING-SOR
    confirm_with: vertical-sor.confirm_rule(domain=accounting)
    current_state_tool: customer-state.get_contract_state

rules:
  - working_context may support what was said, but never governs a conclusion
  - conflicts are surfaced, never silently merged
```

**Done jab:** Northstar question kam az kam 2 routed decisions banaye (ek sales, ek accounting), har ek
apna governing source naam le, kisi retrieval se pehle.

## Concept 13 — Provenance Aur Citation Envelope

Har item jo layer return kare, ek **envelope** carry karta hai:

| Field | Kyun Matter Karta Hai |
| --- | --- |
| Source system | Kaun owns karta hai |
| Stable ID | Reviewer dobara fetch kar sake |
| Authority class | Law, standard, contract, policy, transaction, guidance, message, example |
| Version + effective period | Retired rules chupke se wapis na aayein |
| Permission basis | Yeh reader kyun allowed tha |

> **Worker koi bhi permitted, task-relevant context parh sakta hai. Lekin usay kabhi *rule* ki tarah
> present nahi kar sakta.**

**Caution:** Document Set ko Agent se directly attach mat karo — yeh 2 retrieval paths banata hai, ek
gate ko bypass karta hai. **Router ko koi role-sensitive knowledge attach nahi hoti — sirf Actions.**

5 Actions:

| Action | Kya Karta Hai |
| --- | --- |
| `search_permitted_context(query)` | Gateway — role credential se resolve karta hai, tool argument se nahi |
| `confirm_rule(domain, stable_id)` | Canonical confirmation |
| `get_opportunity(id)` | Live opportunity state |
| `get_contract_state(id)` | Live contract state |
| `validate_action(domain, action)` | Proposal ko rules ke against check karta hai |

> **Sab indexed retrieval gateway se guzarti hai. Agar koi component gateway ke bina search kar sake,
> gate decoration hai.**

**7-Section Packet** (fixed shape jo output contract hai):
```text
## Decisions involved
## Governing authority
## Current facts
## Supporting context
## Conflicts and gaps
## Permitted next steps
## Citations
```

**Empty *Conflicts and gaps* matlab router ne check kiya aur koi nahi mila. Koi heading hi nahi matlab
usne kabhi dekha hi nahi.**

> **Caution: Compression provenance ko marta hai.** Prose compress karo. Provenance kabhi compress mat
> karo.

## Concept 14 — Conflict Ek Result Hai, Retrieval Failure Nahi

Conflict ke 3 outcomes:

- **Resolved by scope** — sources alag sawal ka jawab de rahe hain, dono apni jagah sahi hain
- **Resolved by authority** — ek applicable source governs karta hai
- **Unresolved** — Worker escalate karta hai, conflicting evidence organized ke sath

**Chautha jo kabhi nahi hona chahiye:** sources ko ek smooth sentence mein blend karna jo koi source ne
kaha hi nahi.

> **Yeh disagreement gayab nahi karta. Yeh disagreement ko reviewable banata hai.**

## Concept 15 — Act Aur Record: Loop Band Karna

```text
layer dhoondta hai  →  Worker reason karta hai  →  governing record validate karta hai
                     →  tool act karta hai  →  owning system record karta hai
```

Teesra step woh hai jo har koi drop karta hai. Governing record sirf woh nahi jahan rule parhi gayi —
yeh woh jagah hai jahan **proposed action** us rule ke against check hoti hai. **Yehi check rule ko real
banata hai, advisory nahi.**

> **Context layer kabhi doosra transaction system nahi ban sakta, aur kabhi governed record ke around
> likhne ka tareeqa nahi ban sakta.**

Read, recommend, prepare, execute — alag grants hain. **Access permission nahi hai.**

**Done jab:** Discount recommendation sales rule ke approval rule se refuse ho, aur refusal rule ka naam
le — "model unsure tha" nahi.

---
[⬅ Governed Half](02-governed-half.md) · [⬆ Index](README.md) · [Agla: Northstar Case ➡](04-northstar-case-and-proving.md)
