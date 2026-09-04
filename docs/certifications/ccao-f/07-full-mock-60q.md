# 07 — Full Mock Exam (60 Questions, Domain-Weighted)

*Timing target: 60 Q in ~85 min (real exam: 60 Q / 120 min = 2 min/Q, isliye yeh drill tighter hai —
real exam se zyada pressure practice karne ke liye). Har domain ka question-count uske official
weight ke proportional hai ([01-domain-blueprint.md](01-domain-blueprint.md)): D1=8, D2=13, D3=7,
D4=10, D5=7, D6=9, D7=6 → total 60. Har Q self-contained hai — correct option **bold** hai, reasoning
usi option ke andar. Grounded strictly in the official blueprint objectives + the 3 verbatim sample
questions ([03](03-how-to-prepare-and-sample-questions.md)) — koi live item-bank content nahi (guide
khud kehti hai sample questions live bank se nahi liye gaye).*

---

### Part 1 — Domain 1: Prompting and Task Execution (14% · Q1–8)

**1.** Ek associate Claude se sirf "customer complaints ka summary do" likhta hai aur generic, kam-useful
output milta hai. Sabse zyada likely missing ingredient?
a) Longer prompt b) **Context (audience, format, aur specific criteria — jaise "top 3 recurring
issues, bullet form, exec-ready") — bina iske Claude default generic-summary mode mein reh jaata hai**
c) Highest-cost model d) Multiple Claude instances

**2.** Ek complex request — "naya onboarding process design karo, docs likho, aur team ko train karo" —
ek hi prompt mein diya jaata hai aur output shallow aata hai. Sahi fix?
a) Prompt chhota karo b) **Task decomposition — teen alag sub-tasks (design → docs → training
material) mein todo, har ek ko apna focused prompt do** c) Sirf Opus use karo d) Task cancel karo

**3.** Pehla draft achha hai lekin tone bahut casual hai ek board-level memo ke liye. Sabse efficient
next step?
a) Poora naya prompt from scratch b) **Prompt iterate karo — specific feedback do ("zyada formal,
board-level tone") aur refine karwao, poora dobara likhne ke bajaye** c) Manually poora rewrite karo
d) Different AI tool try karo

**4.** Brainstorming session ke liye prompting strategy, deep-research task ke prompting strategy se
kaise differ karni chahiye?
a) Dono same hote hain b) **Brainstorming = wide, divergent, kam constraints (zyada options chahiye);
research/analysis = narrow, structured, verification-focused — task-type ke hisaab se adapt karo**
c) Brainstorming hamesha lamba hona chahiye d) Research kabhi prompt nahi maangta

**5.** Ek associate ek 10-step process ko ek single Claude prompt mein daal deta hai aur confuse output
milta hai. Best correction?
a) Steps ko aur bhi combine karo b) **Har logical chunk ko apna prompt/turn do — sequential
decomposition, har step ka output agle step ka input ban sakta hai** c) Prompt delete kar do d) Steps
random order mein daalo

**6.** "Effective prompt" ke core elements mein se konsa business task ke liye zaroori hai jo Domain 1
explicitly test karta hai?
a) Sirf length b) **Task ka clear goal, relevant context, aur desired output format — teeno milke
"effective" banate hain** c) Sirf politeness d) Sirf model name mention karna

**7.** Ek analysis task ke liye Claude se pehla output aata hai lekin ek key data point missing hai.
Sahi approach?
a) Poora task discard karo b) **Follow-up prompt se specifically missing data point point out karo aur
dobara maango — iteration loop** c) Missing data khud calculate kar ke publish kar do d) Assume karo
woh irrelevant tha

**8.** Ek research-type prompt aur ek drafting-type prompt mein sabse bara structural farq kya hona
chahiye?
a) Koi farq nahi b) **Research prompt verification/sourcing-focused instructions carry karta hai;
drafting prompt tone/audience/format-focused hota hai — dono alag cognitive tasks hain** c) Drafting
hamesha chhota hota hai d) Research kabhi Claude se nahi hota

---

### Part 2 — Domain 2: Output Evaluation and Validation (21% · Q9–21)

