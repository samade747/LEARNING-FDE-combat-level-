# The Four Layers: Prompt, Context, Harness, Loop — Summary

Chapter #7 (General Agents group ka aakhri chapter) — poori curriculum ko ek chhoti **map** mein samet
ta hai. Core idea: 4 layers **containers hain, steps nahi**, ek doosre ke andar nested, har ek alag
unit-of-work ka zimmedar. Jab kuch toote, sawal hai "kaunsi layer toti?"

## 00 — The Shape

- **Opening story:** Agent 40 minute chalta hai, $50 kharch karta hai, kuch use layak nahi banata — log
  prompt badalte hain (10 second edit) lekin asal fix ek alag layer mein tha (~11 lafzon ka, jo koi
  jaanta nahi tha).
- **Concept 1 — Containers, Steps Nahi:** Sabse common galti — layers ko ladder ki tarah draw karna
  (prompt beginners ke liye, loop experts ke liye). Galat aur mehnga: outer layer baad mein nahi hai,
  zyada zaroori nahi hai, alag box sizes nahi hain — 4 genuinely alag objects hain jo **wrap** hoti hain,
  chhorti nahi.
- **Concept 2 — Unit-of-Work Test:** Prompt = ek model call; Context = poori window; Harness = ek beat
  (instruction se agent khamosh hone tak); Loop = poori run (koi type nahi kar raha). Vocabulary badle
  bhi to yeh test kaam karta hai — "kaunsa unit of work discuss ho raha hai?" poocho.

## 01 — 4 Layers, Ek Ek Kar Ke

- **Concept 3 — Prompt (ek model call):** Craft narrow hai — kamzor ingredient dhoondo, sirf usay fix
  karo. Prompt toti hai jab: task samjha gaya, roughly sahi kaam hua, lekin galat shape/length/voice —
  kuch factually galat nahi hai.
- **Concept 4 — Context (poori window):** Missing document se model khaali nahi hota — training se
  seekha hua confidently uthata hai. Harness ek **curator** hai — 3 kaam: order (lost-in-the-middle),
  compression (free nahi), dropping policy. **Curator test:** kisi document ko point karo, poocho
  kaunsi rule ne usay wahan daala — jawab "retriever ne wapas kar diya" ho to search box hai, curator
  nahi. Context toti hai jab: jawab confident, fluent, factually galat — aksar kisi **aur** sach cheez
  ke qareeb.
- **Concept 5 — Harness (ek beat):** Job list — context assemble, model call, tools chalao, results
  wapas do, errors handle karo, beat khatam hone se pehle enforce karo. Subagents surprise: tool ki
  tarah call hote hain lekin apni window kholte hain aur poori nested beat chalate hain — wapas aata hai
  summary, poore confidence ke sath, samet us hisse ke jo galat tha.
- **Concept 6 — Turning point: beat kya prove kar sakti hai:** Beat khatam kai wajahon se ho sakti hai
  (timeout, token ceiling, error, model-decides) — koi bhi prove nahi karta kaam successful tha, sirf
  itna ke beat khatam hui. Achi harness real checks enforce kar sakti hai (verification), lekin **"check
  pass hui" aur "check pass hona KAAFI thi" alag baat hai** — dusra loop ka kaam hai. Bank-reconciliation
  example: sab internal signals healthy, claim phir bhi galat.
- **Concept 7 — Loop (poori run):** Heartbeat (schedule/event/condition, warna aap khud heartbeat ho),
  Spine (model ke bahar state, agli beat ko pichli ka pata ho), Outside stops (success condition, limits,
  no-progress check, alag checker). Maker-checker rule: koi bhi stop maker se nahi poochta wo khatam hai.
- **Concept 8 — Human Gate:** Stops = safely fail; Gate = madad ke sath succeed. Ambiguity error nahi
  hai (invoice example — 2 payments 0.52 score dono). Guessing khatarnak hai kyunki silent hai (crash
  loud hota hai). Gate pehle se likha hota hai, triggers: confidence threshold, value limit, hard-to-undo
  action. Jawab naye evidence ki tarah wapas enter hota hai, run wahin se jari rehta hai.

## 02 — Map Use Karna

- **Concept 9 — Kaunsi layer toti?** Table: shape/tone galat par task samjha → Prompt; confident-fluent-
  factually-galat → Context; unproven success claim → Harness; unchecked galat jawab aage jaye →
  Loop/checker; kabhi na ruke/jaldi ruke/guess kare → Loop/stops-gate. Yeh **search order hai, verdict
  nahi** — failures layers cross karte rehte hain. 5-second layer-naming discipline ek fix vs 6 fixes ka
  farq banata hai.
- **Concept 10 — Kaunsi layers aap own karte ho:** Mode 1 (general agent) mein zyada tar 3 **rent**
  karte ho (harness/loop rented, context partly). Mode 2 (Worker manufacture) mein sab 4 aapki. "Mera
  tool ye sab karta hai" ehtiyat: tool **apne** kaam ke liye karta hai, jo Worker aap banate ho uske liye
  nahi. 4-minute check: window bharne pe kya hataata hai, retry kitni dafa, run-limit pe kya hota hai.
- **Concept 11 — Graphs kahan fit hote hain:** Graph 5th layer **nahi** hai — 4 layers ek node ke andar
  kya hota hai describe karte, graph nodes ke darmiyan kya hota hai describe karta hai. Node agent hona
  zaroori nahi (function/rule/tool call/human gate/measurement ho sakta hai). 3 uses: execution graph,
  memory graph, governance graph. 6-node example (Pull, Route, Match [sirf yeh agent hai], Gate, Prove,
  Post) — token cost zyada tar Match ke andar hota hai.
- **Concept 12 — Jab framework aapse larta hai:** Kuch failures genuinely 2-layer hain (dono honestly).
  Kuch diagnoses ek layer point karte, fix doosri layer pe hoti (success-report example: diagnosis
  layer 3, fix layer 4). Kuch failures in 4 mein se koi nahi — model genuinely task nahi kar sakta,
  honest move: behtar model/chhota task/alag approach. Har project ko 4 nahi chahiye.

## 03 — Practice (8-Case Drill)

- 8 worked failure cases, har ek jawab ke sath (layer + fix): (1) format-wrong-content-right → Prompt;
  (2) confident-wrong-pricing → Context; (3) false "all tests passing" report → diagnosis Harness, fix
  Loop (outside stop); (4) budget khatam, wahi 3 approaches repeat → Loop (no-progress check); (5)
  ambiguous invoice-match silently guessed → Loop, missing Gate; (6) subagent summary mein 2 galat claims
  → Harness (confident nested summary — fix: quotes/IDs/receipts); (7) 20-turn session decision se
  contradict karta hai → Context (dropping policy); (8) sab 4 layers clear, phir bhi mediocre → In mein
  se koi nahi (capability limit, Concept 12).
- **Apni khud ki failure pe try karo** — 3-question framework (kaunsa unit of work galat? baad mein kya
  badla, wahi layer thi? kya pakar leta?), legal-ops contract example (team ne prompt badla jab failure
  layer 4 pe thi — pakadta: pehle-se-chuna success condition).
- **Poori section ka nichod:** "A good prompt fails inside bad context. Good context fails inside a bare
  harness. A good harness sits idle without a loop. So when something breaks, name the layer before you
  reach for a fix." — poore chapter ka yaad rakhne layak ek sentence.
