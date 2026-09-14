# PCAO-F — Extreme Prep: "Beyond CCAO-F" Quiz (24 Questions, Complexity 10/10)

*3 din baaki hain proctored PCAO-F tak (18 September 2026) — yeh file isi urgency ke liye bani hai.*

**Yeh `quiz100.md`/`hardquiz.md` (dono `../ccao-f/`) ka duplicate NAHI hai.** Un dono files ne
CCAO-F ke saat shared domains already extreme-difficulty par cover kar diye hain — is file mein
woh dobara nahi hai. Yeh sirf woh hissa cover karti hai jo **PCAO-F CCAO-F se aage jaata hai**
("same blueprint, one level up" — dekho [`README.md`](README.md)): vendor-neutral product/model
class-of-decision, configuration/knowledge-management ka general layer, regulated-client
governance, aur "client ko pehle batao yeh kya nahi karega" wala professional layer.

**Kaise use karo:** Pehle `../ccao-f/hardquiz.md` (ya kam se kam `quiz100.md`) solid score ke sath
kar chuke ho — yeh us par build karti hai. Har question ka **stem lamba aur complex** hai (jaan
boojh kar — 10/10), lekin har **rationale jaan-boojh kar simple rakha gaya hai** — chhote
sentences, aasan lafz, taake exam se 3 din pehle dimagh mein turant baith jaye. Complex scenario +
simple explanation — dono sath.

**Grounding:** `README.md` ka "Same Blueprint, One Level Up" section (gen 71, 2026-09-13 fetch) +
`../ccao-f/01-domain-blueprint.md` (Domain 3/5/6 objectives) + book ke apne crash courses
(`what-ai-actually-is-crash-course`, `claude-chatgpt-101-crash-course`,
`governance-risk-responsible-use-crash-course`, `skills-connectors-crash-course`). Koi live
item-bank content nahi — PCAO-F ka apna item bank public nahi hai, yeh self-authored practice hai.

---

## Section A — Vendor-Neutral Product/Model "Class of Decision" (Q1–Q7)

### Q1

Zainab ek 40-person marketing agency mein AI lead hai. Unki team do tools use karti hai: Claude aur
ChatGPT, dono enterprise plans par. Ek copywriter, Bilal, roz 15-20 chhote social captions likhta
hai — har ek 1-2 lines, koi deep research nahi, koi lamba context nahi chahiye. Bilal complain karta
hai ke uska sabse mehenga model use karna "zyada creative" feel hota hai, isliye woh hamesha top-tier
model (Opus-class ya GPT ka top-tier) use karta hai, chahe kaam simple ho. Zainab ko cost report
dikhti hai: Bilal ka monthly usage baaki 5 copywriters se 4x zyada hai, output quality mein koi
noticeable farq nahi. Zainab kya decide kare?

- A. Bilal ko rokna nahi chahiye — "creative feel" hi quality ka signal hai, subjective judgment
  respect karni chahiye.
- B. **✅ Task ki class define karo (short, low-ambiguity, high-volume caption writing) aur us class
  ke liye ek cheaper/faster model default set karo — sirf genuinely novel ya brand-risk-heavy
  captions ke liye top-tier model reserve karo.**
- C. Sab copywriters ko sirf ek hi tool (Claude ya ChatGPT, jo bhi sasta ho) use karne ka order do.
- D. Bilal se kaho apna kaam khud bina AI ke karo taake cost zero ho jaye.

**Sahi jawab: B**

Simple wajah: Chhota, aasan kaam ke liye sabse mehenga model use karna zaroori nahi hai. Zainab ko
kaam ka type dekhna chahiye — agar kaam simple hai, sasta/tez model kaafi hai. Sirf mushkil ya
risky kaam ke liye mehenga model rakho. A galat hai kyunki "feel" ek proof nahi hai — data khud
keh raha hai quality same hai. C bahut zyada hai — poora tool hata dena zaroori nahi, sirf model
choice sudharni hai. D AI ko chhod dena hai, jo waste hai jab AI kaam kar sakta hai — sirf sahi
model chuno.

---

### Q2

Ek hospital ka compliance officer, Dr. Hina, do AI assistants compare kar rahi hai apne team ke
liye: ek jismein "extended thinking" ya "deep research mode" hai (lamba sochta hai, zyada steps
leta hai, mehenga aur slow hai), aur ek regular fast mode. Unka use-case: patient-facing FAQ
documents draft karna jo pehle se clear template follow karte hain — sirf naye facts fill karne
hain. Kaunsa mode sahi hai, aur kyun?

- A. Deep research mode — patient-facing content hamesha sabse careful mode mein banna chahiye.
- B. **✅ Regular fast mode — kaam template-filling hai, deep multi-step reasoning nahi chahiye;
  "careful" ka matlab slow mode nahi, review process hai.**
