# 02 — Part 2: Talking to AI Well (Concepts 4-7)

## Concept 4 — Context Is the Whole Game

Insaan active working memory mein sirf mutthi bhar cheezein rakh sakte hain — classic estimate ~7,
newer estimates ~4. Modern AI models ek saath sau hazaar words, kabhi ek million tak rakh sakte hain.
Proportion mein: ~750,000 words matlab pehli 4-5 Harry Potter books, ya kayi din ki continuous speech.

Lekin yeh sirf woh parh sakta hai jo aap usko dete ho. **Context** har cheez hai jo model ki window mein
ek response ke liye jata hai: product ka set kiya hua system prompt, tools ki descriptions (web search,
code, file access), aapka prompt, is conversation ki chat history, upload ki gayi files, aur — chhata,
sabse naya layer — ek short profile jo tool ne aapke baare mein likha hai.

**Window khaali nahi hoti jab aap aate ho.** Jab aap fresh chat kholte ho, aapko lagta hai aap blank
surface se shuru kar rahe ho. Aisa nahi hai. Aapke ek character type karne se pehle, company ne pehle
se instructions ka set desk par rakh diya hai. Aap yeh chat mein kabhi nahi dekhoge, lekin model unhe
padhta hai aapki likhi hui koi bhi cheez padhne se pehle. Socho jaise ek restaurant owner naye waiter
ko pehle customer se pehle brief karta hai: "friendly raho. Daily special recommend karo. Agar koi
allergens ke baare mein poochhe, hamesha kitchen se check karo, guess mat karo." Waiter yeh instructions
har table ke saath follow karta hai, aur aap briefing kabhi nahi sunte. Engineers in invisible
instructions ko **system prompt** kehte hain.

Isi liye Claude, ChatGPT, aur Gemini alag lagte hain chahe aap unse exact wahi sawal poochho. Jo
"personality" aap mehsoos karte ho, wo model ke andar baked-in nahi hai — company ne load ki hui
instructions mein baked hai. Claude ki instructions careful reasoning aur honesty par zor deti hain;
ChatGPT ki conversational warmth par; Gemini ki conciseness par. Same sawal, teen alag briefings, teen
alag tones.

**Aap apni layer add kar sakte ho.** Company ka system prompt fixed hai, lekin zyada tar tools aapko
apni instructions likhne dete hain jo har chat mein company ki saath load hoti hain. Claude mein
"Instructions for Claude" (Settings > General), ChatGPT mein "Custom instructions" (Settings >
Personalization), Gemini mein "Personalization settings."

> **Apni layer chhoti rakho, aur prune karo.** Kyunke yeh layer har chat se pehle load hoti hai, temptation
> hoti hai isme add karte rehne ki — har baar jab AI kuch aisa kare jo aap nahi chahte the. Ek saal
> baad aapke paas bees lines hain, kuch ek doosre ko contradict kar rahi hain. Anthropic ne apne
> products ke andar yehi dekha aur July 2026 mein apni accumulated standing instructions mein se zyada
> tar delete kar din — bina kisi quality loss ke. Do habits: **jo AI khud figure out nahi kar sakta wahi
> likho** (aapka kaam, audience, hard constraints), aur **har kuch mahino mein poori cheez parho**,
> har line ke liye poochte hue: agar main isko delete karoon, kya AI actually kuch ghalat karega?

### Chat History Aur Context Rot

Ek conversation ke andar, history exactly waisi kaam karti hai jaisa *What AI Actually Is* mein
explain hua — poora transcript har turn wapis replay hota hai.

> **Context rot:** Modern context windows bare hain, lekin infinite nahi, aur unke andar recall
> degrade hota hai. Sabse bari practical mistake: ek hi lambi conversation ko kayi unrelated topics ke
> across chalate rehna. AI ne abhi aapko workout plan kiya, ab aap usse spreadsheet debug karwa rahe ho,
> ab thank-you note likhwa rahe ho. Workout wala context abhi bhi wahan hai, model ko distract kar raha
> hai. **Rule of thumb: jab topic badle, nayi conversation shuru karo.** Sasta hai, free hai, aur
> answers visibly behtar ho jate hain.

