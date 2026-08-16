# 08 — Four-Phase Workflow + Five Failure Patterns

## Seven Principles Production Mein Ek Loop Ban Jate Hain

Jab loop haath mein aa jaye, principles phases ke andar khud-ba-khud fire hote hain:

1. **Explore** *(Bash + Observability)* — relevant files parho, unknowns saamne lao. **Read-only. Koi
   writes nahi abhi.**
2. **Plan** *(Code-as-Interface + Persistence)* — structured artifact ki tarah likha hua plan banao.
   Save karo. Review karo. Edit karo. **Yeh sabse important phase hai — zyada tar leverage yahin hai.**
3. **Implement** *(Decomposition + Verification)* — plan ko chote atomic steps mein execute karo, har
   ek ke baad verify karo, commit/save karo.
4. **Commit** *(Observability)* — final verification pass, decisions rules file mein wapis save karo
   agli baar ke liye.

**Chaaron phases ko wrap karta hai:** *Constraints (P6).* Kaunse folders agent dekh sakta hai, kaunsi
connectors call kar sakta hai, kis approval mode mein hai — yeh session start (ya config) mein set hota
hai aur **har** phase ko govern karta hai. Explore mein read-only Plan Mode P6 hai. Implement mein
`deny` rule jo write block karti hai — wahi P6 hai. Commit se pehle final approval card — wahi P6 hai.
**P6 diagram mein ek box nahi, diagram ke *around* ka box hai.**

Shape same rehta hai chahe akhir mein artifact ek merged pull request ho, ek redlined MSA ho, ek closed
quarterly variance pack ho, ya hiring debrief ho. Sirf inputs/outputs badalte hain, phases nahi — isiliye
yeh loop domains ke across portable hai.

## Panch Failure Patterns

Jab loop ke andar kuch ghalat ho, taqreeban hamesha in 5 mein se ek pattern mein aata hai. Pattern
pehchano to pata chal jata hai kaunsa principle use karna hai.

| # | Pattern | Symptom | Rokta Kaunsa Principle |
| --- | --- | --- | --- |
| 1 | **The Drift** | Agent brief se dheere dheere door hota jata hai | Persistence (P5) — brief file mein likho |
| 2 | **The Confident Wrong** | Plausible output jo chupke se galat hai | Verification (P3) — check step force karo |
| 3 | **The Big Bang** | Ek bara change ghanto ka kaam nuke kar deta hai | Decomposition (P4) — chote reversible units |
| 4 | **The Scope Creep** | Agent aisi cheezein touch karta hai jo authorize nahi | Constraints (P6) — scope + approvals |
| 5 | **The Black Box** | Agent 20 minute chala, pata nahi kya kiya | Observability (P7) — execution view dekho |

Table ko dono taraf se parho: har principle apna pattern **rokta** hai; jab pattern dikhe, us column ke
principle ki taraf jao. Kuch hafton real use ke baad, naam diagnostic shorthand ban jate hain — "yeh ek
Confident Wrong tha" bolna kaafi hai poori team ko batane ke liye kaunsa verification step missing tha.

---
[⬅ Principle 7](07-principle-7-observability.md) · [⬆ Index](README.md) · [Agla: Worked Example + Capstone ➡](09-worked-example-capstone.md)
