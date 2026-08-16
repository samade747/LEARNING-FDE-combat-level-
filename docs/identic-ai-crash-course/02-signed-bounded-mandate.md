# 02 — Act 2 Setup + Scenario 2: Signed Bounded Mandate

## Act 2 Ka Setup — Company Khadi Karo, Heartbeat On Karo

Ab Claudia ko job milti hai. Aap Claudia ke through kaam nahi karte, har decision ke liye usay bulate
nahi. Aap company khadi karte ho, uske haath (skills) install karte ho, heartbeat wire karte ho, aur
**switch on** karte ho. Phir coding agent chala jata hai, aur aap ek delegate ko akele chalte dekhte ho.

Company pichle course se continue hoti hai: uska apna CEO hai aur ek self-expanding workforce jo apne
gaps spot karke aapko (board ko) hires propose karti hai. Claudia usay aapke delegate ki tarah oversee
karti hai; woh uski CEO nahi hai.

Yeh ek bara setup prompt hai jo 4 kaam ek sath karta hai: company khadi karta hai, Claudia ke 3 skills
install karta hai (sign, post, ledger likhna), aur **heartbeat start karta hai**. Woh dry-run mein
jagti hai abhi: real queue parhti hai aur log karti hai woh kya karti, kuch post nahi karti, kyunki
aapne abhi tak uski limit set nahi ki. Woh Scenario 2 mein set hoti hai.

**Coding agent ko paste karo:**
```text
Stand up my company, give Claudia her hands, and turn on her heartbeat. I'm the founder and owner
of the AI-native customer-support company from the last three courses... The company has its OWN
CEO plus four Workers (Tier-1 Support, Tier-2 Specialist, Manager-Agent, Legal Specialist)...
Install Claudia's chief-of-staff skills... Then start her heartbeat so she wakes on her own and
reads the queue, but keep her waking in dry-run for now...
```

**Done jab:** sandbox dashboard company dikhaye CEO + 4 Workers ke sath, Claudia ka heartbeat chal
raha ho (kam az kam ek baar khud jagi ho), aur uska dry-run log dikhaye woh kya karti — kuch post
kiye bina.

<details>
<summary>CEO kaun hai? (Aap, Claudia, aur company)</summary>

3 layers hain: **Aap** board ho (pichle course mein is CEO ko approve kiya). **Claudia** aapki
delegate hai, company ke upar ek separate layer, jo aapke routine board decisions clear karti hai aur
aapka intent CEO tak carry karti hai. **Company ka CEO** workforce ko roz chalata hai. Koi bhi ek
agent 2 seats nahi rakhta — yehi poora point hai.
</details>

> **Carry-forward:** Claudia ka heartbeat chal raha hai aur woh real queue parh rahi hai, lekin abhi
> act nahi kar sakti — uske paas na identity hai jo company accept kare, na koi agreed limit. Scenario
> 2 usay dono deta hai, aur uska agla wake real mein ek clear karta hai.

---

## Scenario 2 — Ek Signed, Bounded Mandate (~15 min)

Abhi Claudia **soch** sakti hai aapki tarah, lekin **act** nahi kar sakti. Yeh step usay ek real
approval clear karne deta hai, safely. Iske liye aap usay wohi 2 cheezein dete ho jo kisi trusted
employee ko dete: **ek signature jo sirf woh bana sake** (koi baad mein prove kar sake ke decision
genuinely uski thi), aur **ek spending limit** (clear, deliberately narrow cap jispar woh khud act
kar sake; usse bara kuch aap tak).

> **Poora idea: ek signature aur ek limit.** Yeh dono rails hain jinke andar uska loop chalta hai. Woh
> har baar decide nahi karti ke bounds mein rahe ya nahi — limit posting ke act mein hi wired hai,
> taake bounds ke bahar decision post ho hi na sake chahe woh try kare.

> **Ek rule yaad rakhne wala:** uski limit hamesha aapki apni authority se **narrower** ho sakti hai,
> kabhi wider nahi. Aap accidentally usay zyada power nahi de sakte — uska circle hamesha aapke andar
> baitha rehta hai.

