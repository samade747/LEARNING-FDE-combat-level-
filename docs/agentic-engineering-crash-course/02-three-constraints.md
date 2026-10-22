# 02 — Teen Constraints Jo Har Coding Agent Ko Milti Hain

Coding agent ek magical engineer nahi — ek model hai [harness](../harness-engineering/README.md)
mein wrapped. **3 properties** har workflow ko shape karti hain.

## 2.1 Smart Zone Aur Dumb Zone

Model agle **token** predict karte waqt context window ke **har** doosre token ko weigh karta hai.
Har token ka **attention budget** fixed hota hai. N tokens ki window mein ~N² attention relationships
competing hoti hain.

Session shuru mein agent **smart zone** mein hota hai — sharp, focused. Session barhti hai, har
token ka signal competitors se **dilute** hota hai — agent **dumb zone** mein drift karta hai: schema
bhool jata hai, fields invent karta hai, apni earlier reasoning se contradict karta hai. **Same model,
same parameters** — bas plate par zyada mouths.

**Practical ceiling**: frontier models bhi, chahe 200k ya 1M window ka marketing claim ho, coding ke
liye **advertised window se bohot neeche** rehte hain. Practitioner reports **~100k tokens** waterline
par converge karte hain. Bare window help karti hai **retrieval** mein, **reasoning horizon** utne
factor se nahi extend karti.

```
turn  5  → schema paste (8 fields)
turn  9  → agent User.email correctly use karta hai
turn 47  → context ~80k tokens
turn 52  → agent likhta hai user.emailAddress  ← field exist nahi karta
turn 55  → agent invent karta hai user.preferences
           ⇒ smart zone exit ho gaya.
           ⇒ /clear, fresh session mein schema dobara paste karo.
```

Same model, same prompt turn 52 par jo turn 9 par tha. **Sirf attention budget badla.** Cure push
karna nahi — **har unit of work smart zone ke andar fit karo**, khatam hone par session throw away
karo.

## 2.2 The Memento Problem

Models **stateless** hain — koi bhi cheez provider requests ke across carry nahi hoti. Session ke
andar continuity harness re-feed karta hai; sessions ke **across** continuity koi **memory system**
disk par likhti hai.

Yeh **feature** hai. Sab se reliable cheez: **context clear karna agent ko ek known-good state par
wapis le jata hai.** Jo agent 40 turns dumb-zone mein drift kiya, wahi agent `/clear` ke 5 second
baad fresh attention budget ke sath excellent kaam karta hai.

**2 recovery tareeqe:** **Clearing** (session khatam, naya shuru — total reset) vs **Compaction**
(purani session summarize, naya seed — lossy). Developers compaction pehle try karte hain (kam
destructive lagta hai) — is instinct ko suspicious samjho: **compaction dumb-zone reasoning ka kuch
hissa carry karti hai.** Clearing + chhota written **handoff artifact** (PRD, ticket, AGENTS.md) agli
session ko **same starting state** har baar deta hai.

> **Working principle:** Agent ko *Memento* ke protagonist ki tarah treat karo. Uska bhoolna plan
> karo. Har zaroori fact **environment** mein survive kare (AGENTS.md, CONTEXT.md, Skill, ticket),
> chat history mein nahi.

## 2.3 Jagged Intelligence

Pehle 2 constraints **kitna** attend kar sakta hai ke baare mein hain. Teesra **kya** mein acha hai
ke baare mein hai — aur yeh engineers ko sabse zyada surprise karta hai.

LLMs **jagged** hain — uniformly smart nahi, kuch domains mein sharply peak karte hain, doosron mein
stagnate. State-of-the-art model ek lakh-line codebase refactor kar sakta hai **aur usi session mein**
50 meter door car-wash tak chalne ki jagah drive karne ki advice de sakta hai. Dono abilities sirf
is baat se connected hain ke labs ne kaunsi RL environments par train kiya.

Frontier models heavily RL se train hote hain **verifiable** tasks par (math, compiling code, formal
proofs) — reward signal clean hai, model un circuits mein brilliantly seekhta hai. Baaqi jagah,
pre-training intuition par chalta hai, bina comparable correction ke.

**4 operational implications:**

1. **Code lucky domain hai.** Tum ek deepest peak par kaam kar rahe ho — isliye nahi ke coding
   intrinsically aasan hai, balke labs ne isay economically prioritize kiya. Peak se bahar, same
   model confidently ghalat ho sakta hai aisi cheez mein jo bachha bhi jaanta hai.
2. **Feedback loops tumhe verifiable circuits mein rakhte hain.** Static types, tests, lints — wahi
   reward signal jis par model trained hua. Tests fail hote dekhna agent ko training ki strongest
   shape mein operate karata hai. Yehi Failure 3 aur `tdd` Skill ka deeper reason hai.
3. **Tumhe pata hona chahiye kaunse circuit mein ho.** Jab agent aisa kuch kare jo junior engineer
   nahi karega, usually tum peak se bahar wander kar gaye ho.
4. **Fresh shuru karte waqt, stack choose karo jo peak ke andar land kare.** Boris Cherny: Claude
   Code TypeScript+React mein hai kyunke "it's very on distribution for the model." Mainstream
   choices (Python/TypeScript, Postgres, popular frameworks) prefer karo — **apni agent workforce**
   ke liye choose kar rahe ho, sirf apne liye nahi.

> **Animals vs Ghosts.** Karpathy LLMs ko **ghosts** kehta hai, **animals** nahi — statistical
> simulations, biological intelligence nahi. Isliye: agent par chillana improve nahi karta,
> sympathy improve nahi karti, "think step by step" dormant cognition nahi jagata. Jo kaam karta
> hai: agent ko ek peak par rakhna (clear context, verifiable feedback, well-named code, precise
> spec) — **agent psychology ko physics samjho, personality nahi.**

---
[⬅ Vibe Coding → Agentic Engineering](01-vibe-coding-to-agentic-engineering.md) · [Agla: Six Failure Modes ➡](03-six-failure-modes.md)
