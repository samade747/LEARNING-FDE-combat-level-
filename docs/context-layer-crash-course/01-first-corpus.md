# 01 — Part 2: Pehla Corpus (Concepts 5-9)

Ek chota synthetic company banate hain: 2 governed records, 2 operational snapshots, aur working-context
ka folder (email/chat).

## Concept 5 — Shared Method Connect Karo, Phir Customer

Pehle woh source jise koi permission nahi chahiye — Onyx ka **Web** connector (yeh book khud, public,
governed source).

Phir **Northstar fixtures** connect karo (base folder mein ship hoti hain):

| Folder | Kya Hai |
| --- | --- |
| `sales-sor/` | 3 governed sales rules, stable ID/version/date ke sath |
| `accounting-sor/` | 4 governed accounting rules, ek **jaan-boojh kar superseded** file |
| `operational/` | 2 JSON records (approval pending, acceptance not received) — **kabhi index nahi hote** |
| `working-context/` | 3 emails, 2 chat threads — ek claim karta hai finance ne kuch agree kiya jo koi governed source support nahi karta |

**3 alag connectors, kabhi ek nahi:**

| Connector | Source Class |
| --- | --- |
| `VERTICAL-SALES-SOR` | Vertical record |
| `VERTICAL-ACCOUNTING-SOR` | Vertical record |
| `CUSTOMER-WORKING-CONTEXT` | Working context, evidence-only |

> **Caution:** Aap jo connect karte ho woh kabhi aapka nahi banta. Customer ka content customer ka
> rehta hai. Sirf **promotion law** se material upar move hota hai: pattern 3+ customers mein repeat ho,
> de-identify ho, review pass kare, aur aapke expert ki apni voice mein rewrite ho.

**Document Sets** ek search scope hai, authority hierarchy nahi. Yeh sirf batata hai kya dekha ja sakta
hai, kya governs karta hai nahi.

## Concept 6 — Sync Dekho, Chunker Ne Kya Feka

Ek governed record entry apne saath 12 cheezein carry karti hai: stable ID, domain, authority class,
jurisdiction, version, effective date, approval status, applicability, owner, superseded-by, checker,
permission boundary. Generic indexing sirf **sentence** preserve karti hai — 12 controls gayab, aur
**kuch bhi retrieved text mein unki gair-mojoodgi announce nahi karta.**

## Concept 7 — Search Karo, Dekho Kya Wapis Aya

3 sawal har result par, jab tak reflex na ban jaye:

**Kahan se aya?** Onyx yeh achha karta hai — citation wahin hai.

**Kya yeh banda dekh sakta hai?** Abhi honest jawab hai: **sab kuch sab dekh sakte hain** (Concept 8 ka
subject).

**Kya yeh abhi bhi governs karta hai?** Onyx nahi bata sakta. Superseded accounting file ka topic search
karo — dekho kaunsi version pehle ati hai.

> **Retrieval hit ek pointer hai, answer nahi.**

## Concept 8 — Permission Inheritance, Community Edition Kahan Rukti Hai

**Yeh course ka sabse important concept hai**, aur sabse zyada skip hone wala.

**Warning:** Onyx Community Edition permission-sync connectors, user groups, RBAC — yeh sab **Onyx Cloud
aur Enterprise Edition** ke features hain, Community Edition ke nahi. Pure Community Edition lab mein
**har student same corpus dekhta hai.**

**Caution:** Jab tak deployment permission test pass na kare, koi real corpus connect mat karo — na
employer ka drive, na client ka, na apna inbox. Untested-for-permission layer partial system nahi, ek
**fast** system hai jo galat rules ki taraf point kiya hua hai.

## Concept 9 — Khud Gate Banao, Ek "Kuch Nahi" Wale Role Se Test Karo

Chunki Community Edition per-user document gate nahi karta, aap gate ek layer upar, retrieval ke saamne
banate hain.

**Order sab kuch hai:**
```text
1. Identity resolve karo
2. Permissions resolve karo (yeh identity kya dekh sakti hai, har source ke liye)
3. Eligible docs filter karo — RETRIEVAL SE PEHLE
4. Retrieve aur rank karo
5. Answer assemble karo
6. Action rights alag se resolve karo
```

**Unsafe order** (jo natural lagta hai): sab kuch retrieve karo, model ko sab do, phir model ko bolo jo
reader nahi dekh sakta uska zikr mat karo. **Model context ke andar chhupa hua passage chhupa hua nahi
hota.**

```text
Add an access layer in front of Onyx retrieval. Define three roles...
Tag each fixture with the minimum role that may read it... Filter the
eligible document set by role BEFORE calling Onyx, never after.
```

**Test jo sab se zyada matter karta hai:**
```text
Build a permission test set... Include the Northstar case that matters:
ask "what did the sales manager say about booking this quarter" as
account_executive, where the correct answer is nothing at all.
```

**Done jab:** teenon roles exactly wahi dekhein jo unhe dekhna chahiye, aur `account_executive` ko manager
ki email ke baare mein **kuch na mile.** **Jo layer kabhi "kuch nahi" return nahi karta, woh test hi nahi
hua.**

> **Yeh privacy sawal nahi, control sawal hai:** Ek firm ki periodic access review certify karti hai ke
> ek named user ke paas specific entitlements hain. Aapka layer phir us user ko aisa content de deta hai
> jo woh entitlements kabhi grant nahi karte. **Context layer jo entitlement model ke bahar effective
> access deta hai, ek control nahi todta — woh chupke se un sab controls ki review ko invalidate kar deta
> hai jo usay certify karti hai.**

---
[⬅ Foundations](00-foundations.md) · [⬆ Index](README.md) · [Agla: Governed Half ➡](02-governed-half.md)