**9.** Claude ek regulation summary deta hai, ek specific subsection number high confidence ke sath cite
karte hue. Compliance ko bhejne se pehle sabse appropriate action?
a) As-is bhej do, confidence high thi b) **Cited subsection ko official regulation text ke against
verify karo bhejne se pehle** c) Claude se apni confidence rate karwao d) Sirf reword kar do

**10.** Ek Claude-generated report mein do paragraphs ek doosre ko contradict karte hain (ek jagah
revenue "up 8%", doosri jagah "down 3%"). Yeh kis evaluation skill ka test hai?
a) Bias detection b) **Inconsistency identification — internal contradictions spot karna publish se
pehle** c) Model selection d) Prompt iteration

**11.** Ek output "confidently" ek statistic deta hai jiska koi source nahi diya gaya. Sabse appropriate
step?
a) Statistic ko as-is use karo, confident sounded b) **Fact-check/validate karo original source ke
against — unsourced confident-sounding claims hallucination ho sakte hain** c) Statistic delete kar do
bina check kiye d) Claude se "sach bolo" kehna

**12.** Ek output different demographic groups ko systematically different tone mein describe karta hai
bina justification ke. Yeh kya hai?
a) Formatting issue b) **Bias — evaluation ka ek core objective hai outputs mein bias identify karna,
sirf accuracy nahi** c) Hallucination d) Model selection error

**13.** Kab decide karna chahiye ke ek output ko human review/additional verification chahiye?
a) Kabhi nahi, Claude hamesha accurate hai b) **Jab stakes high hon (compliance, financial, legal,
safety), ya jab confidence-vs-verifiability gap ho — Domain 2 ka explicit objective hai "decide kab
human review zaroori hai"** c) Sirf jab output lamba ho d) Sirf jab user pooche

**14.** Ek internal-only draft aur ek client-facing final report — dono same raw Claude output se aate
hain. Evaluation step mein farq?
a) Koi farq nahi, same output bhej do dono jagah b) **Output ko intended audience ke liye edit/adapt/
refine karo — internal draft kam formal ho sakta hai, client-facing ko polish + tone-check chahiye**
c) Client version hamesha chhota hona chahiye d) Internal version kabhi review nahi hoti

**15.** "Kaunsa model use karna hai" (speed vs quality trade-off) aur "output accurate hai ya nahi"
— yeh do decisions kis tarah domain-split hote hain?
a) Dono Domain 2 mein aate hain b) **Model/tool choose karna Domain 3 (Product and Model Selection)
hai; output ko evaluate karna Domain 2 hai — do alag decision points, exam dono ko separately test
karta hai** c) Dono Domain 6 mein aate hain d) Yeh farq exam mein test nahi hota

**16.** Ek Claude output data table de raha hai jab user ne actually ek narrative summary maanga tha.
Sabse relevant evaluation objective?
a) Accuracy check b) **Appropriate output format select/adapt karna — information ko sahi
format (artifact/inline/structured/narrative) mein organize karna Domain 2 ka explicit objective hai**
c) Bias check d) Model selection

**17.** Do alag Claude outputs (same prompt, dobara run) compare karte waqt sabse zyada value kis
cheez se milti hai?
a) Sirf lamba wala choose karo b) **Dono ko criteria (accuracy, completeness, audience-fit) ke against
compare karo aur behtar ko select/merge karo — "compare" explicitly Domain 2 objective hai** c) Pehla
hamesha behtar hota hai d) Comparison zaroori nahi

**18.** Ek associate Claude se poochta hai "kya yeh sach hai?" aur Claude "haan, main confident hoon"
kehta hai. Kya yeh sufficient validation hai?
a) Haan, self-report reliable hai b) **Nahi — self-reported confidence accuracy ka reliable signal
nahi hota (guide ka apna sample-question rationale); external fact-check zaroori rehta hai** c) Sirf
lamba jawab chahiye d) Doosra AI tool poochna zaroori

**19.** Ek output completeness ke liye evaluate karte waqt sabse zaroori question?
a) Kitna lamba hai b) **Kya har part of the original request address hua, ya kuch chhoot gaya?** c)
Formatting kaisi hai d) Kitni der mein generate hua