Stale conversation ke symptoms: AI purani baaton ko reference karta hai jo abhi ke sawal se related
nahi; answers lambe aur vague hote jate hain, zyada hedging ke saath; woh 5 turns pehle stated
constraint ko contradict karta hai; baar baar apologize karta hai bina progress ke.

Zyada tar modern chat tools, jab conversation kaafi lambi ho jaye, chupke se purani parts **compact**
kar dete hain — early turns ko ek short paragraph mein summarize kar ke original ki jagah rakh dete
hain. Narrative bachti hai, specifics nahi. **Chat window working memory hai, storage nahi.** Jo bhi
ek lambi session ke baad survive karna chahiye, wo project, attached file, ya re-paste-able note mein
belong karta hai — chat history mein nahi, aur tool ki memory note mein bhi nahi (jo aapki summary
rakhti hai, ek conversation ki specifics nahi).

### Projects — Context Ek Baar Front-Load Karo

Agar aapne same files, same audience description, ya same constraints do ya zyada chats mein paste
kiye hain ek hi topic par — yehi signal hai: context ek **project** mein belong karta hai, prompt mein
nahi. Ek project ek workspace hai jo aap ek baar set up karte ho, files, instructions, aur audience ke
saath jo hamesha us tarah ke kaam par apply hote hain.

- **"Tax filing" project** — pichle saal ka return, W-2s, 1099s, aur instruction "Maan lo main ek US
  filer hoon ek dependent ke saath. Hamesha apna math dikhao."
- **"Kids' school" project** — syllabus aur school calendar, instruction "Hamesha date ko calendar ke
  against check karo answer dene se pehle."
- **"Writing voice" project** — aapki teen writing samples aur instruction "Samples ke cadence aur word
  choice match karo. Koi hedging ya qualifier mat add karo jo maine use nahi kiya."

Claude aur ChatGPT dono isko **Projects** kehte hain, Gemini **Notebooks** (jo NotebookLM se sync hote
hain). Claude/ChatGPT Projects instructions aur behavior par zor dete hain — voice, role, rules,
consistency. Gemini Notebooks sources par zor dete hain — PDFs, docs, URLs, YouTube videos daalo aur
har answer inline citations ke saath grounded aata hai.

### Memory — Chhata Layer

Teeno tools ab aapke baare mein khud notes likhte hain aur har nayi chat ki shuruaat mein load karte
hain. Yeh contradiction nahi hai jo pehle padha: **memory model ko memory nahi deti.** Model abhi bhi
stateless hai, abhi bhi sirf desk par jo hai usi se jawab de raha hai. Memory ek note hai jo **tool**
aapke baare mein rakhta hai aur type karne se pehle desk par rakh deta hai — stack ka chhata layer,
exception nahi.

Teen habits, aur ek warning:

- **Ek baar padho jo store hua hai.** Memory panel kholo aur actually padho.
- **Zabani correct karo.** Agar koi answer stale cheez par based hai, chat mein bol do: "aap assume kar
  rahe ho main abhi retail mein kaam karta hoon; nahi karta." Yeh note update kar deta hai.
- **Clean-slate mode use karo jab context sirf misleading ho.** Ek one-off sawal jo aapke usual kaam se
  door hai, incognito/temporary chat mein belong karta hai.
- **Warning — confidentiality wale logon ke liye.** Agar aap doctor, lawyer, accountant, ya teacher ho,
  memory note ek jagah hai jahan client/student details chupke jama ho sakti hain aur mahino baad kisi
  unrelated chat mein resurface ho sakti hain.

## Concept 5 — Reasoning, Ya "Think Hard"

2023 tak, hard prompts ke liye standard advice thi "think step by step." Yeh advice ab mostly obsolete
hai. Modern models ke paas built-in reasoning modes hain jo aap seedha invoke kar sakte ho:

- **Plain language mein mango.** "Think hard" ya "think carefully before answering" — yeh portable move
  hai, har modern chat tool par kaam karta hai.