- C. Dono modes ek sath use karo, jo bhi better output de wahi rakho.
- D. Mode ka koi farq nahi padta jab tak final review insaan kare.

**Sahi jawab: B**

Simple wajah: "Deep thinking" mode tab chahiye jab kaam mein sochna, plan banana, ya research
karna ho. Yahan sirf template mein naye facts daalne hain — yeh simple kaam hai. Careful hone ka
matlab hai ke koi insaan output check kare, na ke AI ko slow mode mein daal do. A confuse karta hai
"careful" ko "slow mode" ke sath — yeh do alag cheezein hain. D theek keh raha hai review zaroori
hai, lekin galat keh raha hai mode se farq nahi padta — mode se cost aur speed dono par farq padta
hai.

---

### Q3

Ek law firm ka paralegal, Omar, ek 90-page contract ko ek hi conversation mein upload karta hai aur
poochta hai "sab clauses summarize karo." AI ka jawab pehle 30 pages ke liye detailed hai, phir
progressively shorter hota jaata hai, aakhri 20 pages ka summary sirf 2 lines mein hai. Omar sochta
hai model "lazy" ho gaya. Iska asal wajah kya hai, aur fix kya hai?

- A. Model ne jaan-boojh kar kaam kam kiya — dobara "please be thorough" bol kar dobara try karo.
- B. **✅ Lamba context degrade karta hai — jitna zyada text ek sath diya jaye, utna zyada model
  beech/aakhir ka detail miss karta hai ("lost in the middle"). Fix: document ko chunks mein todo
  (jaise 20-30 pages ke groups), har chunk alag se summarize karwao.**
- C. PDF format hi problem hai — Word file use karni chahiye thi.
- D. Ek naya session start karo aur wahi sawal dobara poochho.

**Sahi jawab: B**

Simple wajah: Bahut zyada text ek sath dene se AI beech ka ya aakhir ka hissa bhool sakta hai —
yeh sabhi bade models mein hota hai, ek known limitation hai. Isko "lost in the middle" kehte hain.
Fix simple hai: bara document chhote hisson mein todo, har hisse ka alag summary lo. A galat hai
kyunki model ne jaan-boojh kar kuch nahi kiya, yeh ek predictable pattern hai. C format ka masla
nahi hai. D bhi wahi lamba text dobara dega — same problem repeat hogi.

---

### Q4

Ek startup ka founder, Ayesha, apni team se kehti hai: "Jab bhi conversation lambi ho jaye aur AI
confuse lagne lage, hum bas naya session start kar dete hain — purana context bilkul chhod dete
hain." Uska co-founder, Talha, kehta hai isse important decisions/context bhi kho jaate hain. Dono
sahi aur ek adhoora hai — sahi approach kya hai?

- A. Talha sahi hai — kabhi bhi naya session start nahi karna chahiye, hamesha purana continue karo.
- B. Ayesha sahi hai — hamesha naya session best hai, purana context noise hi hota hai.
- C. **✅ Dono partially sahi hain — agar same task continue ho raha hai, pehle summarize/compact
  karo (important decisions/facts ek chhote note mein save karo), phir naya session us note ke
  sath shuru karo. Agar poori tarah naya/unrelated task hai, tab fresh session theek hai.**
- D. Session restart karna ek technical setting hai jo sirf IT team decide kar sakti hai.

**Sahi jawab: C**

Simple wajah: Agar same kaam continue karna hai, purani important baatein pehle ek chhote note
mein likh lo, phir naya session usi note ke sath shuru karo — kuch bhi nahi khota. Agar bilkul naya
kaam hai jiska purane se koi lena dena nahi, tab seedha naya session theek hai, purana chhod do.
Yeh do alag situations hain, isliye ek hi jawab dono ke liye sahi nahi ho sakta. D irrelevant hai —
yeh IT setting nahi, roz ka kaam-karne ka tareeqa hai.

---

### Q5

Ek retail company apne customer-support team ke liye AI product choose kar rahi hai. Option 1:
sasta, tez, chhota context window. Option 2: mehenga, thora slow, bara context window. Unka
use-case: har customer ka pura purchase history (kabhi kabhi 200+ orders) padh kar personalized
jawab dena. Sahi choice ka reasoning kya hona chahiye?

- A. Hamesha sasta option chuno — cost sabse important factor hai.
- B. Hamesha mehenga option chuno — customer-facing kaam mein hamesha best chahiye.
- C. **✅ Task ki requirement dekho: yahan bara context (200+ orders padhna) genuinely chahiye,
  isliye bara-context option zaroori hai — cost yahan secondary hai kyunki chhota-context option
  task hi poora nahi kar sakta.**
