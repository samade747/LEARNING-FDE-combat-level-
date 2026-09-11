# 08 — Teaching Walkthrough (Roman Urdu, Domain-by-Domain)

*Yeh file un `05`/`06`/`07` se alag hai — woh test/cram-format hain, yeh **concept-teaching** format hai:
har domain ka plain Roman Urdu walkthrough (jaisa Zia Tutor AI padhata), phir scenario-based
brainstorming questions (MCQ nahi — open reasoning, taaki aap khud apni class ko sikha sakein).
Blueprint order mein chalta hai ([01-domain-blueprint.md](01-domain-blueprint.md) se grounded).
Answers khud likho, phir agla domain maango — is file mein reference-answers baad mein add hongi jab
aap apne jawab de dein.*

---

## Domain 1 — Prompting and Task Execution (14%)

CCAO-F ka pehla domain sabse chhota weight (14%) rakhta hai — is wajah se bhi ke yeh sabse "obvious"
skill hai: acha prompt likhna. Lekin exam yahan sirf yeh nahi dekhta ke aap fancy prompt likh sakte ho
— yeh dekhta hai ke aap **task ko sahi tarah decompose aur adapt** kar sakte ho.

Teen core ideas:

1. **Effective prompting** — ek achha business prompt teen cheezein deta hai jo Claude khud guess
   nahi kar sakta: **audience** (kaun parhega), **format** (kis shape mein chahiye), aur **goal** (kis
   decision ko feed karega). "Write something about our product" fail isliye hota hai kyunki teenon
   missing hain — lambi prompt ya persona add karne se bhi fix nahi hota jab tak yeh teen cheezein na
   aayein.

2. **Task decomposition** — jab ek request mein multiple parts hon (jaise quarterly review: budget +
   status + staffing + risks), to ek hi mega-prompt shallow output deta hai. Sahi approach: har part
   ko apna focused prompt do, phir combine karo. Yeh wahi principle hai jo harness-engineering mein
   "sub-tasks" ke roop mein aata hai — same logic, business-writing context mein.

3. **Adapting strategy by task type** — yeh sabse zyada test hota hai. **Divergent tasks**
   (brainstorming) mein loose constraints, zyada options chahiye. **Convergent tasks** (drafting,
   analysis) mein tight structure, format, tone chahiye. Ek associate jo dono ko same tarah prompt
   karta hai — woh galat hai, chahe prompt "acha" hi kyun na ho.

**Iteration** bhi isi domain ka hissa hai: pehla draft kabhi perfect nahi hota. Sahi move specific
feedback dena hai ("zyada casual karo, request ko pehle paragraph mein lao"), poora naya prompt likhna
ya manually rewrite karna nahi.

### Scenario Brainstorming — Domain 1

1. Ek HR associate Claude se poochta hai: "policy document ka summary do." Output generic aur kaam
   ka nahi. **Aap iss associate ko kya 3 sawal poochne ko kahoge taaki woh apna prompt improve kare?**

2. Ek marketing lead ek hi din mein Claude se do kaam leta hai: (a) 20 naye taglines brainstorm
   karna, (b) final launch email draft karna. **Dono ke liye prompting strategy mein kya farq hoga —
   specifically kaunsi cheez "loose" rakhoge aur kaunsi "tight"?**

3. Ek associate complain karta hai ke "Claude ka pehla draft hamesha ghalat hota hai, mujhe har baar
   poora naya prompt likhna padta hai." **Yeh unka misconception kahan hai, aur aap unhe iteration ka
   sahi tareeka kaise sikhaoge — ek concrete example ke sath?**

*(Aapke jawab: abhi pending — likh kar bhejo, phir yahan reference answers add hongi.)*

---

## Domain 2 — Output Evaluation and Validation (21%)

CCAO-F ka **sab se bara domain**. Thesis yehi hai: asal skill answer *lena* nahi, answer **check**
karna hai — pehle woh CCAO-F pass karne ke tumhare apne goal ke liye bhi sab se zyada marks yehi domain
deta hai, isliye yahan sab se zyada waqt lagana literally sab se acha ROI hai.

