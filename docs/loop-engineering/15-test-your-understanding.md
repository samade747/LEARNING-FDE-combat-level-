# 15 — Test Your Understanding (Exam Assessment)

Book ke live page par yeh section ek interactive `<Flashcards />` widget se shuru hota hai (auto-generated, page ke apne key-terms se) — koi static text nahi, isliye copy karne layak content nahi hai; live version [loop-engineering-crash-course](https://agentfactory.panaversity.org/docs/loop-engineering-crash-course#flashcards) par dekho.

Uske baad **61-question assessment** aata hai (book ke apne `<Quiz>` component se, verbatim) — course ke har concept (1 se 15 tak, dogfooding, dreaming, aur verification-skills interlude sameet) ka scenario-based test, sahi jawab ke sath ek real-world analogy bhi. Yeh poora quiz neeche hai, taake khud test kar sako ya apni class ko exam ki tarah de sako. Content seedha book se hai (English mein — precision zaroori thi, translate nahi kiya).

---

### Q1.

**Q:** A developer says their morning loop now handles all maintenance, so they stopped reading the diffs it opens. They just trust whatever it ships. According to Concept 1, which part of their job did they wrongly hand to the loop?

- Intent that specifies each task precisely
- **Accountability for the code it ships** ✅
- The middle steps the loop automates away
- The heartbeat that fires each run

**Explanation:** The course splits a loop's value into two ends it can never automate: intent and accountability. The loop automates the middle steps. But standing behind the result stays your job. So trusting the output without reading it gives up accountability. Specifying each task precisely is the other end that stays yours, and they did specify the task, so that is not what they gave up. Handing over the middle steps is exactly what loops are for, not a mistake. The heartbeat is loop machinery the system is meant to own. The course warns that a loop running on its own is also a loop making mistakes on its own. Real-world: a finance manager who auto-posts entries without reading them still owns the errors at audit.

*(Concept 1: From prompting to looping (intent + accountability))*

---

### Q2.

**Q:** An engineer schedules an agent to run every morning to clear a backlog. But each morning it does the same first item again and never moves on. Which missing part best explains this, and why?

- The heartbeat: without a schedule it cannot start itself
- The worktree: without isolation its runs overwrite each other
- **The spine: without on-disk state each run forgets yesterday** ✅
- The connector: without MCP it can only suggest, not act

**Explanation:** The loop already fires every morning, so the heartbeat is present. The symptom is that it never builds on yesterday. The model forgets everything between runs. So without on-disk state (the spine), each beat repeats its first step forever: no spine, no loop. A missing schedule would mean it never starts at all, but here it does start daily. Missing isolation only matters when parallel agents overwrite files, which is not the symptom here. A missing connector would stop it acting in real tools, but it would still remember progress. The fix is a progress file that every run reads at the start and updates at the end. Real-world: a night-shift worker with no memory who never reads the handover log redoes the same task every shift.

*(Concept 2: What a loop is made of (the spine))*

---

### Q3.

**Q:** A team wants a scheduled loop that runs even when every laptop is closed, with no servers of their own to maintain, and they accept daily run caps. Which path fits, and why?

- OpenCode with cron: it runs on your own machine
- **Claude Code Routines: they run on Anthropic's servers** ✅
- Claude Code /loop: it keeps running inside the session
- OpenCode run: it exits after a single prompt

**Explanation:** Cloud Routines run on Anthropic's servers even with every laptop closed and nothing installed locally, and they accept the daily run caps the team is fine with. That is an exact match. Running OpenCode from cron needs a machine of yours powered on, which the team wants to avoid. A single opencode run exits after one prompt. It is one beat, not a scheduled loop that survives closed laptops. The in-session /loop lives inside an open session and stops the moment the terminal closes, so it cannot run unattended. This is the two-approach difference: Claude Code includes the cloud scheduler, while OpenCode provides the worker and requires you to add the trigger. A familiar comparison is choosing managed cloud scheduling instead of maintaining your own scheduler.

*(Concept 3: Two ways to build a loop (built-in parts vs self-connected parts))*

---

### Q4.

**Q:** A developer runs opencode run "summarize today's commits" once. It prints a summary and exits, and they call this "a loop." Why does the course see it differently?

- It is the whole loop: the schedule itself already lives inside opencode
- It is a maker-checker: a separate reviewer already graded the output
- **It is one beat: a heartbeat is needed to repeat it** ✅
- It is the spine: the printed summary becomes the memory

**Explanation:** The course calls opencode run, which runs one prompt and exits, exactly one beat of a loop. It becomes a loop only when you wrap it in something that fires on a timer (cron, launchd, GitHub Actions). So a single manual run lacks the heartbeat that makes a loop a loop. It is not the whole loop with a built-in schedule. OpenCode is the worker, and you supply the heartbeat from the OS or CI. No reviewer graded anything, so calling it a maker-checker is wrong. That split needs a second agent. The printed summary is not the spine either. The spine is on-disk state a future run reads, not terminal output that scrolls away. Real-world: running a backup script by hand once is not the same as a scheduled nightly backup.

*(Concept 3: Two ways to build a loop (OpenCode provides the worker))*

---

### Q5.

**Q:** To save tokens, an engineer has the same agent write a fix and then say whether that fix is good. According to "what a loop is made of," which rule does this break?

- **The agent that writes work must not grade it** ✅
- The skill must provide saved project knowledge to each run
- The connector must act in real tools, not suggest
- The heartbeat must fire the loop on a schedule

**Explanation:** "What a loop is made of" names subagents as the maker-checker split: the agent that writes the code is not the agent that grades it, because a model that checks its own output almost always approves it. Having one agent both write and approve breaks that split. The connector acting in real tools is about whether the loop can open a PR, not who judges the fix. The skill holding knowledge prevents each run from rebuilding project context, which is an efficiency point unrelated to grading. The heartbeat firing on a schedule starts the loop but says nothing about self-review. Skipping the separate checker is what makes an unattended loop hard to trust. Real-world: the person who writes a check should not also be the one who approves it. That is the classic separation of duties.

*(Concept 2: What a loop is made of (maker-checker subagents))*

---

### Q6.

**Q:** Two teammates describe their role after moving to loops. Which description matches what Concept 1 says a person is still paid for?

- Starting every turn and reading each reply
- Watching each step the loop runs in real time
- Writing the longest, most detailed prompt possible
- **Specifying intent precisely and owning what ships** ✅

**Explanation:** The course says you are paid for intent and judgment: saying precisely what you want, and standing behind what ships. These are the two ends a loop cannot automate. Starting every turn and reading each reply is the old prompting shape, the middle the loop now automates, not what you are still paid for. Writing the longest possible prompt misreads the shift: the course says the difference is not a bigger prompt, so value moved to the loop's design, not prompt length. Watching each step in real time goes against the unattended model, where your attention is only at the gate. Real-world: a film director sets the vision and approves the final cut, rather than operating every camera.

*(Concept 1: From prompting to looping (what you are paid for))*

---

### Q7.

**Q:** A loop starts three agents at once, and they keep overwriting each other's edits to the same files. Which part of the loop's anatomy was skipped?

- **The worktree, which isolates each agent's checkout** ✅
- The connector, which lets each agent open a PR
- The skill, which tells each agent the project habits
- The spine, which records what each agent finished

**Explanation:** The symptom is parallel agents overwriting each other's edits to the same files. That is exactly what a worktree prevents: a separate working folder on its own branch, so one agent's edits cannot touch another's checkout. The spine records what each run finished, which is memory between runs, not collision protection during a run. A connector lets agents act in outside tools like opening a PR, which is unrelated to file isolation. A skill carries project habits so runs start warm, but shared knowledge does nothing to keep two agents from writing the same file at the same time. Isolation is what makes running more than one agent at once safe. Real-world: two builders given separate copies of the blueprint and separate rooms, instead of both writing on the one shared sheet.

*(Concept 2: What a loop is made of (worktree isolation))*

---

### Q8.

**Q:** A manager argues that moving to loops means less work, because you "set it and forget it": build it once and never look again. How does the course correct this?

- Loops are easier than prompting once the schedule is running
- **Loops are harder than prompting: the reward is leverage** ✅
- Loops remove the need to check what ships overnight
- Loops shift all judgment onto the checker subagent

**Explanation:** The course is direct: a loop is not magic and not set it and forget it. Building one you can trust unattended is harder than prompting, not easier, and the payoff is leverage, since one good loop does the work again and again. Calling loops easier gets this backwards. Claiming loops remove the need to check what ships goes against a core warning: a loop running on its own is also a loop making mistakes on its own, so checking the work stays your job. Shifting all judgment onto the checker subagent overstates it. The checker makes "done" mean something, but a human still owns intent and accountability. Real-world: automating a factory line raises output but demands more engineering up front and ongoing inspection, not less.

*(Concept 1: From prompting to looping (harder, not easier))*

---

### Q9.

**Q:** A newsletter tells a reader that "loop engineering" means making the agent's inner while-loop stronger, meaning the cycle that sends context to the model, runs its tool calls, adds the results, and repeats until the model stops asking. How does this course relate that inner loop to the loop it teaches?

- The two are the same loop: the inner cycle already contains a heartbeat and a spine
- **The inner loop is machinery inside one beat: this course teaches the outer loop around it** ✅
- The inner loop replaces the outer one once dynamic workflows are enabled
- The inner loop only exists in OpenCode, while Claude Code runs the outer loop

**Explanation:** The course's note says both usages are real but sit at different layers. The inner while-cycle inside every agent runtime is real engineering, but it is the machinery inside one beat. This course is about the outer loop around it: what the agent works on, when it fires, and what happens to the result. Saying the two are the same misses that the inner cycle has no heartbeat and no spine of its own. It ends when the turn ends and remembers nothing after. Dynamic workflows codify the body of a beat. They do not merge the inner loop into the outer one. And the inner loop exists in every agent runtime, both tools included. It is not an OpenCode-only feature. Knowing which loop a claim is about keeps you from applying advice at the wrong layer. Real-world: an engine's combustion cycle versus the delivery route the truck drives. Both are loops, at very different sizes.

*(Concept 1 note: Two loops share one name)*

---

### Q10.

**Q:** A student finished the whole Spec-Driven course in the claude.ai chat box and wants to run a real unattended loop right there. What does the course say, and why?

- The chat box can, because Routines live inside chat
- The chat box can, since it re-prompts itself each turn
- **The chat box can't: in chat you are the schedule** ✅
- The chat box can't, because it has no skills or MCP

**Explanation:** The plain claude.ai chat box always waits for you and cannot fire on a schedule or event. So in chat, you are the schedule, and it cannot run a true unattended loop. Saying Routines live inside the chat box is wrong: Routines are a Claude Code feature reachable through the same login, and they run on Anthropic's servers, not inside the chat conversation. Claiming the chat re-prompts itself is backwards. It waits every turn, and when you re-prompt by hand you become the heartbeat the loop is meant to remove. The "no skills or MCP" answer reaches the right verdict for the wrong reason, since the real blocker is the missing schedule. Real-world: a chat window is a person waiting for your next message, not an alarm clock.

*(Framing: where loops can run (claude.ai chat box))*

---

### Q11.

**Q:** A reader memorizes every Claude Code loop command but never grasps why a loop needs a heartbeat, working parts, and a spine. When the CLI changes next month, what does the course predict?

- Their skills transfer cleanly to OpenCode's different commands
- They learned loop engineering and can ignore the docs
- **They learned this month's CLI, not loop engineering** ✅
- They will still design safe loops without reading updates

**Explanation:** The course's line is exact: memorize the keystrokes and miss the shape, and you learned this month's CLI, not loop engineering. The lasting layer is the loop's shape (the heartbeat, working parts, and spine), plus the maker-checker split and the two ends. The mechanical layer of flags, paths, and commands ages every week. So a reader who learned only commands keeps nothing that transfers. Claiming they learned loop engineering gets the result backwards, and the course never says to ignore the docs, since where course and docs disagree, the docs are right. Their skills cannot transfer cleanly to OpenCode, because only the shared shape transfers, and shape is exactly what they skipped. Designing safe loops without updates fails twice over. Real-world: memorizing one GPS's buttons does not help you drive a different car.

*(Concept 3 / Framing: durable shape vs mechanical CLI)*

---

### Q12.

**Q:** A developer runs `/loop 5m check the deploy` in Claude Code, then closes the laptop and goes home, expecting it to keep checking overnight. The next morning nothing has run. Why did the loop never fire while they were away?

- `/loop` silently failed because the deploy had finished hours earlier
- `/loop` hit its built-in nightly token ceiling and paused itself
- `/loop` needs a GitHub webhook trigger to keep firing through the night
- **`/loop` runs inside the session, so closing the terminal stops it** ✅

**Explanation:** `/loop` is tied to the open session on purpose: close the terminal or let the laptop sleep, and the timer stops. The course calls this a safety feature, not a bug, because a casual in-session loop should not outlive its session. Overnight work needs a scheduled task or cloud Routine. Claiming it paused on a 'nightly token ceiling' invents a limit `/loop` does not have. Needing a 'GitHub webhook trigger' confuses an in-session timer with event-driven Channels and Routines, a different heartbeat entirely. Blaming a 'silent failure because the deploy finished' misreads the symptom: the loop never ran because the session was gone, not because the task completed. Real teams learn this when a laptop lid closes and the 'overnight' watcher quietly never fired.

*(Concept 4: In-session loops)*

---

### Q13.

**Q:** An OpenCode in-session loop wraps `opencode run` in a `while` loop with `sleep 300`, but each beat feels slow and costly. The course suggests running `opencode serve --port 4096 &` once and then using `--attach` on each beat. What does that actually fix?

- It lets the loop keep running after the terminal is closed
- It replaces the shell `sleep` with a more accurate timer
- It adds a separate checker model to grade each beat's output
- **It avoids paying the MCP server start-up cost on every beat** ✅

**Explanation:** Each `opencode run` normally starts the whole runtime from scratch (config, model, plugins, and any MCP servers), and that start-up cost is paid on every beat. Starting `opencode serve` once and `--attach`-ing keeps that runtime warm, so each beat skips it. That is the course's exact reason. Thinking it keeps the loop alive after the terminal closes is wrong: the shell loop, like `/loop`, still dies with the session, and staying alive needs cron or a Routine. A 'more accurate timer' misses the point, since `sleep 300` is already the timer and accuracy is not the problem. Adding 'a separate checker model' describes the maker-checker split from run-until-done, not what `serve`/`--attach` does. This is like a database connection pool that stays open so you do not reconnect on every query.

*(Concept 4: In-session loops)*

---

### Q14.

**Q:** A developer runs `/goal The auth code is good and well-structured.` and is surprised the loop never reliably stops on its own. What is the core problem with this stopping condition?

- It lacks a ceiling, so the loop retries until it runs forever
- The condition needs a GitHub webhook before `/goal` can evaluate it
- **A command cannot prove it, so the checker has nothing to verify** ✅
- A smaller checker model is too weak to judge code quality fairly

**Explanation:** `/goal` stops only when a separate checker can confirm the condition by reading what Claude has printed into the conversation. 'The auth code is good' is a judgment no command can prove, so nothing objective ever lands in the transcript for the checker to confirm, and 'done' never resolves. The course says write conditions a command can prove, like tests passing and lint clean. The missing-ceiling answer names a real safety gap, but a ceiling only caps wasted tries, so even with one, this loop would hit the cap rather than succeed. That leaves the unprovable condition as the root cause. 'Needs a GitHub webhook' confuses run-until-done with event triggering. Calling the smaller checker 'too weak to judge quality' misreads its job: it reads the command results Claude already ran. It is not asked for an opinion on style. This is why good acceptance criteria are testable, not just hopes.

*(Concept 5: Conditional loop (run-until-done))*

---

### Q15.

**Q:** In an OpenCode run-until-done loop, the agent does the work and then `npm test && npm run lint` decides whether to stop. Why does the course call the test runner and linter the most honest checker there is?

- **A command cannot convince itself the work is actually fine** ✅
- A command is cheaper than spending tokens on another model
- A command always agrees with whatever the maker just claimed
- A command runs faster than a second review agent would

**Explanation:** The course names the test runner and linter the most honest checker, because a command cannot convince itself the work is fine. Unlike a model, it has no reason to go easy on its own output. Saying it 'runs faster' or is 'cheaper than another model' both name real side benefits, but neither is the honesty point, since a fast or cheap check could still be a pushover. 'Always agrees with the maker' is the opposite of honest. It describes a model grading its own work, the exact failure maker-checker exists to prevent. The point is that a command cannot be talked into a lie: a passing test suite is evidence, not an opinion. This is why CI gates trust automated tests over a developer's 'looks good to me' before a merge.

*(Concept 5: Conditional loop (run-until-done))*

---

### Q16.

**Q:** A loop has a clear success condition ("all integration tests pass") but the tests can never pass, because a required external service is missing. No limit is set. What does the course say happens next?

- **It keeps retrying and can drain your whole token budget** ✅
- It stops after the default three tries and warns you
- It escalates to a human reviewer after the first failed attempt
- It switches to a cheaper model and quietly keeps going

**Explanation:** With a success condition the loop can never meet and no limit, it retries forever, and the course warns this spends your whole token budget chasing a goal it cannot reach. Stopping 'after the default three tries' invents a built-in cap that does not exist. The whole lesson is that you must add the limit yourself. Escalating 'after the first failed attempt' describes a deliberate human-gate design, not the default of an uncapped run-until-done loop. Switching 'to a cheaper model' is a cost lever from a different concept and would not stop the runaway. It would just make each wasted beat cheaper while still never ending. This is the real-world runaway loop that shows up as a surprise four-figure cloud bill the next morning.

*(Concept 5: Conditional loop (run-until-done))*

---

### Q17.

**Q:** A capped run-until-done loop uses all eight of its tries calling the same tool with the same arguments, repeating one mistake until the limit finally stops it. Which brake was missing, per the course's three stops?

- A tighter success condition that a command can prove
- A higher ceiling, so the loop had more room to recover
- **No-progress detection, which stops a loop repeating the same action** ✅
- A cloud Routine, which never repeats a failed beat

**Explanation:** The course names three stops, always: a success condition, a limit, and a no-progress check. If the agent repeats the same action with the same arguments, it is stuck, and another retry will not fix it. Here the limit worked, but every try was wasted repeating one mistake, which is exactly what a stuck-check ends early. A tighter success condition changes what 'done' means but does nothing about a loop repeating the same failing action on the way there. A higher ceiling makes the waste bigger, not smaller: more identical retries, more tokens. And a cloud Routine is a heartbeat. It schedules beats, it does not check them for repetition. The lesson: a limit caps the damage, a stuck-check stops it early. Real-world: a robot vacuum bumping the same chair leg until its battery dies, instead of noticing and going around.

*(Concept 5: Conditional loop (run-until-done) (three stops))*

---

### Q18.

**Q:** A `/goal` run works for dozens of turns. Its context fills with old tool output and dead ends, and its decisions get visibly worse, with each bad turn adding more junk. What is happening, and what is the defense?

- **A doom loop from context rot: compact, offload to files, use subagents** ✅
- The spine is corrupted: delete progress.md and restart the run
- The heartbeat is firing too often: slow the schedule to hourly
- The checker model is too weak: upgrade it to a stronger model

**Explanation:** The course's note on long runs names this the doom loop. A run-until-done loop that works for many turns fills its own context with junk, and model quality drops as the pile grows. Each worse decision adds more noise, which makes the next decision worse. The defenses are the context habits from the agentic coding course: compact long runs, move big outputs to files, and hand messy subtasks to a subagent so only the clean result comes back. Deleting progress.md attacks the spine, which is memory between runs, not the context inside this one run. Slowing the heartbeat changes how often beats fire, not what happens within one long beat. Upgrading the checker judges the output but does nothing about the rotting context the maker is reasoning over. Treat context as a budget, not a bucket. Real-world: a meeting in its third hour makes worse decisions than the same people made in the first thirty minutes.

*(Concept 5 note: Long runs get worse over time)*

---

### Q19.

**Q:** You want a maintenance task to run every weekday at 9am, even when your laptop is closed and nothing is installed on it. Which Claude Code option fits?

- A `claude -p` line in your local machine's crontab
- An in-session `/loop` left open overnight
- A Channel that pushes Telegram messages into a session
- **A cloud Routine, which runs on Anthropic's servers on a schedule** ✅

**Explanation:** A cloud Routine runs on Anthropic's servers on a schedule, with nothing installed locally. So it fires at 9am even with the laptop closed. That is the exact requirement. A `claude -p` line in crontab is a fine scheduled one-shot, but it runs on your machine, so a closed laptop means it never fires. An in-session `/loop` needs the terminal and session to stay alive, which is the opposite of unattended. A Channel pushing Telegram messages is event-driven input into a running session, not a scheduled, laptop-off task. The deciding factor is where the work runs: only the managed cloud option does not depend on your hardware. This is why teams move nightly jobs off a developer's laptop and onto a hosted scheduler nobody has to keep awake.

*(Concept 6: Unattended schedules)*

---

### Q20.

**Q:** Your cloud Routine runs fine, but it can only push to branches whose names start with `claude/`, which blocks a push to `release/`. Why?

- A bug that a re-run usually clears up
- **A deliberate guardrail you can lift per repo with a setting** ✅
- The GitHub connector lacks `pull-requests: write`
- The daily run cap was reached, freezing other branches

**Explanation:** By default a Routine may push only to branches beginning with `claude/`. The course calls this a deliberate guardrail, which you can lift per repository with the 'Allow unrestricted branch pushes' setting. Calling it 'a bug a re-run clears up' treats an intentional rule as a glitch. The daily run cap is real, but it limits how many times a Routine runs, not which branches it may push to, so it cannot explain a branch-name block. Missing `pull-requests: write` permission would stop it opening PRs, not restrict branch names. The guardrail exists so an unattended agent cannot push changes onto protected branches while you sleep. It mirrors how CI bots are scoped to their own branch prefixes so a runaway automation cannot touch `main` directly.

*(Concept 6: Unattended schedules)*

---

### Q21.

**Q:** A team turns an `opencode` PR-comment workflow into a scheduled GitHub Actions job. The schedule fires correctly, but nothing useful happens each morning. What did they most likely forget?

- **A scheduled run has no comment, so the `prompt` is required** ✅
- The `schedule` cron must be in local time, not UTC
- They forgot to grant `contents: write`
- A second checker agent must approve before the schedule fires

**Explanation:** On a schedule there is no PR or comment to read an instruction from. So the course says the `prompt` is required for scheduled events. Leave it out, and the run has nothing to do. The 'cron must use local time' answer is wrong: GitHub Actions cron is UTC, and mistiming would only change when it fires, not make a firing do nothing. Needing `contents: write` is a real requirement for opening branches or PRs, but missing it causes a permission error, not silent no-ops, so it does not match these symptoms. A 'second checker agent approving before the schedule fires' invents gating that is not how scheduling works. The lesson: a comment-driven workflow leans on the comment for intent, and a schedule has none. Teams hit this exact gap converting a PR-review bot into a nightly job.

*(Concept 6: Unattended schedules)*

---

### Q22.

**Q:** You want a loop to react the instant a Telegram message arrives, pushing it straight into a running Claude Code session instead of waiting on a clock. Which feature is built for that?

- A cloud Routine polling every five minutes
- **Channels, which push chat events into a running session** ✅
- The `/goal` run-until-done command with a checker
- An `opencode run` line wrapped in a cron job

**Explanation:** Channels are built to push chat events from sources like Telegram, Discord, and iMessage straight into a running session. The course's picture for them is the doorbell: nothing happens until the message arrives, then the session reacts at once. A cloud Routine on a polling schedule reacts on a clock, not the instant a message lands, so it adds delay and misses the 'instant' requirement. The `/goal` run-until-done command is about stopping when a checked condition is met, not reacting to outside messages. An `opencode run` wrapped in cron is again schedule-driven, and it lives on the OpenCode approach, not Claude Code chat events. The split is schedule ('check every hour') versus event ('react the moment X happens'). This is the same split as a cron job versus a webhook in ordinary backend systems.

*(Concept 7: Event-driven)*

---

### Q23.

**Q:** After running `opencode github install`, a team opens a pull request and the generated workflow runs, but they gave it no `prompt`. What does OpenCode do by default?

- It silently exits, because a prompt is always required
- It opens a fresh issue summarizing the new PR
- It waits for a `/oc` or `/opencode` comment first
- **It reviews the pull request by default, no prompt needed** ✅

**Explanation:** The course states that for a `pull_request` event with no prompt, OpenCode reviews the PR by default. So the installed workflow simply runs a review. 'Silently exits because a prompt is required' is true only for scheduled events, which have no comment or PR to act on. A PR event supplies its own default behavior. 'Waiting for a `/oc` comment' confuses one trigger type with another, since comment triggers are separate from the automatic PR-opened trigger. 'Opening a fresh issue' invents an action the default never takes. It reviews the existing PR instead of filing new work. The takeaway: event context can stand in for an explicit prompt. This is like many CI bots that run a sensible default action on PR-open without anyone telling them exactly what to do.

*(Concept 7: Event-driven)*

---

### Q24.

**Q:** A loop starts three agents at once to fix three bugs in the same repo, and one agent's changes keep vanishing or getting tangled with another's. What is the cause, and the fix the course gives?

- They lack a connector: add an MCP server so each agent can open its PR.
- They share one model: give each agent a stronger model to avoid collisions.
- They never read progress.md: have each agent read the spine before it starts.
- **They share one working folder: give each agent its own git worktree.** ✅

**Explanation:** The collision happens because all three agents write into the same working folder, so their edits overwrite one another. A git worktree gives each agent a separate folder on its own branch that still shares repo history, keeping the edits apart. Handing each agent a stronger model misreads the problem: model quality has nothing to do with two processes writing the same files at once. Having each read the progress file addresses memory between runs (the spine), not shared file access. Adding an MCP connector lets the loop act in outside tools like GitHub, which does nothing to stop concurrent checkouts from overwriting each other. This is the same reason human teammates each branch instead of all committing to one shared working copy.

*(Concept 8: Isolation via worktrees)*

---

### Q25.

**Q:** In Claude Code, you want each helper subagent inside a scheduled run to get a fresh checkout that cleans itself up afterward, so parallel fixes never collide. Which setting does that?

- Pass `--worktree`, which isolates the whole session, not each helper
- **Set `isolation: worktree` on the subagent for a self-cleaning checkout** ✅
- Run `git worktree add` by hand for each helper
- Declare the worktree inside the `mcp` section of your config

**Explanation:** The scenario asks for a per-helper, self-cleaning checkout inside a scheduled run. That is exactly what setting `isolation: worktree` on a subagent does in Claude Code. Passing `--worktree` isolates the whole session in its own checkout, rather than giving each helper subagent its own, so it solves a different level of the problem. Running `git worktree add` by hand is the OpenCode approach. In Claude Code the feature is built in, so reaching for raw git ignores the tool you are using. The `mcp` section is where you declare connectors the loop reaches, not where isolation is configured, so it cannot create a worktree at all. This mirrors CI systems that spin up a fresh, disposable workspace per job and tear it down afterward.

*(Concept 8: Isolation via worktrees)*

---

### Q26.

**Q:** Your scheduled triage loop works out your project's conventions and triage steps from scratch on every beat, wasting tokens and inviting mistakes. What is the right fix?

- Add an MCP connector so the loop can fetch the conventions live.
- Paste the full list of conventions into the prompt on every run.
- Record the conventions in `progress.md` and rewrite them each run.
- **Write that knowledge once into a `SKILL.md` file the agent reads each run.** ✅

**Explanation:** A loop starts as a fresh session on every beat, so working out conventions and triage steps each time wastes tokens and invites mistakes. The fix is to write that knowledge once into a `SKILL.md` the agent loads on every run. Pasting the full convention list into the scheduled prompt is the long, hard-to-maintain instruction block the course warns against: it bloats the prompt you pay for each beat, and nobody keeps it updated. Recording conventions in `progress.md` confuses stable project knowledge with run-to-run state. The spine tracks what was tried and what is open, not durable habits. Adding an MCP connector lets the loop act in outside tools, which has nothing to do with carrying knowledge into fresh sessions. It is the same logic as onboarding docs a new hire reads, instead of being re-briefed daily.

*(Concept 9: Knowledge via skills)*

---

### Q27.

**Q:** A teammate keeps a sixty-line scheduled prompt full of triage steps that nobody keeps updated. Using the course's reasoning about skills, how should the prompt and the steps be split?

- **The prompt becomes one line, 'run the daily-triage skill', and the skill holds the steps.** ✅
- The steps move into `progress.md`, and the prompt reads them at the start.
- The steps move into `CLAUDE.md`, so they load on every session.
- The prompt keeps every step, and you skip the skill to stay simpler.

**Explanation:** The course's point is that a skill keeps the loop prompt tiny. The scheduled prompt shrinks to one line that says run the daily-triage skill, and the skill file holds the detailed steps. So the logic stays easy to update and cheap per beat. Keeping every step in the prompt is exactly the long, unmaintained instruction block the tip argues against. Moving the steps into `progress.md` misuses the spine, which records run-to-run state, not reusable procedure. Putting them in `CLAUDE.md` is tempting, but the rules file is for short, steady habits read on every run, and it should stay lean. Detailed triage steps belong in a skill that loads only when the task matches. This is like a runbook the on-call engineer calls up by name, rather than reciting from memory.

*(Concept 9: Knowledge via skills)*

---

### Q28.

**Q:** Your loop reads CI logs and drafts genuinely good fixes, then writes a summary saying 'here is the fix', but nothing ever lands in GitHub. What is the loop missing?

- A worktree on its own branch, so parallel edits stop overwriting each other.
- A progress file on disk, so it remembers which fixes it drafted.
- A stronger checker model, so the reviewer stops failing the fix.
- **A connector built on MCP, so the loop can open the PR, not just describe it.** ✅

**Explanation:** A loop that only reads files can only talk. The missing piece is a connector built on MCP, which lets the loop act, opening the PR instead of just describing the fix. A worktree solves isolation between parallel agents editing files, not the inability to reach GitHub. A stronger checker concerns the maker-checker verdict on quality, but here the fix is already good, and nothing is being graded badly. A progress file is the spine that remembers across runs, which still would not push anything to GitHub. The course frames this as the difference between a loop that says here is the fix and one that opens the PR, links the ticket, and posts to the channel once CI is green. It is the gap between an assistant that drafts an email and one allowed to send it.

*(Concept 10: Action via connectors)*

---

### Q29.

**Q:** A developer who set up a GitHub connector in Claude Code assumes the same config will drop straight into OpenCode, because both speak MCP. Where does the course say this breaks?

- Nowhere: an MCP config file is identical across both tools.
- **The protocol carries over, but packaging and auth often need tool-specific configuration.** ✅
- MCP is a Claude Code feature, so OpenCode cannot use connectors at all.
- Only the model ID differs: the connector setup is otherwise identical.

**Explanation:** Both tools speak MCP, so the protocol itself carries over. But packaging and authentication (local vs hosted, OAuth, permissions) often need tool-specific configuration, and that is where the copy-paste assumption breaks. Claiming MCP is Claude Code only is false: the course stresses that OpenCode declares servers in `opencode.json` and speaks the same protocol. Expecting an exactly identical config ignores that Claude Code lists connectors in a routine, while OpenCode uses an `mcp` section with subprocess or HTTPS-plus-OAuth handling. Saying only the model ID differs makes light of the auth and packaging work that actually varies between the tools. This is like two apps both speaking OAuth yet still needing their own client setup, redirect URLs, and secrets before either can sign you in.

*(Concept 10: Action via connectors)*

---

### Q30.

**Q:** Your scheduled `opencode run` uses MCP connectors, and every beat pays a slow MCP server start-up cost. What does the course recommend?

- Move the connectors into `.claude/agents/`, so they load faster.
- Run every beat with `claude -p`, so the server never starts.
- **Start `opencode serve` once, then `--attach` to it on each beat.** ✅
- Add the servers to a cloud routine's connector list instead.

**Explanation:** In a scheduled `opencode run` that uses MCP connectors, the course says to start `opencode serve` once and `--attach` to it each beat. That way you stop paying the MCP server start-up cost on every firing. Moving connectors into `.claude/agents/` is a Claude Code path, and that folder is where subagents live, not connectors, so it would not help an OpenCode run. Switching beats to `claude -p` abandons OpenCode for Claude Code entirely, and still would not address the server start-up cost. Adding the servers to a cloud routine's connector list is again the Claude Code mechanism, not the OpenCode worker pattern. This is like keeping a database connection pool warm instead of opening a fresh connection on every request.

*(Concept 10: Action via connectors)*

---

### Q31.

**Q:** An unattended loop retries a failed beat, and its 'create customer' tool runs a second time, leaving two duplicate records. What property was the tool missing, and why does it matter in a loop?

- **Idempotency: writes must be safe to repeat, because a loop retries** ✅
- Read-only mode: a loop's tools should never write to real systems
- A stronger model: a smarter maker would not have retried
- OAuth: an authenticated tool cannot create the same record twice

**Explanation:** Among the properties the course says a connector needs because it is in a loop, the key one here is that writes must be safe to repeat. A loop that retries a failed step calls the same write again, so a blind 'create' becomes duplicate records and double billing, while an update-or-create is harmless to rerun. Making every tool read-only throws away the whole point of connectors: a loop that cannot act can only talk. A stronger model does not remove retries. Retrying is the loop working as designed, which is exactly why the write must tolerate repetition. OAuth authenticates who is calling, and an authenticated caller can create duplicates just as easily. By hand you absorb this by skipping the duplicate. Unattended, nobody is there to absorb it. Real-world: payment APIs use idempotency keys so a retried charge never bills the customer twice.

*(Concept 10: Action via connectors (idempotent writes))*

---

### Q32.

**Q:** A loop's single agent writes a fix, says 'done, tests pass', and the loop commits it overnight. By morning the fix is broken. What flaw does the course name, and the remedy?

- **The writer graded its own work: a separate checker agent must approve it.** ✅
- The loop lacked a heartbeat: add a schedule so it runs each morning.
- The worktree was missing: isolate each fix so edits cannot collide.
- The skill was missing: write the steps down so it stops guessing.

**Explanation:** The flaw is that the same agent wrote the fix and then graded it. A model that checks its own output almost always approves it. So the remedy is a separate checker agent that must approve the work before it lands. Blaming a missing heartbeat is wrong: the loop already fired on schedule, so scheduling is not the gap. Blaming a missing worktree confuses isolation between parallel edits with the trust problem of self-grading. One checkout can still ship a wrong fix. Blaming a missing skill addresses where knowledge lives, not who certifies the result. The course calls maker-checker the single most important choice, and the only reason you can leave a loop alone. It is like requiring a second set of eyes to approve a pull request, rather than letting the author merge their own.

*(Concept 11: Maker-checker subagents)*

---

### Q33.

**Q:** You are configuring a maker-checker split in OpenCode. Which setup of the checker agent matches the course's advice?

- Skip the second agent and let the maker mark its own work done.
- Give the checker the same strong model as the maker, with full edit rights.
- Run one agent twice and treat its second pass as the checker.
- **Give the checker its own cheaper, read-only model, and have the maker call it.** ✅

**Explanation:** In OpenCode the recommended split gives the checker its own, often cheaper, read-only model, with the maker calling it through an `@` mention or the Task tool. So a fresh perspective grades the diff without being able to edit it. Giving the checker the same strong model plus full edit rights wastes tokens and lets the reviewer change the very code it should only judge. Running one agent twice and treating the second pass as the checker is still self-grading, which the course says is far too easy. Skipping the checker entirely removes the only safeguard that lets you leave a loop running unattended. A common split is a strong model that implements and a focused, cheaper one that checks. This echoes finance, where whoever books a payment is never the one who approves it.

*(Concept 11: Maker-checker subagents)*

---

### Q34.

**Q:** A teammate insists their Claude Code dynamic workflow 'is a complete loop' because it fans twelve subagents out and grades their work. Why does the course say it is NOT a loop, and what would make it one?

- It uses too many subagents: capping them under sixteen makes it a loop.
- **It runs once with no heartbeat or spine: add a Routine and a progress file.** ✅
- It runs in the cloud, not locally: moving it onto cron makes it a loop.
- It lacks a read-only checker: adding one reviewer makes it a loop.

**Explanation:** A dynamic workflow runs once and forgets everything when it ends. With no heartbeat to fire it again and no spine to remember, it is the body of a single beat, not a loop. Adding a Routine for the heartbeat and a progress file for the spine is what turns it into a loop. The agent cap of about sixteen at once is a runaway guardrail, not what makes something a loop, so capping agents changes nothing about loop-ness. The workflow in the scenario already grades its subagents, so a missing checker is not the issue. Where it runs, cloud or local, is just the heartbeat's location and does not add memory between firings. This is like a single nightly batch job versus the cron entry plus state file that together make a recurring, stateful pipeline.

*(Interlude: Dynamic workflows)*

---

### Q35.

**Q:** A colleague builds a dynamic workflow that fans work out to subagents, runs it once, and calls it "my overnight loop." Why is that label wrong?

- A workflow can only spawn one subagent, so it never runs work in parallel
- A workflow runs continuously in the background, making it an unsafe loop
- **A workflow runs once and forgets everything, with no heartbeat and no spine** ✅
- A workflow cannot contain a maker-checker split, which a real loop needs

**Explanation:** The course's warning is clear: a dynamic workflow runs once, forgets everything when it ends, and has no heartbeat and no spine. So it is the body of one beat, not a loop. The claim that it spawns only one subagent is false. The whole point is fanning work out to many agents (capped near 16 at once, 1000 per run). The 'runs continuously in the background' idea is wrong, because it ends when the run finishes and does not keep firing on its own. And it cannot lack a maker-checker split, because a workflow IS the maker-checker and worktree splits packaged together. The missing pieces are the heartbeat and the spine. It is like a single dishwasher cycle versus the nightly timer that fires it, plus the log of what is clean.

*(Interlude: Dynamic workflows)*

---

### Q36.

**Q:** A dynamic workflow performs one run and then stops. What two things must you add to turn it into a real loop?

- A stronger maker model and a second checker to grade its output
- **A heartbeat that starts each beat and a progress file that survives between runs** ✅
- More subagents and a higher agent cap, so the run keeps going longer
- An isolated worktree per candidate and a read-only reviewer with a verdict

**Explanation:** A workflow performs the body of one beat. To make it a loop, add a heartbeat (such as a Routine, `/loop`, or cron) to start later beats, and add a progress file that stores state between runs. A stronger maker and a second checker improve the work inside one beat, but they do not create a schedule or persistent memory. More subagents also increase scale without adding repetition or state. Worktree isolation and a read-only reviewer are already parts of the body, not the missing loop components.

*(Interlude: Dynamic workflows)*

---

### Q37.

**Q:** You start a long dynamic workflow run, it gets interrupted, and the next day you open a fresh Claude Code session expecting to pick up where it stopped. What actually happens?

- It resumes from a saved checkpoint, because the runtime saves progress to disk
- It refuses to start, because an interrupted run locks until you clear it
- It resumes automatically, because the /workflows view restores the last run
- **It starts over, because a run's memory lives only within that one run** ✅

**Explanation:** The course states that a workflow run's memory lives only within that run: you can resume it inside the same session, but a fresh session starts it over. So expecting next-day continuation is the trap. The 'saved checkpoint on disk' answer describes the spine (a progress file the agents write), which is exactly what a bare workflow lacks. The runtime does not save run memory for you. The '/workflows view restores the last run' answer is wrong, because that view lets you save a successful script as a reusable command, not reload an interrupted run's memory. And nothing locks an interrupted run. There is no such guard. This is why a workflow needs a heartbeat and a progress file around it. Like a browser tab with no saved draft, closing it loses the work.

*(Interlude: Dynamic workflows)*

---

### Q38.

**Q:** A developer who works only in OpenCode asks where the /workflows command is, so she can codify a fan-out orchestration. What is the honest answer?

- Run the bundled /deep-research, OpenCode's built-in saved-workflow command
- Use the opencode workflow save command to capture that run as a rerunnable command
- **There is none: the capped for loop and &/wait fan-out you write is the workflow** ✅
- Trigger it with the ultracode keyword, which OpenCode shares with Claude Code

**Explanation:** OpenCode has no /workflows command. The course says the script you already write IS the workflow: the capped `for` loop from Concept 5 plus the `&`/`wait` fan-out from Concept 8. Your shell holds the plan, `opencode run` is each agent, and exit codes are the checker. The '/deep-research' answer is a Claude Code bundled workflow, not an OpenCode equivalent. There is no 'opencode workflow save' command. Saving a script as a reusable `/command` is the Claude Code /workflows feature. And the 'ultracode' keyword is a Claude Code trigger for dynamic workflows, not shared with OpenCode. The tradeoff is real: full control and no agent cap, at the price of writing and maintaining the orchestration yourself. Like building your own production line instead of buying one that is ready to use.

*(Interlude: Dynamic workflows)*

---

### Q39.

**Q:** A team logs each run's progress as messages in the ongoing agent conversation, then cannot understand why run #5 redoes work run #1 already finished. What is the root cause?

- The conversation grew too long, so the model dropped the earliest messages
- The runs fired too close together, so they overwrote each other's state
- **The model forgets everything between runs, so conversation state is wiped each time** ✅
- The conversation lacks a schedule, so each run cannot tell which run came first

**Explanation:** Concept 12's core fact is that the model forgets everything between runs. So any state held in the conversation is wiped, and the loop just repeats its first step forever. The fix is to keep state outside the model, on disk, in a progress file. The 'conversation grew too long, dropped earliest messages' answer is a context-window mix-up. The loss is total between separate runs, not truncation within one. The 'fired too close, overwrote each other' answer invents a race condition. Separate runs do not share conversation state to overwrite. And 'lacks a schedule' confuses the heartbeat with memory. A schedule starts runs but stores nothing. This is why a loop's record lives in the repo, not the chat: the repo remembers, the model does not, just as a worker's shared notebook outlasts any single shift's memory.

*(Concept 12: State that survives between runs)*

---

### Q40.

**Q:** Your loop keeps repeating the same mistake every run. The course says the fix is not a cleverer prompt. What should you do, and where does it go?

- **Write the lesson into the rules file, so the fix holds for every run** ✅
- Add the lesson under the Done section of progress.md, so tomorrow reads it
- Hand the case to a stronger checker model that catches it each run
- Move the failing step into its own subagent for that one case

**Explanation:** Concept 12 says that when the loop keeps making the same mistake, have the loop write the lesson into the rules file (`CLAUDE.md` / `AGENTS.md`). So the fix stays for every future run, as a steady habit read at the start of each beat. Putting it under `progress.md`'s Done section fails, because the progress file records run state (tried, passed, open), not durable habits. A completed-items log does not change future behavior. A stronger checker model catches more mistakes but does not prevent the recurring one, and the course explicitly rejects a 'cleverer' approach. Spinning up a specialist subagent adds machinery without addressing memory. The durable fix is written guidance every run reads. Like adding a permanent line to the team handbook instead of re-explaining the same rule at every standup.

*(Concept 12: State that survives between runs)*

---

### Q41.

**Q:** When you sit down at the human gate after an unattended night, the course says you read the spine, not the full transcript. Why is the progress file enough to catch up?

- **It records what was tried, what passed, and what is still open for a human** ✅
- It stores the full transcript compressed, so nothing from the runs is lost
- It holds the rules file's habits, which is all a reviewer needs to decide
- It streams every model action live, so you can replay each run step by step

**Explanation:** The spine doubles as your record. Because the progress file is plain text in the repo, it captures what was tried, what passed, and what is still open, so you read it instead of every run's full transcript. The 'streams every action, replay step by step' answer is the opposite of the point. The spine is a digest, not a live feed. The 'full transcript compressed' answer also misses it. The file is a summary you write on purpose, and the whole tip is that you do NOT need the transcript. The 'holds the rules file's habits' answer confuses the two layers of state: the rules file carries steady habits, while the progress file carries run results, which is what you review at the gate. Like reading a shift handoff note rather than the security camera footage.

*(Concept 12: State that survives between runs)*

---

### Q42.

**Q:** A loop has a success condition, a limit, an isolated worktree, a read-only checker, a human gate, and logging, but no state file. The checklist says a missing item makes a loop "unsafe, forgetful, or invisible." Which is this, and what breaks?

- Invisible: an overnight failure stays silent because nothing records each run
- **Forgetful: with nothing on disk, each run repeats its first step forever** ✅
- Unsafe: a risky fix reaches main because no checker grades it first
- Unsafe: parallel runs collide and overwrite each other's edits

**Explanation:** The missing item is the state file (the spine, Concept 12), and the checklist's word for that gap is forgetful. With nothing on disk, the model's wiped memory means each run repeats its first step instead of building on the last. The 'invisible, overnight failure silent' answer describes the missing log or notification, which this loop already has. The 'risky fix reaches main, no checker' answer describes a missing read-only checker, which this loop already has. The 'parallel runs collide' answer describes missing worktree isolation, which this loop also has. Each wrong answer names a real checklist gap, just not the one removed here. That is the diagnosis skill. Like a night-shift worker with no logbook redoing yesterday's task every shift because they cannot recall finishing it.

*(Part 5: Minimum safe loop checklist)*

---

### Q43.

**Q:** A skeptic asks what stops a wrong fix from being merged to main while you sleep, in the morning-triage loop. Which answer matches the loop's actual design?

- A single reviewer PASS is enough, since the checker uses a stronger model
- The per-run limit halts the loop before any wrong fix can reach a protected branch
- **Three together: a reviewer PASS, only low-risk changes open a PR, risky work goes to a human** ✅
- The worktree isolation alone, since collisions are the only way main gets a bad change

**Explanation:** The course answers this with three safeguards working together. The reviewer subagent must return PASS (maker-checker). Only low-risk changes may open a PR. And the human gate routes anything risky or failing to a 'needs a human' note instead of main. Every run is also capped and logged. A single PASS being 'enough' is incomplete. PASS alone does not screen out risky changes, so the low-risk filter and human gate still apply. The limit governs cost and retries, not merge safety, so it never decides whether a fix reaches main. And worktree isolation only stops parallel agents from colliding. It does nothing to stop a bad-but-isolated fix from being merged. Like a bank wire that needs both an automated fraud check and a human approval above a threshold, not just one gate.

*(Part 5: The morning-triage loop)*

---

### Q44.

**Q:** On one real morning the reviewer returns FAIL on an image-library advisory, because the safe fix changes the output format, a public behavior change. Per the loop's design, what happens to that item?

- It is dropped silently, since a FAIL means the candidate was never valid
- It opens a PR anyway, but the title is flagged for a maintainer later
- It is retried on fresh branches until the reviewer finally returns PASS
- **It is written to the 'needs a human' section of progress.md, and no PR opens** ✅

**Explanation:** The skill's decision rule and the 'one real morning' example agree: on FAIL, or any change touching something risky like a public behavior change, the loop does not open a PR. It appends a short entry to the 'Open / needs a human' section of `progress.md`, saying what it tried and why it stopped. Opening a PR anyway breaks the rule that risky or failing work never goes straight toward main. Retrying until PASS is wrong, because a genuine public-behavior change will not pass review, so trying over and over just burns the limit. The loop escalates instead. And dropping it silently is the opposite of the design. The spine records it visibly so a human sees it at the gate. This is the maker-checker plus human-gate pattern that lets a real change-management process flag breaking changes for a person.

*(Part 5: The morning-triage loop)*

---

### Q45.

**Q:** A teammate's morning loop costs about $20 a month at five beats per weekday. Wanting faster reactions, they reschedule it to fire every five minutes around the clock. What does the course predict?

- Token cost per beat falls, because each run is shorter
- The loop responds faster but costs about the same each month
- **The monthly bill climbs comfortably past $1,000 for no value** ✅
- Worktree isolation breaks once parallel runs overlap

**Explanation:** The per-beat cost stays roughly fixed at about $0.21. What explodes is the number of beats. Firing every five minutes around the clock is over a hundred times as many beats as five a weekday, pushing a $20 loop comfortably past $1,000 a month for no extra value. The cost comes from how often the loop runs, not from which command you used. The claim that per-beat cost falls is backwards. Shorter gaps between runs do not shrink a beat's tokens. 'Roughly the same cost' ignores that beats multiply with frequency. Worktree collisions are a real risk for parallel agents, but that is an isolation problem, not a result of how often the loop fires. Real-world: setting a cron job to run every minute can quietly run up a cloud bill while delivering nothing new.

*(Concept 13: Token cost is the real limit (cadence dominates))*

---

### Q46.

**Q:** A loop's bill is too high, but the schedule cannot change. Which lever does the course call the single biggest saving while leaving cadence untouched?

- Replace the maker-checker split with one cheaper combined agent
- **Do the work cheaply, but keep a strong model for checking** ✅
- Paste the full project rules file into every scheduled prompt
- Raise the retry limit so fewer runs fail their checks

**Explanation:** Matching the model to the job is the course's single biggest saving, and it leaves cadence untouched: a cheap model does the mechanical work while a strong model checks. Collapsing the maker and checker into one agent destroys the only reason you can trust an unattended loop, since a model that checks its own output almost always approves it. Pasting the full project rules into every scheduled prompt does the opposite of keeping the prompt short. You re-pay for those tokens on every beat, which is why detail belongs in a skill that loads on demand. Raising the retry limit increases spend and invites runaway retries, the classic way token bills grow out of control. Real-world: routing simple support tickets to a cheap model and escalating only the hard ones to a premium model.

*(Concept 13: Match the model to the job)*

---

### Q47.

**Q:** On the OpenCode path, an engineer swaps in DeepSeek V4 Flash (about 30x cheaper) for both the maker and the checker, expecting roughly 30x savings. Why might the savings not appear?

- **A weaker maker writes worse fixes, so retries eat the savings** ✅
- Cheaper models always read far more tokens on every beat
- Claude Code refuses to run any model that is not Claude
- DeepSeek V4 Flash will not run on the OpenCode path

**Explanation:** The cheap-maker, trustworthy-checker caveat is the trap here: a weaker model writes worse fixes, fails review more often, and the extra retries eat the 30x savings. The course's fix is a cheap mechanical maker working from a clear spec, paired with a checker you trust, like the test runner and linter. The claim that DeepSeek cannot run on the OpenCode path is exactly wrong. Picking your own model is the whole reason the model lever exists on that path. Cheaper models do not read more tokens per beat. The token count per beat is roughly fixed, and only the price per token drops. Claude Code does run Claude only for its loop commands, but that is a fact about Claude Code, not why a both-cheap OpenCode swap underdelivers. Real-world: cutting QA to save money and shipping more defects.

*(Concept 13: Cheap maker, trustworthy checker)*

---

### Q48.

**Q:** After moving to a model 30x cheaper, an engineer fires the loop every five minutes and is surprised the bill still beats Sonnet run hourly. What explains this?

- A 30x-cheaper model only fails when scheduled too often
- The cheaper model silently reverts to Sonnet pricing overnight
- **Cadence still dominates: how often it runs sets the bill** ✅
- Hourly Sonnet runs skip the checker, so they cost nothing

**Explanation:** The model scales the bill down, but cadence sets it: a 30x-cheaper model firing every five minutes can still cost more than Sonnet running hourly, because run frequency and retries multiply the number of beats. A cheaper model does not 'only fail when scheduled too often'. It does not fail from cadence at all, it simply costs per beat times a huge beat count. Cheaper models do not secretly revert to Sonnet pricing overnight. The discount is real and lasting. And hourly Sonnet runs still pay for both the maker and the checker, so they do not cost nothing. Real-world: a cheaper cloud instance billed by the minute still produces a large bill if you leave thousands of them running.

*(Concept 13: Cadence still dominates)*

---

### Q49.

**Q:** A scheduled loop pastes a long instruction wall into every prompt and also carries a bloated rules file. According to the course, why is this costly, and what is the right fix?

- **Both are billed every beat: push the detail into a skill** ✅
- Bloat is fine, because skills are billed once per month
- Long prompts are free, but rules files bill per character
- The fix is to delete the rules file and inline everything

**Explanation:** You pay for the loop prompt and the rules file on every beat, so the fix is to keep both short and push the detail into a skill that loads only when used. The scheduled prompt then shrinks to one line like 'run the daily-triage skill.' Long prompts are not free: every token in them is re-billed each beat. And a rules file is not billed 'per character' as a special rule. It is just more tokens. Bloat is not fine, and skills are not a once-a-month charge. They load on demand and keep each beat cheap. Deleting the rules file entirely throws away the steady habits the loop reads every run. The goal is short, not gone. Real-world: trimming a verbose system prompt to cut per-call API costs across thousands of requests.

*(Concept 13: Keep the prompt and rules file short)*

---

### Q50.

**Q:** A loop's maker-checker reports every PR as 'done' with a PASS, so a teammate stops reading the diffs and just merges. What is wrong with that habit, per the course?

- **'Done' is still a claim, not proof: you read the diffs** ✅
- A passing checker fully removes your need to verify anything
- Reading diffs is only needed when the checker returns FAIL
- The checker's PASS is mathematical proof the code is correct

**Explanation:** The maker-checker split makes 'done' mean something, but it is still a claim, not a proof. So you read the diffs the loop opened before the work counts. Your job moved rather than vanished. The idea that a passing checker fully removes your need to verify is the press-go-and-stop-reading trap the course warns against. Reading diffs only when the checker returns FAIL misses the bad fixes a too-soft checker approved on PASS, which is exactly where silent mistakes hide. And a checker's PASS is a model's judgment, not mathematical proof. A model grading work can still be confidently wrong. Real-world: a green CI check is reassuring, but a senior engineer still reviews the pull request before merging it to production.

*(Concept 14: Checking the work is still your job)*

---

### Q51.

**Q:** Two engineers build the identical loop. Over months, one understands their project more deeply while the other understands it less. What does the course conclude?

- The second engineer simply chose a weaker, cheaper model
- The loop itself decides whether you keep understanding or not
- A better-designed loop would have forced both to stay engaged
- **The same act can keep you engaged or let you stop thinking** ✅

**Explanation:** The course's point is that designing the loop is one action with two possible results. Done with care, it keeps you engaged. Done to avoid the work, it lets you stop thinking. The loop cannot tell which. But you can. The difference was not a weaker model, because both engineers built the exact same loop, so the tooling is identical. The loop itself does not decide your understanding. The whole lesson is that the tool is neutral and the choice is the builder's. And no loop design can force engagement, since the same design serves both the engaged builder and the one avoiding the work. Real-world: a calculator can deepen a student's grasp of math or let them avoid ever learning it, depending entirely on how they use it.

*(Concept 15: The understanding gap)*

---

### Q52.

**Q:** As Claude Code keeps absorbing the loop's machinery (dynamic workflows, /goal, Routines), a junior asks which part of the skill will not be automated away. What is the course's answer?

- Writing the shell scripts that wire the scheduler together
- **Precise intent that can be checked, plus accountability** ✅
- Picking which cheap model the maker should run on
- Memorizing every flag, path, and model identifier

**Explanation:** As the tools absorb more machinery (the orchestration, the checker, and the schedule), the two ends from Concept 1 stay human: intent specified precisely enough to be checked, and accountability for what ships. That is why the course calls this engineering, not button-pushing. Writing the shell scripts is precisely the machinery the tools now absorb through Routines and /goal, so it is being automated, not preserved. Picking the cheap model is a mechanical cost tactic, useful but not the durable core of the skill. Memorizing flags, paths, and model IDs is the throwaway mechanical layer the course explicitly tells you to look up rather than internalize. Real-world: as accounting software automates bookkeeping, the CPA's judgment and signature remain the part that cannot be handed to the machine.

*(Concept 15: Intent and accountability (the through-line))*

---

### Q53.

**Q:** A nightly loop fails at 2am, leaves nothing behind, and the engineer only notices days later that nothing shipped. Which observability practice would have prevented the surprise?

- **Have every run append a timestamped note, even on failure** ✅
- Run it every five minutes so failures repeat until noticed
- Let the checker model approve its own work more loosely
- Send all output only to the terminal you already closed

**Explanation:** The missing practice is writing a line every run, even on failure. Each beat should append a timestamped note of what it tried, what passed, and what broke. A silent failure is the worst kind, and that note is what makes a 2am failure visible later. Firing every five minutes does not fix visibility. It multiplies cost and still leaves no record if each run stays silent. Loosening the checker makes the loop ship worse work, the opposite of observability. And sending output only to a terminal you already closed is the exact anti-pattern the course names. Output must go where you will actually see it, like a log file or a Slack message. Real-world: a backup job that fails silently for weeks until you discover there is nothing to restore.

*(Observability: write a line every run)*

---

### Q54.

**Q:** Someone wants to put a brand-new loop straight onto a nightly unattended schedule. What does the course advise instead, and where should they look first when something seems wrong?

- Trust it nightly at once: the maker-checker split guarantees safety
- **Run it under supervision for several days, and read the spine first** ✅
- Schedule it nightly now, then read the full transcript later
- Disable logging at night so the loop runs faster while unattended

**Explanation:** The guidance is to prove the loop before overnight use: run the loop hourly and watched for a few days before trusting it nightly and unattended. When something looks wrong, read the spine (the progress file) first, because it records what the last good run did. Trusting it nightly at once skips those watched runs, and the maker-checker split reduces risk but never guarantees safety. Scheduling it now and reading the full transcript later inverts the advice. You graduate the loop slowly and you read the compact spine, not every run's transcript. Disabling logging makes an overnight failure silent, the worst kind, directly against writing a line every run. Real-world: a pilot logs supervised flight hours before being cleared to fly solo at night.

*(Observability: prove the loop before overnight use)*

---

### Q55.

**Q:** An agent writes lessons to memory during its own sessions, yet the same mistake keeps repeating across ten different sessions and it never notices. Per the dreaming note, what limitation of in-band memory explains this?

- The agent's markdown files are the wrong format for storing lessons
- **The agent only sees its own session, so cross-session patterns are invisible to it** ✅
- The agent's rules file is read-only, so no lesson can ever be saved
- The agent's model is too small to recognize that a mistake is repeating

**Explanation:** In-band memory happens inside one live session, and that session is all the agent can see. A mistake repeating across ten sessions is a pattern that lives between sessions, exactly where no single in-band agent has visibility. That is one of the two built-in limits of in-band memory, alongside split attention between the task and memory work. The wrong-format answer fails because markdown files are exactly the recommended store. Format is not the problem. The read-only rules file answer contradicts the setup: the agent IS writing lessons, they just cover one session each. The too-small model answer misses that no model, however strong, can spot a pattern in transcripts it never receives. The fix is an out-of-band process with fleet-wide visibility, like dreaming. Real-world: each teacher sees only their own class, so only the head teacher who reads every class's results can spot a school-wide gap.

*(Concept 12 note: Dreaming (in-band vs out-of-band memory))*

---

### Q56.

**Q:** A dreaming pass reviews a month of transcripts, finds a failing tool call repeated across the fleet, and proposes a change to the shared memory store with example transcripts attached. What happens before the change takes effect?

- Nothing: an evidence-backed proposal is applied to the store automatically
- The proposal waits until every agent in the fleet approves it by vote
- **A human reviews the proposal and its evidence, then accepts or rejects it** ✅
- The change runs in a sandbox store for a week, then merges itself

**Explanation:** The dreaming process proposes changes and attaches evidence (example transcripts and how often the pattern appeared), but a human accepts or rejects each change before it lands. That is the human gate, placed exactly where the course says it belongs: a shared memory store is read by every future run, so a wrong automatic edit there is costly and hard to reverse. Automatic application removes the gate from the highest-leverage write in the whole system. Agents voting invents a mechanism the design does not have, and a fleet approving edits to its own rules is still self-grading at scale. A self-merging sandbox sounds cautious but still ships with no one accountable for the change. The lesson mirrors Concept 12's warning: an improvement loop rewriting its own rules with nobody watching is the one loop that most needs a reviewer. Real-world: a curriculum change proposed by the head teacher still goes to the school board before every classroom teaches it.

*(Concept 12 note: Dreaming (the human gate on memory changes))*

---

### Q57.

**Q:** Two agents in a fleet edit the same shared memory file at the same time, and one agent's update silently vanishes. Which production guardrail from the shared-memory note was missing?

- Portability: the store was not kept in an open format behind a clean interface
- Permissions by level: ordinary agents should never write to any file at all
- Versioning: recording who changed what would have stopped the overwrite
- **A conflict check before writing: verify the file did not change while drafting, and retry if it did** ✅

**Explanation:** The symptom is a lost update from two simultaneous writers, and the guardrail built for exactly that is the conflict check: before committing, the agent checks whether the file changed while it was drafting its edit, and if so it re-reads and tries again instead of overwriting. Versioning is close but answers a different question: it records history so a bad change can be rolled back after the fact. It does not prevent the collision in the moment. Permissions by level protect the organization-wide rules from ordinary agents, but these two agents may both legitimately have write access to this file, and 'never write at all' overshoots into breaking the spine. Portability is about moving curated memory between products, unrelated to concurrent writes. Databases solved this decades ago with optimistic locking, and agent memory inherits the same discipline. Real-world: two people editing one shared document without sync, where the second save quietly erases the first person's work.

*(Concept 14 note: When many loops share one memory (guardrails))*

---

### Q58.

**Q:** An attacker plants an instruction inside a GitHub issue body. A working loop reads that issue during a normal run, and a week later the dreaming pass reviews the transcripts and proposes adding the attacker's instruction to the rules file, with evidence attached, since the pattern really does appear in the logs. What protects the system at this point?

- Nothing: evidence-backed proposals are trustworthy by definition, so the rule lands
- **The human gate: a person reads the proposal and its cited source runs before anything is merged** ✅
- The connector list: removing the GitHub connector would have blocked the issue from being read
- The daily run cap: the dreaming pass cannot fire often enough to launder an injection

**Explanation:** This is memory poisoning by laundering: a one-time injection in untrusted input (an issue body) gets promoted into a durable rule that every future run reads. The dreaming note's two rules are the defense, and the second one is decisive here. Evidence helps, because the proposal must cite the runs it came from, but evidence alone is not enough, because the injected text really does appear in the logs, so the citation checks out mechanically. What stops it is the human gate: a person opens the cited source runs, sees that the 'pattern' is an instruction someone planted rather than a lesson the loops learned, and closes the PR. Trusting evidence-backed proposals by definition is exactly the trap. The evidence is real, the lesson is malicious. Removing the GitHub connector breaks the working loop's actual job, because triage requires reading issues, so it is not a defense, it is an amputation. And the run cap limits how often the pass fires, not what a single pass can write. Real-world: a forged invoice with a valid-looking paper trail still gets caught only because a human in accounts payable checks who actually ordered the goods.

*(Concept 12 note: Dreaming warning (memory poisoning and laundering))*

---

### Q59.

**Q:** A developer embeds a lint-and-fix check into a skill that came from a plugin, and it works, until the plugin updates and the check silently disappears. What went wrong, and what is the right pattern?

- The check needed `allowed-tools`: adding that line survives plugin updates
- **Embedding only works on skills you can edit: wrap the plugin skill in a thin skill that chains your check after it** ✅
- Plugin skills cannot run checks at all: the check must move to a Routine
- The check should have been written in the rules file, which plugins cannot touch

**Explanation:** The verification-skills interlude names this hard limit: embedding a check means appending it to the producing skill, and built-in or plugin-managed skills get overwritten on update, so the appended check vanishes. The right pattern for a skill you cannot edit is chaining via a thin wrapper: a small skill of your own that invokes the original skill, then invokes your check. Your wrapper survives every plugin update because the plugin never touches it. Adding `allowed-tools` scopes what a check may do. It does nothing to protect an embed from being overwritten. Plugin skills can absolutely be verified, just from outside, not by editing them. And the rules file holds short standing habits read every run, not a full check procedure. Moving the check there bloats every beat and still would not chain it to the plugin skill's completion. Real-world: you do not edit a vendor's library in node_modules. You wrap it, so your changes survive the next install.

*(Interlude: Codify the checker (embedding vs wrapper-skill chaining))*

---

### Q60.

**Q:** A verification check has been invoked by hand after every single change for two weeks, and its owner now wants it to gate every teammate's PR starting tomorrow, while also planning to keep changing its rules daily. Per the graduation rule, what is right and what is premature?

- Both steps are premature: a check must run for a quarter before any promotion
- Both steps are fine: a check that works once is ready for the team
- **Promoting it out of standalone is right, because running it after every change is the signal, but gating team PRs while still changing it daily is premature** ✅
- Neither home matters: where a check runs never changes its behavior

**Explanation:** The interlude gives two graduation signals, and this scenario triggers exactly one. Catching yourself running a check after every change is the stated signal that it is ready to leave the standalone home, so embedding or chaining it now is correct, not premature. But the second rule says to wait before adding a PR-wide gate while the chain is still changing, because once the check guards the team's PRs, every change to it is visible to the whole team, and this owner plans daily changes. So the promotion to a permanent home is earned. The jump to team infrastructure is not, yet. 'Wait a quarter' invents a fixed timeline the course does not have. The ladder is based on behavior, not on the calendar. 'Works once, ready for the team' skips the whole ladder. And where a check runs absolutely matters: the home decides who fires it, when, and who feels its changes. This is Part 6's watched-before-unattended rule, applied to the checker itself.

*(Interlude: Codify the checker (the graduation rule))*

---

### Q61.

**Q:** A colleague reads Anthropic's verification-loops article and concludes that a verification loop is a full loop in this course's sense (heartbeat, spine, and all), so writing one replaces everything in Parts 2 and 4. What is the correct taxonomy?

- Correct: a verification loop schedules itself and remembers between runs
- **A verification loop is small-loop machinery inside one beat: it becomes a big loop's checker only when a heartbeat fires it, and it still has no spine of its own** ✅
- A verification loop is the spine: the check results are the memory between runs
- A verification loop replaces the maker-checker split, so Concept 11 no longer applies

**Explanation:** The interlude makes the taxonomy point explicitly: a verification loop (attempt, check, fix, repeat) runs inside one beat. It has no heartbeat of its own and no spine. When the beat ends, it ends. What connects it to this course is composition: the same written check becomes the checker of a big loop the moment a heartbeat (a schedule, an event, a PR trigger) fires it. Claiming it schedules itself and remembers between runs hands it exactly the two parts it lacks. Calling it the spine confuses a check that runs during a beat with state that survives between beats. Check results vanish with the session unless something writes them to disk. And far from replacing maker-checker, a codified check is what the checker grades against, because Concept 11's split is how the check gets applied by someone other than the maker. Real-world: a factory's quality-control station is essential, but it is not the production schedule and it is not the inventory ledger.

*(Interlude: Codify the checker (small-loop vs big-loop taxonomy))*

---

[⬅ Sources & Further Reading](14-sources-further-reading.md) · [⬆ Index](README.md)