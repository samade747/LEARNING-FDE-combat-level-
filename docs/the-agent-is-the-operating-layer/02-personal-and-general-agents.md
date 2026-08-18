# 02 — Personal Agents vs General Agents — Do-Layer Model

## 5. Personal Agents Aur General Agents

AI Operating Layer mein do tarah ke agents rehte hain. Inhein confuse karna baqi architecture ko samajhna mushkil bana deta hai.

Dono usi layer mein rehte hain jahan insaan ab khara hota hai. Ek **kaam** ki taraf oriented hai. Doosra **insaan** ki taraf.

**General agents operators hain. Woh kaam karte hain.**

Developers ke liye misalein: Claude Code aur OpenCode — banate hain, test karte hain, refactor karte hain, deploy karte hain. Knowledge workers aur domain experts ke liye: Claude Cowork aur OpenWork jaise tools — research, analyze, likhte, aur coordinate karte hain.

General agent koi product se juda chatbot nahi hai. Yeh reason kar sakta hai, tools use kar sakta hai, aur asli environment mein kaam complete kar sakta hai. Aap isay ek task ke liye call karte ho. Yeh task execute karta hai. Session khatam ho jata hai. Yeh ek **task-scoped specialist** hai.

**Personal agents aapke delegate hain. Woh aapko jaante hain.**

Yeh aapke sath rehte hain, aapka context hold karte hain, aage ki planning karte hain, aur bohat sare tasks ke across act karte hain. Yeh category RTX Spark ke around banna shuru ho chuki hai. Independent agent makers — **OpenClaw** aur **Nous Research ka Hermes** — ne Windows-native agents is stack par commit kiye hain. Yeh is fall pehle RTX Spark laptops ke sath nazar aane wale hain.

Personal agent **aap** ki taraf oriented hota hai, ek task ki taraf nahi. Yeh private aur local reh sakta hai. Yeh aapka kaam aur preferences yaad rakhta hai, proactively act karta hai, aur aapki apps/files ke across phaila hota hai. Yeh layer ke andar aapka **standing representative** hai.

Mil kar yeh agents ek **operator aur delegate** banate hain. *Agent Factory Thesis* is structure ko formalize karti hai — **Two-Layer Model** ki tarah:

- **Edge Layer** — yahan personal agent baitha hota hai jo principal (insaan) ko represent karta hai. Thesis is self-sovereign agent ko **Identic AI** kehti hai: ek agent jo aap **own** karte ho, rent nahi.
- **AI Workforce Layer** — neeche AI Workers ka workforce hota hai jo asli kaam karta hai.

Thesis inke lifespan, memory, initiative, multiplicity, aur governance mein farq explain karti hai. Yeh paper ek narrower sawal poochta hai: **is split ka interface par kya asar hota hai?**

### Ek Load-Bearing Relationship

Interface argument ek relationship par khara hai. Aap **general agents (Claude Code, OpenCode) se personal agent ko banate aur manage karte ho.** Yeh tools uski memory, permissions, aur skills configure karte hain.

Runtime par yeh relationship **ulti** ho jati hai. Personal agent aapki intent samajhta hai, general agents aur AI Workers ko dispatch karta hai, aur wapis report karta hai. Aap developer tools se apne "chief of staff" ko manage karte ho. Chief of staff baqi sab kuch manage karta hai.

Thesis isay apne **two modes of general-agent use** ki tarah develop karti hai.

### Klarna: Ek Real-World Proof (Chhoti Scale Par)

Yeh sirf ek forecast nahi hai. Ek chhoti version already bare scale par chal chuki hai.

2024 mein Klarna ne apne customer service ke saamne ek AI agent laga diya. Usne **do-tihaayi** (two-thirds) sare chats handle kiye — pehle mahine mein 2.3 million conversations sameet. Klarna ne kaha ke us agent ne roughly 700 full-time employees ke barabar kaam kiya. Average resolution time 11 minute se ghat kar 2 minute se kam ho gaya. Company ne isay ~$40 million annual profit improvement ka credit diya.