Teen core ideas:

1. **"Prove it on work you already know"** — naye data par trust karne se pehle, ek purana case do
   jiska sahi jawab tumhe pehle se pata hai. Assistant se woh reproduce karwao, phir compare karo. Teen
   outcomes hain — sab useful: (a) match ho gaya → similar future work ke liye *earned* confidence,
   (b) kuch miss hua → instruction improve karo, (c) ek hissa reliably nahi ho raha → wo hissa human ke
   paas rehta hai. Pass hona future har case ka guarantee nahi deta, aur accountability transfer nahi
   karta — result check karna, stand behind karna, disclose karna phir bhi tumhara kaam hai.

2. **Independent verification** — jis agent/model ne output banaya, wohi uska sab se kamzor verifier
   hai, kyunki usi ke blind spots output mein bhi hain aur review mein bhi honge. Verification ko ek
   **independent path** chahiye: khud padhna, ek doosra model, ek test, ya ek hard constraint (database
   rule). Same source se dobara "yeh sahi hai?" poochna verification nahi hai.

3. **Cross-model checking (jab stakes high hon)** — single model se rubric ke against self-score
   maango ("clarity/accuracy/structure/missing — 1-10 each, ek line justification"), phir apne
   suggestions khud apply karwao (grade ~9 tak). High-stakes work ke liye doosri **model family**
   (Claude vs ChatGPT vs Gemini) se same rubric pe check karwao — alag training data, alag blind spots;
   unka disagreement wahi signal hai jo ek model akela nahi de sakta. Caveat: teenon model same cheez
   pe wrong ho sakte hain — legal/medical/financial/real-person claims ke liye yeh score ek progress
   signal hai, truth signal nahi; human expert hi final check hai.

### Scenario Brainstorming — Domain 2

1. Ek HR associate Claude se employee-complaint summary banwata hai aur "yeh theek lagta hai" keh kar
   bhej deta hai. **Kaunsi cheez missing hai jo isay real evaluation banati?**
2. Ek finance analyst Claude se quarterly variance report banwata hai — high-stakes, board ko jayega.
   **Kya loop chalaoge — single-model self-critique kaafi hai ya cross-model bhi zaroori? Kyun?**
3. Ek associate kehta hai "Claude ne khud kaha yeh accurate hai, to maine trust kar liya." **Yahan
   reasoning mein galti kahan hai?**

*(Aapke jawab: likh kar bhejo, phir reference answers add hongi.)*

---

## Domain 3 — Product and Model Selection (12%)

Yeh domain teen naam yaad karne ka nahi — ek **decision pattern** ka hai jo names badalne ke bawajood
zinda rehta hai (khud guide bhi warn karti hai: model names rotate, pattern nahi).

1. **Model tier pattern** — har vendor apne models ko usi 3-level trade-off pe arrange karta hai:
   **fast default** (roz-marra kaam, sasta/tez), **thinking mode** (multi-step reasoning, tricky
   analysis — dheema, careful), **heavy flagship** (sab se mushkil kaam, sab se mehenga/dheema). Claude
   pe: Haiku (fast), Sonnet (fast-tier ka everyday), Opus (flagship); thinking ek alag switch hai,
   model name nahi. **Model ko task se choose karo, habit se nahi.**

2. **Default middle, escalate for depth, drop for bulk** — zyada tasks middle-tier model handle kar
   leta hai. Upar jao jab task ko ek bara, complex structure ek sath coherent rakhna ho (lambi document
   analysis, hard architecture). Neeche jao high-volume low-depth kaam ke liye (bulk reformatting,
   quick classification at scale). Mehenga model routine email pe kharch karna utni hi badi galti hai
   jitni sasta model hard analysis pe.

