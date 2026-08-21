# 11 — Practice Log (Meri Apni Hands-On Progress)

*Yeh file [07-practice-projects.md](07-practice-projects.md) se alag hai. Woh file bata ti hai
**"kaise karna hai"** (mechanical steps, full detail). Yeh file record karti hai **"maine khud kya
kiya"** — apna practice run, ek project ke baad ek, checkbox ke sath. Isi pattern par jo
[Loop Engineering ki practice log](../loop-engineering/11-practice-log.md) mein use hua.*

**Rule:** ek project ka checkbox tab hi tick hota hai jab uska **"Done jab"** criteria khud dekh liya
ho — sirf steps parh lena kaafi nahi.

**2 rules jo har project mein chalti hain (07 se):** throwaway git repo use karo (jaan-boojh kar
guardrails trip karoge), aur har project mein jaan-boojh kar ek failure khud banao — harness sirf us
ghalti se proof hoti hai jo woh pakre.

---

## Progress Checklist (8 Projects + Appendix Drills)

| # | Project | Status | Practice Notes |
| --- | --- | --- | --- |
| 1 | 🧱 The First Wall | ⬜ Not started | |
| 2 | 🪝 The Lint Hook | ⬜ Not started | |
| 3 | 🗣️ The Error Audit | ⬜ Not started | |
| 4 | ✂️ The Tool Diet | ⬜ Not started | |
| 5 | 📋 The Typed Reviewer | ⬜ Not started | |
| 6 | 🔩 The Ratchet Week | ⬜ Not started | |
| 7 | 🔒 The Fenced Night | ⬜ Not started | |
| 8 | 🔁 The Model Swap (Capstone) | ⬜ Not started | |
| A | Appendix — 3 Hook Pipeline Drills | ⬜ Not started | |

Status legend: ⬜ Not started · 🔶 In progress · ✅ Done (self-check pass ho gaya)

---

## Project 1 — The First Wall *(abhi shuru karo)*

**Concept:** 4 (permission rules) · **Time:** 20-30 min · **Difficulty:** Easy

> 🧩 **Sabse aasan zaban mein:** jaise ghar ke gate par ek chowkidar khara ho jo ek fixed list dekh kar
> kehta hai "yeh log andar nahi aa sakte" — chahe darwaza khula ho, chowkidar phir bhi rok deta hai.
> Yahan "chowkidar" deny-list rules hain (secrets, recursive delete, force-push), aur "darwaza khula
> hona" iska matlab hai ke agent chahe to command likh sakta hai — lekin tool layer usay execute nahi
> hone deti.

**Kya karna hai:** Throwaway repo mein deny list likho (secrets files, recursive deletes, force-push),
phir har rule khud trip karo — agent se secret parhwao, force push karwao.

### Done jab (self-check)
- [ ] Har deny rule ek deliberate attempt ko block kar chuki
- [ ] Pata hai kis layer ne enforce kiya (tool layer, sandbox nahi)

**Runnable scaffold:** [`projects/first-wall/README.md`](projects/first-wall/README.md)

---

## Project 2 — The Lint Hook *(agla)*

**Concept:** 8 (hooks) · **Time:** 30-45 min · **Difficulty:** Easy-Medium

> 🧩 **Sabse aasan zaban mein:** jaise ek teacher copy check kar ke wapas kar deta hai "yeh galti thik
> karo" (feedback — copy wapas nahi le li) — lekin exam mein jab tak sawal sahi na ho, agla sawal khulta
> hi nahi (gate — kaam "done" hi count nahi hota). Dono alag cheezein hain: feedback sirf batata hai,
> gate rokta hai.

**Kya karna hai:** Post-edit hook lagao jo linter chalaye aur failures agent ko wapas de. Phir ek
`Stop`/`pre-commit` gate lagao jo lint fail hone tak khatam hi na hone de.

### Done jab (self-check)
- [ ] Dono behaviors dekhe (feedback vs gate)
- [ ] Ek line mein farq bata sako

**Runnable scaffold:** [`projects/lint-hook/README.md`](projects/lint-hook/README.md)

---

## Project 3 — The Error Audit *(agla)*

**Concept:** 7 (AX) · **Time:** 45-60 min · **Difficulty:** Medium

> 🧩 **Sabse aasan zaban mein:** jaise ek foreign traveler ko rasta batate waqt sirf "galat rasta hai"
> kehna kaafi nahi — usay yeh batana hoga "seedha jao, phir left lo." Error message bhi waisi hi honi
> chahiye: sirf "fail hua" nahi, balke "yeh badlo" — taake agla attempt khud theek ho jaye, kisi insaan
> ki madad ke bina.

**Kya karna hai:** Ek connector chuno jo loops use karti hain. Uski 3 sab se common errors jaan-boojh
kar trigger karo, har message rewrite karo taake agla step bataye.

### Done jab (self-check)
- [ ] Fail hui call agent ki agli koshish pe khud heal hui
- [ ] Us beat ki taraf ishara kar sako jo pehle waste hoti thi

**Runnable scaffold:** [`projects/error-audit/README.md`](projects/error-audit/README.md)

---

## Project 4 — The Tool Diet *(agla)*

**Concept:** 6, 7 · **Time:** 1-2 hrs, phir ek hafta beats · **Difficulty:** Medium

> 🧩 **Sabse aasan zaban mein:** jaise ek mistri ko poora tool-box dene ki bajaye sirf woh 3 auzaar do jo
> is kaam ke liye chahiye — kam options, kam confusion, kam galat auzaar uthane ka chance.

**Kya karna hai:** Triage loop ke sab tools list karo, list ko sirf zaroori tak kaato, ek hafta chhoti
list pe beats chalao.

