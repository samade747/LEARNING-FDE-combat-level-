# 02 — Part 2 & 3: Reframe + The Four Promotions

## Part 2 — Reframe: Worker Kaam Ke Andar Chhupa Hua Hai

**Har baar jab aap ne task Mode 1 mein achhi tarah solve kiya, aap ne ek trail chhora** — aur woh trail
hi worker ka raw material hai.

Ek achi Mode 1 session ne kya banaya socho: aap ne brief likha (kis se kaam, kya chahiye, "done" ka
matlab kya). Aap ne clear shape mein output manga. Aap ne check chalaya. Aap ne result file mein save
kiya. Kuch bhi throwaway nahi tha. To manufacturing do moves hai, scratch-build nahi:

1. **Harvest** — woh pieces uthao
2. **Harden** — har ek ko itna mazboot karo ke woh aapke bina chal sake

**Saaf lafzon mein:** hardening asli kaam hai — exits design karna, khud grade karne wala eval banana,
runtime khada karna — yeh genuine engineering hai, sirf jo already karte ho woh likh dena nahi. Reframe
aapko blank page se bachata hai; build ko trivial nahi banata.

**Yehi hai jahan economics flip hoti hai** — poori book ka dil. Haath se solve karte waqt, labour ek
**task** hai. Us solution ko worker mein promote karne ke baad, wahi labour ek **asset** ban jata hai.
Yehi poora farq hai Diego mein (100 ghante/saal) aur Ana mein (kuch ghante, ek dafa).

## Part 3 — Char Promotions

Crossing ek bara build nahi hai. Yeh **4 specific upgrades** hain, aur aap ne har ek ke liye hard
thinking already Mode 1 mein kar li thi. Har promotion woh cheez leta hai jo aap **haath se** karte the,
aur usay woh cheez banata hai jo worker **khud** karta hai.

### Promotion 1 — Aapka Brief Spec Banta Hai

Mode 1 mein aap har baar chota brief likhte the: *works from, want at the end, done when* (Gate 3 ki
teen lines). Yeh aapke zehan ya scratch note mein rehta tha, aap usay chalte chalte adjust kar sakte
the.

Worker aapka zehan parh nahi sakta, to woh brief ek **spec** banta hai — *specification* — ek likha hua
document jo worker **har ek run par** parhta hai, jo exactly batata hai woh kya karta hai, kis par, aur
kis standard tak. Spec wahi teen lines hain, ab explicit, complete, aur permanent. Skip karo, to worker
gaps ko guesses se bharega — har run mein thora alag.

*Seekho:* [Spec-Driven Development](../spec-driven-development/README.md).

### Promotion 2 — Aapka Check Eval Banta Hai

Mode 1 mein aap khud output verify karte the (Principle 3): parhte the, numbers source se check karte
the, trust karte the kyunki *aap* ne dekha.

Worker aapke bina chalta hai, aksar din mein kai baar. "Aap har baar parho" scale nahi karta, aur woh
moment nahi pakarta jab worker chupke se galat hona shuru ho. To aapka check ek **eval** banta hai —
*evaluation* — saved example inputs jo apne known-good answers ke sath paired hain. (Fuzzy kaam ke
liye, "known-good answer" ek label, rubric score, ya checklist ho sakta hai.) Worker ke results inke
against automatically grade hote hain — checking aapke bina hoti hai aur aapko warn karti hai jaise hi
worker drift shuru kare. Aapka ek-dafa reading ek hamesha-chalne wala test ban jata hai. Skip karo, to
drift silent hoti hai — pata unhappy customer se chalta hai, check se nahi.

*Seekho:* Eval-Driven Development.

### Promotion 3 — Aap Loop Se Nikalte Ho, Exits Design Karte Ho

Mode 1 mein aap loop ke **andar** the (Principle 6, 7): har step dekhte the, jab bhatakta to redirect
karte, aage badhne se pehle approve karte. Aap safety net the.

