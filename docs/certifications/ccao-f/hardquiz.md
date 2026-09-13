# CCAO-F — Hard Companion Quiz (100 Questions, Complexity 12/10)

*Yeh `quiz100.md` ka **harder companion set** hai — sab 100 scenarios naye hain, koi bhi
`quiz100.md` ke scenario se duplicate nahi. Jahan `quiz100.md` khud ko "complexity 10/10" kehta
hai, yeh set jaan-boojh kar us se aage jaata hai. Teen cheezein specifically harder banati hain:*

1. **Lambe, denser scenarios** — har stem mein named role + concrete numbers/constraints +
   multiple stakeholders (3–5 sentences minimum), taake tumhe pehle scenario ko poora parhna pare
   phir hi principle apply karna aaye.
2. **Closer-call distractors** — har option "good vs best" ya "defensible vs correct" hai. Koi
   bhi option obviously silly nahi — har ek woh mistake represent karta hai jo ek competent-but-
   not-yet-senior associate asaani se kar sakta hai (jaise: "review karwa dena" bola lekin WHO/
   WHAT/WHEN naam nahi liya; ya "halo delegation" — pichli baar kaam ho gaya isliye is baar zyada
   de dena).
3. **Deeper book concepts jo `quiz100.md` ne kam chhue** — delegation map ke 3 layers
   (eligibility → ownership → implementation), error taxonomy ke 6 named types (factual error,
   logical gap, false confidence, missing context, fabricated source, stale fact), data tiers
   (green/yellow/red), five checks for a new capability (source/reach/fit/outside-content/
   actions), cross-model-family checking (same family = not independent), "halo delegation" aur
   "unstaffed gate" jaise named traps, aur troubleshooting ka pura 5-step "cheapest-first" ladder
   (under-specification → context overload → wrong feature/model → stale configuration →
   expectation mismatch).

**Distribution (same official blueprint weights × 100 as quiz100.md):**

| Domain | Weight | Questions |
| --- | --- | --- |
| 1 — Prompting and Task Execution | 14% | Q1–Q14 |
| 2 — Output Evaluation and Validation | 21% | Q15–Q35 |
| 3 — Product and Model Selection | 12% | Q36–Q47 |
| 4 — Workflow Integration and Solution Design | 16% | Q48–Q63 |
| 5 — Configuration and Knowledge Management | 12% | Q64–Q75 |
| 6 — Governance, Risk, and Responsible Use | 15% | Q76–Q90 |
| 7 — Troubleshooting and Optimization | 10% | Q91–Q100 |

**Kaise use karo:** `quiz100.md` pehle solid score (75%+) ke baad hi yeh set attempt karo — yeh
sequel hai, entry point nahi. Ek domain cold attempt karo, phir rationale parho — har rationale
mein yeh bhi likha hai ke har GALAT option **kis wajah se plausible dikhta hai**, taake tumhe pata
chale tum khud kis trap mein girte ho. Timing target: 100 Q in ~180 min (harder stems, zyada
reading load).

**Grounding:** official exam-guide blueprint objectives ([01](01-domain-blueprint.md)) + teen
verbatim sample questions ([03](03-how-to-prepare-and-sample-questions.md)) + *The AI Agent
Factory* crash courses (Zia Tutor corpus **gen 71**, 2026-09-14 ko fetch hua) —
`ai-prompting-2026`, `problem-solving-crash-course`, `workflow-design-diagnosis-crash-course`,
`governance-risk-responsible-use-crash-course`, `skills-connectors-crash-course`,
`ai-fluency-crash-course`, `how-to-think-ai-era`, `claude-chatgpt-101-crash-course`,
`what-ai-actually-is-crash-course`. Koi live item-bank content nahi — guide khud kehti hai sample
questions live bank se nahi.

---

## Domain 1 — Prompting and Task Execution (Q1–Q14)

### Q1
Meridian Legal Ops ki associate, Farah, ek naye vendor-risk questionnaire ke 40 answers draft
karwana chahti hai. Woh ek single prompt bhejti hai: *"Yahan 40 sawalat hain, humari purani
vendor files attach hain, sab ka jawab do."* Output aata hai — lekin pehle 10 answers detailed
hain, agle 15 half-sentence hain, aur aakhri 15 mein "insufficient information" repeat hota hai
bina yeh bataye ke kaunsi specific file missing thi. Farah ke paas 2 ghante hain deadline tak.
Sabse effective next move kya hai?

- A. Wahi prompt dobara bhejo, lekin "please be thorough for all 40" add karo.
- B. **✅ 40 sawalat ko 3–4 batches mein todo (jaise related-topic groups), har batch apne relevant
  files ke sath bhejo, aur har batch ka output verify karne ke baad agle batch par jao.**
- C. Sirf un 15 "insufficient information" wale answers ko dobara ek naya prompt mein bhejo, baaki
  25 ko as-is rakho.
- D. Claude se poocho kaunsi files missing hain, phir woh files upload kar ke ek hi prompt mein
  saara kaam dobara maango.

**Sahi jawab: B** — Yeh ek breadth-heavy convergent task hai jahan single-pass generation depth
degrade karti hai jaise-jaise list lambi hoti hai (quality drift ek known single-pass failure mode
hai). Batching decomposition ka case hai, na ke "please be thorough" (A) — jo koi missing
information supply nahi karta. C attractive lagta hai kyunki woh problem-area target karta hai,
lekin woh yeh assume karta hai ke pehle 25 answers fully correct hain — jabke unhe kabhi verify
nahi kiya gaya, sirf "detailed lagte hain." D theek direction hai (missing files identify karna)
lekin phir dobara ek hi mega-prompt mein wapas chala jaata hai — usi single-pass problem ko repeat
karta hai jise fix karna tha.

### Q2
DeltaWorks ke ek product manager, Hamza, do alag kaam ek hi afternoon mein karwana chahte hain:
(1) naye feature ke liye 30 taglines brainstorm, (2) us feature ka ek formal customer-facing
changelog entry, jo legal bhi review karega. Hamza dono prompts mein exactly same structure use
karta hai: "Give me options with rationale for each, formatted as a numbered list, 1-2 sentences
each." Result: taglines list boring aur samey-samey lagti hai, aur changelog entry mein har line
ke sath ek "rationale" hai jo customer-facing text mein bilkul jagah nahi banti. Root cause?

- A. Numbered list format dono task-types ke liye ghalat hai — bullets use karne chahiye the.
- B. **✅ Divergent task (brainstorm) ko loose constraints aur breadth chahiye thi, convergent task
  (legal-reviewed changelog) ko tight structure/tone chahiye thi — Hamza ne dono ko same
  "options + rationale" mold mein force kar diya, jo kisi ke liye bhi sahi fit nahi.**
- C. Legal review ki wajah se changelog prompt mein "be extremely careful" add karna chahiye tha.
- D. Dono prompts alag conversations mein hone chahiye the, structure koi farq nahi karta.
**Sahi jawab: B** — Ek hi rigid template dono opposite-natured tasks par thop dena hi asal ghalti
hai: brainstorming ko options ke sath internal "rationale" nahi chahiye (woh breadth ko slow karta
hai), aur legal-reviewed customer text ko "rationale per option" wala shape nahi chahiye (woh
customer ke liye noise hai). A format symptom pakadta hai lekin cause miss karta hai — bullets bhi
same template-mismatch problem repeat karte. C ek vague safety-word add karta hai jo tone
concretely define nahi karta. D sahi observation hai (separate conversations achha idea hai) lekin
asal defect — structure ka mismatch — address nahi karta.

### Q3
Northwind Consulting ki analyst, Priya, Claude se kehti hai: *"Write me a compelling case for why
our client should adopt the new pricing model."* Output fluent aur confident hai, lekin Priya ko
lagta hai ke woh generic hai — koi bhi consulting firm koi bhi client ko yeh de sakti thi. Client
ka naam, unka current pricing pain-point, aur woh specific decision jo yeh memo drive karega —
teenon Priya ke apne notes mein hain lekin prompt mein kabhi gaye nahi. Best fix?

- A. Prompt mein "make it more persuasive and data-driven" add karo.
- B. Claude se pehle poocho ke woh client ke baare mein kya jaanta hai, phir uske jawab ke hisaab
  se aage badho.
- C. **✅ Client ka naam, unka specific current pain-point, aur woh decision jise memo feed karega —
  teeno apne notes se copy kar ke prompt mein daalo.**
- D. Ek doosra example "compelling case" doc attach karo taake Claude us jaisa likhe.

**Sahi jawab: C** — Missing context (audience/situation/purpose) hi generic output ka classic root
cause hai; jo information sirf Priya ke paas hai (client-specific facts) usay supply karna hi
seedha fix hai. A wording ko tez karta hai bina naya fact diye — output "sound" zyada confident
ho sakta hai lekin utna hi generic reh sakta hai. B ek reasonable-lagne wala move hai lekin
inefficient hai: Claude se guess karwa kar phir correct karna, jab Priya ke paas facts already
maujood hain, ek extra unnecessary round-trip hai. D style ka example de sakta hai lekin content
ka gap (client-specific facts) abhi bhi khaali rahega — style aur substance alag cheezein hain.

### Q4
Vantage Ops ke associate, Tomás, ek client-facing status email ka draft Claude se maangta hai.
Pehla draft tone-wise perfect hai lekin asal message — ke delivery date 2 hafte peeche ja rahi hai
— aakhri paragraph mein ek subordinate clause mein chhupi hui hai. Tomás jaanta hai exactly kya
galat hai. Best next prompt?

- A. "Try again, make the delay clearer."
- B. **✅ "Tone bilkul rakho jo hai; delay ki announcement ko pehle do sentences mein lao aur ek
  specific naya date do; baaki structure waisa hi chhodo."**
- C. Nayi conversation shuru karo aur poora context dobara type karo taake fresh perspective mile.
- D. Email khud rewrite karo — pehla paragraph delay ke sath, phir Claude ke baaki draft ko
  as-is neeche paste kar do.

**Sahi jawab: B** — Specific, named feedback (kya rakhna hai + kya move karna hai + kya add karna
hai) exact fail-point ko target karta hai bina jo already achha hai use disturb kiye. A vague hai
— "clearer" define nahi karta ke structurally kya move karna hai, is se dobara random placement
aa sakta hai. C context ko poora discard karta hai jab sirf ek structural move chahiye tha — waste
of the good tone work already done. D ek reasonable manual patch hai lekin unnecessarily labor-
intensive hai jab ek chhota targeted prompt wahi result 30 second mein de sakta tha.

### Q5 — Multiple response (select TWO)
Orbit Analytics ke ek naye associate ko sikhaya ja raha hai ke "task decomposition" kab prompt
chaining (fixed sequence of focused passes) ki tarah honi chahiye aur kab dynamic honi chahiye
(structure pehle map karo, phir plan adapt karo jaise dependencies saamne aati hain). Kaunse DO
scenarios **dynamic decomposition** ke liye behtar fit hain, fixed prompt-chaining ke bajaye?

- A. Har hafte ek fixed-format 4-section status report banana (budget, risks, hiring, forecast).
- B. **✅ Ek legacy codebase mein "comprehensive test coverage add karo" — jahan pehle se pata nahi
  ke kaunse modules high-risk hain.**
- C. **✅ Ek naya market jahan koi existing research nahi — "humein is market mein entry ke liye kya
  pata hona chahiye" open-ended investigate karna.**
- D. Ek fixed 5-criteria vendor-comparison table banana teen known vendors ke liye.

**Sahi jawab: B aur C** — Dono open-ended investigations hain jahan aspects ki list khud pata nahi
— structure pehle discover karni padti hai, phir plan adapt hoti hai jaise naye dependencies/
findings saamne aate hain. A aur D dono predictable, multi-aspect-lekin-known-shape tasks hain
(fixed sections, fixed criteria) — inhe ek fixed sequence of focused passes (prompt chaining) hi
efficiently handle karti hai; unhe "dynamic" treat karna unnecessary overhead create karta hai.

### Q6
Clearline Insurance ke associate, Ben, ek 12-page claims-policy document rewrite karwa raha hai
taake naye regulatory language reflect ho. Woh poori 12 pages ek prompt mein deta hai aur "rewrite
karo" kehta hai. Result: page 1-3 naye terminology consistently use karti hain, lekin page 9 tak
purani terminology wapas aa jaati hai — jaise Claude "bhool gaya" ke kya rewrite ho raha tha. Yeh
kis principle ki violation hai, aur fix?

- A. Claude bade documents nahi parh sakta — ise chhota karna hoga.
- B. **✅ "Small, reversible decomposition" principle — ek chapter/section ek waqt mein rewrite karo,
  har section ko previous rules ke against check karo, phir agle par jao.**
- C. Prompt mein "remember to use new terminology throughout" 5 baar repeat karo.
- D. Regulatory terminology list ko prompt ke bilkul end mein daalo taake "fresh" rahe.

**Sahi jawab: B** — Yeh classic single-pass drift hai (jaisa lambi document rewrites mein hota
hai) — poori document ek sath rewrite karne se style rules bhool jaate hain jab tak page 12 aaye.
Chapter-by-chapter with a check against prior rules hi fix hai. A galat hai — model 12 pages parh
sakta hai, masla depth-consistency hai token limit nahi. C ek hi instruction repeat karna kisi
naye control ka wajood nahi banata — drift phir bhi ho sakta hai kyunki verification step missing
hai. D placement trick hai jo systematic fix nahi — koi guarantee nahi ke end-of-prompt info page
9 tak survive karegi.

### Q7
Bridgepoint HR ki associate, Naila, Claude se ek difficult termination-conversation script maang
rahi hai — usay apne manager ko yeh conversation lead karwani hai kal. Woh apna pehla prompt bhejti
hai, phir result padh kar 4 alag revisions maangti hai ek ke baad ek: "make it warmer," phir "no,
make it more direct," phir "add empathy back," phir "shorten it." Har round output alag direction
mein move karta hai bina consistently behtar hue. Sabse likely diagnosis?

- A. Model conversation lambi ho gayi isliye confuse ho raha hai.
- B. **✅ Feedback contradictory aur vague hai (warmer → direct → empathy → shorter, bina yeh naam
  liye ke exact kaunsa sentence/section problem hai) — Naila ko pehle define karna chahiye ke
  "warm" aur "direct" is specific conversation mein kaise dikhte hain, phir ek specific hissa
  target karna chahiye.**
- C. Termination scripts inherently AI se nahi likhwaye ja sakte.
- D. Naila ko sabse capable/flagship model try karna chahiye.