- D. Dono options mila kar use karo — ek se order history nikalo, doosre se jawab likho.

**Sahi jawab: C**

Simple wajah: Sahi choice hamesha kaam se shuru hoti hai, price se nahi. Yahan kaam ko bahut sara
purchase history padhna hai — agar tool ka context window chhota hai, woh kaam kar hi nahi
payega, chahe kitna bhi sasta ho. Isliye pehle dekho kaam ko kya chahiye, phir uske hisaab se
option chuno. A aur B dono hamesha-ek-hi-jawab wali soch hai, jo galat hai — sahi jawab task par
depend karta hai.

---

### Q6

Ek NGO ka program manager, Sana, ek AI assistant ko apne team ke liye choose kar rahi hai jo
weekly donor-reports likhega. Uska ek colleague suggest karta hai: "Jo bhi tool latest/newest hai
wahi best hoga, purana version drop kar do." Sana confuse hai. Sahi approach kya hai?

- A. Hamesha latest version use karo — newer hamesha better hota hai.
- B. **✅ Version ko task ke against test karo pehle (kuch sample reports banwa kar dekho), phir
  decide karo — "naya" ka matlab "is specific kaam ke liye behtar" nahi hota, kabhi naya version
  kisi cheez mein different trade-off leta hai.**
- C. Purane version par hamesha rehna chahiye, kyunki naya version unpredictable hai.
- D. Version ka koi farq nahi padta, sirf prompt quality matter karti hai.

**Sahi jawab: B**

Simple wajah: "Naya" hamesha "behtar for my kaam" ka matlab nahi hota. Sahi tareeqa hai: pehle
test karo — us specific kaam (donor-reports) par naya version try karo, dekho kaisa result deta
hai, phir faisla lo. A aur C dono bina test kiye faisla kar rahe hain, jo risky hai. D bhi galat
hai — prompt achhi ho phir bhi model/version se result par farq padta hai.

---

### Q7

Ek consulting firm ka analyst apne client ko batata hai: "AI se humne yeh report banayi — humne
sabse powerful, sabse mehenga model use kiya, isliye aap ispar bharosa kar sakte hain." Client ka
CFO poochta hai: "Aapne verify kaise kiya ke yeh sahi hai?" Analyst ke paas seedha jawab nahi hai.
Yahan asal masla kya hai?

- A. Analyst ne galat model choose kiya.
- B. **✅ Analyst "model powerful hai" ko "output verified hai" samajh raha hai — yeh do alag
  cheezein hain. Model kitna bhi powerful ho, verification (fact-check, cross-check numbers, human
  review) ek alag, zaroori step hai jo skip nahi ho sakta.**
- C. Client ko itna technical sawal nahi poochna chahiye tha.
- D. Firm ko client ko batana chahiye tha kaunsa model use hua.

**Sahi jawab: B**

Simple wajah: Model ka mehenga/powerful hona iska matlab nahi hai ke uska jawab sahi hai. Har AI
kabhi na kabhi galti karta hai, chahe wo kitna bhi acha model ho. Isliye output ko hamesha check
karna padta hai — numbers verify karo, facts confirm karo, ya kisi insaan se review karwao. "Best
model use kiya" kehna kaafi nahi hai jawab dene ke liye. C aur D dono side-issues hain, asal masla
verification ka missing hona hai.

---

## Section B — Configuration & Knowledge Management (General Layer) (Q8–Q13)

### Q8

Ek HR team apne AI assistant ko company policy documents ke sath configure karti hai — 15 PDFs
upload karti hai: benefits, leave policy, code of conduct, etc. 3 mahine baad, leave policy badal
jaati hai (naya rule: 20 din se 25 din). HR team naya PDF upload kar deti hai lekin purana wala
delete nahi karti. Ab employee poochte hain "kitni leave milti hai" aur kabhi 20 din ka jawab aata
hai, kabhi 25 din ka. Root cause aur fix?

- A. AI khud confused hai — dobara training chahiye.
- B. **✅ Purana aur naya document dono ek sath maujood hain, AI dono ko valid samajh raha hai —
  fix: purana document delete/archive karo taake sirf current-valid information present rahe.**
- C. Employees ko galat sawal poochna band karna chahiye.
- D. Har jawab ke sath dono numbers (20 aur 25) dikhana chahiye taake employee khud chuno.

**Sahi jawab: B**

Simple wajah: Jab purani aur nayi dono files ek jagah rakhi jaati hain, AI ko pata nahi chalta
kaunsi sahi hai — dono ko sach maan leta hai. Isliye jab koi info update ho, purani wali file hata
do, sirf nayi rakho. Yeh training ka masla nahi hai (A galat) — yeh maintenance ka masla hai. D
confusion ko chhupata hai, fix nahi karta.

