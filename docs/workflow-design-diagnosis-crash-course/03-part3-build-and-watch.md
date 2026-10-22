# 03 — Part 3: Build It, Aur Watch It (Concepts 9-10)

## Concept 9 — The Loop: Ideate, Prototype, Feedback, Refine

AI design partner hai, vending machine nahi. Jo tum saamne rakhte usi par react karta, tumhari
situation ke baare mein kuch nahi jaanta jo tumne nahi bataya. Solution pucho karke nahi milega —
**4-step loop** chalao: **ideate** (options banana), **prototype** (ek concrete banana react karne
ke liye), **feedback** (kya galat hai dikhana, jo pehle se nahi pata tha), **refine** (fix karna).
Phir round.

Loop ko **Project ke andar** chalao taki background/limits/pehle decisions stable rehein. Scattered
chats mein har round thodi alag understanding se restart hota — isliye solution ki jagah drafts
ka dher mil jata.

### Worked Example: 3 Cycles, Koi Code Likhe Bina

Analytics team ko chhota internal tool chahiye tha metrics track karne ke liye. Build pay karne
ke jagah, AI se **artifact** (chhota working web page chat ke andar) banwaya.

**Cycle 1 — build:** "5 metrics ka simple dashboard artifact banao, har ek ke liye chart." Artifact
aata, working, 5 charts, readable, roughly right. **Yeh cycle overconfident banati**, kyunke kuch
hard abhi nahi poocha.

**Cycle 2 — filter aur totals:** date-range filter + totals row maangi. Filter kaam karta. **Totals
galat hain** — obviously nahi, figures right size/format mein hain. Ek analyst ne notice kiya
column add nahi hota — sirf kyunke usay roughly pata tha number kya hona chahiye. **Kuch toota
nahi — totals likhe gaye the, compute nahi hue, likha number calculated jitna hi right dikhta.**
Fix better prompt nahi — **Concept 3** hai mid-loop: totals row calculation hai, code execution
mein jaati, prose mein nahi.

**Cycle 3 — color aur print:** brand colors + print-friendly layout maangi. Pehli baar kaam kiya.
Dono 1-sentence requests thi. **Cycle 3 description problem thi** — better describe karne se solve
hui. **Cycle 2 feature problem thi** — kitna bhi describe karo solve nahi hoti.

> **Dono ko alag pehchanna hi skill hai. Part 4 iska procedure hai.**

<details>
<summary>Failing cycle middle mein kyun hai</summary>

Cycle 2 **bina noise fail hoti** — yehi point hai. Loud failure kuch nahi sikhati, error message
bata deta kahan dekhna hai. Real failure wo hai jo review pass kar jati, kyunke output smooth/
formatted/confident tha. Real use tak pahunchti kyunke kuch usay catch karne ko nahi tha.
</details>

## Concept 10 — Jab Yeh Prompt-and-Iterate Se Outgrow Ho Jaye

Dashboard artifact ek chhoti team ki internal need serve karti thi. 6 mahine baad 3 departments
har Monday kholte, ek uske numbers board report mein daalta. **Yeh ab alag object hai, kisi ne
decide nahi kiya.**

**Escalation signal** = point jahan tool prompt-and-iterate se outgrow hua. Doosre log kisi cheez
par infrastructure ki tarah depend karna shuru kar dein, usko requirements chahiye jo pehle nahi
thi — uptime, access control, koi jisko call karein jab toote, aur guarantee ke March jaisa kaam
abhi bhi karti. Yeh kaam developer/architect expertise ke sath rehta.

**Escalate karna correct answer hai, failure ki admission nahi.** Failure opposite hai — kuch
prompt se chalate raho lambe time tak baad bhi jab doosre log depend karte hain, kyunke kisi ne
mark nahi ki jab wo chhoti rehna band hui.

> **2 signals jo similar sunte, alag jagah point karte:**
>
> | Signal | Matlab | Kahan Jao |
> |---|---|---|
> | Doosre log ab is par depend karte | Infrastructure hai, engineering chahiye | Developer/architect expertise |
> | Maine yeh same tareeqe se 3 baar solve ki | Shape stable hai, manufacture ho sakti | From One-Off to Worker |
>
> Pehla **kaun exposed hai** ke baare mein hai. Doosra **kya method change hona band hua** ke
> baare mein.
