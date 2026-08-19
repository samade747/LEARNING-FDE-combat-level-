# Building the Context Layer — Summary

15 Concepts. Pichle course (Digital FTE) mein ek Worker ko apna store diya gaya tha; yeh course **poore
workforce ka corpus** banata hai — ek company ke saare scattered sources (SharePoint, email, chat, live
systems) ko governance ke sath serve karna. Har cheez jo layer return kare, 3 sawalon ka jawab de: **Yeh
kahan se aya? Kya yeh banda dekh sakta hai? Kya yeh abhi bhi lagu hota hai?**

## 00 — Foundations (Concepts 1-4)

- **Concept 1 — Scope Jump:** pichla store 4 properties rakhta tha jo notice nahi hoti thin: sab kuch
  aap ne likha, ek hi reader, ek kism ki truth, construction-se-current. Company connect karte hi sab
  gayab: content kisi aur ka (kuch superseded), alag readers ko alag jawab milna chahiye, alag weight ke
  documents, aur staleness silent hoti hai. **"Pichla course retrieval problem tha. Yeh governance
  problem hai jo retrieval problem ke kapre pehne hai."**
- **Concept 2 — 4 Source Classes:** (1) Agent Factory System of Record — shared method, web-indexed,
  cite-able; (2) Vertical Systems of Record — customer ke sales/accounting rules, indexed+MCP-confirmed;
  (3) Customer operational records — ERP/CRM/ledger, live typed query, kabhi index nahi; (4) Customer
  working context — email/chat/files, permission-aware indexing, **sirf evidence, kabhi rule nahi**.
  Pehli 3 authoritative hain; sirf chauthi mein professional authority nahi — aur yehi woh class hai jahan
  log sabse pehle point karte hain (isliye "fluent lekin baseless" jawab aam hain).
- **Concept 3 — Onyx Kya Hai:** open-source AI chat jo docs/apps/logs se connect hota hai, "System of
  Context" ka open reference implementation. **Yeh nahi hai:** System of Record (copies rakhta hai,
  originals nahi), permission system (apna kuch enforce nahi karta), answer (retrieval hit = pointer).
  **Model bhi source nahi** — retrieval khaali ho to model apni knowledge se plausible jawab de dega,
  koi error dikhaye bina. Standard mode install karo, **Lite nahi** (Lite vector index+workers disable
  karta hai). Min resources: 4 vCPU, 10GB RAM.
- **Concept 4 — Onyx vs Glean:** Glean commercial System of Context hai. Rule: "hum woh sikhate hain jo
  aap khol sakte ho." Architecture same hai dono mein — course ka zyada tar hissa **product ke baare mein
  hai hi nahi**, 7 cheezein jo aap khud banate ho (professional judgment, platform feature nahi).

## 01 — Pehla Corpus (Concepts 5-9)

- **Concept 5 — Shared Method Pehle, Phir Customer:** synthetic Northstar company: `sales-sor/` (3 rules),
  `accounting-sor/` (4 rules, 1 jaan-boojh kar superseded), `operational/` (2 JSON, kabhi index nahi),
  `working-context/` (emails/chats, ek finance-agreement ka unsupported claim). 3 alag connectors kabhi
  merge nahi. **Aap jo connect karte ho woh kabhi aapka nahi banta** — sirf promotion law se material
  upar move hota hai (3+ customers repeat, de-identify, review, apni voice mein rewrite). Document Sets =
  search scope, authority hierarchy nahi.
- **Concept 6 — Chunker Kya Feka:** governed record 12 metadata fields carry karta hai (stable ID,
  domain, authority class, jurisdiction, version, effective date, approval status, applicability, owner,
  superseded-by, checker, permission boundary) — generic indexing sirf sentence rakhti hai, 12 controls
  gayab ho jate hain silently.
- **Concept 7 — 3 Sawal Har Result Par:** kahan se aya (Onyx achha karta hai)? Kya banda dekh sakta hai
  (abhi honest jawab: sab sab dekh sakte hain)? Kya abhi bhi governs karta hai (Onyx nahi bata sakta)?
  **Retrieval hit pointer hai, answer nahi.**