---

### Q9

Ek finance team ka AI assistant "system instructions" mein likha hai: "Hamesha professional tone
use karo. Hamesha accurate raho. Hamesha helpful raho. Kabhi galti mat karo." Team complain karti
hai ke instructions follow hone ke bawajood output mein abhi bhi errors aate hain. Kya masla hai in
instructions mein?

- A. Instructions bahut short hain, aur lambi honi chahiye.
- B. **✅ Instructions vague/generic hain ("accurate raho," "kabhi galti mat karo") — yeh koi
  specific, checkable action nahi batate. Behtar instruction woh hai jo specific steps de (jaise
  "har number ko source document se cross-check karo, agar match na ho toh flag karo").**
- C. AI instructions ko ignore kar raha hai jaan-boojh kar.
- D. Instructions ko dobara har message ke sath type karna chahiye.

**Sahi jawab: B**

Simple wajah: "Hamesha accurate raho" ek achi wish hai lekin AI ko exactly nahi batata KYA karna
hai. Achi instruction woh hoti hai jo ek concrete step de — jaise "numbers ko source se milao."
Vague instructions kaam nahi karti kyunke unmein koi action nahi hota, sirf ek general order hota
hai. A galat hai — lamba hona zaroori nahi, specific hona zaroori hai. C bhi galat — AI ignore
nahi kar raha, instruction hi useless thi.

---

### Q10

Ek marketing team apne AI ko Google Drive se connect karti hai taake woh latest brand guidelines
padh sake. 2 hafte baad, ek naya team member complain karta hai ke AI purani, deprecated brand
guideline (jo 6 mahine pehle Drive se delete ho chuki thi lekin AI "yaad" rakhta hai) follow kar
raha hai. Kya ho raha hai?

- A. AI ne file delete hone ke baad bhi content memorize kar liya hai permanently.
- B. **✅ Zyada mumkin hai ke connector properly refresh nahi hua, ya AI purani conversation ke
  context mein wahi purana content abhi bhi carry kar raha hai — fix: connector re-sync karo aur
  naya session start karo taake purana cached context clear ho.**
- C. Google Drive khud galat hai, koi doosra tool use karna chahiye.
- D. Team member ko khud manually latest guideline paste karni chahiye har baar.

**Sahi jawab: B**

Simple wajah: Agar ek purani conversation mein kabhi guideline padhi gayi thi, woh purani jaankari
usi conversation mein reh sakti hai, chahe original file delete ho chuki ho. Fix simple hai: naya
session start karo aur connector ko dobara refresh karo, taake sirf latest content mile. A galat
hai — yeh "permanent memory" nahi hai, yeh ek specific conversation ka context hai. C aur D dono
asal masla avoid karte hain.

---

### Q11

Ek legal team knowledge-source upload kar rahi hai: purani contract templates, kuch already
outdated regulations, aur current active policies — sab ek hi folder mein, koi labeling nahi. AI
se poocha jaata hai "current NDA template kya hai" aur woh kabhi outdated template return karta
hai. Sahi fix kya hai (sirf "check karo" kehna kaafi nahi hai)?

- A. Sab files delete kar ke sirf ek current file rakho, kabhi kuch aur upload mat karo.
- B. **✅ Knowledge sources ko organize/label karo (jaise folder ya naming convention se "CURRENT"
  vs "ARCHIVE" clearly mark karo), aur outdated/archived material ko active knowledge source se
  alag rakho.**
- C. Team ko har baar manually poochna chahiye "yeh current hai ya nahi."
- D. AI ko instruction do "sirf sabse naya document use karo" — file dates AI khud samajh lega.
  (Note: date-parsing/labeling reliably nahi hota bina explicit organization ke.)

**Sahi jawab: B**

Simple wajah: Agar purani aur nayi files mix hain bina kisi tareeqe ke, AI ko farq karna mushkil
hota hai. Sahi tareeqa: files ko clearly organize karo — jo active hai usay "current" label do, jo
purana hai usay "archive" mein alag rakho. A bahut extreme hai (kabhi update nahi kar sakte). D
risky hai — sirf "naya document use karo" kehna bharosemand nahi hai jab tak organization khud
clear na ho.

---

### Q12

Ek e-commerce team apne product-description-writer AI ko instructions deti hai: "500 words se kam
mat likho." Result: chhote, simple products (jaise ek pencil) ke liye bhi 500-word essays ban rahe
hain jo customers padhte hi nahi. Kya galat hai?

