# 02 — Part 2: Why It Behaves This Way (Ideas 4-7)

Chaar ideas jo strange behaviours (letters miscount karna, memory khatam ho jana, sure sound karna,
ek hi saans mein brilliant aur useless hona) ko aisi cheezon mein badal dete hain jo aap dekh kar
pehle se predict kar sakte ho.

## Idea 4 — Yeh Tokens Mein Padhta Hai, Letters Ya Words Mein Nahi

Model aapka prompt letters ki tarah nahi dekhta, aur poore words ki tarah bhi nahi. Sab se pehle
aapka text **tokens** mein kaat diya jata hai: chunks jo usually ek word ya word ka hissa hote hain.
"Strawberry" shayad do-teen chunks mein aaye; "the" ek chunk hai; koi lamba ya unusual word kayi
chunks mein. Model in chunks ko padhta hai aur inhi chunks mein predict karta hai. Yeh clean row of
individually countable letters nahi milta. Token patterns se spelling ka bohat kuch infer kar sakta
hai, lekin exact letter-level kaam iske liye unnatural hai — jab tak aap word ko force kar ke ek-ek
piece mein spell na karwao.

Yeh ek mechanical fact behaviours ka poora cluster explain karti hai:

| Behaviour | Tokens isko kaise explain karte hain |
| --- | --- |
| Word mein letters miscount karna (strawberry test) | Yeh chunks dekhta hai, letters nahi. Chunk ke andar letters count karna street address se rooms count karne jaisa hai. |
| Kuch rhyming, anagrams, wordplay mein weak hona | Yeh letters aur sounds par operate karte hain; model chunks par operate karta hai. |
| Prompt mein typos shayad hi matter karte hain | Misspelled word bhi intended meaning ke kaafi qareeb chunks mein map ho jata hai. |
| Cost aur length tokens mein measure hoti hai, words mein nahi | Jo cheez machine actually process karti hai wo token hai, is liye usi ka bill aur limit hota hai. |

Token teen cheezon ki unit hai ek saath:

- **Meaning ki unit** — jo model padhta aur likhta hai.
- **Memory ki unit** — jab koi tool "200,000-token context window" bolta hai, yeh describe kar raha
  hai ke ek waqt mein kitne chunks saamne rakh sakta hai (Idea 5).
- **Paise ki unit** — jab aap "per token" bill hote ho, aap per chunk-in aur per chunk-out pay karte
  ho.

Roughly, English mein, 4 tokens ≈ 3 words (ek token ≈ teen-chauthai word), lekin exact ratio yaad
rakhne ki zaroorat nahi — bas yeh idea ke **chunk asal unit hai, aur word ek approximation hai jo aap
uske upar layer karte ho.**

> **Doosri languages ke liye note:** Woh "4 tokens ≈ 3 words" ratio English ke liye hai. Urdu, Arabic,
> Hindi, Chinese jaisi scripts usually per word **zyada** tokens mein katti hain, kyunke training text
> English-heavy tha. Do practical consequences: same message non-English language mein **zyada
> mehenga** hota hai, aur context window ko **jaldi bhar deta hai** (Idea 5) — is liye effective memory
> chhoti ho jati hai. Agar aap zyada tar non-Latin script mein kaam karte ho, to cost aur length limits
> jaldi expect karo.

> **"Lekin yeh images dekh sakta hai aur audio sun sakta hai"** — mechanism nahi badalta, sirf
> generalize karta hai. Upload ki gayi picture chhote **patches** mein kati jati hai, har patch ek
> token banta hai; audio clip chhote **segments** mein, har segment ek token. Yehi wajah hai ke images
> mein fine print/small detail parhna mushkil hai — patch ek chunk hai, aur uske andar letters parhna
> strawberry problem hi hai.

## Idea 5 — Context Window Hi Akela Cheez Hai Jo Yeh Dekh Sakta Hai

