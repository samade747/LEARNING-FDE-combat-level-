# 00 — Overview: Naya Mindset, PRIMM-AI+, Workbench

## Concept 1 — Aap Code Parhte Ho; Agent Likhta Hai

Purane Python courses "production" sikhate the: function type karo, loop type karo, class type karo. AI
ne yeh bottleneck hata diya. Ab jo skill matter karti hai woh hai **direction aur verification.**

| Purani Job (ab automated) | Nayi Job (ab bhi aapki) |
| --- | --- |
| Blank page se implementation type karna | Precisely batana kya chahiye, alfaz mein jo agent samjhe |
| Syntax yaad karna | Syntax itna pehchanna ke critically parh sako |
| Code ko chalana | Prove karna ke code *correct* hai, sirf *runnable* nahi |
| Code jahan lande wahin chhod dena | Legible rakhna, kyunki *aap aur agent* dono baad mein parhte hain |

Yeh **10-80-10 rule** hai programming par apply. Aap pehle 10% (kya banana hai
aur "correct" ka matlab) aur aakhri 10% (verify karna) own karte ho. Agent beech ke 80% (code generate
karna) own karta hai.

> **Yaad rakhne ki zaroorat nahi:** Parhna likhne se bohat aasan hai. Aapko yaad nahi rakhna ke list
> square brackets use karti hai — bas `["a", "b"]` ko list ki tarah **pehchanna** hai. Yehi is poore
> course ka bar hai: recognition, recall nahi.

## Concept 2 — PRIMM-AI+ Method

Har naya Python piece 5 steps se guzarta hai, agent har ek mein partner hota hai:

| Step | Aap Kya Karte Ho | Agent Ka Role |
| --- | --- | --- |
| **Predict** | Chalne se pehle guess karo code kya karega | Chup rehta hai — yeh aapka guess hai |
| **Run** | Chalao aur asli output dekho | Aapke liye chalata hai |
| **Investigate** | Guess ko reality se compare karo; kyun poocho | Line by line explain karta hai |
| **Modify** | Ek cheez badlo, dobara predict karo, dobara chalao | Jo edit batao karta hai |
| **Make** | Apna version specify karo scratch se; agent banaye; verify karo | Aapki spec ke against generate karta hai |

**AI+** wahi hissa hai jo isay AI-era version banata hai: agent hamesha ek reading partner ki tarah
available hai, aur **kuch bhi faith par accept nahi hota.**

**Testing sab jagah fit hoti hai.** Investigate, Modify, Make ka engine hai **test** — ek chota check jo
"correct" ka matlab pin karta hai. Pehle ek single `assert` line, phir objects par, phir validation rules
par, aakhir mein poora **Test-Driven Generation** loop.

> **Predict optional nahi hai:** Seedha Run par jaane ka instinct hota hai. Mat karo. **Aapke prediction
> aur asli output ke beech ka gap** hi wahan hai jahan learning hoti hai.

## Concept 3 — Workbench 5 Minute Mein

Chahiye: Python chalane ka tareeqa, kuch quality tools, aur aapka agent. Ek installer pehle do cover
karta hai: **uv** — ek fast package manager jo Python khud aur project manage karta hai.

Agent ko instruction do:

```text
Set up a new Python project here using uv. Add pytest for tests, pyright
for type checking, and ruff for formatting. Create a hello.py that prints
"ready". Then run it and show me the output.
```

Agent `uv` commands chalata hai, files banata hai, script chalata hai — **aap ek command bhi type nahi
karte.**

| Tool | Aapke Liye Kya Karta Hai |
| --- | --- |
| **uv** | Python aur project ke packages install karta hai, tezi se |
| **pytest** | Tests chalata hai aur batata hai kaunse pass/fail hue |
| **Pyright** | Code ke type labels parhta hai aur mismatches flag karta hai — chalne se pehle |
| **Ruff** | Style/formatting check karta hai — code ka spell-checker |

> **Reading ke liye kyun matter karta hai:** Pyright aur Ruff **reading machines** hain. Jab agent code
> generate karta hai, yeh tools usay aapke liye parhte hain aur ek poori class ki galtiyan turant pakar
> lete hain: galat type, unused variable, typo'd name.

**Agar setup fail ho:** Aapko error samajhne ki zaroorat nahi. Red text copy karo, wapis paste karo:
*"yeh fail hua. Error parho aur fix karo."* **Getting unstuck agent ka kaam hai; stuck hona notice karna
aapka kaam hai.**

---
[⬆ Index](README.md) · [Agla: Shapes ➡](01-shapes-everywhere.md)
