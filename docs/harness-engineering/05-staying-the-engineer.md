# 05 — Staying the Engineer: Insaan Ka Kaam Khatam Nahi Hota

Harness failures ka **type** badalta hai. Ye aapko involvement se **bahar nahi** karta — aur iske do
problems **isliye barhti hain kyunke ye kaam karta hai**.

## Concept 11: Observability — Jo Dikhta Nahi, Wo Hai Hi Nahi

Ab tak sab kuch **lamhe mein** act karta hai: ye block karo, wo check karo. **Observability** harness ki
apni memory hai — kya chala, kya block hua, har beat ki cost kya thi, verdict aisa kyun aya.

**Wajah:** *chup chaap fail hone wali loop, koi loop na hone se bhi buri hai* — kyunke aap yakeen karte
ho kaam ho raha hai jab nahi ho raha. Harness version isme add karta hai: **guardrail jo chup chaap fire
ho, kuch nahi sikhata.** Wo raat 3 baje wala blocked `.env` read raat ka sab se **valuable event** hai —
lekin sirf tab jab aap isay dekho, kyunke ye batata hai koi aapki defenses test kar raha hai, aur deewar
ne rok liya.

**3 aadatein jo zyada tar cheez cover karti hain:**

1. **Har beat ek jagah log karo** — actions taken, actions blocked, verdict, cost. Spine record karti
   hai **kaam** ne kya kiya. Harness log record karti hai **system** ne kya kiya.
2. **Failure ko loud banao** — fail/blocked beat aapko notify kare, khud discover na hona pare. **Chup**
   ka matlab **success** hona chahiye, ya chup ka koi matlab hi na ho.
3. **Cost ko signal ki tarah dekho, sirf bill ki tarah nahi** — jo beat achanak 3 guna cost kare, wo
   beat **bhatak gayi** — ek planning failure jo sab se pehle **cost** mein khud ko announce karti hai.

**Claude Code** mein bohat kuch built-in hai: session transcripts, `/usage` breakdown, background-task
notifications. **OpenCode** mein khud assemble karo: `opencode run --format json` structured output deta
hai, GitHub Actions ka workflow log free mein searchable hai.

## Concept 12: Harness Ki Limits

Ratchet sirf ek taraf ghumta hai — yehi iska **khatra** bhi hai. **3 forces** ise wapas kheenchti hain:

### 1. Capability vs Control Trade-Off

Har rule jo ek failure hataati hai, ek **move bhi hataati hai**. Bohat zyada deny, hook, cap karo, to
agent wo **surprising-but-right** kaam nahi kar payega — unusual fix, bold refactor. **Maximum tight**
harness **minimum ambition** wala kaam deti hai. Craft ye hai: **tightness ko blast radius se match**
karo — overnight loops real repos pe **tight** chalti hain, throwaway prototype session **loose**
chalti hai. **Aap** decide karte ho.

### 2. Harness Coupling

Ek harness jo ek model ki ajeeb aadaton pe zyada fit ho jaye, khamoshi se **usi model ka hissa** ban
jati hai. Model badlo, aur wo over-fitted parts (jo sirf us model ke liye shaped thin) tootne lagte
hain: token budgets ek tokenizer ke liye size ki hui, prompts jo ek model ki phrasing pe depend karte
hain. (Pichli course mein aap ne dekha: nayi model generation same text ke liye ~30% zyada tokens
banati hai, jo purani model pe measure kiya har budget tor deti hai.)

**Defense:** *behaviors* ki jagah *contracts* (exit codes, schemas, tests) se couple karo, aur kabhi
kabhar apni harness ko **doosre model pe** chala kar dekho kya tootta hai.

### 3. Rule Debt

Har rules-file line **har beat pe tokens** cost karti hai, har hook **har action pe seconds**, aur har
ask-rule **ek human interruption**. Ratchet lesson tabhi apni jagah kamata hai jab wo **repeating**
failure roke. Ek dafa ki oddity ke liye permanent rule banana safety nahi — **junk** hai.

> **Concrete schedule:** Rule set ko **monthly review** karo. Jo rule 90 din se **fire nahi hui**, aur
> koi incident isse linked nahi, wo **removal ki candidate** hai. Secrets ke ird gird ki deewarein is
> rule se **bachi hui** hain. Tripwires aur thresholds nahi.

## Khud Harness Kab Banao?

Jab tak Claude Code/OpenCode ki surfaces aapki rules express kar sakti hain, unhi ke saath raho — yehi
zyadatar logon ke liye zyadatar waqt sahi hai, aur vendor ki harness khud har hafte behtar hoti hai. **Khud
apni harness tab banao** jab product ki deewarein aisi requirement rokein jo aapke paas **asal mein**
ho: apna tool interface, apna verification stack, apna deployment shape.

## Aakhri Baat

> Loop aapki **intent** ya **accountability** nahi sambhal sakta. Harness bhi nahi sambhal sakta. Jo
> harness sambhalti hai wo hai aapka **judgment, permanent bana hua** — har rule ek decision hai jo aap
> ne **ek dafa** liya, hamesha ke liye enforce hoti hai, jab aap so rahe ho. Isi liye discipline ka
> founding tagline insaan ko pehle rakhta hai: ***"Humans steer. Agents execute."*** Harness sirf
> **steering hai, likhi hui**.

---
[⬅ Complete Harness Example](04-complete-harness-example.md) · [Agla: Dogfooding ➡](06-dogfooding.md)
