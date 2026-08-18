# 04 — Part 4: Working Safely and Choosing Tools (Concepts 11-13)

Teen aakhri concepts: AI ko apni files aur permissions tak safely access kaise dein, sahi tool kaam ke
liye kaise choose karein, aur jab koi human expert room mein na ho to quality ka objective signal kaise
lein.

## Concept 11 — AI Desktop Apps Aur Permissions

Ab ek poora category hai **AI desktop apps** ka: apps jo aapke computer par chalte hain aur, permission
ke saath, aapki files dhoond sakte hain, parh sakte hain, aur unpar act kar sakte hain. Claude ka
[Cowork](https://claude.com/product/cowork) aur [OpenWork](https://openworklabs.com/) do examples hain.

Yeh kya kar sakte hain jo chat nahi kar sakti: PDFs ke messy folder ko dekh kar naya organization
propose karna (rename, move, subfolders) aur approve hone par execute karna; project ke liye related
files jorna aur khud se cheezein notice karna; poore folder ke across parh kar summarize karna.

Safe workflow: **1) Task batao. 2) Plan mango, action nahi — app file operations ki list propose
karta hai. 3) Plan review/edit karo. 4) Tab jaake execution approve karo.**

> **Yeh parhein kisi bhi AI app ko file access dene se pehle:** Do facts zyada tar log hard way seekhte
> hain — **deleted files often recycle bin mein NAHI jati** jab ek AI app delete karti hai; woh gone
> hoti hain. **Edited files edit history NAHI rakhti** jab tak version control na ho; AI ka change
> purani version ko overwrite kar deta hai. Jab tak aap yeh safely kuch baar kar na lo, har permission
> request ko smallest zaroori folder tak scope karo.

**Permission ladder:**

| Comfort Level | Kya Allow Karein | Kya Na Bolte Rahein |
| --- | --- | --- |
| Pehli sessions | Ek chhote folder tak read-only access | Kuch bhi jo write, delete, ya rename kare |
| 2-3 successful runs ke baad | Ek specific folder ke andar read/write | Desktop/documents root jaisi broader directories |
| Ek clean week ke baad | Project tree ke across read, scoped subfolder mein write | Us project se bahar kuch bhi |
| Trusted | Tool-specific permissions | Open-ended "jo zaroorat ho karo" |

Principle: scope track record ke saath barhta hai, na ke company par kitna trust hai uske saath.

## Concept 12 — Cost, Speed, Aur Kaunsa Model Kab

- **Text:** seconds, ek response ka fraction-of-a-cent.
- **Speech:** seconds, audio ke minute ka kuch cents.
- **Images:** tens of seconds, per generation kuch cents. No early-stop — poori image ek saath.
- **Video:** minutes per generation, kayi cents se dollars tak. Iteration painful hai.
- **Deep research:** minutes, kuch cents se quarter tak, lekin dozens sources synthesize karta hai.

Cost entry level par barely ek constraint hai — zyada tar chatbots free access dete hain jo is page ke
prompts comfortably handle karta hai. Do implications: **iteration cost shape karti hai aap kya karte
ho** (text 50 baar iterate kar sakte ho ek dopeher mein, video nahi — is liye images/video generate
karte waqt prompt mein zyada invest karo pehle), aur **costs neeche trend kar rahe hain.**

**Kaunsa model kis task ke liye?** AI **jagged** hai — alag models alag cheezon mein achhe hain, aur
leader har kuch mahino mein badalta hai. Koi single best model nahi. Do habits: **same prompt 2-3
models mein routinely try karo**, aur **ek tool se shaadi mat karo.**

[Arena](https://arena.ai/leaderboard) bookmark karne laayak leaderboard hai — users blind head-to-head
comparisons mein vote karte hain. **Mahine mein ek baar check karo** — leaders jaldi rotate hote hain.

Teen habits jo compound hoti hain: **kam se kam do tabs khule rakho** (primary tool aur backup);
**prompt scratchpad rakho** (achhe results wale prompts collect karo); **notice karo jab model ghalat
ho** — scolding ki tarah nahi, data ki tarah.

## Concept 13 — Models Checking Models

Jab koi ground truth na ho (koi answer key nahi, koi expert paas nahi baitha, koi test jo red fail na
ho), aap phir bhi quality ka objective signal le sakte ho — models ko ek doosre ko grade karwa kar.

Alag models ke alag blind spots hote hain — overlapping lekin identical nahi training data par, alag
reward signals ke saath, alag teams ne alag cheezon par zor diya. Ek point jo ek model miss karta hai,
doosra model often pakar leta hai. Yeh **sirf tab kaam karta hai jab models genuinely alag families se
hon** — Anthropic (Claude), OpenAI (ChatGPT), Google (Gemini), xAI (Grok), Meta, DeepSeek. Do Claude
models ek doosre ko cross-check karna cross-model checking nahi hai — unke priors bohat similar hain.

### Single-Model Self-Critique Loop (Halki Version)

Zyada tar everyday tasks ke liye kaafi hai: ek round "isko 1-10 par is rubric ke against score karo,
phir apne suggestions implement karo." Ek higher-leverage variant: numerical target set karo aur model
ko autonomously usi taraf iterate karne do. "Apni khud ki rubric ke against tab tak iterate karo jab
tak har criterion par 9.5 na pahunch jao, phir final version dikhao." Yeh Concept 6 se contradict nahi
karta — farq rubric hai. Bina rubric ke, "kya yeh achha hai?" "great work!" ban jata hai. Named criteria
ke saath scored 1-10, model ko batana parta hai *doosre points mein kya missing hai* — wo pointer hi
hai jo aap implement karte ho.

### Full Multi-Model Recipe (High-Stakes Version)

1. Best model se shuru karo jo aapke paas hai (Arena + apna quick A/B test).
2. Poori context ke saath pehla draft banao (Concept 1, 5, 7 use karke).
3. Model se apna output khud grade karwao, named criteria ke against 1-10.
4. Apne khud ke suggestions implement karwao. Repeat jab tak grade plateau na ho (~9).
5. Draft ko ek **doosri family** ke model tak le jao. Same rubric mango.
6. Doosre model ki critique pehle model ko wapis do: "ek doosre model ne yeh critique diya. Evaluate
   karo kaunse points adopt karne laayak hain, aur kyun."
7. High-stakes kaam ke liye, ek **teesri family** ke model se repeat karo.
8. Stop karo jab score do independent models ke across aapke target ko cross kare.

> **Privacy note high-stakes kaam ke liye:** Cross-model checking matlab aapka draft multiple tools
> mein paste karna. Sensitive material ke sath karne se pehle har tool ki data policy check karo.

> **Honest caveat:** Teen models phir bhi ek hi cheez mein sab ghalat ho sakte hain — wo jitna aap
> sochein usse zyada training data share karte hain. Score ek **progress signal** hai, truth signal
> nahi. High-stakes content (legal, medical, financial, ya kisi real person ke baare mein) ke liye
> koi cross-model pass ek human expert ka replacement nahi hai. Models craft ke liye check karte hain.
> Insaan un facts ko check karte hain jo matter karte hain.

**Kab loop skip karein:** ek short email, quick lookup, casual brainstorm — single-model theek hai.
Multi-model cross-check un kaamon ke liye save karo jahan ghalat hona mehenga hai. Rule of thumb: agar
ek thoughtful colleague ise review karne mein 2 ghante lagata, to yeh loop deserve karta hai.

---
[⬅ Part 3 — Beyond Text](03-beyond-text.md) · [⬆ Index](README.md) · [Agla: Recap + Practice Prompts ➡](05-recap-and-practice-prompts.md)
