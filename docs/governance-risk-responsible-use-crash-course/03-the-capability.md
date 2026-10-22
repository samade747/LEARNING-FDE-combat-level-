# 03 — Question 3: The Capability — Kya Main Yeh On Kar Sakta Hoon?

Colleague tumhe public forum se ek **Skill** bhejta (saved instructions set jo AI ko ek task
tumhare tareeqe se sikhati) — meeting notes ko summaries mein badalti. Achhi chali hai unke liye,
aur uski instructions meeting-notes tak limited nahi hain. Enable, escalate, ya decline karo?
Decide karo pehle.

AI systems ab text generate karne se zyada karte — Skills/tools/plugins/connectors/web pages/
files/code/browsers/email/calendars use kar sakte. **Sawal ab "model trust karta hoon?" nahi —
"main is session/agent ko kitni authority add kar raha hoon?" hai.**

## 3.1 — Extensions Ko Software Ki Tarah Treat Karo, Prompts Ki Tarah Nahi

Skill mein instructions/scripts/resources/dependencies ho sakte. Connector doosri system mein
data/actions expose kar sakta. Description ki friendliness se, ya colleague ne share ki isse
judge mat karo.

**Skill apni permission list nahi rakhti.** Connector ke scopes hote jo tum grant+narrow kar
sakte. Skill ka koi dial nahi — jo bhi session already reach kar sakti usi se chalti hai, sirf
task ko jo chahiye usse nahi. Skill ki definition mein tools ki list ho to **pre-approve** karti
(bina prompt kiye chalein) — **widen karti kya hota hai, narrow nahi karti Skill kya touch kar
sakti.**

**5 checks chalao:**

1. **Source:** kisne banaya/publish kiya?
2. **Reach:** kaunsa data/files/systems/tools/credentials touch kar sakti jahan chalti?
3. **Fit** (appropriateness bhi bolte): kya reach job ke proportionate hai?
4. **Outside content:** web pages/incoming email/customer files/tumne-na-likha content parhegi?
5. **Actions:** send/pay/delete/publish/edit/approve, ya aur hard-to-reverse change kar sakti?

Pehli 3 batati capability workflow mein belong karti ya nahi. Last 2 batati mistake/hostile
instruction kitni dangerous ban sakti.

**2nd check answer karne ke liye package kholo** — files parhna hi tareeqa hai jaanne ka kya
karti hai, kya claim karti nahi. Warning sign: **scope creep** — formatting Skill ki instructions
formatting se bohot zyada jati ho to kuch bata rahi hain jo summary line nahi bataata.

> **"Internal" vetted nahi matlab.** Sabse hard source case anonymous forum download nahi hai —
> **apni hi company ki doosri team ki Skill** hai, kyunke "internal" vetted feel karti bina vetted
> hue. Unhone apni convenience ke liye broad reach grant ki ho sakti, ya purani policy ke against
> bani ho, ya tumse kam-sensitive data ke liye design ki ho. Enable karne se pehle publisher se
> confirm karo kya access karti aur kyun.

## 3.2 — 3 Outcomes

Har capability decision **3 outcomes** mein se ek mein khatam hota:

- **Enable** — source pata, reach proportionate, task fit, actions controlled
- **Escalate** — useful ho sakti, par kuch important unsettled hai (source unclear, reach broad,
  tool zaroorat-se-zyada access chahti, security sawal role se bahar hai)
- **Decline** — clearly disproportionate, untrustworthy, ya job ke liye zaroori nahi

**Escalating careful-rehne-ki-permission nahi maangna hai.** Achhi escalation unresolved sawal
naam karti: _"Yeh tool useful hai, par shared drive write access maangti jabke workflow sirf read
chahta. Security review kar sakta kya access narrow ho sakti?"_ — "Can I use this?" se bohot
behtar.

## 3.3 — Trusted Tool, Untrusted Content

Capability trusted publisher se aa sakti aur phir bhi aisi content parh sakti jo kisi untrusted
ne likhi. Email/web page/customer upload/shared document mein instructions ho sakti jo model ko
steer karne ki koshish karein — **prompt injection** family of attacks.

> **Key point: tool kisne likha aur content kisne likha — 2 alag trust sawal hain.**

Risk sharply badhti jab AI workflow **untrusted content parhti AND consequential actions le
sakti** dono.

**Ordinary knowledge work ke liye useful default:**
- AI ko sirf wahi parhne do jo chahiye
- **read-only** access prefer karo jab kaafi ho (AI dekh sakta, change nahi)
- send/publish/pay/delete/approve/irreversible-edits ko defined human gate ke peeche rakho jab
  tak workflow ne zyada autonomy earn na ki ho

> **Agent builders ke liye:** system level par reach architecture ban jati — scoped credentials,
> tool allow-lists, typed actions, confirmation policies, network restrictions, isolation, audit
> logs, reading-content aur executing-actions ka clear split. Governing principle: **least
> privilege** — narrowest authority do jo job khatam kare, job change hone par revisit karo.

<details>
<summary>Going deeper: scanning helps, approval nahi hai</summary>

Security scanning kuch malicious Skills/plugins catch karti — yeh establish nahi karti capability
tumhari data/environment/use ke liye appropriate hai. Anthropic ka current Enterprise
documentation skill/plugin scanning ko certain new uploads/edits par malicious-content beta check
describe karta — pass hona "every respect mein safe" ka guarantee nahi. Scanner pass hone ke baad
bhi source/reach/fit review rakho.
</details>

## Worked Examples

- Trusted publisher ki document-formatting Skill → **Enable** approved environment mein
- Unknown-source "analytics booster" broad instructions ke sath → **Escalate** specific concerns
  ke sath
- Read-only connector reporting database tak, approved route + limited access → **Enable**;
  "just in case" write access mat do
- Forum Skill (opening): publisher unknown, session jo bhi reach kar sakti usse chalegi, notes-
  summarize karne ke proportion se bohot zyada → **Escalate ya Decline**. Enable kar ke hafta watch
  karna risk samajhne se pehle access de deta.

## Now Do It — Record Ka Block 3

Har Skill/connector/integration/browser/code-tool/action ke liye: source+reach+fit; outside
content jo parhti; consequential actions jo le sakti; outcome (enable/escalate/decline).

```text
Read this package and tell me what it actually instructs the AI to do,
including anything beyond what it says it is for.

Point out any file, network, credential, tool, or external-service
access you can see. Explain what would become risky if the session it
runs in can reach sensitive data or take consequential actions.

Do not certify it as safe. Finish with one of three lines: obvious
concerns found, no obvious concerns found in this review, or not
enough information to say.
```
