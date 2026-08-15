# 05 — Staying Honest: Lock-in Aur Limits

## Concept 11: Lock-in Ek Rate Hai, Ownership Drift Karti Hai

Pehle ghar ke baad har ghar ke sath 2 slow failures ate hain, dono khud ko announce nahi karte.

**Lock-in ek rate hai, ek event nahi.** Koi bhi pehle din portability sign away nahi karta. Ye **leak**
hoti hai: ek rule jo vendor-side setting mein tweak hui aur kabhi repo mein mirror nahi hui, ek eval
case jo sirf service console ke andar add hua, ek bar jo dashboard mein renegotiate hua bina kisi commit
ke. **Har ek item chup chaap suitcase se fixtures ki taraf move ho raha hai.** Aapke lock-in ka measure
ek direct sawal hai: *"agar ye ghar is quarter gayab ho jaye, move ki keemat kya hogi?"* **Defense:
repo truth rakhta hai.** Quarterly practice run — *"repo se akela ek fresh ghar configure karo"* —
portability ka hold-out set hai.

**Ownership drift hoti hai chahe kuch leak na ho.** Zyada subtle failure **aap mein** hai, files mein
nahi. Ek ghar jo mahinon chup-chaap chalta rahe, aapke sar mein ek chhoti promotion invite karta hai:
*"ye system measured hai"* se *"ye system theek hai"* tak. Baselines abhi bhi green, schedule abhi bhi
chup, aur aap dheere dheere per-category report parhna band kar dete ho, calibration replay karna band
kar dete ho, naye vendor capability pe Concept 8 ka "new-reach" sawal poochna band kar dete ho.
**Discipline mein koi step nahi hai "aur phir ye khud ko maintain karti hai." Scheduled run system ko
watch karti hai. Calendar reminder AAPKO watch karta hai.**

> **Simple:** 2 slow problems chup chap ate hain. Pehla, ghar chhorna waqt ke saath mushkil hota jata hai
> — ek chhoti setting ki dafa, jab tak sab kuch repo mein na ho. Doosra, ghar jo mahinon chup rahe, aapko
> check karna band kar deta hai. **Fix dono ke liye same hai:** repo ko single source of truth rakho,
> aur reports asal mein parhne ke liye calendar reminder set karo.

## Concept 12: Koi Bhi Ghar Kya Fix Nahi Kar Sakta

Section ka ant wahin karte hain jahan is section ki har course khatam hui: **honest boundary** pe. Behtar
ghar badalta hai **kab** aapka agent kaam karta hai, **kaun** usay zinda rakhta hai, **3am pe kya hota
hai**. Ye **ek cheez nahi badalta**: agent **kitna acha** kaam karta hai. Weak spec Anthropic ke cloud pe
bhi weak rehti hai. Uncalibrated judge 8 cents/ghanta pe bhi uncalibrated rehta hai. Missing eval case
har runner pe missing rehta hai. **Runtime decision is section ki aakhri course isi liye hai kyunke ye
pehli course hoti to bekaar hoti** — jo kuch ye relocate karti hai, wo pehle relocate hone ke qabil hona
chahiye tha.

> **Simple:** Behtar ghar badalta hai kab aapka agent chalta hai, kaun isay zinda rakhta hai, aur 3am pe
> isay kaun fix karta hai. Ye agent ko zyada smart ya sahi nahi banata. Weak plan cloud mein bhi weak
> hai. Achha kaam spec, harness, aur tests se ata hai jo aap pehle hi bana chuke ho. **Ghar sirf decide
> karta hai kaun isay chalta rakhta hai.**

## Poori Trilogy Ka Ant

> Aap ne ek general agent ko **drive** karna seekha, phir usay spec se **direct** karna, phir loop ko
> **delegate** karna, harness ko **harden** karna, aur checker ko **measure** karna, aur ab poore system
> ko kahin **house** karna jo uske qabil ho. Aakhri mein aap ke paas wo cheez hai jo ye book pehle page
> se assemble kar rahi thi: **ek specified, guarded, measured, housed unit of work.** Isay book ki
> vocabulary ke against rakho aur agla darwaza khud khul jata hai: wo unit, doosre logon ke liye bani,
> ek owned runtime, product surface, aur price ke sath — iska naam hai: **Digital FTE.**

**3 darwaze is section se nikalte hain (4 sawal batate hain kaunsa aapka hai):**
- **Personal Agent Harnesses** — us reader ke liye jiska Q2 personal scale pe "must own" tha
- **Mode 1: Problem-Solving** — real problems solve karna abhi wale system se — zyada tar readers ka
  agla step
- **Mode 2: Manufacturing** — jahan is course ka har promise complete hota hai: ghar 4 (Agent SDK)
  khulta hai, decoupled architecture ek design choice ban jati hai jo aap khud lete ho

> **Section ka closing thought:** Loop ne aapke agent ko waqt diya. Harness ne usay limits diye. Evals
> ne usay track record diya. **Ye course ne usay aakhri cheez di jo ek worker ko chahiye: ek pata jo
> aapka nahi hai.**

### Self-Check
**Sawal:** Ek reader kehta hai: *"To endgame ghar 3 hai. Managed hi wahan hai jahan sab kuch aakhir jata
hai."* Q1-Q4 aur Concept 10 ki mix se, 2-line correction likho.
**Jawab:** Koi endgame ghar nahi hai — 4 sawal **har loop ke liye alag** poochhe jate hain, aur healthy
system deliberately gharon mein phaila hota hai: ghar 1 mein banao, ghar 2 mein schedule karo, ghar 3
(ya owned runtime) se serve karo jab **must** demand kare. Aur koi bhi ghar agent ke liye upgrade nahi
hai — quality spec, harness, aur suite mein rehti hai, jo travel karte hain. **Ghar sirf decide karta hai
lights kaun on rakhta hai.**

---
[⬅ Choosing a Home](04-choosing-a-home.md) · [Agla: Practice Projects ➡](06-practice-projects.md)
