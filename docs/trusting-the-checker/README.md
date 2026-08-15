# Trusting the Checker — Notes (Roman Urdu + English)

Ye notes **"Trusting the Checker: An Evals Crash Course"** chapter ka easy explainer hain (Loop →
Harness → Graph → Trusting the Checker, position #11), Panaversity ke **The AI Agent Factory** book se
(Zia Tutor AI connector ke zariye).

Source: https://agentfactory.panaversity.org/docs/trusting-the-checker-crash-course

## Index

1. [00 — Overview: "PASS" Ka Masla](00-overview.md)
2. [01 — Golden Set (Test Cases Kahan Se Aate Hain)](01-golden-set.md)
3. [02 — Judge Ko Calibrate Karna](02-calibrating-judge.md)
4. [03 — Evals Loop Ke Andar (Regression + Drift)](03-evals-in-loop.md)
5. [04 — Ek Complete Eval Suite (Reviewer Ka Performance Review)](04-complete-eval-suite.md)
6. [05 — Staying Honest (Goodhart's Law + Limits)](05-staying-honest.md)
7. [06 — Practice Projects (8 eval builds)](06-practice-projects.md)

## Ek Line Mein Poori Cheez

> **Aapka poora system ek lafz pe khara hai: "PASS".** Loop course ne kaha rubric score *"a claim, not
> a proof"* hai. Harness course ne kaha *"a harness change without a re-run eval is a guess."* Ye course
> wo qarz chukati hai — **evals** sikhati hai: tester ko test karne ka discipline, taake *"checker ne
> PASS kaha"* ek aisi statement ban jaye jo aap **number se defend** kar sako.

## Zaroori Farq

- **Test** ek specific property verify karta hai — run twice, same jawab
- **Eval** estimate karta hai ke probabilistic system representative cases mein kitna acha perform karta
  hai — usually repeated runs pe. Agent ek **distribution** hai, ek fixed answer nahi.

**Koi framework, koi Python package, koi dashboard nahi** — poora eval suite chhoti files ka folder,
shell script, aur `jq` hai.
