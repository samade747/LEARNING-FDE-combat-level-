# 04 — Question 4: The People — Kya Yeh Kisi Ko Unfairly Affect Karti Ya Disclosure Chahiye?

Hiring coordinator AI se applications screen kar ke shortlist banata, "qualified candidates" ki
tarah forward karta. Manager sirf unhi ko interview karta, jo screen se drop hue unhe kabhi nahi
dekhta. Concern kya hai yahan, aur kya yeh wo hai jo tum pehle naam karte? Decide karo pehle.

Pehli 3 questions mostly organization+uski info protect karte. **Yeh ek bahar dekhta hai.**

**Pucho:**

1. Kaun affected hai, including log jo output kabhi nahi dekhte?
2. Unke liye kya galat ho sakta?
3. Kya wo notice/challenge kar sakenge?
4. Fair process kaisa dikhega?
5. Disclosure required hai, ya AI involvement reasonably unko matter karegi?

Bias sirf data ke sath nahi aati — prompt se, task framing se, ya language-generation ke
patterns se bhi aa sakti. "Strongest candidates rank karo" request mein unstated standard hota,
output usay inherit karta. **Check sirf facts-right-hain ka nahi — framing ne result tilt kiya ya
nahi ka hai, aur risk affected person ke stakes ke sath barhta.**

## 4.1 — Kaun Excluded Hua Dekho

**Sabse aasan AI risk miss hone wala:** system ek set narrow karta, insaan sirf survivors inspect
karte.

Examples: candidate shortlists, fraud/risk flags, escalation-ke-liye-chuni tickets, attention-ke-
liye-chuni leads, relevant-chuni documents, priority-ranked log/cases.

AI systematically ek group hata deta to koi notice nahi karta jab review sirf jo bacha usay
dekhta. **Practical control: exclusions ko bhi sample karo, inclusions jitna hi.**

Yeh **employment, access, benefits, education, finance, ya health** decisions mein sabse zyada
matter karta. Organization ke apne legal limits bhi ho sakte automated decision-making par — yeh
framework unhe replace nahi karta.

Opening ki shortlist: concern yeh nahi ke AI involved thi, na sirf yeh ke applicants ko nahi
bataya gaya (yeh bhi matter kar sakta) — **yeh ke koi nahi dekh raha kaun hataya gaya.**

## 4.2 — Disclosure: Rules Pehle, Judgment Baad Mein

Is order mein pucho:

**Pehle: disclosure required hai?** Law/policy/contract/professional rules/client commitments/
organizational standards check karo. Koi ek require karta to decision already ban gaya.

**Doosra: koi rule answer nahi karta to — kya AI involvement is person ki understanding change
karegi work ya relationship ke baare mein?** AI jo table reformat karti alag hai AI se jo manager
ka personal assessment draft karti jo employee parhega. Routine tooling label nahi chahti;
consequential/relational work zyada transparency deserve karta.

**2 cases jo common hain:**

**Authorship** — kaam jo tumhare naam/organization ke naam se jata, tumhara hai stand-behind karna
chahe AI ne kitna bhi drafted ho. Rule na ho to test use karo: reader ki understanding change hoti
agar jaanti? Board paper/reference letter/published article usually **haan**. Tidied-up meeting
agenda usually **nahi**.

**Notetaker meeting mein** — call join karta, saari 4 questions ko touch karta ek saath.
Appropriate hai summary-review ke sath (misattributed commitment real error hai). Conversation
customer/employee/deal info rakh sakti — recording ko upload jaisi route-check chahiye. Notetaker
poori conversation reach kar sakta participant ki tarah — **sab affected hain, shuru mein
announce karo.** Kuch jurisdictions har participant ki consent require karti — colleague jo baad
mein pata lagae usay routine tooling nahi lagegi.

**Rule settle na kare aur case ordinary ho, disclose karo, conceal mat karo.** Case ordinary na ho
to escalation rule-invent-karne se behtar hai.

## 4.3 — Verdict Nahi, Sawal Escalate Karo

Structured reasoning zyadatar ambiguous cases handle karti. **3 signals** batate yeh akela handle
na kare:

- Affected population bari hai
- Potential harm significant hai
- Sawal aise area ko touch karta jahan team ko resolve karne ki standing nahi (law, contract,
  employment, professional obligation)

Koi bhi ek kaafi hai. **Escalate karna timidity nahi — decision jiske pass hai usay route karta.**

**Weak escalation:** "Mujhe lagta theek hai. Approve kar sakte?"

**Strong escalation:** "Yeh workflow hai, kaun affected hai, humne control add ki, aur jo point
framework settle nahi karta: kya hamari disclosure obligation is audience par apply hoti."

## Worked Example: Performance-Review Drafting

<details>
<summary>Performance-review example, sab 4 questions se guzarti</summary>

Manager chahta apni notes se draft performance-review summaries banayein.

**Case:** appropriate with human review — manager assessment own kare, har statement notes se
verify kare.

**Data:** employee info sensitive internal material hai — approved route use karo, unnecessary
personal details bahar rakho.

**Capability:** ordinary drafting ko shayad naya connector nahi chahiye. HR tools se automatic
data pull ho to access+scope ko bohot stronger review chahiye.

**People:** employees directly affected hain — manager ko consistency check karni chahiye alag
employees ke beech, sirf har paragraph alag-alag sahi lagta hai ke nahi. Disclosure obligations
policy/contract/context par depend karti.

AI performance review ko automatically galat nahi banati. Point yeh hai ke workflow ko controls
chahiye jo logon ko affect karne ke tareeqe ke around shaped hon.
</details>

## Now Do It — Record Ka Block 4

Kaun affected hai (jo output kabhi nahi dekhte including); kya harm/unfairness credibly ho sakta,
exclusions bhi review karte ya nahi; rule kya disclosure require karta, judgment kya add karta;
kya escalation chahiye.

```text
Here is a workflow: [describe it].

Take me through the four People questions one at a time, and wait for
my answer before you move on. Who is affected, including people who
will never see the output? What could go wrong for them, and would
they be able to tell? What would a fair outcome look like? What
disclosure does a rule require, and what would only be my own
judgment?

Then say whether this is mine to decide and document, or something to
escalate. If it should be escalated, draft it as a question with my
reasoning attached, not a request for approval. Do not tell me it is
compliant.
```