Worker steps khud chalata hai, koi dekh nahi raha hota. Yahan hai jahan log ghalti karte hain: routine
hissa aasan hai — aapka Mode 1 method already handle karta hai. Mushkil hissa **edges** hain — unusual
input, aisa case jo aapke method ko kabhi nahi mila. Aapko **pehle se** decide karna hai worker kya
kare jab aisi cheez mile jo handle nahi kar sakta. Almost hamesha jawab hai: **ruko aur insaan ko bulao.**
Yeh exits design karna (kab escalate karna, kisko, kya info ke sath) — yehi is promotion ka asli kaam
hai, aur yehi kaam worker ko trust-worthy banata hai.

Har task ke edges hote hain, chahe kitna hi simple lage: code likhne wala worker rukta hai jab uska
change tests break kare; invoices pay karne wala worker ek set amount se upar flag karta hai bajaye pay
karne ke; documents file karne wala worker confused case ko alag rakhta hai bajaye guess karne ke.
**Shape kabhi nahi badalta: routine handle karo, exception escalate karo.**

*Seekho:* Build AI Agents · Building a Digital FTE.

### Promotion 4 — Aapka Session Runtime Banta Hai

Mode 1 mein kaam ek session mein rehta tha jo aap kholte the. Laptop band, kaam khatam. Agli baar ke
liye kuch save karna (Principle 5) aap khud, haath se, files mein daalte the.

Worker ko aapke bina bhi exist karna hai. Isko chahiye ek **runtime** — software jo worker ko zinda
rakhti hai, khud chalta rehta hai — aur rehne ki jagah jahan woh reachable aur reliable ho. Uski memory
khud persist hoti hai, kyunki aapne save karna yaad rakha isliye nahi. Skip karo, to koi worker nahi hai
— sirf aap, haath se session kholte hue, wahi jahan aap ne shuru kiya tha.

*Seekho:* Deploy the Agent Harness. (Agar worker sirf aapke liye hai, ek halka rasta hai — agla page
dekho.)

## 4 Promotions — Ek Nazar Mein

| Mode 1 Mein Kya Tha | Mode 2 Mein Kya Banta Hai | Kahan Seekho |
| --- | --- | --- |
| Brief (works from / want at end / done when) | **Spec** jo worker har run parhta hai | Spec-Driven Development |
| Apna eyeball check | **Eval** jo worker ko automatically grade kare | Eval-Driven Development |
| Aap dekhte, redirect karte | Worker loop chalata hai aur edges par **escalate** karta hai | Build AI Agents · Digital FTE |
| Session jo kholo/band karo | **Runtime** jispe worker rehta hai | Deploy the Agent Harness |

Yehi poori crossing hai. Char upgrades, har ek woh cheez jo aap haath se karke already samajh chuke the.

> **Kya carry hota hai, rebuild nahi hota: Plugins.** 4 promotions woh hain jo *badalte* hain jab aap
> cross karte ho. Ek zaroori cheez zyada nahi badalti: aapke **plugins** — *skills* (packaged know-how)
> aur *connectors* (aapki dusri apps/data se links) jo aap ne already Mode 1 mein use kiye. Yeh open,
> cross-runtime formats par bane hote hain, isliye same skills/connectors claude.ai, general agents
> (Claude Code, OpenCode, Cowork, OpenWork), personal harnesses, aur manufacture kiye workers mein bhi
> — aksar halki si adaptation ke sath — carry ho jate hain.

## Research Ke Peeche

- **Fred Brooks**, *The Mythical Man-Month* (1975): "plan to throw one away — you will, anyway." Aapke
  repeated Mode 1 solves wahi throwaways hain — permanent worker banane se pehle hafte waste nahi ho
  rahe, aap woh experiment chala rahe ho jo batata hai permanent worker kya hona chahiye.
- **Lisanne Bainbridge**, *Ironies of Automation* (1983): Jab routine automate karte ho, insaan remove
  nahi hota — insaan **rare, mushkil cases** ke liye zimmedar reh jata hai, aur automation jitna
  reliable hoga, woh rare interventions utne hi important (aur mushkil) ban jate hain. Yehi wajah hai
  Promotion 3 exits design karne ke baare mein hai, routine ke baare mein nahi.

---
[⬅ The Signal](01-the-signal.md) · [⬆ Index](README.md) · [Agla: The Fork ➡](03-the-fork.md)
