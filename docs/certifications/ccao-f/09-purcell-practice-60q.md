# 09 — Matthew Purcell Practice 60Q (Full Answer Key, Roman Urdu Reference)

*Yeh **independent, third-party** practice set hai — Matthew Purcell (LinkedIn: purcellmatthew) ne
banaya, ek candidate jo CCAO-F pass kar chuka. Anthropic se affiliated nahi, live item bank se nahi
liya gaya (PDF ka apna disclaimer). Original PDF is folder mein hai:
[`Matthew-Purcell-CCAO-F-Practice-60Q.pdf`](Matthew-Purcell-CCAO-F-Practice-60Q.pdf).*

**Maqsad:** poora 60Q set (sawaal + sahi jawab + rationale) Roman Urdu mein, taake PDF khole bagair
bhi padha/revise kiya ja sake. Domain order aur numbering (1.1, 1.2, ...) PDF ke apne hi hain — 7
domains, [`01-domain-blueprint.md`](01-domain-blueprint.md) ke weights follow karte hue. Har item ke
sath ek chhota "kyun doosre options ghalat" note hai — PDF ke apne "Why not the others" se translate
kiya gaya.

---

## Domain 1 — Prompting and Task Execution (8 Q)

**1.1 — Generic product post.** Marketing associate "write something about our new product" likhta
hai aur generic result milta hai. Best revision?
A. "Better" likhna · **B. 150-word LinkedIn post, small-business audience, tone, waitlist CTA specify
karna ✅** · C. Same vague ask 3 baar repeat karna · D. Elaborate flattery persona, koi specifics nahi
**Explanation:** Effective prompt deliverable + length + audience + tone + goal deta hai — B sab
paanch dete hai. A pressure add karta hai info nahi; C wahi missing context repeat karta hai; D
persona deta hai lekin audience/format/purpose phir bhi missing.

**1.2 — Shallow quarterly review.** Budget+status+staffing+risks ek single prompt mein maangna
shallow/uneven coverage deta hai. Fix?
A. Word count double karna · B. "Try harder" kehna · C. Bullet points mein chhupana · **D. Decompose
karna: har section alag request, review, phir combine ✅**
**Explanation:** Task decomposition har section ko full attention deta hai, errors step-level pe pakre
jaate hain. A longer shallow coverage deta hai, depth nahi; B model ko actionable instruction nahi;
C problem hide karta hai, fix nahi.

**1.3 — Client email tone fix.** Draft bohot formal, request buried. Best iteration?
**A. Specific feedback: tone warm karo + request opening mein lao ✅** · B. Same prompt dobara bhejna
· C. Nayi conversation shuru karna · D. Khud manually sab edit karna
**Explanation:** Specific, actionable feedback deliberate revision enable karta hai. B aur C luck pe
depend karte hain (same input → same shortcomings); D fastest fix forfeit karta hai.

**1.4 — Brainstorm vs charter.** Naam brainstorm karna vs formal charter draft karna — strategy kaise
alag ho?
A. Identical prompt dono ke liye · B. Brainstorm strict, charter free-form (ulta) · **C. Brainstorm:
varied options + judgment defer; charter: structure + tone + constraints ✅** · D. Brainstorming
avoid karna
**Explanation:** Divergent task (brainstorm) volume/variety chahta hai; convergent task (charter)
explicit structure chahta hai. A dono tasks ke opposite goals ignore karta hai; B strategy ulti laga
deta hai; D factually galat hai — idea generation strongest use case hai.

**1.5 — Regional sales "analyze this".** Bland restatement milta hai. Genuinely useful analysis
request?
A. "Deeper/thorough" dobara kehna · **B. Specific: 3 sabse zyada declining regions identify karo,
explanations suggest karo, kuch unusual flag karo — retention decision ke liye ✅** · C. "World-class
data scientist" persona · D. Half-length summary mangna
**Explanation:** Analysis prompt questions + criteria + decision batata hai — "describe" ko "help me
decide" mein badalta hai. A/C sirf restyle karte hain, kya dekhna hai nahi batate; D compression
mangta hai, analysis nahi.

**1.6 — Technical incident report → exec briefing.** Sabse important prompt element?
A. Har technical detail rakhna · B. Longest output mangna · C. Aisi language jo audience samajhti hi
nahi · **D. Audience + needs state karna: non-technical execs, one page, customer impact/cost lead,
3 decisions ✅**
**Explanation:** Audience naam batana highest-leverage instruction hai adaptation tasks mein. A wahi
original problem recreate karta hai (execs detail mein doob jaate); B length ko value samajhta hai; C
nonsensical hai.