3. **Context/session judgment** — jab conversation lamba ho jaye aur quality girne lage, sawal "model
   badlo" nahi hai, balke: **restart** karo (fresh session), **summarize** karo (progressive
   disclosure), ya **persist** karo (Project mein daal do taake dobara explain na karna pare)? Sahi
   choice task ki nature pe depend karti hai — ek hi jawab sab jagah fit nahi hota.

### Scenario Brainstorming — Domain 3

1. Ek marketing associate roz 50 chhoti product descriptions Opus (flagship) pe generate karta hai,
   "best quality chahiye" keh kar. **Yeh decision kahan galat hai, aur sahi tier kya hoga?**
2. Ek analyst ek 3-ghante-lambi conversation mein Claude se coding help le raha hai, aur output quality
   girne lagi hai. **Model badlein ya kuch aur? Pehle kya poochoge?**
3. Ek consultant client ko "hum hamesha sab se flagship model use karte hain" keh kar impress karna
   chahta hai. **Yeh statement CCAO-F ki judgment ke hisaab se kyun weak hai?**

*(Aapke jawab: likh kar bhejo, phir reference answers add hongi.)*

---

## Domain 4 — Workflow Integration and Solution Design (16%)

Teesra sab se bara domain — yahan test hota hai ke AI ko ek **existing workflow** ke andar sahi jagah
pe fit kar sakte ho, aur uska result stakeholders ko sahi tarah explain kar sakte ho.

1. **Task definition se shuru karo, tool se nahi** — "hume behtar reporting chahiye" ek requirement
   nahi hai, ek vague wish hai. Har request ko 5 settled answers mein todo: **kya produce hoga, kiske
   liye, kitni baar, kis data se, kis format mein**. Jo answer nahi pata, wo ek clarifying question hai
   jo kisi se poochni hai — model se guess nahi karwani, kyunki model missing slots ko khud "likely-
   looking default" se bhar dega.

2. **Delegation map — 3 criteria har step ka ownership decide karte hain**: **reversibility** (galti
   undo ho sakti hai?), **stakes** (worst-case cost kya hai?), **accountability** (jawabdeh kaun hai —
   aur kya wo insaan sach mein review kar sakta hai?). In teeno se har step **AI-appropriate**,
   **human-retained**, ya **collaborative** (AI banata hai, ek named insaan judge karta hai) ban jata
   hai.

3. **Value + limits ko sahi tarah communicate karo** — "fully automated", "AI handles X", "utna hi
   acha jitna insaan" — teenon overstate karte hain aur pehli visible galti pe trust tod dete hain.
   Sahi move: **pehle bataao tool kya karta hai, phir human checkpoint ka naam lo** — ek extra sentence,
   lekin defendable claim. Audience ke hisaab se detail badlo (technical lead ko mechanism, executive
   ko outcome, risk team ko sirf control) — lekin **gate kabhi mat chhupao**; stakeholders AI workflow
   pe zyada trust karte hain jab human checkpoint explicit ho, kam nahi.

### Scenario Brainstorming — Domain 4

1. Ek operations lead sirf itna kehta hai: "Claude se hamara onboarding process automate karwa do."
   **Pehle kaunse 5 sawal poochoge, task definition banane ke liye?**
2. Ek 6-step approval workflow hai. **Kis step ko "collaborative" banaoge bajaye "AI-appropriate" ke —
   aur kaunsa criterion (reversibility/stakes/accountability) yeh decide karta hai?**
3. Ek team lead client ko batata hai "yeh system fully automated hai." **Isay teen alag audiences
   (technical, executive, risk) ke liye kaise rewrite karoge — bina gate chhupaye?**

*(Aapke jawab: likh kar bhejo, phir reference answers add hongi.)*

---

## Domain 5 — Configuration and Knowledge Management (12%)

Yeh domain ek hi mechanism ko char naamon mein dekhta hai — sab **context window mein sahi waqt pe
sahi text daalne** ka control hain.

