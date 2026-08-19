# Is This an Agent Problem? — Summary

Ek 3-Gates mental checklist jo tool kholne se **pehle** chalti hai: kaunsa kaam agent ko dena chahiye,
kaunsa nahi — kisi tool ka naam liye bina, sirf kaam ki nature dekh kar.

## 00 — Overview: Ana vs Yusuf

- Kahani: Ana 10 min ruk kar 3 sawal khud se poochti hai tool kholne se pehle; Yusuf seedha tool kholta
  hai. Same kaam, same tool, alag result — Ana ka trust-worthy hai, Yusuf ka nahi.
- **Rule in one line:** *"The cheapest mistake to fix is the one you catch before you start."* Plan mein
  galti free hai; agent ke ek ghante ke ghalat kaam ke baad pakdi gayi galti wapis nahi ati.
- Reminder: chatbot **jawab deta hai**, agent **jaake kaam karta hai**.
- Teen Gates table: Gate 1 (kya isko agent chahiye?), Gate 2 (ek dafa ya har hafte?), Gate 3 (finished
  kaisa dikhta hai?) — order mein chalte hain, ek skip karo to uski galti hoti hai.
- 3 short bullets: har AI kaam ko agent nahi chahiye; kitni baar karte ho decide karta hai; "finished"
  pehle decide karo.

## 01 — Gate 1: Does This Need an Agent At All?

- **Check 1a:** Agar task ek exact, har-baar-same step mein describe ho sakta hai → regular tool
  (spreadsheet, search box, find-replace), AI nahi. Judgment/mixed-file-types/no-existing-app chahiye →
  AI job hai.
- **Check 1b:** Sirf jawab chahiye (kuch bhi aapka nahi chhuta) → chatbot. Files/data par **act** karna
  hai → agent. Poora farq: jawab vs action.
- Cooking analogy: "anda kitni der ubaalu" = chatbot; "fridge dekho aur list banao" = agent; "prices
  jodo" = calculator (koi bhi nahi).
- Mei's worked example: 4 morning tasks, 2 nikle AI tasks bhi nahi (spreadsheet, chatbot), 2 agent (folder
  scan + judgment). Gate 1 kaam ko rokta hai jo wahan belong nahi karta, agent ki taraf dhakelta nahi.

## 02 — Gate 2: Once, or Every Week? (Mode 1 vs Mode 2)

- **Mode 1** = ek dafa solve karo (agent kholo, kaam karo, chale jao). **Mode 2** = permanent helper banao
  (Digital FTE) — sirf tab worth jab kaam bar bar wapis aye.
- **3 Dials**, sab upar honay chahiye Mode 2 ke liye: (1) kitni baar (repeat?), (2) kitna same (shape
  identical?), (3) worth it (time/items/error-cost/hassle justify karta hai?).
- Sabse mehnga galti **quiet** hai: Mode 2-worthy kaam ko hamesha haath se karte rehna (chota lagta hai
  har baar, saal mein 20+ ghante ban jata hai).
- **Rule:** teesri baar jab wahi kaam wahi tareeqe se karo, ruko aur Gate 2 chalao — deliberate check
  banao, feeling ka intezaar mat karo.
- David's example: naya-employee setup (low freq, low sameness → Mode 1 hamesha) vs Monday summary
  (high/high/worth-it → Mode 2). Same banda, same hafta, opposite answers.

## 03 — Gate 3: What Does "Finished" Look Like?

- 3 chhoti lines agent kholne se pehle: (1) **works from** (input — specific, "mere emails" vague hai),
  (2) **chahiye akhir mein** (output shape, sirf topic nahi), (3) **done-check** (testable, ek minute
  mein confirm ho sake — "acha hai" jaisa vague nahi).
- Gate 3 **target** decide karta hai, prompt likhna nahi — instructions kaise phrase karein woh agla
  course sikhata hai.
- Ana's worked example: works-from (support folder, 400 messages, 7 din), chahiye (spreadsheet + one-page
  note), done-check (counts 400 tak jodna). Yusuf ke paas yeh kuch nahi tha — result trust/check nahi
  kar saka.

## 04 — Worked Example + Reference Card

- Teenon gates ek real task par ek sitting mein chalana: Gate 1 → tool/chatbot/agent; Gate 2 → Mode
  1/Mode 2; Gate 3 → teen lines. Gates ~10 min lete hain, jo galtiyan rokte hain woh poori dopeher (ya
  mahine, Mode 2 ke liye) le sakti hain.
- **Reference Card (tool-agnostic, 2026 tools ke sath):** Sirf jawab → claude.ai/ChatGPT/Gemini. Ek dafa
  solve → Claude Code/OpenCode/Cowork/OpenWork. Worker khud own karo (ownership choice, mode nahi) →
  OpenClaw/Hermes. Manufacture karo → OpenAI Agents SDK/managed Claude agent.
- **Ownership vs Mode — 2 alag sawal, kabhi collide nahi:** Ownership poochta hai "drive karta hoon ya
  own karta hoon?"; Mode poochta hai "ek dafa solve ya lasting banata hoon?"

## 05 — Practice Exercises

- **Exercise 1 (Gate 1):** 5 hafte-ke tasks lo, har ek ka exit (tool/chatbot/agent) + wajah likho. Red
  flag: sab 5 "agent" ban jayein to force kar rahe ho.
- **Exercise 2 (Gate 2):** 3 repeat-hue tasks, 3 dials set karo, Mode 1/2 verdict. Sabse valuable finding:
  jo task surprise kare (haath se karte rahe, nikla Mode 2).
- **Exercise 3 (Gate 3):** Sabse recent real task, teen lines likho, done-check ko sharp karo jab tak
  testable na ho.
- **Research background (optional):** Gate 1 — Kaplan's *law of the instrument* (1964), Maslow (1966),
  Task-Technology Fit (Goodhue & Thompson, 1995). Gate 2 — Fowler's *Rule of Three* (1999), Knuth's
  "premature optimization" (1974), xkcd 1205. Gate 3 — Locke & Latham *goal-setting theory* (2002),
  Definition of Done practice.
