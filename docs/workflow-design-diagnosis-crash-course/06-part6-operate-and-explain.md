# 06 — Part 6: Operate Karo, Explain Karo (Concepts 17-18) + Recap

## Concept 17 — Jab Bad Output Nikal Jaye

Ab tak sab bad-output-reach-karne-ki-chance kam karta. Kuch isay hata nahi deta. Gate ek busy
Friday ko skip ho jata. Configuration review ke beech mein stale ho jati. Eventually jo workflow
tumne design ki kuch bhejti jo nahi bhejni chahiye thi — design judge hota **agle ghante mein kya
hua** se, map se nahi.

Zyadatar teams ke pass is ghante ka plan nahi hota, response improvised/slow/defensive ban jata.
**First-hour procedure** (stop spread, facts record, organization path se report) [Governance,
Risk & Responsible Use] mein hai. Yeh **4 cheezein** workflow designer **advance mein** decide
karta, taki us procedure ke pass act karne ko kuch ho:

1. **Kaise rukta hai.** Fastest tareeqa yeh workflow halt karne ka kya hai, kaun kar sakta hai,
   permission chahiye? "Humein setup karne wale se pucchna padega" ho to pehle yeh fix karo — baqi
   sab wait karte hain.
2. **Kya already bahar hai.** "Kya yeh ek output galat hua" nahi — **kitne outputs affect hue,
   kahan gaye?** Stale configuration ek bad result nahi deti — jo din stale hui usi din se **har**
   result deti, aur kisi ko pata nahi kaunsa din tha.
3. **Kisko bataya jata, kab tak.** Customer, internal owner, risk/compliance team. Pehle se decide
   karo — moment mein delay ka pull bohot strong hota, late disclosure early se zyada cost karti.
4. **Map mein kya change hota.** Har incident design ke baare mein kuch batata. 4 causes mein se
   kaunsa tha? Step galat classify hui, ya sahi classify hui par gate staffed nahi thi? Map mein
   change karo, date ke sath, taki fix us hafte se zyada chale.

Decisions 1 aur 4 tumhari hain, **design time par** decide hoti ya kabhi nahi. Jo team bata sakti
kya karti jab workflow galat ho, usay workflow chalane ki permission milti hai.

## Concept 18 — Kya Karta Hai Bolo, Phir Gate Naam Do

AI ko team workflow mein daalna matlab unko describe karna jinhon ne nahi banaya — manager,
client, risk team, outside reviewer.

**Tumhe believed kiya jata jab accurate ho** — value jitna clearly limits bhi state karo. Tool
kya kar sakta overstate karna pehla visible miss hi trust kho deta.

**3 phrases overstate karti, teeno common hain:**

- _"Fully automated"_ — almost kabhi true nahi, pehla visible error public mein expose karta
- _"AI handles X"_ — human gate sentence se drop ho jati, sunne wala sochta koi gate nahi
- _"It's basically as good as a person at Y"_ — standard set karti jo tool eventually miss karega

**Repair har baar same hai:** **jo tool karta bolo, phir human checkpoint naam do.** Ek extra
sentence cost karta — defend-able claim aur non-defendable claim ka farq.

**3rd clause add karo** jab audience decide kar rahi trust karni ya nahi: **kya refuse karta
bolo**. Har well-designed workflow ke cases hain jo decline+handover karne ke liye bani hoti.
Yeh list naam dena prove karta boundary advance mein design hui, incident se nahi mili.

**Same workflow, 3 tareeqon se:**

**Legal lead ko** (mechanism+failure modes chahiye): "Clauses nikaalti, playbook-departure mark
karti, pehli redline likhti. Change approve karna tumhara hai. Jo watch karna: obligation jo
implied hai, stated nahi — yeh miss kar sakti, isliye flags ko apne read ka prompt maano, uske
substitute nahi."

**Practice executive ko** (outcome+oversight chahiye): "Standard contract ka turnaround 2 din se
~half-day ho gaya hai, same approval standard ke sath. Lawyer abhi bhi har change sign-off karta
building se nikalne se pehle."

**Client ke risk function ko** (control chahiye): "Drafting AI-assisted hai. Qualified lawyer har
term review+approve karta, aur bina sign-off kuch nahi jata."

Same facts, 3 detail levels. Koi bhi gate drop nahi karta.

> **Stakeholders AI workflow ko zyada trust karte, kam nahi, jab human checkpoints explicit hain.**

Instinct human involvement kam dikhana chahta (lagta tool kam kar raha). Effect opposite hai —
"AI yeh karta hai" aur "jab AI galat ho to kya hota" ke beech unexplained gap wahi hai jahan risk
team sunna band kar deti.

## Recap: Yaad Rakhne Wala Sentence

> **Output verdict nahi hai. Step ko judge karo kya cost karta aur kaun jawabdeh hai se, aur
> failure ko judge karo kab shuru hua se.**

6 stages ek line mein: requirements settle karo, har step 3 criteria se map karo, loop se build
karo, timing se diagnose karo, fix configuration mein daalo, phir kya karta bolo aur gate naam do.
