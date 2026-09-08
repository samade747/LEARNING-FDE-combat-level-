# CCAO-F — 100-Question Scenario Quiz (Complexity 10/10)

*Yeh sabse mushkil practice set hai is folder mein. Har question ek scenario hai, 4 options, aur har
option **plausible** hai — "sahi vs faltu" nahi, "achha vs sabse behtar" choose karna hai (jaise real
exam). Kuch questions **multiple-response** hain (select TWO) — clearly marked.*

**Distribution (official blueprint weights × 100):**

| Domain | Weight | Questions |
| --- | --- | --- |
| 1 — Prompting and Task Execution | 14% | Q1–Q14 |
| 2 — Output Evaluation and Validation | 21% | Q15–Q35 |
| 3 — Product and Model Selection | 12% | Q36–Q47 |
| 4 — Workflow Integration and Solution Design | 16% | Q48–Q63 |
| 5 — Configuration and Knowledge Management | 12% | Q64–Q75 |
| 6 — Governance, Risk, and Responsible Use | 15% | Q76–Q90 |
| 7 — Troubleshooting and Optimization | 10% | Q91–Q100 |

**Kaise use karo:** ek domain cold attempt karo (koi jawab na dekho), phir answer + rationale check
karo. Timing target: 100 Q in ~150 min. Har domain 75%+ chahiye.

**Grounding:** official exam-guide blueprint objectives + teen verbatim sample questions
([03](03-how-to-prepare-and-sample-questions.md)) + *The AI Agent Factory* ke prompting / governance /
workflow-design crash courses (Zia Tutor corpus gen 66). Koi live item-bank content nahi — guide khud
kehti hai sample questions live bank se nahi.

---

## Domain 1 — Prompting and Task Execution (Q1–Q14)

### Q1
Ek associate ki prompt: *"Act as a world-class analyst with 20 years' experience and write a really
thorough, insightful competitive analysis of our market."* Output fluent hai lekin generic ("slop").
Sabse effective fix?

- A. Aur strong persona do — analyst ki firm, credentials, awards specify karo.
- B. Claude ko kaho "think harder and be more insightful."
- C. Persona hatao aur us ki jagah **audience, woh decision jo analysis feed karega, required sections,
  aur length** do.
- D. Wahi prompt extended thinking mode mein chalao.

**Sahi jawab: C** — Completeness (audience + purpose + structure) clever wording se zyada matter karti
hai. Persona aur "think harder" koi missing information add nahi karte; thinking mode woh context nahi
bana sakta jo diya hi nahi gaya.

### Q2
Ek quarterly business review mein revenue variance, hiring status, top-3 delivery risks, aur
next-quarter forecast cover hone hain. Ek single prompt uneven, shallow sections deta hai. Best
approach?

- A. Wahi prompt dobara, magar 2x word count maango.
- B. Har section ko apna prompt + apne inputs do, har ek verify karo, phir ek combined consistent draft
  maango.
- C. Claude se poocho woh kis section par least confident hai, sirf woh regenerate karo.
- D. Char topics ek numbered list mein do aur exactly ek paragraph per topic force karo.

**Sahi jawab: B** — Decomposition har part ko focused context deta hai aur assembly se pehle
verification allow karta hai. Word count, self-assessed confidence, aur rigid paragraph limits depth
fix nahi karte.

### Q3
Ek hi ghante mein: (1) ek internal AI-literacy program ke 25 naam generate karna, (2) us program ka
formal one-page charter likhna. Dono prompts kaise differ hone chahiye?

- A. Dono mein tone, structure, length precisely fix karo — consistency zaroori hai.
- B. Dono loose aur open rakho — Claude freedom ke sath best perform karta hai.
- C. Naming prompt loose (bahut options, kam constraints); charter prompt tightly specified (structure,
  tone, length).
- D. Naming prompt tightly formatted; charter prompt kai freeform options maange.

**Sahi jawab: C** — Divergent tasks ko breadth + loose constraints chahiye; convergent tasks ko tight
structure. Dono ko ek jaisa treat karna hi ghalti hai.

### Q4
Claude ke client-update email ka pehla draft bahut formal hai aur asal ask (timeline change) aakhri
paragraph mein dabi hui hai. Best next move?

- A. Nayi conversation shuru karo aur original prompt dobara type karo.
- B. Wahi identical prompt dobara bhejo taake alag sample mile.
- C. Targeted feedback do: "Warmer tone; timeline-change request ko pehle do sentences mein lao; baqi
  waisa hi rakho."
- D. Accept karo aur poora email haath se rewrite karo.

**Sahi jawab: C** — Jo specific hissa fail hua use naam do aur sirf woh badlo. Scratch se rewrite ya
resend batata nahi ke kya ghalat tha.

### Q5
Ek associate ek strong 600-word thought-leadership post chahta hai. Kaunsi sequence "brainstorm-iterate
loop" ko best reflect karti hai?

- A. Poora draft maango, phir usko baar-baar grade + fix karo.
- B. Topic scope karo (key arguments + counter-arguments), 3 outline options lo, ek pick + refine karo,
  bullets mein expand, bullets critique, phir draft.
- C. Full context do, ek best outline maango, phir usko draft karwao.
- D. Outline khud likho, phir Claude se sirf prose maango.

**Sahi jawab: B** — Leverage drafting se pehle structural iteration mein hai. Ek outline ya seedha
draft us jagah ko skip kar deta hai jahan value hai.

### Q6
Teen vendor proposals ko paanch weighted criteria ke against analyse kar ke ek recommend karna hai.
Best prompt design?

- A. "Yeh teen proposals parho aur batao kaunsa best hai."
- B. Paanch criteria + weights do, pehle per-criterion comparison maango, phir recommendation with
  assumptions stated.
- C. Pehle recommendation maango, phir supporting reasons.
- D. Har proposal ke liye freeform pros-and-cons list maango.

**Sahi jawab: B** — Convergent/analytical kaam mein evaluation structure supply karo aur comparison ko
conclusion se alag rakho — taake reviewer bina dobara kiye disagree kar sake.

### Q7 — Multiple response (select TWO)
Kaunsi do cheezein aksar generic output ko usable output mein badalti hain?

- A. Lambi prompt.
- B. Woh audience jo output parhega.
- C. Claude ke liye ek persona/role.
- D. Woh decision ya action jo output feed karega.

**Sahi jawab: B aur D** — Audience aur purpose hi missing context hain; length aur persona nahi.

