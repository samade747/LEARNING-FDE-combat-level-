# 04 — Permission Model Se Pehle, Provenance, Conflict

## Permission Comes Before the Model

**Yeh invariant sab se zyada skip hoti hai** — kyunke skip karna ~6 hafte tak sab asaan rakhta hai.
Document ke access rules uske home system mein rehte hain. Layer copy banaye to **access rules bhi
copy karna** zaroori hai, aur har query ke waqt dobara check karna. **Permission inherit hoti hai,
invent nahi.**

**3 alag permission sawal, 3 alag jawab:** (1) Kya yeh insaan yeh source dekh sakta hai? (2) Kya yeh
Worker is task ke liye dekh sakta hai? (3) Kya yeh Worker jo action follow kar sakti hai wo perform
kar sakta hai? Ek manager salary data parh sakta hai, ek recruiting Worker ek narrow field check kar
sakta hai — **koi bhi payroll change nahi kar sakta.** Read/reason/recommend/prepare/execute **alag
grants** hain.

**Safe order:** identity resolve → source permissions resolve → eligible records filter → retrieve+
rank → packet assemble → **action permission alag se tool boundary par resolve**. **Unsafe order:**
sab retrieve karo, model ko bhejo, model ko kaho "mat batana jo reader nahi dekh sakta."

> **Model context ke andar chhupi hui passage chhupi nahi hoti.**

Apna permission model banane ki jagah inherit karo — warna ek junior ek reasonable sawal poochta hai
aur ranked-first, friendly-summary mein, compensation memo mil jata hai jo usne kabhi dekhni nahi
thi. **Koi attack nahi hua. Layer ne apna kaam ghalat rules ke against kar diya.**

### Yeh Sirf Privacy Nahi — Control Ka Sawal Hai

**Segregation of duties ability-combinations ke baare mein hai, visibility ke nahi** (journal entry
banana + approve karna). Read access khud SoD conflict nahi hoti — "humne SoD toda" kehna meeting
mein haar jayega. **Asal exposure ek layer neeche hai:** access control poore control environment ki
foundation hai. Layer jo entitlement-model se bahar effective access de deti hai, **periodic access
review ko ek jhooti picture certify karwa rahi hai** — kuch nahi chora gaya, koi documented rule nahi
tootha, lekin review ab wo certify kar rahi hai jo sach nahi.

> **Context layer jo entitlement model se bahar effective access deti hai, ek control nahi todta —
> us review ko chup-chaap invalid kar deti hai jo sab control certify karti hai.**

## Provenance Travels With Every Item

Packet mein har material item **kam az kam yeh fields** carry karta hai: Source system, Stable ID,
Authority class, Scope, Version+effective period, Owner, Retrieved/synced-at, Permission basis,
Citation. **Bina provenance ke packet text ka dher hai. Sath mein, reviewable evidence hai.**

Layer kabhi source labels nahi strip karti reranking/summarizing mein — 5 sources ko ek smooth
paragraph mein merge karna signed-contract/approved-policy/informal-message ka farq mita deta hai.

**Governed truth vs Supporting context** (ek level upar, record ki apni Authority/Orientation ki
tarah): Governed truth SoR se aata hai — citable. Supporting context customer ke working material se
— cite ho sakta hai **evidence** ki tarah, kabhi **rule** ki tarah nahi.

| Content | Class | Worker kaise use kare |
| --- | --- | --- |
| Applicable reporting standard | Governed truth | Cite karo, version+jurisdiction ke sath |
| Expert ki authored procedure | Governed truth | Cite karo expert methodology ki tarah |
| Signed contract | Governed truth (customer layer) | Cite karo contract ki tarah |
| Current ERP posting | Governed truth (apne scope mein, live) | Cite karo + reading time |
| Prior-year working paper | Supporting context | Parho, attribute karo, rule ki tarah kabhi cite mat karo |
| Salesperson ka "customer ne accept kiya" message | Supporting context | Clue ki tarah parho, acceptance ka proof nahi |
| Message jo reader khol nahi sakta | Kuch nahi | Kabhi dikhti hi nahi (permission inherited) |

**Example:** ek 3-saal purana email "we always capitalise these" — fluent, relevant, **basis ki tarah
precisely ghalat.** Correct jawab requirement ko standard tak route karti hai, email ko sirf past-
practice evidence ki tarah use karti hai, aur agar disagree karen to dono ko flag karti hai. Ek
accounting error jo 12 mahine repeat hui, phir bhi error hai.

## Conflict Is a Result, Not a Retrieval Failure

Jab 2 source disagree karen, unko ek sentence mein blend mat karo jo koi source ne nahi kaha. Disagreement
**visible** rakho, decide karo kaunsa source governs, aur authority settle na kare to **escalate**
karo.

Conflict ke **exactly 3 outcomes:**
- **Resolved by scope.** Sources alag sawal ka jawab de rahe hain, dono sahi (sales/accounting seam ka
  roz-marra case).
- **Resolved by authority.** Ek applicable source governs, hierarchy batati hai kaunsa.
- **Unresolved.** Worker escalate karta hai, conflicting evidence already organized.

Escalation bar record ne already set ki hai: **insaan ka kaam kam karna chahiye** — "sources conflict
karte hain" nahi kehti, **kaunse sources, kya har ek kehta hai, kaunsa authority test apply hua, kya
open hai, kaun settle kar sakta hai** batati hai.

> **Ek trustworthy System of Context disagreement ko ghaib nahi karti. Usay reviewable banati hai.**

---
[⬅ Context Packet + Indexing Rules](03-context-packet-and-indexing-rules.md) · [Agla: Read-Reason-Act, Invariants, Placement ➡](05-read-reason-act-invariants-placement.md)
