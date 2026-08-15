# 01 — 4 Layers, Ek Ek Kar Ke

## Concept 3: Prompt — Unit Ek Model Call Hai

Prompt wo message hai jo aap compose karte ho: model kaun bane, kya chahiye, achha kaam kaisa lagta hai,
examples, jawab ki shape. Ye sab **ek single input** hai, **ek single response** produce karta hai.

**Craft yahan narrow hai** — sab se kamzor ingredient dhoondo, sirf usay fix karo. Shape galat hai to
sahi shape ka example do. Tone galat hai to audience naam do. **Sab 5 ingredients ek saath rewrite karna
kuch nahi batata konsa problem tha.**

Log is layer mein zyada invest karte hain — kyunke ye **bina code likhe practice ho sakti hai**, aur
**10 second mein edit** ho sakti hai. Dono achhi baatein hain. Dono **trap** ban jati hain jab production
mein kuch ghalat ho, kyunke pressure mein log wo cheez badalte hain jo **aasan** ho, jo **toti hai** wo
nahi.

**Prompt toti hai jab:** Model ne task samjha aur roughly sahi kaam kiya, lekin jawab galat shape mein,
galat length mein, galat voice mein ata hai. **Kuch factually galat nahi hai.**

## Concept 4: Context — Unit Poori Window Hai

Window wo sab kuch hai jo model **ek response likhte waqt** dekh sakta hai. Jo file attach nahi ki, wo
model ke liye **fact ki tarah available nahi hai.**

**Lekin ulti taraf bhi literally mat lo:** model khaali nahi hota jab window patli ho — wo training se
seekha hua sab kuch carry karta hai. **Missing document wale model khaali nahi hota — wo sab se likely
cheez uthata hai jo pehle se janta hai, aur usay wahi confidence se kehta hai jo truth ke liye hota.**

**Isliye "kuch to hamesha choose karta hai"** — ye **curator** hai. **3 kaam window ki wajah se hote
hain:**

1. **Order pehle** — position batati hai material kitni strongly land karta hai. "Lost in the middle"
   research — important passage beginning/end pe accuracy sab se zyada, middle mein kam
2. **Compression agla, aur free nahi** — 40 pages ko 4 mein summarize karna fit karta hai, lekin
   dropped exception wapas nahi milti
3. **Dropping aakhri, ek policy hai** — koi to decide karta hai jab window bhar jaye kya nikle. Aap ye
   policy set nahi karo to **harness aapke liye set kar degi, worst waqt pe, ek rule se jo aap ne kabhi
   parha nahi.**

> **Curator test:** Kisi document ko point karo aur poocho **kaunsi rule ne usay wahan daala.** Agar
> honest jawab hai "retriever ne wapas kar diya," aapke paas **search box hai, curator nahi.**

**Context toti hai jab:** Jawab fluent, confident, **factually galat** hai. Aksar wo **kisi aur cheez ke
baare mein sahi** hota hai — purana version, alag customer. **Confident, wrong, aur kisi sach cheez ke
qareeb — teeno milkar ek signature hain.**

## Concept 5: Harness — Unit Ek Beat Hai

Ek instruction dete ho. Agent 3 files parhta hai, command chalata hai, error parhta hai, edit karta hai,
dobara chalata hai, phir khamosh ho jata hai. Aap ne ek dafa type kiya. ~12 cheezein hui. **Ye poora
stretch ek beat hai**, aur harness wo code hai jo isay chalati hai.

**Job list chhoti hai:** Context assemble karo. Model call karo. Tools chalao. Results wapas do. Errors
handle karo. Beat khatam hone se pehle jo prove hona chahiye, wo enforce karo.

Aap pehle se ek use kar rahe ho. Claude Code, OpenCode, Cowork — sab harness hain.

**Zaroori surprise:** **Subagents tool ki tarah call hote hain, lekin kuch bara behave karte hain.**
Tool call result deta hai. **Subagent apni window kholta hai aur apni beat chalata hai.** Jo tool-shaped
opening se wapas ata hai, wo **poori nested copy ka output** hai.