- **Concept 8 — Permission Inheritance:** sabse important, sabse zyada skip hone wala concept. Community
  Edition mein permission-sync/RBAC **nahi** milta (sirf Cloud/Enterprise mein) — pure lab mein har
  student same corpus dekhta hai. Jab tak permission test pass na kare, koi real corpus (employer/client/
  apna inbox) connect mat karo — untested layer "fast lekin galat-rules-pointed" hota hai.
- **Concept 9 — Khud Gate Banao:** order zaroori — identity resolve → permissions resolve → eligible docs
  filter (**retrieval se pehle**) → retrieve+rank → answer assemble → action rights alag resolve. Unsafe
  order: sab retrieve kar ke model ko bolna "jo na dikhe uska zikr mat karo" — **model context ke andar
  chhupa passage chhupa nahi hota.** Test: `account_executive` role se manager-ki-email wala sawal poochna
  chahiye ke "kuch na mile." Control-review angle: untested layer certified access-review ko invalidate
  kar deta hai.

## 02 — The Governed Half (Concepts 10-11)

- **Concept 10 — Two-Call Pattern:** Neon mein `governed.rule` table (stable_id, domain, authority_class,
  jurisdiction, version, effective_from/to, approval_status, superseded_by, owner, body). FastMCP server
  `vertical-sor` 3 read-only tools: `search_rules`, `confirm_rule`, `validate_action` — kabhi connector se
  crawl nahi, hamesha **poocha** jata hai. **Discovery** = kahan ho sakti hai (recall/speed, pointer
  return); **Confirmation** = officially applicable kaunsa (domain/class/jurisdiction/version/approval
  check, answer return). Demo: stale Neon branch par search stale jawab deta hai, `confirm_rule` current
  branch se correct karta hai — "**ek jawab se revenue book ho sakta hai, doosre se nahi.**"
- **Concept 11 — Live State:** balances/approvals/current versions kabhi index nahi hote — index karna
  stale copy banana hai. **Working context index karo. Governed knowledge discover karo. Current truth
  live query karo.** Format/length kuch decide nahi karta — **freshness risk sab decide karta hai.**

## 03 — Routing Aur Citing (Concepts 12-15)

- **Concept 12 — Authority Routing:** 3 sawal-shapes: "Rule kya hai?" → SoR discovery+confirmation;
  "Number kya hai?" → owning system ka typed query; "Case mein kya kaha gaya?" → working context evidence.
  Pehle profession decide hoti hai, phir source. `authority-map.yaml` prompt likhne se pehle likho —
  routes + rules (working context kabhi conclusion govern nahi karta, conflicts kabhi silently merge nahi).
- **Concept 13 — Provenance/Citation Envelope:** har item: source system, stable ID, authority class
  (law/standard/contract/policy/transaction/guidance/message/example), version+period, permission basis.
  Worker permitted context parh sakta hai lekin kabhi rule ki tarah present nahi kar sakta. Document Set
  ko Agent se directly attach mat karo (2 retrieval paths, gate bypass). Router mein sirf **Actions**
  (koi role-sensitive knowledge attach nahi) — 5 actions table: `search_permitted_context`, `confirm_rule`,
  `get_opportunity`, `get_contract_state`, `validate_action`. **7-Section Packet** fixed output shape:
  Decisions involved / Governing authority / Current facts / Supporting context / Conflicts and gaps /
  Permitted next steps / Citations — empty "Conflicts" section = checked-and-clean; missing heading =
  never checked. **Compression provenance ko marta hai** — prose compress karo, provenance kabhi nahi.
- **Concept 14 — Conflict Ek Result Hai:** 3 valid outcomes — resolved by scope, resolved by authority,
  unresolved-escalate. 4th (kabhi nahi hona chahiye): sources ko smooth sentence mein blend karna.
  "Disagreement gayab nahi hota, reviewable ban jata hai."
- **Concept 15 — Act Aur Record:** loop = layer dhoondta → Worker reason karta → governing record
  validate karta → tool act karta → owning system record karta. **Teesra step sab drop karte hain**
  — proposed action rule ke against check hona hi rule ko "real" banata hai, advisory nahi. Read,
  recommend, prepare, execute — alag grants, **access permission nahi hai**.

## 04 — Northstar Case End-to-End + Proving It (Parts 5-6)