1. **Char features, ek mechanism** — **account instructions** (har window mein jaata hai — isliye
   sirf wahi likho jo *har* conversation mein sach ho, topic-specific cheez Project mein daalo);
   **Project** (pehle se loaded window — usi ek kaam ke liye instructions + knowledge files, always on
   jab tak us project mein ho); **memory** (self-updating note jo Claude periodically banata hai — tum
   control karte ho kya yaad rahe/bhoola jaye, incognito toggle isay skip karta hai); **chat
   history/search** (retrieval — pichle transcripts se relevant thread khींch kar current window mein
   laana).

2. **Connectors** — connect karna ~1 minute ka kaam hai, lekin connect karne ke baad har conversation
   mein alag se **enable** karna padta hai (yeh sab se common mistake hai). 10+ connectors ho to
   load-on-demand chuno. **Regulated data** (healthcare, legal, student records) pe kabhi pehle
   synthetic/invented data se practice karo, phir hi approved real accounts use karo.

3. **Skill vs Connector vs Project vs Custom Instructions — ek-line test har ek ka**: Skill = "main
   baar baar *kaise* karna hai explain kar raha hoon" (on-demand); Connector = "main kisi doosri app se
   copy-paste kar raha hoon" (access); Project = "yehi files/rules *har* cheez pe apply hoti hain
   *yahan*" (scoped, always-on); Custom instructions = "main chahta hoon yeh *hamesha, har jagah* sach
   ho" (global). Skill ko Project se confuse mat karo — Project hamesha on hai apne workspace mein,
   Skill sirf tab jagta hai jab request match kare.

### Scenario Brainstorming — Domain 5

1. Ek associate apni account instructions mein likhta hai: "hamesha Markdown table mein jawab do."
   **Yeh kyun galat scope hai, aur is instruction ko kahan hona chahiye?**
2. Ek teacher har course ke liye alag Project banata hai (syllabus + rubric + samples), lekin phir bhi
   har chat mein instructions repeat karta hai. **Kya missing hai unke setup mein?**
3. Ek consultant Gmail connector 3 hafte pehle connect kar chuka hai, lekin aaj ki chat unka inbox
   nahi dekh pa rahi. **Sab se pehla sawal kya poochoge?**

*(Aapke jawab: likh kar bhejo, phir reference answers add hongi.)*

---

## Domain 6 — Governance, Risk, and Responsible Use (15%)

Doosra sab se bara domain — is book ka apna governance framework **4 sawal** ka hai, har ek ke 3
jawab, aur **beecha wala jawab hi asal professional judgment** hai.

1. **4 sawal, har ek ke 3 jawab**: **The Case** (kya AI yeh kaam kar sakta hai? — fully appropriate /
   appropriate with review / inappropriate), **The Data** (kya yeh info andar ja sakti hai? — green /
   check first / red), **The Capability** (kya main yeh tool/skill/connector on kar sakta hoon? —
   enable / escalate / decline), **The People** (kya yeh kisi ko unfairly affect kar sakta hai ya
   disclosure chahiye? — decide & document / disclose / escalate). Outer do columns kuch commit nahi
   karte — **beecha wala column tumhe kuch specific naam lene par majboor karta hai** (ek reviewer, ek
   control, ek route, ek disclosure).

2. **The Case ke 4 screens**: **reversibility** (galti pakad kar undo ho sakti hai?), **consequence
   of error** (trivial/expensive/harmful/regulated/irreversible?), **human judgment/empathy** (kya yeh
   kaam relationship/care maangta hai jo insaan ko khud rakhni chahiye?), **accountability** (jawabdeh
   kaun hai, aur kya wo sach mein review kar sakta hai?). In charon se ek **"deciding factor"** nikalta
   hai — wo ek screen jo asal mein classification carry kar rahi hai ("yeh appropriate-with-review hai
   kyunki company customer ke paise ke fact ke liye accountable rehti hai" — is tarah ka sentence
   check/challenge ho sakta hai).

