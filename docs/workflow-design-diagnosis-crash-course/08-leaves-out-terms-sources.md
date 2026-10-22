# 08 — Course Kya Chhodta Hai + Terms + Sources

## Yeh Course Kya Chhodta Hai, Aur Wo Kahan Milta

| Yahan Nahi Hai | Kahan Milta Hai |
|---|---|
| Kya AI yeh kaam/data touch kar sakta hai | Governance, Risk & Responsible Use (agla Foundations) |
| Kya task ko AI chahiye thi hi | Is This an Agent Problem? |
| Apne personal kaam mein kya delegate karna | AI Fluency |
| Projects/knowledge/Skills configure+maintain karna | ChatGPT & Claude Quick Reference + Skills & Connectors |
| Output correct hai ya nahi deeply judge karna | Trusting the Checker |
| Model choose karna | Which AI Employees in 2026 |
| Harness+loop wale system debug karna | The Four Layers |
| Prompt-and-iterate se outgrow hone ke baad build karna | Spec-Driven Development + From One-Off to Worker |
| Review gates ko evaluation infrastructure mein badalna | Eval-Driven Development |
| Legal-clock-wala incident response | Apna compliance function, course nahi |

Agla Foundations: **Governance, Risk & Responsible Use**. Credentials collect kar rahe ho to yeh
course Associate exam ke **Workflow Integration and Solution Design** + **Troubleshooting and
Optimization** domains cover karta.

## Terms Glossary

- **Delegation map** — workflow step-by-step, har step ka owner+stated reason
- **Reversibility** — AI galat kare to undo ho sakta?
- **Stakes** — bad case mein error kya cost karti
- **Accountability** — kya yeh step wo call hai jiske liye jawabdeh hai — machine par kabhi move
  nahi hoti
- **AI-appropriate** — step jo AI own kar sakta (undo ho sakta, koi judge karta)
- **Human-retained** — step jo person outright owns
- **Collaborative** — AI produces, named person judges — koi judge na kare to collaborative hona
  band
- **Over-delegation** — AI ko step ke risk se zyada dena
- **Halo delegation** — step AI ko dena kyunke pehla step achha gaya
- **The unstaffed gate** — collaborative step jiski review ab really nahi hoti
- **Map owner** — ek named person jawabdeh ke kya map reality describe karti
- **Scheduled read** — map ki review fixed date par
- **Escalation signal** — doosre log tool par depend karte, prompt-and-iterate se outgrow hui
- **Under-specification** — pehli response se output galat, prompt kuch le kar nahi gayi
- **Context overload** — output session bare hone par worse hoti
- **Stale configuration** — output slowly worse hoti kyunke instruction/knowledge/Skill purani
- **Expectation mismatch** — task jo tool kar hi nahi sakta
- **The diagnostic sequence** — prompt, session length, feature+model, configuration, phir task —
  cheapest pehle
- **Promotion** — fix ko conversation se configuration mein move karna
- **Rule, reference, procedure** — promoted fix kahan jaye uska test
- **Baseline** — workflow ki measurement change karne se pehle
- **Parallel run** — purana+naya workflow saath, kuch cycles ke liye

## Sources and Grounding

Yeh course Anthropic ke **Claude Certified Associate** material par bana hai (Workflow
Integration and Solution Design + Troubleshooting and Optimization). Framework unka hai —
delegation criteria, 3 classifications, contract-review+onboarding workflows, mapping errors,
RFP+capacity-plan examples, build loop, escalation signal, 4 causes, cheapest-first sequence,
reaction-to-instruction, rule/reference/procedure test, friction signals, reporting audit,
stakeholder framing — sab usi material se.

**4 cheezein additions hain, restatements nahi:**

- **Window test (Concept 4)** aur hiring-freeze failure — source synthesis/judgment steps separate
  karta, isay "kya supply ho sakta" sawal ki tarah frame karna is book ka hai
- **Failing cycle (Concept 9)** — source build loop ka pehla cycle dikhata; Cycle 2 ke written-
  not-computed totals aur description-vs-feature contrast is book ke liye likhe gaye
- **Unstaffed gate + stale configuration ko ek pair** — dono source mein hain, alag modules mein;
  ek failure ko 2 sides se dekhna is book ki observation hai
- **Map ownership + scheduled read (Concept 8), incident decisions (Concept 17)** — source drifted
  configuration ki maintenance cover karta; map ko named owner/review date/4 questions dena, aur
  stop-scope questions design time par decide karna is book ke additions hain

Product behavior (long sessions compress kaise hoti, code execution kya karta) mid-2026 tak
current thi source mein. Reliance karne se pehle current docs check karo.

(Checked: Zia Tutor AI connector, 2026-10-23.)