**20.** Ek associate raw Claude output ko bina kisi review ke seedha client ko forward kar deta hai kyunki
"deadline tight thi". Yeh kis principle ko violate karta hai?
a) Prompting b) **Output evaluation/validation — chahe deadline ho, accuracy/completeness/audience-fit
check karna is credential ka core (21%) hai; time pressure evaluation skip karne ka valid reason nahi**
c) Model selection d) Configuration

**21.** Curate/organize information ka matlab evaluation stage mein kya hota hai?
a) Sirf delete karna b) **Relevant information ko structure/prioritize karna aur sahi output form
(artifact vs inline vs structured data) mein present karna — raw output ko useful shape dena** c)
Sirf translate karna d) Model change karna

---

### Part 3 — Domain 3: Product and Model Selection (12% · Q22–28)

**22.** Ek high-volume, short customer-reply drafting task, jahan speed/cost deep-reasoning se zyada
matter karte hain. Best choice?
a) Har baar sabse capable, highest-cost model b) **Ek faster, lower-cost model jo straightforward
high-volume tasks ke liye suited ho (jaise Haiku-tier)** c) Sab features disable kar do d) Doosra
platform try karo

**23.** Ek complex, multi-step legal-reasoning task ke liye model choice kis factor pe base honi chahiye?
a) Sabse sasta model b) **Task complexity — deep reasoning chahiye to sabse capable model (jaise
Opus-tier) reserve karo, cost/speed secondary** c) Random selection d) User ka mood

**24.** Ek long research conversation context limit ke qareeb pahunch rahi hai. Sahi move?
a) Bina kuch kiye continue karo, Claude khud handle karega b) **Context limitation recognize karo aur
decide karo — summarize karke naya session start karo, ya key info persist/save karo before restarting**
c) Poori history delete kar do bina summary ke d) Model badal do, context issue fix ho jayega

**25.** Ek task ke liye "Projects" feature vs plain "chat" — decision kis pe based honi chahiye?
a) Random b) **Kya task ko persistent instructions + knowledge sources chahiye jo repeatedly reuse
hon (Projects), ya ek one-off quick query hai (chat)** c) Hamesha Projects use karo d) Hamesha chat use
karo

**26.** "Research mode" ka appropriate use-case kya hai product-selection ke objective ke hisaab se?
a) Simple one-line facts ke liye b) **Multi-source, deeper investigation tasks jahan Claude ko khud
information gather/synthesize karni ho — feature ko task ki depth se match karo** c) Har task ke liye
d) Sirf coding tasks

**27.** Haiku, Sonnet, aur Opus mein differentiate karne ka core skill kya hai (exam ke nazariye se)?
a) Naam yaad rakhna b) **Har model ka cost/speed/capability trade-off samajhna aur task requirement ke
sath align karna — yeh Domain 3 ka explicit objective hai** c) Sirf Opus use karna hamesha d) Model
naam irrelevant hai

**28.** Ek associate ek short, simple FAQ-answering task ke liye sabse expensive/slowest model choose
karta hai "quality ke liye". Yeh kis mistake ka example hai?
a) Sahi decision b) **Model selection ko task requirements ke sath misalign karna — high-cost model
low-complexity task pe waste hai; Domain 3 explicitly cost/speed/quality trade-off test karta hai** c)
Prompting error d) Governance violation

---

### Part 4 — Domain 4: Workflow Integration and Solution Design (16% · Q29–38)

**29.** Ek team apna manual research process Claude se accelerate karna chahti hai. Pehla step kya hona
chahiye Domain 4 ke objectives ke hisaab se?
a) Seedha Claude ko poore process pe laga do b) **Existing requirements aur use-case analyze karo —
kahan Claude value add karega aur process kis tarah design/adapt hona chahiye** c) Team ko replace kar
do d) Process ko ignore karo

**30.** "Augment" vs "redesign" workflow integration mein farq?
a) Same cheez hai b) **Augment = existing process ke andar Claude ek step add karta hai; redesign =
poora process Claude ke around naye sirey se banaya jaata hai — dono valid integration patterns hain,
context pe depend karta hai** c) Augment hamesha behtar hai d) Redesign kabhi zaroori nahi