**Pehla prompt — signature aur limit set karo, live hone se pehle review karo:**
```text
Set Claudia up to act for me, but show me everything before you switch it on. Give her a signature
only she holds. Set a deliberately conservative limit: she can approve refunds up to $2,000 and
budget overruns up to 20% on her own; anything bigger, plus every hire, firing, or policy change,
always comes to me. Show me that limit and her signature's fingerprint, and wait for my okay...
Never show me or save her secret key.
```

**Dusra prompt — loop ko ek clear karte dekho, aur limit ko refuse karte dekho:**
```text
Trigger one of Claudia's heartbeat wakes now so I can watch it live... Then, to prove the limit is
real, put a refund well over her ceiling into the queue and let her next wake reach it; show me her
loop refusing to post it and logging why...
```

**Done jab:** ek heartbeat wake par, bina kisi instruction ke, Claudia ek routine refund clear kare,
signed; ek over-limit refund uske loop se **refuse** ho, na post ho, refusal log ho; aap 3 cheezein
dekh sako: uski signature ki fingerprint (kabhi secret key nahi), uski conservative limit, aur cleared
decision **2 jagah** record hua ho — company ka apna log aur Claudia ki separate ledger (Scenario 4
mein "do kyun" ka jawab).

<details>
<summary>Signing plain lafzon mein</summary>

Claudia ek **private key** rakhti hai (secret, aapke disk par), company matching **public key**
rakhti hai. Jab woh decide karti hai, ek short signature banati hai decision ke exact bytes par.
Koi bhi public key se check kar sakta hai: yeh Claudia ki key se aya hai, aur signed hone ke baad ek
character bhi nahi badla. Standard tool (`ed25519`) ordinary libraries mein ship hota hai.
</details>

<details>
<summary>3 checks jo har post se pehle chalte hain</summary>

1. **Kya yeh waqai Claudia hai, aur kya woh abhi bhi trusted hai?** Registration exist kare, revoked
   na ho. Yeh pehle chalta hai taake forged requests expensive cryptography tak na pahunchein.
2. **Kya uski signature verify hoti hai?** Decision uski key se aya, tamper nahi hua.
3. **Kya yeh action uske envelope ke andar hai?** Amount aur type delegated range mein ho. Fail hone
   par bhi ledger row likhi jati hai — forged attempt bhi auditable honi chahiye.

**Counterintuitive part:** Company ke approval routes board-level par governed hain — sirf board-level
credential approve/reject drive kar sakti hai. Isliye Claudia jo credential use karti hai woh **board
credential hai, scoped down by aapki apni delegation layer** — yehi delegation ko delegation banata
hai. Yehi wajah hai Claudia company ka registered agent **nahi** hai: company-agent credential kuch
approve nahi kar sakti (routes reject karte), to usay register karna kuch nahi kamata. Ek hi Claudia
hai, company ke upar delegate, aur uski identity uski apni signature aur ledger hai.
</details>

<details>
<summary>"Approve" kya karta hai aur kya nahi karta</summary>

Approval karna ek **decision** record karta hai. Yeh khud se linked issue ko aage nahi le jata ya
kisi Worker ko act karne ke liye nahi jagata — woh ek alag, explicit step hai. Claudia ka kaam yahan
khatam hota hai: "decision record hua, ledger row likhi gayi." Yeh uska role clean rakhta hai: woh
decision govern karti hai, kaam mein chupke se dakhal nahi deti.
</details>

> **Carry-forward:** Claudia ka loop ab ek real approval clear karta hai apne aap, signed aur bounded,
> aur bounds ke bahar refuse karta hai. Scenario 3 volume ko ek realistic week tak barhata hai, aap
> kuch nahi karte, aur uske job ka baqi hissa add hota hai: intent neeche carry karna, aur har wake
> par ek-line brief wapis dena.

---
[⬅ Act 1](01-act1-she-thinks-like-you.md) · [⬆ Index](README.md) · [Agla: Ek Hafta Approvals ➡](03-week-of-approvals.md)