- **The Case:** AE 20% discount maangta hai (approval pending), signed contract billing allow karta hai,
  Accounting SoR acceptance par revenue recognize karta hai (acceptance nahi mila), sales manager ki email
  kehti hai finance theek hai is quarter book karne se. Sawal: teenon (discount+invoice+revenue) mil sakte
  hain?
- Full build: Onyx + 4 source classes + Neon governed schema + `vertical-sor` MCP + 5 Document Sets +
  `authority-map.yaml` + context-gateway + Context Router (koi Document Set attach nahi, sirf Actions).
- **6 Checks:** permission-before-retrieval? har path gateway se? discovery/confirmation alag calls?
  operational state live? conflicts preserved (not summarized)? Neon record sirf MCP se (koi connector
  nahi)?
- Correct packet example diya gaya hai (Governing authority / Current facts / Supporting context /
  Conflicts and gaps / Permitted next steps) — **do alag refusals, ek blended "haan" nahi.**
- **5 Failure Tests (jaan-boojh kar todo):** email edit (conflict surface hona chahiye), stale Neon branch
  (confirmation correct kare), customer-state server band (refuse "current state confirm nahi ho sakti"),
  sales rules gateway se hatao (missing authority naam le, email substitute na kare), cross-domain
  Document Set directly attach karo (gate bypass expose hota hai). **"Confident, fluent, well-cited, poori
  tarah ghalat jawab" ek confirmation-call-miss se — yeh koi nahi bhoolta.**
- **8 Eval Dimensions:** Inventory, Routing, Authority, Freshness, Permission, Conflict, Gaps, Citation.
  Same model se professional-correctness auto-grade mat karo — authority/conclusion checks explicit
  expected-value comparisons rakho.

## 05 — Poore Workforce Ko Serve Karna Aur Operate Karna (Part 7)

- **2 tareeqe, ek hi permission boundary:** Native Onyx MCP server quick hai lekin **client apna scope
  choose karta hai** — Community Edition mein iska matlab "sab kuch." **Context Gateway MCP server** hi
  woh route hai jo tikta hai — bearer tokens server-side role-mapped, **role kabhi tool argument se nahi
  ata**. Token = boundary: TLS, per-person (per-role nahi), expiry zaroori — expire-na-hone-wala
  role-shaped token "job title likha hua shared password" hai. Test: same sawal 2 roles se, 2 alag
  results confirm.
- **Workforce test:** layer complete tab hota hai jab **har authorized human aur AI Worker** same governed
  inventory apni working surface se access kar sake, same identity/permission boundary ke sath.
- **Operate:** har connector ke 9 recorded fields (owner, source class, credential owner, refresh
  frequency, expected doc count, last sync, staleness, escalation). Trap: error ho to bhi search kaam
  karta rehta hai stale corpus par — "search working" ≠ "corpus current." Upgrade discipline: 8 steps
  (version record → release notes → backup → settings export → eval baseline → non-prod upgrade → evals
  dobara → compare).
- **Production Definition of Done:** 10-point checklist (classification, connector ownership, versioned
  routing, source-confirmed knowledge, live current facts, pre-retrieval permissions, visible
  conflicts/gaps, reopen-able citations, tested backups, SoC never rewrites SoR).
- **Digital FTE Bridge:** pichle course ne Worker ko owned knowledge di; yeh course ne company knowledge
  tak access diya (permission+provenance+confirmation ke sath). Digital FTE = is Worker ke around
  "contract of success" + outcome-pointing — retrieval yehi hai, authority governed record hai, trust
  model ki property nahi.

## 8 Rules — Poore Course Ka Nichor

1. Authority kabhi move nahi hoti — layer citation carry karta hai record tak, khud source nahi banta
2. Relevance authority nahi hai — routing pehle decide hoti hai
3. Permission inherit hoti hai, invent nahi — model se pehle enforce hoti hai
4. Freshness field-by-field decide hoti hai — working context index, governed knowledge discover, current truth live query
5. Provenance har item ke saath travel karti hai, compression usay kabhi strip nahi karta
6. Conflict preserve aur escalate hota hai, blend nahi hota
7. Working context chupke se governing authority nahi banta — promotion authorship hai, reviewed
8. Discovery confirmation nahi hai — search hit pointer hai, governing record confirm karta hai
