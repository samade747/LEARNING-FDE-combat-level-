# 01 — Question 1: The Case — Kya AI Yeh Kaam Kar Sakta?

Support agent ke pass billing complaint hai, customer bolta double charge hui, agent chahta AI
account record se reply draft kare. AI yeh kaam kare? Pehle decide karo: haan, haan-review-ke-
sath, ya nahi.

**Yeh sawal pehle aata.** AI ko yeh kaam karna hi nahi chahiye to data/tools ke baad ke sawal
matter nahi karte.

Zyadatar everyday cases ko 4 screening questions chahiye, risk matrix nahi. AI Fluency Framework
par based governance material inhe **Delegation criteria** bolta — wohi screens jo decide karte
workflow ka kaunsa hissa handover karna. **Accountability**, 4th screen, matlab outcome ke liye
kaun jawabdeh rehta.

| Screen | Plain-English Sawal |
|---|---|
| **Reversibility** | Output galat ho to harm hone se pehle catch+undo kar sakte? |
| **Consequence of error** | Galat ho to cost trivial/expensive/harmful/regulated/irreversible hai? |
| **Human judgment/empathy** | Task relationship/care/context par chalta jo insaan khud rakhe? |
| **Accountability** | Kaun jawabdeh hai, aur kya wo actually AI ka kaam review+own kar sakta? |

## 1.1 — 3 Answers Mein Se Ek

Har case ko **3 answers** mein se ek milta: fully appropriate, appropriate with review, ya
inappropriate.

- **Fully appropriate** — low consequence, reversible, as-you-go review aasan. Koi special
  governance gate nahi chahiye. (Approved sources se internal FAQ, restructured notes.)
- **Appropriate with review** — AI useful hai, par specific human check use/send/act se pehle
  honi chahiye. (Billing reply, financial summary, shortlist jo attention decide karti.)
- **Inappropriate** — task human-owned rehta, kyunke consequence/undo-karne-ki-difficulty/human-
  responsibility review se repair nahi ho sakti. (Final medical/legal/disciplinary determination —
  qualified person judgment banae+own kare. AI support kar sakta, decision-maker nahi ban sakta
  sirf isliye ke answer produce kar sakta.)

## 1.2 — Deciding Factor Dhoondo

**Deciding factor** = wo ek screen jo actually classification carry karti hai.

**Pucho:** _Agar 4 answers mein se ek change hota, kaunsa change is use case ko alag classification
mein move karta?_

Condolence message ke liye deciding factor human relationship ho sakti (message rewrite karna
aasan hai tab bhi). Billing reply ke liye accountability decide karti — company jawabdeh rehti
customer ke paise ke baare mein jo bolti.

Naam dena discussion improve karta. "Risky lagta" ke jagah: _"Yeh appropriate-with-review hai
kyunke organization factual claim ke liye jawabdeh rehta."_ Yeh sentence check/challenge/improve
ho sakta hai.

## 1.3 — Human-in-the-Loop Gate Nahi Hai

"Ek insaan review karega" responsible sunta, practice mein aksar kuch matlab nahi rakhta.

**Defined gate** = review jo 3 cheezein naam karti: **kaun** review karta (role jo responsibility
actually hold karta), **kya** verify karta (specific risk jo review catch karne ke liye bani),
**kab** review karta (output hard-to-undo hone se pehle).

Compare: "Koi check karega" vs "**Account manager** delivery facts **dispatch record ke against**
check karta customer ko report jaane **se pehle**." Doosra control hai, pehla intention hai.
**Gate is form mein likh nahi sakte to workflow chalne ke liye ready nahi hai.**

<details>
<summary>Going deeper: consequence aur accountability alag hain</summary>

High-consequence task automatically prohibited nahi hai — kabhi well-designed gate kaafi control
restore karta. Low-consequence task bhi human chahti ho sakta — relationship hi task ka point
hota. 4 criteria score karke add mat karo — unhe use karo yeh dikhane ke liye case ek category
mein kyun hai, doosri mein nahi. **Accountability tool par transfer nahi hoti** — manager/
clinician/lawyer/employer kam responsible nahi ban jata kyunke AI ne kaam ka hissa draft kiya.
</details>

## Worked Examples

| Use Case | Classification | Kyun | Gate |
|---|---|---|---|
| Approved policy docs → internal FAQ | Appropriate | Reversible, low consequence, authoritative sources | Normal editorial review |
| Billing complaint ka customer response draft | Appropriate with review | Company account facts ke liye jawabdeh | Support agent facts+tone verify karta sending se pehle |
| Final professional determination generate karna | Inappropriate (final decision-maker ki tarah) | Accountability+consequence tool mein transfer nahi ho sakti | Human professional determination banata+owns karta |
| Applications summarize karna reading organize karne ke liye | Appropriate with strong review | Applicants ke liye consequential, unfair filtering ka khatra | Hiring owner **inclusion aur exclusion** dono decisions review karta |

## Now Do It — Record Ka Block 1

Apni workflow ke liye likho: AI kya karta, human kya abhi bhi karta; classification; deciding
factor; gate (kaun kya check karta, kab).

```text
Here is a workflow I am thinking of handing to AI: [describe it].

Push back on my reasoning. Screen it on reversibility, consequence of
error, how much human judgment it needs, and who stays accountable.
Say whether it looks fully appropriate, appropriate with review, or
inappropriate, and which single factor is deciding that.

If it needs review, write the gate as who checks what, and when. Do
not tell me it is approved or compliant. List anything I would have
to confirm with my organization.
```
