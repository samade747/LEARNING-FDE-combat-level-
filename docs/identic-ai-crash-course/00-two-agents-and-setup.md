# 00 — Do Agents, Aur Woh Kabhi Overlap Nahi Karte

## Do Agents Jo Course Mein Ate Hain

Poore course mein sirf 2 agents hain, aur yeh **kabhi ek sath on nahi hote**:

- **Aapka coding agent** (Claude Code ya OpenCode) — **BUILD** karta hai. OpenClaw verify karta hai,
  Claudia ke files place karta hai, company khadi karta hai, aur **Claudia ka heartbeat on karta hai.**
  Yeh sirf setup hai. Uska aakhri kaam heartbeat start karna hai, phir woh chala jata hai.
- **Claudia** — hamesha ke liye **GOVERN** karti hai, akele. Uska heartbeat usay jagata hai, woh queue
  parhti hai, routine cheezein clear karti hai, baqi aapke chat app par bhejti hai, phir so jati hai.
  Koi usay per-decision invoke nahi karta. Setup ke baad sab kuch yehi hai.

Ek baar Claudia on ho jaye, uska loop yeh hai: **jago → queue parho → har item ke liye pucho "main
khud approve karti ya escalate karti?" → routine clear karo, sign karo, log karo → important cheezein
chat app par bhejo apni opinion ke sath → so jao.**

Chat window ke ulat (jo aap khulte ho jab sawal ho), Claudia apne clock par chalti hai aur pehle aapko
message karti hai jab kuch zaroori ho. Yehi ability — khud jagna aur khud reach out karna, sirf jawab
dena nahi — poori wajah hai ke woh aapki queue clear kar sakti hai jab aap so rahe ho. **Paperclip**
aapki company hai, jo Workers aur queue rakhti hai; yeh Act 2 tak tasveer mein nahi ati.

## Claudia Kaun Hai

Claudia ek personal AI hai, OpenClaw par chalti hai, aapki machine par. Woh **hai** kya: aapka twin,
ek AI jo aapko janti hai. Woh **karti** kya hai (Act 2 mein): aapki chief of staff, ek delegate jo
apne heartbeat par jagti hai aur bina puche aapki queue clear karti hai.

> **"Identic AI" kyun kehte hain:** "Chief of staff" job hai. Identic AI category hai — Don Tapscott
> ka term (*You to the Power of Two*, 2025) ek personal AI ke liye jo genuinely aapki ho. Tapscott
> 5 nishaniyan batata hai: **personal** (ek insan ke liye), aapki **values** reflect kare, aapka
> extension jaisi lage, **waqt ke sath yaad** rakhe, aur **self-sovereign** ho — aap owned aur
> controlled, kisi platform se rented nahi. Aakhri nishani sabse zaroori hai, aur sabse zyada chupke
> se surrender hoti hai. Trap cloud nahi hai; trap hai apni AI ko ek vendor se **managed service ki
> tarah rent** karna jo instance own karta hai. Claudia sabse saaf raasta leti hai: aapke apne hardware
> par chalti hai, aapke apne disk par files mein seekhti hai — isliye aapka accumulated judgment aapka
> hai, keep/backup/delete karne ke liye, kabhi kisi vendor ka read/revoke karne ka nahi. Scenario 6
> mein yehi ownership decide karti hai ke aap bache ya nahi.

## Build Rhythm

Coding agent ke sath kaam karne ka poora tareeqa 5 steps hai: **aap plain request paste karte ho, woh
plan propose karta hai, aap approve karte ho, woh execute karta hai, dono verify karte ho.** Aap kabhi
khud command type nahi karte. Yaad rakho: yeh rhythm sirf **setup** describe karta hai. Ek baar
Claudia ka loop on ho jaye, koi rhythm follow karne wali nahi — woh aapke bina chalti hai.

Starter download karo aur coding agent mein kholo. Starter ek **bare base** hai: iske sath ek
`AGENTS.md` brief hai jo coding agent ko sikhati hai OpenClaw verify karna, ready-made Claudia place
karna, local Paperclip sandbox khadi karna, decisions sign karna, governance ledger likhna, aur
Claudia ka heartbeat wire karke start karna.

```bash
# Unzip, phir Claude Code mein kholo:
cd identic-ai
git init
claude
```

`git init` OpenCode ke liye zaroori hai (uska undo feature isi par chalta hai), aur Claude Code ke
liye bhi strongly recommend hai — commits scenarios ke darmiyan progress save karte hain.

**Brief load hui confirm karo.** Coding agent ko yeh paste karo:

```text
What can you do for my OpenClaw chief of staff and, later, my Paperclip company?
```

Jawab mein specifics dikhne chahiye: OpenClaw verify karna, ready-made Claudia place karna, baad mein
local Paperclip sandbox khadi karna, decisions sign karna, governance ledger, conservative envelope,
aur heartbeat start karna. Agar generic AI baat lage, confirm karo ke aap `identic-ai/` folder ke andar
se khole hain.

> **Recovery move poore course ke liye:** kuch bhi gadbad ho to paste karo: "Something did not work.
> Read the most recent OpenClaw and Paperclip logs, tell me in plain language what you see, and
> propose a fix I can approve."
>
> **Agar koi scenario khinch jaye:** paste karo: "What is blocking us, in one sentence? Let's re-plan
> from there."

---
[⬆ Index](README.md) · [Agla: Act 1 ➡](01-act1-she-thinks-like-you.md)
