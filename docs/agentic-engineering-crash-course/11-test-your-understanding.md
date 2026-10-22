# 11 — Test Your Understanding (18-Question Assessment)

Book ke apne "Knowledge Check" `<Quiz>` block se verbatim (English, precision ke liye).

1. **Q:** A teammate argues that since AI now writes most of the code, careful naming and clean module boundaries no longer earn their keep. Where does the chapter say this reasoning breaks down?
   - **The names and boundaries you draw become inputs the agent learns from** ✅
   - Clean naming only matters for the humans who still read pull requests
   - Modern models ignore existing names and infer all structure from scratch
   - Naming conventions slow the agent down by adding tokens to parse
   *(Intro: Software fundamentals matter more in the AI era)*

2. **Q:** Deciding whether to vibe code or apply agentic engineering for a payroll Digital FTE an organisation will trust with real money. Which call fits the chapter's framing?
   - Vibe code it; the agent already preserves the quality bar automatically
   - **Apply agentic engineering, because vibe coding here is malpractice** ✅
   - Vibe code the logic and engineer only the user interface layer
   - Either is fine since the typist, not the stance, sets quality
   *(Section 1.2: Vibe coding raises the floor; agentic engineering preserves the ceiling)*

3. **Q:** OpenCode ships its installer as a paragraph of natural language pasted into a coding agent rather than as a bash script. Which Software 3.0 idea does this best illustrate?
   - Bash scripts are deprecated and no longer run on modern systems
   - Natural language always executes faster than the equivalent compiled instructions
   - **The artifact you produce is now text intended for an agent** ✅
   - Installers must avoid code so non-programmers can read them
   *(Section 1.1: Software 3.0, a new computing paradigm)*

4. **Q:** At turn 9 your agent uses `User.email` correctly, but by turn 52 the same session writes `user.emailAddress`, a field that does not exist. The model and prompt are unchanged. What actually shifted?
   - The model silently swapped to a weaker variant mid-session
   - Your schema file was edited by another process between turns
   - The advertised context window shrank as the session progressed
   - **Attention budget thinned as competing tokens diluted each signal** ✅
   *(Section 2.1: The smart zone and the dumb zone)*

5. **Q:** A colleague upgrades to a model marketing a 1M token window and says coding sessions can now run far longer before quality drops. How does the chapter temper that?
   - **Bigger windows help retrieval but do not extend the reasoning horizon** ✅
   - A 1M window pushes the dumb zone past anything a coding session reaches
   - Reasoning quality for code scales linearly with the advertised window size
   - Larger windows only raise your token bill and buy nothing useful at all
   *(Section 2.1: The smart zone and the dumb zone)*

6. **Q:** Most developers reach for compaction over clearing because it feels less destructive. Why does the chapter tell you to treat that instinct with suspicion?
   - Compaction permanently corrupts the files written earlier in the session
   - Compaction costs far more tokens than starting a fresh session does
   - **Compaction preserves some of the dumb-zone reasoning that caused the trouble** ✅
   - Clearing is slower because the harness must rebuild the whole index
   *(Section 2.2: The Memento problem)*

7. **Q:** A state-of-the-art model finds a zero-day vulnerability, then in the same session tells you to walk fifty metres to a car wash instead of driving. What is the chapter's explanation for this pairing?
   - The model was distracted by the sheer size of the earlier security task
   - **Capability peaks where labs trained with verifiable rewards, valleys elsewhere** ✅
   - The model degrades predictably the longer any one session is left to run
   - Physical-world tasks are simply harder for it than finding security flaws
   *(Section 2.3: Jagged intelligence)*

8. **Q:** The chapter says static types and automated tests do more than catch bugs, framing them through jagged intelligence. What deeper role do they play?
   - They document the codebase so future humans onboard faster
   - They reduce the token count the agent must process per turn
   - They let the agent skip reading the existing implementation files
   - **They keep the agent inside the verifiable circuits it was trained on** ✅
   *(Section 2.3: Jagged intelligence)*

9. **Q:** Starting a greenfield Digital FTE, you can pick any language and datastore. Citing on-distribution reasoning, which stance does the chapter recommend?
   - **Prefer mainstream choices the agent writes well, like Python and Postgres** ✅
   - Pick whatever language and datastore you personally write fastest in alone
   - Choose niche tools now, since the long tail will surely catch up soon enough
   - Let the agent select the whole stack on its very first turn, unguided
   *(Section 2.3: Jagged intelligence, fourth implication)*

