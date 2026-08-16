# 00 — Part 1: Ek Worker Se Team Tak (Concepts 1-3)

## Team Itni Chhoti Kaise Hui

20 saal se software ship karne wali unit **pod** thi: ek product lead, 6-10 engineers ke sath (Amazon
ka "two-pizza team"). Ratio arbitrary nahi tha — **code likhna slow part tha.** Ek lead utne engineers
ko direction de sakta tha jitne busy rakh sake.

**Coding agents ne yeh balance tod diya.** Jab har engineer agents ka fleet drive karta hai, building
ab slow part nahi rahi — to pod ko 10 log bharne ki zaroorat nahi. Human count girta hai, output barhta
hai. Pod simat ke apni limit tak pahunchti hai: **ek insan, Digital FTEs ke workforce ko command karta
hua.** Yehi team hai jo yeh course sikhata hai.

**Asal cheez number nahi, wajah hai.** Jab execution sasti ho jati hai, **slow part move ho jata hai.**
Yeh move hota hai *kya banana hai* decide karne, aur *jo wapis aya woh sahi hai* judge karne mein. To
pod sirf simti nahi — **uska bottleneck ulat gaya:** *"kya hamare paas ise banane ke haath hain?"* se
*"kya hamare paas ise validate karne ki judgment hai?"* **Yehi ulat-pher poori operating model ki
wajah hai** — jo ek scarce cheez yeh model protect karti hai: human judgment.

## Concept 1 — Single-Player Khatam Ho Chuka

AI ke sath kaam karna single-player tha: ek insan, ek chat window, ek task. Shift hai **multiplayer**
ki taraf: kai insan aur kai agents ek workspace mein, shared goals ki taraf pull karte hue.

**Multiplayer agent** kai insano ke sath kaam karta hai. Digital FTE ki tarah, apni memory/skills rakhta
hai. Chat window se alag, uske paas apne **credentials** hain (kisi insan se borrow nahi kiye), aur woh
**jahan kaam hota hai wahin rehta hai** — team ke channels aur docs mein, private session mein nahi.

> **Claude Tag (June 2026):** Anthropic ne Claude ko team ke Slack channels mein standing member ki
> tarah ship kiya — koi bhi @Claude tag kar sakta hai, sab dekh sakte hain woh kaam kar raha hai, koi
> bhi mid-task redirect kar sakta hai. Per-channel memory, scoped identity. Anthropic ke internal team
> ka 65% code ab isi se banta hai.

## Concept 2 — Worker Ko 3 Cheezein Chahiye

- **Persistent memory** — goal ko dinon tak yaad rakhe, ek prompt nahi (AI Searchable Context)
- **Apni identity** — insan se juri nahi credentials (AI Identity)
- **Broad, searchable access** — likhi hui cheez se organization kaise chalti hai seekhe (system of
  record + RAG)

In ke bina, "team mein agent add karo" matlab ek insan apna password ek script ko de raha hai.

## Concept 3 — Scarce Resource Human Judgment Hai

Poori operating model **ek cheez protect karti hai: insaani attention aur judgment.** Agents fast aur
kai hain; log bottleneck **aur** authority dono hain.

**Failure mode (operating model ke bina):** Log side mein apne personal AIs ke fleets chalate hain. Kaam
duplicate hota hai. Team ka context private windows mein tut jata hai jo koi (insan ya agent) dekh nahi
sakta. Fix zyada agents nahi — **ek team khule mein chalana hai.**

**4 Practices (poora course):**
1. **Khule mein kaam karo**
2. **Ek roster, saaf roles**
3. **Ek north star**
4. **Trust, kamaya hua**

> Har practice ek cheez protect karti hai: **human judgment.**

---
[⬆ Index](README.md) · [Agla: Khule Mein Kaam Karna ➡](01-work-in-the-open.md)
