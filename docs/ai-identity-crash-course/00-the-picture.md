# 00 — Ek Tasveer: Venue Aur Wristband

Identity abstract lagti hai jab tak aap isay ek raat ki outing se map na karo. Yeh ek tasveer zehan mein
rakho, aur poora course usi mein fit ho jayega.

Aap ek venue par ate hain. **Door** par koi aapki ID ek dafa check karta hai — yeh **sign-in** hai, aap
kaun ho prove karna. Aapko har bar par dobara ID nahi dikhani parti. Iski jagah ek **booth** aapko ek
**wristband** print karti hai. Yeh band proof hai aap allowed ho; venue band hote hi expire ho jati hai,
aur bouncer misbehave karne par usay kaat sakta hai. Andar, **bartender** sirf band par nazar dalta hai
aur serve karta hai. Band par ek seal hai jo sirf booth bana sakti hai, isliye bartender usay bina booth
ko phone kiye trust karta hai.

| Venue Ki Cheez | Identity Term |
| --- | --- |
| **Door** — ID ek dafa check | **Sign-in** |
| **Booth** — bands print karti hai | **Issuer** (aap) |
| **Wristband** — seal ke sath | **Token** |
| **Bartender** — band par nazar | **Validator** |

**Seal ka trick:** Booth ke paas **private key** hai (stamp jo seal banata hai) — kabhi bahar nahi jati.
Booth door ke paas seal ki **saaf photo** taang deti hai — **published (public) key**. Koi bhi photo se
seal genuine confirm kar sakta hai, lekin photo se kaam karne wala stamp nahi bana sakta. **Yehi poora
trick hai:** photo stranger ko band **verify** karne deti hai bina kabhi usay **forge** karne diye.

## Frontier: Agent Ki Apni Band

Jab agent apna kaam karta hai, uske paas **apni** band hoti hai — `agent #7` ke naam, aapke nahi. Aur
kabhi kabhi ek **stamped band**: *"acting for Alice, drinks only, void at midnight, over $50 needs
Alice"* — yeh **on-behalf-of authority** hai: scope, expiry, aur human approval ke sath.

## Tokens Aur Sessions, Zero Se

**Session:** Server ko yaad rehta hai aap signed in ho. Door check karne ke baad, browser mein ek chota
marker (**cookie**) set hota hai, har request par parha jata hai — venue ko yaad hai aap aaj raat aaye
the.

**Token:** Wristband khud — kaun ho aur kya kar sakte ho iska signed claim. Common kism: **JWT** (JSON
Web Token), 3 hisse dots se jude: `header.payload.signature`. Payload claims carry karta hai; signature
booth ki seal hai.

**OAuth** (aur **OIDC** upar, "banda kaun hai" carry karne ke liye) woh agreed protocol hai jahan booth
doosri app ke liye band print karti hai: ek app banda bhejti hai sign in karne, aapka server token wapis
deta hai, doosri app usay parhti hai.

---
[⬆ Index](README.md) · [Agla: Apna Sign-In Own Karo ➡](01-own-your-signin.md)
