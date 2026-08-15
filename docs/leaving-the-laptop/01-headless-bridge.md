# 01 — Headless: Har Ghar Ka Pul

## Concept 3: Har Ghar Headless Boli Bolta Hai

Ye khamosh fact hai jo is poore course ki har move mumkin banati hai: **aap already ye pul paar kar chuke
ho**, evals course mein, bina batae ke ye pul tha. Eval runner ne `claude -p` aur `opencode run` call
kiya — agent ek **command** ki tarah, conversation nahi. Koi open window nahi, koi session babysit nahi:
prompt jata hai, kaam hota hai, output ata hai, process khatam.

**Yehi headless mode hai**, aur is poore course ka bunyad yehi hai: **jo bhi command chala sakta hai, wo
ab aapka agent chala sakta hai.** Shell script chala sakti hai. Cron job chala sakta hai. CI runner chala
sakta hai. Cloud scheduler chala sakta hai. Ghar 2 se aage, har ghar bunyadi tor pe sirf iska alag jawab
hai: **kis ka computer headless command chalata hai, aur kis ke clock pe.**

**Nayi aadat, kyunke ab koi insaan nahi dekh raha:** **headless runs loudly fail hone chahiyen.** Session
mein, aap error dekhte ho. Runner pe, koi check na kiya gaya exit code ek aisi beat hai jo chup chaap
nahi hui — Concept 1 ki wahi warning, cloud mein rebuilt. Is course ki har headless wrapper exit code
check karti hai aur failure pe **loud** hoti hai (loop course ka 5th verb). **Chup ka matlab success hona
chahiye — ye aap enforce karte ho, koi inherit ki hui default nahi.**

> **Simple:** Interactive mode aap agent se baat kar rahe ho. Headless mode koi bhi (script, schedule,
> server) agent ko ek note thama kar result collect kar raha hai. Ek dafa agent notes le sakta hai, wo
> kahin bhi kaam kar sakta hai jahan notes deliver ho sakein.

## Concept 4: Ghar 2, Cloud Schedule — Pehle Clock Bahar Jata Hai

Pehli move jaan-boojh kar sab se chhoti hai: jo banaya wo sab rakho, **sirf clock relocate karo**. Config
(rules file, skills, subagents, hooks) bilkul wahi rehti hai. Jo badalta hai: **beat kaun shuru karta
hai**.

### Claude Code — Routine

`/schedule` command (alias `/routines`) conversation se ek Routine banata hai. Ye Anthropic-managed cloud
pe chalta hai chahe aapka laptop khula ho ya nahi.

**3 honesty notes:**
- **Routines research preview hain** — live docs se verify karo
- **Scheduled run ghante ke kuch minute baad shuru ho sakta hai** (docs isay "stagger" kehte hain).
  *"Around 9am"* asal promise hai
- **Green run status sirf itna kehta hai ke session infrastructure error ke bagair khatam hua** — ye
  matlab **nahi** ke aapka task succeed hua. Loud-failure rule aapko khud enforce karni hai.

> **Trap:** Desktop app mein **Local** choose karna Desktop scheduled task banata hai jo **aapki machine**
> pe chalti hai — ye ghar 1 hai timer ke sath, move bilkul nahi.

**Repo-attached loops ke liye, vendor-neutral version:** **GitHub Actions** `schedule:` trigger pe
`claude -p` headlessly chalati hai, CI runner pe, repo config checked out. **Honesty note:** scheduled
workflows best-effort hain — load mein late start ho sakti hain, occasionally drop bhi ho sakti hain.

### OpenCode — Scheduler Aap Chunte Ho

OpenCode ke paas first-party hosted control plane nahi hai. Ghar 2 hai ek scheduler **jo aap chunte ho**
— repo-attached loops ke liye GitHub Actions pattern, baaki sab ke liye koi bhi machine jo cron chala
sake.

> **Farq lesson hai, defect nahi:** Open tool aapko poori runtime decision deta hai, kuch bhi chupaya
> nahi. **Aap ab khud vendor ho** — runner ki uptime, credentials, updates aapki responsibility hain.

## Success Ki Definition

**Kam se kam ek poora operating cycle aur kam se kam 10 successful beats, laptop band, chup ka matlab
baseline.** *"Ek dafa cloud se chala"* nahi — evals course sikha chuki hai ek green run ki keemat kya hai.

## Minimum Unattended Kit

Ye course DevOps engineer nahi banati — **6 controls, jab koi insaan run na dekhe to koi bhi optional
nahi:**

| Control | Rule | Rukti Hui Failure |
| --- | --- | --- |
| **Idempotency** | Retried beat repeat hona safe ho | Invoice do dafa bhej dena |
| **Missed-run detection** | Ek doosra system notice kare jab pehla kabhi shuru hi na hua ho | Process jo kabhi nahi chali apni gair-mojoodgi report nahi kar sakti |
| **Concurrency lock** | Ek waqt ek beat, agar 8am wali abhi zinda hai to 9am wali wait kare | 2 agents ek hi files edit kar rahe hon |
| **Credential discipline** | Scoped service credentials, least privilege, rotated, kabhi personal login nahi | Cloud runner aapki poori identity hold kare |
| **Time semantics** | Timezone likhi hui, daylight-saving decided pehle se | 6pm invoice jo saal mein 2 dafa 1 ghanta khisak jaye |
| **Cost + execution limits** | Max duration, turns, retries, spend per beat | Bhatakti hui run jo raat mein poora budget kha jaye |

> Ye kit ghar 2 ki **entrance fee** hai, aur aage bhi travel karti hai — har agla ghar bhi yehi 6 mangta
> hai, kabhi aapki script ki tarah, kabhi service settings ki tarah.

> **Ehtiyat — trap jo chupi hui hai:** Aapke laptop pe, human gate ki ek convenient property thi: **aap
> wahin thay.** Ghar 2 mein, loop chalta hai chahe aap screen ke qareeb ho ya nahi — escalations bina
> dekhe jama ho sakti hain. **Isliye ghar 2 ki move ek upgrade force karti hai jo laptop kabhi nahi
> mangta tha: escalation channel aapke desk tak nahi, AAP tak pohanchna chahiye** (message, mention,
> issue jispe aapka naam ho).

### Self-Check
**Sawal:** Aapki pehli cloud-scheduled beat green chalti hai. Teammate kehta hai migration ho gaya. 2
cheezein abhi missing hain "done" honest kehne se pehle?
**Jawab:** Pehla: ek green beat ek run ke baare mein fact hai, ghar ke baare mein nahi. Migration **rate**
se prove hota hai — poora operating cycle + kam se kam 10 beats baseline ke against, ek raat nahi. Doosra:
loud failure test nahi hui. Jab tak aap jaan-boojh kar ek failure plant na karo aur alarm aap tak na
pohanche, chup ambiguous hai.

---
[⬅ Overview](00-overview.md) · [Agla: Managed Runtime ➡](02-managed-runtime.md)