**1.7 — TWO elements for customer announcement.** ✅ **B.** Audience + purpose naam batana, ✅ **D.**
Format/length/tone specify karna.
**Explanation:** Yeh do cheezein model ko sahi target aim karne dete hain. A aur E exactly wahi info
withhold karte hain jis pe quality depend karti hai; C sirf emphasis badalta hai, understanding nahi.

**1.8 — Vendor audit → board summary, 5 activities order.** Sahi order?
A. 2→3→1→4→5 · **B. 3→2→1→4→5 ✅** · C. 3→2→4→1→5 · D. 2→4→5→1→3
**Explanation:** Requirements pehle (3) taake extraction aim ho; extract (2); verify before dependence
(1); draft from verified findings (4); refine last (5). A extraction ko purpose define karne se pehle
karta hai; C unverified findings se draft karta hai; D dono accuracy-check aur purpose-setting draft
ke baad tak delay karta hai.

---

## Domain 2 — Output Evaluation and Validation (13 Q)

**2.1 — Precise stat + citation.** "Sector grew 14.2%, annual report ke mutabiq" board paper ke liye.
Pehle kya chahiye?
A. Kuch nahi, precision + named source kaafi hai · B. Claude se confidence poochna · **C. Figure ko
actual report/authoritative source ke against verify karna ✅** · D. 14% round kar dena
**Explanation:** Specific-looking details + citations exactly hallucination jaisi dikhti hain. A
specificity ko reliability samajhta hai; B potentially-wrong source ko khud grade karne deta hai; D
error ko chhota karta hai, check nahi.

**2.2 — Narrative vs table contradiction.** Narrative "har region grew" kehta hai, table ek region
decline dikhata hai. Kya karna?
**A. Internal inconsistency — reliability warning. Dono ko source spreadsheet ke against check karo
aur correct karo ✅** · B. Narrative trust karna · C. Table trust karna · D. Dono ka average
**Explanation:** Jab output khud se contradict kare, koi ek galat hai — sirf source arbiter ho sakta
hai. B/C arbitrarily ek ko winner bana dete hain jabke koi bhi galat ho sakta hai; D meaningless
operation hai.

**2.3 — HR job ad, "young energetic digital native".** Appropriate response?
A. Publish kar do, AI text neutral hai · B. Zyada exciting banwana · C. Disclaimer add karke publish
karna · **D. Age-biased framing recognize karo, skills/competencies pe revise karo, AI-drafted HR
content ko bias ke liye review karna standard practice banao ✅**
**Explanation:** Models everyday-language biases reproduce karte hain — hiring content mein yeh
legal/ethical consequence rakhta hai. A false hai; B problem ko polish karta hai; C ad ke apne wording
ko contradict karta hai bina fix kiye.

**2.4 — Supplier contract clause, koi ghalti nazar nahi aa rahi.** Next step kya decide karta hai?
A. Supplier ko bhej do agar theek lage · **B. Stakes decide karte hain — legally binding language
qualified legal counsel se review chahiye, chahe draft kitna bhi polished ho ✅** · C. Claude se khud
apni clause double-check karwana aur uska confirmation maan lena · D. Clause chhota kar dena
**Explanation:** Human-review-kab-chahiye judgment consequences ke baare mein hai, confidence ke
nahi. A fluency ko legal soundness samajhta hai; C drafter ko khud apna kaam grade karne deta hai; D
risk kam nahi karta, sirf word count kam karta hai.

**2.5 — Research brief fact-check.** Genuine validation kaunsa hai?
A. Claude se khud confirm karwana · B. Brief dobara generate karke compare karna · **C. Har material
claim ko independent, authoritative sources ke against check karna ✅** · D. Sirf spelling/grammar
padhna
**Explanation:** Validation ka matlab hai model-se-bahar ground truth ke against compare karna. A
claim ke author ko hi referee bana deta hai; B consistency test karta hai, truth nahi; D polish check
karta hai, accuracy nahi.

**2.6 — 30-page policy → 1-page summary, completeness check.** Practical check?
A. Sirf length confirm karna · **B. Source ke section headings + key provisions ke against coverage
compare karna — represented ya consciously omitted ✅** · C. Claude se poochna kuch chhoota to nahi ·
D. Word count/compression ratio consistency count karna
**Explanation:** Omissions summary mein khud invisible hote hain — source ke structure ke against dekhna
padta hai. A/D length measure karte hain, coverage nahi; C summarizer se poochna wahi gap miss karega
jo usne pehle miss kiya.

