# 02 — Part 2: The Delegation Map (Concepts 5-8)

Har step 3 decisions leta, aur in-mixing hi map ko reasonable-dikhne-wala-par-galat banati:

1. **Eligibility — kya AI yeh touch bhi kar sakta?** 2 gates: data gate (yeh data tool mein jaa
   sakta?) aur input gate (step ko chahiye sab supply ho sakta — window test). Koi bhi "nahi" sawal
   khatam kar deta, step kitna bhi mechanical dikhe.
2. **Ownership — step kiska hai?** 3 criteria decide karte (Concepts 5-7).
3. **Implementation — kya carry karta?** Sabse akhir mein decide hota, sirf jo steps pehli 2 cross
   kar gaye:

| Step Kya Hai | Kya Carry Karta | Kyun |
|---|---|---|
| Fixed-steps repeatable procedure | Skill | Sabke liye same tareeqe se chalti |
| Rules/reference jo step ko hamesha chahiye | Project knowledge | Bina paste kiye har run available |
| Output jis par calculation depend karti | Code execution | Compute hui, generate nahi |
| Har output par standing constraint | Standing instruction | Bina kisi ko yaad rakhe apply hoti |
| Insaan ka step | Named review gate | Insaan, moment, aur checked cheez |

**3rd decision ko 2nd se door rakho.** "Yeh compute hona chahiye" sahi hai, par Implementation
column mein jata — AI ko step dene ka reason nahi, aur isay reason banana hi high-stakes
calculation ko unreviewed chhod deta.

Last row teams skim karte: step jo person ke pass rakha, "human" likh dene se khatam nahi hota —
ek **named person, named moment, named checked cheez** chahiye. "Ek insaan dekhta hai" hi wajah hai
Concept 7 ka gate unstaffed ho jata.

## Concept 5 — 3 Criteria Har Step Decide Karte

Workflow steps order mein likho. Har ek classify karo: **AI-appropriate** (AI own kar sakta),
**human-retained** (person outright owns), ya **collaborative** (AI produces, named person
judges).

Ownership sirf in **3 criteria** se decide hoti:

- **Reversibility** — undo ho sakta AI galat kare to? Draft rewrite ho sakti; sent email nahi.
  Undo-ho-sakne-wale steps delegation tolerate karte — error ka cost redo hai, error nahi.
- **Stakes** — mistake kya cost karti **bad case mein** (average mein nahi)? Misfiled label ek
  minute cost karta. Galat penalty figure jo bhi penalty hai cost karta.
- **Accountability** — iska outcome kiske upar hai? Har step ke liye koi jawabdeh hota, isliye sirf
  yeh sawal har step human rakh deta. Sharper sawal: **kya yeh step wo call hai jiske liye wo
  jawabdeh hai, ya input jise wo judge karta kuch act karne se pehle?** Jo step ek input produce
  karta jise koi judge karta, handover ho sakta — accountability judging par rehti. Jo step khud
  decision hai, nahi ho sakta — kuch bhi uske baad usay carry karne ko nahi bacha. **Accountability
  kabhi machine par move nahi hoti, kyunke machine se pucha nahi ja sakta.**

> AI ne is step par test run mein kaisa kiya — yeh criterion **nahi** hai. Concept 7 batata kyun.

**Yeh 3 sawal hain, score nahi.** Add nahi kar rahe, 3 "yes" ka wait nahi. Usually ek criterion
decide karta, baqi 2 agree karte — **wohi naam do**. Jahan 3 disagree karein, **strictest jeet
jaata** — undo ho sakta, kam cost karta, par phir bhi koi decision hai jiske liye koi jawabdeh hai
— human rehta.

> 4-criterion version bhi milegi (+ kya human creativity/empathy chahiye) — wo alag sawal answer
> karti (kya poora use case AI ke sath hona chahiye, Eligibility ke qareeb). Ownership decide
> karne ke liye, 3 hi rehte.

## Concept 6 — 2 Workflows, Same Criteria, Alag Answers

**Contract Review:**

| Step | Owner | Criterion | Carried By |
|---|---|---|---|
| Clauses extract karna | AI | Reversible, low stakes | Skill |
| Playbook departures flag karna | AI | Reversible, errors redline par surface | Skill |
| Redline+rationale draft karna | Collaborative | High stakes, human har edit judge karta | Skill+gate |
| Penalty clause ka financial exposure compute karna | AI | Reversible, approval gate par checked | Code execution |
| Har change approve/reject karna | Human | Yeh wo decision hai jiske liye jawabdeh hai | Named reviewer |
| Sign aur send karna | Human | Irreversible, externally binding | Named signer |

**Penalty-exposure row galat samjhi jati:** arithmetic hona step ko low-stakes nahi banata — figure
approval decision ko feed karta. Safe banata jo cheez: result undo ho sakta aur agli hi row mein
human ke saamne jata. Wo gate hata do, step AI-appropriate rehna band ho jata, arithmetic change
na ho tab bhi.

**Playbook row galat copy hoti:** flagging AI-appropriate hai kyunke koi agli row mein flags
parhta — galat flag galat redline ki tarah dikhta. Same step kisi workflow mein daalo jahan koi
baad mein flags nahi parhta, wo collaborative ban jata (jaisa expense-vs-travel-policy check).
**Step change nahi hua — kya koi uske baad khara hai, wo change hua.**

**Onboarding Documents** (same pattern, unrelated field):

