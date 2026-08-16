# 01 — Part 2: Har Jagah Milne Wale Shapes (Concepts 4-9)

Yeh core shapes taqreeban 70% Python cover karte hain jo aap kabhi bhi parhoge. Har ek ko
**Predict → Run → Investigate** se guzaro.

## Concept 4 — Values, Variables, 4 Types

`=` ka matlab "value ko box mein rakho" — math wala "equals" nahi. 4 basic types:

```python
name: str = "Ayesha"        # str   — text
age: int = 30               # int   — whole number
price: float = 19.99        # float — decimal
is_active: bool = True      # bool  — True/False
```

`: str` waghera **type hints** hain — optional, lekin is course mein hamesha use hote hain, kyunki yeh
code ko parhna aasan banate hain aur agent ko exactly batate hain kya banana hai.

**Predict:** `age = age + 1` ke baad `age` kya hoga? `=` ko *"compute karo right side, phir left mein
store karo"* parho — "equals" nahi.

## Concept 5 — Functions Aur Unki Signature

Function ka pehla line, **signature**, ek **contract** hai:

```python
def total_with_tax(price: float, tax_rate: float) -> float:
    return price + (price * tax_rate)
```

*"Mujhe price aur tax_rate do, dono decimals, main decimal wapis doonga."* **Aap function ka body parhe
bina bhi promise samajh sakte ho.** Body galat ho sakta hai; signature batati hai woh kya karne wala
tha.

**Pin karo test se:**

```python
assert total_with_tax(100.0, 0.15) == 115.0
assert total_with_tax(0.0, 0.15) == 0.0
```

Chup rehna matlab har claim theek hai. `assert` woh atom hai jisse har test bana hota hai.

## Concept 6 — Collections: Data Group Karna

```python
notes: list[str] = ["buy milk", "call Sara"]                   # list  — ordered, badal sakta hai
note: dict[str, str | bool] = {"title": "Meeting", "done": False}  # dict — key:value pairs
tags: set[str] = {"work", "urgent"}                             # set   — unique, no duplicates
point: tuple[int, int] = (3, 5)                                 # tuple — ordered, fixed
```

Sabse zyada milenge **list** aur **dict** — dict hi asal mein har AI agent ka data pass karne ka
tareeqa hai (JSON se directly maps hota hai).

## Concept 7 — Control Flow Aur Comprehensions

`if`/`for` decisions aur repetition karte hain. Indentation structure hai, decoration nahi.

```python
for price in prices:
    if price > 100:
        print(f"{price} is expensive")
```

**f-string:** `f"..."` mein `{...}` ki jagah value bhar jati hai.

**elif chain:** top se bottom check hota hai, pehla match jo true ho wahi chalta hai.

**Comprehension** ek `for` loop ek line mein fold kiya hua:

```python
expensive = [price for price in prices if price > 100]
```

Parho left-to-right: *"price do, har price ke liye prices mein, agar price > 100."* AI code mein yeh
shape har jagah milegi — data cleaning/reshaping mein.

## Concept 8 — Classes Aur Objects

**Class** = blueprint. **Object (instance)** = us blueprint se bana hua cheez.

```python
class Note:
    def __init__(self, title: str, body: str) -> None:
        self.title = title
        self.body = body
        self.done = False

    def mark_done(self) -> None:
        self.done = True
```

- `__init__` — setup method, jab object banta hai chalta hai
- `self` — *"yeh particular object"*
- `self.title` waghera — **attributes** (data)
- `mark_done` — **method** (action)

`object.attribute` = data parho; `object.method()` = object ko action karne ko kaho. Yeh ek pattern
poore agent code mein milega: `agent.run(task)`, `db.save(note)`.

**Pin karo:**

```python
n: Note = Note(title="Groceries", body="milk, eggs")
assert n.done is False
n.mark_done()
assert n.done is True
```

## Concept 9 — Baqi Shapes: `while`, Slicing, `try`/`except`, `input()`

Yeh 4 aap khud kam likhte ho, lekin agent inhe hamesha use karta hai — pehchanna zaroori hai.

- **`while`:** jab tak condition true rahe repeat karta hai. Dhyan rahe — condition kabhi false na ho to
  infinite loop.
- **Slicing:** `letters[1:3]` = position 1 se 3 tak (3 exclude). `letters[-1]` = last item.
- **`try`/`except`:** risky code chalata hai, error catch karta hai crash hone ki jagah.
  ```python
  def safe_divide(a: float, b: float) -> float:
      try:
          return a / b
      except ZeroDivisionError:
          return 0.0
  ```
- **`input()`:** hamesha **text** return karta hai, chahe user number type kare. Math karne se pehle
  `int()`/`float()` se convert karna zaroori hai — agar aisa na ho, yeh bug flag karo.

**Pin karo error case bhi:**

```python
def test_safe_divide() -> None:
    assert safe_divide(10.0, 2.0) == 5.0
    assert safe_divide(10.0, 0.0) == 0.0
```

> **Verify karne ke liye zaroori:** Generated code mein subtly ghalat hone ki common jagahein — kabhi na
> rukne wala `while`, off-by-one slice, silently error swallow karne wala `except`, ya math se pehle
> convert na hua `input()`.

---
[⬅ Overview](00-overview.md) · [⬆ Index](README.md) · [Agla: Power Concepts ➡](02-power-concepts.md)