**2.7 — Dense jargon-heavy analysis → customer panel.** Good output adaptation?
**A. Claude se rewrite karwana — plain language, defined terms, customer impact lead — phir accuracy
ke liye review ✅** · B. Original bhej dena · C. Technical sections delete karna · D. Dense version
rakh kar glossary appendix add karna
**Explanation:** Audience ke liye edit/adapt karna core evaluation skill hai — same substance, reshaped,
phir fresh accuracy check (rewriting naye errors la sakti hai). B kuch usable nahi deta; C substance
hata deta hai; D adaptation ka kaam reader par daal deta hai.

**2.8 — 3 alag outputs (quick fact, 4-vendor comparison, reusable brief) — sahi format?**
A. Sab artifacts · B. Sab inline · C. Brief inline, comparison separate message, fact artifact (ulta)
· **D. Quick fact inline; comparison structured table; reusable brief artifact ✅**
**Explanation:** Format use follow karta hai — transient answers inline, comparative data structure
mein, reuse/iterate wala content artifact mein. A/B ek hi format teeno jobs pe force karte hain; C
har output ko sabse kam-fit format deta hai.

**2.9 — Do sensitive apology drafts compare karna.** Soundest way?
A. Longer wala choose karna · **B. Criteria define karo (acknowledge, responsibility, remedy, voice
match), dono ko un criteria pe assess karo ✅** · C. Claude se khud dono compare karwana aur uska pick
bhej dena · D. Dono ko poora merge karna
**Explanation:** Comparison ek criteria-based kaam hai. A length ko quality ka proxy banata hai; C ek
accountable judgment outsource karta hai; D length double karta hai, tone kisi ka bhi nahi rehta.

**2.10 — Scattered findings, 3 colleagues ko agle hafte chahiye.** Kya karna?
A. Poora transcript forward kar dena · B. Memory pe rely karna aur agle hafte dobara poochna · **C.
Curate karo: Claude se validated findings ek organized document mein consolidate karwao, review/correct
karo, share karo ✅** · D. Har message spreadsheet row mein copy karna
**Explanation:** Curate/organize karna conversation ko ek work product mein badalta hai. A mess+dead-ends
teeno logon ko de deta hai; B gamble hai; D disorder ko doosre container mein preserve karta hai.

**2.11 — Internal custom expense tool, confident step-by-step instructions.** Kya recognize karna?
**A. Claude private company tool ke internals nahi jaan sakta — confident steps plausible invention
hain, internal docs se check karo ✅** · B. Confidence genuine knowledge indicate karta hai · C. Claude
screen dekh raha hai · D. Internal tools universal standards follow karte hain isliye generic steps
dependable hain
**Explanation:** Key evaluation skill hai "kya model asal mein yeh jaan sakta hai?" poochna. B fluency
ko knowledge samajhta hai; C ek capability attribute karta hai jo exist hi nahi karti; D wishful hai.

**2.12 — TWO signals extra verification chahiye.** ✅ **B.** Specific figures/quotations/citations jo
rely hongi. ✅ **E.** Recent events ya specialized facts jo associate khud confirm nahi kar sakta.
**Explanation:** Risk concentrate hota hai jahan claims specific, load-bearing, aur reviewer ki apni
verification-capability se bahar hon. A, C, D presentation qualities hain — accuracy ke baare mein
koi info nahi dete.

**2.13 — TWO practices standard validation ke liye.** ✅ **A.** High-stakes factual claims ko external
authoritative sources ke against check karna. ✅ **D.** Specialized content (legal/medical/financial)
qualified human reviewer ko route karna.
**Explanation:** Do pillars: independent sources + qualified human expertise — dono model-se-bahar
compare karte hain. B/C model ka apna signal recycle karte hain (self-confidence/self-agreement evidence
nahi); E spelling check karta hai, jo risk kabhi tha hi nahi.

---

## Domain 3 — Product and Model Selection (7 Q)

**3.1 — Har mahine same 12 docs + rules re-upload karna.** Overhead remove karne wala feature?
A. Research mode (web se documents dhoondna) · B. Longer first message · **C. Claude Project — docs
knowledge mein, rules/rubric instructions mein, har chat equipped shuru hoti hai ✅** · D. Claude ko
"pichle mahine se yaad rakho" kehna
**Explanation:** Projects recurring work ke liye hain — knowledge+instructions ek baar configure, har
conversation mein apply. A private docs ke liye public web search karta hai; B setup manually repeat
karta hai; D cross-chat recall pe rely karta hai jo assume nahi karni chahiye.

**3.2 — Comprehensive market overview, multiple current sources + citations chahiye.** Approach?
A. Plain chat, training knowledge pe rely · **B. Research capability use karna — multi-source, current,
cited report ✅** · C. Haiku format se conciseness force karna · D. Purana report upload karke guess
karwana kya badla hoga
**Explanation:** Feature selection depth ko tooling se match karta hai. A outdated/uncited answer deta
hai; C format gag hai method nahi; D researched info khud invent karwata hai.