### Q8
Ek associate ek one-off internal FAQ answer refine kar raha hai. Teen rounds ke baad har naya prompt
bahut kam farq la raha hai. Best move?

- A. Iterate karte raho jab tak Claude khud "done" na kahe.
- B. Iterate karte raho jab tak 9.5/10 self-grade na mile.
- C. Khud wheel le lo aur aakhri edits haath se finish karo.
- D. Zyada detailed prompt ke sath dobara shuru karo.

**Sahi jawab: C** — Deliver-once task ke liye tab ruko jab aage prompting sirf marginal change de rahi
ho aur ek chhota manual edit kaam khatam kar de. 9.5 plateau us kaam ke liye hai jo tum own karte ho
aur reuse karte ho.

### Q9
Ek achhi tarah likhi single mega-prompt bhi ek multi-part deliverable ke liye kyun fail hoti hai?

- A. Claude lambi prompts parh nahi sakta.
- B. Har part ko shallow treatment milti hai aur ek part ki galti isolate + verify karna mushkil hota
  hai.
- C. Lambi prompts hamesha hallucination trigger karti hain.
- D. Model turant context khatam kar deta hai.

**Sahi jawab: B** — Breadth without focus-per-part uneven depth deti hai aur verification mushkil.

### Q10
Ek associate: *"EU AI Act research karo aur batao humein kya karna hai."* Best refinement?

- A. Add karo "be thorough and cite everything."
- B. Company ka role (deployer vs provider), jurisdiction, systems in scope, aur yeh ke claims
  verifiable sources se attributed hon legal review ke liye — sab specify karo.
- C. Claude se har point par apni confidence rate karwao.
- D. Bullet summary maango taake chhota rahe.

**Sahi jawab: B** — Task ko scoping context aur ek verification expectation chahiye; "be thorough" aur
self-rated confidence kuch checkable add nahi karte.

### Q11
Ek colleague jo output ko Excel mein sort/filter karega. Output kaise maango?

- A. Ek achhe format ka paragraph summary.
- B. Ek table ya spreadsheet file, ek row per record.
- C. Theme ke hisaab se grouped bullet list.
- D. Ek artifact jismein prose ho.

**Sahi jawab: B** — Agar work product data hai to structured data maango taake load + manipulate ho
sake, prose nahi.

### Q12
Kaunsa feedback ek draft ko sabse reliably improve karega?

- A. "Yeh theek nahi, dobara try karo."
- B. "Ise behtar aur zyada professional banao."
- C. "Second section maan raha hai ke reader hamara pricing model janta hai; ek sentence add karo jo
  usko define kare, aur third paragraph cut karo."
- D. "Main ise 6/10 dunga."

**Sahi jawab: C** — Jis exact hisse ko badalna hai us ka naam lena model ko direct karta hai; vague
feedback aur bare score nahi.

### Q13
Ek staffing plan mein headcount ek attached dataset ke ticket-volume growth se derive hona hai, plus
ek narrative recommendation. Best structure?

- A. Ek prompt: "Data parho aur batao kitne log hire karne hain aur kyun."
- B. Claude se kaho code execution se growth aur per-analyst throughput compute kare, phir alag se
  headcount recommend kare aur assumptions state kare.
- C. Recommendation maango, phir usse math double-check karne ko kaho.
- D. Summary numbers prompt mein paste karo aur recommendation maango.

**Sahi jawab: B** — Computation ko recommendation se alag karo aur assumptions maango; ek likha hua
figure calculated figure jaisa dikhta hai lekin trust nahi kiya ja sakta.

### Q14
20 taglines brainstorm karne ke baad associate ko 3 pasand aaye. Best next prompt?

- A. "In sab 20 se launch campaign banao."
- B. "20 aur taglines do."
- C. "Yeh 3 hain jo mujhe pasand, aur kyun; is voice mein har ek ke 5 refined variants do, phir ek
  pick karenge."
- D. "Best wala pick karo aur campaign bana do."

**Sahi jawab: C** — Divergent set se deliberately narrow karo taste feedback ke sath, converge se
pehle. Seedha campaign par jaana ya model ko pick karne dena tumhara judgment skip karta hai.

---

## Domain 2 — Output Evaluation and Validation (Q15–Q35)

### Q15 (official-style)
Claude ek naye regulation ka confident summary deta hai jismein ek specific subsection number cited
hai. Compliance team ko bhejne se pehle best action?

- A. As-is bhej do — Claude ne high confidence express ki.
- B. Cited subsection ko official regulation text ke against verify karo bhejne se pehle.
- C. Claude se confidence rate karwao aur high ho to bhej do.
- D. Zyada formal sound karne ke liye reword karo, phir bhej do.

**Sahi jawab: B** — Citation numbers jaise specific-looking details prime hallucination risk hain;
self-reported confidence aur reformatting accuracy establish nahi karte.

### Q16
Associate poochta hai "are you sure?" aur Claude kehta hai "Yes, I'm confident." Yeh output ki accuracy
ke baare mein kya batata hai?

- A. Ab yeh verified hai.
- B. Likely correct hai — model shayad hi kabhi false confidence claim karta hai.
- C. Taqreeban kuch nahi — models ghalat jawab par bhi confidence state kar sakte hain.
- D. Factual claims ke liye correct, opinions ke liye nahi.

**Sahi jawab: C** — Confidence reliability signal nahi; verification authoritative source se aani
chahiye.

### Q17
Claude ne ek 4-part request ka jawab diya lekin part 3 khamoshi se chhod diya. Associate ne notice
nahi kiya aur forward kar diya. Kaunsa evaluation step yeh pakadta?

- A. Tone ko audience ke against check karna.
- B. Original request dobara parh kar confirm karna ke har part address hua.
- C. Claude se poochna ke woh confident tha.
- D. Extended thinking mein chalana.

**Sahi jawab: B** — Completeness evaluation ka matlab output ko har requirement se wapas map karna.

### Q18
Ek market brief ke summary mein "revenue grew 12%" hai aur appendix table mein "revenue grew 21%".
Issue aur fix?

- A. Tone inconsistency; voice standardise karo.
- B. Internal inconsistency; use se pehle dono figures ko source data ke against reconcile karo.
- C. Formatting; table upar le aao.
- D. Bias; second opinion lo.

**Sahi jawab: B** — Internal contradiction accuracy problem ka signal hai; dono ko source tak trace
karo.

