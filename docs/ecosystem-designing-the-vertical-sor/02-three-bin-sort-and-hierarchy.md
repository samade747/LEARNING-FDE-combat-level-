# 02 — Three-Bin Sort Aur Source Hierarchy

## The Three-Bin Sort

Archaeology ne jo bhi dhoonda uska sorting method: purane workflow ka har element (checklist item,
form, handoff, report, sign-off) lo — **ek element = ek instruction jo koi akela follow/skip kar sake**
(agar ek checklist line 3 actions chhupati hai, sort karne se pehle 3 mein split karo). Har ek se ek
sawal poocho: **yeh kyun exist karta hai?** Sirf teen honest jawab hain, har jawab ek bin hai.

### Bin 1 — Law Aur Trust Require Karte Hain. **Rakho.**

Partner ki signature. Paise move hone se pehle insaani approval. Regulator-named separation of duties.
Standard-required evidence. Yeh overhead nahi hai — inhe delete karna innovation nahi hai. Jis profession
mein trust becha jata hai, **named human judgment khud product hai**.

Bin 1 ko **invariants** ki tarah likho — rules jo sach rehte hain chahe workflow/software/customer sab
badal jayein. *Har conclusion ko traceable evidence se support hona chahiye. Preparer apna hi payment
approve nahi kar sakta. Missing evidence ko kabhi confirmation nahi maana jayega.* Paanch sawal invariants
dhoondte hain: kaam shuru hone se pehle kya sach hona chahiye, complete hone par kya sach hona chahiye,
kya kabhi nahi hona chahiye, kaunsi evidence hamesha exist honi chahiye, konse decisions named person ke
accountable rehne chahiye. List **chhoti** rakho — rule jo sirf useful hai woh guidance hai; rule jiski
violation result ko invalid/unlawful/untrustworthy bana de woh invariant hai.

### Bin 2 — Human Limits Require Karte Hain. **Redesign Karo.**

Tick-and-tie checklist isliye hai kyunke thaka hua insaan items miss karta hai — Worker sab check kare
aur exception report de. File 3 juniors mein isliye batti hai kyunke koi akela poori file nahi hold kar
sakta — Worker poori hold karta hai, handoffs gayab. Friday batch isliye hai kyunke insaani aankhein
continuously watch nahi kar saktin — Worker act kar sakta hai jab document aaye, threshold cross ho, ya
deadline nazdeek aaye.

**Bin 2 kabhi simply delete nahi hota** — element ka *purpose* survive karta hai, Worker capability +
ek checker (jo reviewer trust kare) ki tarah rebuild hota hai.

**Sharpest refinement:** *ek control ka purpose Bin 1 hai; uska mechanism zyada tar Bin 2 hai.* Jaise:
"manager har transaction review karta hai" — yeh isliye hai kyunke purana system normal aur unusual
transactions mein farq nahi kar sakta tha. Purpose (risk controlled rahe) invariant hai — rakho.
Mechanism (sab review karo) human-limits workaround hai — redesign karo: routine cases automated checks
se guzrein, manager ka attention exceptions par jaye. Risk abhi bhi controlled hai; attention theek waqt
kharch hota hai.

### Bin 3 — Purani Technology Require Karti Thi. **Delete Karo.**

Ek system se dusre mein figures dobara type karna. Files rename karna. Same numbers ko 3 reports ke liye
format karna. Status emails/tracking spreadsheets jo sirf visibility ke liye hain. Do databases match
karna jo sirf isliye disagree karte thay kyunke woh talk nahi kar sakte thay. **Kuch bhi khud ki tarah
survive nahi karta.** Agar Bin 3 element koi real purpose chhupata hai, to woh galat sort hua — pehle
purpose ko Bin 1/2 mein move karo, phir mechanism delete karo.

### Do Warnings

1. **Kuch Bin 1 elements habits jaisi lagti hain** — retention period, required form, fixed sequence —
   yeh purani habits lag sakti hain lekin regulator ki rule ho sakti hain. **Jab shak ho, element Bin 1
   mein rehta hai** jab tak governing sources + expert confirm na karein ke safely redesign/remove ho
   sakta hai. **Chesterton's Fence:** fence hatane se pehle jaano kyun banaya gaya tha — sort hi tareeqa
   hai jaanne ka, sort record hi proof hai ke tumne poocha.
2. **Sort khud governed content hai.** Har sorting decision, apni reason ke sath, SoR mein record karo
   (kept because circular X, redesigned because purpose completeness, deleted because retyping). Yeh
   expert ka judgment hai — corpus ke har judgment jaisa hi treatment: owner, review, version. Jab rule
   badle, affected elements ko dobara sort karo. **Jo design decision likhi nahi gayi, woh compliance
   meeting mein defend nahi ho sakti.**

## The Source Hierarchy — Kaunsi Authority Jeette Hai

Corpus **the given** hai, lekin given flat nahi hai. Jab do sources disagree karein, Worker ko pata hona
chahiye kaunsa jeetega — isliye har vertical SoR ko ek **source hierarchy** chahiye, pehli reflex se
pehle likhi hui.

Typical hierarchy (aapki apni profession ki alag hogi):
1. Current law/regulation
2. Binding professional standards
3. Official regulator interpretations
4. Approved domain policy
5. Expert ki authored procedures
6. Customer-specific policy
7. Historical examples

**Refinement:** hierarchy hamesha ek seedhi ladder nahi hoti jo har sawal ka jawab de — har source ki
authority-class aur scope record karo. Higher source **sirf tab** jeetta hai jab dono sources ek hi sawal
address karte hon aur dono is case par apply hote hon.

Har source ko register entry do: publisher, authority class + scope, jurisdiction, version, effective
period, rights basis, owner, stable ID ([Template 4](06-templates.md)). **Relevance kaafi nahi hai —
source applicable bhi hona chahiye** — warna system ek perfectly relevant passage retrieve kar sakta hai
galat jurisdiction/version/retired standard se.

**Cross-border rule:** jurisdiction har authority entry par ek scope hai. Worker case ki jurisdiction
resolve karta hai retrieve karne se pehle. Har naya country apne ladders ke sath **isi** SoR mein add hota
hai (expert ki methodology rungs share karte hue jahan profession same hai) — **kabhi do countries ke
rules ek page mein blend mat karo**, kyunke blended page kisi bhi country mein cite nahi ho sakta. Naya
country = **naya build**, apni coverage ek outcome se dobara shuru karta hai — purane ki thicker version
nahi.

---
[⬅ 01 — Outcome + Archaeology](01-outcome-and-archaeology.md) · [Agla: 03 — Authority Vs Orientation ➡](03-authority-vs-orientation.md) · [⬆ Index](README.md)