**3.3 — Client proposal, kayi rounds revision expect hain.** Best way of working?
A. Har revision naya pasted block, scroll karke compare · B. Poora proposal har message mein retype
karna · C. Ek paragraph per conversation, alag chats mein · **D. Artifact ke tor par develop karna —
ek evolving document, revise/review/handoff ✅**
**Explanation:** Artifacts substantial content ke liye ghar hain jo iterate ho raha ho — ek canonical
version. A scrollback mein versions bury karta hai; B manual duplication hai; C ek document ko
disconnected contexts mein fragment karta hai.

**3.4 — Nuanced synthesis (3 conflicting reports) vs 200 addresses reformat.** Model choice kaise
differ kare?
**A. Synthesis: sabse capable model (reasoning quality matter karti hai); reformatting: fast/low-cost
model ✅** · B. Dono fastest · C. Dono most capable · D. Ulta assign karna
**Explanation:** Model tiers task-need match karte hain. B reasoning-heavy task underpower karta hai; C
light-model-equivalent task pe overpay karta hai; D dono logic ulti kar deta hai.

**3.5 — High-volume routine replies, koi complex reasoning nahi.** Sahi tier + confirmation?
A. Highest-cost tier hamesha · B. Tiers din ke hisaab se alternate karna · **C. Fast/low-cost tier
(Haiku-class), sample drafts spot-check karke standardize karna ✅** · D. Jo tier recently use hui wahi
**Explanation:** Yeh textbook high-volume/low-complexity profile hai fast tier ke liye. A premium
pay karta hai jo task use nahi kar sakta; B/D selection logic hi nahi hain.

**3.6 — Long planning conversation ke important decisions, weeks ke liye matter karte hain.** Durable
kaise banaya jaye?
A. Future chats mein Claude yaad rakhega, trust karna · **B. Deliberately persist karna — Claude se
decision summary banwao, verify karo, kisi durable jagah (Project knowledge) save karo ✅** · C.
Conversation tab hamesha khula rakhna as system-of-record · D. Poori conversation dobara repeat karna
jab bhi chahiye
**Explanation:** Memory considerations manage karna matlab jaanna kya persist hota hai — aur act karna.
A galat recall assume karta hai; C ek browser tab ko single point of failure banata hai; D full cost
dobara pay karta hai.

**3.7 — TWO situations jo Project ke liye call karte hain.** ✅ **A.** Recurring task jahan har
conversation same reference docs+instructions use kare. ✅ **D.** Team consistent behavior chahti hai
(shared context/tone/rules) sab conversations mein.
**Explanation:** Projects stable, reused context mein shine karte hain. B ko koi setup chahiye hi nahi;
C/E powers attribute karte hain jo Projects ke paas nahi (model speed badhana, context limits khatam
karna).

---

## Domain 4 — Workflow Integration and Solution Design (10 Q)

**4.1 — 40 pages raw interview notes.** Requirements-analysis stage mein Claude kaise best support
kare?
A. Claude khud final requirements decide kar le, stakeholders dobara consult na karna · **B. Notes ko
themes mein organize karna, needs/pain-points extract karna, structured requirements list draft
karna — analyst validate kare stakeholders se ✅** · C. Notes skip karke generic "intranets usually
require" poochna · D. Sirf grammar fix
**Explanation:** Claude labor-intensive middle (structuring) mein excel karta hai; judgment steps
(validation/prioritization) analyst ke paas rehte hain. A stakeholders ko unki apni needs ke decisions
se hata deta hai; C generic patterns substitute karta hai; D synthesis engine ko spell-checker bana
deta hai.

**4.2 — Office relocation, blank page se credible plan.** Effective use?
A. Final approved plan Claude se maangna, unedited circulate karna · B. Claude avoid karna · C.
Claude ko sirf baad mein slides banane ke liye use karna · **D. Claude se first-pass plan draft
karwana (workstreams, sequencing, risks, stakeholders), phir real org/budget knowledge se refine
karna ✅**
**Explanation:** Research/planning support ka matlab hai blank-page-problem Claude se beat karna,
phir human context se correct/complete karna. A reality-untested plan publish karta hai; B hours
forfeit karta hai; C decoration ke liye reserve karta hai.

**4.3 — Invoice-approval process inefficient lagta hai, pata nahi kahan.** Process optimization mein
Claude kaise support kare?
**A. Process step-by-step describe karna, Claude se likely bottlenecks/redundant approvals/questions
identify karwana, phir real data se verify karna ✅** · B. Claude ko khud invoices approve karne dena
· C. Motivational memo banwana · D. Process wholesale replace kar dena Claude ke "best practice"
suggestion se
**Explanation:** Claude analytical partner hai — hypotheses generate karta hai jo data se verify hote
hain. B analysis se unsupervised financial-control execution tak jump karta hai; C theater hai; D
evidence ke bagair generic template swap karta hai.

