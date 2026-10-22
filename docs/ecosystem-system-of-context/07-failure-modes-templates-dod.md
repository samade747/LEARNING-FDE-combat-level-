# 07 — 11 Failure Modes, 4 Templates, Definition of Done

## The Failure Modes

Log sochte hain yeh layer 5 cheezon mein se ek hai — **koi bhi nahi hai**: document dump nahi, vector
database nahi, model ki memory nahi, universal source of truth nahi, permissions ke around jaane ka
tareeqa nahi. **11 tareeqe jo ghalat ho sakta hai:**

1. **Flat index** — har source searchable, har result equally authoritative. Cure: authority routing.
2. **Flattened portfolio** — kai records ek pool mein, sales rule accounting sawal ka jawab deta hai.
   Cure: federation.
3. **Reliance on the copy** — synchronized page authority ban jati hai. Cure: discovery ≠ confirmation.
4. **Stale answer** — synced copy ek fact ke liye use hoti hai jo live fetch honi chahiye thi. Cure:
   indexed-or-live decision har field ke liye.
5. **Retrieve first, hide later** — forbidden content model context mein pehle, filter baad mein.
   Cure: permission model se pehle.
6. **Model as the quiet source** — retrieval kuch nahi laati, model "pata" se jawab deta. Cure: model
   source nahi hai, missing evidence packet field hai.
7. **The prompt as integration layer** — lamba prompt 10 systems interpret karne ke liye, connections
   kabhi implement nahi hote. Cure: connectors, tools, schemas, deterministic policy.
8. **Citations without provenance** — link milta hai, authority class/version/scope gayab. Cure: full
   provenance envelope.
9. **The blended conflict** — 2 disagreeing sources ek fluent sentence mein. Cure: conflict
   preservation, authority testing, escalation.
10. **Shadow record** — context platform apni transactions copy store karti hai, log usay source se
    zyada trust karne lagte hain. Cure: source-owned live retrieval, governed write-back.
11. **Product-shaped doctrine** — architecture jo vendor define karta hai lab mein. Cure: open
    interfaces, replaceable components.

## The Templates

4 working documents — **customer ke engagement record mein fill karo, shared vertical mein nahi.**

**Template 1 — Connected Source Register:** ek row per source (source system, kya governs, kya nahi,
mode indexed/live/both, max tolerated lag, permission origin, citable?, owner).

**Template 2 — Authority Routing Map:** ek row per sawal (question, kaunsi profession, governing
source, scope/jurisdiction, path, supporting-context-only kya, conflict rule).

**Template 3 — Boundary Contract:** (compliance officer ko dikhane wali document) — kya index ho
sakta hai, kya live fetch hona chahiye (aur kyun), kya kabhi connect nahi hota, access rules kaise
travel karte hain, permission kab re-check hoti hai, governed-truth vs supporting-context, action
kahan record hota hai, kya is instance se bahar nahi jata, promotion ka raasta, source outage par kya
hota hai.

**Template 4 — Permission Test Set:** role, sawal, role kya dekh sakta hai source mein, layer ne kya
diya, pass/fail, date, retested. **Kam az kam ek sawal jiska honest jawab "kuch nahi" ho** — jo layer
kabhi "kuch nahi" wapis nahi karti, wo tested nahi hai.

## The Definition of Done

System of Context ready hai jab har box check ho (customer ka information owner permission boxes
khud check karta hai):

- [ ] Thin slice khatam hai, Worker already cite karta hai (layer banne se pehle)
- [ ] Har source ka register row (Template 1)
- [ ] Har sawal ka routed authority+path (Template 2)
- [ ] Multiple verticals ho to profession pehle route hoti hai, koi seam cross nahi
- [ ] Boundary contract likha hai, customer ne parha hai (Template 3)
- [ ] Koi operational state indexed nahi, har changeable field live fetch hoti hai
- [ ] Governed knowledge sync ho sakta hai discovery ke liye, canonical identity ke sath
- [ ] Kuch bhi governed sirf index se rely nahi hota — applicable record confirm karti hai
- [ ] Multiple verticals ho to har finding apna record naam rakhti hai
- [ ] Har item ke access rules travel karte hain, query-time re-check hoti hai
- [ ] Permission test set pass (kam az kam ek "kuch nahi" test) (Template 4)
- [ ] Har item full provenance carry karta hai, summarizing strip nahi karti
- [ ] Conflict policy likhi hai, conflicts escalated evidence-organized ke sath
- [ ] Reflex jo governing source nahi dhoondh paata escalate karta hai, tested
- [ ] Reviewer har conclusion record se rebuild kar sakta hai, model se poochhe bina
- [ ] Read/recommend/prepare/execute alag grants, tool boundary pe enforced
- [ ] Har executed action result-owning system mein record hoti hai
- [ ] Named fallback/escalation path source outage ke liye high-risk kaam mein
- [ ] Kuch bhi is instance se shared vertical mein promotion review ke bina nahi gaya
- [ ] Named technical/domain/security/business owners exist karte hain
- [ ] Customer ka information owner ne connected sources+permission results approve kiye

**Evaluation set** successful searches se kahin zyada honi chahiye — relevant-but-non-authoritative
message, retired policy jo wording match kare, wrong customer, wrong jurisdiction, live value jo
index hone ke baad badli, bina-permission reader, bina-action-permission Worker, 2 conflicting
sources, missing required source, source outage high-risk action ke beech.

> Yeh list **definition of done** hai. Yeh **definition of safe to deploy** bhi hai — har unchecked
> box ek tareeqa hai jisse ek helpful system ghalat insaan ko sahi document de de.

---
[⬅ Reference Implementation + Ayesha](06-reference-implementation-and-ayesha.md) · [Agla: Appendix + Recap ➡](08-appendix-and-recap.md)