### Q19
Ek internal newsletter draft mein koi factual error nahi lekin woh ek department ko delay ki wajah ke
tor par frame karta hai. Domain-2 concern aur best response?

- A. Completeness; aur departments add karo.
- B. Bias/framing; publish se pehle neutral, evidence-based language mein revise karo.
- C. Consistency; pichhle mahine ke newsletter se align karo.
- D. Yeh Domain-2 issue nahi; accurate hai.

**Sahi jawab: B** — Output evaluate karne mein loaded framing aur unfair attribution check karna bhi
shamil hai, sirf facts nahi.

### Q20
Kaunsa output sabse clearly human subject-matter review maangta hai, chahe quality kitni bhi achhi ho?

- A. Internal team-event ideas ka brainstorm.
- B. Ek first-draft internal meeting agenda.
- C. Ek client ke contractual obligations ka summary jis par account team act karegi.
- D. Ek blog intro ka tone rewrite.

**Sahi jawab: C** — Client-facing, decision-driving, contractual content verification ladder ke top
par.

### Q21
Ek associate 30 minute ek throwaway internal brainstorm ki har line fact-check karne mein lagata hai
aur ek client-facing financial summary sirf skim karta hai. Kaunsa principle violate ho raha hai?

- A. Hamesha sab kuch barabar verify karo.
- B. Verification effort ko output ke stakes aur reversibility se match karo.
- C. Brainstorms kabhi verify mat karo.
- D. Client work ko kam checking chahiye kyunki client review karega.

**Sahi jawab: B** — Diligence consequence ke sath scale honi chahiye.

### Q22
Claude ek press-style draft mein ek named executive ka direct "quote" include karta hai. Best action?

- A. Rakho — sentiment achhi tarah capture karta hai.
- B. Fabricated maano jab tak executive ne asal mein na kaha ho; hatao ya approved quote se replace
  karo.
- C. Kam specific sound karne ke liye soften karo.
- D. Claude se source poocho aur jawab par trust karo.

**Sahi jawab: B** — Attributed quotes real aur approved hone chahiye; model se source poochna
verification nahi.

### Q23 — Multiple response (select TWO)
Kaunse do elements ek output mein pehle sources ke against check hone chahiye?

- A. General topic framing.
- B. Ek specific statistic with a percentage.
- C. Ek named study with a year.
- D. Overall structure.

**Sahi jawab: B aur C** — Specific figures aur named sources classic fabrication points hain.

### Q24
Claude ne ek technically correct lekin jargon-heavy analysis banayi. Audience ek non-technical client
sponsor hai. Best move?

- A. Bhej do — accurate hai.
- B. Adapt karo: plain language, decision aur us ke implications se shuru, technical detail appendix
  mein.
- C. Aakhir mein glossary add kar ke bhej do.
- D. Claude se kaho "make it more executive."

**Sahi jawab: B** — Evaluation mein correct content ko audience ke liye adapt karna shamil hai; vague
"more executive" changes name karne se weak hai.

### Q25
Associate ke paas same deliverable ke do versions hain — ek concise, ek detailed. Kaunsa use karein,
kaise decide?

- A. Hamesha detailed wala — zyada info safe hai.
- B. Har ek ko audience, us decision jo woh feed karta hai, aur reader ke waqt ke against judge karo,
  phir pick ya blend karo.
- C. Jo Claude prefer kare.
- D. Hamesha concise wala — executives busy hote hain.

**Sahi jawab: B** — Fit-to-purpose aur audience decide karti hai, koi blanket rule nahi.

### Q26
Claude ne 15 findings diye; sirf 6 client ke asal sawaal se relevant hain. Delivery se pehle best
move?

- A. Completeness ke liye sab 15 include karo.
- B. Relevant findings tak curate karo, logical order mein, scope note karte hue.
- C. Pehle 6 jaise aaye waise bhej do.
- D. Client se poocho unhe kaunse chahiye.

**Sahi jawab: B** — Jo matter karta hai us tak organise aur curate karna usable output banane ka hissa
hai.

### Q27
Ek output mein factual claim validate karne ka sabse reliable tareeka?

- A. Claude se khud double-check karne ko kaho.
- B. Ek independent authoritative source ke against check karo.
- C. Output regenerate karo aur dekho claim repeat hota hai.
- D. Colleague se poocho "sounds right?"

**Sahi jawab: B** — Independent authoritative verification; regeneration wahi error repeat kar sakta
hai.

### Q28
Ek naye category ke analysis par Claude ko trust karne se pehle associate ko pehle kya karna chahiye?

- A. Ek past case par chalao jis ka correct outcome pehle se pata hai aur compare karo.
- B. Sabse mushkil live case par chalao stress-test ke liye.
- C. Claude se apni methodology describe karne ko kaho.
- D. Do Claude runs ko aapas mein compare karo.

**Sahi jawab: A** — Ek trusted baseline hi bata sakta hai ke reproduction hui ya sirf plausible-sounding
output.

### Q29
Woh known-answer test pass karna deta hai:

- A. Transferable assurance — ab similar outputs verify karne ki zaroorat nahi.
- B. Similar work ke liye tested confidence, lekin final result ki accountability kabhi transfer nahi
  hoti.
- C. Regulated work par human review skip karne ki ijazat.
- D. Us category ke liye guarantee.

**Sahi jawab: B** — Confidence scale hoti hai; accountability insaan ke paas rehti hai.

### Q30
Ek plan mein headcount figure ek sentence mein likha hua hai, attached data se derived. Yeh validation
risk kyun hai?

- A. Prose figures hamesha ghalat hote hain.
- B. Page se pata nahi chalta ke calculate hua ya likha gaya; ek likha figure apni working nahi
  dikhata.
- C. Model arithmetic nahi kar sakta.
- D. Sentences reliably numbers contain nahi kar sakte.

**Sahi jawab: B** — Consequential numbers ko code se compute karwao taake woh ek re-runnable
calculation tak trace karein.

### Q31
Ek 20-page report drift karti hai: executive summary ki recommendation section 6 se contradict karti
hai. Likely cause aur best fix?

- A. Bias; reviewer lao.
- B. Document ek bare single pass mein generate hua; section-by-section regenerate + reconcile karo,
  ya decision ko ek single source ke against verify karo.
- C. Formatting; cross-references add karo.
- D. Tone; voice unify karo.

