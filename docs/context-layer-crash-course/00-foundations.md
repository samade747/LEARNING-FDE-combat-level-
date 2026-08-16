# 00 — Part 1: Foundations (Concepts 1-4)

## Concept 1 — Scope Jump: Ek Store Se Sab Ke Sources Tak

Aapka pichla store (Postgres) 4 properties rakhta tha jo aap ne kabhi notice nahi kiya: **aap ne har
cheez likhi thi.** **Ek hi reader tha.** **Ek hi kism ki truth thi.** **Yeh construction se current tha**
(sirf aapka worker likhta tha).

Jaise hi aap ek company connect karte ho, yeh chaaron gayab ho jate hain. Content unka hai (kuch ghalat,
kuch superseded). Ek junior aur ek partner ko same sawal ka **alag** jawab milna chahiye. Corpus mein ek
signed contract, ek policy memo, ek chat message, aur live invoice status — sab **bohat alag weight**
rakhte hain. Aur jo document Tuesday ko index hua, woh Wednesday ko kisi ne replace kar diya ho sakta hai
bina aapko bataye.

> **Pichla course retrieval problem tha. Yeh governance problem hai jo retrieval problem ke kapre pehne
> hai.**

## Concept 2 — 4 Source Classes

Is build ki sabse mehngi galti: har connected system ko ek undifferentiated dher ki tarah treat karna.
Kuch bhi connect karne se pehle inhe 4 classes mein baanto:

| Class | Examples | Kaise Ata Hai | Worker Cite Kar Sakta Hai? |
| --- | --- | --- | --- |
| **Agent Factory System of Record** | Shared method, standards | Web-indexed, canonical page ko cite | Haan, shared method ki tarah |
| **Vertical Systems of Record** | Northstar ke sales/accounting rules | Indexed for discovery, phir **confirmed** MCP se | Haan, governing rule ki tarah |
| **Customer operational records** | ERP, CRM, ledger, contract | Live typed query, kabhi index nahi | Haan, uski apni state ke liye, timestamp ke sath |
| **Customer working context** | Email, chat, files | Permission-aware indexing | **Evidence** ki tarah, kabhi rule ki tarah nahi |

**Pehli 3 authoritative hain**, alag alag sawalon par. **Sirf chauthi mein governing professional
authority nahi hai.** Yeh woh class hai jispar sab log sabse pehle search tool point karte hain — isiliye
itne pilots fluent jawab dete hain jinke peeche kuch nahi hota.

## Concept 3 — Onyx Kya Hai (Aur Kya Nahi)

**Onyx** open-source AI chat hai jo aapke docs, apps, logon se connect hota hai. Yeh course isay **System
of Context** ka open reference implementation ki tarah treat karta hai.

**3 cheezein jo yeh nahi hai:**

- **Yeh aapka System of Record nahi hai.** Onyx dhoondne ke liye copies rakhta hai. Aapka governed record
  cite karne ke liye originals rakhta hai.
- **Yeh permission system nahi hai.** Jahan support ho wahan permissions inherit karta hai, aapke
  profession ke controls ka apna kuch enforce nahi karta.
- **Yeh answer nahi hai.** Retrieval hit ek **pointer** hai. "Yahan dekho" bolta hai.

> **Caution: Model bhi source nahi hai.** Aapka Worker ek language model par chalta hai, aur woh model
> professional sawal ka jawab **apne knowledge se** de dega agar retrieval kuch na de. Output bilkul
> grounded answer jaisa dikhta hai. Koi error nahi ata. Model ke paas koi source nahi — sirf weights hain.
> **Plausibility provenance nahi hai.**

**Onyx vs Lite:** **Standard** install karo, Lite nahi — Lite vector index, background workers, aur
poori infrastructure disable kar deta hai jo yeh course sikhata hai.

```text
Read the current official Onyx Quickstart and Resourcing pages... Install
the latest stable Onyx Community Edition in Standard mode... Do not
choose Lite. Show me the plan and the resource check before starting
any container.
```

**Resource warning:** kam RAM par (4GB) Onyx failures software bugs jaisi dikhti hain lekin asal mein
resource problem hoti hain. Minimum: 4 vCPU, 10GB RAM.

## Concept 4 — Onyx: Glean Se Farq

**Glean** commercial System of Context hai — market ne yeh naam popularize kiya. Is course ka rule:

> **Hum woh sikhate hain jo aap khol sakte ho. Aap woh deploy karoge jo customer ne already khareed rakha
> hai. Architecture dono mein same hai — aur yehi hissa aapka hai.**

**Kyun Onyx, Glean nahi:** (1) Control tab tak seekh nahi sakte jab tak khud na banao. (2) Closed box
architecture nahi sikhati. (3) **Poore course ka zyada tar hissa product ke baare mein hai hi nahi** —
7 cheezein jo aap banate ho na Onyx na Glean decide karta hai, kyunki woh professional judgment hain,
platform features nahi.

---
[⬆ Index](README.md) · [Agla: Pehla Corpus ➡](01-first-corpus.md)
