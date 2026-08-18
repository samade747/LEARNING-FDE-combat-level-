# 01 — Part 1: The Machine (Ideas 1-3)

Teen ideas ke baare mein ke jab aap "send" dabate ho to literally kya ho raha hai. Yeh teen samajh
lo, aur AI ke behaviour ka do-tihaai hissa surprising rehna band ho jayega.

## Idea 1 — Yeh Next Piece Predict Karta Hai, Lookup Nahi

Poore course ki sabse important line yeh hai: **language model ek machine hai jo, kuch text diya
jaye, to predict karta hai ke aage kaunsa text sabse plausible aata hai, ek chhoti si piece ek waqt
mein.** Yehi core mechanism hai. Baqi sab isi ka natural result hai.

Zyada tar log sochte hain AI ek bohat tez librarian ki tarah kaam karta hai: aap sawal poochte ho, wo
apni vast internal encyclopedia mein se relevant fact dhoondta hai, aur wapis parh deta hai. Yeh
mental model **ghalat** hai, aur AI ke saath zyada tar mistakes isi galat model se aati hain.

Asal mein jo hota hai wo duniya ke sabse well-read autocomplete jaisa hai. Aapne autocomplete dekha
hoga "Happy birthday to..." ko "you" se complete karte hue. Language model bhi yehi karta hai, bas
itni zyada text par trained hai ke *kisi bhi* prompt ko continue kar sakta hai, sirf common phrases
nahi. Yeh ek waqt mein ek word nahi, ek **token** continue karta hai (Idea 4). Har piece wapis khud
mein feed hoti hai next piece decide karne ke liye. France ki capital poochein, to yeh koi database
row `France → Paris` lookup nahi karta — yeh woh continuation produce karta hai jo, jo kuch bhi usne
parha, uske hisab se "The capital of France is" ke baad sabse plausible aata hai, aur wo "Paris" nikla
kyunke yeh sequence training text mein lakhon baar aaya.

Well-worn facts ke liye prediction aur lookup same jawab dete hain, is liye farq academic lagta hai.
Farq academic rehna band ho jata hai jahan text patla ho jata hai:

- France ki capital poochein → plausible continuation *hi* sach hai. Prediction, knowledge jaisa
  lagta hai.
- Kisi self-published novel ka plot poochein jo sirf kuch sau copies bikin aur kabhi review nahi hui →
  koi well-worn continuation nahi hai, is liye model sabse *plausible-sounding* cheez produce karta
  hai, milte-julte books ko blend karke. Yeh phir bhi prediction hai. Bas iske paas predict karne ke
  liye kuch sach nahi hai.

Machine dono cases mein *exact wahi* kaam kar raha hai. Sirf aap farq bata sakte ho — aur sirf tab jab
aap jaante ho ke yeh kya kar raha hai.

> **Reframe carry karne wali baat:** Librarian ki tasveer bhool jao jo retrieve karta hai. Ek writer ki
> tasveer socho jo continue karta hai. Librarian jise kitab nahi milti wo bolta hai "hamare paas nahi
> hai." Ek writer jisko story continue karne ko kaha jaye, wo kabhi ruk kar yeh check nahi karta ke
> continuation *sach* hai ya nahi. Continue karna hi poora kaam hai. Isi liye AI kabhi "mere paas woh
> nahi hai" nahi bolta jaise librarian bolta — jab tak use specifically train na kiya jaye. Plausible
> continuation iska native act hai; truth uske upar layer ki gayi cheez hai, imperfect tareeqe se.

### "Stochastic" Ka Matlab

Model ek fixed next token predict nahi karta — yeh plausible next tokens ka poora spread predict
karta hai, har ek ki apni likelihood ke saath ("Paris" bohat likely, "the largest city in France"
possible, aur dusre options kam likely) — phir usi spread mein se ek **choose** karta hai. Engineers
isko **stochastic** kehte hain: output ek spread se *sample* hota hai, ek fixed answer ki tarah
compute nahi hota — is liye same input alag output de sakta hai har baar.

Yeh boldness kitni hai, isko **temperature** naam ki setting control karti hai. Low temperature almost
hamesha single most likely token leta hai — steady, repetitive. High temperature kam likely tokens
tak reach karta hai — varied, zyada creative, kabhi kabhi off. Zyada tar chat products beech ki value
use karte hain, isi liye same sawal do baar poochne par do alag-alag wording milti hai jo roughly same
matlab rakhti hain.