**Sahi jawab: B** — Bara single-pass generation drift karta hai; decomposition aur reconciliation
address karti hai.

### Q32
Claude ne ek policy FAQ likhi jo common cases achhe handle karti hai lekin woh exception chhod deti
hai jo associate ne specifically mention kiya tha. Evaluation lesson?

- A. FAQs exceptions cover nahi kar sakti.
- B. Check karo ke explicitly-stated requirements aur edge cases mojood hain, sirf obvious content
  nahi.
- C. Zyada length maango.
- D. Accept karo — exceptions rare hain.

**Sahi jawab: B** — Completeness mein specific aur unusual dono shamil hain, khaaskar jab named hon.

### Q33
Ek regulated financial disclosure jo Claude ne draft ki, use hona chahiye:

- A. Kisi qualified insaan se line-by-line reviewed aur source figures ke against checked, kisi bhi
  use se pehle.
- B. Bhej do agar Claude ki confidence high hai.
- C. Do paragraphs spot-check karo.
- D. Internally bina review use karo, externally review ke sath.

**Sahi jawab: A** — Regulated, high-stakes content ko full expert review + source verification chahiye.

### Q34
Claude ne ek 40-page contract summarise kiya. Account team ke summary par rely karne se pehle associate
ko chahiye:

- A. Trust karo agar coherent hai.
- B. Summary ke key obligations aur dates ko actual contract clauses ke against check karo.
- C. Claude se dobara summarise karwao aur compare karo.
- D. Claude se summary rate karwao.

**Sahi jawab: B** — Summarised source ki key claims original ke against verify hoti hain.

### Q35 — Multiple response (select TWO)
Kaunse do signs batate hain ke ek output ko human review chahiye?

- A. Woh ek irreversible external decision feed karta hai.
- B. Woh ek internal draft hai jise aap waise bhi edit karenge.
- C. Woh ek regulated domain se related hai.
- D. Woh ek brainstorm hai.

**Sahi jawab: A aur C**

---

## Domain 3 — Product and Model Selection (Q36–Q47)

### Q36 (official-style)
High volume mein short customer-reply drafts chahiye jahan speed aur cost deep reasoning se zyada matter
karte hain. Best choice?

- A. Har reply ke liye sabse capable, highest-cost model.
- B. Ek faster, lower-cost model jo straightforward high-volume tasks ke liye suited hai.
- C. Cost kam karne ke liye sab product features disable karo.
- D. Kisi doosre AI platform par switch karo.

**Sahi jawab: B** — Model selection ko task requirements se align karna: high-volume straightforward
kaam ke liye faster/cheaper model; capable model complex reasoning ke liye reserve.

### Q37
Current model names memorise karne se pehle fast/thinking/flagship tier pattern kyun seekhna?

- A. Names kabhi nahi badalte.
- B. Names aur versions tez badalte hain; tier pattern task ke hisaab se choose karne deta hai aur
  names se zyada chalta hai.
- C. Pattern sirf exam par required hai.
- D. Tiers pricing exactly determine karte hain.

**Sahi jawab: B**

### Q38
Kaunsa task extended thinking / reasoning mode ko best justify karta hai?

- A. Ek list reformat karna.
- B. Ek multi-step financial trade-off analysis jismein interacting constraints hain.
- C. Ek one-line factual lookup.
- D. 50 subject lines generate karna.

**Sahi jawab: B**

### Q39
Ek associate roz kai baar wahi brand guidelines, tone rules, aur product facts Claude mein paste karta
hai. Best move?

- A. Paste karte raho — reliable hai.
- B. Ek Project banao jismein yeh instructions + knowledge hon taake har chat inherit kare.
- C. Sab kuch ek bohot lambi prompt template mein daal do.
- D. Har baar naya chat use karo taake fresh rahe.

**Sahi jawab: B** — Projects store knowledge; recurring stable context wahan jaata hai.

### Q40
Kaunsa artifact use karne ka sabse clear case hai?

- A. Ek quick question poochna.
- B. Ek 10-page proposal co-write aur iterate karna.
- C. Ek yes/no answer lena.
- D. 20 ideas brainstorm karna.

**Sahi jawab: B**

### Q41
Instructions, memory, aur projects ko separate karne wala rule?

- A. Instructions for scoped work, memory for rules, projects for context.
- B. Instructions for stable rules, memory for evolving context, projects for scoped work.
- C. Teenon interchangeable hain.
- D. Memory for stable rules, projects for baqi sab.

**Sahi jawab: B**

### Q42
Complete karo: "Projects ___ store karte hain; skills ___ perform karte hain."

- A. tasks; knowledge
- B. knowledge; tasks
- C. prompts; connectors
- D. context; memory

**Sahi jawab: B**

### Q43
Ek one-time board-level strategy memo jahan nuance aur correctness paramount hain aur volume ek hai.
Best model choice?

- A. Sabse fast, cheapest model budget bachane ke liye.
- B. Sabse capable model — volume-one par cost negligible hai aur quality paramount.
- C. Jo bhi default ho.
- D. Do saste models aur merge.

**Sahi jawab: B**

### Q44
Ek 3-din purani conversation ab aise answers de rahi hai jo earlier decisions ignore karte hain. Best
fix?

- A. Claude se kaho behtar yaad rakhe.
- B. Key decisions summarise kar ke ek fresh chat mein continue karo, aur stable context ko Project
  mein move karo.
- C. Chalte raho — recover kar lega.
- D. Model switch karo.

**Sahi jawab: B**

### Q45
Kaunsa statement correct model-selection judgment reflect karta hai?

- A. Hamesha top model — quality kabhi ghalat nahi.
- B. Model ko task se match karo: simple high-volume ke liye cheap/fast, complex ya high-stakes ke
  liye capable.
- C. Hamesha cheapest model aur iterate.
- D. Model choice cost par meaningfully asar nahi daalti.

**Sahi jawab: B**

### Q46
Ek associate ko kai sources par ek synthesised review with citations chahiye. Best feature fit?

- A. Ek plain single chat message.
- B. Research / deep-research mode (ya extended thinking with sources), phir citations verify karo.
- C. Sirf ek artifact.
- D. Ek Project bina knowledge ke.

**Sahi jawab: B**

### Q47 — Multiple response (select TWO)
Naya chat shuru karne ki kaunsi do achhi wajah hain?