**31.** Ek associate ko ek naye workflow mein Claude integrate karna hai lekin stakeholders sceptical
hain. Domain 4 ka explicit objective yahan kya hai?
a) Ignore stakeholders b) **Claude ki value AUR limitations dono stakeholders ko honestly communicate
karna — sirf benefits nahi, kahan yeh fit nahi baithta bhi batana** c) Sirf benefits sell karo d) Sirf
limitations batao, value mat batao

**32.** Solution design support ke liye Claude use karte waqt associate ka role kya rehta hai?
a) Passive — Claude sab decide karega b) **Active — Claude leverage karna design/development/iteration
support ke liye, final judgment aur integration decisions associate/team ke paas rehte hain** c) Koi
role nahi d) Sirf Claude ko monitor karna, kuch nahi karna

**33.** Process optimization ke liye Claude leverage karna Domain 4 mein kaisi cheez hai?
a) Out of scope b) **Explicit objective — Claude ko research, planning, aur process optimization ke
liye use karna workflow-integration skill ka hissa hai** c) Sirf Domain 7 ka kaam d) Sirf technical
teams ke liye

**34.** Ek existing manual approval workflow mein Claude add karte waqt sabse important integration
question?
a) Kaunsa font use hoga b) **Yeh naya step existing process ke saath kaise fit baithta hai — augment
karna hai ya redesign, aur kahan human checkpoint rehna chahiye** c) Claude ka naam kya rakhna hai d)
Kitni der lagegi setup mein

**35.** Ek stakeholder poochta hai "Claude humare liye sab kuch automate kar dega?". Domain 4-aligned
jawab?
a) "Haan, sab kuch" b) **"Nahi — Claude specific tasks mein value add karega (research, drafting,
analysis), lekin limitations bhi hain; humein workflow design karna hoga jahan yeh fit baithe"** c)
"Pata nahi" d) "Ignore karo, khud figure out karo"

**36.** Requirements analysis ke bina seedha ek Claude-based solution deploy karna kis risk ko badhata
hai?
a) Koi risk nahi b) **Mismatch risk — solution actual use-case/requirements se align nahi hoga, kyunki
Domain 4 ka pehla objective hi "requirements analyze karna" hai solution design se pehle** c) Sirf cost
risk d) Sirf speed risk

**37.** Ek associate ek naya customer-support workflow design karta hai jahan Claude sirf drafts banata
hai aur human final-send karta hai. Yeh integration pattern kya demonstrate karta hai?
a) Poor design b) **Thoughtful augmentation — Claude value-add karta hai (drafting) jabke accountability/
final judgment human ke paas rehta hai; solution design ka mature pattern** c) Automation failure d)
Governance violation

**38.** "Iteration" solution-design context mein Domain 4 ke hisaab se kya matlab rakhta hai?
a) Sirf prompt iterate karna (Domain 1) b) **Solution ko real usage/feedback ke baad refine karna —
workflow khud bhi ek iterative design process hai, sirf ek prompt nahi** c) Kuch nahi, ek-time setup
hoti hai d) Sirf model switch karna

---

### Part 5 — Domain 5: Configuration and Knowledge Management (12% · Q39–45)

**39.** Ek team apna Claude Project set up kar rahi hai. Configuration ke do core components kya hain
Domain 5 ke hisaab se?
a) Sirf model name b) **Instructions + knowledge sources — dono milke Project ka behavior define karte
hain** c) Sirf pricing plan d) Sirf team size

**40.** Google Drive/Gmail jaise connectors manage karna kis domain ka explicit objective hai?
a) Domain 2 b) **Domain 5 — "uploaded knowledge aur connectors manage karna" explicit objective hai**
c) Domain 3 d) Domain 7

**41.** Ek system-level instruction likhte waqt sabse important quality kya honi chahiye?
a) Lambi honi chahiye b) **Clear aur effective honi chahiye — ambiguous instructions inconsistent
behavior ka sabse bara source hain** c) Multiple languages mein honi chahiye d) Har baar badalte rehna
chahiye

**42.** Ek Project ke knowledge sources purane ho chuke hain (outdated pricing docs). Sahi maintenance
step?
a) Ignore karo, Claude khud pata laga lega b) **Configurations/knowledge sources ko update/maintain
karo — Domain 5 explicitly "inform/maintain/update" ko objective mein rakhta hai** c) Poora Project
delete kar do d) Instructions delete kar do, knowledge rehne do

