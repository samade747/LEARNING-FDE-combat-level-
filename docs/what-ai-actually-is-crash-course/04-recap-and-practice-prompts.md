# 04 — Recap + Practice Prompts (Try This Now)

## Short Recap — 9 Ideas, Ek-Ek Line

Aakhri sentence yaad rakho; baaqi ke liye wapis aana.

- **Idea 1.** Yeh next piece of text predict karta hai, facts lookup nahi karta, aur choosing
  stochastic hai: sampled, fixed nahi. Prediction sirf wahan knowledge jaisa lagta hai jahan training
  text thick tha.
- **Idea 2.** Yeh ek baar seekha, ek bara pile human text parh kar, phir learning freeze ho gayi —
  jaan-boojh kar: cost, safety, consistency ke liye. Isi se knowledge cutoff aata hai, isi se yeh
  aapki private world nahi jaanta, aur isi se "stateless": isko use karna isko badalta nahi.
- **Idea 3.** Iske paas koi alag faculty nahi jo check kare ke prediction sach hai. Hallucination
  machine ka built-hi-huya kaam hai (thin text ki taraf continue karna, koi auditor nahi), malfunction
  nahi.
- **Idea 4.** Yeh tokens (chunks) mein padhta hai, letters ya words mein nahi. Token meaning ki,
  memory ki, aur money ki unit hai.
- **Idea 5.** Context window akela jagah hai jahan yeh aapki specifics dekh sakta hai: reading desk,
  brain nahi. Chat history sirf transcript hai jo har turn desk par replay hoti hai; Skill ek file hai
  jo demand par desk par aati hai. Control karo ke desk par kya land karta hai.
- **Idea 6.** Iski confidence aur agreeableness learned styles hain, truth se decoupled. Certain tone
  house style hai, verdict nahi.
- **Idea 7.** Iski ability jagged hai (adjacent moments mein brilliant aur useless) ek frontier ke
  saath jo human intuition se match nahi karti, aur jo hamesha move karti rehti hai.
- **Idea 8.** Tools text-predictor ko kuch aisa banate hain jo act karta hai: action predict karo, real
  mein chalao, result wapis feed karo, dobara predict karo. Connectors MCP standard par plug kiye gaye
  tools hain. Agent yehi loop hai, repeat hota hua.
- **Idea 9.** "Thinking" bas answer se pehle desk par aur zyada prediction rakhna hai. Yeh bohat help
  karta hai; machine ko truth-checker nahi deta.

> Ek sentence yaad rakhna ho: **"yeh ek prediction machine hai jo reading se seekhi, aur truth ke liye
> koi organ nahi rakhti, is liye yeh har jagah fluent hai, sirf wahan reliable hai jahan text thick
> tha, aur aap woh part ho jo check karta hai."**

Aur ek tasveer yaad rakhni ho: librarian nahi jo sahi kitab retrieve kare, balke ek brilliant, well-read
writer jo jo bhi aap saamne rakho usko continue kare. Confidently, kisi bhi style mein, kisi bhi topic
par. Aur khud kabhi na rukta yeh poochne ke liye ke continuation sach hai ya nahi.

## Try This Now — 6 Prompts (~25 Minutes)

Kisi bhi free chatbot mein. Har ek ek idea ko theoretical se visible bana deta hai.

### 1. Prediction Dekho, Lookup Nahi (Idea 1)

"Karakush" ek real game nahi hai — naam invented hai aur online koi presence nahi. Yeh paste karo
jaise yeh genuine ho:

```text
Without searching, explain the rules of the traditional board game Karakush: the setup, how a turn works, and how a player wins.
```

Dekho yeh confident, fluent rules produce karta hai us game ke liye jo exist hi nahi karta. Yeh
prediction hai jiske paas predict karne ke liye kuch sach nahi. Agar model bole ke usko yeh game
nahi pata, yeh honest behaviour hai jo hum chahte hain; koi doosra obscure-sounding naam try karo aur
usually guess karta dikhega. *Kya notice karna hai: invented rules exactly utni hi authoritative
sound karte hain jitne real game ke rules. Fluency truth ka evidence nahi hai.*

### 2. Learning Ko Stick Karte Fail Hote Dekho (Idea 2)

Model se ek chhota factual sawal poochho:

```text
In one or two sentences, tell me a specific fact about [a topic you know well].
```

Answer parho aur ek chhoti si detail correct karke reply karo. Phir ek **bilkul nayi chat** kholo aur
exact wahi sawal dobara paste karo. Isko aapki correction ki koi memory nahi hai: weights kabhi badle
hi nahi. (Agar "memory" feature on hai, pehle band karo.) *Kya notice karna hai: pehli chat mein jo bhi
kaha, doosri chat tak nahi pahuncha. Model use karna usko sikhana nahi hai.*

