# 04 — Part 4: Failure Signals Aur Pattern Revision (Concepts 14-16.5)

Aap ne starting pattern chun liya. System chal raha hai. Kya batata hai pattern galat tha? Poora loop
ek picture mein: **har failure signal ek fix point karta hai, aap sabse sasti fix se sabse mehngi tak
escalate karte ho, aur sirf woh signal jo cheap fixes ke baad bhi recur kare aapko decision tree tak
wapis bhejta hai.**

## Concept 14 — 5 Failure Signals

**Signal 1: ReAct loops ya solved work revisit karta hai.** Same tool similar arguments ke sath baar-
baar call hota hai, ya partial outputs re-derive karta hai. Pattern mein structure ya stop conditions
ki kami hai — agent ko pata nahi kab "done" hai.

*Observability mein:* trace-length anomalies, duplicate-tool-call patterns, "let me try again" jaisi
reasoning text.

*Likely wajah (frequency order mein):* prompt "done" define nahi karta; tool contracts loose hain;
task genuinely planning maangta tha (Q3 yes hona chahiye tha).

**Signal 2: planner plan banata hai lekin execution diverge karta hai.** Plan "stage 1: research;
stage 2: draft; stage 3: review" kehta hai. Execution stage 1 karta hai, phir stage 3 jump karta hai,
phir stage 2 wapis ata hai.

*Observability mein:* plan-execution divergence metric, reordering signals, inserted-stage signals.

*Likely wajah:* task ki structure partially articulable hai (lightweight planning use karo); planner
ka domain match nahi karta (prompt improve karo); task genuinely articulable structure nahi rakhta
(Q3 = no hona chahiye, pure ReAct par downgrade karo).

**Signal 3: reflection answer improve nahi karti.** Critique pass chalta hai, critique produce hota
hai, agent refine karta hai, refined output original se indistinguishable (ya worse) hai.

*Observability mein:* pre/post-reflection comparison scores, criterion-firing rates, critic-generator
agreement rate (almost hamesha pass = rubber-stamping).

*Likely wajah:* criteria bohat vague hain; critic aur generator same model/similar prompts hain; task
ko reflection chahiye hi nahi thi (Q4 = no hona chahiye).

**Signal 4: multi-agent routing fail hota hai.** Coordinator galat specialist ko task bhejta hai, ya
2 specialists conflicting outputs dete hain jo aggregator reconcile nahi kar sakta.

*Observability mein:* routing accuracy metric, handoff-completeness signals, integration-failure rate.

*Likely wajah:* specialists ke roles overlap karte hain; handoff contracts implicit hain; task ko
multi-agent chahiye hi nahi tha (Q5 = no hona chahiye, single agent par collapse karo).

**Signal 5: system complex lagta hai lekin behtar nahi.** Sabse mushkil diagnose karna, koi single eval
signal isay catch nahi karti. Architecture mein multiple layers hain (planning + reflection + multi-
agent) lekin output quality measurably better nahi hai.

*Detection:* baseline comparison — task ka simpler version implement karo (single agent + ReAct, no
reflection, no multi-agent), golden dataset par quality measure karo. Simpler version ~10% ke andar
perform kare to complex architecture apna cost nahi kama raha.

*Likely wajah (almost hamesha):* team ne patterns layer kiye bina test kiye har layer justified thi ya
nahi — overshoot multiple decisions ke across accumulate hua.

## Concept 15 — Targeted Fixes Jo Architecture Chorne Ki Zaroorat Nahi Rakhtin

Zyada tar fixes prompt, contract, ya instrumentation level par hoti hain, architectural level par nahi.

| Signal | Pehle Try Karo (Sabse Sasta) | Agar Kaam Na Kare | Architectural Change |
| --- | --- | --- | --- |
| ReAct loops/revisits | Explicit stop conditions add karo | Tool contracts improve karo | Planning layer add karo (Concept 11) |
| Plan-execution divergence | Lightweight planning (kam, broader stages) | Planner prompt domain examples se improve karo | Pure ReAct par downgrade karo (Concept 10) |
| Reflection improve nahi kar rahi | Criteria specific/checkable banao | Critic ke liye alag model, explicit checking tools | Reflection poori tarah hatao |
| Multi-agent routing fail | Coordinator deterministic routing par switch karo | Handoff contracts explicit/structured banao | Overlapping specialists merge karo; single agent |
| Complex-but-not-better | Sabse upar wali layer hatao, measure karo | Agli layer bhi hatao, iterate karo | Single agent par wapis jao, evidence se rebuild karo |