**4.4 — Content workflow (research→outline→draft→review→publish), draft stage bottleneck hai, review
theek chal raha hai.** Integration kaise?
A. Poora workflow (review sameet) ek Claude step se replace karna · B. Claude ko publishing stage pe
insert karna · **C. Bottleneck augment karna — Claude structured first drafts banaye outlines se,
research direction + expert review wahi rahein ✅** · D. Har stage ka time zyada precisely measure
karna
**Explanation:** Good integration surgical hota hai — jo stage actually throughput rok rahi hai wahi
target karo, jo kaam kar raha hai (human quality gate) usay chhedo mat. A safeguard hata deta hai; B
galat stage optimize karta hai; D bottleneck measure karta hai, relieve nahi.

**4.5 — Weekly client-reporting workflow mein Claude integrate karna, 5 activities order.** Sahi
order?
A. 4→3→2→5→1 · B. 3→2→4→5→1 · C. 2→4→3→1→5 · **D. 2→4→3→5→1 ✅**
(Map+baseline → select highest-value/lowest-risk stage → pilot → evaluate vs baseline → scale)
**Explanation:** Pehle understand karo phir change karo, prove karo phir scale karo. A workflow samjhe
bagair stage select karta hai; B decide karne se pehle pilot karta hai; C poori team ko scale kar deta
hai evaluation se pehle.

**4.6 — TWO strongest candidates for Claude support (5 activities: inbox triage, negotiations,
status report, invoice approval, mentoring).** ✅ **A.** Inbox triage — Claude drafts categorization,
worker reviews. ✅ **C.** Status report — Claude drafts, worker reviews/edits.
**Explanation:** Frequent, high-volume text tasks jahan human final judgment rakhta hai, best fit hain.
B/E relationship work hain (negotiation/mentoring) jo human presence/trust maangte hain; D Claude ko
autonomous financial-control decision de deta hai.

**4.7 — Successful pilot, skeptical leadership ko present karna.** Sahi approach?
**A. Concrete outcomes report karna (6hr→2hr, quality maintained) + honest limitations ✅** · B.
"Flawless" claim karna budget ke liye · C. Sirf limitations present karna · D. Koi specific numbers na
dena, taake challenge na ho sake
**Explanation:** Value communicate karna evidence + honesty hai. B expectations tod dega; C genuine
result ko cautious-theater mein bury karta hai; D unfalsifiability ke liye credibility trade karta hai.

**4.8 — Team automatic CRM-integrated triage chahti hai (API, auto-trigger).** Kya karna?
A. Khud weekend mein CRM API build kar lena Claude-generated code se · B. Team ko batana yeh impossible
hai · **C. Recognize karna yeh technical implementation mein cross ho gaya — developer/Architect ko
escalate karna ✅** · D. Manually har naya ticket copy-paste karke simulate karna
**Explanation:** Associate competency ki boundary jaanna zaroori hai — API integration engineering
scope hai. A production engineering ko role ke safety net se bahar le jata hai; B false hai; D ek
insaan ko manual API bana deta hai.

**4.9 — TWO practices jo pilot ko trustworthy banate hain.** ✅ **B.** Frequent, low-risk task chuno
jahan outputs reality ke against easily check ho sakein. ✅ **D.** Success measures (time/quality/
adoption) pehle se define karna.
**Explanation:** Sensible proving ground + advance-fixed criteria = measurement, impression nahi. A/C
blast radius maximize karte hain kuch prove hone se pehle; E baseline hata deta hai jo numbers ko
meaning deta.

**4.10 — TWO uses jo competitive-landscape briefing mein genuine value add karein.** ✅ **A.**
Collected articles/reports ko organized themes + disagreement points mein synthesize karna. ✅ **C.**
Structured comparison draft banana as reviewable starting point.
**Explanation:** Claude ka contribution structure + speed hai — human phir verify/judge karta hai. B,
D, E Claude ko truth ka final authority ya autonomous decision-maker bana dete hain — jo human ke paas
rehna chahiye.

---

## Domain 5 — Configuration and Knowledge Management (7 Q)