Yeh **agents ko diye gaye kaam ki economics** dikhata hai. Lekin yeh **boundary** bhi dikhata hai. 2025 tak, Klarna ne complex cases ke liye human agents wapis laa diye. Customer service relatively structured kaam hai, phir bhi ek human floor bacha raha.

**Sabaq dono taraf jata hai.** Substitution bara hota hai jab task bounded ho. Yeh kamzor hota jata hai jab kaam ambiguous, regulated, ya irreversible ho jaye. Leading edge aage barh raha hai, lekin poora front ek sath collapse nahi ho raha.

### Second Consequence: Agents "Means of Production" Bhi Hain

Chip launches ek dusra consequence implied karte hain jo shayad hi naam liya jata hai: general agents sirf naya interface nahi — yeh **naya production ka zariya (means of production)** bhi hain.

Manufacturing mode mein, jise thesis **Mode 2** kehti hai, ek general agent baqi system banata hai — specialized AI Workers aur woh personal agent jo unhein coordinate karta hai.

Layer **recursive** hai: jin agents se aap baat karte ho, woh un agents ko bana sakte hain jo asli kaam karte hain. Yehi recursion **AI-Native Company** ko drive karti hai.

Thesis is idea ko ek line mein compress karti hai: **log direction set karte hain, agents kaam karte hain, aur companies headcount ki jagah intelligence scale karti hain.**

Thesis **architectural** case banati hai — kaun kaam karta hai aur workforce kaise banti hai. Yeh paper **interface** case banata hai — kaam kahan hota hai. Yeh app-on-an-OS se hat kar seedha operating layer mein move karta hai.

[What You Carry In](../what-you-carry-in/README.md) teesra piece complete karta hai — **ownership** ka case: practitioner khud kya hold kar sakta hai jab model rented ho, runtime badalta rahe, aur method ek kitab mein free diya ja raha ho.

## 6. Computer Jo Khud Ko Control Kare

CNN ne RTX Spark moment ko seedhe alfaaz mein describe kiya: duniya ki sabse bari technology companies unn computers par daaw laga rahi hain jo **khud ko control karte hain**. Yeh phrase promise aur dar dono capture karta hai.

Ek computer jo — aapki intent lene ke baad — khud ko control kare, yehi AI Operating Layer ka waada hai. Chaar dahaiyon ki human-run computing training ne humein is idea ko pareshan-kun banaya hai.

Mechanism concrete ho raha hai. RTX Spark ~1 petaflop local AI compute aur 128GB tak unified memory deta hai. Yeh powerful models aur autonomous agents ko device par chalne deta hai, bina har task cloud bheje.

NVIDIA ka OpenShell runtime control karta hai ke agent kya kar sakta hai. Yeh sensitive kaam ko local models ki taraf route kar sakta hai aur kuch bhi device se bahar jaane se pehle personal information hide kar sakta hai. Microsoft bhi agents ko Windows mein ek shared security layer ke through wire kar raha hai jo decide karti hai kya local rahe aur kya cloud ja sakta hai.

NVIDIA isay "tool se teammate tak" ka move kehta hai. Microsoft isay PC ka naya chapter kehta hai. Dono ek hi cheez describe kar rahe hain: machine ek instrument hona chhod kar ek **actor** ban jati hai jise aap direct karte ho.

Lap par woh petaflop khoobsurat windows render karne ke liye nahi hai. Yeh ek aise computer ko support karta hai jo goal hold kar sake, reason kar sake, plan kar sake, aur locally act kar sake — privately aur continuously.

---
[⬅ Piche: Chalis Saal Purana Stack](01-the-forty-year-stack-and-the-ai-operating-layer.md) · [⬆ Index](README.md) · [Agla: Yeh Baar Alag Kyun Hai ➡](03-why-this-time-is-different.md)