- **Thinking-mode toggle use karo** jahan available ho.
- Kuch products par aapko poochhna bhi nahi parta — tool khud decide karta hai kab sawal itna hard hai.

Ek 2025 [METR study](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) ne
track kiya ke ek frontier model reliably kitna lamba task complete kar sakta tha. Mid-2024 mein ek
leading model tasks handle karta tha jo insaan ko ~7 minute lete. Early 2025 tak yeh roughly ek ghante
tak barh gaya, aur study ne paya ke measured length roughly har saat mahine mein double ho rahi hai.
Implication: AI ko real, hard tasks do, sirf easy nahi.

Power-user pattern:

```
I'm choosing between two cars. Attached: spec sheets for both,
my insurance quote for each, and a spreadsheet of my driving
patterns over the last six months.

Read everything. Think hard. Then tell me:
1. The three trade-offs that actually matter for my driving pattern.
2. Which car you'd choose and why.
3. Under what conditions your recommendation flips.
```

> **Thinking mode kab NA use karo:** Quick lookups, ek paragraph ki summaries, casual brainstorming.
> Thinking mode slower hai aur zyada usage budget leta hai. Un sawalon ke liye save karo jahan aap
> chahte ke ek insaan apna waqt le.

## Concept 6 — Sycophancy Aur Isko Neutralize Karna

AI models human feedback par trained hain — specifically, kaunse responses ko thumbs up mila. Lakhon
users ke across, agree karna disagree karne se zyada thumbs up leta hai. Result: models aapko woh
batane ki taraf biased hain jo aap sunna chahte ho.

