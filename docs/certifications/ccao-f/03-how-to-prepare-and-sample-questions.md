# 03 — How to Prepare + Sample Questions (Guide Sections 7–8)

## How to Prepare (Section 7)

**Koi ek required course nahi hai.** Anthropic guarantee nahi karta ke koi specific resource pass
guarantee kare. Recommended combo — hands-on experience + neeche wale resources:

- Exam blueprint ([Section 6](01-domain-blueprint.md)) self-assess karo, har objective ke against
- Official Anthropic documentation/help articles review karo — Projects, Artifacts, Memory, Skills,
  Code Execution
- Prompts structure karna, tasks decompose karna, aur outputs iterate karna practice karo
- Real workflows banao: ek Project configure karo instructions + knowledge sources ke sath, outputs
  ko accuracy/bias ke liye evaluate karo
- Responsible-use judgment practice karo: data sensitivity, appropriate use cases, kab
  escalate/human-review karna hai
- Neeche diye sample questions complete karo item-style familiarize karne ke liye

## Sample Questions (Section 8, Full — Guide Se Verbatim)

*Yeh illustrative items hain — exam ke style aur cognitive level dikhate hain, live item bank se nahi
liye gaye.*

### Sample 1 · Domain 2 — Output Evaluation and Validation

Ek associate Claude se ek naye regulation ka summary maangta hai, aur Claude ek confident summary
deta hai jisme ek specific subsection number cite hota hai. Compliance team ko bhejne se pehle, sab se
appropriate action kya hai?

- **A.** As-is bhej do, kyunki Claude ne high confidence express kiya
- **B.** ✅ Cited subsection ko official regulation text ke against verify karo bhejne se pehle
- **C.** Claude se apni confidence rate karwao aur agar rating high ho to bhej do
- **D.** Summary ko zyada formal sound karne ke liye reword karo, phir bhej do

**Rationale:** Language models specific-looking details (jaise citation numbers) fabricate kar sakte
hain — yeh hallucination hai. Compliance audience ke liye bound factual claims/citations ko authoritative
source ke against validate karna zaroori diligence step hai. Self-reported confidence (A, C) accuracy ka
reliable signal nahi hota, aur reformatting (D) correctness address nahi karti.

### Sample 2 · Domain 3 — Product and Model Selection

Ek associate ko high-volume mein short customer-reply drafts generate karne hain jahan speed aur cost
deep reasoning se zyada matter karte hain. Task ke liye sab se best choice kaunsi hai?

- **A.** Har reply ke liye sab se capable, highest-cost model use karo quality maximize karne ke liye
- **B.** ✅ Ek faster, lower-cost model use karo jo straightforward, high-volume tasks ke liye suited ho
- **C.** Cost kam karne ke liye sab product features disable kar do
- **D.** Kisi doosre AI platform pe switch kar jao

**Rationale:** Model selection ko task requirements ke sath align karna matlab hai straightforward,
high-volume kaam ke liye ek faster/lower-cost model match karna, aur sab se capable model complex
reasoning ke liye reserve rakhna. Hamesha top model use karna (A) cost/latency budget waste karta hai;
features disable karna (C) ya platform switch karna (D) trade-off address nahi karte.

### Sample 3 · Domain 6 — Governance, Risk, and Responsible Use

Ek project manager ek spreadsheet upload karna chahta hai jisme customer names aur account numbers
hain, taaki Claude trends analyze kar sake. Organizational policy regulated personal data share karne
ko restrict karti hai. Sab se appropriate action kya hai?

- **A.** File as-is upload kar do, kyunki analysis internal hai
- **B.** ✅ Personal identifiers ko remove ya anonymize karo upload karne se pehle, policy ke mutabiq
- **C.** File upload kar do lekin Claude ko instruct karo ke retain na kare
- **D.** Analysis poori tarah skip kar do

**Rationale:** Data-sensitivity aur privacy safeguards apply karne ka matlab hai regulated identifiers
ko redact/anonymize karna use se pehle, taaki analysis protected data expose kiye bina proceed ho sake.
As-is upload karna (A) policy violate karta hai; model ko retain-na-karne ka instruction dena (C) policy
control satisfy nahi karta; task abandon karna (D) unnecessary hai jab anonymization use enable kar
sakta hai.

---
[⬅ 02 — Book Coverage + Scope](02-book-coverage-and-scope.md) · [Agla: 04 — Policies, Resources + Doc Control ➡](04-policies-resources-and-doc-control.md)