10. **Q:** Your agent keeps writing a paragraph to describe what your team calls a materialisation cascade, burning tokens talking past you. Which failure mode and cure does this match?
    - Weak feedback loops; make the environment loud with tests and types
    - Misalignment on the design concept; grill before any asset is written
    - **No ubiquitous language; keep a CONTEXT.md of domain terms loaded each session** ✅
    - Shallow modules; run a periodic deepening pass across the whole codebase
    *(Section 3: Failure 2, the agent is too verbose)*

11. **Q:** A senior engineer reports feeling more tired, not less, after a week of AI pairing despite shipping far more code. What does the chapter diagnose as the cause?
    - The agent introduced subtle bugs that drained debugging energy
    - **Reading every line at five-times pace multiplies cognitive load** ✅
    - Compaction kept losing context and forcing constant re-explanation
    - The model picked an off-distribution stack the engineer disliked
    *(Section 3: Failure 5, my brain cannot keep up)*

12. **Q:** You want to split a PRD for a gamification feature into issues. Why does the chapter call horizontal slicing, one issue each for database, API, and UI, the wrong shape?
    - It produces more total issues than vertical slicing does
    - It forces every issue to be flagged human-in-the-loop rather than AFK
    - It makes each issue too large to fit a single agent session
    - **No end-to-end feedback arrives until the third issue finally lands** ✅
    *(Section 4.3: Vertical slices and tracer bullets)*

13. **Q:** Someone proposes treating specs as the whole workflow: write the spec, compile it through the agent, ignore the code, and on any problem edit the spec and recompile. What is the chapter's core objection?
    - Specs are simply too slow to write to keep up with fast-moving feature work
    - Agents cannot read long markdown specifications reliably enough yet
    - **Hidden code constraints the spec never anticipated pull it from reality** ✅
    - Specs require a separate tool that neither harness supports natively
    *(Section 4.2: The limits of specs-to-code)*

14. **Q:** A `gamification-prd.md` written in March is loaded in July to extend the system. The chapter says the agent inherits a problem before it writes a line. What is it?
    - **The spec decayed; names, boundaries, and requirements have all moved on** ✅
    - The spec is simply too long now to fit inside the agent's context window
    - The spec was written back then by a weaker model than the current one
    - The spec lacks the YAML frontmatter the harness needs to parse it at all
    *(Section 4.2: The limits of specs-to-code)*

15. **Q:** You are about to add a streak feature and must decide where it belongs. Why does the chapter prefer one deep `GamificationService` over many small exported functions for AI work specifically?
    - Deep modules let the agent write the feature without any tests at all
    - Many small functions always run faster than one larger class does
    - Deep modules require writing fewer total lines of implementation code overall
    - **A small interface lets the agent trust one boundary, not many** ✅
    *(Section 7.1: Deep modules over shallow modules)*

16. **Q:** In the shallow gamification version a caller can forget to invoke `validateAntiCheat` and silently corrupt the system. How does the deep version make that bug impossible?
    - It adds a runtime assertion that throws if the anti-cheat check was skipped
    - **It hides `validateAntiCheat` inside `awardLessonCompletion`, beyond a caller's reach** ✅
    - It documents the required call order in a comment at the top of the module
    - It moves anti-cheat into a separate service the dashboard has to import
    *(Section 7.1: Deep modules over shallow modules)*

17. **Q:** The chapter says a senior engineer can hold the architectural map of a million-line codebase in their head. The gray-box principle explains how. What is the mechanism?
    - **The map contains only interfaces, and interface change-sets stay small** ✅
    - The agent summarises the whole codebase into a short briefing each morning
    - Modern IDEs render the full dependency graph so memory is unnecessary
    - The engineer reads every diff but at five times their normal pace
    *(Section 7.3: Design the interface, delegate the implementation)*

18. **Q:** The closing frames your agent as an excellent tactical programmer, a sergeant who can take any well-specified hill. According to the chapter, what stays uniquely the strategic programmer's job?
    - Writing the individual functions and tests the sergeant cannot produce
    - Choosing the programming language the sergeant is allowed to use
    - **Deciding which hill, forming the design concept, and holding the map** ✅
    - Reviewing every line the sergeant writes before any merge happens
    *(Section 10: Closing, the strategic programmer)*

---
[⬅ Closing — The Strategic Programmer](10-closing-strategic-programmer.md) · [⬆ Index](README.md)