- A. AI ki writing quality kharab hai.
- B. **✅ Instruction ek rigid, one-size-fits-all rule hai jo product ki complexity ignore karti
  hai — behtar instruction product-type ke hisaab se range de (jaise "simple products: 50-100
  words; complex/technical products: 300-500 words").**
- C. Customers ko lambi descriptions padhni chahiye, unki problem hai.
- D. 500 words ka rule hata do, koi limit mat do.

**Sahi jawab: B**

Simple wajah: Ek hi fixed number (500 words) sab products ke liye sahi nahi ho sakta — chhota
product ko chhoti description chahiye, bara/complex product ko lambi. Instruction ko flexible
banao: product ke type ke hisaab se range do. A galat hai — AI ne exactly wahi kiya jo bola gaya
tha, quality ka masla nahi. D bhi extreme hai — koi limit na hona bhi problem create kar sakta hai.

---

### Q13

Ek team apne AI ke "knowledge base" mein customer complaints ka raw data daal deti hai — including
kuch complaints jinmein customers ke phone numbers aur home addresses hain. Woh AI ab customer-
facing chat mein use ho raha hai. Sabse zaroori pehla fix kya hai?

- A. Complaints ka data delete kar do, kabhi use mat karo.
- B. **✅ Knowledge base se personal/sensitive information (phone numbers, addresses) remove ya
  redact karo pehle, uske baad hi customer-facing use continue karo — data-sensitivity ek
  governance obligation hai, na ke baad mein sochne wali cheez.**
- C. AI ko instruction do "personal info kabhi mat bolo" — data mein rehne dena theek hai.
- D. Sirf internal team ko is data tak access do, customer-facing use waisi hi rakho.

**Sahi jawab: B**

Simple wajah: Agar sensitive data (phone number, address) knowledge base mein hai, woh kabhi na
kabhi accidentally customer ko chala jaa sakta hai. Sirf "mat bolo" kehna kaafi nahi (C galat) —
data ko waha se hi hata do ya chhupao (redact karo), phir hi use karo. Yeh ek safety/privacy step
hai jo pehle hona chahiye, baad mein nahi.

---

## Section C — Governance in a Regulated-Client Context (Q14–Q20)

### Q14

Ek FDE consultant ek healthcare client ke sath kaam kar rahi hai jo HIPAA-regulated hai (patient
data protection law). Client ka team AI assistant ko patient records ke sath directly connect
karna chahta hai taake "faster summaries" mil sakein. Consultant ko pata hai ke unka current AI
vendor HIPAA-compliant Business Associate Agreement (BAA) nahi offer karta. Client keh raha hai
"koi masla nahi, hum careful rahenge." Consultant kya kare?

- A. Client ki request maan lo — woh client hai, unka decision final hai.
- B. **✅ Regulatory requirement (BAA/HIPAA compliance) ek hard constraint hai, "careful rahenge"
  ise replace nahi kar sakta — consultant ko clearly batana chahiye ke yeh setup regulatory risk
  create karta hai, aur ek compliant alternative (BAA-covered vendor, ya de-identified data) propose
  karna chahiye.**
- C. Kaam start kar do, agar masla ho toh baad mein fix kar lenge.
- D. Poora project cancel kar do, kyunki koi bhi AI use risky hai.

**Sahi jawab: B**

Simple wajah: Kuch rules (jaise patient data ka HIPAA law) sirf "careful rehne" se nahi maante —
yeh legal requirement hai. Agar vendor iske liye proper agreement nahi deta, yeh use karna galat
hai chahe client raazi ho. Sahi kaam: client ko clearly batao ke yeh risk hai, aur ek safe rasta
(jaise data se naam/details hata kar use karna) suggest karo. A galat hai kyunki client ki marzi
kanoon nahi badalti. D bahut extreme hai — safe tareeqa maujood hai, poora cancel karna zaroori
nahi.

---

### Q15

Ek bank ka compliance team AI se loan-application summaries likhwata hai jo phir loan-officer
padhta hai decision lene ke liye. AI summary mein ek applicant ke baare mein likha hai: "Yeh
applicant thoda risky lagta hai." Compliance officer, Farhan, yeh line dekh kar ruk jaata hai. Kya
masla hai, aur kyun?

- A. Koi masla nahi — yeh sirf ek observation hai, useful hai.
- B. **✅ Vague, unexplained judgment ("risky lagta hai") bina specific, factual reasoning ke —
  regulated lending decisions mein har judgment ko traceable, factual reasoning se backed hona
  chahiye (jaise "debt-to-income ratio 55%, jo threshold 40% se zyada hai"), warna yeh bias ya
  discrimination claim ka risk create karta hai.**
- C. AI ko loan applications par kabhi comment nahi karna chahiye.
- D. Farhan ko is line ko ignore kar dena chahiye, AI usually sahi hota hai.

**Sahi jawab: B**

Simple wajah: Lending (loan dena) jaise regulated kaam mein, har decision ka reason clear aur
factual hona chahiye — sirf "risky lagta hai" kehna kaafi nahi, yeh bias jaisa lag sakta hai.
Behtar hai ke exact number/fact diya jaye (jaise income vs debt ratio). Isliye Farhan ka rukna sahi
hai — yeh flag karna zaroori tha. C zyada extreme hai — AI comment kar sakta hai, bas factual hona
chahiye.

---

### Q16

Ek EU-based company apne customer data ko AI tool mein process karti hai. Unka legal team batata
hai ke GDPR (EU privacy law) ke tehat, customers ko yeh haq hai ke unka data "bhula diya jaye"
(right to erasure) agar woh maange. Team poochti hai: "Agar customer ka data hamare AI ki purani
conversation mein already use ho chuka hai, kya hum sirf database se delete kar dein, kaafi hai?"

- A. Haan, sirf original database record delete karna kaafi hai.
- B. **✅ Nahi — team ko yeh bhi check karna chahiye ke customer ka data kahan-kahan persist ho raha
  hai (knowledge base, cached conversations, logs), aur un sab jagah se bhi remove/anonymize karna
  hoga — "erasure" ka matlab sirf ek jagah delete karna nahi hai.**
- C. AI tools GDPR se exempt hain, koi action zaroori nahi.
- D. Sirf customer ko email kar do ke "aapka data delete ho gaya," actual delete zaroori nahi.

**Sahi jawab: B**

Simple wajah: Jab koi customer kehta hai "mera data hata do," matlab hai data HAR JAGAH se hatna
chahiye — sirf ek database nahi, balke saari jagah jahan woh save hua ho (logs, cache, knowledge
files). Sirf ek jagah delete karna adhoora kaam hai. C aur D dono galat hain — yeh legal obligation
hai, ignore ya jhoot nahi bol sakte.

---

### Q17

Ek pharmaceutical company ka marketing team AI se ek naye medicine ke baare mein customer-facing
content likhwata hai. AI output mein medicine ke benefits detail mein hain lekin side-effects sirf
ek line mein "kuch side effects ho sakte hain" — bina specifics ke. Regulatory reviewer, Dr. Adeel,
ise reject karta hai. Kyun?

- A. Content bahut lamba hai.
- B. **✅ Pharma/medical marketing mein regulatory requirement hoti hai ke risks/side-effects utni
  hi detail se batayi jayein jitni benefits — asymmetric detail (benefits detailed, risks vague)
  misleading marketing ka classic pattern hai aur regulation violate karta hai.**
- C. AI ko medicine ke baare mein likhna hi nahi chahiye tha.
- D. Marketing team ko khud likhna chahiye tha, AI use nahi karna chahiye tha.

**Sahi jawab: B**

Simple wajah: Jab benefits detail mein likhe jayein lekin risks sirf ek choti si line mein chhupa
diye jayein, yeh unfair/misleading lagta hai — aur medicine jaisi cheez mein yeh kanooni tor par
bhi galat hai. Dono taraf (fayda aur nuksan) barabar detail se batana chahiye. C aur D extreme hain
— AI use ho sakta hai, bas output ko is rule ke against check karna zaroori hai.

---

### Q18

Ek government-contractor company apne internal AI assistant mein "classified" ya "controlled
unclassified information" (CUI) documents upload karne se pehle poochti hai: kya unka current AI
vendor is tarah ka data handle karne ke liye appropriate hai? Ek employee kehta hai: "Bas upload
kar do, dekh lete hain kya hota hai." Sahi approach kya hai?

- A. Employee sahi hai — try karne mein koi harj nahi, baad mein delete kar sakte hain.
- B. **✅ Pehle vendor ki data-handling certification/compliance verify karo (jaise FedRAMP ya
  equivalent), aur agar vendor appropriate certification nahi rakhta, controlled/classified data
  upload hi mat karo — "try kar ke dekhte hain" regulated data ke sath acceptable approach nahi
  hai.**
- C. Sab data ko pehle encrypt kar ke upload karo, phir koi masla nahi.
- D. Sirf senior management ki verbal permission lo, phir upload kar do.

**Sahi jawab: B**

Simple wajah: Kuch data itna sensitive hota hai (jaise government-controlled information) ke usay
kisi bhi tool mein daalne se pehle check karna zaroori hai ke woh tool is kaam ke liye officially
approved hai ya nahi. "Try kar ke dekhte hain" is tarah ka data ke sath khatarnak hai — ek baar
data chala jaye toh wapas nahi aata. A aur D dono is zaroori check ko skip karte hain.

---

### Q19

Ek recruiting firm AI use karti hai resumes screen karne ke liye. 3 mahine baad, ek internal audit
dikhata hai ke AI unconsciously ek particular university se aane wale candidates ko consistently
higher score de raha hai — jo ek protected-characteristic-correlated pattern ban sakta hai (agar
woh university demographically skewed hai). HR head, Nadia, kya kare?

- A. Kuch nahi — AI ne khud yeh pattern nahi seekha hoga, coincidence hai.
- B. **✅ Isay bias/disparate-impact risk ki tarah treat karo — screening process ko pause karo,
  root cause investigate karo (training data, prompt, ya scoring criteria mein bias), aur jab tak
  fix na ho tab tak human review mandatory karo.**
- C. Us university ke candidates ko manually reject karna shuru kar do taake balance ho jaye.
- D. AI ko sirf naam hata kar resumes do, baaki sab same rakho.

**Sahi jawab: B**

Simple wajah: Agar AI baar-baar ek particular group ko zyada number de raha hai bina kisi achi
wajah ke, yeh ek governance red-flag hai — chahe AI ne "jaan-boojh kar" na kiya ho, result mein
bias hai. Sahi kaam: turant rokna, wajah dhoondhna, aur jab tak fix na ho insaan se check karwana.
A ise ignore karta hai jo risky hai. C khud ek naya discrimination create karta hai.

---

### Q20

Ek client, jo ek regulated financial-services firm hai, apne FDE consultant se poochta hai: "AI se
hum apni saari client-facing investment advice generate karwa sakte hain na, bina kisi human
advisor ke?" Consultant ko pata hai ke unki industry mein "investment advice" dene ke liye licensed
human advisor legally required hota hai. Consultant kya kahe?

- A. "Haan, AI kaafi capable hai, seedha use kar sakte hain."
- B. **✅ "Nahi — is regulation ke tehat licensed human advisor ka involvement legally required hai;
  AI draft/research assist kar sakta hai, lekin final advice ek licensed human se hi aani chahiye
  aur unki sign-off honi chahiye."**
- C. "AI use kar lo, lekin chhupa kar rakho ke AI use ho raha hai."
- D. "Yeh mera decision nahi hai, aap jo chahein karein."

**Sahi jawab: B**

Simple wajah: Kuch professions mein (jaise investment advice dena) kanoon kehta hai ke sirf licensed
insaan hi final advice de sakta hai. AI madad kar sakta hai — research, draft banana — lekin
aakhri faisla aur sign licensed human ka hona chahiye. Consultant ka kaam hai yeh clearly batana,
chhupana nahi (C galat) aur chup reh kar side lena bhi nahi (D galat) — yeh client ko regulatory
risk mein daal sakta hai agar na bataya jaye.

---

## Section D — "Tell the Client What It Won't Do First" (Q21–Q24)

### Q21

Ek FDE, Kamran, ek naye client ke sath kickoff meeting mein hai. Client excited hai aur poochta hai
"AI hamare liye kya kya kar sakta hai?" Kamran ek lambi list deta hai jo AI kar sakta hai. Meeting
ke end mein client poochta hai "aur yeh cheez?" — ek cheez jo AI nahi kar sakta (jaise real-time
stock trading execution). Kamran ko pehli baar yeh batana pada ke AI woh nahi karega. Client
disappointed lagta hai. Kamran ne kya missed kiya?

- A. Kuch nahi — client ne khud poocha, Kamran ne sahi jawab diya.
- B. **✅ Kamran ko meeting ki shuruaat mein hi, client ke poochne se pehle, clearly batana chahiye
  tha ke AI kya NAHI karega — is se client apni expectations pehle se set kar leta, disappointment
  nahi hoti.**
- C. Client ko khud research karni chahiye thi AI ki limitations ke baare mein.
- D. Kamran ko AI ki limitations chhupani chahiye thi taake client excited rahe.

**Sahi jawab: B**

Simple wajah: Sirf yeh batana ke AI kya kar sakta hai kaafi nahi hai — jo cheezein AI NAHI karega,
woh bhi pehle hi bata deni chahiye, bina client ke poochne ka intezaar kiye. Is se client surprise
nahi hota aur trust banta hai. A theek lagta hai lekin best practice miss karta hai — proactively
batana chahiye tha. D bahut galat hai — chhupana trust todta hai.

---

### Q22

Ek AI consulting firm apne proposal document mein likhti hai: "Hamara AI solution aapke customer
support ko 100% automate kar dega, koi human agent ki zaroorat nahi hogi." Ek senior FDE, Rida, yeh
draft dekh kar ise reject karti hai. Kyun?

- A. 100% automation technically possible nahi hai, isliye jhoota claim hai.
- B. **✅ Dono wajah sahi hain: (1) yeh claim likely technically overstated hai — edge cases,
  escalations, complex complaints hamesha kuch human involvement maangte hain, aur (2) is tarah ka
  absolute claim client ko galat expectation deta hai jo baad mein trust todega jab reality alag
  nikle.**
- C. Client ko yeh sunna pasand nahi aayega.
- D. Firm ko pehle isay test karna chahiye tha, phir claim karna chahiye tha.

**Sahi jawab: B**

Simple wajah: "100%" jaisa absolute word khatarnak hota hai — asal duniya mein hamesha kuch aisi
situations aati hain jo insaan ko handle karni padti hain (jaise bahut ajeeb ya sensitive
complaint). Aisa bolna client ko galat ummeed deta hai. Behtar hai honest, realistic claim karna —
jaise "80-90% routine queries automate honge, complex cases human ke paas jayenge." D bhi ek sahi
point hai lekin B poori wajah cover karta hai.

---

### Q23

Ek client apne FDE se poochta hai: "Kya AI hamari 10-saal purani legacy database ko directly samajh
sakta hai, bina kisi conversion ke?" FDE ko pata hai ke technically AI ko yeh data samjhaane ke
liye pehle ek "translation layer" (data ko readable format mein convert karna) banana padega — yeh
seedha nahi ho sakta. FDE kya kare?

- A. "Haan bilkul, AI kuch bhi samajh sakta hai" bol kar client ko khush rakho.
- B. **✅ Clearly batao ke direct nahi ho sakta — pehle ek translation/integration layer banana
  hoga, iska time aur cost bhi bata do, taake client informed decision le sake.**
- C. Project start kar do bina batayen, kaam karte karte pata chal jayega.
- D. Client ko bol do ke yeh unka masla hai, hum sirf AI provide karte hain.

**Sahi jawab: B**

Simple wajah: Agar koi cheez seedha kaam nahi karti (jaise purani database ko samajhna), yeh pehle
hi client ko batana chahiye — kitna time lagega, kitna paisa lagega, sab clear karo. Is se client
surprise nahi hota project ke beech mein. A jhoot hai. C aur D dono client ko andhere mein rakhte
hain jo trust todta hai.

---

### Q24

Ek FDE consultant apna final report client ko deti hai. Report mein likha hai: "AI ne yeh 500
customer complaints analyze ki aur pattern dhoonda." Client poochta hai: "Kya AI ne har complaint
individually verify ki, ya sirf overall pattern nikala?" Consultant realize karti hai ke usne khud
bhi yeh clearly nahi socha tha. Sahi jawab kaise dena chahiye, aur is situation se kya seekha ja
sakta hai?

- A. "Haan sab verify ho gaya" bol do, client ko satisfy karne ke liye.
- B. **✅ Honestly batao ke exactly kya hua tha (jaise: "AI ne saari 500 complaints padhi aur pattern
  nikala, lekin individual complaint ki 100% accuracy verify nahi ki gayi — agar aapko har complaint
  ki confirmation chahiye, woh ek alag, additional step hoga"). Seekh: hamesha pehle se clear karo ke
  AI ka output kis level ka confidence/verification carry karta hai, report likhne se pehle hi.**
- C. Client ko itna deep sawal nahi poochna chahiye tha.
- D. Consultant ko sawal ka jawab dene se mana kar dena chahiye, confidential hai.

**Sahi jawab: B**

Simple wajah: Jab client poochta hai "kitna verify hua," consultant ko sach batana chahiye — kya
sirf overall pattern dekha gaya, ya har cheez individually check hui. Jhoot bolna (A) risky hai —
baad mein pakda ja sakta hai. Sabse achi aadat: report likhne se pehle hi khud clear karo ke kitna
verification hua hai, taake aisa sawal aane par turant, honest jawab de sako.

---

## Answer Key (Quick Grid)

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | B | 7 | B | 13 | B | 19 | B |
| 2 | B | 8 | B | 14 | B | 20 | B |
| 3 | B | 9 | B | 15 | B | 21 | B |
| 4 | C | 10 | B | 16 | B | 22 | B |
| 5 | C | 11 | B | 17 | B | 23 | B |
| 6 | B | 12 | B | 18 | B | 24 | B |

**Scoring (self-check, extreme set):** 20/24+ = ready for the "beyond CCAO-F" layer. 15-19/24 =
re-read `README.md`'s "Same Blueprint, One Level Up" section, retry. Under 15 = do
`../ccao-f/quiz100.md` + `hardquiz.md` first (shared core), yeh set baad mein.

---
[⬅ PCAO-F Index](README.md) · [Shared-core hard quiz (CCAO-F)](../ccao-f/hardquiz.md)