Yeh us "frequency equals reliability" rule ki mechanical root hai jo *AI Prompting in 2026* mein hai —
jitni baar koi true continuation training text mein aaya, model utni strongly usko predict karta hai.
Sparse topic → weak prediction → confident-sounding guess.

> **"Lekin ChatGPT web search kar sakta hai, kya yeh lookup nahi karta?"** Product kar sakta hai; model
> phir bhi nahi karta. Modern tools predictor ko extras mein wrap karte hain (web search, file
> reading, code execution, memory note) aur yeh extras real, current facts fetch kar sakte hain.
> Lekin facts context window mein land karte hain (Idea 5), aur model unko answer mein badalta hai
> apne ek hi tareeqe se: unse continuation predict kar ke. "Yeh predict karta hai, lookup nahi" wala
> baat machine ke beech mein sach rehta hai, chahe system ne abhi kuch lookup kiya ho.

## Idea 2 — Yeh Padh Kar Seekha, Phir Seekhna Ruk Gaya

Predictions kahan se aayein? **Training** se: model ko bohat zyada human text dikhaya gaya, aur wo
baar baar apne aap ko adjust karta raha taake us text ki agli piece behtar predict kar sake. Yehi
adjustment process hi hai jisme model kuch "seekhta" hai. Training khatam hone par result ek fixed set
of internal numbers mein freeze ho jata hai (engineers inko **weights** ya **parameters** kehte hain)
jo dobara kabhi nahi badalte.

Training pile mein internet ka bara hissa, digitized books, open-source code, encyclopedias, academic
papers, forum archives shamil hote hain — trillions of tokens, jitna ek insaan hazaar zindagiyon mein
bhi na parh sake. Yeh pile kahan se aaya, kis permission se — yeh ek live public dispute hai (authors
aur publishers ne sue kiya hai). Practical takeaway yeh hai: model ne ek bohat bara, uneven pile parha
— iski strengths aur blind spots usi pile ki hain. Jahan pile thick tha, wahan achi prediction; jahan
patla tha, wahan guess (Idea 1).

### Training vs Inference

- **Training** — one-time education, ek baar, past mein, company ne ki. Expensive, slow, finished.
- **Inference** — jo har baar hota hai jab **aap** use karte ho: frozen weights aapke prompt par chalte
  hain continuation predict karne ke liye. Fast, cheap, aur — yeh crucial part hai — **iske andar kuch
  nahi badalta.**

Jab aap model ko conversation mein correct karte ho aur wo bolta hai "aap sahi hain, meri ghalti," to
usne kuch **seekha nahi**. Usne woh text predict kiya jo correction ke baad plausibly aata hai. Isi
conversation ke andar aapki correction help karti hai kyunke wo context window mein baithi hai (Idea
5) aur model wahan se continue karta hai. Lekin model ke andar kuch nahi badla. Chat band karo, agli
conversation exactly wahi frozen weights se shuru hoti hai, koi trace nahi ke correction hua tha. Aap
model ko nahi badal sakte.

### Knowledge Cutoff Aur Private World

| Consequence | Frozen weights se kyun follow karta hai |
| --- | --- |
| **Knowledge cutoff** | Training ek certain date par khatam hui; uske baad jo hua wo weights mein nahi hai. Model permanently ek brilliant expert hai jo ek specific din news parhna band kar chuka. |
| **Aapki private world nahi jaanta** | Aapki company ke numbers, calendar, kal ka email — yeh kabhi training text mein the hi nahi, is liye weights mein kuch nahi. Model chhupa nahi raha — information kabhi thi hi nahi freeze karne ke liye. |

### Frozen Kyun Rakha Gaya — Jaan-Boojh Kar

| Reason | Freeze kyun zaroori banata hai |
| --- | --- |
| **Cost** | Training expensive half hai — mahino ka computing, sau-crore dollars. Inference cheap half hai. Agar model har conversation mein relearn kare to expensive machinery har chat mein aa jaye. |
| **Safety aur testing** | Frozen model ek baar test hota hai, phir har user ke liye usi tested envelope mein rehta hai. 2016 ka ek famous chatbot jo live seekhta tha, ek din mein corrupt ho gaya aur band karna para. |
| **Consistency** | Lakhon log ek hi identical weights share karte hain. Aapke colleague ka model exactly aapka model hai; ek bug har jagah reproduce hota hai. |

