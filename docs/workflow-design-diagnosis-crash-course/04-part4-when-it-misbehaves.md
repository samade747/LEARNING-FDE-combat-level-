# 04 — Part 4: Jab Yeh Misbehave Kare (Concepts 11-12)

## Concept 11 — 4 Causes, Timing Se Alag Pehchano

Output disappoint kare, zyadatar log hiumm ya tool incapable maan lete, ya random change karte
jab tak chal jaye. Dono ek sawal skip karte jo narrow karta: **symptom pehli baar kab dikha?**

4 causes bad output banate jo page par kaafi same dikhta. **Timing inhe alag karti, aur yeh free
information hai jo already tumhare pass hai.**

> **Timing batati pehle kahan dekhna hai. Cause kya hai yeh nahi batati.**

| Symptom Kab Dikhi | First Hypothesis | Cheap Confirmation | Fix Confirmed To |
|---|---|---|---|
| Pehle answer se galat | **Under-specification** | Prompt dobara parho — missing cheez actually usme hai? | Jo chhoda usay add karo |
| Theek shuru hui, phir degrade hui | **Context overload** | Fresh session mein instruction restate karo — hold hoti? | Restart ya summarize |
| Ek repeatable error type | **Wrong feature/model** | Sahi feature/stronger tier se ek baar chalao | Feature/tier change karo |
| Pehle kaam karti thi, ab nahi | **Stale configuration** | Instruction/knowledge source ki date check karo | Configuration maintenance |

**Under-specification** = prompt ne wo diya hi nahi jo step ko chahiye tha — pehli response se
dikhti, sabse common cause, sabse cheap fix.

**Context overload** = conversation context window se lambi ho gayi — earlier text shorten/drop
hota, early instructions force kho deti. Better prompt help nahi karta — problem abhi likhi prompt
nahi hai.

**Wrong feature/model** = step galat tool ko gayi. Numbers thodi off = calculation prose mein
maangi gayi. Shallow work depth-task par = **tier** (fast-cheap se slow-capable tak model
version) speed ke liye chosen. Zyada prompting wo nahi khareedega jo tool produce nahi kar sakta.

**Stale configuration** = setup jo depend karta purana ho gaya. "Pehle kaam karti thi" ki tarah
dikhti — koi error report nahi hota, output slowly worse hoti.

> Har confirmation ek minute se kam leta, aur negative bhi aa sakta — **wasted minute nahi hai,
> sabse likely cause rule out kiya.**

> **Stale configuration silently fail karti.** Baqi 3 announce karte. Last quarter ke figures
> Project knowledge base mein baithe hain, is quarter ka report unko quote karta, perfectly
> formatted. Model ko pata nahi chalta diya gaya data purana hai. **Yeh Concept 7 ke unstaffed
> gate ka twin hai** — dono ek control hain jo sahi se set hui, decay hoti jab sab assume karte
> abhi bhi hold hai — **scheduled review dhoondti hai.**

## Concept 12 — Sequence Cheapest Pehle Chalta Hai

Yeh order mein run karo, task-fit question se pehle:

1. **Prompt dobara parho uske 5 parts ke against.** Role, context, task, constraints, format —
   kuch under-specified hai?
2. **Conversation ki length check karo.** Overloaded hai, restart/summary chahiye?
3. **Feature aur model check karo.** Calculation code-execution chahta, ya hard task speed tier
   par hai?
4. **Configuration current hai check karo.** Instructions, knowledge, Skills.
5. **Sirf tab, task fit hai ya nahi pucho.**

Yeh order **diagnostic sequence** hai — cheapest fix pehle.

**Step 1** sirf dobara parhna nahi — prompt ko uske 5 parts ke against hold karo: role, context
(wo background jo model ko pata nahi ho sakta), task (clear instruction), constraints, output
format. Prompt likhne wale ko fine lagta, kyunke missing piece unke zehan mein baithi hoti.
Slot-by-slot jaana absence visible banata.

Prompt dobara parhna seconds cost karta aur sabse common cause resolve karta — isliye pehle hai.
Task question karna last hai, kyunke attempt khatam kar deta.

**Step 5 exist karta, aur kabhi sahi hai.** "Maine next-quarter ki exact sales figure predict
karne ko bola, number galat tha." Koi prompt/restart/feature-change/configuration-check fix nahi
karta. **Expectation mismatch** = task jo tool kar hi nahi sakta (ek exact future number predict
karna). Fix task ko hai — range maango stated assumptions ke sath, ya drivers ka model jo adjust+
rerun kar sako.

Real mismatch naam dena ek poora afternoon prompt tune karne se bachata jo output jo kabhi
available nahi thi ke liye. Par step 5 hai kyunke baqi 4 cheaper causes rule-out hue ya nahi, yehi
farq hai.

**Complaints same lagti, diagnoses alag:**

| Jo Bologe | Diagnosis | Fix |
|---|---|---|
| "Summary key points miss karti rehti" | Under-specification | "Key" ke criteria naam do |
| "Format beech mein follow karna band ki" | Context overload | Summary se restart, ya format persist karo |
| "Numbers subtly galat hain" | Wrong feature | Calculation code execution mein move karo |
| "Pichle mahine chali thi, ab off hai" | Stale configuration | Instructions/knowledge audit karo |
| "Next quarter ki exact figure predict nahi kar sakti" | Expectation mismatch | Task reshape karo jo fit ho |

Wording se kabhi pata nahi chalta kaunsi mein ho — isiliye sequence exist karti. End-to-end
1-2 minute leta, aur zyadatar waqt cheap fix par land karta. **Opinion banane se pehle sequence
reach karo kiska fault hai.**