**5.1 — Har conversation mein same 3 paragraphs (tone/structure/format) paste karna.** Sahi
configuration fix?
A. Har baar paste karte rehna, repetition se "seekh" jayega (galat mechanic) · B. Paragraphs chhote
karna · C. Knowledge file ke tor par attach karke umeed rakhna Claude notice karega · **D. Standing
rules ko Project custom instructions mein daalna — har conversation mein automatically apply hote
hain ✅**
**Explanation:** Behavioral rules Project instructions ke liye hain — ek baar configure, har chat mein
apply, bhoolne ka scope hi nahi. A galat mechanic samajhta hai (kuch bhi chats ke beech "seekha" nahi
jata); C behavioral rules ko reference-content ki jagah rakhta hai, force kamzor karta hai.

**5.2 — 2,000 files wali drive, sirf 15 relevant.** Knowledge mein kya upload kare?
A. Poori 2,000-file drive · **B. 15 relevant, current documents — curated knowledge base, maintained
✅** · C. Kuch bhi nahi, "prompts hi kaafi hain" · D. Sirf sabse purani files
**Explanation:** Knowledge curation volume se behtar hai — focused set precise retrieval deta hai. A 15
signal docs ko 1,985 noise/stale files ke neeche bury karta hai; D bilkul galat property optimize karta
hai.

**5.3 — Team ke status-report docs Google Drive mein, kayi log update karte hain.** Sahi approach +
pehle kya check kare?
**A. Google Drive connector use karna — Claude current files directly access kare — pehle data/access
policy compliance confirm karke ✅** · B. Har subah manually re-upload karna · C. Colleagues ko update
karna band karne ko kehna · D. Claude ko guess karwana kya badla
**Explanation:** Connectors exactly isi ke liye hain — live access, stale snapshots ki jagah. B manual
overhead hai jo feature khatam karta hai; C tooling gap ke around process bend karta hai; D invention
invite karta hai.

**5.4 — Best system-level instructions kaunsi hain?**
A. "Hamesha helpful/professional raho, achha kaam karo, judgment use karo" (vague aspirations) · B.
"Never make mistakes" (meaningless) · **C. "Customer-service replies draft karo. Tone: warm, plain
English. Always: issue acknowledge karo, next steps batao. Never: refund promise mat karo (escalate
karo), 200 words se zyada mat likho." ✅** · D. Poori 30-page policy manual paste karna as instructions
**Explanation:** Effective instructions specific, structured, behavioral hote hain — always/never
rules har turn pe actionable hain. A/B aspirations hain, behavior kuch nahi badalte; D operative rules
ko archive material ke neeche drown karta hai.

**5.5 — Behavioral rules (tone/escalation) vs reference material (catalog/policy docs) — kahan
jayein?**
A. Dono har chat ke first message mein paste karna · **B. Behavioral rules → custom instructions;
reference material → Project knowledge ✅** · C. Dono knowledge files, instructions empty · D. Ulta —
rules knowledge mein, catalog instructions mein
**Explanation:** Do configuration surfaces ka alag kaam hai: instructions har turn behavior govern
karte hain; knowledge reference library hai jo relevant hone par consult hoti hai. C configuration ko
manual repetition se replace karta hai; D dono surfaces ko poori tarah invert karta hai.

**5.6 — Quoting Project superseded prices cite kar raha hai (pricing_2024.xlsx purana).** Proper
knowledge maintenance?
A. Har baar chat instruction "purani prices ignore karo" · B. Naya pricing file purane ke sath upload
karna (dono rehte hain) · C. Reps ko mentally adjust karne kehna · **D. Purani file remove karo, naya
pricing document upload karo, knowledge sources ko review cycle pe daalo ✅**
**Explanation:** Configuration maintain karna matlab knowledge base ko reality ke sath sync rakhna —
stale sources sirf supplement nahi, remove hone chahiye, plus review cadence. A per-chat incantation
hai; B do contradictory sources ko retrieval ke liye compete karwata hai.

**5.7 — Project setup, 5 activities order.** Sahi order?
A. 4→1→2→3→5 · B. 2→3→4→5→1 · **C. 4→2→3→1→5 ✅** (Create → instructions → knowledge → test → refine)
· D. 4→2→3→5→1
**Explanation:** Project pehle exist kare (4), phir configuration — instructions+knowledge (2,3) —
evaluation se pehle, aur refinement (5) tabhi meaningful hai jab test (1) ne kuch reveal kiya ho. A
unconfigured Project test karta hai; D test se pehle refine karta hai.

---

## Domain 6 — Governance, Risk, and Responsible Use (9 Q)

**6.1 — Appropriate, low-risk use bina extra approvals ke?**
A. Regulator ko official response bina human review ke bhej dena · B. Unredacted customer identity
records analyze karna · **C. Apne rough meeting notes ko organized minutes mein badalna, sharing se
pehle review karna ✅** · D. Employee ke symptoms ka diagnosis generate karna
**Explanation:** Data-sensitivity + stakes + oversight weigh karna hai. C internal, user-authored,
human-reviewed hai — safe zone. A high-stakes external communication hai review step ke bagair; B
regulated personal data bina safeguard ke; D professional medical judgment hai.