| Step | Owner | Criterion | Carried By |
|---|---|---|---|
| HR export se new-hire details pull karna | AI | Reversible, confirmation step par checked | Code execution |
| Approved template se offer letter draft | AI | Reversible draft, send hone tak low stakes | Skill |
| Welcome note personalize karna | Collaborative | Manager ki voice supply nahi ho sakti | Named reviewer |
| Compensation approved req se match confirm karna | Human | Yeh check hai, uske baad kuch nahi | Named reviewer |
| Signed offer send karna | Human | Irreversible, externally binding | Named signer |

## Concept 7 — Map Galat Hone Ke 3 Tareeqe

Team 2 careless nahi thi — hafton tak AI ko redlines achhe se draft karte dekha, phir easy clauses
approve karne di. Reasonable response evidence ke against, aur sabse common tareeqa workflow ek
risk pick karti bina kisi ne choose kiye.

**Over-delegation** = AI ko step ke risk se zyada dena — reward se hota hai. Drafting achhi rehti
hafta-dar-hafta, agla step safe feel karta. Agla step nahi hai — **alag kisam ka step hai.**

> **Drafting quality draft ke baare mein evidence hai. Decision ke baare mein nahi.**

**Halo delegation** = step AI ko dena kyunke pehla step achha gaya. Competence real thi — sirf
alag step ki thi.

**Unstaffed gate** = collaborative step jiski review ab really nahi ho rahi. Reviewer busy ho,
queue lambi ho, drafts 2 mahine se achhi hon — review ek glance ban jati, phir click. **Kuch
decide nahi hua, koi ne map change nahi kiya, par step ab automated hai.** Map nahi batati, kyunke
map wo record karti jo tumne design kiya, jo chal raha wo nahi.

**Mapping the tool instead of the work** = team features ke around map karti jo pasand hain. Achhi
Skill bana li, workflow ek step gain karti us Skill ki shape ki — **teeno mein sabse dekhna hard
hai**, kyunke workflow genuinely tool achhe se use karti — sirf wo kaam nahi hai.

**Worked example — customer complaint workflow:**

| Step | Owner | Stated Reason |
|---|---|---|
| Complaint+history pull karna | AI | Mechanical retrieval |
| Issue template mein summarize | AI | Summarising Skill bohot achhi hai |
| Severity classify (low/med/high) | AI | 3 mahine se summaries accurate hain |
| Customer response draft | Collaborative | AI drafts, duty agent review karta |
| Response send karna | AI | Sirf low severity, drafts strong rahi |
| CRM mein outcome log karna | AI | Mechanical write |

<details>
<summary>Diagnosis</summary>

**Row 3 halo delegation hai.** Stated reason _summaries_ accurate hain — severity classification
alag step hai, decide karta customer escalate ho ya ignore. Missed high-severity complaint ek
hafte baad reclassify karne se recover nahi hoti.

**Row 5 over-delegation hai, row 4 wahan se aayi.** "Low severity only" control jaisi lagti, par
severity row 3 ne set ki — usi system se jo ab bina review send kar rahi. Step khud ko gate-skip
karne ki permission nahi de sakta. Sending undo bhi nahi ho sakti.

**Row 2 mapping-the-tool hai.** Reason yeh ki Skill achhi hai, step ko is tareeqe se karna zaroori
hai isliye nahi.

**Row 4 ko watch karo, fix nahi.** Jaisa likha sahi hai. Par duty agent har draft review karta,
including jo row 5 ab bina unke bhejegi — kisi ne nahi bataya per-shift kitne drafts hain.

Har stated reason **true** hai. Skill genuinely achhi hai, summaries genuinely accurate thi. **Bad
maps true statements se banti hain, galat step ke baare mein.**
</details>

**Check karne ka order:** kaam map karo bina tools zehan mein rakhe, har step khud se classify
karo, phir har collaborative step ke liye pucho kaun review kar raha aur kab. **Yeh sawal regularly
pucho: kya maine design kiye gates abhi bhi staffed hain?**

## Concept 8 — Map Kiska Hai, Kab Dobara Parha Jata

**Delegation map** = workflow step-by-step likhi hui, har step ka owner+stated reason ke sath. Ek
baar likhi jati, phir slowly galat ho jati — kisi ne change nahi ki, workflow uske neeche move hui.
Step add hua, reviewer role change hua, volume double hui, gate jo 20 cases/week par chalta 50 par
nahi chalta.

3 controls isi tarah decay hote: review gate (glances ban jati, phir clicks), standing instruction
(output slowly rule miss karta), map khud (workflow describe karti jo koi nahi chalata) — **har ek
ka signal "None" hai jab fail hoti.**

Ek jawab: **scheduled read** — map ki review fixed date par.

Map ko 2 cheezein chahiye jo zyadatar maps ke pas nahi: **owner** (ek named person, team nahi —
kaam nahi karta, par jawabdeh hai map reality describe kar rahi ya nahi) aur **review date**
(quarterly reasonable default, pehle agar volume/staffing/legal position change ho).

**Review ke 4 sawal (~20 min):**

1. Koi step add/remove hua jo map par nahi hai?
2. Har collaborative step ke liye: pichle hafte kaun ne review kiya, kitna time diya? Koi answer
   na de to step automated hai, map galat.
3. Volume/stakes change hui? Purane numbers ka gate naye numbers par fail hota.
4. Har configuration jo map depend karta abhi bhi current hai?

**Sawal 2 real problems dhoondta** — "last week" poochta hai, policy nahi (policy wo hai jo map
already bolti; last week jo actually hua).
