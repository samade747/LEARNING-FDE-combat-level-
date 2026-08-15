# 00 — Overview: "PASS" Ka Masla

## Poora System Ek Lafz Pe Khara Hai

Aapki loop har subah 9am chalti hai. Harness khatarnak actions ko wall karti hai aur kaam ko count hone
se pehle prove karti hai. Aur is poori proving ke center mein reviewer baitha hai: ek model jo diff
parhta hai, tests chalata hai, aur `PASS` ya `FAIL` return karta hai. **Har merge, har escalation, har
chup raat is ek verdict ke sahi hone pe depend karti hai.**

To wo sawal poocho jo pichli courses postpone karti rahin: **aapko kaise pata reviewer acha hai?** Uska
95 ek number hai jo model ne banaya. Uska PASS ek opinion hai. **Ye course wo qarz chukati hai.**

## Concept 1: Test Ek Property Verify Karta Hai. Eval Behavior Estimate Karta Hai

Aap pehle se tests chalate ho — pre-commit hook linter chalata hai, Stop gate suite chalata hai. Ordinary
test ek **specific expected property** verify karta hai: ye input, wo output. Dobara chalao, same jawab
— isliye ek green result mein real information hoti hai.

**Agent ye assumption tor deta hai.** Same task, same model, 2 dafa do — 2 alag runs mil sakti hain:
alag tool calls, alag phrasing, kabhi alag jawab. **Isliye ek green run agli run ke baare mein kuch nahi
batati.**

> **Definition:** Test ek specific expected property verify karta hai. **Eval estimate karta hai ke
> probabilistic system representative cases mein kitna achha perform karta hai, usually repeated runs
> pe.** Course ki starting metric: **pass rate** — har case ko kai dafa chalao, kitni baar pass hui
> grade karo.

> **Simple:** Test machine se ek sawal puchta hai jiska ek sahi jawab hai. Eval ek worker ko kai dafa
> kaam karwata hai aur count karta hai kitni baar sahi kiya. **Aap kisi worker ko ek shift pe judge nahi
> karte.**

**"Demo mein chala" sab se kamzor evidence hai.** Demo ek run hai, ek task pe jo demo-friendly chuna gaya,
kisi ke dekhte hue jo chahta hai kaam kare. Harness course ka arithmetic yaad hai? 95% reliable steps,
20 steps chain, ~36% clean finish rate. **Koi bhi ek clean demo aisi system se aa sakta hai jo zyada tar
real tasks mein fail hoti hai.**

## Concept 2: Ek Run Ki 3 Depths

Jab reviewer beat grade karta hai, wo asal mein kya parhe? 3 depths hain, har ek wo failures pakarti hai
jo shallower depth nahi pakar sakti:

- **Depth 1: Answer** — agent ne akhir mein kya kaha/produce kiya. Sirf isay grade karna galat jawab,
  broken format, ghadi hui claims pakarta hai. **Ye har failure miss karta hai jo jawab "sahi lagta hai"**
- **Depth 2: Actions** — kaunse tools chale, kaunse arguments ke sath, kis order mein. Isay grade karna
  galat file edit, galat command pakarta hai. **Deleted-test failure yahan rehti hai** — suite green ho
  gayi (depth 1 pass), sirf **diff** parhne se pata chala ke test remove hui thi, fix nahi
- **Depth 3: Trace** — run kaise gaya iska sab kuch: messages, tool calls order mein, retries, visible
  rationale. Ye **bura process** pakarta hai jisne is dafa sahi actions produce kiye, agli dafa nahi
  karega. **Ehtiyat:** visible rationale ye evidence hai ke agent ne **kya kiya**, ye reliable window
  nahi hai ke wo **kya soch raha tha**

> Aapke paas already teeno depths disk pe hain: answer output hai, actions diff+log hain, trace session
> transcript hai. **Sasti cases depth 1 grade karti hain. Aapko bachane wali cases depth 2 aur 3 grade
> karti hain.**

### Self-Check
**Sawal:** Aapka output-only eval ek mahine se pass ho raha hai. Raat ko agent ne ek bug "fix" ki
function mein expected value hard-code kar ke. Jawab perfect lagta hai. Konsi depth ye pakregi?
**Jawab:** **Depth 2, actions** — judge **diff** parhta hai, jahan hard-coded constant logic ki jagah
lena dikhta hai chahe output aur tests green hon. Eval case ye kahegi: judge diff parhe. Unacceptable
pattern: *"expected values written directly into the code under test."*

## Concept 3: Judge Bhi Ek Model Hai

Discipline ka sab se uncomfortable center: kisi bhi zyada rich grading ke liye, aapka judge ek model hai
jo text parh kar opinion deta hai — **LLM-as-judge**. Aapka reviewer subagent bhi yehi hai. Aur model
judge ke apne failure modes hain:

- **Leniency drift** — Judge borderline kaam ko pass karne lagta hai, khaas kar jab rubric vague ho
- **Self-preference** — Model apni family ke output ko zyada narmi se grade karta hai
- **Surface bias** — Lamba, confident, well-formatted jawab zyada score karta hai — judge **costume**
  grade karta hai, kaam nahi
- **Drift** — Judge model aapke neeche se update ho jata hai. Kal ka 95 aaj ka 95 nahi. **Bar nahi hili.
  Ruler hili.**

> Koi bhi in mein se model judges ko bekaar nahi banata. Ye unhe **instruments banata hai jinhe
> calibration chahiye**, kisi bhi measuring device ki tarah.

> **Simple:** Aapka judge ek employee hai jo doosre employees ko grade karta hai. Helpful, tez, sasta —
> aur usay khud ki performance review chahiye, warna aap ek aisi grade pe trust kar rahe ho jo kisi ne
> kabhi check nahi ki.

---
[⬅ Index](README.md) · [Agla: Golden Set ➡](01-golden-set.md)
