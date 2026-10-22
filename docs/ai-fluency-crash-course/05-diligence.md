# 05 — Part 2: Diligence (Concept 6)

Pehle 3 Ds behtar results ke liye hain. Diligence alag sawal poochta hai: **"Should I use AI this
way at all?"**

**Example:** Lecturer AI se end-of-term feedback draft karata hai. Writing excellent hai — lekin
usne student names, grades, disciplinary notes ek consumer AI service mein paste kiya jo university
ne approve nahi kiya tha. Students ko nahi bataya gaya ke AI ne comments likhe jo academic record
ka hissa ban sakte hain. **Output achha ho sakta hai, AI ka use phir bhi irresponsible hai.**

**Diligence** = responsibility lena iski ke AI kaise use hua aur uske output ka kya hota hai. Teen
hisse:

1. **Creation diligence** — pehle/during responsible choices
2. **Transparency diligence** — AI ka role honest batana jab log affected hon
3. **Deployment diligence** — used/released hone se pehle verify karna aur ownership lena

## 6.1 Creation Diligence

Share karne se pehle pucho: personal data hai? Confidential company info? Yeh tool mein daalna
allowed hai? Data kaun access/keep kar sakta? Organization-approved service hai? Legal/contractual/
professional restrictions?

Easiest path hamesha responsible nahi hoti — real customer database kisi bhi open AI tool mein
copy karna 5 minute bachata hai, serious privacy problem banata hai.

Often fix task drop karna nahi — **data strip karna hai.** Lecturer approved tool mein har naam/ID
remove kar sakta tha, grade range + ek behavior rakh kar draft kar sakta tha. AI ko **pattern**
chahiye, **person** nahi.

**Redaction** = identifying details remove karna AI ko data dene se pehle, task ka pattern rakh kar.

Redaction 2 directions mein fail hoti: bohot zyada hata do, task nahi ho sakta (grade na ho, incident
na ho — yeh feedback nahi); bohot kam hata do, details ki combination phir bhi ek insaan point
karti ("the only student who missed week 3 lab" naam jitna identifying hai). Test: koi jo sirf tumhara
pasted text parhe, wo pehchaan sake kaun? Data strip karna tool question ka jawab nahi deta.

## 6.2 Transparency Diligence

Har AI-assisted task announcement nahi maangti. Par jab AI doosron ko materially affect kare,
disclosure matter kar sakti — academic work, hiring decisions, customer communications, medical/
financial advice, professional reports, "original human work" presented cheezein.

**Jitna zyada AI-assisted result doosron ko affect karta, transparency ka case utna strong hai.**

Transparency matlab har workflow detail publish karna nahi — matlab hai AI ke role ke baare mein
log misleading na karna jab wo role matter karta ho.

## 6.3 Deployment Diligence

Publish/send/execute/decision mein use hone se pehle check karo. Jitne zyada log result tak pahunche,
utni zyada checking chahiye. Jo step undo nahi ho sakta, deeper check deserve karta hai.

Apne liye note ek nazar leta hai. Welcome email full read leti hai. Regulator ko report second
reviewer leti hai. Kuch bhi irreversible (sent payment, deleted folder) act se pehle check leta hai
— baad mein reviewer nahi hota.

Checking: facts verify, sources confirm, calculations check, bias/unfair outcomes review,
permissions/rights confirm, organization policy follow, high-impact actions ke liye human approval.

> **Numbers rule:** Jo number decision ka base ho (total/percentage), compute hona chahiye, generate
> nahi. AI financial report summarize karega bina column actually add kiye — likely-looking total
> predict karta hai jo galat ho sakta jab har line item right ho. Number spreadsheet/calculator/AI-
> run-code se lo, phir inputs check karo (right rows/rate?). Agar summary mein figures hain bina
> visible calculation ke, puchho number kahan se aaya.

**"Would I confidently put my name on this?"** Agar jawab na hai, kaam ready nahi hai.

Kabhi honest jawab "I am not sure" hota hai — case unclear hota hai, plainly wrong nahi. Job
applicants ka AI-ranked shortlist reasonable lagta hai, par pata nahi chalta ke do universities ke
graduates ko favor kiya ya nahi. 4 sawal pucho:

1. Kaun affected hai, including log jo result kabhi nahi dekhenge?
2. Unke liye kya galat ho sakta, aur kya wo pata kar sakenge?
3. Fair outcome kaisa dikhega?
4. Kya disclose hona chahiye, kisko?

Sab 4 answer kar sako to decide karo, likh lo. Na kar sako, escalate karo jiske pas decision owner
hai. **Guessing wo ek option hai jo unclear case ko tumhari mistake bana deta hai.**

**AI work automate kar sakta hai. Accountability automate nahi kar sakta.**

Agar AI-assisted system harmful decision le, operating organization phir bhi responsible hai. Agar
coding assistant security flaw introduce kare aur engineer ship kare, engineer + organization
dono result own karte hain.

> **Where this leads:** Diligence hi wajah hai Agent Factory **governance-first** hai. System
> scale par: creation diligence → data rules/access control/approved-tool policy; transparency
> diligence → disclosure/UX design; deployment diligence → evaluation gates/audit logs/
> monitoring/human review. Policy sirf tab chalti hai jab approved tool utna hi easy ho jitna wo
> tool jo log already open rakhte hain. Mode 2 mein yeh responsibility product mein build hoti
> hai. Aage: System of Record, Designing the Vertical SoR.