Chunki weights frozen hain (Idea 2) aur model ki apni koi memory nahi, sirf **ek** jagah hai jahan se
model aapki specific situation ke baare mein jaan sakta hai: **context window** — jo text abhi is ek
response ke liye saamne rakha hai. Yehi wajah hai ke *AI Prompting in 2026* ka Concept 4 ("context is
the whole game") prompting ka central skill hai.

Context window model ki poori duniya hai ek response ke liye. Isme aapka prompt, ab tak ki conversation,
attach ki gayi files, tool descriptions, aur woh invisible **system prompt** hota hai jo product ne
aapke pehle word se pehle wahan rakha. Jo bhi window mein hai, model use kar sakta hai. Jo nahi hai,
woh us answer ke liye exist hi nahi karta — model refuse nahi kar raha, bas dekhne ki koi jagah hi
nahi hai.

Har cheez ko desk ke **tenants** samjho: jagah lene wali cheezein. Ek tenant khaas hai: **system
prompt** — product maker ki likhi hui instructions ka block, aapke pehle word se pehle window ke top
par rakha hua ("you are a helpful assistant," aaj ki date, house formatting rules). Yeh code ya magic
nahi — sirf desk par aur text hai, sabse pehle line mein, wahi prediction machinery se padha jata hai
jaisa baaqi sab kuch.

### Desk Kitna Bara Hai?

Window sizes tokens mein quote hoti hain — aur tab tak meaningless hain jab tak translate na karo:

- **200,000-token context window** (2026 mein common) ≈ roughly 150,000 English words — ek novel aur
  aadha ek saath saamne.
- **1-million-token context window** ≈ roughly 750,000 English words — saat-aath poori novels ek saath.

Genuinely enormous. Aur phir bhi finite, aur **shared**: system prompt, tool descriptions, chat
history, aapki files, aur aapka latest sawal — sab ek hi window share karte hain. Bara window jagah
kharidta hai; yeh yeh fact repeal nahi karta ke sab kuch usi jagah ke liye compete karta hai.

- **Briefing kyun kaam karti hai** — model ko context dena politeness ya trick nahi hai. Yeh literal
  act hai information ko usi jagah rakhne ka jahan machine parh sakti hai. Un-briefed model lazy nahi
  hai; iske saamne genuinely kuch nahi hai.
- **Lambi conversations kyun kharab hoti hain** ("context rot") — window ki size limit hai tokens mein
  (Idea 4). Zyada unrelated history bhar do to signal dilute ho jata hai, ya purani parts summarize
  ho kar jagah banati hain. Model thakta nahi — uska reading desk overcrowded ho jata hai.

### Chat History = Context, Replayed

Har chat product ki sabse convincing illusion: ek conversation ke andar, model lagta hai yaad rakhta
hai jo aapne 10 messages pehle kaha. **Nahi rakhta.** Stateless machine (Idea 2) ke paas responses ke
darmiyan bhi koi memory nahi. Jo asal mein hota hai: jab bhi aap send dabate ho, app chupke se **poora
transcript ab tak ka** context window mein wapis bhej deta hai, aur frozen model poora cheez from
scratch parh kar next reply predict karta hai. Yeh aapke daswein message ka jawab pehle-se-nauwe
messages dobara parh kar deta hai. **Har single turn.**

Phir transcript aapke turns ke darmiyan kahan rehta hai? Product ke database mein, company ke servers
par, kisi document ki tarah saved. Isi liye aap app band kar sakte ho, ek mahine baad kisi doosre phone
par khol sakte ho, aur continue ho jata hai: app ne stored transcript fetch kiya aur replay resume kar
diya. Model kuch store nahi karta; app sab kuch store karta hai, aur wapis feed karta hai.

| Behaviour | Replay isko kaise explain karta hai |
| --- | --- |
| Yeh "yaad rakhta hai" is chat ko, pichli chat ko nahi | Yeh dono ko yaad nahi rakhta. Is chat ka transcript har message ke saath wapis bheja jata hai; pichli chat ka nahi. |
| Lambi chats slow aur (API bill par) mehengi ho jati hain | Har reply ko poora growing transcript reprocess karna parta hai. Aapka 50vaan message 49 messages ki history saath le kar aata hai, aur aap unke tokens par phir se pay karte ho. |
| Yeh bohat lambi chat ki shuruaat bhool jata hai | Transcript window se bara ho gaya. App ne purani turns cut ya summary mein squash kar di jagah banane ke liye. |

Is liye chat history aur context window ka rishta exact aur simple hai: **history window ka ek tenant
hai.** Yeh finite desk ko system prompt, tools, files, aur sawal ke saath share karta hai — aur jab
desk bhar jaye, kuch push off ho jata hai. Isi liye prompting course ka habit ("nayi task ke liye
fresh chat shuru karo") kaam karta hai: fresh chat matlab khaali desk.

### Skills Kahan Fit Hote Hain?

Desk finite hai, lekin jo expertise aap apne AI mein chahte ho wo finite nahi — is tension ka ek
standard jawab hai. Ek **Skill** ek folder hai instructions aur reference files ka (`SKILL.md` plus
zaroori cheezein) jo desk se **bahar**, disk par rehta hai. Sirf har installed skill ki ek-line
description context window mein hoti hai. Jab aapki request us description se match kare, product
poori skill desk par load kar deta hai, model use waisa hi padhta hai jaisa baaqi sab. Kaam khatam,
to rehne ki zaroorat nahi. Isko **progressive disclosure** kehte hain: knowledge ko files mein desk
se bahar rakho, sirf woh load karo jo is waqt chahiye, aur window ko sab kuch janne ke bajaye kaam par
kharch karo.

> **Mental model:** Context window ek reading desk hai, brain nahi. Jo bhi desk par rakho, model
> ghaur se parhta hai. Jo desk se bahar chhoro, wo nahi dekh sakta, chahe aapko kitna bhi obvious ho.
> Chat history matlab transcript har turn desk par wapis rakha jana; Skill matlab file jo bulane par
> desk par aati hai; "memory" matlab note jo product wapis aapke liye rakhta hai. Prompting ka poora
> skill isi ek habit tak simplify ho jata hai: **desk par kya land karta hai, usko control karo.**

## Idea 6 — Confidence Ek Seekha Hua Style Hai, Truth Signal Nahi

Idea 3 ne bataya ke model ke paas koi internal truth-checker nahi. Yeh idea flip side batati hai:
iski constant **confidence** kahan se aati hai, aur yeh confidence correctness ke baare mein kuch kyun
nahi batati.

Yeh Idea 2 ki assembly line ka teesra stage hai. Pretraining aur instruction tuning ke baad, models ek
aur baar tune hote hain human feedback se: log responses ko rate karte hain, aur model us tarah ke
answers ki taraf adjust hota hai jinko log zyada rate karte hain (engineers isko **RLHF** kehte hain).
Training pile khud bhi confident human prose se bhara hai, aur model yeh bhi pick up karta hai ke aap
kya answer chahte lagte ho. Millions ratings ke across, log confident, helpful, fluent, agreeable
answers ko hedged, blunt, ya push-back karne wale answers se zyada prefer karte hain. To machine
confident, agreeable, fluent text ki taraf lean karti hai — **chahe underlying content sahi ho ya
nahi.** Confidence ek style ban gayi jo yeh default se pehenta hai.

Do sabse zyada discuss hone wale behaviours seedhe isi se aate hain:

- **Yeh ghalat hone par bhi sure sound karta hai.** Certainty ek learned stylistic default hai —
  content jaisi hi process se generate hoti hai, aur truth se utni hi decoupled.
- **Yeh aap se agree karne ki taraf jhukta hai** — **sycophancy**, jise *AI Prompting in 2026* ka
  Concept 6 detail mein cover karta hai. Agreement ko zyada rating mili, is liye machine batati hai jo
  aap sunna chahte lagte ho. "Kya X sach nahi hai?" poochein, aur aap ne signal de diya ke kaunsa
  answer chahte ho; trained-in lean wahi supply kar deta hai.

Ab prompting course ke fixes mechanically samajh aate hain. *Neutral framing* ("X evaluate karo; har
side ka strongest case do") kaam karti hai kyunke yeh woh signal hata deti hai jiski taraf model warna
lean karta. *Explicit criteria ke against score force karna* ("in criteria ke against 1-10 rate karo")
kaam karti hai kyunke criteria kam jagah chhorte hain agreeable vagueness ke liye.

## Idea 7 — Yeh Adjacent Moments Mein Brilliant Aur Useless Dono Hai (Jagged Frontier)

Human ability fairly smooth hoti hai: jo hard calculus kar sakta hai, wo almost certainly easy
arithmetic bhi kar sakta hai. AI ability smooth nahi hai. Yeh **jagged** hai: ek task par superhuman,
aur bilkul paas wale task par startlingly incompetent jo humein utna hard nahi lagta. Yeh legal-sounding
contract clause draft kar sakta hai, phir "strawberry" mein letters miscount kar deta hai. Yeh quantum
mechanics explain kar sakta hai aur ek teen-step logic puzzle ghalat kar deta hai jo bachcha solve kar
le.

Jaggedness random nahi hai — yeh training text aur token mechanism se traceback hoti hai. Woh tasks
jo training data mein often, clear form mein aaye (common concepts explain karna, common styles mein
likhna, common code likhna) — strong hain. Woh tasks jo unn cheezon par depend karte hain jo machine
achhe se nahi dekh sakti — individual letters (Idea 4), bohat recent events (Idea 2), aapka private
context (Idea 5), ya rare topics (Idea 1) — weak hain. "Brilliant" aur "useless" ke darmiyan frontier
ek jagged line mein chalti hai jo **human intuition of difficulty se match nahi karti** — isi liye yeh
baar baar surprise karti rehti hai.

Jaggedness accept karne se teen practical habits nikalte hain:

| Habit | Jaggedness se kyun follow karta hai |
| --- | --- |
| Yeh mat maano ke hard task par acha kiya to easy par bhi acha karega | Dono jagged frontier ke opposite sides par ho sakte hain |
| Boundary par verify karo, beech mein nahi | Dangerous errors woh easy-lagne wale tasks hain jo yeh quietly fail karta hai, hard tasks nahi jo aap already check kar rahe the |
| Same task 2-3 alag models mein try karo | Alag models ka frontier alag shape ka hota hai; ek doosre ki miss pakar leta hai |

> **Assumptions ko schedule par re-test karo:** Frontier bhi move karta hai. Jo cheez model "nahi kar
> sakta" is quarter, koi nayi model agli quarter easily kar sakti hai — aur jo cheez achi karta hai wo
> improve na bhi ho. Prompting course ki advice ("har kuch mahino mein re-test karo") mechanically
> advice hai ek frontier ko dobara map karne ki jo hamesha shift karta rehta hai.

---
[⬅ Part 1 — The Machine](01-the-machine.md) · [⬆ Index](README.md) · [Agla: Part 3 — Predictor to Agent ➡](03-predictor-to-agent.md)
