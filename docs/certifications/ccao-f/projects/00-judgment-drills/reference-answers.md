# Reference Answers — 8 Judgment Drills

*Compare karo, copy mat karo — agar tumhara reasoning alag hai lekin **defensible** hai (aur asal
CCAO-F domain se grounded hai), woh bhi theek ho sakta hai. Jo galat hai woh reasoning-hi-nahi ya
CCAO-F ke apne domain-logic se conflict karna hai.*

---

## Drill 1 — Gartner statistic

**Sahi jawab:** Client presentation mein istemal karne se pehle, statistic ko asal Gartner report ke
against verify karo. Number aur source dono confident-sounding hain — exactly jaisa hallucination
sound karta hai. Presentation mein galat cited statistic pesh karna reputational risk hai.

**Kyun:** Domain 2's core lesson — self-confident-sounding output verification ka substitute nahi
hai. External citations (reports, regulations, statistics) khaas tor par verify-worthy hain, kyunke
inki galti pakarna mushkil hai jab tak koi specifically check na kare.

---

## Drill 2 — Contradicting summaries

**Sahi jawab:** Dono summaries ko flag karo as unreliable jab tak reconciliation na ho — seedha ek
choose kar ke aage mat barho. Ya to source document dobara khud parho ya ek clarifying re-prompt
karo jo dono claims ko explicitly resolve kare.

**Kyun:** Do contradicting-lekin-confident outputs ek clear inconsistency signal hain — Domain 2 ka
"inconsistencies identify karna" objective. Arbitrarily ek pick karna guessing hai, evaluation nahi.

---

## Drill 3 — Opus for short Slack drafts

**Sahi jawab:** Model choice change karo ek faster/cheaper model (jaise Haiku) ki taraf — task
(short, low-complexity, high-volume) requirement se match karta hai. "Best quality" har waqt sabse
mehnga model maangne ki tarah nahi kaam karta.

**Kyun:** Sample Question 2 ka exact shape — Domain 3's core objective "model selection ko task
requirements ke sath align karna" hai, hamesha-top-model nahi.

---

## Drill 4 — "Poora automate karo, no human touch"

**Sahi jawab:** Push back karo — background-check verification aur legal sign-off jaise steps
regulatory/legal accountability rakhte hain jo ek named human ke paas honi chahiye. Claude draft/
prepare kar sakta hai, lekin final legal/compliance decision human ke paas rehna chahiye.

**Kyun:** Domain 6 (Governance) + Domain 4 (Workflow Integration) ka overlap — "Claude ki limitations
stakeholders ko communicate karna" ka matlab hai manager ko batana **kahan** automation appropriate
nahi hai, sirf uski request follow nahi karna.

---

## Drill 5 — Stale Project knowledge sources

**Sahi jawab:** Project ke knowledge sources ko update karo naye refund policy document ke sath.
Jab tak update na ho, Project ko flag karo ya temporarily disable karo refund-related queries ke
liye, taake purani policy confidently na cite ho.

**Kyun:** Domain 5's "Claude configurations, knowledge sources, aur instructions ko inform/maintain/
update karna" — stale knowledge source ek silent-failure risk hai, sirf setup-once-forget nahi.

---

## Drill 6 — Medical history paste

**Sahi jawab:** Ruko aur organization ki data-sensitivity policy check karo health data ke liye
pehle. Agar policy restrict karti hai, personal identifiers/health details anonymize/redact karo ya
task ko approved workflow se karo.

**Kyun:** Sample Question 3 ka exact shape — Domain 6's core objective. "Pehle kaam kar lo, policy
baad mein check karunga" order galat hai — policy check **pehle** aata hai.

---

## Drill 7 — Implicit bias inference

**Sahi jawab:** Output ko flag/reject karo aur regenerate karo, explicit instruction ke sath ke
protected characteristics (ethnicity, religion, etc.) ko naam se infer na kare hiring recommendations
mein. Yeh bias hai, chahe explicitly kaha na gaya ho.

**Kyun:** Domain 6's "AI usage ke ethical implications samajhna" + Domain 2's "biases identify
karna." Implicit bias utna hi real hai jitna explicit — usay "Claude ne toh kuch bura nahi kaha"
kehke rationalize mat karo.

---

## Drill 8 — "Vibe off lagti hai," koi specific example nahi

**Sahi jawab:** Team se specific, concrete examples maango (ek input + uska actual output) —
vague complaints diagnose nahi ki ja sakti. Jab tak koi actual case na ho, "kharab ho gaya" ek
untestable claim hai.

**Kyun:** Domain 7's "issues identify/diagnose/resolve karna" ka pehla step hamesha concrete
reproduction hai — "feel off" troubleshooting ka starting point nahi ban sakta, sirf ek symptom
report hai jo abhi investigation maangta hai.

---
[⬅ Worksheet](worksheet.md) · [README](README.md)
