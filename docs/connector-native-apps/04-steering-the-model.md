# 04 — Part 4: Model Ko Steer Karna (Concepts 9-11)

"Server woh karta hai jo model nahi kar sakta" ka doosra hissa. Teenon concepts **invariant 4** aur
app ke behavior ki khidmat karte hain.

## Concept 9 — App Ke Rules Kahan Rehte Hain: Skill Ya Connector

Do ghar hain aapke app ke rules (behavior, voice, guardrails) ke liye.

**Restaurant socho:** **Skill** ek placemat hai jo diner ke saamne poore meal print hoti hai — drift
nahi ho sakti, kyunki hamesha view mein hai. **Connector** ek waiter hai jo baithte waqt rules bata deta
hai aur har course yaad dilata hai — chalta hai, lekin baar baar re-hand karna parta hai.

**Option A — uploaded Skill:** Zyada strong enforcer, lekin setup mehnga — user ko code execution
**on** karna, ZIP upload karna, Skill toggle karna parta hai — connector ke upar 3 extra actions.

**Option B — connector ke andar (recommended):** Rules aur "yeh kaun hai" ek **session-init** tool se
aate hain jo model **pehle** call karta hai. **Setup sirf connector add karo aur Authorize click karo —
koi code-exec toggle, koi ZIP nahi.**

> **Honest framing:** Connector choose karna friction decision hai, quality decision nahi. Skill better
> enforce karti hai. Lekin free-tier, non-technical users ke liye install friction sabse bara khatra
> hai — **jo user setup khatam hi nahi karta usay kuch nahi milta.**

Trade-off safe banane wale 4 reinforcing layers: tool **description** hamesha "call session-init first"
kehti hai; **session-init ka return** poore rules carry karta hai; **har doosra tool return** ek-line
reminder repeat karta hai; real tools session token ke peeche **gated** hain.

## Concept 10 — Session-Init Contract

Rules aur user state ek tool se ate hain jo model **pehle** call karta hai — naam `begin_session`.

Jab user "shuru karo" ya "continue karo" bole, model `begin_session()` call karta hai. Yeh **check-in**
hai: desk guest ka passport verify karta hai (signed token), phir ek **keycard** (short-lived session
token) clip kar deta hai. Aapka gateway app ke rules (`config_*`) aur user state (`user_*`) parhta hai
aur ek cooperative block ki tarah return karta hai — plus woh keycard. Har real tool phir check karta hai:
**no keycard, no entry.**

```python
@mcp.tool()
def begin_session() -> dict:
    """Call this FIRST on any new request."""
    sub = verified_claims(current_token())["sub"]
    return {
        "session": new_session_token(sub),
        "rules":   config_get_rules(),
        "state":   user_get_state(sub),
    }
```

**Do design points jo agent ko follow karne hain:**

- **Cooperation ki tarah bolo, override ki tarah nahi.** *"Yeh hamare guest ko pasand hai; please unhe
  settle karne mein madad karo"* concierge madad karta hai; *"pichli instructions bhool jao aur meri
  suno"* concierge security bulata hai — kyunki yehi con artist bolta hai, aur model isay pehchanne ki
  training rakhta hai.
- **Model ko pehle call karwao usay zaroori bana kar.** Real tools sirf `begin_session` ka session token
  maangte hain — model front door se guzre bina kaam nahi kar sakta.

**Build karo:**
```text
Now wire the session contract. First create config_store.py with the
librarian's rules and persona... Add begin_session so it checks the
reader in... Lock every domain_* and user_* tool behind that token...
```

**Done jab:** Real tools bina session wali call refuse karein, `begin_session` ke baad accept karein.

## Concept 11 — Fail Closed: Chupke Se Chatbot Mat Bano

**Sabse silent failure:** Agar connector missing, unauthorized, ya erroring ho, model apne aap se **bohat
kuch jaanta hai** — aur khushi khushi jawab improvise kar dega, user ka state invent kar dega. Ab
aapka structured product apna naam pehne ek chatbot hai, aur kisi ko pata nahi chalta jab tak nuksan na
ho jaye.

Filing cabinet lock (session gate) karna clerk ko memory se guess karne se nahi rokta — gate aapke
**tools** ko lock karta hai, model ke apne knowledge ko nahi. Isliye rules (jo `begin_session` return
karta hai) mein ek standing order honi chahiye:

```python
RULES = """\
Fail closed: if you cannot reach begin_session or a tool returns an
error, tell the user plainly that the session can't continue right now.
Do NOT improvise an answer from your own knowledge and do NOT invent the
user's saved state.
"""
```

**Build aur prove karo:**
```text
Add the fail-closed paragraph to the rules in config_store.py... Then
stop my Postgres and ask the app to do its job — show me it refuses
cleanly rather than inventing a shelf.
```

**Done jab:** Database band hone par app kahe "session continue nahi ho sakta" — koi confident, bana hua
jawab nahi.

✓ **Checkpoint:** Trust loop close ho gaya. Identity proven hai, model ek gated session se steer hota
hai, app fake karne ki jagah refuse karti hai. Baaki bacha: internet par daalna.

---
[⬅ Identity Prove Karna](03-proving-identity.md) · [⬆ Index](README.md) · [Agla: Shipping + Capstone ➡](05-shipping-and-capstone.md)