Isi liye jab prompting course model ko **stateless** kehta hai — yeh word precisely lo, ek chosen
property ki tarah, missing feature nahi. Stateless matlab: apni koi memory nahi, har response frozen
weights + jo abhi saamne hai usse from scratch compute hoti hai, aur inference time par aap kuch bhi
karo, koi mark nahi chhorta.

> **"Memory" features kaise kaam karte hain?** Kuch products "memory" offer karte hain jo chats ke
> darmiyan yaad rakhta lagta hai. Yeh weights **nahi** badalta — wo inference time par abhi bhi
> impossible hai. Jo hota hai: product chupke se aapke baare mein **kuch facts text ki tarah save
> karta hai** aur har nayi conversation ke shuru mein wapis context mein daal deta hai (Idea 5). Model
> yaad nahi rakh raha; product ek note wapis feed kar raha hai.

## Idea 3 — Koi Alag Jagah Nahi Jahan Yeh Check Kare Ke Sach Hai

Ideas 1 aur 2 ko jorho aur woh fact milta hai jo logon ko sabse zyada frustrate karta hai. Ek human
expert ke paas do faculties hoti hain: ek jo answer **generate** karti hai, aur doosri, quiet wali jo
usko **check** karti hai: "ruko, kya main sure hoon? yeh maine kahan seekha? kya yeh sahi lagta hai?"
Dono disagree kar sakti hain.

**Model ke paas sirf pehli faculty hai.** Andar koi doosri machine nahi jo prediction ko truth ke liye
check kare aapke paas pahunchne se pehle. Wahi single process jo correct continuation produce karta
hai, incorrect bhi produce karta hai — koi internal flag nahi jo dono ko alag karta ho.

Yehi hai jise log **hallucination** kehte hain: fluent, confident, bilkul false statements. Yeh word
lagta hai jaise koi malfunction ho, koi glitch jise fix karna hai. Yeh glitch **nahi hai**. Yeh machine
ka bilkul waisa kaam hai jaisa banaya gaya: ek plausible continuation predict karna, jahan plausible
continuation sach nahi nikla. Ab aap dekh sakte ho *kyun* hota hai, pehli teen ideas se: machine ka
sirf ek act hai continue karna (Idea 1), yeh sirf uski taraf continue kar sakta hai jo frozen training
text mein thick tha (Idea 2), aur andar kuch result ko check nahi karta (yeh idea). Thin text + majboori
continuation + koi auditor nahi = confident invention.

> **Isi liye confidence par trust nahi kar sakte:** Model ka confident tone koi evidence nahi ke yeh
> sahi hai. Tone ek **style** hai jo confident human writing se seekha gaya (Idea 6 mein zyada); yeh
> content jaisi hi process se generate hota hai, aur truth se utna hi decoupled hai. Ek banaya hua
> statistic bhi utne hi assured voice mein aata hai jitna ek real. Yehi wajah hai ke *How to Think in
> the AI Era* course maujood hai — uska Error Taxonomy (Discipline 3) ek checklist hai un false
> continuations ko haath se pakarne ke liye jo machine khud pakar nahi sakti. Aap missing second
> faculty ho.

### Example — Tuition Academy Ki Fees

Ek parent ne AI se ek chhoti si local tuition academy ki exact fee schedule aur class timings poochi
— jiski koi website nahi thi, online presence bilkul nahi ke barabar. AI ne confident, neatly
formatted table banayi courses, timings, aur monthly fees ki. **Har figure ghalat/invented tha.** AI
ne jhoot nahi bola aur malfunction bhi nahi hua. Academy training text mein barely present thi, is
liye predict karne ke liye koi real schedule nahi tha — aur na hone par, machine ne wohi kiya jo yeh
kar sakti hai: sabse *plausible-looking* fees produce ki, usi confident voice mein jo verified facts
ke liye use karti hai. Iske paas koi second faculty nahi thi jo whisper kare "tum guess kar rahe ho."
Woh whisper aapko dena hoga.

---
[⬅ Overview](00-overview.md) · [⬆ Index](README.md) · [Agla: Part 2 — Why It Behaves This Way ➡](02-why-it-behaves-this-way.md)
