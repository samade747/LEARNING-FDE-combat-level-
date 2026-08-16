# 02 — Part 3: The Governed Half (Concepts 10-11)

> **Aasan lafzon mein:** Searching aapko pointer deti hai. Answer nahi deti. Yahan doosra hissa add hota
> hai: aapke apne Neon database mein ek chota governed rules table, version aur date ke sath. Phir aap
> isay tool ki tarah serve karte ho taake Worker index mein mili rule ko original se check kar sake:
> **kya yeh abhi bhi rule hai?**

## Concept 10 — Apna Record MCP Par Serve Karo: Two-Call Pattern

Ab tak sab **indexed discovery half** tha. Sab kuch *searchable copy* ki tarah aya, aur copy ek pointer
hai. Ab **canonical aur live half** ata hai — bilkul alag tareeqe se.

**Pehle, record ko authority do:** Neon project mein ek chota `governed` schema banao — `rule` table
jisme `stable_id`, `domain`, `authority_class`, `jurisdiction`, `version`, `effective_from/to`,
`approval_status`, `superseded_by`, `owner`, `body` columns hon.

**Phir serve karo:** Yeh koi crawl-hone-wala folder nahi hai — **kabhi connector point mat karo.** Yeh
ek **poocha jaane wala** source hai:

```text
Wrap our Neon-hosted governed record in a FastMCP server called
vertical-sor. Three read-only tools:
- search_rules(domain, query) — candidate rules deta hai
- confirm_rule(domain, stable_id) — full current entry deta hai
- validate_action(domain, action) — proposed action ko rules ke against check karta hai
Use the pooled Neon connection string, connect with a read-only role,
serve over Streamable HTTP in stateless mode.
```

**Discovery aur confirmation do alag calls hain, aur yeh farq hi poora point hai:**

- **Discovery poochta hai:** relevant information kahan ho sakti hai? Recall, similarity, speed ke liye
  optimize. Output: **pointer.**
- **Confirmation poochta hai:** kaunsa source officially applicable hai? Domain, authority class,
  jurisdiction, version, effective date, approval status check karta hai. Output: **answer.**

```text
search discovers  →  aap route karte ho  →  record confirm karta hai  →  Worker cite karta hai
```

> **Discovery kabhi confirmation nahi hoti.** Aap governed pages ko discovery ke liye index kar sakte ho
> — lekin **copy par kabhi rely mat karo.**

**Demonstration jo course ki sabse valuable cheez hai:**

```text
Create a Neon branch of our record, change the implementation-revenue
rule on the default branch from acceptance to billing so it's stale...
point search_rules at the stale branch while confirm_rule stays on the
current one, and ask when revenue may be recognised. Show me both
answers side by side.
```

**Done jab:** Aap ne stale branch ko confidently "*at billing*" bolte dekha, aur confirmation call usay
"*at acceptance*" correct karte dekha. **Ek jawab se Northstar is quarter revenue book kar sakta hai,
doosre se nahi — yehi poore course ka farq hai.**

## Concept 11 — Live State Har Baar Poocha Jata Hai

Balances, approval status, current versions — kuch bhi authored nahi, kuch bhi stable nahi, sab exact
hai. Isay index karo to aap us cheez ki purani copy bana rahe ho jiski poori value **current hona** hai.

> **Agar stale value conclusion, permission, payment, ya customer action badal sakti hai — live fetch
> karo.**

**3 Retrieval Modes:**

| Information | Kaise Pahunchte Hain |
| --- | --- |
| Working context | Permission-aware indexing |
| Governed knowledge | Discovery index, **confirmed** honi chahiye |
| Current records/actions | Live typed query, MCP/API par |

> **Working context index karo. Governed knowledge discover karo. Current truth live query karo.**

Format aur length kuch decide nahi karte. **Freshness risk sab kuch decide karta hai.**

```text
Serve Northstar's two operational records through the customer-state
server, separate from vertical-sor... Then ask "may we recognise the
revenue" twice, once from indexed snapshot, once from live call,
flipping acceptance from not-received to received in between.
```

**Done jab:** Indexed answer aur live answer disagree karein, aur aap exactly bata sako controller ko
kaunsa dena hai.

---
[⬅ Pehla Corpus](01-first-corpus.md) · [⬆ Index](README.md) · [Agla: Routing Aur Citing ➡](03-routing-and-citing.md)