**43.** Ek associate Project instructions mein sensitive internal-only policy detail daal deta hai jo
external users bhi access karenge. Yeh kis tarah ka gap hai?
a) Prompting gap b) **Configuration + governance gap — knowledge management (Domain 5) aur data-
sensitivity (Domain 6) dono cross hote hain: sensitive content ko access-scope ke hisaab se configure
karna zaroori hai** c) Model selection gap d) Troubleshooting gap

**44.** Instructions aur knowledge sources ka farq kya hai configuration ke nazariye se?
a) Koi farq nahi b) **Instructions = behavior/format/tone guide karti hain ("kaise respond karo");
knowledge sources = factual grounding data provide karti hain ("kis info se respond karo") — dono
mil kar Project configure karte hain** c) Instructions optional hain d) Knowledge sources hamesha
zaroori nahi

**45.** Ek naya team-member Project use karta hai lekin outputs inconsistent aa rahe hain teammates ke
mukable. Sabse likely root cause?
a) Model change b) **Configuration drift/gap — shayad instructions clear nahi hain ya knowledge sources
sabke liye same tarah maintain nahi hue** c) Naya team-member ki galti d) Random Claude behavior, fix
nahi ho sakta

---

### Part 6 — Domain 6: Governance, Risk, and Responsible Use (15% · Q46–54)

**46.** Ek project manager customer names + account numbers wali spreadsheet upload karna chahta hai
trend-analysis ke liye; policy regulated personal data share karna restrict karti hai. Sabse
appropriate action?
a) As-is upload karo, analysis internal hai b) **Personal identifiers remove/anonymize karo upload se
pehle, policy ke mutabiq** c) Upload karo lekin Claude ko "retain mat karo" kaho d) Analysis poori
tarah skip kar do

**47.** "Appropriate vs inappropriate use case" identify karna Domain 6 ka pehla explicit objective hai.
Ek associate medical-diagnosis final decision Claude se leta hai bina doctor review ke — yeh kya hai?
a) Appropriate use, Claude accurate hai b) **Inappropriate/high-risk use case — regulated,
safety-critical decisions ko bina human/expert review ke Claude pe fully outsource karna governance
violation hai** c) Domain 3 ka issue d) Prompting issue

**48.** "Organizational AI policy follow karna" ka practical matlab kya hai roz-marra kaam mein?
a) Policy ignore karna agar deadline tight ho b) **Har task se pehle check karna ke woh org ki AI usage
policy (data handling, approved use cases, review requirements) ke andar hai** c) Sirf managers ke
liye applicable hai d) Sirf naye employees ke liye

**49.** Ek associate Claude se ek employee ke performance review draft karwata hai bina us employee ko
bataye ke AI use hua. Ethical-implications angle se yeh kya raise karta hai?
a) Koi issue nahi b) **Transparency/disclosure concern — AI-assisted decisions/content jo logon ko
significantly affect karte hain, unme appropriate disclosure/human oversight ka ethical sawal uthta
hai** c) Sirf Domain 3 ka issue d) Sirf technical issue

**50.** Regulatory-sensitive industry (healthcare/finance) mein Claude use karte waqt extra kya zaroori
ho jaata hai?
a) Kuch extra nahi b) **Regulatory-specific considerations (jaise HIPAA, financial-data rules) ko
governance judgment mein factor karna — same task, higher-stakes context** c) Sirf faster model use
karna d) Sirf zyada prompts likhna

**51.** Ek associate ek borderline use-case face karta hai jahan policy clear nahi hai. Sabse responsible
step?
a) Khud guess laga kar proceed karo b) **Escalate karo — governance/compliance/manager se clarify
karwao before proceeding, jab policy ambiguous ho** c) Task cancel karo permanently d) Ignore karo aur
publish kar do

**52.** Data-sensitivity considerations sirf "personal data" tak limited hain?
a) Haan b) **Nahi — Domain 6 data-sensitivity, regulatory, AUR privacy teenon ko cover karta hai;
confidential business data, trade secrets, regulated categories sab shamil hain, sirf PII nahi** c)
Sirf financial data d) Sirf health data

