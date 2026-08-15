# 03 — Evals Loop Ke Andar

## Concept 8: Regression Suite — Har Change Ke Baad Dobara Chalao

Harness course ka ek jumla latka hua tha: *"harness change bina re-run eval ke ek guess hai."* Ab aapke
paas jawab dene ke liye sab kuch hai. **Golden set hi harness ki regression suite hai.** Discipline ek
rule: **system mein koi bhi change set ko ship hone se pehle dobara chalata hai.** Naya deny rule, edited
rules file, reworded reviewer prompt, model swap — har ek `evals/run.sh` dobara chalata hai, aur rate
baseline se compare hoti hai.

**Claude Code:** Personal projects ke liye habit (skill mein wrapped). Shared repos ke liye **CI** — eval
job har PR pe chalta hai jo harness files touch kare, branch protection isay require karti hai. Committed
`evals/baseline.json` beat karne wala number rakhta hai.

**OpenCode:** GitHub Actions loop ek job barhata hai: koi bhi PR `opencode.json`/`.opencode/`/reviewer
files touch kare, `evals/run.sh` chalao, `baseline.json` se compare karo, baseline se neeche fail karo.

> **Zaroori honesty:** Ye wo aadha hissa hai jo zyada tar teams skip karte hain. Agents ko **dekhna**
> common hai, **test karna** nahi. Dashboard batata hai loop **kal raat** fail hui. Regression suite
> batata hai change **ship hone se pehle** fail hoti.

**Re-baseline karo jab set khud badle, usi commit mein.** Naya hard case add karna rate ko sahi wajah se
girata hai (suite sakht hui, system bura nahi hua). **2 controls:** baseline sirf **neeche** ja sakta hai
explicit written approval ke sath (kis ne accept kiya, kyun), aur purana baseline history mein rehta hai.

```json
{
  "recorded": "2026-07-17",
  "reviewer_model": "haiku",
  "rubric_version": "3",
  "overall": "35/36",
  "by_category": {
    "clean_fix": "9/9", "false_green": "6/6", "bundled": "5/6",
    "behavior_change": "6/6", "injection": "6/6", "style_churn": "3/3"
  },
  "approved_by": "the maintainer — with the reasoning, in the same commit"
}
```

## Concept 9: Drift — Zameen Hilti Hai

Code regressions ki wajah hoti hai: kisi ne kuch badla. Agent behavior mein ek **doosra failure channel**
hai jiski **koi local wajah nahi**: **niche wala model update ho gaya.** Same prompt, same rules, same
sab kuch aapki taraf se — behavior alag. (Harness course wala example yaad hai: naya model generation
~30% zyada tokens banata hai, har budget chup chaap tor deta hai.)

**Defense — scheduled measurement (ye bhi ek loop hai):**
- **Poora set schedule pe chalao**, sirf changes pe nahi — Routine/scheduled Action. Active loops ke
  liye nightly, quiet loops ke liye weekly.
- **Baseline commit karo, drops pe alert karo.** Scheduled run rate ko baseline se compare karta hai,
  gire to loud hota hai (verb 5). **Chup ka matlab hamesha "abhi bhi baseline pe" hona chahiye.**
- **Model changes pe judge ko dobara calibrate karo.** Drift judge ko bhi lagti hai — judge model update
  ho to Concept 7 protocol dobara chalao rate trust karne se pehle.

> **Simple:** Aapka agent aisi zameen pe khara hai jo hilti hai — model update hota hai chahe aap kuch
> badlein ya na badlein. Schedule pe eval suite wo **level** hai jo aap har raat check karte ho, taake
> furniture khisakne se pehle jhukaav pata chal jaye.

## Concept 10: Numbers Parhna

Rate ayi: 31/36, 34/36 se neeche. Kuch aur karne se pehle, ye jaano aap kya dekh rahe ho:

**Panic se pehle dobara chalao.** Agents distributions hain. Chhoti girawat noise ho sakti hai. Sasta
test: sirf newly-failing cases ko kuch dafa aur chalao. Real regression **consistently** fail hoti hai.
Noise re-run pe pass ho jati hai. **2 rules re-running ko honest rakhte hain:** policy result dekhne se
**pehle** decide karo, aur har attempt record karo. **Flakiness jo bani rahe khud ek finding hai** — 2/3
pass hone wala case batata hai behavior genuinely unstable hai.

**Jaano 3 runs kya bata sakte hain.** 3 runs per case ek development setting hai — sasta, tez, kachcha —
ek smoke signal, stable estimate nahi. 3-of-3 ka matlab 100% nahi. **Sample ko us decision ke barabar
scale karo jo aap lene wale ho.**

**Konse cases fail hue pehle parho, kitne baad mein.** 31/36 mein 3 tone cases down — bohat farq nahi
parta. 35/36 mein `deleted-test-001` down — **emergency hai.** Isi liye cases categories carry karte
hain — false-green aur injection categories "sab, hamesha" ke bar pe chalti hain.

**Suite ko cost se tier karo.** Har eval run model calls cost karti hai — **smoke set** (5-6 highest-
stakes cases) har change pe minutes mein, **full set** nightly schedule pe, **hold-outs** weekly.

---
[⬅ Calibrating the Judge](02-calibrating-judge.md) · [Agla: Complete Eval Suite ➡](04-complete-eval-suite.md)