3. **"Koi review karega" ek gate nahi hai** — asal **defined gate** teen cheezein naam leta hai:
   **WHO** review karta hai (jo role sach mein responsible hai), **WHAT** woh verify karta hai (specific
   risk jo review pakadne ke liye hai), **WHEN** (isse pehle ke output undo karna mushkil ho jaye).
   "Hum human-in-the-loop rakhenge" ek *intention* hai, gate nahi. **Accountability kabhi tool par
   transfer nahi hoti** — manager, clinician, lawyer utne hi responsible rehte hain chahe AI ne draft
   ka hissa likha ho.

### Scenario Brainstorming — Domain 6

1. Ek project manager director ke sawal ka jawab dene se pehle customer spreadsheet (naam + account
   numbers) AI chat mein paste kar deta hai. **Kaunsa sawal (Case/Data/Capability/People) yahan sab se
   pehle poochna chahiye tha, aur kya jawab hota?**
2. Ek hiring team AI se applications summarize karwata hai "reading organize karne ke liye." **Yeh
   "appropriate with review" kyun hai, aur gate mein WHO/WHAT/WHEN kya honge?**
3. Ek manager kehta hai "AI ne yeh draft banaya, isliye final mistake AI ki hai." **Yeh statement
   governance ke hisaab se kyun galat hai?**

*(Aapke jawab: likh kar bhejo, phir reference answers add hongi.)*

---

## Domain 7 — Troubleshooting and Optimization (10%)

Sab se chhota domain (10%), lekin exam ka apna message clear hai: **fix karne se pehle diagnose karo —
model badalna pehla instinct nahi hona chahiye.**

1. **5 possible diagnoses, ek waqt mein ek sawal** — jab output disappoint kare, seedha fix suggest
   mat karo. Poocho: kya yeh **under-specification** hai (task clearly define nahi hui), **context
   overload** (conversation bohat lambi ho gayi), **wrong feature ya model** (galat tool choose hua),
   **stale configuration** (purani instructions/knowledge outdated ho chuki), ya **task jo fit hi nahi
   karta** (yeh kaam AI ke liye tha hi nahi)? Diagnosis se pehle fix suggest karna sab se common mistake
   hai — aur zyada tar waqt jawab "under-specification" nikalta hai, "galat model" nahi (jo pehla
   instinct hota hai).

2. **Symptom → concept mapping ek trained habit hai** — "har hafte same instructions type kar raha
   hoon" → isay Skill/Project bana do; "ek ghante baad quality gir rahi hai" → context bohat lamba ho
   gaya, naya session/summarize karo; "simple kaam par bill zyada aa raha hai" → galat model tier use ho
   raha hai (Domain 3 se link); "yaad nahi rakhta rules" → instructions file missing ya bohat lambi
   hai. Symptom se seedha concept tak pohochna practice se aata hai, memorizing se nahi.

3. **Optimize karna = feedback se adjust karna, poora restart nahi** — jaisa Domain 1 mein iteration
   tha (specific feedback, na ke naya prompt), workflow-level pe bhi yehi: ek chhota, specific change
   try karo, dekho kya sudhar hota hai, phir agla. Efficiency ke liye optimize karte waqt bhi
   **check/verification step kabhi mat hatao** — tez lekin galat, slow lekin sahi se zyada mehenga hai.

### Scenario Brainstorming — Domain 7

1. Ek associate complain karta hai "Claude ka output aaj kal kharab aa raha hai, pehle acha tha." **Fix
   suggest karne se pehle, unse kaunse 3 diagnostic sawal poochoge?**
2. Ek team har naye project ke liye Opus (flagship) use karti hai kyunki "last time kaam ho gaya tha."
   **Yeh troubleshooting/optimization ki nazar se kahan galat hai?**
3. Ek analyst ka weekly report prompt 2 mahine se same hai, lekin output quality gir rahi hai. **Kya
   check karoge — prompt badlo ge, ya kuch aur?**

*(Aapke jawab: likh kar bhejo, phir reference answers add hongi.)*

---
[⬅ CCAO-F Index](README.md) · [01 — Domain Blueprint](01-domain-blueprint.md)
