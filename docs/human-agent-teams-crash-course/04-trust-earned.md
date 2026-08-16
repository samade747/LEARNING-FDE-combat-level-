# 04 — Part 5: Trust, Kamaya Hua (Concepts 10-12)

## Concept 10 — Autonomy Reliability Ke Sath Barhti Hai

Naye colleague ko pehle din chabiyan nahi dete. Agent ko pehle din 500 bug fixes nahi dete. **Autonomy
proven reliability ke mutabiq grant karo, phir jaan-boojh kar, per task-type widen karo.**

**Trust Ladder (5 levels):**

| Level | Agent Kya Karta Hai | Insan Kahan Hai |
| --- | --- | --- |
| **L0** | Sirf draft karta hai | Insan sab kaam karta hai |
| **L1** | Act karta hai, har output review hota hai | Insan sab review karta hai |
| **L2** | Act karta hai; verifier check karta hai | Insan sirf exceptions review karta hai |
| **L3** | Limits ke andar act karta hai; escalations batch | Insan batched escalations review karta hai |
| **L4** | Task type khud chalata hai, approved scope mein | Insan weekly report review karta hai |

Naya agent ek task-type par L1 se shuru hota hai aur repeated, verified wins ke baad barhta hai. **Same
agent ek task type par L4 aur doosre par L1 ho sakta hai — autonomy worker-on-a-job ko milti hai, poore
worker ko nahi.**

> **Claude Tag ka lived example:** Ek engineer ne Tag trivial fixes se shuru kiya, hafton mein progressively
> bara kaam delegate kiya jab results theek nikle. Autonomy **per task type** widen hui, sab ek sath
> nahi. Aur widen hone diya usay verification ne — Tag sandbox mein kaam chalata, check karta, evidence
> post karta (aksar ek video) — insaan attention kharch karne se pehle.

> **Caution — Ladder ka chhupa assumption sadd sakta hai:** Har level L0 se upar isi baat par khara hai:
> insan bata sake agent ghalat hai. Yeh ability permanent nahi — **AI gravity** (AI ka output bina check
> kiye accept karne ka constant pull) usay chupke se ghisti hai. Reviewer jo parhna band kar chuka, woh
> L1 label hai jo L4 reality par hai. **Ladder dono taraf move honi chahiye** — autonomy tab widen hoti
> hai jab **agent** proven ho, aur tab narrow honi chahiye jab **insan** engage karna band kar de.
> Har hafte, agent ke kuch passes khud dobara verify karo, chahe kuch bhi ghalat na lage — **especially
> tab, kyunki clean passes ki lambi streak hi pull sabse strong hoti hai.**

## Concept 11 — Kaam Checkable Banao

Autonomy safely barhne wali cheez: kaam **insaan dekhne se pehle verify ho sakta hai.** Code ke tests
hote hain. Baaki kaam bhi grade ho sakta hai: document rubric ke against, report checklist ke against.

Yeh team level par **Eval-Driven Development** hai — rubric ek eval hai jo ek worker ke output par
apply hoti hai, ek checklist ki tarah jo koi teammate chala sake.

**Doer-verifier:** ek agent kaam karta hai, doosre agent ka **sirf** kaam usay check karna hai. Sasti
insurance — agent ka time kharch karti hai insan ka time bachane ke liye.

**Draft karo:**
```text
Write a verification rubric for [my worker]'s main output: concrete
pass/fail checks. Then describe a doer-verifier setup.
```

**Check karo:** Doosra agent sirf is rubric se pehle ko grade kar sakta hai, aur aap pass ko trust
karenge? Agar "pass" ke baad bhi har line parhne ka mann ho, rubric specific nahi hai.

## Concept 12 — Insaani Attention Ko Paisa Ki Tarah Kharch Karo

Ek naya failure mode: insano ko output mein doob dena. Achhi teams apne agents se **questions batch**
karwati hain, **key context repeat** karwati hain, aur **ek waqt mein kitne items dikhein** limit karti
hain.

**Reflection cycle mein build karo:** Team se weekly **"lessons and missteps"** report mangwao — galtiyan
track hoti hain, repeat nahi hoti.

**Draft karo:**
```text
Draft a weekly team report template: what it shipped, lessons and
missteps, which task types earned more autonomy. Then propose an
attention budget: what I review, what's batched, the cap.
```

**Check karo:** Busy hafte mein, kya yeh insan ko sirf important cheezein decide karwata hai? Agar phir
bhi sab kuch parhna parta hai, budget scarce resource protect nahi kar raha.

---
[⬅ North Star](03-north-star.md) · [⬆ Index](README.md) · [Agla: Team Khadi Karo ➡](05-standing-up-team.md)
