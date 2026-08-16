# 03 — Step 4-5: Real App Connect Karo + Resource Server

## Step 4 — Ek Real App Connect Karo

Ab prove karo booth kisi aur ke liye bhi kaam karti hai. **Client app** ek alag venue hai jo aap se log
sign in karwati hai bina aapke koi secret share kiye. Issuer ko **AuthCo** naam do, nayi app ko **Notes**.
Notes koi password nahi dekhti, koi database nahi chhuti.

```text
Read specs/04-connect-a-real-app/spec.md... Plan the approach, show me
the plan, then build it in small steps. Keep Notes a fully separate
process. Run the spec's acceptance checks.
```

**Separation genuine hai prove karo:**
1. Notes ke paas `BETTER_AUTH_SECRET` ki koi copy nahi — sirf public photo (key) se verify kar leti hai
2. `aud` claim ek character se todo — Notes ka verifier reject kare
3. AuthCo par client revoke karo — Notes ki agli call fail ho

## Step 5 — Ek Resource Server Connect Karo

**Resource server** ek bar hai jo sirf bands check karta hai, kabhi sign in nahi karwata — wahi
**bartender** jo aap ne Connector-Native Apps mein khela tha, ab apni zameen par. Yeh **bearer token**
leta hai (jo bhi band pakre, bas dikhaye), **audience** stamp parhta hai (*"is bar ke liye acha"*), aur
**RS256** signing algorithm check karta hai.

```text
Read specs/05-connect-a-resource-server/spec.md... Configure AuthCo to
sign RS256 tokens audience-bound to my API, stand up a tiny protected
resource that verifies offline via JWKS.
```

**Loop band karo:** Apna connector ([Connector-Native Apps](../connector-native-apps/README.md) se) laao,
uski issuer settings AuthCo par point karo — dekho woh aapke issuer ki token accept karta hai.

**Attack tests jo koshish karne layak hain:**
1. **Galat algorithm:** EdDSA se sign karo, RS256-only verifier ko do — reject hona chahiye
2. **`alg: none` attack:** signature strip karo, header mein `alg: none` set karo — reject
3. **Sneaky forgery:** public key ko HMAC secret ki tarah use kar ke `HS256` se sign karo — RS256-pinned
   verifier reject kare (yehi wajah hai algorithm **pin karna** zaroori hai, token ke header se parhna
   nahi)
4. **Galat audience:** valid band ki `aud` badal do — refuse honi chahiye chahe signature genuine ho

---
[⬅ Issuer Banna](02-become-the-issuer.md) · [⬆ Index](README.md) · [Agla: CIMD + Milestone ➡](04-cimd-and-milestone.md)