### Done jab (self-check)
- [ ] Wrong-tool incidents ka before/after compare kiya
- [ ] After count chhota hua (ya confirm kiya list pehle se hi lean thi)

**Runnable scaffold:** [`projects/tool-diet/README.md`](projects/tool-diet/README.md)

---

## Project 5 — The Typed Reviewer *(agla)*

**Concept:** 9 (typed output) · **Time:** 1-1.5 hrs · **Difficulty:** Medium-Hard

> 🧩 **Sabse aasan zaban mein:** jaise ek examiner sirf "pass/fail" nahi likhta, balke ek form bharta hai
> jismein har field check hoti hai — agar ek field ajeeb/adhoori ho, poora form reject hota hai, guess
> nahi kiya jata.

**Kya karna hai:** PASS/FAIL reviewer ko JSON verdict pe upgrade karo, field-by-field `jq` validation
add karo, protocol breaks ko "needs a human" mein route karo.

### Done jab (self-check)
- [ ] Lambi/unclear review escalation path mein gayi, guess nahi hui
- [ ] Hand-crafted `{"verdict": "MAYBE"}` reject hua

**Runnable scaffold:** [`projects/typed-reviewer/README.md`](projects/typed-reviewer/README.md)

---

## Project 6 — The Ratchet Week *(agla)*

**Concept:** 10 (failure classes, ratchet) · **Time:** 1 hafta, ~15 min/din · **Difficulty:** Medium

> 🧩 **Sabse aasan zaban mein:** jaise ek doctor har bimari ko category mein daal kar file mein likhta
> hai — agli baar wahi bimari dobara aaye to fauran pehchani jati hai aur usi fix se theek hoti hai.
> Yahan "category" 4 failure classes hain, "file" `HARNESS.md` hai.

**Kya karna hai:** 7 din, har agent mistake ko 4 failure classes mein classify karo, har fix
`HARNESS.md` mein log karo.

### Done jab (self-check)
- [ ] Per-class count mil gaya, pata hai harness kahan patli thi
- [ ] Same-shape 2 failures pehli ke baad namumkin ho gayin

**Runnable scaffold:** [`projects/ratchet-week/README.md`](projects/ratchet-week/README.md)

---

## Project 7 — The Fenced Night *(agla)*

**Concept:** 5, 11 · **Time:** 1-2 hrs, phir ek overnight run · **Difficulty:** Medium-Hard

> 🧩 **Sabse aasan zaban mein:** jaise raat ko ghar ke sab darwaze-khirkiyan band kar ke sone jao, aur
> subah check karo kya kisi ne khulne ki koshish ki thi — aur agar ki, kya alarm baja (loud) ya chup
> chaap ruk gaya (invisible block bhi fail hai, chahe usne roka ho).

**Kya karna hai:** Morning-triage loop ko poori tarah fence karo (worktree, no network/chhoti allowlist,
gated branches). Attack karo: malicious-injection issue queue mein daal ke raat guzarne do.

### Done jab (self-check)
- [ ] Subah ka log dikhaya har injected action block hui
- [ ] Blocks loud thin, chup nahi

**Runnable scaffold:** [`projects/fenced-night/README.md`](projects/fenced-night/README.md)

---

## Project 8 — The Model Swap (Capstone) *(agla)*

**Concept:** 12 (coupling), sab 5 verbs · **Time:** 2-3 hrs, phir teen raatein · **Difficulty:**
Capstone

> 🧩 **Sabse aasan zaban mein:** jaise ek recipe sirf ek hi chef ke haath se na banti ho, balke likhi hui
> ho taake koi bhi chef follow kar sake — agar recipe "iss chef ki aadat" pe depend karti hai (behavior-
> coupling), naya chef aate hi tootegi. Recipe ko measurements/steps (contract-coupling) mein likhna
> hi asli test hai.

**Kya karna hai:** Hardened loop ko teen raaton tak alag model pe chalao. Jo tootay/shift ho log karo,
behavior-coupling se contract-coupling (exit codes, schemas, tests) mein move kar ke fix karo.

### Done jab (self-check)
- [ ] Har failure contract-coupling mein move kar ke fix hua
- [ ] Loop dono models pe clean chali — proof ke harness aapki hai, kisi ek model ki nahi

**Runnable scaffold:** [`projects/model-swap/README.md`](projects/model-swap/README.md)

---

## Appendix — 3 Hook Pipeline Drills *(baad mein)*

> 🧩 **Sabse aasan zaban mein:** jaise ek CCTV camera lagao (drill 1 — dekho kitna record hota hai),
> phir ek gate lagao jo sirf ek cheez rokta ho aur wajah bataye (drill 2), phir ek alarm jo sirf
> zaroori waqt hi baje, har waqt nahi (drill 3 — warna log ignore karna shuru kar dete hain).

- **Drill 1 — See the stream:** hook/plugin lagao jo har tool call `trace.log` mein likhe. Ek normal
  beat chalao, log parho.
- **Drill 2 — Block on purpose:** `PreToolUse` check likho jo `curl` wali koi bhi Bash command block
  kare, error mein allowed alternative bataye.
- **Drill 3 — The conditional gate:** test-suite `Stop` hook sirf tab chale jab source files badli hon
  (`git diff --name-only` check).

### Done jab (self-check)
- [ ] Drill 1: ek beat ke sab tool calls log mein dikhein
- [ ] Drill 2: `curl` command block hui, error ne alternative bataya
- [ ] Drill 3: gate sirf source-change beats par chali, har beat par nahi

**Runnable scaffold (tested, 3 hooks confirmed working):** [`projects/hook-pipeline-drills/README.md`](projects/hook-pipeline-drills/README.md)

---
[⬅ Sources & Further Reading](09-sources-further-reading.md) · [⬆ Index](README.md)
