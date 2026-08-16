# 03 — Part 3: Identity Prove Karna — Jo Model Fake Nahi Kar Sakta (Concepts 7-8)

Yeh "server woh karta hai jo model nahi kar sakta" ka pehla hissa hai. Dono concepts **invariant 3**
hain.

## Concept 7 — Identity Verified Subject Se, Model Se Kabhi Nahi

Problem: aapki `user_state` table ko **sahi** person ki row mein likhna hai. Lekin model hi user se baat
kar raha hai, aur **model ko kabhi decide nahi karne dena ke kiska data parhna/likhna hai.**

AI ko ek hotel concierge socho jo guest ke liye kaam karta hai. Jab concierge front desk ko kahe "room
412 apna mail chahta hai," desk usay uski baat par mail nahi de sakta — ek confused ya manipulate hua
concierge galat room bata sakta hai, kisi aur ka mail leak kar sakta hai. Agar Claude aapko `user_id`
pass kar sake, yehi khatra hai — ek user doosre ka data dekh lega.

**Rule: model kabhi identity supply nahi karta.** Jab user connector authorize karta hai, woh ek trusted
service se sign in karta hai jo aapke server ko ek signed token deti hai jisme user ka verified id —
**subject**, ya `sub` — hota hai. Yeh token guest ka **passport** hai: desk isi se padhta hai kaun hai,
concierge fake nahi kar sakta. Aapka server `sub` seedha token se parhta hai aur usay database key ki
tarah use karta hai.

Yeh rule **given** `auth.py` enforce karta hai — isliye yeh file complete ship hoti hai aur aap kabhi
rewrite nahi karte.

## Concept 8 — Sign-In (OAuth), Plain English Mein

Yahan mechanism **OAuth** hai — wahi "Sign in with Google." Yeh concept slow karne wala hai — kyunki
failure mode sneaky hai: auth code **dikh** sakta hai sahi lekin chupke se ghalat ho sakta hai.

> **Poori idea 5 lines mein:** User kahin aur sign in karta hai. Woh service ek signed token issue karti
> hai. Aapka server token verify karta hai. Aapka server `sub` token se parhta hai. Model kabhi identity
> supply nahi karta.

**2 jobs, aap sirf 1 karte ho:** Sign-in hard hai aur liability (aap passwords rakhte). To aap nahi karte
— ek specialist login handle karta hai aur ek **token** deta hai. Aapka server sirf **check** karta hai.

| Party | Kaun Hai | Aap Banate Ho? |
| --- | --- | --- |
| User | Data jiska hai | — |
| Claude's MCP client | Anthropic ke cloud mein, user ki taraf se poochta hai | Nahi |
| Sign-in service | Clerk/Auth0/Stytch (rented) ya Better Auth (self-host) | Nahi — rent ya self-host |
| Aapka gateway | Sirf tokens **check** karta hai | Haan |

**Flow:**
1. **Discovery** — bina token wali call `401` deti hai (yeh universal "sign-in karo" signal hai). Claude
   aapke server ke `/.well-known/oauth-protected-resource` note ko follow karta hai
2. **Sign-in** — user consent screen dekhta hai, Google/email se login karta hai. **Koi password Claude
   ya aapke server ko kabhi nahi chhuta**
3. **Token** — sign-in service short-lived token deti hai jisme verified `sub` aur ek *audience* (aapke
   server ke liye stamped) hoti hai
4. **Har call ke baad** token carry hota hai; server check kar ke `sub` parhta hai

**4 Checks (border desk passport inspection ki tarah):**

| Check | Sawal | Agar Skip Kiya Jaye |
| --- | --- | --- |
| Genuine? | Real signed token, forgery nahi? | Koi bhi koi bhi naam se token forge kar sakta hai |
| Trusted issuer? | Hamari sign-in service se aaya? | Kisi bhi service se token accept ho jayega |
| Stamped for us? | Isi server ke liye minted? | **Sabse dangerous** — doosri app ka token replay ho sakta hai |
| Still in date? | Expire to nahi hua? | Chura hua token hamesha kaam karta rahega |

Ek rule in 4 ke upar: identity `sub` se aati hai, tool argument se kabhi nahi (Concept 7).

**Build karo, 2 steps mein (strong model par):**

**Prompt 1 — lock lagao:**
```text
Wire the OAuth layer around the given auth.py, and don't rewrite auth.py.
... so an unauthenticated tool call returns HTTP 401. Show me an
unauthenticated call returning 401.
```

**Prompt 2 — prove karo lock discriminate karta hai:**
```text
Mint a token from the mock and show me it resolves its sub through
auth.verified_claims. Then mint a token for a different audience... show
me it's rejected.
```

**Done jab:** Achha token `sub` resolve kare, wrong-audience token reject ho, aur aap ne 4 checks kaam
karte dekhe hon.

## Beginner Track: Rehearsal, Real Nahi

Aap ne poora flow **rehearse** kiya — real mein part nahi bane. Production mein:

| Step | Laptop Par (Rehearsal) | Production Mein |
| --- | --- | --- |
| Kaun sign in karta hai | Koi nahi; aap stand-in | **End user**, Authorize click par |
| Token kaun mint karta hai | Local `mock_auth` | Real sign-in service |
| Server tak kaun le jata hai | Aapka test script | Claude ka cloud |
| Server kya karta hai | 4 checks | **Wahi** 4 checks |

**Zaroori:** Aapka gateway aur `auth.py` in dono columns ke beech **nahi badalte.** Real version mostly
ek swap hai — mock ki jagah real sign-in service.

✓ **Checkpoint:** Server jaanta hai kaun hai. Identity token se aati hai, model se nahi. Ab model ko
**behave** karwana hai.

---
[⬅ State Aur Domain](02-state-and-domain.md) · [⬆ Index](README.md) · [Agla: Model Ko Steer Karna ➡](04-steering-the-model.md)