- A. Topic badal kar kisi unrelated cheez par aa gaya.
- B. Conversation bohot lambi hai aur answers degrade ho rahe hain.
- C. Aap thodi alag phrasing chahte ho.
- D. Claude ne ek chhoti si galti ki jo aap already correct kar chuke.

**Sahi jawab: A aur B**

---

## Domain 4 — Workflow Integration and Solution Design (Q48–Q63)

### Q48
Ek invoice-approval process mein kaunsa step Claude ke end-to-end own karne ke liye sabse kharab fit
hai?

- A. Invoice se approval-request summary draft karna.
- B. Contract terms se deviate karne wali invoices ko review ke liye flag karna.
- C. Payment execute karna aur usko ledger mein likhna.
- D. Ek mahine ke approvals ko report ke liye summarise karna.

**Sahi jawab: C** — System-of-record writes aur irreversible financial actions ko deterministic
systems + human authority chahiye.

### Q49
Ek operations lead poora client-onboarding process "AI ko de dena" chahta hai. Best first move?

- A. Poora flow turant automate karo.
- B. Steps map karo, Claude ko pehle drafting/summarising steps par daalo (human review retained),
  measure karo, phir redesign consider karo.
- C. Decline karo — onboarding automate nahi ho sakta.
- D. Kuch test karne se pehle process ko AI ke around redesign karo.

**Sahi jawab: B** — Ek step augment karo, accountability rakho, value prove karo, phir redesign sirf
justified ho to.

### Q50
Kisi process ko automate karne se "haan" kehne se pehle sabse useful do sawal?

- A. "Kaunsa model cheapest hai?" aur "Kitna time lagega?"
- B. "Decision points kahan hain aur un ke liye kaun accountable hai?" aur "Kaunse steps
  language/synthesis hain vs deterministic/irreversible?"
- C. "Client ko AI pasand hai?" aur "Budget hai?"
- D. "Kya hum human review skip kar sakte hain?" aur "Data bara hai?"

**Sahi jawab: B**

### Q51
Stakeholders ko Claude-based reporting workflow pitch karte hue associate ko chahiye:

- A. Sirf time savings emphasise karo buy-in ke liye.
- B. Concrete value state karo (jaise 2 ghante → 20 minute, consistent structure) aur honest limits
  (review chahiye, system of record nahi, data restrictions), aur human checkpoints name karo.
- C. Promise karo ke yeh fully autonomous hoga.
- D. Limitations mention mat karo taake doubt na ho.

**Sahi jawab: B**

### Q52
Ek proposed workflow ko API integration, ek unattended cross-tool agent, aur ek custom connector
chahiye. Yeh:

- A. Associate ke scope mein hai.
- B. Associate scope se bahar — design aur build ke liye Claude Architect/Developer ko escalate karo.
- C. Attempt karo aur sirf fail hone par escalate karo.
- D. Sirf ek governance sawal hai.

**Sahi jawab: B**

### Q53
Ek process map mein Claude wahan insert hona chahiye jahan woh:

- A. Human decision-maker ko replace kare.
- B. Repetitive drafting/synthesis toil hataye jabke humans decision points rakhein.
- C. Seedha system of record mein likhe.
- D. Review step eliminate kare.

**Sahi jawab: B**

### Q54
"Augment" ka matlab hai:

- A. Poore process ko AI ke around redesign karna.
- B. Ek specific existing step ko tez karna (AI drafts, human reviews and sends).
- C. Process se humans hatana.
- D. Aur steps add karna.

**Sahi jawab: B**

### Q55
Ek client kehta hai "hum chahte hain AI support handle kare." Best next step?

- A. Ek full autonomous support agent propose karo.
- B. Actual support workflow analyse karo: ticket types, volumes, decision points, current owners, aur
  "handle" ka matlab — phir propose karo Claude kahan fit hota hai.
- C. Sabse capable model recommend karo.
- D. Poocho kis competitor se woh worried hain.

**Sahi jawab: B**

### Q56
Ek stakeholder ko sabse defensible value statement?

- A. "Yeh analyst role ki zaroorat khatam kar dega."
- B. "Yeh weekly reports ke first-draft time ko kaafi kam karega, analyst review aur final ko own
  karega."
- C. "Yeh error-free hoga."
- D. "Yeh review ki zaroorat khatam karta hai."

**Sahi jawab: B**

### Q57
Kisi process ko AI ke around redesign karna (sirf augment nahi) kab appropriate hai?

- A. Turant, maximum value capture ke liye.
- B. Jab augmenting ne value prove kar di ho, structural gain clear ho, aur team kaam karne ka tareeka
  badalne ke liye ready ho.
- C. Kabhi nahi.
- D. Jab bhi client kahe.

**Sahi jawab: B**

### Q58 — Multiple response (select TWO)
Kaunse do steps human ko loop mein rakhte hain?

- A. Ek client deliverable par final sign-off.
- B. Ek first draft generate karna.
- C. Policy ki ek exception approve karna.
- D. Text reformat karna.

**Sahi jawab: A aur C**

### Q59
Ek stakeholder maan raha hai ke workflow ka output authoritative hai. Associate ko chahiye:

- A. Rehne do taake confidence bani rahe.
- B. Expectation correct karo: outputs drafts/decision support hain jinhe review chahiye; system of
  record kahin aur hai.
- C. Sirf appendix mein disclaimer add karo.
- D. Batao ke Claude usually sahi hota hai.

**Sahi jawab: B**

### Q60
Ek working 6-prompt weekly workflow ko optimise kaise karein?

- A. Aur review steps add karo.
- B. Prompts ko template banao, stable context ko Project mein move karo, aur agar quality hold kare
  to cheaper model par jao.
- C. Safety ke liye sabse capable model par switch karo.
- D. Har prompt do baar chalao.

**Sahi jawab: B**

### Q61
Solution design mein Claude best use hota hai:

- A. Final architecture decision karne ke liye.
- B. Options aur trade-offs map karne, iterations draft aur critique karne, aur assumptions
  pressure-test karne ke liye — humans decide karte hain.
- C. Design review ko replace karne ke liye.
- D. Design approve karne ke liye.

**Sahi jawab: B**

### Q62
Ek established workflow mein Claude introduce karne ka lowest-risk tareeka?

- A. Ek poora sub-process replace karo.
- B. Ek high-toil, low-risk step par human review ke sath add karo, aur results ke hisaab se expand
  karo.
- C. Saara data us se route karo.
- D. Use core systems ka write access do.

