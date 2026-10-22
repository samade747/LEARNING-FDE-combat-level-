# 03 — Discipline 3: The Error Taxonomy

Yeh discipline **What AI Actually Is** ke Idea 3 ka practical jawab hai: machine ka apna
truth-checker nahi hai, **tum ho**. 6 error types yehi hain "checker hona" ka practical matlab.

AI se sawal poochte, answer smooth+professional aata, use kar lete. 3 din baad pata chalta ek
number galat tha, source exist nahi karta. Mistake wahan thi, par writing itni achhi thi ke miss
ho gayi. **Mistake jo pay karta usually tumhi ho** — checker nahi jo baad mein pakde.

**Taxonomy kyun?** Naming system hai — fixed labeled categories. Farq: 1 AI sentence 2 error types
mein fit ho sakta. Power **naming** mein hai — "check karo yeh achha hai" bohot vague, eyes slide
over. "Check karo fabricated source hai ya nahi" specific hunt hai, specific target ke sath.

## 6 Error Types

| Type | Kaisa Dikhta | Kahan Pehle Dekho |
|---|---|---|
| **Factual error** | Galat number/date/naam | Koi bhi specific-number wala sentence |
| **Logical gap** | Conclusion evidence se follow nahi karta | "Therefore"/"so" words, pucho evidence prove karta? |
| **False confidence** | Uncertain cheez ko fact ki tarah bola | Smoothest paragraphs — "may"/"could" na ho |
| **Missing context** | Important detail chhod di jo answer change karti | Expert kya pehle puchta? |
| **Fabricated source** | Book/article/study jo exist nahi karta | Har named source — title search karo |
| **Stale fact** | Pehle true thi, ab nahi | Time ke sath change hone wali cheez: price, rules, laws |

**Technique:** output ek baar parho, par **6 sawalon ke sath** zehan mein, har sawal jahan ruke
wahan ruko. 6 baar nahi parhna — ek baar, 6 questions ke sath.

## Worked Example — Used Car

Parent ek 2021 Honda CR-V shortlist kar rahe the, Claude se listing+photos+mechanic-note ke sath
likha bola. Claude confident summary di — almost forward kar dete, par 6-row scan chalaya:

| Type | Mila | Verdict |
|---|---|---|
| Factual error | "32,000 miles" likha, photo mein 58,000 dikha | Caught, photo se correct kiya |
| Logical gap | "Clean accident history, therefore no mechanical problems" | Caught, clean history ≠ clean engine |
| False confidence | "200,000 trouble-free miles guaranteed" | Caught, "many CR-Vs last long if serviced" likha |
| Missing context | Timing belt (60,000 miles par due) mention nahi hui — mechanic ne flagged kiya tha | Caught, add kiya |
| Fabricated source | "Consumer Reports March 2026" quote jo exist nahi karti | Caught, hataya |
| Stale fact | "$1,000 rebate abhi bhi valid" — pichle mahine khatam hui | Caught, math se hataya |

5/6 error types ek hi summary mein mile. Sabse hard: fake Consumer Reports quote — real magazine
jaisi lagti thi.

> **Topic nahi aata to:** AI se exact source maango (author/title/year); precise-lagte numbers se
> suspicious raho jinka source na ho; 2 minute mein check nahi kar sakte to ACCEPT na karo, MODIFY
> likho "not yet checked."

## Research Ke Peeche

- **Processing fluency (Alter & Oppenheimer, 2009):** jo parhna aasan hota, usay zyada trust karte
  — true ho ya na ho. AI bohot smoothly likhta — isi bias ka near-perfect trigger. Named-error-scan
  "feels true" se "checks out" ki taraf shift karta.
- **Cognitive ease (Kahneman, 2011):** effort-free info fast System 1 accept kar leta, slow System 2
  so jata. Smooth AI prose System 2 ko so-ne deta. Har named check System 1 autopilot tod deta.
- **Confidence ≠ accuracy (Nate Silver, 2012):** jo sabse confident sunte, aksar sabse kam accurate
  hote. False-confidence row tone ko truth se separate karta.
- **Gerd Gigerenzer:** murky judgment ("yeh achha hai?") ko concrete pieces mein todna accuracy
  badhata, facts change na hon tab bhi. 6 sawal ek murky judgment ko 6 concrete pieces mein todte.
