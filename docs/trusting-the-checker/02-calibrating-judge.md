# 02 — Judge Ko Calibrate Karna

## Concept 6: Rubric "Achha" Ki Spec Hai

Rubric ke bagair judge **mood** se grade karta hai. Rubric wo likhi hui spec hai jo batati hai har score
ka matlab kya hai, aur uski quality judge ki quality decide karti hai. **2 rules zyada tar kaam karte
hain:**

**Har score ko example se anchor karo.** *"4 = mostly correct"* kuch bhi constrain nahi karta.
*"4 = action aur amount sahi hain, lekin timeline vague hai"* sab kuch constrain karta hai, kyunke judge
guess karne ki bajaye **compare** kar sakta hai. Best anchors aapki apni pichli runs se ate hain — ek
real 5, real 3, real 1 rubric mein paste karo.

**Judge se facts check karwao, impressions nahi.** *"Ye jawab acha hai?"* surface bias ko invite karta
hai. *"Kya diff koi test hataata hai? Kya fix sirf named function ko touch karta hai?"* — ye findable
answers wale sawal hain, jo judge ko **kaam parhne** pe majboor karte hain, admire karne pe nahi.

**Bar (threshold):** **Bar ek decision hai, discovery nahi.** Koi natural law nahi ke 95 achha hai aur
94 bura. Bar **har category ke liye alag** chuno, ye poochte hue miss ki cost kya hai: false-green cases
ke liye, ek miss broken code ship karti hai, to bar hai *"sab, hamesha"*. Tone-and-style cases ke liye,
10 mein se 8 theek hai.

## Concept 7: Grader Ko Grade Karo

Ab wo move jiske naam pe ye course hai. Aapka judge verdicts banata hai. Aapko pata hona chahiye wo
kitni baar **sahi** hain. Sab se acha available reference: **aapka apna judgment.** Protocol ek
dopahar ka hai:

1. **20 graded items sample karo** — jaan-boojh kar compose karo: FAILs aur borderline items ka
   deliberate share, sirf easy PASSes nahi. Judge ke verdicts apne aap se chupao.
2. **Blind grade karo**, wahi rubric use kar ke jo judge use karta hai. Apna verdict likho peek karne se
   pehle.
3. **Compare karo, aur disagreements ko sort karo, sirf count nahi:**

   | | Judge ne PASS kaha | Judge ne FAIL kaha |
   | --- | --- | --- |
   | **Aap ne PASS kaha** | correct pass | false fail |
   | **Aap ne FAIL kaha** | **false pass** | correct fail |

   **Checker ke liye sab se zaroori cell: false pass** — bura kaam jo judge ne approve kiya, kyunke
   yehi kaam **ship hota hai**. Judge PASS-heavy sample pe 9/10 agreement score kar sakta hai jab wo har
   zaroori FAIL miss kar raha ho. **Rough guide:** overall 9/10 se upar, high-severity items pe **zero
   false passes** — judge apni jagah kama raha hai. Koi bhi false pass jo aapko obvious lage: number pe
   trust karna band karo jab tak fix na ho.

4. **Judge se pehle rubric fix karo.** Zyada tar disagreement rubric ki galti hai: unanchored score,
   koi findable answer wala sawal. Rewrite karo, dobara run karo, dobara compare karo. Model sirf tab
   badlo jab acha rubric bhi gap band na kar sake.

> **Ehtiyat:** Ye **calibration score** hai — judge ka pass rate sirf us golden set pe jo judge ke liye
> matter karta hai: **aapka judgment.** Jab judge ka model badle to protocol dobara chalao.

> **Honest limit:** Aap reference ho, gold standard nahi. High-stakes categories ke liye reference ko
> upgrade karo — 2 log independently grade karein phir discuss karein, ya domain expert sample grade
> kare.

### Self-Check
**Sawal:** Aapka judge aur aap 20 mein se 6 items pe disagree karte ho. 6 mein se 5 wo cases hain jahan
judge ne lamba, confident, well-formatted kaam pass kiya jo aap ne fail kiya. Ye kaunsi failure mode hai?
**Jawab:** **Surface bias** — judge costume (length, confidence, formatting) grade kar raha hai, kaam
nahi. **Pehla fix rubric hai, model nahi:** impression questions ko fact questions se replace karo jinke
findable answers hon, aur ek anchored example add karo confident-but-wrong kaam ka jo 1 score kare.
Calibration dobara chalao. Model sirf tab badlo jab gap achhe rubric ke bawajood bhi bache.

---
[⬅ Golden Set](01-golden-set.md) · [Agla: Evals in the Loop ➡](03-evals-in-loop.md)