Ye asal cheez deta hai (40 documents subagent parh sakta hai, aapki window mein kabhi na ayein). Lekin
asal cost bhi hai: **jo wapas ata hai ek summary hai, poore confidence se likha, us hisse samet jo galat
tha.** Aap ne 40 documents nahi dekhi. Kuch bhi downstream nahi dekhega.

## Concept 6: Wo Limit Jo Harness Ko Define Karti Hai — Course Ka Turning Point

Beat kai wajahon se khatam ho sakti hai — timeout, token ceiling, error, model decide kare ke done hai.
**Inme se koi bhi prove nahi karta ke kaam successful tha. Sirf itna prove karte hain ke beat khatam
hui.**

Achi harness beat ke andar real checks enforce kar sakti hai — test suite chalao, schema validate karo.
**Ye verification hai, model ki opinion nahi.**

Lekin boundary zaroori hai:

> **Beat prove kar sakti hai ke ek specific check pass hui. Ye decide nahi kar sakti ke wo check pass
> hona KAAFI tha.**

**Bank-reconciliation agent example:** 40 matches propose karta hai, kehta hai statement balance hai —
lekin kabhi 2 totals compare nahi kiye. Context assemble hui, tools chale, koi error nahi. **Har internal
signal healthy lagta hai. Claim phir bhi galat hai.**

Prompt mein *"verify your work"* likhna solve nahi karta — model *"verified"* utni aasani se likh sakta
hai jitni *"done."* **Success ki final definition BAHAR se ani chahiye us kaam se jo judge ho raha hai.**
Isi liye ye **agli layer** ki hai.

## Concept 7: Loop — Unit Poori Run Hai

Loop wo cheez deti hai jo ek beat khud ke liye nahi de sakti.

**Heartbeat** har beat shuru karta hai — schedule, event, condition. Iske bagair, **aap heartbeat ho.**

**Spine** model ke bahar state store karta hai, taake agli beat ko pata ho pichli ne kya kiya:
```text
run: nightly reconciliation, 2026-03-14
done: pulled 412 payments and 388 open invoices
in progress: matching pass 3 of 5, 341 matched so far
needs a person: invoice 4471, two candidates both at 0.52
budget: 3 beats used of 12
```

**Outside stops** poori run ko continue rakhein ya nahi decide karte hain:
- **Success condition** pehle se chuna, command se prove hua
- **Limits** beats/spending/waqt pe
- **No-progress check** — repeated attempts bina meaningful change ke
- **Alag checker** — jisne kaam banaya, wo judge nahi

**Inme se koi bhi maker se nahi poochta ke wo khatam hai.** Yehi **maker-checker rule** ek sentence
mein hai.

**Opening failure yaad hai?** Missing piece ek **no-progress check** thi, behtar prompt nahi.

## Concept 8: Human Gate — Ek Exit Hai, Stop Nahi

Stops runs ko **safely fail** karne ka tareeqa hain. **Gate runs ko madad ke sath succeed** karne ka
tareeqa hai.

**Zaroori idea:** *"Ambiguity ek error nahi hai."* Invoice 4471 2 payments se match karta hai, dono
0.52 score karte hain. **Ye matcher ki bug nahi. Yehi data hai.** Bina gate ke, agent ke paas sirf 2
options hain, dono bure: **fail** ho sakta hai (9 passes ka legitimate kaam phenk kar), ya **guess** kar
sakta hai.

> **Guessing khatarnak hai.** Crash **loud** hai. Guess **silent** hai, aur bilkul sahi jawab jaisa
> dikhta hai — same format, same confidence. **Koi downstream farq nahi bata sakta.**

Gate **pehle se likha hota hai**, waqt pe decide nahi hota. Triggers: confidence ek line se neeche, value
ek limit se upar, koi bhi action jo undo karna mushkil ho. Gate fire hoti hai to case **named person**
ko jati hai. Ayesha (accounts payable) 20 second mein sahi choose karti hai — usay March mein double
payment yaad hai.

**Uska jawab run khatam nahi karta — naye evidence ki tarah wapas enter hota hai, run wahin se jari
rehti hai.**

---
[⬅ The Shape](00-the-shape.md) · [Agla: Using the Map ➡](02-using-the-map.md)
