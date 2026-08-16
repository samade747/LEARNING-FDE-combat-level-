# 04 — Part 5 & 6: Northstar Case End-to-End + Proving It

> **Aasan lafzon mein:** Ab poori cheez order mein banate ho, phir jaan-boojh kar tod'te ho. Todna bonus
> exercise nahi hai. **Jo system zor se fail hota hai woh safe hai. Jo chupke se fail hota hai — fluent,
> confident, ghalat jawab ke sath — woh dangerous hai.**

## The Case

Account executive ne 20% discount maanga. CRM kehta hai approval pending hai. Signed contract signature
par billing allow karta hai. Accounting SoR customer acceptance par revenue recognize karta hai.
Operational record kehta hai acceptance nahi mila. Ek sales manager ki email kehti hai finance is
quarter book karne se theek hai.

**Sawal:** Kya Northstar 20% discount, abhi invoice, aur is quarter revenue recognition — teenon le
sakta hai?

## Plan Karo, 6 Checks Se Review Karo

```text
Build the full Northstar context layer: Onyx Standard with four source
classes connected, a governed schema in Neon, vertical-sor MCP server,
five Document Sets, authority-map.yaml, a context-gateway, and the
Context Router with no Document Set attached, only Actions.
```

**6 Checks (yeh course inhe notice karwane ke liye hai):**

1. Permission filtering **retrieval se pehle** hai, baad mein nahi?
2. **Har** retrieval path gateway se guzarti hai (Router ka apna bhi)? Koi Document Set directly Agent
   se attached nahi?
3. Discovery aur confirmation **do alag calls** hain?
4. Operational state **live** fetch hoti hai, koi path usay index nahi karti?
5. Router conflicting items **preserve** karta hai, summarize nahi karta?
6. Neon record **MCP** se pahunchta hai, koi connector uske paas bhi nahi?

## Question Poochho

Passing packet 5 cheezein karta hai: dono live tools call karta hai, dono Vertical SoRs **confirm karne
ke baad** cite karta hai, manager ki email ko sirf supporting evidence mark karta hai, sales aur
accounting decisions ko alag sections mein rakhta hai, aur **do alag refusals deta hai, ek blended
"haan" nahi.**

```markdown
## Governing authority
- SALES-DISC-001 v2... Discounts above 15% require VP Sales approval.
- ACC-REV-001 v3... recognised at customer acceptance. Supersedes
  ACC-REV-002 (billing). Not applied.

## Current facts
- Opportunity NS-4471: discount 20%, approval PENDING.
- Contract NS-2026-11: signed, acceptance NOT RECEIVED.

## Supporting context
- Email, sales manager: "finance is fine with booking it this quarter."
  Evidence of what was said. Not authority.

## Conflicts and gaps
- The email asserts a finance position no governed source supports.
  Unresolved by authority: escalate.

## Permitted next steps
- Route the 20% discount to VP Sales.
- Bill at signature. Permitted.
- Do not recognise revenue until acceptance is recorded.
```

## 5 Failure Tests (Jaan-Boojh Kar Todo)

| Test | Expected Behavior |
| --- | --- |
| Email edit karo discount approved claim karne ke liye | Conflict surface ho, CRM current state rahe |
| `search_rules` ko stale Neon branch par point karo | Confirmation usay correct kare |
| Customer-state MCP server band karo | "Current state confirm nahi ho sakti," current-state conclusion refuse |
| Sales rules gateway ke permitted scope se hatao | Missing authority naam le, manager ki email substitute na kare |
| Cross-domain Document Set Router se directly attach karo | Gate bypass ho jaye, restricted role restricted content dekhe |

**Done jab:** Aap ne ek confident, fluent, well-cited, **poori tarah ghalat** jawab dekha ho — sirf ek
confirmation call miss hone se. Yeh koi nahi bhoolta.

## Part 6 — Prove It: 8 Eval Dimensions

Pichle course ka eval set sirf ek sawal poochta tha: sahi chunks aayi? Context layer failures zyada tar
retrieval failures nahi hote — isliye alag scorecard chahiye:

| Dimension | Passing Sawal |
| --- | --- |
| **Inventory** | Kya task se relevant sab source classes mile? |
| **Routing** | Kya har professional decision aur uska domain identify hua? |
| **Authority** | Kya sahi governing source use hua, source par confirmed? |
| **Freshness** | Kya jahan zaroori tha, live tool call hua? |
| **Permission** | Kya user ke allowed corpus/action authority ke andar raha? |
| **Conflict** | Kya disagreement surface hua, blend nahi hua? |
| **Gaps** | Kya missing cheez state hui, guess nahi hui? |
| **Citation** | Kya reviewer har rule/item reopen kar sakta hai? |

```text
Build an eval harness... Do NOT auto-grade professional correctness with
the same model that answered. Leave authority and conclusion checks as
explicit expected-value comparisons.
```

**Definition of done:** cross-domain case har dimension pass kare **sivaye** production permission
fidelity ke, jo explicitly open gate rehta hai.

---
[⬅ Routing Aur Citing](03-routing-and-citing.md) · [⬆ Index](README.md) · [Agla: Serving Aur Operating ➡](05-serving-and-operating.md)