**Principle: sabse chote scope par fix karo.** Prompt tightening tool-contract changes se sasti hai,
tool-contract changes architectural changes se sasti hain. **Exception:** agar signal prompt/contract
fixes ke baad bhi recur kare, yeh evidence hai architecture genuinely galat hai.

## Concept 16 — Jab Decision Tree Galat Hoti Hai

Decision tree acchi hai. Infallible nahi. **3 situations:**

**Situation 1: task properties deployment ke baad badalti hain.** Stable workflow adaptive ban jata
hai (business 20 edge cases add karti hai). Specialized expertise commodity ban jati hai (LLM behtar
ho jata hai, generalist ab woh kaam kar sakta hai jo specialist maangta tha). *Fix:* Concept 14 ki
observability isay catch kare gi. Nayi task properties ke sath decision tree dubara chalo.

**Situation 2: alag sub-tasks alag patterns maangte hain.** Maya ka agent routing, lookups, refunds,
escalations sab handle karta hai — kuch workflow-shaped hain (lookup: deterministic), kuch ReAct-shaped
(refund investigation: adaptive). Single-agent ReAct sabko handle karta hai, lekin adequately, achi
tarah nahi. *Fix:* multi-pattern composition ki tarah recognize karo — top-level coordinator pattern-
specific sub-systems ko route kare.

**Situation 3: constraints jawab badalte hain.** Hard latency budget reflection ko exclude karti hai.
Hard cost budget multi-agent ko exclude karti hai. *Fix:* constraint-driven choice ko explicitly
separate decision ki tarah track karo, document karo. "Decision tree multi-agent ki taraf point kar
rahi thi, lekin cost ceiling ki wajah se single-agent chuna. Known limitation: specialization-driven
failures zyada common hongi."

## Concept 16.5 — Anti-Pattern Gallery

**5 overshoot anti-patterns vs 3 undershoot** — real production frequency reflect karta hai. Overshoot
zyada visible hai (elaborate patterns achi demos banate hain); undershoot zyada dangerous hai (subtle
failure modes).

| Galat Choice | Kyun Fail Hoti Hai | Behtar Starting Pattern |
| --- | --- | --- |
| Multi-agent simple content generation ke liye (3 agents ek LinkedIn post ke liye) | Coordination overhead specialization gain se bohat zyada. 3x tokens, koi measurable improvement nahi | Single agent + ReAct, ya Sequential (Q5 genuinely fire kare tab hi multi-agent) |
| ReAct fixed invoice processing ke liye | Agent kabhi steps skip karta hai, kabhi re-validate karta hai. 5% runs mein step-budget exhaustion | Sequential Workflow — path known aur stable hai |
| Planner open-ended debugging ke liye | Task structure articulable nahi. Plan stage 2 tak galat ho jata hai | Single agent + ReAct — pure ReAct unknown shape+content handle karta hai |
| Reflection vague quality criteria wale tasks par | Critic/generator same blind spots share karte hain, rubber-stamping | Reflection hatao, ya human review use karo |
| Ek giant agent kai domains ke liye | Context overflow, role confusion, tool-routing errors cascade | Multi-agent specialist system, domain-specific — Q5 genuinely fire karta hai |
| Stable workflow mein planning add karna | Har run extra LLM call kuch na kamate hue pay karta hai | Sequential Workflow — path fixed hai to planning ki zaroorat nahi |
| Single-agent massive context wale tasks ke liye | Context window degradation, reasoning weaken hoti hai | Multi-agent with focused contexts — Q5 ka context claim fire karta hai |
| Reflection skip karna genuinely verification chahne wale outputs par | Subtle errors ship hote hain | Reflection layer add karo — Q4 fire karta hai |

**Gallery ka pattern:** zyada tar galat choices pattern-overshoot hain, aesthetic appeal se driven
(multi-agent impressive lagta hai, planning rigorous lagti hai, reflection careful lagti hai). Chota
lekin equally important subset pattern-undershoot hai, simplicity bias se driven.

**Self-check:** *"Agar ek senior engineer meri choice review kare, sabse likely objection kya hoga?"*
Agar aap predict aur defend nahi kar sakte, aap ne abhi principled choice nahi ki.

---
[⬅ 5 Patterns In Depth](03-five-patterns.md) · [⬆ Index](README.md) · [Agla: Decision Lab ➡](05-decision-lab.md)
