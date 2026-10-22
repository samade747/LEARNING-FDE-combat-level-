# 10 — Closing: The Strategic Programmer

Tumhara agent ek excellent **tactical** programmer hai — ek sergeant jo kisi bhi well-specified hill
le sakta hai, kisi bhi language mein, raat ke beech mein, aur subah tak ek working slice wapis la
sakta hai. Function/test likhna sikhana nahi parta — harness, model, tools pehle hi solve kar chuke
hain.

**Jo sergeant nahi kar sakta:** decide karna **kaunsi hill**. Yeh nahi bata sakta ke business ko
asal mein kis system ki zaroorat hai. Yeh nahi bata sakta ke teesra module jo tum maang rahe ho
ek alag module honi chahiye ya kisi existing deep module mein fold honi chahiye. Yeh architectural
map mahino/saalon tak zehan mein nahi rakh sakta — iske paas sirf current session aur disk par kuch
files hain.

**Sergeant se upar sab kuch strategic programmer ka role hai — tumhara role.** Stakeholder ke sath
align hona. Design concept banana. Slice choose karna. Interface design karna. Diff parhna. Map
hold karna. System design mein roz invest karna (Kent Beck ne 30 saal pehle insaanon ke liye likha,
ab human engineers + Digital FTEs ke hybrid workforce par lagu hota hai).

Chapter ki shuruat ki narrative — ke AI software fundamentals replace karti hai — **ghalat hai**
kyunke yeh confuse karti hai *code kaun likhta hai* ko *acha code kaisa dikhta hai* se. **Author
badla hai; standard nahi.** Codebases jo insaanon ke liye achi thi, agents ke liye bhi achi hain.
Jo bad thi, agents ke liye bhi bad hain — **aur worse, kyunke agents badness ko amplify karte hain.**

> **Purani kitabein parho:** *The Pragmatic Programmer. A Philosophy of Software Design.
> Domain-Driven Design. Extreme Programming Explained. The Design of Design.* Har page is technology
> se pehle ki hai, aur har page ab **zyada sharply** apply hoti hai jab se likhi gayi thi.

**Ek line carry karne layak hai, Karpathy se:** *"You can outsource your thinking, but you can't
outsource your understanding."* Agent typing karega, search karega, boilerplate, API-detail recall,
tedious refactor. Increasingly thinking bhi karega — options generate karega, weigh karega, drafts
likhega, experiments chalayega. **Jo uniquely tumhara rehta hai: understanding** — yeh system kyun
bana, kiske liye hai, kaun isay rely karta hai, yeh kya kabhi nahi karni chahiye. Understanding hi
agent ko direct karne deti hai. Iske bina, agent ki koi destination nahi, aur bina destination fast
agent sirf expensive tareeqa hai lost hone ka.

**Corollary, Boris Cherny se:** jab coding solved ho jaye aur domain knowledge bottleneck ban jaye,
**software likhne ka best insaan wo hai jo domain sab se achhi tarah samajhta hai, wo nahi jisne
historically software likha.** Accounting software ka best author ek **really good accountant**
hai. Historical analogy: printing press — Gutenberg se pehle, reading ek specialist trade thi;
decades mein printed output explode ho gaya; literacy broad-majority skill ban gayi, profession
nahi rahi. Yehi arc software ke liye shuru ho raha hai. Ek generation mein, **software banana** har
domain ke professionals ka ordinary kaam hoga (accountants jo apne ledgers likhte hain, doctors jo
apne clinical workflows likhte hain) — aur "engineer" kehlana **narrower aur deeper** cheez hoga: wo
insaan jo woh **substrate** design karta hai jis par baaqi workforce banti hai.

**Yehi workforce shape hai jo yeh book sikhati hai.** Digital FTE jo tum aage manufacture karoge ek
domain expert ka tool hai — agentic engineer ne banaya, lekin accountant/underwriter/analyst ne
specify+govern+use kiya jo kaam own karta hai. Is chapter ke principles+workflows wahi hain jo in
Digital FTEs ko **trustworthy** banate hain is ownership ke layak. Pipeline, Skills, deep modules,
persistent loops, sandboxes, smart-zone discipline, jagged-intelligence awareness — sab ek domain
expert ke liye reliable software ki service mein, bina code ki ek line parhe. **Yehi agentic
engineering ka contract hai un logon ke sath jo yeh serve karti hai.**

## Further Reading

- **Matt Pocock**, *Software Fundamentals Matter More Than Ever* — keynote jo chapter ki thesis
  inform karta hai.
- **Matt Pocock**, [*Dictionary of AI Coding*](https://github.com/mattpocock/dictionary-of-ai-coding) —
  canonical glossary, §08 ka source.
- **Matt Pocock**, [*Skills for Real Engineers*](https://github.com/mattpocock/skills) — installable
  skill pack poore chapter mein use hua.
- **Andrej Karpathy**, *From Vibe Coding to Agentic Engineering* — Software 1.0/2.0/3.0 framing,
  jagged intelligence, animals vs ghosts (§01, §02).
- **Boris Cherny (Anthropic)**, *Why Coding Is Solved, and What Comes Next* — on-distribution
  argument, persistent loops/routines, printing-press analogy (§01, §02, §06, §10).
- **John Ousterhout**, *A Philosophy of Software Design* — deep/shallow modules.
- **David Thomas & Andrew Hunt**, *The Pragmatic Programmer* — tracer bullets, headlights.
- **Eric Evans**, *Domain-Driven Design* — ubiquitous language.
- **Kent Beck**, *Extreme Programming Explained* — design mein daily invest.
- **Frederick P. Brooks**, *The Design of Design* — design tree, design concept.

## Companion Skills (Yeh Chapter)

6 Skills jo poore pipeline mein chalti hain (Matt Pocock's pack se): `grill-me`, `grill-with-docs`,
`to-prd`, `to-issues`, `tdd`, `improve-codebase-architecture`. Ek one-time bootstrap
`setup-matt-pocock-skills` pehle chalti hai har repo mein.

Pack total **14 skills** ship karta hai. Pipeline ke bahar bhi: `diagnose` (disciplined bug
debugging), `triage`, `zoom-out`, `prototype`, `write-a-skill` (meta-Skill), `handoff`, `caveman`
(terse-prompt mode) — sab Claude Code aur OpenCode dono mein identically chalti hain.

---
[⬅ Practical Drills](09-practical-drills.md) · [Agla: Test Your Understanding ➡](11-test-your-understanding.md)