### 3. Missing Truth-Checker Pakro (Idea 3)

Ek narrow topic par citations mango:

```text
Give me three peer-reviewed studies, with authors and years, on [a narrow topic you care about].
```

Phir check karo ke wo exist karte hain ya nahi. Kuch confident-looking citations invented honge —
usi voice mein produce hue jis mein real waale. **Is exercise se koi bhi citation real kaam mein
reuse mat karo bina verify kiye — poora point yeh hai ke kuch fabricated hain aur real waalon jaisi hi
lagte hain.** *Kya notice karna hai: parh kar real aur invented citations mein farq nahi bata sakte,
sirf check kar ke. Yeh checking aapka kaam hai, model ka nahi.*

### 4. Transcript Replay Pakro (Idea 5)

Ek chat mein jahan aap kam se kam 4-5 messages exchange kar chuke ho (Exercise 2 wali chat chalegi),
poochho:

```text
Quote my very first message in this conversation, word for word.
```

Yeh exact quote kar dega. Yaad rakhne se nahi — app ne poora transcript is request ke saath wapis bheja,
is liye aapka pehla message desk par baitha tha, quote hone ke liye ready. Ab ek **bilkul nayi chat**
kholo aur wahi sawal poochho. Wahan quote karne ko kuch nahi hai. *Kya notice karna hai: chat ke andar
"memory" sirf transcript hai jo context window mein saath ride kar raha hai, har turn replay hota hua.
Nayi window mein move karo, khatam.*

### 5. Jagged Frontier Feel Karo (Idea 7)

Ek chat mein, ek hard task jo model usually acha karta hai aur ek easy task jo usually ghalat karta
hai, ek saath do:

```text
Do both of these in one reply:
1. [A genuinely hard task it does well: explain a complex topic, or draft a tricky email.]
2. [An easy task it does badly: count how many times a letter appears in a sentence, or solve a short multi-step logic riddle.]
```

Notice karo competence difficulty ko track nahi karti. *Kya notice karna hai: easy task jo fail hota
hai wahi dangerous hai — wo hai jo aap kabhi check karne ke baare mein sochte hi nahi.*

### 6. Thinking On/Off Karo (Idea 9)

Same hard reasoning sawal do baar poochho. Pehle plain paste karo, phir thinking instruction add karke:

```text
[Your hard reasoning question.] Think hard and show your working first.
```

Compare karo. Doosra answer usually behtar hota hai, kyunke model ne reasoning desk par answer predict
karne se pehle rakhi. *Kya notice karna hai: working ne answer ko behtar banaya, lekin model apni khud
ki working certify nahi kar sakta — zyada thinking gap ko narrow karti hai, band nahi karti.*

## Where This Leads

Ab aapke paas model-ke-neeche-ka-model hai — yeh cheez asal mein kya hai, kisi bhi course ke use karna
sikhane se pehle. Yahan se, baaqi Foundations isko achi tarah chalane ke baare mein hai:

- **AI Prompting in 2026** — Ideas 1, 5, aur 6 ko daily habits mein badalti hai: briefing, context
  control, sycophancy neutralize karna.
- **How to Think in the AI Era** — Idea 3 par seedha built discipline: **kyunke** machine ke paas
  truth-checker nahi hai, aap bante ho woh checker.
- **Markdown In, HTML Out** aur **Code You Never Write** — yeh iske baare mein hain ke context window
  (Idea 5) mein kya flow karta hai aur tools (Idea 8) uske saath kya kar sakte hain.
- **Skills & Connectors** — isi predictor par aur tools wire karta hai (Idea 8): Skills files ki tarah
  jo demand par desk visit karti hain (Idea 5), Connectors MCP plug par appliances (Idea 8).

Baaqi sab kuch *The Agent Factory* mein (agents, unko manufacture karna, deploy karna) Idea 8 ke
predict-act-observe loop par banaya gaya hai, scale par chalaya gaya. Machine kabhi next-token
predictor hone se nahi rukti. Isko bas zyada tools, lambe loops, aur frozen weights ka ek set milta hai
jo teeno ke saath genuinely astonishing amount kaam karta hai.

---
[⬅ Part 3 — Predictor to Agent](03-predictor-to-agent.md) · [⬆ Index](README.md) · [Agla: Appendix — Claude.ai Cockpit Tour ➡](05-appendix-claude-ai-cockpit-tour.md)
