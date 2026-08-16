# 04 — Principle 4: Small, Reversible Decomposition

> **Failure mode:** "Ek bare change ne poori dopeher ka kaam kyun barbaad kar diya?"

Bare tasks ko chote steps mein todo. Ek step khatam karo, correct hai check karo, progress save karo,
phir agle par jao. Agar kuch ghalat ho, sirf last chota step gawate ho, poori dopeher nahi.

AI bhi isi tarah best kaam karta hai. Agar 12 steps ek message mein do, AI step 5 tak drift kar jayega
aur aapko end tak pata nahi chalega. Agar wahi 12 steps ek ek kar ke do, har ek check kar ke — result
bohat behtar hota hai.

**Rule of thumb:** *agar change wapis lene mein 2 minute se zyada lage, change bara tha.*

## Enforcement Prompt

```text
Break this task into the smallest steps you can. After each step:
  1. Show me what you did
  2. Run the verification check for that step
  3. Commit / save a numbered version
  4. Wait for my OK before starting the next step
```

## Example Table

| Task | Ek Bara Prompt (Bura) | Step-by-Step (Acha) |
| --- | --- | --- |
| Letter likhna | Sab 7 paragraphs ek sath; para 3 ki galti para 7 tak unnoticed | Facts → check → argument → check → conclusion. Har galti jaldi pakri jati hai |
| Report likhna | 6 pages ek sath; revenue number galat, structure off, fix karne mein 90 min | Outline → approve → section by section. 40 min mein khatam |
| Spreadsheet | 12 tabs ek sath; formulas toot jate hain | Ek tab ek waqt, pichle se compare karke |

## Pixar Lesson

1998 mein Pixar ki *Toy Story 2* production files galti se delete ho gayi — 2 saal ka kaam, seconds mein
gaya. Backup weeks pehle fail ho chuka tha, kisi ko pata nahi chala. Sirf isliye bachi kyunki ek employee
ke paas ghar par personal copy thi. **Progress save karna kuch aisa nahi jo yaad rakhna pare — process
mein built-in hona chahiye.**

## Undo Trap

Sarah ne budget file edit ki, aur bigar di. `git reset --hard` chalaya — budget fix ho gaya, lekin
volunteer list bhi mit gayi jo usne ek ghanta edit ki thi (kyunki commit nahi ki thi). `git reset --hard`
**sab kuch** wapis le jata hai last save point tak. **Agar save nahi kiya, gaya.**

**Sabak: chote steps mein baar baar save karo. Aapke last save ka size — utna hi max kaam aap gawa
sakte ho.**

## Hands-On Practice

Course "Pack 3 — Decomposition" deta hai: case brief + style guide. Same demand letter do tareeqon se
banwao — pehle ek prompt mein (Run A), phir 4 steps mein pause karke (Run B). Run A mein usually ek
problem hoti hai (style guide violation, galat number, vague deadline). Run B cleaner hota hai kyunki
har section aapne parh kar check kiya.

**Sabak:** AI equally capable hai har section likhne mein. Problem yeh nahi ke AI bura hai — problem yeh
hai ke section 4 tak pahunchte pahunchte AI shuru ke rules bhool jata hai. Checkpoints hi farq banate
hain.

## Apne Kaam Par Apply Karo

1. Woh kaam chuno jo pehle ek-shot mein likha tha aur unhappy the.
2. Shuru karne se pehle 4-7 steps list karo, har ek ke liye ek check line.
3. Har step ke baad save karo (git commit, ya numbered versions `-v1`, `-v2`).
4. AI ko aage rush mat karne do — "one step at a time."

**Kyun matter karta hai:** Sabse buri galtiyan ek bare obvious failure se nahi atin — chote errors se
atin jo lambe uninterrupted run mein jama hote hain. Har step check karna unhe jaldi pakarta hai, aur
aapko beech mein direction badalne deta hai bina pehle steps gawaye.

---
[⬅ Principle 3](03-principle-3-verification.md) · [⬆ Index](README.md) · [Agla: Principle 5 ➡](05-principle-5-persisting-state.md)
