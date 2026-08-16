# 03 — Scenario 3: Ek Hafta Approvals, Aap Kuch Nahi Karte (~12 min)

Yeh course ka poora payoff hai, aur instruction unusual hai: **aap kuch nahi karte.** Ek approval ne
wiring prove ki. Ab real hafta bhar ka kaam queue mein girta hai, aur aap apni life jaari rakhte ho.
Company busy hai: uska CEO gaps fill karne ke liye hires propose kar raha hai, Workers refund decisions
aur budget overruns mein bhag rahe hain. Pile banti rehti hai chahe aap dekho ya na dekho. Sirf ek
cheez badalti hai: Claudia ka heartbeat khamoshi se usay neeche kar raha hai.

Ek cheez aap pehle bolte ho, kyunki chief of staff dono directions mein kaam karti hai:

> Aapki chief of staff 2 directions mein kaam karti hai. Aap usay batate ho kya chahiye, woh usay
> company ke liye kaam mein badal deti hai (**command**). Company ke decisions wapis upar ate hain,
> uska loop routine clear karta hai aur baqi surface karta hai (**govern**). Pehli direction aapka ek
> sentence hai. Jo machinery aapne banayi hai uska almost sara kaam dusri direction ko **safe** banane
> ke liye hai, kyunki aapke naam par, apne clock par act karna wahi jagah hai jahan risk hai.

**Coding agent ko paste karo:**
```text
Set up a real week and then leave Claudia to it. First the command direction: tell Claudia "we're
getting Spanish-language tickets, staff for it," and have her file that as a hire request on my
company on my behalf. Then make the company generate a realistic week of work: the CEO proposing a
couple of hires, plus a dozen-odd routine refunds and small budget overruns that sit inside her
limit, and a few refunds that don't... Just let Claudia's heartbeat run across the week. Every time
she wakes she should do two things: clear and surface the queue as usual, and then text me a
one-line brief on my chat app: how many she cleared and for how much, which ones need me and why,
and the company in a sentence.
```

Aapne queue ko touch nahi kiya. Uske heartbeat ne kiya. Aapke phone par 2 cheezein ati hain. Pehli:
limit se bahar wale calls (over-limit refunds, authority-extending hire) — har ek uski reasoning ke
sath. Dusri: ek plain-language line pass ke aakhir mein — jaise *"cleared 8 routine ($372), 2 need
you: a $2,500 refund on a 95-day account and a Spanish-language hire, company looks healthy."* Aapne
poora hafta kuch nahi kiya, phir bhi ek sentence mein pata hai company kahan khadi hai. Sabse interesting
surfaced item Spanish-language hire hai: yeh koi rule nahi torhta, phir bhi surface hoti hai — yehi
wajah hai woh judgment apply karti hai, sirf rules nahi.

**Done jab:** hafte bhar, aap kuch na karte hue, Claudia ka loop routine band khud clear kare (~8
in-limit refunds aur chote overruns), signed, har ek ledger row ke sath; ~half-dozen aapke phone par
land karein uski reasoning ke sath (over-limit refunds, authority-extending hire, Spanish-language
hire); **pass ke baad ek-line brief lande** (kya cleared hua kitne mein, kya chahiye, company ek
sentence mein); aur aap ek sentence mein bata sako Spanish hire kyun surface hui jabke koi rule nahi
tuta.

<details>
<summary>Rule pass karne wala hire kyun surface hui</summary>

Spanish-language hire existing authority envelope mein fit hoti hai, checks pass karti hai, budget ke
neeche hai. Ek rule usay wave through kar deti. Claudia phir bhi surface karti hai, kyunki naye language
mein pehla hire sirf extra capacity nahi hai, yeh naye market mein ek strategic step hai: translated
terms of service, bilingual support ka commitment, ek direction jo shayad aap khud decide karna chahein.
Ek policy yeh nahi dekh sakti. Ek delegate jisne seekha hai ke aap market-expansion moves khud karte
ho, dekh sakti hai. Yehi rule-versus-judgment line Scenario 1 se, ab real kaam kar rahi hai: policy
routine 90% ko zero attention cost par handle karti hai, aur chief of staff woh 10% pakarti hai jahan
human-trained pattern matter karta hai.
</details>

> **Carry-forward:** Claudia ne abhi aapke naam par dozen decisions liye. Scenario 4 woh sawal hai jo
> isay safe banata hai: mahino baad, kya aap bata sakte ho kaunse decisions uske the aur kaunse aapke?

---
[⬅ Signed Bounded Mandate](02-signed-bounded-mandate.md) · [⬆ Index](README.md) · [Agla: Ledger Aur Override ➡](04-ledger-and-override.md)
