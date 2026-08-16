# 03 — Part 4: TDG Loop End-to-End (Concepts 16-17)

## Concept 16 — Ek Poora Cycle: Test-Driven Generation

TDG purana order ulta karta hai. Purana: *code likho → shayad test karo*. Naya: **failing test likho jo
"correct" define kare → agent code generate kare → test se verify karo.** Test afterthought nahi hai —
yeh **specification** hai. Aur test **aap se** aani chahiye — agar agent code aur test dono likhe, to aap
AI ke kaam ko AI ki apni expectations se check kar rahe ho — koi independent signal nahi.

**Step 1 — Requirement ko failing tests ki tarah likho** (`test_tax.py`):

```python
from tax import total_with_tax

def test_basic() -> None:
    assert total_with_tax(100.0, 0.15) == 115.0

def test_zero_price() -> None:
    assert total_with_tax(0.0, 0.15) == 0.0
```

`pytest` abhi chalao — fail hoga, kyunki `tax.py` exist hi nahi karti. **Yeh failure hi poora point hai.**
Aapke paas ab ek precise, executable "done" ki definition hai.

**Step 2 — Agent implementation generate karta hai:**

```text
Read test_tax.py. Create tax.py with a total_with_tax(price: float,
tax_rate: float) -> float function that makes both tests pass. Then
run pytest and show me the result.
```

**Step 3 — Aap verify aur iterate karte ho.** `pytest` output parho. `2 passed` matlab code aapki spec
meets karta hai. Agar red ho, traceback parho, phir refine karo — **blindly dobara prompt mat karo.**

> **Dhyan rahe:** Agar agent failing test ko **test** badal kar pass karwaye, na ke **code** badal kar,
> usay roko. Test aapki spec hai; agent ko spec rewrite karne ki ijazat nahi.

| TDG Step | Kaun Lead Karta Hai | PRIMM-AI+ |
| --- | --- | --- |
| Requirement + failing tests likhna | **Aap** (pehle 10%) | Make |
| Implementation generate karna | **Agent** (80%) | — |
| Tests chalana, verify, iterate | **Aap** (aakhri 10%) | Investigate/Modify |

> **Yeh loop har cheez par use karo — finale nahi, default hai.** Har unit jo agent produce kare aur
> jiska checkable contract ho — har function, har method, har validation rule — isay TDG se guzaro.
> **Rule:** agar aap kisi cheez ke liye test nahi likh sakte, aap abhi nahi samajhte "correct" ka matlab
> uske liye — aur na hi agent samajhta hai.

## Traceback Parhna (Jab Kuch Toote)

Python fail hone par **traceback** print karta hai — red text ki deewar jo darawni lagti hai lekin asal
mein gift hai. **Bottom-up parho:** last line error naam leti hai, upar wali lines batati hain kahan hua.

```
Traceback (most recent call last):
  File "tax.py", line 2, in total_with_tax
    return price + (price * tax_rate)
TypeError: can't multiply sequence by non-int of type 'float'
```

Aapko khud fix karne ki zaroorat nahi — **itna parhna hai ke agent ko exactly batao kya ghalat hai.**

**6 Common Errors (yaad nahi karne — pehchanne hain):**

| Last Line Kehti Hai | Matlab | Agent Ko Kya Batao |
| --- | --- | --- |
| `ModuleNotFoundError`/`ImportError` | Package install nahi hai | "X install nahi — uv se add karo" |
| `NameError` | Naam define hi nahi hua (typo) | "y use hua lekin defined nahi — typo?" |
| `TypeError` | Galat kism ki value | "number text ki tarah aa raha hai — convert karo" |
| `AttributeError` | Object ke paas woh cheez nahi hai | "is object mein `titel` nahi — typo lagta hai" |
| `KeyError` | Dict mein woh key nahi hai | "key 'x' dict mein nahi — missing case handle karo" |
| `IndexError` | List mein woh position nahi hai | "list expected se chhoti hai" |

> **Kabhi blindly dobara prompt mat karo:** Sabse mehnga habit hai bina parhe "try again" dabana. Agent
> khushi khushi ek **doosra** ghalat jawab dega. Traceback parho, asal problem samjho, phir describe
> karo.

## Concept 17 — Vague Goal Se Specifiable Pieces Tak

Concept 16 ne ek unit spec/verify karna dikhaya. Real projects ek vague sentence ki tarah ate hain:
*"ek tool banao jo meri notes summarize kare."* Isko ek test nahi likh sakte. **Decomposition** skill
hai — goal ko chote pieces mein todna, har ek itna chota ke typed signature aur test mil sake.

**5 Steps:**

1. **Goal ek sentence mein bolo.** *"Meri notes parho, batao kitni done hain, kaunsi pending hain."*
2. **Steps list karo jo haath se karte.** Verbs: *load* → *count* → *find* → *summarize* → *print*. Har
   verb ek candidate unit hai.
3. **Har unit ko typed signature do — input se output.** Yehi spec hai. Body abhi nahi; agent likhega.
   ```python
   def load_notes(path: str) -> list[Note]: ...
   def count_done(notes: list[Note]) -> int: ...
   def pending_titles(notes: list[Note]) -> list[str]: ...
   def summarize(notes: list[Note]) -> str: ...
   ```
4. **Har unit ko TDG karo, order mein.** Har line ab exactly Concept 16 ka cycle hai.
5. **Sab wire together karo aur poora flow test karo.** Agent se `main()` likhwao jo sab pieces order
   mein call kare.

**Yeh dekho hua:** ek vague sentence 4 chote, independently-verifiable contracts ban gaye. Agent ne har
line code likhi. Lekin **aap** ne pieces dhoonde aur decide kiya har ek kya promise karta hai.

> **Heuristic:** agar kisi unit ka test likhna mushkil hai, woh bohat zyada kaam kar rahi hai. Split
> karo. Jo function test nahi ho sakta, woh verify bhi nahi ho sakta.

**Reusable prompt template** (har project ke liye):

```text
I want to build: [your one-sentence goal]

First, break it into 3-5 small functions or classes.
For each unit, propose ONLY:
  1. a typed signature (inputs and output)
  2. expected behavior in one line
  3. edge cases to consider
  4. pytest tests

Do NOT write any implementation yet. Wait for me to approve the tests.

After I approve, generate the implementation to pass those tests.
Then run pytest, pyright, and ruff, and show me only the
changed files and the test results.
```

Do zaroori lafz: **ONLY** aur **NOT** — yeh agent ko code (aur uske apne tests) likhne se rokte hain jab
tak aap decide na karo "correct" kya hai.

---
[⬅ Power Concepts](02-power-concepts.md) · [⬆ Index](README.md) · [Agla: Judgment + Practice ➡](04-judgment-practice.md)