**Sahi jawab: B**

### Q63
Jab ek requested workflow Associate scope se bahar ho, associate ko chahiye:

- A. Waise bhi build karo aur umeed rakho.
- B. Clearly explain karo kya scope mein hai kya nahi, aur technical build ko Architect/Developer ko
  route karo jabke use-case aur process par khud involved raho.
- C. Poori engagement decline karo.
- D. Client ko batao yeh impossible hai.

**Sahi jawab: B**

---

## Domain 5 — Configuration and Knowledge Management (Q64–Q75)

### Q64
Kaunse Project instructions stronger hain?

- A. "Be helpful, professional, and thorough."
- B. "UK English mein likho; teen se zyada items ki list ke liye bullets; statistics kabhi invent mat
  karo; audience non-technical client sponsors; agar koi figure provided knowledge mein nahi to keh
  do."
- C. "Act like a senior consultant."
- D. "Follow best practices."

**Sahi jawab: B** — Specific, testable rules vague aspirations se behtar.

### Q65
Kya per-prompt ki jagah Project instructions mein hona chahiye?

- A. Aaj ke task ka specific data.
- B. Stable rules: tone, format defaults, audience, always/never constraints.
- C. One-off question.
- D. Pichhle draft par feedback.

**Sahi jawab: B**

### Q66
Ek associate ek client-reporting Project mein 40 loosely related documents upload kar deta hai "taake
Claude ke paas sab kuch ho." Outputs kam relevant ho jaate hain. Best advice?

- A. Aur upload karo taake full context ho.
- B. Authoritative, relevant documents tak curate karo; bohot saara low-signal material retrieval
  dilute karta hai.
- C. 40 Projects mein split karo.
- D. Saara knowledge hatao aur prompts par rely karo.

**Sahi jawab: B**

### Q67
Ek 6-mahine purana "Brand Voice" Project ab purani tagline aur purana logo guidance deta hai. Root
cause aur process fix?

- A. Model regression; model switch karo.
- B. Stale knowledge/instructions; brand assets badalne par Project ki sources update karo aur ek
  owner assign karo jo maintain kare.
- C. Prompt problem; lambi prompts likho.
- D. Kuch ghalat nahi; dobara poocho.

**Sahi jawab: B**

### Q68
Jab aap ek connector enable karte ho, Claude access kar sakta hai:

- A. Us service mein sab kuch.
- B. Sirf woh jo aap ka apna account dekhne aur karne ke liye permitted hai.
- C. Sirf woh files jo aap explicitly attach karo.
- D. Kuch nahi jab tak admin har request approve na kare.

**Sahi jawab: B** — Connector aap ki apni permissions inherit karta hai.

### Q69
Ek workflow ke liye connector add karte hue best practice?

- A. Convenience ke liye pehle se write/send access do.
- B. Read-only se shuru karo, access ko task ke hisaab se tightly scope karo, aur confirm karo ke aap
  ko woh account connect karne ki ijazat hai.
- C. Saari apps connect karo taake Claude ke paas context ho.
- D. Work data ke liye personal account use karo.

**Sahi jawab: B**

### Q70
Ek app connect karne se pehle associate ko yeh sab poochna chahiye SIVAYE:

- A. Yeh kya read kar sakta hai?
- B. Kya yeh write, send, delete, ya buy kar sakta hai?
- C. Kaunsa model use karega?
- D. Kya main yeh account connect karne ki ijazat rakhta hun?

**Sahi jawab: C** — Model choice permission decision se unrelated hai.

### Q71
Jab company pricing badle, ek pricing-dependent Project ke liye correct action?

- A. Users ko kaho har prompt mein naye prices mention karein.
- B. Project ki knowledge source aur instructions update karo, aur change date note karo.
- C. Har quarter naya Project banao.
- D. Kuch nahi; Claude infer kar lega.

**Sahi jawab: B**

### Q72
Ek Project mein ek hi policy document ke do versions hain. Likely effect?

- A. Claude dono ka average le lega.
- B. Confident answers jo shayad outdated version follow karein; exactly ek current version rakho.
- C. Claude har baar poochega kaunsa use karna hai.
- D. Koi effect nahi.

**Sahi jawab: B**

### Q73
Ek shared Project ko accurate rakhne ka sabse sustainable tareeka?

- A. Umeed rakho users problems report karein.
- B. Ek named owner assign karo jo schedule par aur change events par instructions + knowledge review
  aur update kare.
- C. Project lock kar do taake koi edit na kar sake.
- D. Har mahine rebuild karo.

**Sahi jawab: B**

### Q74
Har hafte associate ko ek hi tone drift manually fix karni padti hai ek Project ke output mein. Best
fix?

- A. Manually fix karte raho.
- B. Tone rule ko explicitly Project instructions mein encode karo taake dobara na ho.
- C. Bare model par switch karo.
- D. Har baar naya chat shuru karo.

**Sahi jawab: B**

### Q75 — Multiple response (select TWO)
Ek achhe knowledge source ki do khaasiyatein?

- A. Woh task ke liye authoritative hai.
- B. Woh lamba hai.
- C. Woh current aur version-controlled hai.
- D. Woh loosely related background hai.

**Sahi jawab: A aur C**

---

## Domain 6 — Governance, Risk, and Responsible Use (Q76–Q90)

### Q76 (official-style)
Ek PM customer names aur account numbers wali spreadsheet upload karna chahta hai taake Claude trends
analyse kare. Org policy regulated personal data share karne ko restrict karti hai. Best action?

- A. As-is upload karo — analysis internal hai.
- B. Upload se pehle personal identifiers remove ya anonymize karo, policy ke mutabiq.
- C. Upload karo lekin Claude ko instruct karo retain na kare.
- D. Analysis poori tarah skip karo.

**Sahi jawab: B**

### Q77
"Upload karo lekin Claude ko kaho retain na kare" acceptable control kyun nahi?

- A. Claude hamesha sab kuch retain karta hai.
- B. Ek model instruction policy ya contractual data control nahi; woh governance requirement satisfy
  nahi karti.
- C. Yeh response slow karta hai.
- D. Yeh sirf Enterprise par kaam karta hai.

**Sahi jawab: B**

### Q78
Privacy constraints ke tehat dataset analysis ke liye tayyar karne ka sabse sound tareeka?

- A. IDs ke ilawa sab kuch hatao.
- B. Woh information hatao jo task ko nahi chahiye, phir baaki data aur intended route ko us standard
  ke against check karo jo aap ki organisation ko govern karta hai.