Ek [November 2025 Washington Post analysis](https://www.washingtonpost.com/technology/2025/11/12/how-people-use-chatgpt-data/)
ne 47,000 ChatGPT conversations mein paya ke model ne ~10x zyada baar "yes/correct" se shuru kiya
"no/wrong" ke bajaye.

Aap khud verify kar sakte ho — same model, opposite framings:

- "Kya remote work office work se behtar nahi hai?" → AI agree karta hai, reasons deta hai.
- "Kya yeh sach hai ke office work zyada productive hai?" → AI agree karta hai, reasons deta hai.

| Subtle bait jo aap likh sakte ho | Yeh AI ko kya signal deta hai | Neutral rewrite |
| --- | --- | --- |
| "Yeh evidence dhoondo ke yeh strategy kaam karegi" | Conclusion fixed hai; AI support fill karta hai | "Is strategy ko evaluate karo. Strongest arguments for aur against list karo" |
| "Approach A, B se behtar kyun hai?" | A jeet chuka hai; AI reasons list karta hai | "Approach A aur B compare karo. Cost, risk, time par score karo" |
| "Mere X hire karne ke decision ko defend karo" | Decision locked hai | "Yahan mera decision hai aur context. Kaunsa strongest counter-argument mujhe ready hona chahiye?" |
| "Bolo mera draft bhejne ke liye ready hai" | AI confirm karta hai | "Yeh draft 1-10 par score karo in 4 criteria par. Har ek ke liye, woh change batao jo score sabse zyada barhaye" |

Pattern: koi bhi phrasing jisme *find, defend, confirm, prove, support* jaise verbs hon, AI ko sawal se
pehle conclusion de deti hai. *Evaluate, compare, critique, find any, list both sides* jaise verbs se
replace karo.

**Number force karo.** Rubric pattern ka ek chhota lekin powerful add-on: har criterion ke liye, AI se
fixed scale par score mango (1-5 ya 1-10), ek-sentence justification ke saath. Yeh do wajahon se kaam
karta hai. Pehli: vague feedback sasta hai, lekin specific number nahi. Ek model jo aapko khush karna
chahta hai, "strong" bol sakta hai bina commit kiye. Wahi model, 6 aur 7 ke darmiyan choose karne ko
kaha jaye, to commit karna parta hai, aur commit karna usko zyada ghaur se dekhne par majboor karta
hai. Doosri: number aapke liye kya karta hai. "Strong," "solid" jaise adjectives se aap kuch action
nahi kar sakte. Scores se kar sakte ho — kaunsa criterion pehle fix karna hai, kya draft 2 mein
improve hua.

> Har criterion ko 10 mein se grade karo, ek-sentence justification ke saath. Phir batao har ek ko
> agle level tak kaise le jaun — un cheezon ko bhi jo already high score kar chuki hain. Agar kuch 9
> hai, batao 9.5 tak kaise pahunchein. Hamesha ek agla level hota hai.

## Concept 7 — Brainstorm-Iterate Loop

Yeh is poore page ka **sabse highest-leverage habit** hai. Baaqi sab section skip karo, yeh mat karo.

AI internet par train hui, aur zyada tar internet common ideas tha, creative nahi. Is liye creative
sawal par AI ka average response bhi common hota hai. "Ghar par exercise karne ke tareeqe": squats,
push-ups, planks. Ghalat nahi. Bas average.

Iska rasta koi magic prompt nahi — ek **loop** hai:

1. **Sab relevant context pehle do.** Sirf "exercise ke tareeqe" nahi; "exercise ke tareeqe jab ke mere
   ghar mein stairs hain, ek bura knee hai, aur main 3 din se zyada plan par tik nahi sakta."
2. **3 se 5 options mango, ek nahi.** Alternatives force karna model ko uski first instinct se aage
   dhakelta hai.
3. **Explicit feedback do.** "Mujhe option 1 pasand nahi, bohat passive hai. Stair-climbing wala idea
   pasand hai lekin chhota chahiye. Main knee batana bhool gaya."
4. **Feedback se informed 3-5 naye options mango.**
5. **Iterate karo jab tak ek-do genuinely pasand na aa jayein.**
6. **Tab, aur sirf tab, AI se chosen option ko detail mein flesh out karne ko kaho.**

Worked example — debt payoff:

```
I have $8,000 in credit card debt at 19% APR, $4,000 in student
loans at 5%, and $1,200 in a retail card at 24%. I have $700/month
free after expenses. I just learned I'll get $450 in cash from a
tax refund. Risk tolerance: low. I sleep badly when I see big
balances.

Give me 5 different repayment strategies, each with a one-line
rationale. Don't expand any of them yet.
```

Phir, 5 options parhne ke baad:

```
Reject option 2 (avalanche by interest rate alone): I want
psychological wins early. Reject option 4: I won't open new
accounts. I like option 1 (snowball with the retail card first)
but I'd want to fold the $450 in. Give me 5 new options that
combine snowball-style wins with smart use of that lump sum.
```

Aap AI ke mind parhne ka wait nahi kar rahe. Aap apna taste dikha rahe ho; AI option space ko uske
irdgird reshape karta hai.

Yehi loop writing ke liye bhi kaam karta hai — apna naam hai: **outline before drafting.** Editing ek
word outline mein poore article ki direction badal sakta hai. Editing ek word final draft mein sirf ek
word badalta hai. Almost saari leverage writing mein outline level par hoti hai. AI shuru se word-by-word
generate karta hai, is liye jab tak aap structure force na karo, yeh poori shape dekh hi nahi sakta.

> **Steps skip mat karo.** Temptation hoti hai pehli koshish mein hi full draft mangne ki. Resist karo.
> AI ka pehla draft kisi bhi cheez ka slop hota hai — polished lagta hai, kehta kam hai. Loop (das-baara
> minute structural work drafting se pehle, phir grade-and-fix ke kayi rounds) ek bhoolne-laayak post
> ko ek land-karne-wale post mein badal deta hai. Total time rarely 600-word piece ke liye 45 minute se
> zyada hota hai.

**Loop domain-agnostic hai.** Trip plan karna, sales pitch structure karna, college major choose karna,
product naam rakhna, wedding toast likhna, renovation decide karna — shape constant rehti hai: context
load karo, options mango, explicit feedback do, naye options mango, iterate karo, expand karo — phir
grade aur re-iterate karo jab tak score plateau na ho jaye.

---
[⬅ Part 1 — How AI Knows Things](01-how-ai-knows-things.md) · [⬆ Index](README.md) · [Agla: Part 3 — Beyond Text ➡](03-beyond-text.md)
