# 13 — Where to Go Next

Book ke apne pointers, agla kya seekhna hai:

- **Ek se zyada loop chala rahe ho?** Jis lamhe do loops kaam exchange karti hain ya state share karti
  hain, aapko wiring aur shared memory chahiye: [Graph Engineering](https://agentfactory.panaversity.org/docs/graph-engineering-crash-course),
  isi series mein 2 steps aage, dono cover karta hai. (Is repo mein: [`docs/graph-engineering`](../graph-engineering/README.md))
- **Non-coding kaam ke liye loops bana rahe ho?** [Cowork & OpenWork crash course](https://agentfactory.panaversity.org/docs/cowork-crash-course)
  wahi heartbeat idea professionals ke liye dikhati hai, cron ki jagah scheduled tasks ke sath. (Is repo
  mein: [`docs/cowork`](../cowork/README.md))
- **Terminal ki jagah API se loops chalana?** Claude Platform ke **Managed Agents** ab scheduled
  deployments support karte hain (public beta): agent ko cron schedule do, har firing Anthropic ki apni
  infrastructure par fresh session start karti hai — koi scheduler aapko khud build/host nahi karna.
  Yehi Routines wala idea hai, platform primitive ki tarah offer kiya hua. Schedule heartbeat hai, prompt
  beat hai, aur spine abhi bhi aap supply karte ho.
- **Improvement loop khud managed chahiye?** Wahi Managed Agents platform memory aur dreaming tooling
  include karta hai — Concept 12 ke out-of-band improvement pass wala idea, product ki tarah offer kiya
  hua. Shape wahi hai: batch job heartbeat hai, memory store spine hai, approval step human gate hai.
- **Checker bhi managed chahiye?** Do research previews verification-skills interlude ko products bana
  dete hain. **Code Review** har PR par (jo aap enable karo) managed multi-agent review pass chalata hai.
  **Rubrics in Claude Managed Agents** (beta) Concept 2 wala rubric-with-a-bar platform primitive ki
  tarah hai, jahan alag grader agent outcomes verify karta hai aur fail hui cheez ko dobara attempt ke
  liye bhej deta hai. Model ke grade pe kitna bharosa karna hai — [Trusting the Checker course](https://agentfactory.panaversity.org/docs/trusting-the-checker-crash-course)
  (is repo mein [`docs/trusting-the-checker`](../trusting-the-checker/README.md)).
- **Unattended runs ke liye retries tune karna?** Claude Code ka [Error reference](https://code.claude.com/docs/en/errors)
  automatic-retry settings document karta hai, `CLAUDE_CODE_MAX_RETRIES` aur CI-style unattended sessions
  ke liye `CLAUDE_CODE_RETRY_WATCHDOG` mode sameet.
- **Clone-and-run starting points chahiye?** Community repo [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)
  (MIT) production loop patterns (daily triage, PR monitor, CI checker, dependency checker, changelog
  drafter) starter kits ki tarah collect karta hai, readiness checklist ke sath, kai agent CLIs par
  mapped. Third-party aur young hai, maintained hone ka check karo. Iski primitives table isi course ke
  6 parts hain, doosre naam se. Reading trail ke liye [awesome-loop-engineering](https://huggingface.co/datasets/cy0307/awesome-loop-engineering)
  collection (Hugging Face) primary articles ek jagah rakhta hai.
- **[Spec-Driven Development](https://agentfactory.panaversity.org/docs/spec-driven-development-crash-course)**
  mein jo spec likhi thi wo hi aapke loop ki **stopping condition** hai: uske acceptance criteria wahi
  hain jo checker grade karta hai aur `/goal` prove karta hai stop karne se pehle. Jab loop unsafe lage
  chhorne ke liye, fix zyada tar ek **sharper spec** hoti hai, zyada automation nahi. (Is repo mein
  [`docs/spec-driven-development`](../spec-driven-development/README.md))

---
[⬅ Key Words Glossary](12-key-words-glossary.md) · [Agla: Sources & Further Reading ➡](14-sources-further-reading.md) · [⬆ Index](README.md)
