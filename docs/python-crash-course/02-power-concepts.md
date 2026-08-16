# 02 — Part 3: AI-Era Power Concepts (Concepts 10-15)

Yeh concepts "hello world" Python ko us Python se alag karte hain jo aap agent/ML code mein asal mein
dekhoge. Zyada tar aap **likhte nahi** — sirf **pehchante** ho. Ek exception hai type hints, jo aap likhna
seekhte ho.

> **Read-only zone — panic mat karo:** Yahan pace jump karta hai, jaan-boojh kar. **Aapse expect nahi ki
> jata yeh sab likho.** Sirf shape pehchano aur plain English mein bata sako iska kaam kya hai.

## Concept 10 — Type Hints: Agent Ko Steer Karne Wale Labels

**Type hints agent ke liye instructions hain.** Jab aap agent se pehle signature likhte ho:

```python
def summarize_notes(notes: list[dict], max_words: int) -> str:
    ...   # agent yeh part likhta hai
```

— aap ne precisely bata diya: input list of dicts hai, word limit whole number hai, output ek string
hai. Agent ab sahi cheez zyada baar generate karta hai, kyunki guesswork hata di.

> **Achhi "generate karo" request ki anatomy:**
> 1. **Typed signature** — inputs/output pin karo
> 2. **1-2 examples** — input → output (yeh aapke tests bhi ban jate hain)
> 3. **Constraints** — "empty list handle kare," "network call na kare"
> 4. **Verify karne ko kaho** — "phir pytest aur pyright chalao"

## Concept 11 — Dataclasses Aur Pydantic

Raw dict flexible hai lekin dangerous — typo'd key ya galat type chupke se pass ho jati hai.

**`dataclass`** data ko defined shape deta hai (`__init__` khud ban jata hai):

```python
from dataclasses import dataclass

@dataclass
class Note:
    title: str
    body: str
    done: bool = False
```

**Pydantic** aage jata hai — runtime par **validate** karta hai:

```python
from pydantic import BaseModel, Field

class ModelConfig(BaseModel):
    learning_rate: float = Field(gt=0.0, lt=1.0)
    batch_size: int = Field(gt=0)
```

Galat value dene par Pydantic **turant** clear error deta hai. Isiliye Pydantic agent code mein har jagah
hai — yeh JSON schemas bhi auto-generate karta hai jo LLMs tool calling ke liye use karte hain.

**Pin karo error case bhi** (`pytest.raises` se):

```python
def test_rejects_negative_learning_rate() -> None:
    with pytest.raises(ValidationError):
        ModelConfig(learning_rate=-0.05, batch_size=32)
```

> **`@dataclass` ek decorator hai:** `@` symbol function/class ke upar — label jo behavior add karta hai
> bina aap likhe.

## Concept 12 — Generators Aur `yield`

Jab lakhon records process karne hon, sab ek list mein load karna memory khatam kar sakta hai. **Generator**
items **ek waqt mein ek** hand back karta hai. Signal: `yield` (`return` ki jagah).

```python
def stream_notes(lines: list[str]) -> Iterator[str]:
    for line in lines:
        yield line.strip().lower()
```

Return type `Iterator[str]` hi generator ki nishani hai — `list[str]` (poora dher) ka promise nahi,
**stream** ka promise hai. `yield` dekho to parho: *"yeh ek stream produce karta hai, dher nahi."*

## Concept 13 — `with` — Cheezein Safely Kholo/Band Karo

Files, database connections — jo khulna aur reliably band hona chahiye, error hone par bhi:

```python
with open("notes.txt") as file:
    contents: str = file.read()
# file yahan automatically close ho jati hai, error ke bawajood
```

`with` dekho to parho: *"kuch setup karo, is block ke andar use karo, phir safely band kar do."*

## Concept 14 — `async` / `await` — Kai Cheezein Ek Sath

Jab agent 20 API calls karta hai, ek-ek karke karna 20 baar wait karna hai. **Asynchronous** code sab
requests fire karta hai aur responses ate hi handle karta hai.

```python
async def query_llm(prompt: str) -> str:
    response = await call_the_api(prompt)
    return response
```

20 calls 0.1 second ki, sequentially ~2 second lagenge; `async` se ~sabse slow single call ke barabar
time lagega. `async`/`await` dekho to parho: *"yeh code kai slow cheezein ek sath karne ke liye bana
hai."*

## Concept 15 — Dunder Methods — `model(x)` Kyun Chalta Hai

Double-underscore methods (`__init__`, `__call__`) — nickname **"dunders"** — aapke objects ko built-in
cheezon jaisa behave karne dete hain.

```python
class Pipeline:
    def __init__(self, factor: float) -> None:
        self.factor = factor

    def __call__(self, x: float) -> float:
        return x * self.factor

pipeline = Pipeline(2.5)
print(pipeline(10.0))   # 25.0 — object function ki tarah call hota hai
```

`__call__` hi wajah hai PyTorch jaisi libraries mein `model(x)` likhte hain, `model.forward(x)` nahi.
Dunders dekho to parho: *"yeh object apne aap ko native Python cheez ki tarah act karna seekh raha hai."*

> **Aap ne abhi AI code parhna seekh liya:** Aap generator ya async function scratch se **likh** nahi
> sakte abhi. Zaroorat bhi nahi. Lekin ab aap agent ki generate ki file khol kar pehchan sakte ho: "yeh
> class hai apne attributes/methods ke sath, yeh type hint hai, yeh Pydantic model tool schema define
> kar raha hai, yeh generator data stream kar raha hai." **Yehi recognition poori book ki verification
> skill hai.**

---
[⬅ Shapes](01-shapes-everywhere.md) · [⬆ Index](README.md) · [Agla: TDG Loop ➡](03-tdg-loop.md)
