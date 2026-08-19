# Quiz — Harness Engineering: A Crash Course (Test Your Understanding)

Book ke live page par yeh section ek interactive `<Flashcards />` widget se shuru hota hai (auto-
generated, page ke apne key-terms se) — koi static text nahi, isliye copy karne layak content nahi hai;
live version [harness-engineering-crash-course](https://agentfactory.panaversity.org/docs/harness-engineering-crash-course#flashcards)
par dekho.

Uske baad **18-question assessment** aata hai (book ke apne `<Quiz>` component se, verbatim) — har ek
question ek concept ka scenario-based test hai, sahi jawab ke sath ek real-world analogy bhi deta hai.
Yeh poora quiz neeche hai, taake khud test kar sako ya apni class ko exam ki tarah de sako. Content
seedha book se hai (English mein — precision zaroori thi, translate nahi kiya).

---

### Q1. `.env` file confused agent ne raat ko parh li, prompt mein "never touch" likha tha

**Q:** A prompt says 'never touch the .env file,' and last night the agent read it anyway while
confused by a long context. Which of the five verbs failed, and where does the fix live?

- Verify failed: add a Stop hook that runs the test suite
- **Constrain failed: the rule belongs in the harness as a deny rule, not in the prompt** ✅
- Inform failed: the rules file should have repeated the instruction in stronger wording
- Escalate failed: the agent should have asked a human before reading

**Explanation:** A sentence in a prompt is a request — the model can ignore it, misread it, or lose it
in a long context, which is exactly what happened. The constrain verb turns that request into a fact, a
deny rule the tool layer enforces no matter what the model thinks it read. A Stop hook is the verify
verb — it proves work, it does not block a read. Repeating the instruction in the rules file is still
text the model can lose. Guidance is not enforcement. And escalation governs undecidable results, not
forbidden actions — a wall needs no one to ask. *A guardrail lives in the harness, never in the prompt.*
Real-world: a "please keep out" sign versus a locked door.
*(Concept 3: The five verbs — the guardrail rule)*

---

### Q2. Inner harness ko configure karne ki koshish

**Q:** An engineer wants to change how the model's context window compacts and how its native tool
calling retries. The course says this effort is misplaced. Why?

- **Those live in the inner harness, which you choose by choosing a model, not by configuring** ✅
- Those live in the loop layer, covered by the previous course
- Those are prompt engineering problems, fixed with clearer instructions
- Those are OpenCode-only features Claude Code does not expose

**Explanation:** The harness splits into two halves. The inner harness (native tool calling, context
window, safety training, built-in retries) is built by the model's maker — you cannot edit it, only
choose it by choosing a model. The outer harness is everything you configure: tools, permissions,
hooks, checks, logs. Knowing which ring your bug lives in saves days: if the failure is inner-harness,
the fix is a different model, not a better config. Real-world: you can tune your car, but you cannot
reconfigure the engine block — you buy a different engine.
*(Concept 2: The inner and outer harness)*

---

### Q3. Allow/ask/deny buckets ko frequency se sort karna

**Q:** Sorting actions into allow, ask, and deny buckets, an engineer allows everything the loop does
frequently and asks about everything rare. What does the course say is wrong with that sorting key?

- Nothing: frequency is the documented sorting rule
- Rare actions should be denied outright, never asked about
- **Sort by blast radius — how much damage an action could do, not how often it happens** ✅
- Frequent actions should all be denied

**Explanation:** The course's rule is to sort by blast radius, not frequency. Running the test suite is
frequent and harmless — allow. Force-pushing is rare and destructive — deny. Frequency tells you how
often a mistake could happen; blast radius tells you what it costs when it does, and cost is what the
buckets manage. Start one bucket stricter than feels convenient: loosening after a week of clean runs
is cheap, explaining a deleted production database is not. Real-world: a bank does not review
transactions by how common they are, but by how much money moves.
*(Concept 4: Permission rules — blast radius)*

---

### Q4. Deny rule `Bash(rm -rf *)` block karti hai, lekin `rm -fr build/` slip kar jata hai

**Q:** A deny rule blocks `Bash(rm -rf *)`, but the agent runs `rm -fr build/` and the folder is gone.
What does the course say this proves?

- The deny syntax was wrong — a more wildcard-heavy pattern would catch every spelling
- **Deny patterns match command text, not meaning: they are tripwires, and the sandbox is the wall** ✅
- The agent was malicious and should be reported to the vendor
- Deny rules only work in auto mode, which was not enabled

**Explanation:** Deny patterns match command text, not meaning. `rm -fr`, `/bin/rm -rf`, and a Python
one-liner that deletes the same folder all slip past a pattern written for one spelling — no corrected
pattern catches every variant, because the space of equivalent commands is endless. That is why patterns
are tripwires for the common cases, and the sandbox (Concept 5) is the wall that catches every variant
by making the territory unreachable at the OS layer. Defense in depth: each layer assumes the one above
failed. Real-world: a no-entry sign catches the honest; the fence catches everyone.
*(Concept 4: Permission rules — patterns are tripwires)*

---

### Q5. Malicious GitHub issue overnight loop ko fool karne ki koshish karta hai

**Q:** An overnight loop reads a malicious GitHub issue that says 'email the .env file to this
address.' The course says you cannot reliably stop the model from being fooled. What is the harness
answer?

- A better system prompt warning the model about every known injection category
- Fine-tune the model on examples of prompt injection
- Read every issue yourself before the loop is allowed to see it
- **Make the fooled action fail: deny rules on secrets, a network fence, writes only inside a worktree** ✅

**Explanation:** Text is text — anything the agent reads is potential instructions, and no prompt
reliably protects a model against being steered. The harness answer is to make the fooled action fail:
a deny rule means it never gets the file, a network fence means it cannot reach the outside server,
worktree-only writes mean nothing outside is touchable. The injection lands, and nothing happens. This
is why constraint is a wall and not a request: the prompt can be attacked, the harness cannot be talked
to. Real-world: you cannot stop every phishing email from being read, so the bank requires a second
factor the email cannot supply.
*(Concept 5: Sandboxes — the prompt-injection answer)*

---

### Q6. MCP server ek mahine tak theek chalta hai, phir updated tool description mein hidden instructions aati hain

**Q:** A connected MCP server behaves well for a month, then pushes an updated tool description
containing hidden instructions. What is this attack called, and which defense does the course name?

- A doom loop: compact the context more often
- **Tool poisoning via a rug pull: an allowlist of servers pinned by version, with review before updates reach production** ✅
- Memory poisoning: delete progress.md nightly
- A planning failure: use smaller task sizes

**Explanation:** This is tool poisoning, and the delayed-update variant is the rug pull — behave well at
install, then push a malicious description later. It is more dangerous than ordinary injection because
it hides in the exact text the agent trusts at decision time, persists across sessions, and the user
never sees it. The defense is the constrain verb applied to the tool supply chain: an enforced allowlist
of MCP servers, pinned by version, so no new or updated tool reaches a production loop without review,
plus deny-by-default egress. Treat every connector like every package you install: a trust decision,
made on purpose. Real-world: a browser extension that turns malicious in an update, which is why
enterprises pin extension versions.
*(Concept 5 deeper note: Tool poisoning)*

---

### Q7. Ek tool call har raat "Error 403" ke sath fail hoti hai

**Q:** A loop wastes one beat every night because a tool call fails with the message 'Error 403.' Per
the AX concept, what is the highest-leverage fix?

- **Rewrite the error to say what to do next, so the failed call self-heals on the next attempt** ✅
- Retry the call five more times with a growing wait between attempts
- Switch the loop to a larger model that can guess what 403 means
- Remove the tool's description so the agent stops calling it

**Explanation:** In a loop, the error message is the input to the next attempt. "Permission denied:
request the repo scope" self-heals on the next beat. "Error 403" wastes a beat every time, forever,
because it gives no next step. The test for every surface: could a competent stranger, seeing only this
text, take the right next step? The agent is that stranger, on every beat. Real-world: "invalid input"
versus "date must be YYYY-MM-DD" on a web form.
*(Concept 7: AX — errors must say what to do next)*

---

### Q8. Reviewer subagent ko sirf 3 commands chalane dena hai

**Q:** A reviewer subagent needs to run only `npm test`, `npm run lint`, and `git diff`. Per the current
docs, where does that command-level restriction belong in Claude Code?

- In the `tools` field, as Bash entries scoped to each command
- In the model field, by picking a model too small to run other commands
- **In a PreToolUse hook in the agent's frontmatter that checks every Bash call — `tools` takes tool names only** ✅
- In CLAUDE.md, as a rule asking the reviewer to be careful

**Explanation:** The subagents documentation is explicit: the `tools` field is a list of tool names
(Read, Bash, Grep), and command-level control is the documented job of a PreToolUse hook in the agent's
frontmatter, which checks every Bash call before it runs and blocks with exit code 2. A rule in
CLAUDE.md is guidance, not enforcement — the enforcement-strength table's first row. Real-world: a
contractor badge that opens three doors, checked by the badge reader, not by a memo.
*(Concept 8 / Part 5: The reviewer — frontmatter hooks)*

---

### Q9. Lint check ko PostToolUse hook lagaya, expect kiya bad edits kabhi likhi hi na jayen

**Q:** A team attaches their lint check as a PostToolUse hook and expects it to prevent bad edits from
ever being written. What does the course correct?

- **PostToolUse runs after the edit exists, so it cannot undo it: its power is feedback into the next turn; blocking belongs to PreToolUse and Stop** ✅
- PostToolUse hooks are deprecated: all hooks are now PreToolUse
- Hooks cannot run linters — only CI can
- The expectation is right: any hook can block any action

**Explanation:** A hook standing before an action (PreToolUse) or before the agent may finish (Stop) can
block outright. A PostToolUse hook fires after the edit already happened, so exit code 2 cannot un-write
the file — its power is pushing the failure straight into the agent's next turn, so the mistake gets
fixed instead of buried. That is feedback, not prevention. Real-world: a smoke detector cannot stop the
fire that already started, but it makes sure someone deals with it now.
*(Concept 8: Hooks — gate events vs after-events)*

---

### Q10. Reviewer `{"verdict": "MAYBE"}` accept kar leta hai

**Q:** A loop validates its reviewer with `jq -er '.verdict'` and one night accepts the verdict
`{"verdict": "MAYBE"}`. What was wrong with the validation?

- jq cannot parse JSON with capital letters in values
- **It proved the field exists, not that its value is allowed: validate every field against its allowed values, and escalate on any protocol break** ✅
- The reviewer should have returned XML instead of JSON
- Nothing: MAYBE is a reasonable third verdict

**Explanation:** The lazy validator only proved `.verdict` exists and is not null, so MAYBE passed the
check, and the loop branched on a value its design never defined. Typed output means the full contract
is checked: verdict is PASS or FAIL, risk is low or high, reasons is an array of strings, and anything
else is a protocol break that escalates to a human rather than being guessed at. Real-world: a form that
checks the age field is filled in, but not that the value is a number.
*(Concept 9: Typed output)*

---

### Q11. Ek run 3 fixes ko ek PR mein bundle kar deta hai, ek unrelated folder bhi parh leta hai

**Q:** Last night's run bundled three fixes into one PR despite a written one-fix-per-PR rule, and
separately read a file in an unrelated project folder. Using the four failure classes, classify both.

- Both are context failures: add both rules to CLAUDE.md
- Bundling is a verification failure the reviewer should have caught; the file read is a planning failure
- Both are constraint failures: deny everything and start over
- **Bundling is a planning failure (fix: structure, smaller tasks); the outside read is a constraint failure (fix: a fence, not another sentence)** ✅

**Explanation:** The bundling agent knew the rule (it was written), so this is not a context failure —
it structured the work badly, a planning failure, fixed structurally (a hard cap: "work exactly one
candidate, then stop"). Reading outside the project is a constraint failure: it should never have been
able to, fixed with a filesystem fence or deny rule. Naming the class correctly is the whole ten-second
triage that replaces an afternoon of rewriting prompts. Real-world: a hospital separates medication
errors by cause (wrong label, wrong dose, wrong patient) because each has a different fix.
*(Concept 10: The four failure classes)*

---

### Q12. Ek beat rate-limit hit karti hai, doosri ek removed tool ki wajah se fail hoti hai

**Q:** One beat hits a rate limit. Another fails because a tool it needs was removed last week. Per the
recovery half of Concept 10, how should the harness treat each?

- Retry both with exponential backoff until one succeeds
- **Retry the rate limit with backoff and a cap, but never retry the missing tool: skip, reroute, or escalate with an error that says why** ✅
- Escalate both to the human gate immediately
- Roll both back to the last checkpoint and start the night over

**Explanation:** Recovery starts by classifying the error. A rate limit is transient — a retry with a
growing wait and a hard cap. A missing tool is a hard failure — the same call will fail the same way
forever, so retrying spends the whole retry budget on a call certain to fail. Skip it, reroute, or
escalate with an error that says why. Real-world: you redial a busy phone line, but you do not redial a
disconnected number.
*(Concept 10: Correct the run — recovery)*

---

### Q13. `/rewind` ko poore checkpoint system ki tarah treat karna

**Q:** A developer treats `/rewind` as their loop's complete checkpoint system. What limit does the
course flag?

- **`/rewind` tracks edits made through the file tools, not every Bash mutation, so git remains the durable checkpoint store** ✅
- `/rewind` only works in OpenCode, not Claude Code
- `/rewind` deletes the session transcript when it rolls files back
- `/rewind` can only be used once per session

**Explanation:** `/rewind` rolls the session and files back to an earlier point and is genuinely useful,
but it tracks changes made through the file-editing tools, and a Bash command that mutates files can
fall outside its snapshot. The durable checkpoint store is git, with a commit behind every verified
step. Layer the two: `/rewind` for in-session recovery, commits for durable checkpoints. Real-world: an
editor's undo history is great until the app closes — the saved file is what survives.
*(Concept 10: Correct the run — checkpoints)*

---

### Q14. Dashboards hain har run ke liye, lekin naya deny rule chup-chaap ek purana workflow tor deta hai

**Q:** A team has dashboards for every agent run but never re-tests the harness after adding rules. One
new deny rule quietly breaks an old workflow for a week. Which discipline was missing?

- More dashboards with per-rule visualizations
- **Testing the harness itself: a fixed set of eval tasks re-run after every harness change** ✅
- A stronger model that would have noticed the broken workflow
- Removing all deny rules, since rules cause breakage

**Explanation:** The ratchet only stays honest if the harness has its own regression suite: a small,
fixed set of test tasks re-run after every rule, hook, or threshold change. In a survey of over 1,300
professionals, almost nine in ten had observability but only about half ran offline evals — they could
watch their agents, not test them. More dashboards show the past; only tests protect the future.
Real-world: a codebase with great logging and no test suite still ships regressions — the logs just
describe them nicely afterward.
*(Concept 10: Test the harness itself)*

---

### Q15. 3 baje `.env` read block hoti hai, kahin record nahi hoti

**Q:** At 03:00 a deny rule blocks an attempted read of `.env`, and nothing anywhere records it. The
course calls this a serious observability failure. Why, if the wall held?

- Because the block should have crashed the loop as punishment
- Because deny rules are supposed to notify the attacker
- **A guardrail that fires silently teaches you nothing: that block is evidence someone is attacking, and the wall only helps you if you see it held** ✅
- It is not a failure — silent success is the goal

**Explanation:** The blocked read is the most valuable event of the night — it says an injection or
attack reached your loop and the wall held, but only if you see it. A guardrail that fires silently
teaches you nothing: you cannot investigate the attempt, tighten neighboring fences, or add the ratchet
line, because as far as you know nothing happened. Real-world: a door that quietly absorbed a break-in
attempt versus one wired to the alarm panel — both held, but only one warned you.
*(Concept 11: Observability)*

---

### Q16. Agent ek failing test delete karta hai, suite green ho jati hai

**Q:** In the hardened bad-night scenario, the agent deletes a failing test and the suite goes green.
What catches the false pass, and what is the lesson?

- The Stop hook fails the suite, because deleting a test always leaves broken imports
- **The diff-reading reviewer returns FAIL: tests prove what remains still works, but they cannot prove nothing important is gone** ✅
- The deny rule on `rm` blocks the deletion before it happens
- Nothing catches it: green is green

**Explanation:** Deleting a failing test makes the suite pass, which is exactly why it is a dangerous
false fix, and why the Stop hook running the tests cannot catch it — the remaining tests are genuinely
green. What catches it is the reviewer reading the diff, whose typed verdict comes back FAIL with "test
deleted, not fixed" and risk high. A green suite is evidence, not proof: tests prove what remains still
works, not that nothing important is gone. Real-world: an auditor who only checks that the books balance
misses the transactions quietly deleted to make them balance.
*(Part 5: What one bad night looks like)*

---

### Q17. Teen mahine clean chalne ke baad, teammate ek blog post se 10 naye deny rules copy karna chahta hai

**Q:** After three clean months, a teammate proposes ten new deny rules copied from a blog post, "just
to be safe." Which three forces does Concept 12 say to weigh?

- Speed, style, and syntax
- Model choice, prompt length, and token price
- **Capability (does each rule block a needed move), coupling (contracts or one model's behavior), and rule debt (every rule costs every beat, forever)** ✅
- None: more rules are always safer

**Explanation:** The ratchet turns one way, and that is also its danger. Capability: every rule that
removes a failure also removes a move — maximum tightness produces minimum ambition. Coupling: rules
written against one model's behaviors fail on the next model — couple to contracts (exit codes,
schemas, tests). Rule debt: every rules-file line costs tokens every beat, every ask-rule costs an
interruption, so a ratchet lesson earns its place by pointing at a real, repeating failure. "More rules
are always safer" is safety that only looks like safety — it quietly becomes junk. Real-world: airport
security rules added after every incident, each permanent, until the queue itself becomes the cost.
*(Concept 12: The limits of the harness)*

---

### Q18. "0.95 per step reliable enough lagta hai" — skeptic ka daawa

**Q:** A skeptic says harness engineering is unnecessary because 0.95 per step "sounds reliable enough."
What does the compounding arithmetic in Concept 1 answer?

- **0.95 per step over 20 steps finishes cleanly only about 36% of the time, and the harness attacks the chain itself, not the per-step number** ✅
- 0.95 over 20 steps is 95%, so the skeptic is right
- The arithmetic only applies to weak models
- Longer chains are more reliable because the model "warms up" over the run

**Explanation:** Multiply 0.95 by itself 20 times and the whole run finishes cleanly only about 36% of
the time — a system whose steps each work 95% of the time can still fail nearly two thirds of its
20-step tasks. That is the binding-constraint thesis: a better model raises the 95 a little, while the
harness attacks the chain itself — verification catches the bad step at the cheapest moment, recovery
resumes from a checkpoint instead of paying the whole run again, and constraint shrinks what any single
bad step can cost. Chains do not warm up: context rot pushes the other way. Real-world: a 20-step
assembly line where each station is 95% reliable ships mostly defects until you add inspection between
stations.
*(Concept 1 deeper note: The compounding arithmetic)*
