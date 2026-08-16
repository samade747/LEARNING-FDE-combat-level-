# 04 — Step 6: CIMD (Edge) + 50% Milestone

## Step 6 — Client Identity with CIMD (The Edge)

Steps 0-5 settled, production-grade ground hain. Step 6 iske bahar qadam rakhta hai. Ab tak app **client
registration** se prove karti thi kaun hai — pre-approved partner list mein jagah kamati thi. **CIMD**
(Client ID Metadata Document) ke sath, app list skip kar deti hai. Woh ek URL par public sign latka deti
hai jo khud ko describe karta hai, aur booth pehli baar app ke ate hi woh sign parh leti hai — koi
pre-registration nahi.

> Yeh MCP world jahan ja raha hai, lekin yeh ek Better Auth **pre-release plugin** aur ek IETF **draft**
> standard par chalta hai — isliye pehle live API confirm karo.

```text
Read specs/06-client-identity-with-cimd/spec.md... Before writing
anything, query the live Better Auth docs MCP... Then plan it, show me
the plan, move us to the Better Auth 1.7 pre-release channel, and build
it in small steps.
```

**Dekho kya switch hua:**
1. Discovery document mein nayi line dekho — client URL se khud ko identify kar sakta hai
2. Booth ko list ki jagah sign parhte dekho
3. Bad sign do (plain `http://` URL, `#fragment` wala) — refuse hona chahiye

## ~50% Milestone: Apna Pehla Project Jo Aap Drive Karte Ho

Spine ke baad, course fully-specified steps dena band kar deta hai aur **aap khud drive karo** wali
projects deta hai. Pehla halfway mark hai, stable ground par.

### Project: Apna Sign-In Harden Karo

Working sign-in ek target bhi hai — ek leaked password aur koi andar. **2 naye ideas:**

- **Second factor** — password ke bahar ek doosra proof — sirf aapka phone jo code dikha sakta hai
- **Social login** — ek doosra door — *"Continue with Google"* wahi membership tak le jata hai

```text
Read specs/projects/2fa/spec.md and specs/projects/social-login/spec.md.
Plan both, show me the plan, then build them in small steps. Harden the
sign-in you already own with a second factor, and add a "Continue with
Google" door.
```

**Done jab:** Sahi password + galat second factor refuse ho, backup code exactly ek dafa chale, "Continue
with Google" same dashboard par le jaye, koi secret response body ya log mein na dikhe.

---
[⬅ Apps Connect Karna](03-connect-apps.md) · [⬆ Index](README.md) · [Agla: Frontier — Agent Identity ➡](05-frontier-agent-identity.md)