**6.2 — HR turnover analysis, spreadsheet mein names/salaries/health-leave records.** Sahi approach?
A. As-is upload, "internal analysis count nahi hota" (galat) · **B. De-identify pehle — identifiers
remove/pseudonymize, sirf zaroori fields rakho, policy compliance confirm karo ✅** · C. Upload karke
Claude ko "confidential treat karo" bolna · D. Sirf names column analyze karna
**Explanation:** Data-sensitivity practice minimization hai. A galat hai — tool ko data dena disclosure
event hai; C ek chat message ko control ki jagah use karta hai; D ulta hai — identifiers rakhta hai,
analysis discard karta hai.

**6.3 — Healthcare client, patient-feedback records se themes nikalna.** Records process karne se
pehle kya chahiye?
A. Proceed karna, "feedback records medical jaisa nahi lagta" · B. Proceed karke baad mein delete karna
· C. Chhota sample pehle chalake dekhna koi object karta hai ke nahi · **D. Regulatory/contractual
position pehle confirm karna — client ki privacy/compliance function se, sirf unki approval ke
mutabiq process karna ✅**
**Explanation:** Regulated data categories default ulat dete hain — authorization processing se pehle
aata hai. A vibes se regulatory analysis substitute karta hai; B violation ka evidence delete karta
hai, prevent nahi; C violation ko chhota karta hai, lawful nahi banata.

**6.4 — Teammate confidential docs personal free AI account mein paste kar raha hai.** Governance-correct
response?
**A. Problem explain karo, sanctioned workspace ki taraf direct karo, data-exposure reporting process
follow karo ✅** · B. Ignore karna, "same model hai" · C. Khud bhi join kar lena budget bachane ko · D.
Chat history chupke se delete karke kuch na kehna
**Explanation:** Sanctioned channels use karna governance hai — enterprise workspace ke contractual
protections/admin controls exist karte hain. B/C model quality ko governance samajhte hain (asal issue
account terms hain); D exposure aur behavior dono ko chhupa deta hai.

**6.5 — Fictional customer testimonials likhna (marketing ke liye).** Response?
A. Likh dena, "har company polish karti hai" · **B. Decline karna aur explain karna ke fabricated
testimonials deceptive hain — legitimate alternatives offer karna ✅** · C. Sirf first name attribute
karna to risk kam kare · D. "Illustrative" footnote add karke likh dena
**Explanation:** Ethical use deception pe line kheenchta hai — false social proof public ko mislead
karta hai chahe kisi ne bhi type kiya ho. A fabrication ko normalize karta hai; C/D wahi deception ka
cosmetic version hain.

**6.6 — AI-assisted vendor report mein error, director ko submit hua, problem cause hui.** Accountable
kaun?
A. Claude, sentence generate karne ki wajah se · B. Anthropic, tool banane ki wajah se · **C. Associate
jisne report author/submit ki — AI assistance accountability transfer nahi karta ✅** · D. Koi bhi
nahi, "accepted cost"
**Explanation:** Accountability authorship+submission follow karta hai, typing nahi. A/B tool ko
responsible party samajhte hain — koi organization "software ne likha" ko accountability nahi maanta;
D world describe karta hai jahan koi AI-assisted work trust nahi ho sakta.

**6.7 — Colleague poochta hai "mujhe kaunsa custody arrangement legally milega" — khud act karne ke
liye.** Kya recognize karna?
**A. Yeh professional legal advice ka substitute maang raha hai high-stakes personal matter pe —
determination qualified lawyer ke paas jani chahiye ✅** · B. Claude ka jawab binding hoga · C. Theek
hai agar jurisdiction specify ki jaye · D. Family law "simpler" hai isliye theek hai
**Explanation:** Inappropriate-use recognition mein substitution test hota hai — jab ask ek professional
determination hai jis pe koi act karega, tool ka role sirf preparation/understanding tak simat jata
hai. B false legal force attribute karta hai; C ek input detail fix karta hai, category problem nahi;
D false hai.

**6.8 — TWO checks dataset upload se pehle.** ✅ **B.** Kya dataset mein personal/confidential/regulated
info hai jo remove/de-identify/special-handle honi chahiye. ✅ **D.** Kya organization ki AI/data
policy is data-category ko is tool/workspace mein allow karti hai.
**Explanation:** Pre-upload discipline ke do gates hain — data inspect karo, aur intended use policy
ke andar confirm karo. A, C, E incidental/aesthetic properties hain, appropriateness se koi lena-dena
nahi.

