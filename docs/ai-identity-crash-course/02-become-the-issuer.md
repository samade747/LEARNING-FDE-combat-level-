# 02 — Step 2-3: Issuer Bano + Scopes Aur Consent

## Step 2 — Become the Issuer (The Marquee)

**Yeh woh step hai jispar poora track point kar raha tha.** [Connector-Native Apps](../connector-native-apps/README.md)
mein aap **bartender** the — aisi tokens **validate** karte the jo kisi aur ne sign ki thi. Yahan aap
counter ke peeche jate ho aur **booth** ban jate ho. Jab doosri app kisi ko sign in ke liye bhejti hai,
aapka server signed token wapis deta hai jo doosri app **khud** verify kar leti hai — public seal ki
photo se, bina password dekhe, bina database call kiye.

**Handshake samjho:** Jab ek **OAuth client** (doosri venue) banda bhejta hai sign in karne, band seedha
browser se wapis nahi jati. **Authorization-code flow** chalta hai: banda booth par sign in karta hai,
aap app ko ek short-lived **code** dete ho (claim-check stub), app chupke se usay real token se swap kar
leti hai. **PKCE** ek-line proof hai ke wahi app jispar handshake shuru hua, wahi khatam kar rahi hai —
churaya hua stub kisi kaam ka nahi. Band print hone se pehle, banda ek **consent** screen par approve
karta hai.

```text
Read specs/02-become-the-issuer/spec.md and the agent-identity-issuer
skill. Plan it, show me the plan, then build it in small steps. Build
the token verifier as a separate script so the checks are real, and run
all the acceptance criteria, especially the adversarial ones.
```

**3 Understand Prompts (koi spec nahi, sirf dekhne ke liye):**

1. **JWKS endpoint dekho** (seal ki photo, private key nahi hoti):
   ```text
   Fetch my JWKS endpoint and show me what's there. Is my private
   signing key in it? Prove it.
   ```
2. **Band parho, ek character se todo:**
   ```text
   Take an ID token you just issued, decode it... Then change the aud
   by one character and show me the verifier rejecting it.
   ```
3. **Band ko expiry ke baad push karo:**
   ```text
   Issue a token, then move the clock past its expiry and try to use
   it. Show me the exact rejection.
   ```

## Step 3 — Scopes Aur Consent

Token exactly bataye kya kar sakta hai, zyada nahi. **Scope** (band kya allowed hai — jaise "drinks
only" vs "drinks and kitchen") aur **consent screen** jahan banda approve karne se pehle exact list
dekhe. Least privilege real ban jata hai.

```text
Read specs/03-scopes-and-consent/spec.md... Plan the approach, show me
the plan, then build it in small steps. Run the spec's acceptance
checks, especially the adversarial ones.
```

**Prove karo limit real hai:**
1. Chota token do, overreach karne ki koshish karo — refuse hona chahiye
2. Consent screen dekho — sirf woh dikhaye jo signed request mangti hai
3. Zyada authority lene ki koshish karo jo register nahi ki — granted scope mein missing dikhna chahiye

---
[⬅ Apna Sign-In](01-own-your-signin.md) · [⬆ Index](README.md) · [Agla: Apps Connect Karna ➡](03-connect-apps.md)
