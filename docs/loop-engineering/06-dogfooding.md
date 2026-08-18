# 06 — Dogfooding: Yeh Kitaab Khud Apne Loops Kaise Use Karti Hai

Ab tak shape familiar ho chuki hai. Ek loop ek system hai jo kaam dhoondta hai, karta hai, apna result
khud check karta hai, likh leta hai kya kiya, aur decide karta hai aage kya hai — sab kuch ek heartbeat
se start hota hai, spine se joda hua rehta hai. Aap ne ek loop **do dafa** kagaz par banaya hai. Yahan
se yeh kagaz par rehna band ho jata hai.

Koi bhi tool aapse trust maangne se pehle ek fair sawal hai: jinhon ne yeh banaya, kya woh khud isay
use karte hain? Software mein iska ek naam hai, **dogfooding** — apna khud ka product production mein
use karna, asal mein, sirf demo mein nahi. To seedhi baat: **2 loops har roz is kitaab ko chalati hain,
aur yeh wahi loops hain jo yeh course abhi abhi sikha kar hati hai. Kitaab apne aap ke sath bilkul wahi
karti hai jo yeh aapko apne liye karna sikha rahi hai.** Dono alag stacks par chalti hain — Concept 3
asal mein: loop ek dafa seekho, wo har tool ke sath chalti hai.

## Loop 1: Feedback Loop (Kitaab Ko Sahi Rakhti Hai)

Har lesson ke neeche wala feedback box — isi lesson sameet — ek loop ka front door hai.

- **Heartbeat:** 2 cloud Routines. Ek hafte mein kai baar naya feedback triage karti hai, doosri hafte
  mein ek dafa fixes draft karti hai.
- **Spine:** ek live database jo har reader ka note aur usse khule GitHub issues record karti hai. Har
  run pehle wale runs ka kaam parh kar shuru hoti hai, isliye ek note kabhi dobara nahi kaam hota.
- **Ek beat:** naya feedback parho aur sort karo. Zyada tar — ratings, thank-yous, duplicates, aur jo
  pehle se handle ho chuka — khud-ba-khud close ho jata hai, kisi insaan ko chhoona nahi parta. Baaki
  tracked issues ban jate hain, aur chhote, safe wale ke liye loop khud pull request draft kar deti hai.
- **Human gate:** sirf zaroori chand cheezein insaan tak pahonchti hain — koi blocked reader, koi
  contribution offer karne wala, koi genuine content error. Har drafted fix bhi ship hone se pehle ek
  insaan approve karta hai. Baaki sab bina kisi ke handle aur close ho jata hai.
- **Kya kiya hai:** apni pehli runs mein hi hazaron notes ka backlog saaf kar diya jo kisi insaan ke
  paas parhne ka waqt nahi tha, sirf woh handful escalate kiye jinhein waqai decision chahiye tha.

## Loop 2: What's New Loop (Readers Ko Informed Rakhti Hai)

[What's New page](https://agentfactory.panaversity.org/docs/whats-new) — jo abhi khol sakte ho — ek
loop ne likha hai, hath se nahi.

- **Heartbeat:** GitHub Actions schedule, din mein ek baar. Iska worker OpenCode hai, Claude Code nahi —
  matlab is course ka **doosra** tool.
- **Spine:** ek chhoti state file jo yaad rakhti hai aakhri baar kaunsa change likha tha, taake koi entry
  na dohrai jaye na miss ho.
- **Ek beat:** dekho pichli baar se kitaab mein kya change hua, decide karo reader ko waqai kya matter
  karega, har ek ke liye ek plain sentence likho, apne links khud check karo koi toota na ho, publish
  karo.
- **Human gate:** koi nahi. Live jaane se pehle koi approve nahi karta.

## Jahan Yeh Dono Loops Disagree Karti Hain — Isi Page Ki Sab Se Useful Baat

Feedback loop kuch bhi ship hone se pehle insaan ke liye rukti hai. What's New loop kisi ke liye nahi
rukti. Deciding factor yeh nahi ke konsi loop zyada important hai. Yeh hai **galat move ki cost.**
Lesson mein ek bad edit mehnga aur undo karna mushkil hai. Ek clumsy changelog line sirf ek revert door
hai. Isliye jo rule aap apni loops tak le ja sakte ho wo chota hai: **insaan wahan rakho jahan ek galat
khud-ba-khud move mehnga aur wapis lena mushkil ho, aur baaki har jagah insaan ko bahar rakho.** Yehi
Concept 1 ka *intent aur accountability hamesha aapki* — ab ek dial ban gaya jo aap har loop ke liye
alag set karte ho. (Industry ki apni terms mein, [Part 05](05-human-control.md) se: jahan mehnga hai
wahan *in-the-loop*, baaki har jagah *on-the-loop*.)

Aur honest baat — kyunke pichle chand pages "staying the engineer" ke baare mein thay: koi bhi loop
akela nahi chorha jata. Hum run transcripts parhte hain, kyunke green run ka matlab correct run nahi
(Appendix A5). Ek insaan abhi bhi decide karta hai kaunsa feedback fix kamata hai. Loops tireless
middle sambhalti hain, do sirey hamesha hamare rehte hain. Yeh koi limitation nahi jiski maafi mangi
jaye. Yehi **design** hai.

Ab aap ne production mein ek finished loop bahar se dekh li hai. Neeche wale projects wahan hain jahan
aap apni pehli loop khud banate ho.

---
[⬅ Human Control](05-human-control.md) · [Agla: Practice Projects ➡](07-practice-projects.md) · [⬆ Index](README.md)
