# 04 — Scenarios 4-5: Uski Ledger Aur Override Sikhna

## Scenario 4 — Uske Decisions Apne Se Alag Batao (~10 min)

Claudia ke loop ne abhi aapke naam par dozen calls li, aap kuch kiye bina. Ab woh sawal jo aapko thora
nervous karna chahiye — aur yeh nervousness healthy hai: mahino baad, kya aap bata sakte ho kaunse
calls uski thin aur kaunse aapki? Agar nahi bata sakte, aap ne delegate nahi kiya — track kho diya.
Yeh scenario prove karta hai aap hamesha bata sakte ho.

> Jab Claudia kuch approve karti hai aur jab aap khud approve karte ho, company ke records **identical**
> lagte hain. Dono sirf "approved by the board" kehte hain, kyunki woh aapki authority se act karti hai,
> wahi stamp jo aap use karte ho — company akele kabhi farq nahi bata sakti. **Fix:** Claudia apni
> **apni signed ledger** rakhti hai, ek logbook uske decisions ka. Jab bhi **woh** decide karti hai,
> ek line likhti hai "maine yeh kiya, aur yeh wajah hai," signed taake fake na ho sake. Aap koi aisi
> line nahi likhte. Company ke records ko uski ledger ke sath rakho, shared approval se match karo,
> aur poori story mil jati hai: company batati hai **kya** approve hua, uski ledger batati hai **kaunse
> uske the.**

**Coding agent ko paste karo:**
```text
So I have one to compare against, let me clear one approval directly myself the way I sometimes
will. Then show me, side by side, that one approval and one Claudia's loop cleared on its own this
week: I want to see they look identical in the company's records, and that only her own signed
ledger tells them apart. Then have Claudia send me a one-screen summary of everything she handled
this week.
```

**Done jab:** apni ankhon se, ek Claudia-cleared approval aur ek aapka khud cleared approval company
ke records mein same lagein, aur sirf uski signed ledger line unhe alag karti ho (uska naam, uski
reasoning). Aur aapke chat app par ek-screen weekly summary ho.

<details>
<summary>Company kyun farq nahi bata sakti, aur yeh theek kyun hai</summary>

Company ke approval routes board-level par governed hain. Chahe aap khud dashboard mein approve click
karo ya Claudia apni board-scoped credential se signed decision post kare, company wahi tarah ka log
row likhti hai: board ne act kiya. Company natively "AI delegate ne yeh kiya" record nahi karti. Yeh
koi gap nahi jo paper over karni ho; yehi wajah hai Claudia **apni** ledger rakhti hai. Uski ledger woh
ek jagah hai jahan owner-versus-delegate farq record hota hai, reasoning aur signature ke sath jo prove
karta hai decision uski thi aur untampered thi. Dono records 2 alag stores mein hote hain, shared
approval par match hote hain.
</details>

<details>
<summary>Weekly summary kaisi dikhti hai</summary>

Aap ledger row-by-row nahi parhte. Claudia ek hafte ko digest mein badalti hai, roughly:

> **This week:** 142 decisions handled. 134 I cleared on my own (94%). 8 I surfaced to you. You
> overrode 1 of mine.
>
> **Your override:** a $1,847 refund to a customer with prior refunds. Your note: "should have
> surfaced, multiple priors." I have updated: for customers with two or more prior refunds in six
> months, I will surface regardless of amount.
>
> **Worth a glance:** two refunds I approved at lower confidence than usual; both involved patterns
> I have not seen often.

Yehi form aap actually consume karte ho: totals, exceptions, corrections, aur chand low-confidence
calls jinpar woh aapki nazar chahti hai.
</details>

> **Carry-forward:** Ab aap dekh sakte ho Claudia ne exactly kya kiya. Scenario 5 batata hai jab aap
> kisi cheez se disagree karo to kya karna hai.

---

## Scenario 5 — Usay Override Karo, Aur Seekhte Dekho (~8 min)

Der ya sawer Claudia koi aisi call karegi jo aap khud na karte. Aapka instinct hoga isay ek failure
samajhna. Yeh ulta hai.

> Disagreement malfunction nahi hai. Yeh signal hai jo exactly dikhata hai Claudia ki judgment kahan
> khatam hoti hai aur aapki kahan shuru. Aap call reverse karte ho, woh aapki **wajah** ko training ki
> tarah record karti hai, aur agli baar uska heartbeat isi shape ka case mile to woh usay surface
> karegi, clear nahi. Aap kabhi locked out nahi — override hamesha aapka hi hai, aur company hamesha
> aapki rehti hai.

**Coding agent ko paste karo:**
```text
Pick one of the refunds Claudia's loop auto-cleared this week and have me reverse it, the way I
would if I disagreed. Record my override and my reason against her original ledger row, and update
what she's learned so that the case becomes one she'll surface, not clear. Then prove it took: put a
similar refund into the queue and let her next heartbeat reach it, and show me she now surfaces that
one to me instead of clearing it. Last, tell me from this week's numbers whether her overall
behavior looks healthy.
```

**Done jab:** aapka override Claudia ki original ledger row par land kare, aapki wajah ke sath; baad
ke heartbeat par similar refund clear hone ki jagah surface ho, prove karte hue ke correction ek
standing change bani, one-off fix nahi; aur aap ek sentence mein healthy shape naam le sako: zyada
decisions khud, chota fraction surface, overrides itne rare ke har ek closely parha jaye.

<details>
<summary>Disagreement system ka failure nahi, kaam karna hai</summary>

3 wajah override achi nishani hai, buri nahi:

- **Koi learned pattern pehli baar mein sahi nahi hota.** Claudia ke inferred patterns approximations
  hain; ek fail hote dekhna hi pata chalta hai kahan galat hai.
- **Aapki judgment badalti hai.** Month 1 wale aap aur month 6 wale aap same operator nahi ho; market
  shift hoti hai, company grow hoti hai. Override signal hai ke aapki soch badli aur usay catch up
  karna hai.
- **Correction reasoning carry karta hai.** "Should have surfaced, this customer has priors" sirf
  reversal nahi — yeh ek rule hai jo woh baad ke similar-but-not-identical cases par apply kar sakti
  hai.
</details>

<details>
<summary>Shapes jo asal mein warning signs hain</summary>

Healthy steady state roughly: zyada decisions autonomous, chota fraction surface, overrides rare.
3 patterns worry karne layak hain:

- **Aap usay constantly override kar rahe ho** (~1/5 calls ya zyada): envelope bara hai ya patterns
  miscalibrated hain. Envelope tighten karo.
- **Aapne weekly summary parhna band kar diya:** aap chupke se rubber-stamping mein wapis chale gaye
  ho — yehi cheez yeh course rokna chahta hai.
- **Woh almost sab kuch aap tak surface karti hai:** woh zyada cautious hai, poora point (attention
  free karna) kho gaya. Envelope ya confidence threshold loosen karo.
</details>

> **Carry-forward:** Claudia ab ek trustworthy, self-correcting chief of staff hai. Ek sawal reh jata
> hai: agar aapka laptop, jispar woh chalti hai, kho jaye ya chori ho jaye to kya hoga?

---
[⬅ Ek Hafta Approvals](03-week-of-approvals.md) · [⬆ Index](README.md) · [Agla: Laptop Kho Jaye ➡](05-lose-laptop-and-carry-away.md)
