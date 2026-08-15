# 04 — Ghar Chunna: 4 Sawal

## Concept 9: 4 Sawal

Poora course 4 sawalon mein simat jata hai, order mein poochhe hue. Pehle 3 ghar chunte hain. Chautha
decide karta hai **kab** move karna hai.

**Q1: User kaun hai?** Agar honest jawab **aap** hain, jaldi ruk jao: **ghar 2 tقریباً hamesha kaafi
hota hai** — zyada tar readers, zyada tar waqt. Jis lamhe jawab mein **doosre log** shamil hon (team,
client, customer), loop ko aapki gairhaziri, aapki vacation, aapke login se bach kar rehna hai — sawal
Q2 tak sharpen ho jata hai.

**Q2: Kya own karna zaroori hai?** Jo **chahte** ho wo nahi, jo **waqai** own karna zaroori hai. 2
planes ise precise sawal bana dete hain, 3 jawabon ke sath:
- **Kuch bhi own karna zaroori nahi** → fully managed runtime fit hoti hai
- **Sirf execution + data plane** (kaam aur jo wo touch kare, loop nahi) → ghar 3 self-hosted sandbox ke
  sath, custody rakho, operations rent karo
- **Control plane bhi** → agar prompts, sessions, model path own karna zaroori hai → owned runtime, SDK
  path, Mode 2

**Q3: Kya koi insaan jawab ka wait karta hai?** Scheduled/background kaam (triage, reports) schedules
aur managed sessions mein comfortably fit hota hai. **Screen pe wait karta insaan** requirements
badalta hai, owner automatically nahi. Ownership Q2 se ata hai.

**Q4: Buri raat ki keemat kya hai?** Harness course ka budgeting sawal, aakhri dafa poocha gaya. **Low
blast radius:** minimum unattended kit pass karo, jaldi move karo. **High blast radius:** naya ghar kit
**aur** poori suite pass kare, injection categories all-of-them pe, **koi bhi unattended shift lene se
pehle**. **Q4 kabhi destination nahi badalta. Ye speed limit set karta hai.**

> **Simple:** 4 sawal, order mein. Kaun use karta hai: sirf aap, ya doosre bhi? Kya own karna zaroori
> hai: kuch nahi, sirf kaam, ya poori loop? Kya koi screen pe wait karta hai? Aur buri raat ki keemat
> kya hai? Pehle 3 sawal ghar chunte hain. Aakhri sirf itni tezi decide karta hai jitni aap move karte
> ho.

## Concept 10: Ek Move, End to End — Ghar Jaan-Boojh Kar Mix Hote Hain

Morning-triage loop se poori course chalate hain:

**Sawal:** Q1: user aap ho, plus, pichle mahine se, 2 teammates jo report parhte hain. Ye "plus" trigger
hai. Q2: koi **must** nahi, kyunke repo pehle se GitHub pe hai. Queue mein kuch bhi custody-restricted
nahi. Q3: koi screen pe wait nahi karta. **Verdict: ghar 2**, GitHub Actions version. Q4: buri raat galat
triage labels aur ek galat escalation file karti hai — annoying, recoverable, low radius. Speed limit:
kit pass, abhi move karo, 2 hafte probation.

**Move:** Somvar: workflow file (`schedule:` trigger, headless invocation, repo se config, exit code
check, failure loud channel mein) + kit ke 3 sab se sasti controls (concurrency lock, missed-run
heartbeat, per-beat limits). Suitcase check: ek fixture laptop path use kar rahi thi, repair hui, usi
commit mein re-baseline. Naye ghar mein pehli poori-set run: sab categories bar pe. Naya baseline
committed, `runtime: actions` labeled. Agle 2 hafte: lid band, beats schedule pe, chup ka matlab
baseline, ek planted failure beech mein. Beat 10 pass, probation khatam, laptop schedule delete.

**Mix:** Poora system ab **ek ghar mein nahi hai — deliberately.** Loop ghar 2 mein hai. Eval gate wahi
CI mein hai. Heavy one-off jobs (quarterly cleanup) abhi bhi **ghar 1** mein interactively chalti hain,
jahan aap dekh sakte ho. Agar teammates client mein badal jayein, Q1 dobara fire hota hai aur **ghar 3**
conversation mein ata hai — sirf serving path ke liye. **Ghar permanent loyalty nahi hai. Har loop ke
liye 4 sawalon ka jawab hai, aur healthy system usually 2-3 gharon mein phaila hota hai.**

> **Simple:** Ghar wo jagah nahi jahan aap hamesha ke liye settle ho jate ho. Ye har loop ke liye ek
> choice hai, 4 sawalon se. Zyada tar setups 2-3 ghar ek saath use karte hain: daily loop schedule pe,
> aur heavy one-off job laptop pe jahan aap dekh sako. Ek rule mix ko mess banne se rokta hai: **repo
> truth rakhta hai, aur har ghar wahin se set hota hai.**

### Self-Check
**Sawal:** Ayesha ki invoicing loop ab 5 clients serve karti hai, ek bank hai jo demand karta hai data
uski firm ke control kiye infrastructure pe rahe. Har sawal kahan land karta hai, aur uncomfortable
honest conclusion kya hai?
**Jawab:** Q1: users clients hain — ghar 1 se aage. Q2 deciding sawal hai: bank ka *must* **execution
aur data** ke baare mein hai — kahan kaam chalta hai aur kya touch karta hai. **Managed control plane +
self-hosted sandbox** firm ke infrastructure pe ye exactly satisfy kar sakta hai, client data firm ki
custody mein rakhte hue jab ke vendor loop operate kare. Agar must control plane tak bhi jaye (prompts,
sessions, model path), sirf owned runtime jawab hai. Q3: invoicing scheduled background kaam hai. Q4:
galat invoices real clients ko — high radius: kit aur poori suite kisi bhi unattended shift se pehle.
**Honest conclusion:** koi ek ghar fit nahi baithta, aur Ayesha ne wahan touch kar liya hai jahan ek
operator akela configure nahi kar sakta — **yehi Mode 2 hai.**

---
[⬅ The Move](03-the-move.md) · [Agla: Staying Honest ➡](05-staying-honest.md)