- C. Names hash karo aur baaki sab rakho.
- D. Claude se poocho kya hatana hai.

**Sahi jawab: B**

### Q79
Ek associate maan raha hai ke incognito chats ki koi retention nahi. Correct understanding?

- A. Incognito ka matlab kuch bhi kahin store nahi hota.
- B. Incognito chats ko history/memory se bahar rakhta hai lekin ek default retention period phir bhi
  apply hota hai; yeh zero retention nahi.
- C. Incognito model ko disable karta hai.
- D. Incognito ek Project jaisa hai.

**Sahi jawab: B**

### Q80
Associate kis basis par assume kar sakta hai ke inputs models train karne ke liye use nahi honge?

- A. Yeh hamesha sach hai.
- B. Yeh plan aur settings par depend karta hai — Team/Enterprise/API par by default nahi;
  Free/Pro/Max par ek user setting — to route confirm karo.
- C. Sirf agar aap incognito use karein.
- D. Sirf signed NDA ke sath.

**Sahi jawab: B**

### Q81
"Code ek sandbox mein chalta hai, to sensitive file load karna theek hai." Kya ghalat hai?

- A. Kuch nahi; sandboxes secure hain.
- B. Execution isolation code ki reach limit karta hai; yeh establish nahi karta ke file us environment
  mein allowed thi.
- C. Sandboxes data leak karte hain.
- D. Sandboxes slow hote hain.

**Sahi jawab: B**

### Q82
Ek associate maanta hai ek chat private hai kyunki interface mein sirf woh use dekh sakta hai.
Governance reality?

- A. Woh fully private hai.
- B. Team/Enterprise organisational export aur audit mechanisms dete hain; administrative visibility
  route assessment ka hissa hai.
- C. Free plans par sirf admins use dekh sakte hain.
- D. Kuch bhi kabhi exportable nahi.

**Sahi jawab: B**

### Q83
Kaunsa Associate ke design karne ke liye inappropriate use hai?

- A. Internal meeting notes draft karna.
- B. Claude ke output ko human judgment ke bina ek adverse HR decision ka sole basis banana.
- C. Public research summarise karna.
- D. Campaign ideas brainstorm karna.

**Sahi jawab: B**

### Q84
Org ki AI policy client data ko external tools mein forbid karti hai, lekin ek asaan technical
workaround mojood hai. Associate ko chahiye:

- A. Workaround use karo — outcome same hai.
- B. Policy follow karo; workaround ki asaani governance override nahi karti.
- C. Ek baar use karo aur document karo.
- D. Claude se poocho theek hai ya nahi.

**Sahi jawab: B**

### Q85
Ek workflow jo healthcare records handle karega, associate ko pehle kya karna chahiye?

- A. Real records par test karo realistic hone ke liye.
- B. Invented/demo data par test karo, aur real data ke waqt sirf approved accounts aur connectors
  use karo.
- C. Testing skip karo.
- D. Ek colleague ke records use karo.

**Sahi jawab: B**

### Q86
Ek client deliverable substantially AI-drafted hai aur firm ki professional recommendation ke tor par
bina review present ki gayi. Concerns?

- A. Sirf data privacy.
- B. Data handling, accountability (ek insaan recommendation own kare), aur disclosure/appropriate
  review.
- C. Sirf formatting.
- D. Koi nahi; client ne jaldi maanga tha.

**Sahi jawab: B**

### Q87
Claude se job candidates ko rank karwana kaunse governance concerns raise karta hai, aur ek safer
design?

- A. Koi concern nahi; efficient hai.
- B. Bias aur fairness plus accountability; ise zyada se zyada defined criteria ke against structured
  note-taking ke liye use karo, humans decision karein aur own karein.
- C. Sirf speed concerns.
- D. Concerns sirf agar candidates ko pata chale.

**Sahi jawab: B**

### Q88
Kisi bhi upload se pehle pehla governance sawal?

- A. "Kaunsa model cheapest hai?"
- B. "Kya yeh information regulated, personal, ya confidential hai, aur kya policy is route ko allow
  karti hai?"
- C. "Document kitna lamba hai?"
- D. "Kya Claude ko yeh useful lagega?"

**Sahi jawab: B**

### Q89
Kaunsa ek appropriate use case hai jise Associate confidently design kar sakta hai?

- A. Ek regulated tax opinion generate kar ke client ko as-is dena.
- B. Meeting transcripts ko action-item lists mein turn karna jinhe owner review karega.
- C. Loan applications ko approve/reject karna.
- D. Ek medical diagnosis draft karna patient ke liye.

**Sahi jawab: B** — Productivity/synthesis kaam human review ke sath appropriate hai; B ke ilawa sab
adverse/regulated decisions hain jinhe escalate ya avoid karna chahiye.

### Q90 — Multiple response (select TWO)
Claude se data withhold karne ki do legitimate wajah?

- A. Us mein regulated personal identifiers hain jo task ko nahi chahiye.
- B. Woh lamba hai.
- C. Organisational policy ya client contract us route ko prohibit karti hai.
- D. Woh boring hai.

**Sahi jawab: A aur C**

---

## Domain 7 — Troubleshooting and Optimization (Q91–Q100)

### Q91
Ek associate ki product-description prompt "achhi" lagti hai lekin output har baar flat aur
interchangeable aata hai. Sabse likely diagnosis?

- A. Model bug — support ko report karo.
- B. Prompt mein audience, differentiators, aur woh purpose missing hai jo output ko specific banaye.
- C. Model bohot chhota hai.
- D. Context window full hai.

**Sahi jawab: B** — Generic output ka classic cause missing audience + goal; fix rewrite nahi, missing
context add karna.

### Q92
Ek prompt kabhi-kabhi fabricated numbers deta hai. Associate ne prompt ko 3 guna lamba kar diya —
problem barqarar. Asal fix?

- A. Aur bhi lamba karo.
- B. Numbers ko grounding do (authoritative source / Project knowledge) ya code execution se compute
  karwao, aur output verify karo.
- C. Har baar "don't hallucinate" add karo.
- D. Temperature kam karo.

**Sahi jawab: B** — Prompt-length cause address nahi karta; missing grounding karta hai. "Don't
hallucinate" instruction reliable control nahi.

### Q93
Ek prompt paragraph deta hai jab ek comparison table chahiye tha. Fastest fix?