**Sahi jawab: B** — Vague, mutually-in-tension feedback ("warmer" phir "direct" phir "empathy")
bina concrete anchor ke random walk create karta hai — koi definition nahi ke tone ka target state
kya hai. Fix hai ek specific target describe karna ("first sentence mein acknowledge karo ke yeh
mushkil hai, phir facts 2 sentences mein, koi hedge nahi") ek exact section par. A conversation-
length ka masla nahi — yeh feedback-quality ka masla hai chahe pehla hi round ho. C ek scope
statement hai jo galat hai — Domain-6 ki baat hai ke sensitive HR content review chahiye, na ke
ise draft hi na kiya jaaye. D model-selection ek unrelated fix hai — yeh feedback-precision ka
issue hai, capability ka nahi.

### Q8 — Multiple response (select TWO)
"AI Prompting in 2026" ka brainstorm-iterate loop ek pattern deta hai: pehle **context** do, phir
**options generate karo, unme se feedback ke sath narrow karo**. Kaunse DO real examples is loop
ko sahi follow karte hain?

- A. **✅ Ek 4-din trip plan karte hue: budget/dates/who's-going/dislikes do, phir 5 rough
  itineraries maango, 2 reject karo, baaki refine karo.**
- B. Ek naam suggest karne ke liye sirf "give me a good product name" bolna, phir jo pehla naam
  aaye woh use kar lena.
- C. **✅ Ek mushkil email likhte hue: recipient/relationship/desired-outcome do, phir 3 alag tones
  maango, ek pick karo, details refine karo.**
- D. Ek contractor choose karte hue seedha Claude se poochna "kaunsa contractor best hai" bina
  quotes ya priorities diye.

**Sahi jawab: A aur C** — Dono context-first (constraints/situation) → options-with-feedback
(generate, narrow, refine) loop follow karte hain. B aur D dono context skip karte hain aur pehla
output accept kar lete hain — na context diya gaya, na hi iteration hui, jo loop ke dono halves
miss karta hai.

### Q9
Solace Wealth ke associate, Faisal, ek staffing-projection memo likh raha hai jahan headcount
figure ek attached CSV (ticket-volume growth) se derive hona hai. Woh Claude se poochta hai: "is
data ko dekho aur mujhe batao hume kitne analysts hire karne chahiye, ek confident recommendation
ke sath." Claude ek number aur ek confident-sounding paragraph deta hai. Faisal ise as-is board
memo mein paste karta hai. Kya risk hai aur behtar approach kya tha?

- A. Koi risk nahi — Claude data attach kiya gaya tha, isliye number reliable hai.
- B. **✅ Ek prose sentence mein likha figure yeh nahi dikhata ke woh calculate hua ya sirf
  "plausible-sounding" generate hua — behtar approach: Claude se code execution se growth-rate aur
  per-analyst throughput compute karwana, phir recommendation ko us calculation ke against derive
  karna, assumptions explicitly state karte hue.**
- C. Risk hai kyunki CSV format Claude parh nahi sakta — usay pehle table mein convert karna
  chahiye tha.
- D. Faisal ko khud Excel mein number recalculate karna chahiye, Claude ka number ignore kar ke.

**Sahi jawab: B** — Consequential numbers (headcount decisions board ko jaayenge) ko re-runnable
calculation (code execution) se derive karwana chahiye, na ke ek written sentence se — likha hua
figure apni working nahi dikhata isliye trust nahi kiya ja sakta bina verification ke. A confident
tone ko accuracy maan leta hai jo galat assumption hai. C ek false technical claim hai — Claude
CSV parh sakta hai, masla format nahi computation-visibility hai. D poori Claude ki value discard
karta hai jab asal fix sirf "compute karwao, verify karo" hai, "khud dobara sab karo" nahi.

### Q10
Ferrovia Rail ke ops associate, Grace, ek EU rail-safety directive research karwana chahti hain:
*"Naye EU rail safety directive ko research karo aur batao humein operationally kya karna hai."*
Task legal review ke liye jaana hai. Best refinement?

- A. "Be extremely thorough and cite every source you can find" add karo.
- B. **✅ Company ka role (infrastructure manager vs operator), affected rolling-stock/routes,
  jurisdiction, aur yeh requirement ke har claim ek verifiable article/annex number se attributed
  ho legal review ke liye — sab specify karo.**
- C. Claude se poocho har finding par apni confidence 1-10 rate kare, aur sirf 8+ wale rakho.
- D. Output ko sirf 5 bullet points tak limit karo taake legal team jaldi parh sake.

**Sahi jawab: B** — Scoping context (role, applicability, jurisdiction) aur ek concrete
verification requirement (article/annex attribution) dono missing pieces hain jo legal-reviewed
research ke liye zaroori hain. A vague intensifier hai — "thorough" koi checkable criterion nahi
deta. C self-rated confidence accuracy ka reliable signal nahi hai (model apne hi galat jawab par
bhi high confidence de sakta hai). D length constraint completeness ko risk mein daalta hai bina
underlying scoping/verification problem solve kiye.

### Q11
Praxis Media ke ek associate, Leo, ko ek dataset chahiye jo colleague Excel mein pivot-table
banayega — customer churn by region by month, teen columns. Leo Claude se maangta hai: "give me a
nicely formatted summary of churn trends by region." Output ek achhi tarah likha paragraph hai
jisme numbers prose mein embedded hain. Colleague ab manually numbers wapas extract kar raha hai.
Root cause aur fix?

- A. Koi masla nahi — paragraph informative hai, colleague ko adjust karna chahiye.
- B. **✅ Work product structured data tha (row/column manipulation ke liye), prose format maanga
  gaya — output format ko downstream use se match karna chahiye tha: ek table/CSV-shape output,
  ek row per region-month.**
- C. Leo ko Claude se kehna chahiye tha "make it more detailed."
- D. Colleague ko khud Claude se dobara poochna chahiye, Leo se nahi.

**Sahi jawab: B** — Jab downstream use structured manipulation (sort/filter/pivot) hai, output
format bhi structured hona chahiye — prose iske liye galat container hai chahe woh kitna bhi
"achha likha" ho. A quality ko format se confuse karta hai — well-written prose bhi galat format
ho sakta hai is use-case ke liye. C detail add karega lekin structure ka masla solve nahi karega
— zyada prose, zyada extraction work. D process ko complicate karta hai jab asal fix seedha (right
format maango) hai.

### Q12
Anchor Freight ke ek dispatcher-turned-associate, Wren, Claude se ek incident-report draft maang
raha hai jisme unattended forklift collision detail hai. Draft technically accurate hai lekin
factually-neutral report ko is tarah frame karta hai jaise driver akela zimmedar tha, jabke Wren ke
notes mein loading-dock lighting bhi ek factor thi jo mention nahi hui. Yeh kaunsa evaluation issue
hai aur best move (Domain 1 lens se — prompt design)?

- A. Yeh sirf Domain-2 issue hai, Domain-1 se koi lena dena nahi.
- B. **✅ Root cause prompt design mein hai — Wren ne apne notes ka woh hissa (lighting factor)
  prompt mein include hi nahi kiya; agli baar prompt mein explicitly saare contributing factors
  list karna chahiye, na ke Claude par chhodna ke woh khud guess kare kya relevant hai.**
- C. Draft ko bilkul as-is chhod dena chahiye — driver-focus factually galat nahi hai.
- D. Prompt mein "be balanced and fair" add karna kaafi hoga.
**Sahi jawab: B** — Yeh dikhata hai ke Domain 1 (prompting) aur Domain 2 (evaluation) overlap
karte hain: agar prompt mein hi ek known contributing factor missing tha, to output us factor ko
kabhi include nahi karega — model apne se woh fact invent nahi kar sakta jo diya hi nahi gaya. A
galat hai kyunki root-cause fix prompting stage par hai (missing input), sirf output-review par
nahi. C factually incomplete framing ko accept karta hai jo unfair hai. D ek vague instruction hai
jo missing factual input ko replace nahi karta — "be balanced" Claude ko woh fact nahi de sakta jo
usay bataya hi nahi gaya.

### Q13
Solstice Retail ke ek marketing associate, Aditi, 25 campaign taglines brainstorm karwati hai —
sab loose, koi constraint nahi, jaisa divergent task ke liye theek hai. Usay 4 pasand aate hain.
Ab agla step launch-ready final copy banana hai jo legal aur brand dono approve karenge. Sahi agla
prompt kaunsa hai?

- A. "In sab 25 se ek full launch kit (email + social + banner) bana do."
- B. "25 aur taglines do, options zyada chahiye."
- C. **✅ "Yeh 4 hain jo mujhe pasand, aur kyun; hamari brand voice guide (attached) follow karte
  hue har ek ke 3 tightly-worded variants do, phir hum final pick karenge."**
- D. "Best tagline khud pick karo aur poora launch kit bana do."

**Sahi jawab: C** — Divergent phase khatam ho chuki hai; ab convergent narrowing chahiye taste-
feedback ke sath (kyun pasand aaya) plus tight constraints (brand voice) taake variants usable
hon, final-pick se pehle. A seedha ek bade deliverable par jump karta hai bina narrowing consolidate
kiye — decisions abhi bhi loose hain. B divergent phase ko unnecessarily extend karta hai jab
already-preferred options mil chuke hain. D judgment ko Claude ko de deta hai jo Aditi ka apna kaam
hai — model ko "best" define karne ka koi taste-context nahi diya gaya.

### Q14 — Multiple response (select TWO)
Ek naya associate poochta hai: "task decomposition sirf lambe documents ke liye hai kya?" Senior
colleague explain karta hai ke decomposition ka faida sirf length se nahi, balke kuch aur signals
se bhi aata hai. Kaunse DO signals decomposition ko justify karte hain, chahe task chhota length
mein ho?

- A. **✅ Task mein multiple independent-verifiable parts hain (ek part ki galti doosre parts se
  alag check ho sakti hai).**
- B. Task ko sirf ek hi sentence mein describe kiya ja sakta hai.
- C. **✅ Ek part ka result agle part ke liye input banta hai, aur beech mein galti pakadna sasta
  hai poore chain ke aakhir mein pakadne se.**
- D. Task associate ko personally pasand nahi.

**Sahi jawab: A aur C** — Independent-verifiability aur sequential-dependency-with-cheap-early-
detection dono decomposition ka asal case hain — chhota task bhi in signals ke sath decompose hona
chahiye. B (short description) task ki complexity ke baare mein kuch nahi batata — ek one-sentence
task bhi deeply interdependent ho sakta hai. D personal preference koi technical criterion nahi
hai.

---

## Domain 2 — Output Evaluation and Validation (Q15–Q35)

### Q15 (official-style, reworded scenario)
Aria Compliance ke associate, Deven, Claude se ek naye data-protection amendment ka summary
maangta hai. Output confident hai aur ek specific clause number cite karta hai — "Section 14(3)(b)
requires notification within 72 hours." Deven ko yeh summary compliance director ko forward karna
hai jo isi hafte board ko report karega. Deven ke paas amendment ka official PDF bhi open hai
doosri tab mein. Sabse appropriate action?

- A. Forward kar do — Claude ka tone confident tha aur clause number specific lagta hai.
- B. **✅ Forward karne se pehle Section 14(3)(b) ko official PDF mein khol kar exact wording aur
  time-window verify karo.**
- C. Claude se poocho "are you sure about this clause number?" aur uske "yes" ke baad forward karo.
- D. Summary ko thoda reword karo taake zyada authoritative sound kare, phir forward karo.

**Sahi jawab: B** — Specific-looking details (clause numbers, exact figures) fabrication ke sabse
classic points hain — independent source ke against direct verification hi reliable check hai, aur
PDF already open hai to cost almost zero hai. A confidence ko accuracy maan leta hai. C ek self-
verification loop hai — model apne hi output ko "confirm" kar sakta hai bina asal source dekhe,
yeh independent nahi. D sirf presentation change karta hai, underlying claim ko touch nahi karta.

### Q16
Bellwood Analytics ke associate, Kiran, apne draft ko khud teen baar regenerate karta hai — har
baar wahi prompt, teeno versions mein wahi statistic ("industry churn averages 18%") consistent
aata hai. Kiran isay "triangulation" maan kar accept kar leta hai bina external source check kiye.
Kya galat hai is reasoning mein?

- A. Kuch galat nahi — teen consistent outputs ek reliable signal hain.
- B. **✅ Ek hi model se same prompt dobara chalane se independent verification nahi milta — model
  ka wahi training-data blind spot teeno regenerations mein consistently repeat hoga; consistency
  correctness ka proxy nahi hai.**
- C. Teen regenerations bohat kam hain — Kiran ko 10 baar chalana chahiye tha.
- D. Statistic sahi hai kyunki 18% ek "round-ish" number hai jo plausible lagta hai.

**Sahi jawab: B** — Regeneration same model/same knowledge-base se hoti hai, isliye ek systematic
error (jaise ek fabricated-lekin-plausible industry figure) har regeneration mein identically
repeat ho sakta hai — yeh independent path nahi hai jo real verification maangti hai. C sirf
sample-size badhata hai isi flawed method ka, quality nahi. D ek numerology-jaisi heuristic hai
jo koi verification nahi hai.

### Q17
Fenwick Capital ke analyst, Omar, Claude se poochta hai ek 5-part client memo banane ko: executive
summary, market context, risk factors, three scenarios, aur recommendation. Output aata hai jisme
pehle 4 parts achhi tarah likhe hain lekin "recommendation" section missing hai — us jagah sirf ek
transition sentence hai jo agle section ka promise karta hai jo kabhi aata nahi. Omar summary
padhta hai, achha lagta hai, aur client ko bhej deta hai. Kaunsa evaluation step yeh miss karwata?

- A. Tone check — professional lagta tha isliye pass ho gaya.
- B. **✅ Completeness check — original 5-part request ko wapas har section ke against map karna,
  taake confirm ho ke sab 5 present hain, na ke sirf "confident sound karta hai."**
- C. Claude se poochna "did you finish everything?"
- D. Extended thinking mode mein dobara chalana.

**Sahi jawab: B** — Ek missing section (khaas kar jab woh silently drop ho, error message ke bina)
sirf systematic mapping se pakdi jaati hai — request ke har named part ko output mein dhoondo. A
tone accuracy/completeness se independent hai. C self-report unreliable hai — model khud confident
"complete" bol sakta hai jab section chhoot gaya ho. D thinking mode ek missing part wapas nahi
la sakta agar underlying generation hi usay skip kar chuki.

### Q18
Harborview Municipal ke associate, Tess, ek infrastructure report compile kar rahi hai. Executive
summary section kehta hai "bridge repairs cost estimate: $2.1M," jabke detailed cost breakdown
table (usi document mein, Claude ne hi banaya) individual line items sum kar ke $2.4M deta hai.
Tess ko yeh notice tab hua jab ek council member ne poocha "kaunsa number sahi hai?" Best fix?

- A. Dono numbers ko average kar ke $2.25M report karo.
- B. **✅ Yeh internal inconsistency hai — dono figures ko source estimates ke against reconcile
  karo pehle, phir jo correct nikle wahi dono jagah use karo.**
- C. $2.1M ko rakho kyunki woh pehle likha gaya tha (executive summary usually authoritative hota
  hai).
- D. $2.4M ko rakho kyunki woh line-item detail se aaya, aur woh "zyada precise" lagta hai.

**Sahi jawab: B** — Do numbers jo same underlying fact represent karte hain lekin match nahi karte,
ek accuracy red flag hai — averaging ek fabricated third number banata hai jo dono se bhi galat ho
sakta hai. C aur D dono ek number ko doosre se "senior" maan lete hain bina reconcile kiye — order
ya "precision-lagna" correctness ka proof nahi hai; asal source data (individual repair estimates)
ke against check karna zaroori hai.

### Q19
Kestrel Media ki associate, Yasmin, ek internal newsletter draft review kar rahi hai jo koi
factual error nahi rakhta lekin ek missed product-launch deadline ko subtly ek specific team
("engineering was slow to finalize specs") ki wajah se frame karta hai, jabke actual root cause
(jo Yasmin jaanti hai) ek cross-team scheduling conflict tha. Domain-2 concern aur fix?

- A. Completeness issue — aur teams ka mention add karo.
- B. **✅ Bias/framing issue — publish se pehle attribution ko neutral, evidence-based language mein
  revise karo jo actual root cause reflect kare, na ke ek team ko unfairly singled out kare.**
- C. Yeh Domain-2 ka scope nahi — factually accurate hai isliye pass.
- D. Sirf ek disclaimer add karo end mein: "views may not reflect full picture."
**Sahi jawab: B** — Individually-accurate facts bhi unfair ya misleading frame ban sakte hain jab
attribution galat cause implicate kare — output evaluation mein loaded framing check karna shamil
hai, sirf line-by-line fact-check nahi. C bias ko out-of-scope maan leta hai jo ghalat hai (Domain
2 explicitly bias/inconsistency include karta hai). D ek disclaimer add karna underlying unfair
framing ko fix nahi karta, sirf usay legally hedge karta hai.

### Q20
Northfield Advisory ke associate, Cyrus, ke paas 2 outputs hain: ek client-facing tax-strategy
memo jo Claude ne draft kiya, aur ek internal brainstorm list "5 ways to make our onboarding fun."
Cyrus ke paas sirf 20 minutes hain aaj — kis output par apna review-time zyada lagana chahiye, aur
kyun?

- A. Dono ko barabar 10-10 minutes do — fairness zaroori hai.
- B. **✅ Tax-strategy memo par zyada waqt do — verification effort ko stakes aur reversibility se
  match karo: client-facing, financially-consequential content ka error costly aur mushkil-se-
  undo hota hai; internal brainstorm ka error trivial aur reversible hai.**
- C. Onboarding brainstorm par zyada waqt do kyunki woh naya/creative kaam hai.
- D. Dono ko skip karo aur seedha bhej do taake deadline miss na ho.

**Sahi jawab: B** — Diligence effort consequence-proportional honi chahiye — high-stakes, low-
reversibility client-facing financial content ko sabse zyada scrutiny chahiye. A ek "equal effort"
heuristic hai jo stakes ko ignore karta hai — yehi galti hai jo is principle ko violate karti hai.
C prioritization ko ulta kar deta hai. D dono ko unreviewed chhodna sabse zyada risk hai, khaas
kar tax memo ke liye.

### Q21
Praetor Realty ke associate, Beck, ek press-style tenant-newsletter draft mein dekhta hai ke
Claude ne building-manager ka ek direct "quote" include kiya hai — "Our residents' safety has
always been our top priority" — jo sunne mein plausible hai lekin Beck ko yaad nahi ke manager ne
kabhi yeh exact wording kahi ho. Best action?

- A. Rakho — sentiment building ke values ke against consistent hai.
- B. **✅ Fabricated maano jab tak manager ne asal mein confirm na kare ke unhone yeh kaha; jab tak
  confirm na ho, hataao ya generic non-quoted statement se replace karo.**
- C. Quote ko thoda generic bana do taake kam specific lage, phir rakho.
- D. Claude se poocho "did the manager actually say this?" aur uske jawab par trust karo.

**Sahi jawab: B** — Named-person attributed quotes real aur verified/approved hone chahiye —
"plausible sentiment" attribution ke liye kaafi nahi hai; publish se pehle asal confirmation
chahiye. A plausibility ko authenticity samajh leta hai. C sirf specificity kam karta hai, jhoothi
attribution ka core problem (kisi ne yeh kaha hi nahi) waisa hi rehta hai. D model se apne hi
fabrication ke baare mein poochna verification nahi hai — model ke paas "manager ne kya kaha" ka
koi ground-truth access nahi hai.

### Q22
Solaris Energy ke associate, Femi, Claude se ek grid-outage summary maangta hai jo ek non-
technical city-council audience ko present hona hai. Output technically sahi hai lekin "N-1
contingency," "load-shedding cascade," aur "reactive power deficit" jaisi terms bina explanation
ke use karta hai. Femi ke paas dobara likhwane ka waqt nahi — meeting 30 minutes mein hai. Best
move?

- A. As-is present karo — technical accuracy sabse important hai.
- B. **✅ Council ke saamne pehle plain-language decision aur uski implications state karo ("bijli
  4 ghante ke liye kyun gayi, dobara hone se rokne ke liye kya chahiye"), technical terms ko sirf
  parenthetical ya appendix mein rakho.**
- C. Sirf glossary slide add karo aakhir mein.
- D. Claude ko kaho "make it more executive" aur naya draft jo bhi aaye use present karo.
**Sahi jawab: B** — Correct content ko audience-appropriate banane ka matlab hai decision-first,
plain-language lead karna, technical detail ko background mein rakhna — sirf accurate hona kaafi
nahi jab audience non-technical ho. A audience-fit ko ignore karta hai. C ek passive fix hai —
council abhi bhi jargon-heavy body text padhega, glossary end mein help nahi karegi live meeting
mein. D "more executive" ek undefined instruction hai jo unpredictable result de sakta hai 30
minute deadline ke sath risky hai.

### Q23 — Multiple response (select TWO)
"How to Think in the AI Era" ka error-taxonomy 6 named mistake types deta hai: factual error,
logical gap, false confidence, missing context, fabricated source, stale fact. Kessler Logistics
ke associate ko ek Claude-written vendor-comparison memo milta hai jismein likha hai: *"Vendor B's
2019 uptime SLA of 99.99% makes them the clear winner, therefore we should sign the 3-year
contract immediately."* Is single sentence mein kaunse DO error types sabse strongly present hain?

- A. **✅ Stale fact — 2019 ka SLA number 7 saal purana hai aur ho sakta hai ab valid na ho.**
- B. **✅ Logical gap — "clear winner" se "sign 3-year contract immediately" tak jump karta hai bina
  yeh discuss kiye ke aur factors (price, support, exit terms) bhi hain ya nahi.**
- C. False confidence — sentence "may" ya "could" use karta hai.
- D. Fabricated source — sentence koi study ya article cite karta hai jo exist nahi karta.

**Sahi jawab: A aur B** — 2019 ka number aaj ke decision ke liye potentially outdated hai (stale
fact), aur "therefore immediately sign" ek conclusion hai jo uptime alone se justify nahi hota
(logical gap — missing steps jaise cost, terms, other criteria). C galat hai — sentence mein koi
hedge ("may/could") hai hi nahi, balke woh flatly confident hai bina hedge ke, jo alag se ek
concern hai lekin C ka description khud galat hai. D galat hai — is sentence mein koi named study/
article/citation nahi hai jo invent hui ho.

### Q24
Ashgrove University ke associate, Priyanka, ek admissions-committee ke liye applicant-summary
memo banwati hai. Claude 15 findings deta hai per applicant, lekin committee ka rubric sirf 6
specific criteria par based hai. Priyanka in sab 15 ko as-is forward kar deti hai "completeness ke
liye." Kya masla hai?

- A. Koi masla nahi — zyada information hamesha behtar hai committee ke liye.
- B. **✅ Relevant findings (jo rubric ke 6 criteria se match karte hain) tak curate karna chahiye
  tha, logical order mein, aur scope note karna chahiye tha ke baaki 9 kis wajah se exclude hue —
  raw volume completeness nahi banata, usability banati hai.**
- C. Sirf pehle 6 findings jaise aaye waise forward kar dena chahiye tha.
- D. Committee se poochna chahiye tha unhe kaunse 6 chahiye.
**Sahi jawab: B** — Curating jo matter karta hai (rubric-aligned) usable output banane ka hissa
hai; "sab kuch de do completeness ke naam par" actually noise create karta hai jab decision-
criteria already known hain. A yeh galat maanta hai ke zyada volume = zyada value. C arbitrary
hai — "pehle 6 jaise aaye" ka rubric ke 6 criteria se koi guarantee'd match nahi hai. D
unnecessary hai jab rubric already defined hai — Priyanka khud match kar sakti hai.

### Q25
Vireo Health Partners ke ek associate, Sam, ek naye triage-workflow ke liye Claude ka pehla test-
run kar rahe hain — ek purana case jiska outcome unhe pehle se pata hai. Claude ka output us
purane case ke sahi outcome se match karta hai. Sam is result ko kaise samajhna chahiye?

- A. Ab is workflow ko kisi bhi naye triage case par bina review chalaya ja sakta hai.
- B. **✅ Ye similar future work ke liye earned confidence deta hai, lekin final accountability
  Sam/team ke paas hi rehti hai — har naya case abhi bhi apni consequence ke hisaab se verify hona
  chahiye, khaas kar jab woh known-baseline se different ho.**
- C. Yeh sirf ek coincidence hai, kuch bhi prove nahi karta.
- D. Ab Sam is category ke liye ek written guarantee de sakta hai stakeholders ko.

**Sahi jawab: B** — Ek known-answer test pass karna similar-work ke liye confidence banata hai,
lekin accountability kabhi transfer nahi hoti — future cases, especially jo known-baseline se edge
case mein differ karte hon, phir bhi apni stakes ke hisaab se check hone chahiye. A confidence ko
guarantee samajhta hai. C valid signal ko discard karta hai — match hona bilkul useless nahi hai,
sirf transferable-guarantee nahi hai. D ek confidence level ko formal guarantee mein badal deta
hai jo overclaim hai.

### Q26
Thornbury Consulting ke associate, Ilya, ek 20-page market-entry report review kar raha hai jo
Claude ne ek single continuous session mein banayi. Executive summary kehta hai "we recommend
aggressive entry within Q1," lekin Section 6 (Risk Analysis) kehta hai "given regulatory
uncertainty, a phased Q2-Q3 entry is prudent." Ilya ko yeh sirf tab pata chala jab client ne
poocha "aap log kis quarter ki baat kar rahe hain?" Likely cause aur fix?

- A. Client confuse ho gaya, report theek hai.
- B. **✅ Bade single-pass document generation mein drift ka classic pattern — early sections baad
  ke sections se contradict kar sakte hain; fix hai section-by-section regenerate/reconcile karna
  ya final recommendation ko ek single explicit decision-point ke against verify karna.**
- C. Yeh sirf tone-inconsistency hai — voice ko standardize karna kaafi hai.
- D. Report ko formatting ke liye cross-references add kar ke fix kiya ja sakta hai bina content
  badle.

**Sahi jawab: B** — Ek bara document jo single pass mein banaya gaya, apni khud ki earlier
positions se contradict kar sakta hai (drift) — fix hai decomposition (section-by-section, phir
reconcile) ya kam-se-kam final recommendation ko ek explicit source-of-truth decision ke against
lock karna. C aur D dono symptom (contradiction) ko surface-level treat karte hain — voice
standardize karna ya cross-reference add karna underlying logical contradiction fix nahi karta.

### Q27
Amberline Retail ke associate, Nadia, Claude se ek supplier-contract clause explain karwati hai.
Claude confident answer deta hai. Nadia poochti hai "are you sure this is right?" aur Claude
jawab deta hai: "Yes, I'm confident this interpretation is correct based on standard commercial
practice." Yeh exchange Nadia ko is claim ki accuracy ke baare mein kya batata hai?

- A. Ab yeh verified ho gaya — Claude ne dobara confirm kiya.
- B. **✅ Taqreeban kuch nahi — models apne hi galat interpretation par bhi confidently reassure kar
  sakte hain; asal verification ek independent path (actual contract text, ya legal counsel) se
  aani chahiye.**
- C. Zyada confident hoga kyunki Claude ne "standard commercial practice" reference kiya.
- D. Reliable hai kyunki interpretation legal terms use karti hai jo model precisely samajhta hai.

**Sahi jawab: B** — Self-reported confidence — chahe woh reference bhi include kare ("standard
practice") — koi naya independent evidence nahi hai; woh wahi model se ek doosra confident-sounding
statement hai. C aur D dono confidence ki "sound quality" (reference, legal-vocabulary) ko
accuracy ka proxy maante hain, jabke asal contract text ke against check hi reliable path hai.

### Q28 — Multiple response (select TWO)
Ridgeline Manufacturing ke associate ko sikhaya gaya hai ke high-stakes work ke liye "cross-model
checking" tab hi kaam karta hai jab conditions sahi hon. Kaunse DO statements is technique ke
correct use ko reflect karte hain?

- A. **✅ Ek doosri **model family** (jaise Claude ke sath ChatGPT ya Gemini) se same rubric par
  independently check karwana — kyunki alag training data/teams ke blind spots differ karte hain.**
- B. Do Claude models (jaise ek fast-tier aur ek flagship-tier) ko ek doosre ke output check karne
  dena, kyunki dono "alag models" hain.
- C. **✅ Yaad rakhna ke teeno model families kabhi kabhi same cheez par wrong ho sakte hain —
  legal/medical/financial/real-person claims ke liye yeh sirf ek progress signal hai, human expert
  hi final check hai.**
- D. Cross-model check pass hone ko final proof maan lena, kisi bhi domain ke liye.

**Sahi jawab: A aur C** — Genuine cross-check ke liye alag company/family chahiye (alag training
data se alag blind spots), aur high-stakes claims ke liye yeh technique sirf ek additional signal
hai — kabhi bhi human-expert-level guarantee nahi. B galat hai kyunki ek hi company ke do models
(dono Claude) same family hain — unke habits/blind spots kaafi overlap kar sakte hain, yeh
independent check nahi. D overclaim hai jo technique ki apni limitation ignore karta hai.

### Q29
Castellane Legal ke associate, Ruth, ek regulated financial-disclosure draft receive karti hai jo
Claude ne banaya. Deadline aaj shaam hai. Ruth ke paas 2 options hain: (a) poora document line-by-
line review karna source figures ke against, jismein 3 ghante lagenge, ya (b) do random paragraphs
spot-check karna jismein 20 minutes lagenge. Kaunsa approach appropriate hai?

- A. Spot-check (b) kaafi hai — Claude generally accurate hota hai.
- B. **✅ Full line-by-line review (a) zaroori hai — regulated, high-stakes financial disclosure
  content ko kisi bhi use se pehle qualified insaan se source figures ke against poori tarah check
  hona chahiye, spot-checking is stakes-level ke liye insufficient hai.**
- C. Koi bhi review na karo agar deadline tight hai — Claude ki confidence par bhroasa karo.
- D. Sirf woh paragraphs check karo jo "complicated lagte hain," baaki skip karo.

**Sahi jawab: B** — Regulated financial disclosure top-of-the-ladder stakes hai — verification
effort ko poora scale karna chahiye, deadline pressure ke bawajood. A aur D dono partial-review
approaches hain jo is stakes-level ke liye insufficient hain — ek unchecked paragraph mein hi
material error ho sakta hai. C sabse risky hai, deadline pressure ko diligence chhodne ka reason
banana.

### Q30
Falkland Shipping ke associate, Otis, ek 35-page charter-party contract ka summary Claude se
receive karta hai. Summary mein key obligations aur ek specific demurrage-rate clause hai. Otis
isay account-team ko forward karne se pehle kya karna chahiye?

- A. Trust karo agar summary coherent aur well-organized lagta hai.
- B. **✅ Summary ke key obligations aur dates (khaas kar demurrage-rate figure) ko actual contract
  clauses ke against directly check karo.**
- C. Claude se dobara summarize karwao aur dono summaries compare karo.
- D. Claude se summary ko khud rate karne ko kaho (1-10) aur 8+ ho to forward karo.

**Sahi jawab: B** — Summarized source ke key claims (khaas kar numeric/date-specific obligations)
original document ke against verify hone chahiye — coherence accuracy ka proxy nahi hai. C same
model se dobara summarize karwana wahi systematic misreading repeat kar sakta hai jo pehli baar
hui thi — yeh independent verification nahi. D self-rating unreliable signal hai jo A/C jaisa hi
trap hai — model apne kaam ko khud grade kar raha hai.

### Q31
Meridian Health Network ke associate, Zara, ek patient-education handout draft kar rahi hain jo
Claude ne banaya common cold vs flu symptoms differentiate karne ke liye — general public ke liye,
diagnostic use ke liye nahi. Content accurate hai aur ek clear "see a doctor if symptoms worsen"
disclaimer bhi hai. Kaunsa evaluation lens sabse appropriate hai?

- A. Yeh automatically Domain-6 "inappropriate use" hai kyunki healthcare topic hai.
- B. **✅ Yeh general-public educational content hai (fully-appropriate tier ke qareeb) bashart
  accuracy verified ho aur "diagnose/treat" jaisi language avoid ho — stakes ek individual patient
  ke actual diagnosis se kaafi kam hai, isliye standard accuracy-check kaafi hai, full clinical
  sign-off zaroori nahi.**
- C. Content ko turant reject karo — koi bhi health-related AI content banana chahiye hi nahi.
- D. Sirf disclaimer ki wording check karo, symptom-facts ko skip kar do.

**Sahi jawab: B** — Stakes-based judgment yahan zaroori hai: general educational content
(diagnostic decision nahi bana raha) standard fact-accuracy verification maangta hai, na ke ek
individual-patient-diagnosis jaisi full clinical-review ladder. A ek blanket rule hai jo topic ko
stakes se confuse karta hai — "healthcare-adjacent" har cheez automatically inappropriate nahi
hoti. C overcautious/absolutist hai bina actual risk assess kiye. D incomplete hai — disclaimer
theek hai lekin underlying symptom-facts ka accuracy check bhi zaroori hai.

### Q32
Cobalt Systems ke associate, Marco, ek internal IT-policy FAQ Claude se banwata hai. FAQ common
cases (password reset, VPN access) achhi tarah cover karta hai lekin ek specific exception jo
Marco ne apne prompt mein explicitly mention ki thi — "contractors on 90-day badges need a
different renewal process" — FAQ mein kahin nahi hai. Evaluation lesson?

- A. FAQs edge cases cover nahi kar sakti, yeh normal hai.
- B. **✅ Completeness check mein explicitly-stated requirements/edge cases dhoondhna shamil hai,
  sirf obvious/common content nahi — jo cheez Marco ne khud naam li thi woh sabse zyada checkable
  aur sabse zyada important missing item hai.**
- C. Zyada length maango taake sab kuch cover ho jaaye.
- D. Accept kar lo — contractor-case rare hai, priority nahi.

**Sahi jawab: B** — Jab associate ne khud kisi specific requirement ka naam liya ho prompt mein,
uska output mein missing hona sabse easily-caught aur sabse serious completeness gap hai —
explicitly-named cheezein "obvious content" se zyada scrutiny deserve karti hain, kam nahi. A ek
excuse hai jo checking ko avoid karta hai. C length badhana guarantee nahi deta ke specific
named item include hoga. D "rare" hona relevance ko kam nahi karta jab yeh explicitly requested
tha.

### Q33
Union Farmers Bank ke associate, Priscilla, ek loan-covenant summary receive karti hai jismein
Claude "the borrower's debt-to-equity ratio must not exceed 2.5x, per Section 4.2" likhta hai.
Priscilla is figure ko internal risk memo mein use karna chahti hai jo loan-committee ko jaayega.
Sabse defensible verification step?

- A. **✅ Section 4.2 ko actual loan agreement mein khol kar exact ratio aur threshold confirm
  karo.**
- B. Claude se poocho "is this the exact number from Section 4.2?" aur uske "yes" par trust karo.
- C. Dobara summarize karwao aur dekho same number aata hai ya nahi.
- D. 2.5x ko "round number" maan kar accept karo kyunki loan covenants aksar round numbers use
  karte hain.

**Sahi jawab: A** — Independent authoritative source (actual agreement text) ke against direct
check hi reliable hai — yeh committee-facing risk memo mein jaane wala number hai, stakes high
hain. B model se apne hi claim ki confirmation maangna hai (self-referential, independent nahi).
C regeneration wahi systematic misreading repeat kar sakta hai. D ek heuristic guess hai jo koi
actual verification nahi — "round number lagna" ka correctness se koi zaroori connection nahi.

### Q34 — Multiple response (select TWO)
Kaunse DO signs strongest indicate karte hain ke ek Claude-generated output ko human review
chahiye pehle use hone se, chahe output "acha likha hua" lage?

- A. **✅ Output ek irreversible ya mushkil-se-undo external action/decision ko directly feed karega
  (jaise ek signed client communication, ek regulatory filing).**
- B. Output ek internal brainstorm hai jo aap khud se hi further edit/discard karenge.
- C. **✅ Output regulated ya specialist-judgment domain (legal, medical, financial-disclosure) se
  related hai jahan ek qualified professional accountable hai.**
- D. Output lamba hai (500+ words).

**Sahi jawab: A aur C** — Irreversibility/high-stakes-external-action aur regulated/specialist
domains dono top-of-ladder review triggers hain. B ek low-stakes, self-controlled context hai jo
review ki zaroori nahi banata (aap khud hi editor hain). D length koi risk-signal nahi hai — ek
chhota output bhi high-stakes ho sakta hai (jaise ek one-line pricing confirmation), aur ek lamba
output low-stakes ho sakta hai.

### Q35
Whitmore Nonprofit ke associate, Kojo, ek grant-report draft ke do versions banata hai — ek 400-
word concise version, ek 1,800-word detailed version. Dono factually equally accurate hain. Board
meeting mein 10 minutes allotted hain is item ke liye, lekin funder ki formal reporting requirement
mein "comprehensive narrative" maanga gaya hai. Kaunsa version use karna chahiye, kaise decide?

- A. Hamesha detailed version — zyada information hamesha safe hai audit ke liye.
- B. **✅ Board presentation ke liye concise version (10-min slot, decision-oriented audience),
  funder submission ke liye detailed version (formal requirement explicitly "comprehensive" maangta
  hai) — dono audiences/purposes alag hain, isliye ek hi version dono jagah fit nahi baithega.**
- C. Hamesha concise version — boards busy hote hain.
- D. Jo bhi Claude recommend kare use follow karo.

**Sahi jawab: B** — Fit-to-purpose aur audience decide karti hai, aur is case mein dono outputs ki
zaroorat hai kyunki dono audiences/requirements genuinely different hain — koi ek blanket "hamesha
X" rule (A ya C) dono contexts ko sahi serve nahi karega. D judgment Claude ko de deta hai jab
Kojo ke paas khud dono audiences ka context hai jo model ke paas nahi.

---

## Domain 3 — Product and Model Selection (Q36–Q47)

### Q36 (official-style, reworded scenario)
Everline Support ke ops lead, Delia, roz 4,000+ short customer-reply drafts generate karwati hain
(order-status, return-policy jaise routine replies) jahan turnaround-speed aur per-reply cost
matter karte hain, deep multi-step reasoning nahi. Woh currently sabse flagship-tier model use kar
rahi hain "quality ke liye." Monthly bill unexpected high hai aur latency bhi complaints la rahi
hai. Best fix?

- A. Flagship model rakho, lekin sab non-essential product features disable kar do cost bachane ke
  liye.
- B. **✅ Ek faster, lower-cost (economy/fast-tier) model par switch karo jo high-volume,
  straightforward drafting ke liye suited hai; flagship-tier ko un rare replies ke liye reserve
  karo jinhe genuinely multi-step judgment chahiye.**
- C. Kisi doosre AI vendor par switch kar jao cost kam karne ke liye.
- D. Volume kam karne ke liye replies ko batch kar ke din mein ek baar bhejo.

**Sahi jawab: B** — Model selection ko task-requirements se align karna: high-volume, low-
complexity kaam fast/cheap-tier ke liye designed hai; flagship-tier hard, judgment-heavy kaam ke
liye reserve hota hai. A cost symptom ko galat lever se address karta hai — features disable karna
model-tier mismatch fix nahi karta. C ek unrelated, disruptive move hai jab tier-switch hi kaafi
tha. D customer-facing latency ko aur bhi bigaarta hai (replies delay ho jaayenge) bina underlying
cost-issue solve kiye.

### Q37
Ashfield Analytics ke naye associate, Rio, apne senior se poochta hai: "Model names itni jaldi
badalte hain, main kya seekhun taake obsolete na ho jaun?" Senior kya sikhata hai?

- A. Har naye model-release ke exact naam yaad karo, woh hi asal skill hai.
- B. **✅ Underlying 3-level trade-off pattern seekho — fast/default tier (routine kaam), thinking/
  reasoning mode (multi-step analysis), heavy flagship tier (hardest, sabse expensive/slow kaam) —
  yeh pattern names/versions badalne ke bawajood zinda rehta hai.**
- C. Sirf ek hi model hamesha use karo taake confusion na ho.
- D. Naam matter nahi karte — koi bhi model kisi bhi task ke liye equally theek hai.

**Sahi jawab: B** — Vendors apne model line-ups ko consistently isi fast/thinking/flagship trade-
off pe arrange karte hain — naam/version numbers change hote hain lekin yeh pattern-based judgment
transferable rehta hai. A ek fragile approach hai jo har naye release par obsolete ho jaayega. C
task-fit ko ignore karta hai — "ek hi model hamesha" cost/quality dono mein galtiyan create karega.
D galat hai — model tiers genuinely different capability/cost trade-offs rakhte hain.

### Q38
Corvid Analytics ke associate, Han, ek complex multi-constraint supply-chain trade-off analysis
karwa rahe hain jismein interacting variables (cost, lead-time, vendor-reliability, currency risk)
ek sath weigh karne hain. Woh confused hain ke extended thinking/reasoning mode on karein ya
default fast mode. Sahi judgment?

- A. Default fast mode use karo — thinking mode sirf coding tasks ke liye hai.
- B. **✅ Extended thinking/reasoning mode justify hai — yeh task multi-step, interacting-constraint
  reasoning maangta hai jahan model ko answer se pehle "plan" karna faida deta hai.**
- C. Thinking mode kabhi use mat karo — hamesha zyada expensive hota hai bina kisi benefit ke.
- D. Task ko 50 chhote independent sub-tasks mein tod do taake thinking mode ki zaroorat na pare.

**Sahi jawab: B** — Yehi exact use-case hai jahan reasoning mode value add karta hai — multi-step,
interacting-constraint analysis jahan galat sequencing ek galat conclusion de sakta hai. A ek galat
generalization hai — thinking mode coding tak limited nahi. C ek absolutist claim hai jo is
scenario ke liye galat hai — yahan trade-off genuinely worth hai. D artificially task ko itna
fragment karta hai ke interacting constraints (jo ek sath weigh honi chahiye) alag-alag ho jaati
hain — yeh depth ko hi kho deta hai jo task maangta hai.

### Q39
Palmerston Advisory ke associate, Ingrid, roz subah har naye client-chat mein wahi cheez paste
karti hain: firm ka brand-voice guide, teen standard disclaimers, aur ek client-list jo hamesha
relevant hoti hai is engagement ke liye. Yeh ek hi ongoing engagement hai jo mahino chalega. Best
move?

- A. Paste karte raho — yeh reliable aur transparent tareeka hai.
- B. **✅ Ek Project banao is engagement ke liye jismein yeh brand-voice guide, disclaimers, aur
  client-list bataur knowledge/instructions daal do — taake har naya chat automatically inherit
  kare, dobara paste na karna pade.**
- C. Sab kuch ek single "mega-prompt" template mein combine karo jo har baar copy-paste ho.
- D. Har baar naya chat use karna chhod do — ek hi endless conversation mein sab kaam karo.

**Sahi jawab: B** — Recurring, stable, engagement-scoped context ka classic Project use-case hai —
ek jagah configure karo, har chat automatically inherit kare. A aur C dono manual-repetition ko
continue karte hain (bas ek combined-template C mein thoda kam friction ke sath) — dono Project
ke automatic-inheritance faide ko miss karte hain. D lambi single-conversation approach apna
context-degradation risk laata hai (quality girne lagti hai jab session bohat lambi ho jaaye) jo
alag masla create karta hai.

### Q40
Sundale Architecture ke associate, Petra, ek 12-page design-proposal client ke sath live iterate
kar rahi hain — woh chahti hain ke Claude ek editable canvas mein draft rakhe jise dono baar-baar
refine karein, section highlight karein, aur version compare karein, poori conversation ke bahar
bhi reference ho sake. Sabse clear product-feature fit?

- A. Ek quick single chat message jahan poora proposal ek jawab mein aaye.
- B. **✅ Ek Artifact — jismein 12-page proposal persist rahe, dono iteratively refine kar sakein
  bina har baar poora text chat mein retype kiye.**
- C. Ek yes/no confirmation question Claude se poochna.
- D. 20 alag proposal-ideas brainstorm karwana bina structure ke.

**Sahi jawab: B** — Substantial, iteratively-co-edited, standalone content (jo baar-baar refine
hoga aur reference-worthy hai) Artifact ka classic use-case hai. A ek-baari generation hai jo
iteration ko support nahi karta easily. C aur D dono completely different task-types hain
(confirmation, brainstorming) jo is scenario se match nahi karte.

### Q41
Kestrel Wealth ke associate, Dario, teen features confuse kar raha hai: account-level custom
instructions, memory, aur Projects. Woh poochta hai: "In teeno mein farq kya hai, ek line mein?"
Sabse accurate distinction?

- A. Instructions scoped-work ke liye hain, memory rules ke liye, Projects context ke liye —
  teeno interchangeable.
- B. **✅ Custom instructions stable, global rules ke liye hain ("hamesha, har jagah sach"); memory
  evolving, self-updating context ke liye hai jo Claude time ke sath naam leta hai; Projects ek
  specific scoped body-of-work ke liye hain (files + instructions jo sirf us workspace mein
  always-on hain).**
- C. Teeno bilkul same mechanism hain, bas alag naam hai.
- D. Memory stable rules ke liye hai, Projects baaki sab cheezon ke liye.

**Sahi jawab: B** — Yeh teeno genuinely different scopes/purposes serve karte hain: global-always
(instructions), evolving-and-self-updating (memory), scoped-workspace (Projects). A confusing/
circular hai aur "interchangeable" keh kar asal distinction hi discard kar deta hai. C aur D dono
in mechanisms ke actual roles ko galat map karte hain.

### Q42
Complete karo: "Ek Skill baar-baar wahi kaam ___ karne ka tareeka store karta hai; ek Connector
Claude ko doosri app tak ___ deta hai; ek Project ek workspace ke liye files + instructions ko
___ rakhta hai."

- A. **✅ kaise; access; always-on**
- B. kya; permission; scoped
- C. kaunsa; retrieval; global
- D. kab; memory; persistent

**Sahi jawab: A** — Skill = "kaise" (procedure/how-to, on-demand jab request match kare); Connector
= access (Claude aapke apne permissions inherit karta hai us app tak); Project = ek workspace ke
liye always-on context. B, C, D har ek in teen mechanisms ke core purpose ko subtly misdescribe
karte hain (jaise Connector "permission" nahi deta, woh existing permission ko access mein convert
karta hai; Skill "retrieval" nahi hai; Project "global" nahi, "scoped" hai).

### Q43
Vantage Group ke CEO ko ek one-time, board-level strategic-pivot memo chahiye jahan nuance aur
correctness paramount hain — is memo ka volume literally "one" hai (ek hi baar likha jaayega, kabhi
reuse nahi hoga). Associate, Malik, confuse hai kyunki flagship-tier model normally "high volume ke
liye zyada expensive" maana jaata hai. Sahi choice?

- A. Sabse fast/cheapest model use karo, kyunki volume sirf ek hai to cost matter nahi karta.
- B. **✅ Sabse capable (flagship) model use karo — volume-of-one par total cost negligible hai
  (chahe per-token rate zyada ho), aur quality/nuance yahan paramount hai, exactly wahi scenario
  jahan flagship-tier apna case banata hai.**
- C. Jo bhi default model ho wahi use karo, kisi decision ki zaroorat nahi.
- D. Do cheaper-tier drafts banao aur manually merge kar do.

**Sahi jawab: B** — "Volume-of-one, stakes-high" bilkul opposite scenario hai us se jahan cost-
per-token matter karta hai (high-volume) — yahan total dollar cost trivial hai chahe rate zyada
ho, aur quality ka premium justify hai. A cost ko ek wrong dimension (per-unit rate) se judge karta
hai jab total-cost hi asal relevant metric hai is context mein. C default ko blindly follow karna
task-requirement ignore karta hai. D manual-merge complexity add karta hai bina flagship-tier ki
coherent single-pass quality ke barabar guarantee ke.

### Q44
Northbridge Legal ke associate, Wendy, ek 4-din purani conversation mein Claude se kaam kar rahi
hain jismein 15+ back-and-forth revisions ho chuke hain ek contract-review par. Ab Claude ek
earlier-agreed decision (ke "clause 8 ko as-is rakhna hai") ko contradict karta hai aur usay
dobara flag karta hai jaise pehli baar dekh raha ho. Best fix?

- A. Claude ko kaho "please remember our earlier decisions better."
- B. **✅ Key decisions (jaise "clause 8 finalized, as-is") summarize kar ke ek fresh chat mein
  continue karo, aur stable/reusable context (jaise standard clause-review checklist) ko Project
  mein move karo taake future engagements bhi inherit karein.**
- C. Wahi conversation chalte raho — Claude eventually recover kar lega.
- D. Model ko ek doosre vendor ke model se switch karo.

**Sahi jawab: B** — Yeh context-overload ka classic symptom hai (lambi conversation, quality/
consistency girna) — sahi response hai restart (fresh session with a summary) aur/ya persist
(stable content Project mein). A ek instruction hai jo underlying context-window mechanism ko
change nahi kar sakta. C problem ko worsen hone dega. D unrelated fix hai — yeh context-management
issue hai, model-choice issue nahi.

### Q45
Kaunsa statement sabse accurately CCAO-F-level model-selection judgment reflect karta hai?

- A. Hamesha sabse top-tier/flagship model use karo — quality kabhi galat move nahi hoti.
- B. **✅ Model ko task ke requirements se match karo: simple, high-volume kaam ke liye fast/cheap-
  tier; complex, high-stakes, ya multi-step-reasoning kaam ke liye capable/flagship-tier — aur is
  decision ko har naye task ke liye consciously banao, habit se nahi.**
- C. Hamesha sabse cheapest/fastest model use karo aur phir sirf jab output kharab lage tab
  iterate karo.
- D. Model choice sirf branding ka masla hai, cost/quality par meaningfully asar nahi daalti.

**Sahi jawab: B** — Yeh model-tier judgment ka core thesis hai jo poore Domain 3 mein reflect hota
hai. A cost/latency ko routine kaam par unnecessarily waste karta hai. C reverse-mistake hai —
har task ko cheapest-first treat karna high-stakes tasks par risk create karta hai jahan galat
output expensive-se-discover ho sakta hai. D factually galat hai — tiers genuinely different
performance/cost trade-offs rakhte hain.

### Q46
Fairhaven Institute ke associate, Callum, ko ek multi-source synthesised literature review chahiye
— 15+ academic aur industry sources ke across, citations ke sath — jo ek grant-proposal ko support
karega. Best feature fit?

- A. Ek plain single chat message jahan sab kuch ek jawab mein maang liya jaaye.
- B. **✅ Research/deep-research mode (ya extended-thinking-with-sources) use karo taake multi-
  source synthesis ho, phir har citation ko independently verify karo submit karne se pehle.**
- C. Sirf ek Artifact banao bina research-mode ke.
- D. Ek Project banao bina koi knowledge source attach kiye.

**Sahi jawab: B** — Multi-source synthesis-with-citations exactly research/deep-research mode ka
designed use-case hai — lekin citations phir bhi verify honi chahiye (Domain 2 overlap) submit se
pehle. A single-message approach ek genuine multi-source research task ko undersell karta hai. C
Artifact sirf presentation-container hai, research-capability nahi deta. D ek empty Project sirf
workspace banata hai, actual multi-source synthesis nahi karta.

### Q47 — Multiple response (select TWO)
Marchetti Foods ke associate, Luca, ek 6-hafte purani, 200+ message-lambi Project-conversation mein
kaam kar rahe hain jahan responses hal hi mein "off-topic" aur "shallow" feel ho rahe hain. Kaunse
DO factors sabse strongly suggest karte hain ke naya chat shuru karna chahiye (Project ke andar hi,
fresh conversation)?

- A. **✅ Conversation bohat lambi ho chuki hai aur answers noticeably degrade ho rahe hain
  (context-overload ka classic symptom).**
- B. Luca thodi alag phrasing try karna chahta hai isi topic ke liye.
- C. **✅ Topic ab poori tarah unrelated ek doosre matter par shift ho gaya hai jo is conversation ki
  original thread se disconnect hai.**
- D. Claude ne 2 messages pehle ek chhoti typo ki jo Luca ne already khud correct kar diya.

**Sahi jawab: A aur C** — Lambi conversation ka quality-degradation aur ek genuinely unrelated
topic-shift dono naya-chat-shuru-karne ke strong, legitimate reasons hain. B sirf phrasing change
karna hai — usi chat mein bhi ho sakta hai, naya chat zaroori nahi. D ek already-resolved chhoti
galti hai jo continuing conversation ko justify karti hai, restart ko nahi.

---

## Domain 4 — Workflow Integration and Solution Design (Q48–Q63)

### Q48
Palisade Logistics ke ek invoice-approval workflow mein 4 steps hain: (1) invoice se approval-
request summary draft karna, (2) contract-terms se deviate karne wali invoices ko review ke liye
flag karna, (3) ek manager ka final sign-off, (4) approved payment ko ledger mein post karna aur
bank ko instruct karna transfer ke liye. Associate, Reza, sochte hain ke kaunsa step Claude ke
end-to-end ownership ke liye sabse kharab fit hai. Sahi jawab?

- A. Step 1 (summary draft karna) — yeh drafting hai, ownership ke liye bilkul unfit.
- B. Step 2 (deviation flag karna) — pattern-matching hai, AI ke liye unsuitable.
- C. **✅ Step 4 (payment post karna aur bank ko instruct karna) — yeh ek irreversible, system-of-
  record financial action hai; iski reversibility bohat kam hai aur accountability kisi insaan ke
  paas honi chahiye, isliye yeh deterministic systems + human authorization maangta hai.**
- D. Step 3 (manager sign-off) — yeh already human hai to "fit" ka sawal hi nahi.

**Sahi jawab: C** — Reversibility aur stakes dono is step ko human-plus-deterministic-system
territory mein rakhte hain — ek galat bank-transfer instruction undo karna bohat mushkil/costly
hai. A aur B dono actually reasonable AI-appropriate ya collaborative steps hain (drafting aur
flagging dono AI ke strengths hain, human judge karta hai) — inhe "unfit" kehna galat hai. D
sawal ko hi galat samajhta hai — sawal yeh nahi ke step already human hai, balke kaunsa step AI ko
diya jaana chahiye hi nahi.

### Q49
Ferro Insurance ke operations lead, Sana, Claude se poochta hai: "Poore claims-intake process ko
AI ko de do." Associate, Yusuf, is request ko handle kar raha hai. Sabse pehla defensible move?

- A. Poora flow turant automate kar do — Sana leadership hai, unki request follow karo.
- B. **✅ Pehle process ko step-by-step map karo (eligibility, ownership, implementation — teen
  alag decisions), phir Claude ko un high-toil, human-reviewed steps par daalo jahan reversibility/
  stakes/accountability allow karti hain, results measure karo, phir hi bade redesign par consider
  karo.**
- C. Decline kar do — claims-intake automate nahi ho sakta.
- D. Kuch bhi test kiye bina poore process ko AI ke around redesign kar do.

**Sahi jawab: B** — Yeh delegation-map ka poora sequence hai: pehle map karo, phir per-step
ownership decide karo (three criteria se), phir prove-then-expand. A ownership-analysis ko skip
kar deta hai sirf seniority ki wajah se. C ek absolutist refusal hai jab actually kuch steps
genuinely AI-appropriate ho sakte hain. D redesign ko augment-phase se pehle try karta hai, jo
book ka explicit ordering violate karta hai (augment pehle, redesign sirf value-proven hone ke
baad).

### Q50
Halden Manufacturing ke associate, Priti, ek workflow-automation proposal se pehle apna checklist
banati hain. Kaunse DO sawal delegation-map ke "Ownership" layer ke teen criteria ko sabse
directly test karte hain?

- A. "Kaunsa model cheapest hai?" aur "Kitna time lagega implement karne mein?"
- B. **✅ "Agar galat ho jaaye, kya isay undo kiya ja sakta hai (reversibility)?" aur "Worst-case
  mein ek galti ki cost kya hai, aur yeh decision asal mein kiske paas hai (stakes +
  accountability)?"**
- C. "Client ko AI pasand hai?" aur "Budget available hai?"
- D. "Pichli baar jab humne yeh try kiya to kaisa gaya tha?"

**Sahi jawab: B** — Yeh directly teen ownership-criteria (reversibility, stakes, accountability)
ko target karta hai. A cost/timeline sawal hain jo implementation-layer ke liye relevant ho sakte
hain lekin ownership decide nahi karte. C stakeholder-preference/budget hai, ownership-criterion
nahi. D — ye ek trap hai jo book explicitly warn karti hai: "past performance kaise gaya" ownership
ka criterion nahi hai; ek step jo pichli baar achha gaya woh phir bhi high-stakes/irreversible ho
sakta hai aur human-owned rehna chahiye ("halo delegation" ka trap yehi hai).

### Q51
Corrigan Advisory ke associate, Femke, ek Claude-based weekly-reporting workflow client ko pitch
kar rahi hain. Client excited hai aur poochta hai "kya yeh fully autonomous hoga?" Sabse
professionally-sound response?

- A. "Haan, bilkul fully autonomous hoga, aapko kuch nahi karna padega."
- B. **✅ "Yeh weekly draft ka pehla-pass time 2 ghante se 20 minute tak le aayega, consistent
  structure ke sath — lekin ek named team-member final review aur sign-off karega har baar; yeh
  system-of-record nahi hai, aur data restrictions bhi apply hongi."**
- C. Limitations mention mat karo taake client ka confidence na tootay.
- D. Sirf time-savings emphasize karo, review-requirement ko chhupa do.

**Sahi jawab: B** — Concrete value (specific numbers) + honest limits (review needed, not-system-
of-record) + named human-checkpoint — yeh sab combine kar ke ek defensible, trust-building claim
banate hain. A overclaim hai jo pehli visible galti par trust todega. C aur D dono gate ko chhupate
hain — book explicitly warn karti hai ke stakeholders AI-workflows par zyada trust karte hain jab
human checkpoint explicit ho, kam nahi.

### Q52
Oakmont Digital ke ek client ek proposed workflow maangte hain jismein ek custom API integration,
ek unattended cross-tool agent (jo raat ko khud chalega bina supervision), aur ek naya custom
connector build karna shamil hai. Associate, Deja, is request ko kaise handle kare?

- A. Associate ke scope mein poori tarah aata hai — jitna ho sake khud implement karo.
- B. **✅ Yeh technical-build scope (API integration, unattended agent, custom connector) Claude
  Architect/Developer ko escalate karna chahiye; Deja use-case aur business-process design mein
  involved reh sakti hai, lekin actual build associate-scope se bahar hai.**
- C. Try karo aur sirf jab fail ho jaaye tab escalate karo.
- D. Yeh sirf ek governance/data-privacy sawal hai, escalation ki zaroorat nahi.

**Sahi jawab: B** — API integration, unattended agentic automation, aur custom connector-building
teeno explicitly Associate-scope se bahar, Architect/Developer territory hain — escalate karo lekin
process-ownership mein involved raho. A scope-boundary ko galat samajhta hai. C waste of time/risk
create karta hai — kuch cheezein (unattended agent build) shuru se hi scope-mismatch hain, fail
hone tak wait karna unnecessary risk hai. D sirf ek dimension (governance) dekhta hai jab asal
issue technical-build-complexity bhi hai.

### Q53
Thistledown Nonprofit ke associate, Om, ek process-map bana rahe hain jahan ek donor-outreach
step hai. Sahi principle jo decide karta hai ke Claude yahan kahan insert ho?

- A. Claude ko donor se final "ask" conversation lead karne do, kyunki woh persuasive likh sakta
  hai.
- B. **✅ Claude ko repetitive drafting/synthesis toil (jaise donor-history summarize karna, pehla
  outreach-email draft banana) hataane do, jabke ek named human relationship-level decisions
  (personal ask, tone-sensitive follow-up) apne paas rakhe.**
- C. Claude seedha CRM (system of record) mein donor-contact-status likh de bina kisi review ke.
- D. Review step ko eliminate kar do taake process fast ho.

**Sahi jawab: B** — Yeh "augment" ka core definition hai — repetitive toil hatao, human decision-
points (relationship-sensitive interactions) rakho. A human-judgment/empathy-maangne-wale kaam ko
AI ko de deta hai. C system-of-record write ko bina review ke deta hai, jo unsafe hai. D review-
step hatana efficiency ke naam par ek zaroori control ko discard karta hai.

### Q54
"Augment" ka sabse accurate matlab kaunsa hai, jaisa is domain mein use hota hai?

- A. Poore process ko AI ke around se-scratch redesign karna.
- B. **✅ Ek specific existing step ko tez/behtar karna without changing the overall process shape —
  jaise "AI drafts, human reviews and sends" — bina process ki underlying structure ko replace
  kiye.**
- C. Process se humans ko systematically hatana.
- D. Process mein naye extra steps add karte jaana jab tak woh "AI-native" na lage.

**Sahi jawab: B** — Augment ka matlab hai ek existing step ko within-process speed-up karna, na ke
process ko redesign/replace karna — yeh redesign se explicitly alag hai (jo bade structural changes
hote hain, sirf tab jab augmenting ne value already prove kar di ho). A redesign ki definition hai,
augment ki nahi. C over-delegation ki taraf le jaata hai jo augment ka opposite hai. D
unnecessary complexity add karta hai, augment ka goal nahi hai.

### Q55
Brannigan Retail ke client kehta hai: "Hum chahte hain AI hamara customer-support poora handle
kare." Associate, Tobi, ka sabse defensible next step?

- A. Ek full autonomous support-agent design turant propose karo, client ki excitement capture
  karne ke liye.
- B. **✅ Actual support-workflow analyse karo: ticket-types, volumes, existing decision-points,
  current human-owners, aur client ka "handle" se kya matlab hai — phir propose karo Claude
  specifically kahan fit hota hai (aur kahan nahi).**
- C. Sabse capable/flagship model recommend karo bina workflow samjhe.
- D. Poocho ke woh kis competitor se worried hain, aur unki strategy copy karo.

**Sahi jawab: B** — Vague request ("handle karo") ko concrete task-definition mein todna zaroori
hai — 5 settled answers (kya, kiske liye, kitni baar, kis data se, kis format) pehle chahiye, model
ya architecture se pehle. A ek premature commitment hai jo scope/risk ko assess kiye bina ban jaata
hai. C model-choice ek downstream decision hai, workflow-analysis se pehle nahi aani chahiye. D
ek irrelevant tangent hai jo asal task-definition problem solve nahi karta.

### Q56
Kaunsa stakeholder-facing value-statement sabse defensible hai, ek analyst-augmentation workflow
ke liye?

- A. "Yeh analyst role ki zaroorat hi khatam kar dega."
- B. **✅ "Yeh weekly-report ke first-draft time ko significantly kam karega; analyst review aur
  final sign-off khud apne paas rakhega."**
- C. "Yeh error-free hoga, kabhi galti nahi karega."
- D. "Yeh review ki zaroorat hi khatam kar deta hai."

**Sahi jawab: B** — Concrete, honest, gate-explicit claim — value bhi bataata hai aur human-
checkpoint bhi retain karta hai. A, C, D teeno overclaim hain jo pehli visible mistake ya role-
security concern par trust tod denge — job-elimination promise, error-free guarantee, aur review-
elimination teeno defensible nahi hain.

### Q57
Sundown Media ke ek workflow mein 6 mahine se Claude sirf ek "draft karo, human review kare" step
mein augment kar raha hai — measured results consistently strong hain (time-savings verified,
error-rate low). Team ab consider kar rahi hai poore workflow ko AI-ke-around redesign karna. Kab
yeh appropriate hai?

- A. Turant kisi bhi naye workflow ke liye, maximum value capture karne ke liye.
- B. **✅ Jab augmenting ne value already prove kar di ho (jaisa is case mein), structural gain clear
  ho (redesign se genuinely naya faida milega, sirf incremental nahi), aur team apna kaam karne ka
  tareeka badalne ke liye ready ho.**
- C. Kabhi nahi — redesign hamesha bohat risky hota hai.
- D. Jab bhi client keh de "hum aur automation chahte hain," bina kisi aur criteria ke.

**Sahi jawab: B** — Yeh exact sequence hai jo book prescribe karti hai: prove-with-augmentation
first, phir redesign consider karo jab teeno conditions milein. A redesign ko premature bana deta
hai (bina proof ke). C ek absolutist "never" hai jo genuinely-earned redesign opportunities ko
ignore karta hai. D client-request akela sufficient criterion nahi hai — value aur team-readiness
bhi chahiye.

### Q58 — Multiple response (select TWO)
Rosewood Legal Services ke associate, Ines, apne workflow map mein "collaborative" steps (AI
produces, ek named person judges) identify kar rahi hain. Kaunse DO steps genuinely collaborative
hain, na ke "AI-appropriate" ya "human-retained"?

- A. **✅ Ek client-facing settlement-offer letter ka first draft banana, jise ek named paralegal
  review kare tone/completeness ke liye before an attorney signs it.**
- B. Firm ka internal style-guide ke against ek document ko auto-format karna (koi judgment
  involved nahi).
- C. **✅ Ek intake-form se case-summary banana jise ek attorney judge kare before deciding whether
  to take the case.**
- D. Ek final settlement ko sign karna aur client ko bhejna.

**Sahi jawab: A aur C** — Dono mein AI produce karta hai (draft/summary) aur ek named human
judge karta hai before it acts on anything — yeh collaborative ka definition hai. B "koi judgment
involved nahi" hone ki wajah se pure AI-appropriate hai, collaborative nahi (kisi ko judge karne ki
zaroorat nahi). D final sign-and-send ek irreversible decision hai jo khud accountability ka
core hai — yeh human-retained hai, "AI produces, human judges" wala pattern nahi (yahan koi AI-
produced draft judge nahi ho raha, yeh final commitment hai).

### Q59
Millbank Consulting ke ek stakeholder, dekh kar ke Claude-based reporting workflow consistently
achha kaam kar raha hai, ab is output ko "authoritative, system-of-record" ki tarah treat karne
lage hain — bina realize kiye ke woh abhi bhi ek draft/decision-support tool hai. Associate, Priya,
ko kya karna chahiye?

- A. Rehne do — stakeholder confidence build ho raha hai, use disturb mat karo.
- B. **✅ Expectation explicitly correct karo: outputs drafts/decision-support hain jinhe review
  chahiye; actual system of record kahin aur (jaise ERP/CRM) hai — is gap ko chhupana halo-
  delegation ka trigger ban sakta hai jahan future steps bhi bina justification ke AI ko diye jaane
  lagte hain.**
- C. Sirf appendix mein ek chhoti disclaimer add kar do bina baat kiye.
- D. Stakeholder ko batao "Claude usually correct hota hai," jo unki current understanding ko
  reinforce karta hai.

**Sahi jawab: B** — Jab tak stakeholder expectation correct nahi hoti, over-trust "halo delegation"
ki taraf le jaata hai — pichli baar achha gaya isliye zyada scope de dena bina fresh reversibility/
stakes/accountability check ke. A aur D dono is misconception ko active reinforce karte hain. C
passive hai — ek buried disclaimer conversation ki jagah nahi le sakta jo actively expectation
reset kare.

### Q60
Larkspur Ops ka ek working 6-prompt weekly workflow already reliably chal raha hai. Team optimize
karna chahti hai. Sabse sound approach?

- A. Aur review-steps add karo "just in case," chahe woh already-working steps par ho.
- B. **✅ Repeated prompts ko templates/Skills banao, stable recurring context ko Project mein move
  karo, aur agar quality hold kare to ek cheaper/faster model-tier try karo — sab teeno changes
  ko individually verify karte hue.**
- C. Turant sabse capable/flagship model par switch karo "safety" ke naam par bina koi problem
  observe kiye.
- D. Har prompt ko do baar chalao aur outputs compare karo taake "consistency" mile, har run par.

**Sahi jawab: B** — Yeh optimization ka sound pattern hai — configuration ko encode karo (Skills/
Project), aur cost-efficiency try karo bina quality-check hataye. A unnecessary friction add karta
hai jahan koi identified risk nahi thi. C ek unjustified cost-increase hai bina kisi quality-gap
identify kiye. D har run ko double karna cost double karta hai bina koi naya control add kiye —
yeh optimization nahi, waste hai.

### Q61
Solution-design context mein, Claude best kis role mein use hota hai — jab ek naya internal-tool
architecture decide karni ho?

- A. Final architecture-decision khud Claude se lena, bina human sign-off ke.
- B. **✅ Options aur trade-offs map karne, iterations draft/critique karne, aur assumptions
  pressure-test karne ke liye — jabke actual decision-making authority humans ke paas rehti hai.**
- C. Design-review process ko poori tarah replace karne ke liye.
- D. Final design ko approve karne ke liye, taake human-approval-step skip ho sake.

**Sahi jawab: B** — Solution-design mein Claude ki value exploration/critique/pressure-testing mein
hai, final-decision-authority mein nahi. A, C, D teeno decision-making/approval authority ko AI ko
de dete hain, jo accountability-transfer ka classic trap hai (accountability kabhi tool ko move
nahi hoti).

### Q62
Camborne Insurance ke associate, Nils, ek established, human-run underwriting-review workflow mein
Claude introduce karna chahte hain. Sabse low-risk entry-point kaunsa hai?

- A. Ek poora sub-process (jaise entire risk-scoring) turant replace karo.
- B. **✅ Ek high-toil, comparatively-low-risk step (jaise application-form ka summary banana) par
  Claude add karo, human review retained rakhte hue, phir measured results ke hisaab se scope
  expand karo.**
- C. Saara underwriting-data Claude se route karo taake "full context" mile.
- D. Claude ko core underwriting-system par write-access de do taake woh khud records update kar
  sake.

**Sahi jawab: B** — Yeh exact "augment-first, low-risk-step-first, prove-then-expand" pattern hai.
A high-risk sub-process ko turant replace karna galat sequencing hai. C aur D dono unnecessary,
premature scope-expansion hain (over-delegation) bina kisi step ki reversibility/stakes/
accountability establish kiye.

### Q63
Ek client Kingfisher Analytics ke associate, Dora, se ek workflow maang raha hai jismein ek
custom multi-agent orchestration system build karna hai jo scope se bahar hai. Dora ko chahiye:

- A. Waise bhi build karne ki koshish karo aur umeed rakho ke kaam ho jaayega.
- B. **✅ Clearly explain karo kya associate-scope mein hai kya nahi, aur technical build-work ko
  Architect/Developer ko route karo — jabke Dora khud use-case-definition aur business-process-
  design mein involved rehti hai poore engagement ke through.**
- C. Poori engagement decline kar do kyunki ek piece scope se bahar hai.
- D. Client ko batao yeh "impossible" hai, chahe technically Architect/Developer ke liye possible
  ho.

**Sahi jawab: B** — Scope-honesty + appropriate-escalation + continued-involvement (jahan
appropriate) hi correct pattern hai. A scope-mismatch ko ignore kar ke risk create karta hai. C
poori engagement discard karta hai jab sirf ek technical-piece escalate karni thi — overreaction.
D factually galat statement hai ("impossible" jab actually sirf associate-scope se bahar hai, kisi
aur role ke liye possible hai).

---

## Domain 5 — Configuration and Knowledge Management (Q64–Q75)

### Q64
Kaunsa Project-instructions set senior-level "specific, testable" standard ko sabse behtar meet
karta hai, ek client-reporting Project ke liye?

- A. "Be helpful, professional, and thorough in every response."
- B. **✅ "UK English mein likho; teen se zyada items ki har list ko bullets mein do; koi bhi
  statistic invent mat karo — sirf attached knowledge-files se cite karo; agar koi figure knowledge
  mein na mile, explicitly 'not in provided data' likho; audience non-technical client sponsors
  hai."**
- C. "Ek senior consultant ki tarah act karo, 20 saal ka experience."
- D. "Best practices follow karo aur industry standards maintain karo."

**Sahi jawab: B** — Har clause checkable/testable hai (language, format threshold, sourcing-rule,
explicit-gap-behavior, audience) — koi bhi output in criteria ke against verify ho sakta hai. A,
C, D teeno vague aspirations hain jo kisi specific output-shape ko guarantee nahi karte — inhe
"pass/fail" karna impossible hai.

### Q65
Northmoor Realty ke associate, Casper, decide kar rahe hain ke kya Project-instructions mein
daalna hai vs per-prompt mein. Sahi principle?

- A. Aaj ke specific listing ka address aur price Project-instructions mein daalo taake "hamesha
  available rahe."
- B. **✅ Stable rules — tone, format-defaults, target-audience, always/never-constraints — Project
  instructions mein; ek specific listing ka one-off detail current prompt mein.**
- C. Pichle draft par feedback ("shorten paragraph 2") ko Project-instructions mein permanently
  daal do.
- D. Ek one-off client-question ko Project instructions mein daal do taake future reference ho.

**Sahi jawab: B** — Instructions ka scope stable/recurring rules hai; transient, one-off details
current-prompt mein rehte hain. A, C, D teeno one-off/transient content ko galat jagah (permanent
instructions) daalte hain — is se instructions bloat ho jaate hain aur irrelevant/outdated content
future har chat mein inject hone lagta hai.

### Q66
Ashworth Reporting ke associate, Bea, ek client-reporting Project mein 40 loosely-related documents
upload kar deti hain — kuch 2 saal purane meeting-notes, kuch unrelated internal memos — "taake
Claude ke paas poora context ho." Outputs ab kam relevant/scattered feel ho rahe hain. Best advice?

- A. Aur bhi documents upload karo taake "full picture" mile.
- B. **✅ Authoritative, currently-relevant documents tak curate karo — bohat saara low-signal/
  outdated material retrieval ko dilute karta hai aur irrelevant context surface hone ka risk
  badhata hai.**
- C. 40 documents ko 40 alag Projects mein split kar do.
- D. Saara knowledge hata do aur sirf per-prompt context par rely karo.

**Sahi jawab: B** — Knowledge-management ka core lesson: volume quality ka substitute nahi hai —
curated, authoritative sources behtar retrieval dete hain low-signal bulk se. A masla worsen karta
hai. C over-engineering hai jo maintenance-burden badhata hai bina asal masla (curation) solve
kiye. D poore Project ki value discard karta hai jab asal fix sirf curation tha.

### Q67
Glendale Brands ka ek 6-mahine purana "Brand Voice" Project ab purani tagline aur discontinued logo
ka reference deta hai — brand refresh 3 mahine pehle hua tha. Root cause aur process-fix?

- A. Yeh model-regression hai — kisi doosre model par switch karo.
- B. **✅ Stale knowledge/instructions — jab bhi brand-assets change hote hain, Project ki sources
  aur instructions update honi chahiye, aur ek named owner assign hona chahiye jo yeh maintenance
  schedule/change-events par karta rahe.**
- C. Yeh prompt-problem hai — associates ko lambi, zyada detailed prompts likhni chahiye har baar.
- D. Kuch bhi galat nahi — Claude ko dobara poochne se sahi jawab mil jaayega.

**Sahi jawab: B** — Yeh exact stale-configuration failure mode hai jo silently degrade hota hai
("used to work" pattern) — fix hai maintenance-process (owner + change-triggered updates), na ke
model ya prompt. A aur C dono galat root-cause identify karte hain — masla configuration-staleness
hai, model-capability ya prompt-quality nahi. D masla ko ignore karta hai jab systematic fix
zaroori hai.

### Q68
Jasper Freight ke associate, Wale, ek Slack-connector enable karte hain apni chat mein. Woh
poochte hain: "Ab Claude Slack mein kya access kar sakta hai?"

- A. Company ke poore Slack workspace ka sab kuch, admin-level access ke sath.
- B. **✅ Sirf woh channels/messages jo Wale ka apna account already dekhne/access karne ke liye
  permitted hai — connector Wale ki existing permissions inherit karta hai, unse zyada kuch nahi.**
- C. Sirf woh messages jo Wale explicitly copy-paste kar ke attach kare.
- D. Kuch bhi nahi jab tak IT-admin har individual request manually approve na kare.

**Sahi jawab: B** — Connector access-inheritance ka core rule: Claude sirf utna access karta hai
jitna connecting user ka apna account already access kar sakta hai. A over-broad hai (admin-level
nahi). C connector ki poori value ko miss karta hai (manual copy-paste to connector-se-pehle wala
tareeka tha). D har-request-manual-approval ek unnecessarily heavy model hai jo connector ke
designed-behavior se match nahi karta (haan, enterprise-level admin controls exist kar sakte hain
lekin default mechanism yeh nahi hai).

### Q69
Corstone Analytics ke associate, Ige, ek naya workflow ke liye ek Google-Drive connector add kar
rahe hain jo sirf ek specific shared-folder padhna hai. Best-practice sequence?

- A. Convenience ke liye pehle se write/send access de do, taake future kaam bhi easy ho.
- B. **✅ Read-only se shuru karo, access ko task ke hisaab se tightly scope karo (sirf woh folder,
  poori Drive nahi), aur confirm karo ke Ige ko yeh specific account/folder connect karne ki khud
  ijazat hai.**
- C. Saari company-apps ek sath connect kar do taake Claude ke paas maximum context ho.
- D. Personal Google account use karo work-data ke liye taake setup fast ho.

**Sahi jawab: B** — Least-privilege + read-only-first + permission-to-connect-confirmed hi correct
sequence hai. A premature write-access deta hai jab task ko sirf read chahiye. C unnecessary
broad-scope create karta hai (over-provisioning). D personal-account use karna governance/data-
ownership risk create karta hai — yeh Domain 6 ka bhi concern hai.

### Q70
Kaunsa sawal ek naya connector/capability enable karne se pehle poochna **appropriate nahi** hai
(yaani, irrelevant hai is decision ke liye) — the "five checks" (source, reach, fit, outside-
content, actions) ke hisaab se?

- A. "Yeh source kahan se aa raha hai, aur kya woh trustworthy hai?"
- B. "Yeh kya reach kar sakta hai (kitna scope), aur kya woh task-specific hai ya bohat broad?"
- C. **✅ "Kaunsa underlying LLM model is connector ke backend mein chal raha hai?"**
- D. "Kya yeh action le sakta hai (write/send/delete), aur kya outside content (jo woh padhega) ek
  prompt-injection risk hai?"

**Sahi jawab: C** — Backend model-choice ek unrelated technical implementation detail hai jo
connector-enable-karne-ki-permission-decision se disconnect hai. A, B, D teeno directly "five
checks" (source, reach, fit, actions, outside-content-risk) ka hissa hain jo capability-governance
decision ke liye relevant hain.

### Q71
Silvermist Spa Group ki pricing company-wide badalti hai. Ek pricing-dependent client-facing FAQ
Project abhi bhi purani pricing deta hai. Correct action?

- A. Users ko kaho har prompt mein manually naye prices mention karein taake Claude use "sun sake."
- B. **✅ Project ki knowledge-source (pricing sheet) aur agar zaroori ho instructions update karo,
  aur change ki date/version note karo taake future audit trail ho.**
- C. Har quarter ek naya alag Project banao pricing ke liye, purane ko as-is chhod do.
- D. Kuch mat karo — Claude eventually current pricing "infer" kar lega apne aap.

**Sahi jawab: B** — Named-owner maintenance pattern — jab underlying fact change ho, source-of-
truth (knowledge/instructions) update karo aur track karo. A per-prompt-repetition ko systemic
maintenance ka substitute banata hai, jo scale nahi karta. C confusion create karta hai (multiple
active Projects with different pricing). D galat hai — Claude ke paas koi external, live pricing-
feed nahi hai jab tak explicitly diya na jaaye.

### Q72
Thackeray Publishing ke ek Project mein ek editorial-style-guide ke do versions accidentally
upload hain — v1 (purana) aur v2 (current), dono active knowledge mein. Likely effect?

- A. Claude dono versions ka automatically ek "average" nikaal lega.
- B. **✅ Confident answers jo kabhi v1 kabhi v2 follow karein, unpredictably — exactly ek current
  version rakhna chahiye, purani ko remove ya clearly-archived-label karna chahiye.**
- C. Claude har baar explicitly poochega "kaunsa version use karun?"
- D. Koi effect nahi — Claude khud samajh jaayega kaunsa current hai.

**Sahi jawab: B** — Conflicting active knowledge unpredictable/inconsistent outputs create karta
hai bina kisi warning ke — fix hai single-source-of-truth maintain karna. A, C, D teeno galat
assumptions hain ke Claude khud silently is conflict ko "resolve" ya "flag" kar dega reliably —
yeh guarantee nahi hai.

### Q73
Ek shared, multi-team Project ko accurate rakhne ka sabse sustainable, long-term tareeka kya hai?

- A. Umeed rakho ke users khud problems report karenge jab kuch outdated lage.
- B. **✅ Ek named owner assign karo jo scheduled reviews (jaise quarterly) aur change-triggered
  events (jaise pricing/policy change) dono par instructions + knowledge update kare.**
- C. Project ko lock kar do taake koi bhi edit na kar sake, stability ke naam par.
- D. Har mahine poora Project scratch se rebuild karo.

**Sahi jawab: B** — Named ownership + dual-trigger (scheduled + event-driven) review is sabse
sustainable governance pattern hai. A reactive-only approach hai jo systematic drift ko allow karta
hai. C locking maintenance ko hi impossible bana deta hai. D unnecessary churn/waste create karta
hai jab targeted-updates kaafi hote.

### Q74
Elmswood Advisory ke associate, Ren, ko har hafte ek Project ke output mein wahi tone-drift
(zyada casual ho jaata hai) manually fix karni padti hai. Best long-term fix?

- A. Manually fix karte raho — sirf kuch seconds lagte hain, koi bara masla nahi.
- B. **✅ Tone-rule ko explicitly Project instructions mein encode karo (jaise "formal register
  maintain karo, contractions avoid karo") taake yeh recurring manual-fix dobara zaroori na ho.**
- C. Bare/default model par switch karo bina Project ke.
- D. Har baar ek naya chat shuru karo taake "fresh start" mile.

**Sahi jawab: B** — Recurring manual-correction ko configuration mein encode karna hi sustainable
fix hai — ek symptom jo repeat ho raha hai wahi signal hai ke woh instruction mein missing tha. A
manual-toil ko accept kar leta hai jab ek-baari fix available hai. C aur D dono underlying missing-
instruction ko address nahi karte, sirf context ko discard karte hain.

### Q75 — Multiple response (select TWO)
Kaunse DO characteristics ek "achhe" knowledge-source ko define karte hain, Project-configuration
ke context mein?

- A. **✅ Woh task ke liye authoritative hai (source-of-truth, na ke ek secondary/derived copy).**
- B. Woh bohat lamba hai (jitna zyada text utna behtar retrieval).
- C. **✅ Woh current hai aur version-controlled hai (ek hi active version, tracked changes ke
  sath).**
- D. Woh loosely-related background material hai jo "shayad kabhi kaam aaye."

**Sahi jawab: A aur C** — Authoritativeness aur currency/version-control dono directly retrieval-
quality aur trustworthiness decide karte hain. B length ko quality samajhta hai — jaisa Q66 mein
dikha, zyada volume dilution create kar sakta hai. D "maybe-useful" material low-signal noise hai
jo curation ke opposite hai.

---

## Domain 6 — Governance, Risk, and Responsible Use (Q76–Q90)

### Q76 (official-style, reworded scenario)
Hallmark Retail ke ek PM, Ozzy, ek spreadsheet upload karna chahte hain jismein customer-names,
loyalty-account-numbers, aur purchase-history hain, taake Claude quarterly spending-trends analyse
kare. Org-policy regulated personal data ko external AI tools mein share karne ko restrict karti
hai, lekin trend-analysis genuinely valuable hai. Best action?

- A. As-is upload kar do — analysis purely internal purpose ke liye hai.
- B. **✅ Upload se pehle personal identifiers (names, account-numbers) remove/anonymize karo —
  analysis ko pattern chahiye, people nahi; agar totals/counts decision-feeding hain, unhe code-
  execution sandbox mein compute karwao.**
- C. Upload kar do lekin Claude ko prompt mein instruction do "retain mat karna."
- D. Poora analysis skip kar do kyunki data sensitive hai.

**Sahi jawab: B** — Yeh Data-tier (yellow-to-red) ka classic case hai — task ko pattern chahiye,
identifiers nahi; redaction/anonymization use ko policy-compliant banata hai bina task abandon
kiye. A internal-purpose ko permission samajh leta hai jo policy violate karta hai. C ek model-
instruction hai jo koi actual data-control nahi (yeh contractual/technical control nahi hai). D
unnecessary abandonment hai jab redaction se same value mil sakta hai.

### Q77
Marchside Bank ke associate, Théo, sochte hain "Upload kar do lekin Claude ko kaho retain na
kare" ek acceptable control hai kyunki "main usay directly bol raha hoon." Yeh assumption kyun
galat hai?

- A. Claude hamesha sab kuch permanently retain karta hai chahe kuch bhi bola jaaye.
- B. **✅ Ek model-directed instruction (chat mein "retain mat karo" likhna) ek policy ya
  contractual data-control nahi hai — yeh actual retention-settings, data-processing-agreements,
  ya plan-level controls ko replace nahi karta; governance requirement satisfy karne ke liye asal
  technical/contractual control chahiye.**
- C. Yeh sirf response ko slow kar deta hai, koi aur effect nahi.
- D. Yeh sirf Enterprise-tier accounts par kaam karta hai.

**Sahi jawab: B** — In-chat instruction ek behavioral request hai, ek enforced control nahi — real
governance ko actual settings/agreements chahiye. A ek overstatement hai (retention plan/settings
par depend karti hai, "hamesha" absolute claim galat hai). C aur D dono irrelevant/incorrect
technical claims hain jo asal issue (control vs instruction) se hat kar jaate hain.

### Q78
Everdale Analytics ke associate, Min-jun, ek customer-survey dataset privacy-constraints ke tehat
prepare kar rahe hain analysis ke liye. Sabse sound approach?

- A. Sirf explicit IDs (naam, email) hatao, baaki sab columns as-is rakho.
- B. **✅ Woh information hatao jo task ko genuinely nahi chahiye (data-minimization), phir baaki
  data aur intended entry-point/route ko us data-tier standard ke against check karo jo
  organisation govern karti hai — agar unsure ho do tiers ke beech, zyada-cautious tier maano.**
- C. Names ko hash kar do aur baaki sab fields unchanged rakho.
- D. Claude se poocho kya hatana hai aur uske suggestion follow karo.

**Sahi jawab: B** — Data-minimization (sirf task-relevant fields rakho) plus organisation-standard
ke against explicit check hi sound process hai; unsure-case mein zyada-conservative tier choose
karna hai. A sirf direct-identifiers hataata hai, lekin quasi-identifiers (jaise zipcode + age +
purchase-pattern) combine ho kar bhi re-identify kar sakte hain. C hashing bina baqi risk-factors
assess kiye insufficient control hai. D decision Claude ko de deta hai jab yeh organisation-policy
ka judgment call hai, model ka nahi.

### Q79
Ridgemont Consulting ke associate, Aoife, maanti hain ke "Incognito chat" ka matlab hai "kuch bhi
kahin store nahi hota, zero retention." Correct understanding kya hai?

- A. Haan, incognito ka matlab bilkul zero retention hai kahin bhi.
- B. **✅ Incognito chat ko history/memory se bahar rakhta hai (future chats isay reference nahi
  karenge), lekin ek default retention-period phir bhi apply ho sakta hai backend par — yeh zero-
  retention guarantee nahi hai.**
- C. Incognito model ko poori tarah disable kar deta hai.
- D. Incognito ek Project jaisa hi feature hai, bas naam alag hai.

**Sahi jawab: B** — Incognito ek UI/memory-visibility feature hai, ek retention-policy guarantee
nahi — associate ko galat samajh kar sensitive-data ko "safe" nahi maan lena chahiye sirf incognito
ki wajah se. A ek overclaim hai jo actual mechanism ko misrepresent karta hai. C aur D dono
factually galat descriptions hain is feature ke.

### Q80
Brimstone Analytics ke associate, Kato, ko pata karna hai ke kya unke client-inputs "training ke
liye use nahi honge." Kis basis par woh yeh assume kar sakte hain?

- A. Yeh hamesha, har jagah automatically true hota hai.
- B. **✅ Yeh plan aur settings par depend karta hai — Team/Enterprise/API tiers par typically
  by-default training ke liye use nahi hota, jabke Free/Pro/Max par yeh ek user-controlled setting
  hai — Kato ko apne specific account/route ko confirm karna chahiye, assumption nahi banani
  chahiye.**
- C. Sirf tab jab woh incognito-mode use karein.
- D. Sirf agar unhone ek signed NDA sign ki ho Anthropic ke sath.

**Sahi jawab: B** — Yeh plan-dependent hai, ek universal default nahi — associate ko apni specific
route/tier verify karni chahiye. A ek dangerous overgeneralization hai jo galat plan par assume
kiya to actual policy-violation ho sakta hai. C ek narrow/incomplete condition hai (Team/Enterprise
mein bhi by-default apply hota hai bina incognito ke). D ek irrelevant/incorrect requirement hai.

### Q81
Fenmore Robotics ke associate, Petra, sochti hain "code ek sandbox mein chalta hai, isliye ek
sensitive internal-config file load karna theek hai analysis ke liye." Kya is reasoning mein galti
hai?

- A. Kuch bhi galat nahi — sandboxes fully secure hote hain, koi risk nahi.
- B. **✅ Execution-isolation (sandbox) sirf code ki "reach" limit karta hai — yeh is baat ka
  establishment nahi karta ke file us route/environment mein allowed thi shuru se; governance-
  question ("kya yeh data yahan aa sakti hai") sandbox-security-question se alag hai.**
- C. Sandboxes actively data ko leak kar dete hain.
- D. Sandboxes bohat slow hote hain, isliye impractical hain.

**Sahi jawab: B** — Yeh do alag sawal hain jo conflate ho rahe hain: "kya code safely chal sakta
hai" (sandbox handles this) vs "kya yeh data yahan aana chahiye tha" (data-tier/policy question,
independent hai). A over-trusts technical-control ko governance-permission samajh kar. C aur D
dono factually-unfounded generalizations hain jo asal reasoning-error ko address nahi karte.

### Q82
Copperfield Logistics ke associate, Iman, maante hain ke unki chat "fully private" hai kyunki
interface mein sirf woh apna access dekh sakte hain. Governance reality kya hai?

- A. Woh chat fully private hai, kisi ko access nahi.
- B. **✅ Team/Enterprise deployments organisational export aur audit mechanisms provide karte hain
  — administrative visibility/access-review route-assessment ka legitimate hissa hai, isliye "sirf
  main dekh sakta hoon" ek incomplete/misleading assumption hai.**
- C. Free plans par sirf admins hi chats dekh sakte hain, individuals nahi.
- D. Kuch bhi kabhi exportable/reviewable nahi hota, kisi bhi plan par.

**Sahi jawab: B** — Organisational deployments mein admin-level visibility/audit ek real governance
mechanism hai — user-level "sirf mujhe dikhta hai" ka matlab "org bhi nahi dekh sakti" nahi hai. A
overclaim hai. C description reversed/incorrect hai. D absolute claim hai jo enterprise-audit-
capabilities ko ignore karta hai.

### Q83
Kaunsa use-case ek Associate ke liye design karna **inappropriate** hai (governance lens se)?

- A. Internal meeting-notes ko action-items mein draft karna, jise owner review karega.
- B. **✅ Claude ke output ko ek adverse HR decision (jaise termination) ka **sole basis** banana,
  bina kisi human judgment/review ke.**
- C. Publicly-available research ko internal audience ke liye summarize karna.
- D. Naye campaign ke liye ideas brainstorm karna.

**Sahi jawab: B** — Adverse, person-affecting decisions ko AI output ka sole/unreviewed basis
banana ek core inappropriate-use hai — yeh accountability aur fairness dono violate karta hai. A,
C, D teeno standard, human-reviewed ya low-stakes productivity tasks hain jo appropriate hain.

### Q84
Overton Financial ki org-policy client-data ko approved-external-tools se bahar forbid karti hai,
lekin ek associate ko ek asaan technical workaround pata chal jaata hai (jaise apna personal
browser-extension use kar ke same data ek unapproved tool mein daal dena). Associate ko kya karna
chahiye?

- A. Workaround use karo — end-result same hai, koi farq nahi padta.
- B. **✅ Policy follow karo — workaround ki technical asaani governance-requirement ko override
  nahi karti; agar workflow genuinely improve ho sakta hai, sahi route escalate karo ke policy
  review/update ho.**
- C. Ek baar use kar lo aur baad mein document kar do.
- D. Claude se poocho "yeh theek hai kya?" aur uske jawab par decide karo.

**Sahi jawab: B** — "Yeh asaan hai" governance ka substitute kabhi nahi hota — shadow-AI ka exactly
yehi mechanism hai (approved route mushkil lage to log unapproved route dhoond lete hain), jo
organisation ke liye risk create karta hai. A aur C dono policy-violation ko justify/normalize
karte hain. D governance-decision ko model ko outsource karta hai, jo appropriate authority nahi
hai.

### Q85
Willowmere Health Clinic ka ek workflow patient-intake-records handle karega future mein. Associate
ko pehle kya karna chahiye?

- A. Real patient-records par test karo taake realistic results milein.
- B. **✅ Invented/synthetic demo-data par test karo pehle; real-data ke stage par sirf approved
  accounts aur approved connectors/routes use karo, org ki healthcare-data policy ke mutabiq.**
- C. Testing completely skip kar do, seedha production mein deploy karo.
- D. Ek colleague ke apne personal-health records use kar lo testing ke liye "kyunki woh consent de
  chuke hain."

**Sahi jawab: B** — Synthetic-data-first testing pattern regulated/sensitive-domain workflows ke
liye standard hai — real data sirf approved-route establish hone ke baad. A real regulated data ko
unnecessary testing-risk mein daalta hai. C testing skip karna production mein unverified-behavior
risk create karta hai. D ek colleague ka data bhi still real, regulated personal-health-data hai —
ek informal "consent" organisational/regulatory approval ka substitute nahi hai.

### Q86
Ashcombe Advisors ka ek client-deliverable substantially AI-drafted hai aur firm ki "professional
recommendation" ke tor par present ho raha hai bina kisi qualified reviewer ke sign-off ke. Kaunse
concerns yahan uthte hain?

- A. Sirf data-privacy — koi aur issue nahi.
- B. **✅ Data-handling, accountability (ek qualified insaan ko yeh recommendation own karni chahiye
  aur us ke against apni professional judgment stand behind karni chahiye), aur disclosure/
  appropriate-review — teeno saath.**
- C. Sirf document-formatting.
- D. Koi concern nahi — client ne jaldi maanga tha, isliye acceptable hai.

**Sahi jawab: B** — Yeh ek multi-dimensional governance-failure hai (accountability transfer + koi
review-gate + potentially undisclosed AI-authorship for a "professional recommendation") — sabhi
teen dimensions relevant hain saath mein. A aur C dono issue ko ek chhoti dimension tak limit karte
hain jab asal masla broader hai. D deadline-pressure ko governance-exemption maan leta hai, jo
galat hai.

### Q87
Kaunsa design safest hai jab ek hiring-team Claude se job-candidates rank karwana chahti hai?

- A. Koi concern nahi hai — ranking efficient hai, seedha implement karo.
- B. **✅ Bias/fairness aur accountability concerns hain; safer design: Claude ko sirf defined,
  pre-agreed criteria ke against structured note-taking/organizing ke liye use karo (jaise "yeh
  candidate ne yeh 5 required-skills mention kiye ya nahi"), final ranking-decision aur
  accountability humans ke paas rakho.**
- C. Sirf speed-concerns hain, koi aur governance-issue nahi.
- D. Concerns sirf tab uthenge jab candidates ko pata chale ke AI involved tha.

**Sahi jawab: B** — Employment-decisions bias-sensitive, high-stakes, person-affecting hain — AI
ko structured-support-role tak limit karna (na ke decision-maker) hi defensible design hai. A
fairness-risk ko completely ignore karta hai. C ek incomplete framing hai. D disclosure ek separate
concern hai lekin underlying bias/fairness-risk disclosure se independent exist karta hai (disclose
karne se bhi bias khatam nahi hota).

### Q88
Kisi bhi upload se pehle sabse pehla governance-sawal kaunsa poochna chahiye (the-Data question ke
tehat)?

- A. "Kaunsa model sabse cheap hai is task ke liye?"
- B. **✅ "Kya yeh information regulated, personal, ya confidential hai, aur kya organisational
  policy is specific entry-point/route ko allow karti hai?"**
- C. "Document kitna lamba hai?"
- D. "Kya Claude ko yeh information useful lagegi?"

**Sahi jawab: B** — Yeh directly data-sensitivity-tier aur route-approval dono establish karta hai,
jo har aur decision se pehle aana chahiye. A, C, D teeno unrelated ya premature sawal hain jo
governance-gate se pehle aane wale asal sawal ko skip karte hain.

### Q89
Kaunsa use-case ek Associate confidently, bina escalation ke, design kar sakta hai?

- A. Ek regulated tax-opinion generate kar ke client ko as-is de dena bina CPA-review ke.
- B. **✅ Meeting-transcripts ko action-item lists mein convert karna, jinhe har item ka named owner
  review karega before acting.**
- C. Loan-applications ko khud approve/reject karna.
- D. Ek patient ke liye medical-diagnosis draft karna directly patient ko dene ke liye.

**Sahi jawab: B** — Productivity/synthesis-task jahan human-review-gate already built-in hai
(named owner reviews) appropriate, associate-designable use-case hai. A, C, D teeno adverse ya
regulated final-decisions hain jinhe qualified-human ya specialist-role ke paas rehna chahiye,
associate-scope se bahar.

### Q90 — Multiple response (select TWO)
Claude se koi data explicitly withhold karne ki kaunsi DO legitimate wajah hain?

- A. **✅ Us data mein regulated personal identifiers hain jo current task ko genuinely nahi
  chahiye (data-minimization).**
- B. Data lamba hai aur upload karne mein time lagega.
- C. **✅ Organisational policy ya client-contract explicitly is entry-point/route ko prohibit karti
  hai.**
- D. Data boring/uninteresting hai.

**Sahi jawab: A aur C** — Data-minimization (task-unnecessary regulated identifiers) aur policy/
contractual-prohibition dono genuine, defensible governance-reasons hain. B aur D dono irrelevant
convenience/preference-based reasons hain, governance-criteria nahi.

---

## Domain 7 — Troubleshooting and Optimization (Q91–Q100)

### Q91
Vantage Print Shop ke associate, Cleo, ek product-listing prompt use karte hain jo pehle answer se
hi flat/generic output deta hai — har baar. Team-lead sochta hai "sabse capable model try karo."
Diagnostic-ladder ke hisaab se pehla, sabse-sasta check kya hona chahiye?

- A. Turant flagship-tier model try karo aur dekho farq padta hai kya.
- B. **✅ Pehle prompt ko dobara padho aur poocho "kya yeh cheez jo missing lag rahi hai (audience,
  differentiators, purpose) asal mein prompt mein thi bhi?" — "wrong se pehle answer aana" classic
  under-specification symptom hai, sabse cheap-first check yehi hai.**
- C. Turant context-window ko clear kar ke naya session shuru karo.
- D. Model-tier ko downgrade karo cost bachane ke liye, symptom irrelevant maan kar.

**Sahi jawab: B** — "Wrong from the first answer" pattern specifically under-specification ki
taraf point karta hai — sabse sasta, sabse pehla check hai prompt re-read karna. A model-tier-
change ko sabse pehle try karna ladder ko ulta chalata hai (yeh book explicitly warn karti hai —
sabse common instinct galat hota hai). C irrelevant hai kyunki symptom pehle-hi-answer mein hai,
lambi-session degradation nahi. D symptom se completely unrelated action hai.

### Q92
Redshaw Analytics ke associate, Fabio, ek financial-summary prompt kabhi-kabhi fabricated numbers
deta hai. Fabio ne prompt ko 3 guna lamba kar diya, extra caveats add kar ke — problem barqarar
hai, kabhi-kabhi aur bhi worse. Asal, sahi fix?

- A. Prompt ko aur bhi lamba karo, aur zyada "please be accurate" instructions add karo.
- B. **✅ Yeh "wrong feature/model" diagnosis hai — numbers ko code-execution se compute karwao ya
  ek authoritative knowledge-source se ground karo, na ke prose mein "generate" karwao; phir
  output ko independently verify karo.**
- C. Har baar output ko 5 dafa regenerate karo aur jo number sabse zyada baar repeat ho use pick
  karo.
- D. Temperature/creativity-setting kam karo taake output "safe" ho.

**Sahi jawab: B** — Fabricated numbers ka root-cause "prose se number generate karwana" hai, prompt
-length nahi — ladder ke hisaab se yeh "wrong feature/model" category hai (calculation ko code-
execution ki zaroorat thi). A already-tried-and-failed approach ko repeat karta hai. C regeneration
usi model se same systematic-error repeat kar sakta hai (Q16 jaisa hi trap). D ek unrelated control
hai jo fabrication ka root-cause address nahi karta.

### Q93
Cranmore Realty ke associate, Idris, ek prompt bhejte hain jo consistently ek paragraph deta hai
jab ek 4-column comparison-table chahiye tha (property, price, sqft, distance). Sabse fast, cheap
fix?

- A. Poora prompt scratch se rewrite karo.
- B. **✅ Ek explicit output-format-spec add karo (columns ke naam do: "Property | Price | Sqft |
  Distance") ya ek chhota example do sahi shape ka.**
- C. Model-tier upgrade karo — yeh formatting-capability ka masla hai.
- D. Har baar output ko manually table mein convert karo, prompt ko as-is rakhte hue.

**Sahi jawab: B** — Yeh "wrong feature/model" nahi hai — yeh under-specification hai specifically
output-shape ke liye; ek explicit format-spec ya example seedha fix hai. A unnecessarily heavy-
handed hai jab ek chhoti addition kaafi thi. C galat diagnosis hai — yeh model-capability ka masla
nahi, missing-instruction ka masla hai. D manual-workaround ko permanent bana deta hai jab a
one-line prompt-fix available tha.

### Q94
Fernwood Consulting ke associate, Yara, apne underperforming prompt ko systematically diagnose kar
rahi hain. Sabse effective approach kaunsa hai (na ke random-tweaking)?

- A. Random tweaks karte raho jab tak output subjectively behtar na lage.
- B. **✅ Output ko carefully padho aur naam do ke request ka specifically kaunsa hissa fail hua
  (audience ignore hua? length broke? ek specific section missing?) — sirf woh named part badlo
  aur resend karo.**
- C. Claude se khud apne output ko 1-10 grade karwao aur us score ke hisaab se lamba/chhota karo.
- D. Output ko 5 baar regenerate karo aur "best-feeling" wala rakho.

**Sahi jawab: B** — Named, specific diagnosis (kaunsa exact part fail hua) hamesha random-
tweaking, self-grading, ya multi-regeneration se stronger hai — yeh directly root-cause target
karta hai. A trial-and-error hai bina hypothesis ke. C self-assessment unreliable signal hai
(jaisa Domain 2 mein establish hua). D "feeling" subjective aur non-repeatable hai.

### Q95
Oldbridge Freight ka ek working, 6-prompt weekly-reporting workflow already reliably chal raha hai.
Team optimize karna chahti hai efficiency ke liye. Best combined step?

- A. Har prompt ke baad ek extra review-step add karo, chahe already-verified steps ho.
- B. **✅ Redundant steps hatao, repeated prompts ko templates/Skills banao, stable-recurring
  context ko Project mein move karo, aur agar output-quality hold kare to ek cheaper-tier model try
  karo — har change ko individually verify karte hue.**
- C. Sabse capable/flagship model par upgrade karo bina kisi identified quality-gap ke.
- D. Har run ko do baar chalao "consistency ke liye," bina kisi observed inconsistency ke.

**Sahi jawab: B** — Yeh genuine optimization hai — redundancy hatao, configuration encode karo,
cost-efficiency try karo bina quality-check hataye. A, C, D teeno unnecessary cost/friction add
karte hain bina kisi identified problem ke — yeh "optimization" nahi, waste hai.

### Q96
Thornfield Legal ke associate, Priya, ko har hafte ek Project-output mein wahi ek manual-edit karni
padti hai (ek standard disclaimer add karna jo Claude include nahi karta). Best long-term fix?

- A. Manual-edit karte raho — 30 second ka kaam hai, koi bara masla nahi.
- B. **✅ Disclaimer-requirement ko explicitly Project instructions mein encode karo taake har
  output mein automatically include ho — recurring manual-fix ko configuration mein daal do.**
- C. Model switch karo, symptom se unrelated action.
- D. Client se poocho disclaimer chahiye ya nahi, bina underlying configuration-gap fix kiye.

**Sahi jawab: B** — Recurring manual-fix ek missing-instruction ka classic symptom hai — encode
karna hi permanent, scalable solution hai. A toil ko accept kar leta hai jab ek-baari fix
available hai. C unrelated hai. D asal issue (Project-instructions mein gap) ko avoid karta hai.

### Q97
Ashdown Media ke associate, Kwame, ek prompt change karte hain aur unhe lagta hai output "behtar
lagta hai" naye version mein. Sound approach adjust karne ka?

- A. Assume kar lo ke naya version behtar hai aur turant production mein deploy kar do.
- B. **✅ Naye version ko ek known test-case par purane version ke against directly compare karo —
  objectively check karo ke yeh genuinely behtar hai ya sirf "different" hai (novelty-bias se
  bacho).**
- C. Claude se poocho "kaunsa version zyada achha hai?" aur uske jawab par decide karo.
- D. Dono versions ko client ko bhej do aur unse pick karwao bina khud evaluate kiye.

**Sahi jawab: B** — Feedback-driven-adjustment evidence se hona chahiye, "lagta hai" impression se
nahi — same known-case par side-by-side comparison objectively confirm karta hai. A ek untested
assumption par based hai. C self-referential/unreliable hai. D apna judgment-responsibility client
ko offload karta hai, aur ek untested version client ko expose karta hai.

### Q98
Copperline Insurance ke ek complex-report prompt kabhi deep, achhi-tarah-organized output deta hai,
kabhi shallow — bina prompt change kiye, same input ke sath. Sabse likely cause?

- A. Model purely random hai, kuch bhi predict nahi ho sakta, isliye kuch nahi kiya ja sakta.
- B. **✅ Task ek single call ke liye bohot bara/broad hai (jaisa Domain 1 ke decomposition-
  principle mein tha) — decompose karo taake har part consistent depth paaye, na ke poori depth
  ek hi generation par depend kare.**
- C. Prompt mein "please" ya politeness-words missing hain.
- D. Galat model-tier use ho raha hai — turant upgrade karo.

**Sahi jawab: B** — Inconsistent-depth-on-same-broad-task ek decomposition-need ka signal hai
(Domain 1/7 overlap) — breaking the task down produces consistent per-part depth. A ek excuse hai
jo diagnostic-effort avoid karta hai. C irrelevant folklore hai. D ek untested jump hai — decompose
karna pehle try karna chahiye, tier-upgrade se pehle (cheapest-first principle).

### Q99
Hollowell Design ke associate, Nasrin, ne ek one-off client-presentation prompt ko 15 minutes
tune karne mein lagaye — usay sirf ek baar use karna hai, kabhi reuse nahi hoga. Better judgment
kya hota?

- A. "Perfect" prompt ke liye tuning jaari rakho jab tak 10/10 na mile.
- B. **✅ Ek "kaafi-achha" prompt ke baad ruk jao aur output ko manually finish karo — one-off
  deliverable prompt-craft-perfection ke bajaye diminishing-returns par jaldi ruk kar manual-
  finish deserve karta hai.**
- C. Is one-off task ke liye ek poora Skill/Project bana do future-reuse ke liye.
- D. Sabse capable/flagship model use karo taake prompt-quality "matter na kare."

**Sahi jawab: B** — Optimization-effort ko reuse-value se match karo — ek baar-use-hone-wale
deliverable ke liye prompt-perfection chase karna diminishing-returns hai; manual-finish zyada
efficient hai. A time waste karta hai returns ke against. C unnecessary infrastructure banata hai
ek kaam ke liye jo dobara hoga hi nahi. D cost badhata hai bina underlying tuning-time-waste
solve kiye.

### Q100 — Multiple response (select TWO)
Bramwell Ops ka ek workflow already reliably kaam kar raha hai. Kaunse DO optimization-moves valid
hain, diagnostic-ladder aur book ke optimization-principles ke mutabiq?

- A. **✅ Stable, repeated context ko Project/Skill mein move karna (recurring-manual-work ko
  configuration mein encode karna).**
- B. Har step par ek naya human-approval add karna "just in case," bina kisi identified-risk ke.
- C. **✅ Agar output-quality measurably hold kare, to ek faster/cheaper model-tier par jaana aur
  result verify karna.**
- D. Har prompt ko 2x lamba karna "robustness ke liye," bina kisi specific missing-element
  identify kiye.

**Sahi jawab: A aur C** — Configuration-encoding aur verified cost-efficiency dono genuine,
evidence-based optimization moves hain. B unnecessary friction add karta hai bina justification.
D "lambi karna" koi specific fix nahi hai — jaisa Q92/Q93 mein dikha, length problem-specific gap
ka substitute nahi hai.

---

## Answer Key — Quick Grid

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B | 21 | B | 41 | B | 61 | B | 81 | B |
| 2 | B | 22 | B | 42 | A | 62 | B | 82 | B |
| 3 | C | 23 | A,B | 43 | B | 63 | B | 83 | B |
| 4 | B | 24 | B | 44 | B | 64 | B | 84 | B |
| 5 | B,C | 25 | B | 45 | B | 65 | B | 85 | B |
| 6 | B | 26 | B | 46 | B | 66 | B | 86 | B |
| 7 | B | 27 | B | 47 | A,C | 67 | B | 87 | B |
| 8 | A,C | 28 | A,C | 48 | C | 68 | B | 88 | B |
| 9 | B | 29 | B | 49 | B | 69 | B | 89 | B |
| 10 | B | 30 | B | 50 | B | 70 | C | 90 | A,C |
| 11 | B | 31 | B | 51 | B | 71 | B | 91 | B |
| 12 | B | 32 | B | 52 | B | 72 | B | 92 | B |
| 13 | C | 33 | A | 53 | B | 73 | B | 93 | B |
| 14 | A,C | 34 | A,C | 54 | B | 74 | B | 94 | B |
| 15 | B | 35 | B | 55 | B | 75 | A,C | 95 | B |
| 16 | B | 36 | B | 56 | B | 76 | B | 96 | B |
| 17 | B | 37 | B | 57 | B | 77 | B | 97 | B |
| 18 | B | 38 | B | 58 | A,C | 78 | B | 98 | B |
| 19 | B | 39 | B | 59 | B | 79 | B | 99 | B |
| 20 | B | 40 | B | 60 | B | 80 | B | 100 | A,C |

---

## Scoring

- **90–100:** Senior-associate-level judgment — tum quiz100.md aur hardquiz.md dono confidently
  pass kar sakte ho. Real exam is se kaafi aasan lagega.
- **75–89:** Solid, lekin kuch "good vs best" traps abhi bhi pakad rahe hain. Rationale wapas
  padho jahan galti hui — har rationale specifically batata hai trap kya tha.
- **60–74:** Domain 2, 4, aur 6 (52% of exam) ki rationale dobara padho — khaas kar delegation-map
  ke 3 criteria, error-taxonomy ke 6 types, aur governance ke 4 questions.
- **< 60:** Pehle `quiz100.md` par 90%+ score karo, phir [08-teaching-walkthrough.md](08-teaching-walkthrough.md)
  dobara padho, phir yeh set dobara attempt karo — yeh sequel hai, starting point nahi.

---
[⬅ CCAO-F Index](README.md) · [quiz100 — Original 100-Q Set](quiz100.md) ·
[08 — Teaching Walkthrough](08-teaching-walkthrough.md)
