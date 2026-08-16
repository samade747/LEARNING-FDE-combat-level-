# Summary — Project 2: Build Your Portfolio

**Concept:** 5 — Run-Until-Done (Conditional Loop)
**Source:** 100% official (`panaversity/agentfactory-labs`)

## Kya Sikhata Hai

Loop ko **command** rokti hai, timer nahi. "Jab tak taste na ho jaye" wala idea.

## Kyun Zaroori Hai

Zyada tar kaam "har 5 minute check karo" jaisa nahi hota — "yeh khatam hone tak koshish karo" jaisa
hota hai. Yeh project sikhata hai ke stopping condition ko itna precise likhna zaroori hai ke ek
command usay **prove** kar sake, warna loop bhatakti rehti hai.

## Kaise Kaam Karta Hai

Apna CV ya LinkedIn PDF `portfolio-starter/` folder mein daalo, phir `/goal` ko finish line do:

```text
/goal Build my portfolio in site/ from my-cv.pdf... Done when check.py prints 20/20
and the reviewer agent replies PASS on all six judgment promises...
Stop after 15 check attempts or 3 review rounds.
```

Agent CV parhta hai, design decide karta hai, page banata hai, `check.py` chalata hai, apni failures
parhta hai, aur dobara koshish karta hai — jab tak yeh sentence sach na ho jaye.

**Asal lesson:** agent apna kaam khud approve nahi karta. **20/20 "done" nahi hai** — reviewer ko 6
judgment promises bhi PASS karni parti hain jo koi command measure nahi kar sakti (jaise "kya yeh
genuinely designed hai, sirf formatted nahi?"). **Golden rule:** kabhi `check.py` ko edit mat karo
taake wo pass ho jaye.

## Maine Kya Test Kiya

`check.py site` khud chalaya — bina `profile.md` ke saaf, sahi error deta hai ("profile.md is
missing... Copy profile.template.md to site/profile.md and fill it in"). Yeh confirm karta hai checker
sahi kaam kar raha hai. **Poora chalane ke liye aapka CV chahiye** (main woh provide nahi kar sakta).

---
[⬆ Poori Project List](../../README.md#runnable-projects-poore-12-har-ek-ki-real-jagah)