- A. Poora prompt dobara likho.
- B. Ek explicit format spec add karo (columns naam do) ya ek chhota example do sahi shape ka.
- C. Model badlo.
- D. Output ko manually table mein convert karo har baar.

**Sahi jawab: B** — Weakest ingredient (output shape) fix karo — ek example ya explicit format se.

### Q94
Ek underperforming prompt ko systematically diagnose karne ka best tareeka?

- A. Random tweaks karte raho jab tak behtar na ho.
- B. Output parho aur naam do ke request ka kaunsa hissa fail hua (audience ignore? length broke?
  tone drifted?), sirf woh part badlo aur resend.
- C. Claude se score maango 1–10 aur us hisaab se lamba karo.
- D. 5 baar regenerate karo aur best rakho.

**Sahi jawab: B** — Diagnosis (kaunsa part fail hua) grading se stronger hai ek weak result ke liye.

### Q95
Ek working workflow ko efficiency ke liye optimise karne ka best step?

- A. Har prompt ke baad ek extra review step add karo.
- B. Redundant steps hatao, prompts ko templates banao, stable context Project mein move karo, aur
  quality hold kare to cheaper model par jao.
- C. Sabse capable model par upgrade karo.
- D. Har run do baar chalao consistency ke liye.

**Sahi jawab: B**

### Q96
Har hafta associate ko ek Project ke output mein wahi ek edit (ek disclaimer add karna) karni padti
hai. Best long-term fix?

- A. Edit karte raho — 30 second lagte hain.
- B. Disclaimer requirement ko Project instructions mein daalo taake har output mein automatically
  aaye.
- C. Model switch karo.
- D. Client se poocho disclaimer chahiye ya nahi.

**Sahi jawab: B** — Recurring manual fix ko configuration mein encode karo.

### Q97
Ek associate ne ek prompt change kiya aur output "behtar lagta hai." Approach adjust karne ka sound
tareeka?

- A. Assume karo behtar hai aur aage badho.
- B. Change ko ek known case par purane version ke against compare karo — behtar hai ya sirf alag,
  yeh objectively check karo.
- C. Claude se poocho kaunsa version behtar hai.
- D. Dono versions client ko bhej do.

**Sahi jawab: B** — Feedback aur results ke hisaab se adjust karna maano evidence ke sath, impression
ke sath nahi.

### Q98
Ek prompt ek complex report ke liye kabhi kaam karta hai kabhi shallow output deta hai — same prompt.
Sabse likely cause?

- A. Model random hai, kuch nahi ho sakta.
- B. Task ek single call ke liye bohot bara/broad hai; decompose karo taake har part consistent depth
  paaye.
- C. Prompt mein "please" missing hai.
- D. Wrong model tier.

**Sahi jawab: B** — Inconsistent depth on a big task ka signal decomposition ki zaroorat.

### Q99
Ek associate ne 10 minutes ek prompt tune karne mein lagaye jo woh sirf ek baar use karega. Better
judgment?

- A. Perfect prompt ke liye tuning jaari rakho.
- B. Ek "kaafi achha" prompt ke baad output ko manually finish karo — one-off task diminishing
  returns par jaldi rukta hai.
- C. Ek Project banao is one-off ke liye.
- D. Sabse capable model use karo taake prompt matter na kare.

**Sahi jawab: B** — Optimisation effort ko reuse se match karo; ek one-off deliverable prompt-craft
ke bajaye manual finish deserve karta hai.

### Q100 — Multiple response (select TWO)
Ek workflow jo pehle se kaam kar raha hai, us par kaunse do optimisation moves valid hain?

- A. Stable, repeated context ko Project mein move karna.
- B. Har step par ek naya human approval add karna "just in case."
- C. Agar output quality hold kare to ek faster/cheaper model par jaana.
- D. Har prompt ko 2x lamba karna robustness ke liye.

**Sahi jawab: A aur C**

---

## Answer Key — Quick Grid

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | C | 21 | B | 41 | B | 61 | B | 81 | B |
| 2 | B | 22 | B | 42 | B | 62 | B | 82 | B |
| 3 | C | 23 | B,C | 43 | B | 63 | B | 83 | B |
| 4 | C | 24 | B | 44 | B | 64 | B | 84 | B |
| 5 | B | 25 | B | 45 | B | 65 | B | 85 | B |
| 6 | B | 26 | B | 46 | B | 66 | B | 86 | B |
| 7 | B,D | 27 | B | 47 | A,B | 67 | B | 87 | B |
| 8 | C | 28 | A | 48 | C | 68 | B | 88 | B |
| 9 | B | 29 | B | 49 | B | 69 | B | 89 | B |
| 10 | B | 30 | B | 50 | B | 70 | C | 90 | A,C |
| 11 | B | 31 | B | 51 | B | 71 | B | 91 | B |
| 12 | C | 32 | B | 52 | B | 72 | B | 92 | B |
| 13 | B | 33 | A | 53 | B | 73 | B | 93 | B |
| 14 | C | 34 | B | 54 | B | 74 | B | 94 | B |
| 15 | B | 35 | A,C | 55 | B | 75 | A,C | 95 | B |
| 16 | C | 36 | B | 56 | B | 76 | B | 96 | B |
| 17 | B | 37 | B | 57 | B | 77 | B | 97 | B |
| 18 | B | 38 | B | 58 | A,C | 78 | B | 98 | B |
| 19 | B | 39 | B | 59 | B | 79 | B | 99 | B |
| 20 | C | 40 | B | 60 | B | 80 | B | 100 | A,C |

---

## Scoring

- **90–100:** exam-ready is domain profile par. Real exam is se aasan hoga.
- **75–89:** solid. Jo domains 75% se neeche unke [08-teaching-walkthrough.md](08-teaching-walkthrough.md)
  sections dobara.
- **60–74:** blueprint objectives ([01](01-domain-blueprint.md)) dobara + [06 easy guide](06-easy-exam-guide.md)
  ke 3 patterns rattao.
- **< 60:** poora [08-teaching-walkthrough.md](08-teaching-walkthrough.md) + [07-full-mock-60q.md](07-full-mock-60q.md)
  pehle, phir yeh dobara.

---
[⬅ CCAO-F Index](README.md) · [07 — Full Mock (60 Q)](07-full-mock-60q.md) ·
[09 — Purcell Practice Key](09-purcell-practice-60q.md)
