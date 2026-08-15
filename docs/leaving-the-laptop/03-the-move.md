# 03 — Move Khud

## Concept 7: Suitcase Test — Discipline Travel Karti Hai, Mechanics Nahi

Har ghar ke darmiyan move, is course mein ek packing sawal tak simat jati hai: **kya suitcase mein jata
hai, kya arrival pe rebuild hota hai?**

**Jo travel karta hai — trilogy ne asal mein jo sikhaya sab:** Spec (job kya hai, "done" ka matlab kya
hai). Rubric, anchors samet. Golden set, har case ki `origin` line, aur uske baselines. Ratchet log.
Maker-checker split, category bars, human gate. **Is list mein common cheez notice karo: ismein koi
software nahi hai. Ye decisions hain, likhi hui.** Isi liye ye travel karti hai — decision ko farq nahi
parta konsa computer isay enforce karta hai.

**Jo travel nahi karta — jispe kisi vendor ya machine ka naam ho:** Flags, output formats. File paths.
Session state. Ek runtime ke API ke against likha code. Cost assumptions (jo ghar badalne se shape
badalte hain, sirf size nahi).

> **Asal jawab lock-in ka:** **Aapka portable asset discipline layer hai, aur uski portability kuch aisa
> hai jo aap maintain karte ho, jo aapke paas hai wo nahi.** Har dafa jab ek rule sirf vendor-side
> setting mein rehti hai, na ke aapke repo mein — wahi weight suitcase se bahar move ho raha hai. Aadat
> jo aapko movable rakhti hai: **repo truth rakhta hai, aur har ghar wahin se configure hota hai.**

> **Simple:** Ghar move karte waqt, apni cheezein pack karo, dewaron se fixed lamps chhor do. Aapki spec,
> rubric, cases, bars — aapki hain: suitcase mein jati hain. Flags, paths, API shapes purane ghar se
> fixed hain: peeche reh jati hain.

## Concept 8: Trust Re-Earn Hoti Hai, Transfer Nahi

Aapka 35/36 ek **system** ka measurement tha: ye config, ye harness, ye model, ye machine. Move ne ek
saath kai cheezein badal di hain. **Purana number comparison target rehta hai — nayi jagah ko jo meet
karna hai wo standard, na ke koi free label.**

**Arrival protocol (evals course, jaan-boojh kar replay):**

1. **Naye ghar mein poora golden set chalao, sab se pehle.** Smoke set nahi, poora set. Runner headless
   hai, naya ghar headless boli bolta hai
2. **Misses ko category se parho, count se pehle** — tone case down chhota problem hai. Injection case
   down, naye reachable surfaces wale ghar mein, **emergency hai**
3. **Bars hold karo, phir naya baseline record karo, ghar ke naam se labeled.** Purana baseline delete
   nahi hota — wo comparison target hai. Naye ghar ko **existing bars pass karne** hain
4. **Probation, dependence se pehle.** Fixed period: kam se kam poora operating cycle **aur** kam se kam
   10 successful beats, zyada risky/rare loops ke liye lamba. Purana ghar available rehta hai. Result ko
   *"initial operational evidence"* kaho, uptime ka proof nahi

> **Simple:** Aapka purana score purane setup pe measure hua tha, aur move ne wo setup badal diya, to
> score aapke saath nahi ata. Naye ghar mein dobara kamao: pehle din poora test set chalao, dekho kya
> fail hua aur kis type ki failure hai, wahi pass-bar rakho jo hamesha rakha, naya score likho naye
> ghar ke naam se, aur trial period ke liye watch karo trust karne se pehle.

> **Warning:** Naye ghar ki **naya reach** hai — cloud runner alag credentials dekhta hai laptop se.
> Aapke injection aur blast-radius cases purani reach ke against likhe gaye thay. Probation khatam hone
> se pehle, golden set ki hard cases walk karo, har ek se poocho: *"is case ka guard kiya hua failure
> yahan se different lagta hai?"*

### Self-Check
**Sawal:** Ghar 2 pe move karne ke baad, pehli poori-set run 33/36 parhti hai (purana baseline 35/36). Ek
clean-fix case flake hui (re-run pe green). Baaki 2 misses same case hain — ek fixture jo purane laptop
ka absolute path use karti hai. In 3 misses ko sort karo.
**Jawab:** Flake noise hai, evals course ki re-run policy handle karti hai — record hota hai, gate nahi
karta. Repeated miss agent ki regression nahi hai — ye ek **suitcase error** hai: absolute file path
mechanics hai, ye fixture ke andar accidentally travel kar gayi. Fix: case repair karo (path-relative
banao), **system nahi**. Phir usi commit mein re-baseline karo, kyunke **set** badla. Bars khud nahi
hilte, aur repair history mein visible hona chahiye.

---
[⬅ Managed Runtime](02-managed-runtime.md) · [Agla: Choosing a Home ➡](04-choosing-a-home.md)