**6.9 — TWO practices team ke responsible-AI norms mein.** ✅ **A.** AI assistance disclose karna jahan
policy/context require kare. ✅ **C.** Humans ko people-affecting decisions (hiring, performance,
customer commitments) mein accountable rakhna, AI ko support tak limit karna.
**Explanation:** Transparency + human accountability responsible-use norms ka core hain. B highest-stakes
jagah review step hata deta hai; D circular validation hai; E healthy culture ko invert karta hai —
scrutiny hi safeguard hai.

---

## Domain 7 — Troubleshooting and Optimization (6 Q)

**7.1 — Competitive-analysis answers generic/surface-level aa rahe hain.** Pehle kya examine kare?
A. "Bad day" maan kar kal retry karna · **B. Prompt khud — kya company context, competitors, decision,
aur criteria diye gaye hain? ✅** · C. Subscription tier · D. Din ka waqt
**Explanation:** Diagnosis input se shuru hoti hai — generic output context-starved prompt ka signature
hai. A, C, D external causes dhoondte hain jabke cause almost hamesha prompt text mein hi visible hota
hai.

**7.2 — 14-requirement mega-prompt, output kabhi 2-3 requirements drop kar deta hai (alag har baar).**
Cause + fix?
A. Model deliberately selective hai, "total obedience" line add karo · B. 14 requirements fundamentally
impossible hain, aadhe permanently delete kar do · C. "Please" na kehna hi problem hai · **D.
Instruction overload — requirements group/prioritize karo, ya sequential steps mein decompose karo ✅**
**Explanation:** Har baar alag requirements drop hona classic overload signature hai. A ek capacity
pattern ko defiance samajhta hai; B achievable requirements discard karta hai; C superstition hai.

**7.3 — Client-reporting Project mein har conversation wrong tone se start hoti hai, user har baar
manually correct karta hai.** Sahi fix?
**A. Source pe fix karo — Project custom instructions mein required tone specify karo, har conversation
correct start ho ✅** · B. Manually correct karte rehna, "sirf ek-do messages lagte hain" · C. Team ko
default accept karne kehna · D. Har chat ko insult se start karna
**Explanation:** Ek defect jo har conversation mein repeat ho, ek configuration defect hai, conversation
defect nahi. B configuration ke exist hone ke bawajood rework institutionalize karta hai; D noise hai —
tone instructions se set hoti hai.

**7.4 — Marathon conversation, Claude earlier drafts conflate kar raha, slow, corrections miss kar
raha.** Kya ho raha hai + response?
A. Model permanently degraded hai, account reset karo · B. "Kuch galat nahi, length se koi farq nahi
padta" · **C. Accumulated context lamba/muddled ho gaya. Claude se current state summarize karwao,
verify karo, fresh conversation mein seed karke continue karo ✅** · D. Corrections CAPITAL LETTERS mein
type karna
**Explanation:** Lambi, multi-topic conversations context accumulate karti hain jo eventually against
kaam karti hai. Restart-with-summary pattern jo matter karta hai rakhta hai, clutter shed karta hai. A
account-level condition ko misattribute karta hai; B symptom hi deny karta hai; D wahi overloaded
context mein emphasis add karta hai.

**7.5 — Har hafta 15 minute same report requirements re-explain karna.** Sahi optimization?
A. 15 minute cost accept karna · **B. Setup reusable banana — standing requirements ek baar Project
instructions mein capture karo, har hafta seedha kaam se shuru ho ✅** · C. Explain karna band karke
lower-quality accept karna · D. Weekly task team mein rotate karna
**Explanation:** Optimization repeated overhead target karta hai — har cycle identically explain hone
wali cheez reusable configuration mein jani chahiye. A recurring cost pay karta hai jabke one-time fix
available hai; D waste ko redistribute karta hai, eliminate nahi.

**7.6 — TWO practices jo underperforming prompt improve karne ko reliable banate hain.** ✅ **C.** Ek
waqt mein ek element change karna, taake har change ka effect attribute ho sake. ✅ **E.** Har revision
ko same example input pe test karna, like-for-like comparison ke liye.
**Explanation:** Reliable iteration ek fair experiment hai — ek cheez vary karo, test input constant
rakho, farq observe karo. A/B attribution destroy karte hain (sab kuch ek sath change hone se kuch seekha
nahi jata); D tool-hopping diagnosis ki jagah leta hai.

---
[⬅ Chapter Index](README.md) · [07 — Full Mock (60 Q, in-repo)](07-full-mock-60q.md) ·
[Supplementary PDF](Matthew-Purcell-CCAO-F-Practice-60Q.pdf)
