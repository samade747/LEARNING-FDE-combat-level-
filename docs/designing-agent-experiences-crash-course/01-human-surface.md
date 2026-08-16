# 01 — Part 2: Human Surface — Trust Ke Liye Design (Concepts 4-12)

## Concept 4 — Trust Kamaya Jata Hai, Assume Nahi Hota

Delegation trust par chalta hai, aur trust agentic product mein sabse scarce cheez hai.

> **Trust = Reliability (waqt ke sath dikhi hui) × Transparency (check ki ja sakti) × Control (mehsoos
> hota) × Mistakes (undo ho sakti).**

Yeh **product** hai, sum nahi — kisi ek term mein zero, poora zero. **Pehla move sabse humble hai: agent
ko visibly uncertain hone do.** Agent jo apna doubt chhupaye aur confidently ghalat ho, us se zyada
trust todta hai jo bole "yeh part mujhe sure nahi."

**Ulti taraf ki galti bhi real hai: over-trust.** Agent 100 baar sahi ho chuka ho, banda check karna
band kar deta hai, aur jab woh chupke se drift karne lage tab bhi notice nahi karta.

## Concept 5 — Pehla Contact: Onboarding, Cold-Start Trust, Sabke Liye Access

Din 1 par koi track record nahi hota. **3 moves:**

- **Har jump par expectations reset karo** — jab surface act karne ki power paye, saaf batao
- **Stakes ghata kar trust borrow karo** — lowest autonomy stop se shuru karo, plan pehle dikhao, pehla
  task chota aur reversible rakho
- **Naya hone mein honest raho** — "maine yeh pehle nahi kiya, isliye zyada check-in karunga"

**Surface sab ke liye kaam karni chahiye.** WCAG 2.2 floor hai — status screen reader ko announce ho,
plan/undo/human-path keyboard se reachable ho, confidence kabhi sirf color se na ho.

## Concept 6 — Load Redistribute Karo, Aur Batao Kaun Kya Uthata Hai

Agent 3 kism ka weight uthata hai: **cognitive** (analysis/decision), **creative** (drafting), **logistical**
(steps/coordination). **Design ki galti:** weight ko **chupke se** move karna. Isay **agentic sludge**
kehte hain — banda nahi bata sakta agent ne kya kiya, to sab dobara check karta hai, saved time gayab.

**Fix: division of labor visible aur adjustable honi chahiye.** Har waqt banda dekh sake "yeh maine
kiya, yeh tumne kiya, yeh tum par wait kar raha hai."

## Concept 7 — Progressive Transparency: Reasoning Visible, Kabhi Overwhelming Nahi

**Kuch na dikhao** — black box, koi trust nahi. **Sab kuch dikhao** — banda noise mein doob jata hai.
**Jawab: progressive transparency** — default outcome dikhao, banda jitna chahe utna reasoning mein
neeche jaye.

**4 Layers:**
1. **Outcome** — ek plain line
2. **Plan** — ordered steps
3. **Why** — rationale, honest confidence signal (real "high/low/unsure", fake percentage nahi)
4. **Evidence** — sources, tool calls, poora trace

## Concept 8 — Autonomy Dial: Permission Jo Barhti Hai

Autonomy switch nahi hai, ek **dial** hai — aur **banda** (aap nahi) usay pakarta hai. Low se shuru
karo, agent prove kare to barhao.

**Human-in-the-loop** (agent rukta hai, approval maangta hai) vs **human-on-the-loop** (agent act karta
hai, banda dekhta hai, intervene kar sakta hai). Low-stakes, reversible kaam on-the-loop kama sakta hai;
high-stakes/irreversible hamesha in-the-loop.

## Concept 9 — Intent Preview Aur Plan-Review Habit

Sabse sasti galti rokna: act karne se pehle **plan** dikhao, banda edit kar sake. *"Main yeh karne wala
hoon: 1, 2, 3. Kuch badalna hai?"*

**2 rules:** Preview stakes ke mutabiq scale kare. Plan mid-flight editable ho, sirf approve/reject
nahi.

## Concept 10 — Asynchrony Ke Liye Design

Command software synchronous tha. Agentic kaam yeh rhythm todta hai — intent set karo, **disconnect**
karo, wapis aao.

**4 Surfaces:** Intent capture (aap ke bina chal sake), glanceable progress, **nudge, don't notify**
(sirf real decision points par interrupt karo), review-and-refine surface.

**Waiting ka felt experience design karo:** honest progress ("40 invoices parh raha hoon" spinning
circle se behtar), rough expectation ("~2 minute lagenge"), visible cost/budget burn. **Silence "broken"
lagta hai, "busy" nahi.**

## Concept 11 — Repair Aur Redress: Jab Ghalat Ho

Agent ghalat act **karega**. *Might* nahi. **Will.** **4 Moves:**
1. **Undo, ek click jitna qareeb ho sake** — poore course ka sabse strong trust-builder
2. **Straight apology aur plain account** — koi hedging nahi
3. **Corrective action aur agla step** stated
4. **Insan tak visible path** — hamesha

**2 numbers watch karo:** Escalation frequency (healthy band ~5-15%), Recovery success (~90%+).

## Concept 12 — Kai Ko Supervise Karna: Ek Agent Se Workforce Tak

10 Workers ek sath chalein to single-agent surface collapse ho jati hai. **Design problem shape badalti
hai: monitoring se triaging tak.**

**3 Surfaces:** **Fleet view** (ek nazar, har Worker), **Attention triage** (surface rank karti hai kya
abhi zaroori hai), **Drift** (sirf "help maangi" nahi, "escalation rate double ho gaya" bhi surface hona
chahiye — over-trust yahin pakra jata hai).

**Circuit breaker:** Jab Worker ka escalation/error rate apni baseline ka multiple cross kare, surface
khud usay lower autonomy stop par le jati hai ya pause karti hai — insan ke notice karne ka wait nahi
karti.

---
[⬅ The Shift](00-the-shift.md) · [⬆ Index](README.md) · [Agla: Machine Surface ➡](02-machine-surface.md)
