# 03 — Part 4: The New Craft (Concepts 15-18)

## Concept 15 — Naye Design Objects, Aur Choreographer Ka Kaam

Screens nahi bana rahe to kya bana rahe hain?

- **Policy surfaces** — permissions, spend ceilings, ethical boundaries jo agent kabhi cross na kare
- **Confidence conveyors** — provenance chips, uncertainty markers, clean rollbacks
- **System temperament** — agent kitna patient/proactive hai, kitni baar bolta hai

Aap ab screen-crafter kam, **choreographer** zyada hain — insan aur agents ko sath move karwana:
information architecture, conversation design, operations ka feel.

## Concept 16 — Surface Ek Safety Control Hai

Surface trust **banane** ki jagah hai. Yeh trust **defend** karne ki bhi jagah hai. **OWASP Top 10 for
LLM Applications** ka jawab jo aap ne design ki hui surfaces dete hain:

- **Prompt injection** (LLM01) — surface **provenance** visible kar ke aur intent preview se defend
  karti hai
- **Excessive agency** (LLM06) — autonomy dial aur policy surfaces: default kam authority
- **Misinformation/over-trust** (LLM09) — visible uncertainty aur provenance
- **Unbounded consumption** (LLM10) — cost/budget dikhana, spend limits policy surface ki tarah
- **Sensitive-data disclosure** (LLM02) — access pillar: scoped, revocable credentials

**2 rules:** Surface **safety control hai, sirf display nahi** — "clutter kam karne ke liye" hatana
protection hatana hai. Har agentic system ko ek **governance surface** chahiye jispar trust surface
point kare — capability approval, permission review, incident review, audit log, **kill switch** (ek
move mein), drift review.

## Concept 17 — Experience Measure Karna

Surface elegant lag sakti hai aur phir bhi fail ho sakti hai. **Eval-Driven Development** measure karta
hai Worker ka output **correct** hai ya nahi. Experience metrics measure karte hain **relationship**:
kya insan delegate, trust, steer, recover kar sakta hai.

**Scorecard:**
| Metric | Kya Batata Hai |
| --- | --- |
| Plan-acceptance rate | Log plan samajh kar approve kar rahe hain ya blindly reject? |
| Intervention rate | Insan kitni baar step in karta hai (trend dekho) |
| Recovery success | Failure ke baad task achhe se khatam hua? |
| Over- vs under-trust | Bura output accept ho raha, ya achha reject? |
| Notification precision | Kitne interruptions worth the? |
| **Time saved vs attention spent** | Sabse zaroori — agent ka poora promise ek number mein |

**6 Test Sequence Launch Se Pehle:** Plan-review test, Over-trust test, Recovery test, Interruption
test, Accessibility pass, Machine-surface contract test.

## Concept 18 — Anti-Patterns Aur Design Brief

| Anti-Pattern | Kaisa Dikhta Hai | Kaunsa Concept Tootta Hai |
| --- | --- | --- |
| The black box | Bina reasoning ke act karta hai | 7 |
| Agentic sludge | Sab dobara check karte ho | 6 |
| Over-eager agent | Din 1 par high autonomy | 8 |
| Over-trusted agent | High autonomy unchecked kaam par | 4 |
| Notification spam | Har step par ping | 10 |
| Trap door | Undo na ho sakne wala action | 11 |
| Confused deputy | User instruction vs injected mein farq nahi kar sakta | 16 |
| Mystery-meat API | Machine surface jo koi agent parh nahi sakta | 13 |

## Agent Experience Brief (Deliverable)

11 sections, ek decision per section:

1. **2 audiences** — human user aur agent users naam lo
2. **Pehla contact** — onboarding, expectations reset, accessibility
3. **Trust surface** — default kya dikhta hai, 3 layers neeche
4. **Load map** — insan kya rakhta hai, Worker kya leta hai
5. **Autonomy ladder** — 5 stops, kaunse actions hamesha in-the-loop
6. **Async plan** — intent capture, glanceable progress, nudge triggers
7. **Recovery plan** — undo ka matlab, escalation path, 2 health metrics
8. **Scale par** — fleet view, drift signal
9. **Machine surface** — connector/MCP tools, 4 AX questions
10. **Safety surface** — threats aur unke defenses
11. **Scorecard** — jo experience metrics track karoge

Yeh brief woh artifact hai jo [Human-Agent Teams](../human-agent-teams-crash-course/README.md) ke
operating documents Worker ke experience ke liye karte hain.

---
[⬅ Machine Surface](02-machine-surface.md) · [⬆ Index](README.md) · [Agla: Worked Example + Lab ➡](04-worked-example-and-lab.md)