**53.** "Responsible use" ka ek core component Domain 6 mein ethical implications samajhna hai. Ek
example scenario jahan yeh directly apply hota hai?
a) Font choice karna b) **Claude-generated content ko bina disclosure ke real, human-authored content
ki tarah present karna, jab audience ko yeh farq matter karta ho** c) Model version choose karna d)
Prompt length decide karna

**54.** Governance judgment aur output-evaluation judgment (Domain 2 vs 6) mein core farq?
a) Koi farq nahi b) **Domain 2 = "kya yeh output accurate/complete hai?"; Domain 6 = "kya is content ko
generate/use/share karna appropriate, policy-compliant, aur ethical hai?" — dono alag questions hain,
dono zaroori hain** c) Domain 6 sirf legal team ke liye d) Domain 2 governance ko replace kar deta hai

---

### Part 7 — Domain 7: Troubleshooting and Optimization (10% · Q55–60)

**55.** Claude baar-baar off-topic/irrelevant output de raha hai ek repeated task ke liye. Pehla
diagnostic step?
a) Model change kar do immediately b) **Prompt/instructions ko diagnose karo — kya context missing
hai, kya request ambiguous hai — issue identify karo before fixing** c) Task abandon kar do d) Complain
karo AI kharab hai

**56.** Ek workflow jahan Claude use hota hai, expected se zyada time le raha hai per-task. Optimization
angle se sahi approach?
a) Ignore karo, time matter nahi karta b) **Workflow ko efficiency ke liye review karo — kya steps
combine ho sakte hain, kya galat model/feature use ho raha hai, kya prompt over-complicated hai** c)
Poora workflow delete kar do d) Sirf zyada log kaam pe lagao

**57.** Feedback milta hai ke ek Claude-assisted deliverable client ko pasand nahi aaya. Domain 7-aligned
response?
a) Ignore karo feedback ko b) **Feedback ke hisaab se approach adjust karo — prompt, configuration,
ya workflow step mein specific badlav lao based on that feedback** c) Client ko blame karo d) Kabhi
Claude use na karo dobara

**58.** "Underperforming prompt" diagnose karte waqt sabse pehla check kya hona chahiye?
a) Model version b) **Kya prompt mein clear goal, context, aur format specified tha — zyadatar
underperformance missing-context se aati hai, model se nahi** c) Internet speed d) User ka mood

**59.** Ek associate same issue baar-baar face karta hai (repeated poor output) lekin har baar sirf
"try again" karta hai bina kuch badle. Yeh kya miss kar raha hai?
a) Kuch nahi, yeh sahi approach hai b) **Root-cause diagnosis — Domain 7 explicitly "identify/diagnose/
resolve" kehta hai, sirf retry karna optimization nahi hai** c) Zyada retries chahiye the d) Model
kharab hai

**60.** Optimize karne ke baad bhi ek workflow step consistently underperform karta hai. Agla sahi step
(cross-domain judgment)?
a) Permanently ignore karo b) **Reconsider karo ke kya yeh task hi Claude ke liye appropriate fit hai
(Domain 4/3 ka sawal) — troubleshooting kabhi kabhi yeh reveal karta hai ke tool/approach mismatch tha,
sirf prompt issue nahi** c) Sirf retry karte raho forever d) Task delete kar do bina analysis ke

---

## Answer Summary (Quick Self-Check)

Domain distribution confirms coverage: **D1 (Q1–8)=8 · D2 (Q9–21)=13 · D3 (Q22–28)=7 · D4 (Q29–38)=10 ·
D5 (Q39–45)=7 · D6 (Q46–54)=9 · D7 (Q55–60)=6** — matches official weights (14/21/12/16/12/15/10%)
proportionally out of 60. Score by domain, not just total: guide ke apne rules ke mutabiq domain-wise
% sirf informational hai, lekin **prep ke liye woh hi sabse useful signal hai** — jis domain mein 50%+
galat hon, wahin dobara [01](01-domain-blueprint.md) parho.

---
[⬅ CCAO-F Index](README.md) · [06 — Easy Exam Guide](06-easy-exam-guide.md)
