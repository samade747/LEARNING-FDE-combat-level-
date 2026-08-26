# 07 — Test Your Understanding (Assessment)

Book ke live page par yeh section ek interactive `<Flashcards />` widget se shuru hota hai (auto-
generated, page ke apne key-terms se) — koi static text nahi, isliye copy karne layak content nahi hai;
live version [ai-prompting-2026](https://agentfactory.panaversity.org/docs/ai-prompting-2026#flashcards)
par dekho.

Uske baad **30-question assessment** aata hai (book ke apne `<Quiz>` component se, verbatim) — course
ke har concept (Part 1 se Part 4 tak, plus recap aur "what changed" note) ka scenario-based test, sahi
jawab ke sath explanation bhi. Yeh poora quiz neeche hai, taake khud test kar sako ya apni class ko exam
ki tarah de sako. Content seedha book se hai (English mein — precision zaroori thi, translate nahi kiya).

---

### Q1. CRM buy karne ka generic jawab

**Q:** A new analyst types 'which CRM should we buy?' into a frontier model and gets back a generic three-vendor list. A teammate says the answer is generic because the model is weak at enterprise software. Based on Concept 1, what is the actual cause and the fix?

- The model is genuinely weak at enterprise software tasks, so switching to a model that specializes in business tools would produce a specific pick
- The model lacked web search, and turning search on by itself would make the answer specific to this company's exact situation
- **The prompt carried no context; a power user attaches the team's requirements, budget, and current stack, then asks for the trade-offs** ✅
- The question was simply too long for the model to parse, so cutting it down to a few sharp keywords would tighten the recommendation

**Explanation:** Concept 1 frames AI as a smart new colleague who knows nothing about you yet, so the fix is briefing, not switching to a different model. Turning on web search cannot help either, because the team's internal stack and budget are not on the public web. And shortening to keywords removes the very context that would make the answer useful.
*(Concept 1: Novice vs power user)*

---

### Q2. Manager chahta hai model ko onboarding process pehle se pata ho

**Q:** A manager is annoyed that AI did not factor in 'our standard onboarding process' when drafting a plan, saying a model this advanced should already know it. How does the smart-new-colleague model answer this?

- **The model reads whatever you put in front of it but cannot guess what you never told it, so an internal process has to be supplied as context** ✅
- The manager is right, since a frontier model has read enough of the public internet to infer almost any company's internal onboarding process
- The model could infer the process, but only once the conversation grows long enough for it to pattern-match across many turns
- The model would know the process automatically the moment web search is enabled, since it could simply look the company up online

**Explanation:** The colleague analogy is precise: a new hire reads what is in front of them and does not guess what was never said. An internal onboarding process is not in training data, so the model cannot infer it from the internet; it will not emerge just because the chat grows longer; and it is not on the public web for search to find.
*(Concept 1: Novice vs power user)*

---

### Q3. Obscure regional folk game ke rules

**Q:** Someone asks AI for the rules of an obscure regional folk game and receives three confident, fluent paragraphs. Concept 2 says to do what before trusting them?

- Trust the answer, since fluency and confidence reliably indicate the model retrieved a real, well-represented, authoritative source
- Distrust it, but only because language models are weak at games as an entire category, no matter how common the specific game happens to be
- Trust it once you ask the model to rate its own confidence, since a model's stated confidence reliably tracks how accurate it actually is
- **Distrust the confidence: sparse training data means the model likely generalized from similar games, so verify with someone who knows it** ✅

**Explanation:** Concept 2 ties reliability to how well-represented a topic is in training data, and an obscure local game is sparse, so the model blends details from similar games it saw more often. Confidence and fluency are not the signal, and a model's self-rated confidence does not track its accuracy. The issue is data sparsity for this specific game, not games as a category.
*(Concept 2: Pretrained knowledge)*

---

### Q4. Typo fix karne mein waqt zaya, verify karne mein nahi

**Q:** A user spends time carefully fixing every typo in their prompts and never checks AI claims against other sources. Which pair of corrections does Concept 2 actually recommend?

- Keep fixing typos but stop verifying, since the model is most reliable on exactly the popular, well-covered topics people tend to ask it about
- **Stop fixing typos (the model handles messy text fine), but do verify important claims, since it absorbed misconceptions from the same text** ✅
- Keep doing both, since fixing typos sharpens the prompt and verifying protects you, and both genuinely change the quality of what comes back
- Stop doing both, because once you brief the model well, neither a stray typo nor an unchecked claim has any real effect on the final output

**Explanation:** Concept 2 says AI was trained on typo-filled internet text and handles misspellings gracefully, so correcting them is wasted effort. The same sources also carried confidently-wrong claims, so verifying important claims against a primary source is the habit that actually pays off.
*(Concept 2: Pretrained knowledge)*

---

### Q5. Henderson, Nevada mein 20 saal purani closed school suggest ho gayi

**Q:** A runner asks 'where should I run in Henderson, Nevada?' and AI recommends a school that closed to the public twenty years ago, citing an old web page. Which mode fired, what went wrong, and what is the fix?

- **Web search fired but does not check whether sources are current; name authoritative, current sources and ask the model to date each claim** ✅
- Pretrained mode fired with no search at all, and the only real fix is to manually turn web search on for every single local question you ask
- Deep research fired and still failed here, which proves deep research is fundamentally unreliable for any location-based question you ask it
- The model fabricated the school out of nothing, and the only reliable fix from here is to switch to a completely different model family

**Explanation:** Concept 3 uses this exact example: web search retrieved a real but stale page because the retrieval layer does not check whether a source is current. Naming authoritative, current sources and asking the model to date each claim is the fix. It was not pretrained-only, since the answer came from a page; it was not a deep-research failure; and the page was real, not fabricated.
*(Concept 3: The 3 retrieval modes)*

---

### Q6. Web page ka misrepresentation, jabke search hui thi

**Q:** A reader notices AI sometimes misrepresents what a web page actually said, even when it clearly searched. Concept 3 explains why and offers a fix. Which is correct?

- The model hallucinated from training data and never actually read the page at all, so the only real fix is to disable web search entirely
- The page quietly changed between the moment of the search and the moment of the answer, so re-running the same prompt twice and comparing fixes it
- The model cannot read English web pages directly, so you have to paste the relevant page text in yourself every single time you ask
- **A smaller retrieval layer condenses each page before the main model sees it, losing nuance; ask it to quote the exact sentence behind each claim** ✅

**Explanation:** Concept 3 describes a search-and-retrieval layer, often a separate and smaller model, that reduces pages to summaries before the user-facing model reads them, which is where nuance is lost. Asking the model to quote the exact sentence behind each claim surfaces the original wording and catches summary drift. The page was read, it did not change mid-answer, and the model can read web text directly.
*(Concept 3: The 3 retrieval modes)*

---

### Q7. IRS form 1040 vs diabetes medication comparison

**Q:** You need two things today: the official IRS page for form 1040, and a comparison of three diabetes medications with what recent evidence says. Concept 3's AI-vs-Google rule points you where?

- Use AI for both, since AI can do everything Google does and a good deal more, all from one place
- Use Google for both, since each question ultimately resolves to one specific web page you can land on
- **Google to land on the known IRS page, and AI to synthesize the multi-source medication comparison** ✅
- AI for the IRS page for faster navigation, and Google for the medications since there are more sources to read

**Explanation:** Concept 3's rule: reach for Google when you want a link or a specific known site, such as the IRS form page, and reach for AI when you want synthesis across sources, such as the medication comparison. Using one tool for both ignores the link-versus-answer distinction, and using AI for the IRS page while sending the comparison to Google inverts it.
*(Concept 3: The 3 retrieval modes)*

---

### Q8. Alag chat mein kal ka constraint yaad nahi

**Q:** A user is frustrated that today's chat does not remember a constraint they stated in a separate chat yesterday, and assumes the product is broken. What does Concept 4 say is actually happening?

- **The model is stateless and answers only from this response's context window, so yesterday's constraint must be re-supplied as a paste or a file** ✅
- It is a memory bug in the product, and the right thing to do is report it and wait for the vendor to ship a proper patch for it soon
- The free tier strips out memory, and upgrading to a paid plan would carry the context across separate chats automatically from then on
- The model quietly degraded overnight, and simply starting fresh tomorrow morning will restore its memory of the constraint you set

**Explanation:** Concept 4 rests on one fact: the model has no memory of its own and sees only what is in the context window for this response. Nothing outside that stack exists for this answer, so a specific constraint has to be re-supplied. Memory features do change what arrives automatically, but they store a synthesized profile of who you are and how you work, not the verbatim constraints from one particular chat, and they are not gated behind a paid plan. It is not a bug to report and not overnight degradation.
*(Concept 4: Context is the whole game)*

---

### Q9. Ek lambi conversation mein workout, spreadsheet, aur thank-you note mix ho gaye

**Q:** Over one long conversation a user plans a workout, then debugs a spreadsheet, then drafts a thank-you note. The answers get vaguer and start referencing unrelated earlier turns. What is happening and what is the fix?

- The model is overloaded right now, and the fix is to ask it one more, very detailed clarifying prompt that pulls its focus back where you want it
- **Context rot: unrelated earlier topics are crowding the window; start a new conversation when the topic changes and paste in only what matters** ✅
- The model needs a larger context window for this, and upgrading to a million-token model would remove the problem entirely going forward
- The tool itself is simply broken in this session, and the only reliable fix left is to switch over to a completely different AI product

**Explanation:** Concept 4 names this context rot and warns specifically against the one-more-clarifying-prompt instinct, which only adds more tangled context. A bigger window does not fix the mixing of unrelated topics, and the tool is not broken. The cheap, effective fix is to start a new chat and re-paste only the few facts that matter.
*(Concept 4: Context is the whole game)*

---

### Q10. Har chat mein wohi syllabus paste karna

**Q:** A user keeps pasting the same syllabus, the same audience description, and the same instructions into chat after chat about their kids' school. Concept 4 says this is the signal to do what?

- Memorize the standing instructions so that you can at least type them all back in a little faster each time you open a brand-new chat
- Keep one very long conversation open forever for that topic, so the context never has to be entered again from scratch at any point
- Switch to a model with a much larger context window, so that the endless repeated pasting at least becomes a bit cheaper to do
- **Set up a project, a workspace with standing files and instructions that every chat inside it inherits, so context is front-loaded just once** ✅

**Explanation:** Concept 4 says the moment you have pasted the same files or instructions into two or more chats on a topic, that context belongs in a project, not a prompt. Memorizing it still means retyping; a single long chat causes context rot; and a bigger window does not remove the repeated typing.
*(Concept 4: Context is the whole game)*

---

### Q11. "Think step by step" ab obsolete ho chuka hai

**Q:** A 2023 habit was to append 'think step by step' to hard prompts. Concept 5 says that advice is now mostly obsolete. What replaces it, and what is the implication of the METR trajectory?

- **Invoke reasoning directly with 'think hard', a thinking toggle, or letting the tool decide, and re-test what AI can do every few months** ✅
- Nothing really replaces it, because genuinely hard prompts are simply beyond what any of the current models can do reliably, even today
- Keep appending 'think step by step' to hard prompts, because the phrase still measurably improves the quality of modern reasoning models
- Break every hard task into tiny sub-prompts by hand yourself, because the models still cannot explore multiple approaches internally on their own

**Explanation:** Concept 5 says modern models have built-in reasoning you invoke in plain language or with a toggle, and the METR study found the longest reliably-completed task climbing fast, from minutes to an hour or more. So the move is to hand AI harder tasks and re-test your assumptions. The old phrase is no longer the lever, and manual decomposition is no longer required.
*(Concept 5: Reasoning, or think hard)*

---

### Q12. Chhote kaamon ke liye thinking mode on karna

**Q:** A user toggles extended thinking mode on for 'summarize this one paragraph' and 'give me five casual brainstorm ideas.' What does Concept 5 advise?

- Keep it switched on for absolutely everything, since thinking mode never hurts the result and only ever improves the answer you get back
- Turn it off here purely to save money, since the quality of the answer is genuinely identical either way on every kind of task you give it
- **Turn it off for these: thinking mode is slower and spends more budget, so save it for questions you would want a human to take time on** ✅
- Leave it on but just ask for shorter answers, which roughly cancels out the extra cost the thinking would otherwise add to the request

**Explanation:** Concept 5's note on when not to use thinking mode names quick lookups, short summaries, and casual brainstorming as cases where it is just slower and costlier. It is reserved for multi-input, multi-trade-off questions. The cost is not the only reason to turn it off, the quality is not identical on hard questions, and shorter answers do not cancel the extra thinking cost.
*(Concept 5: Reasoning, or think hard)*

---

### Q13. "Approach A behtar kyun hai" — loaded question ka neutral rewrite

**Q:** A user writes 'Why is approach A better than approach B?' and the AI dutifully lists reasons A wins. Concept 6 says the problem is in the prompt. What is the neutral rewrite?

- 'Find more evidence that approach A is the better one, so that I can feel really sure about it before I finally commit to it'
- **'Compare approach A and approach B; score each on cost, risk, and time, and give the strongest case for and against each'** ✅
- 'Confirm for me that approach A is the better one here, and then go on to tell me exactly how confident you are in that'
- 'Tell me one more time why approach A is better, but in much more detail this time and with several concrete worked examples'

**Explanation:** Concept 6 shows that verbs like find, defend, confirm, and prove hand the AI a conclusion before the question even starts. 'Why is A better' presumes A wins. The neutral rewrite lays out both options without hinting at a preference and asks for scored pros and cons on each. The other three keep the conclusion baked in.
*(Concept 6: Sycophancy and how to neutralize it)*

---

### Q14. Business idea ki warm praise vs rubric-based harsh score

**Q:** A founder asks 'I have a great business idea, critique it' and gets warm praise. They re-ask with a five-point rubric scored 1 to 10, and the same model rates the idea harshly with concrete reasons. Why does forcing a number work?

- The number simply flatters the model into trying a bit harder, which is itself a well-known and recognized form of prompt engineering
- The number makes the model switch over into a more capable internal mode that it normally keeps in reserve only for graded, scored tasks
- The rubric quietly replaces the model's own judgment with arithmetic, so the resulting score is purely mechanical and not about the idea
- **Vague praise is cheap, but a specific score forces the model to commit and look harder, and gives you something you can act on and track** ✅

**Explanation:** Concept 6 explains that a model wanting to please can call a draft 'strong' without committing, but being forced to choose between a 6 and a 7 makes it actually look. The number is also a unit of measurement for you: it tells you what to fix first and whether the next draft improved. It is not flattery, not a hidden graded mode, and not a replacement for the model's judgment.
*(Concept 6: Sycophancy and how to neutralize it)*

---

### Q15. Home exercise suggestions "average" nikalti hain

**Q:** Asked for 'ways to exercise at home,' AI returns squats, push-ups, and planks: not wrong, just average. Concept 7 says the way past average is not a cleverer single prompt. What is it?

- **A loop: load context up front, demand three to five options, give explicit feedback, demand new options, iterate, then expand the best one** ✅
- A single longer, more detailed one-shot prompt that carefully anticipates everything you could possibly need from it right up front
- A bigger and more capable model, on the theory that it is really the smaller models that keep defaulting to the most common answers
- Turning on web search for the request, so that the model can go and dig up the less common, more unusual exercises from around the web

**Explanation:** Concept 7 says the average internet answer is common, so the average AI answer is common, and the way around it is the brainstorm-iterate loop, not a cleverer one-shot prompt, a bigger model, or web search. Forcing alternatives and giving explicit feedback is what pushes the model past its first instinct.
*(Concept 7: The brainstorm-iterate loop)*

---

### Q16. Pehle draft likhna vs pehle outline banana

**Q:** A writer is tempted to ask AI for a finished 600-word draft on the first try. Concept 7 says to outline first. What is the underlying reason outlining beats drafting first?

- Outlines are simply shorter than drafts, so the model ends up spending noticeably less of its usage budget when it produces one first
- Outlines are an easier task for the model to handle than full prose is, so the quality of what it produces comes out measurably higher
- **Leverage in writing is structural: a word changed in an outline can redirect the whole piece, and AI writes word-by-word, so force structure first** ✅
- Drafting first is perfectly fine as long as you carefully grade the finished draft afterward; the outline step is really just optional polish

**Explanation:** Concept 7 explains that editing one word in an outline can change the article's whole direction, while editing one word in a draft changes one word, and that AI generates word-by-word, so it cannot see the whole shape unless you force structure first. That is why the outline step is load-bearing, not optional polish, and not just a budget saver.
*(Concept 7: The brainstorm-iterate loop)*

---

### Q17. Whiteboard photo mein missing word vs blurry gym machine photo

**Q:** A teacher photographs a whiteboard where his head blocks one word in a diagram, and AI infers the missing word correctly. But when he asks 'which gym machines are these?' from a slightly blurry photo, AI answers confidently and wrong. What principle does this illustrate?

- The camera quality alone decides the whole outcome here; a noticeably sharper, steadier photo would have made both of the tasks succeed
- AI is simply unreliable with any image at all, so honestly it should not really be trusted or used for visual tasks of any kind
- The whiteboard only worked because text is easy for it; AI genuinely cannot interpret diagrams or full real-world scenes at all yet
- **AI reads images coarsely: strong on gist, scene, and inference, weak on fine detail, so trust the gist and verify fine detail for high stakes** ✅

**Explanation:** Concept 8 says AI is strong on overall scene, composition, and inferring from the gist, like the blocked word, and weak on fine details and reading small or similar-looking objects, like the gym machines. The lesson is to trust the gist and double-check fine detail for high stakes, not to abandon image input or to credit the camera alone.
*(Concept 8: Multimodal)*

---

### Q18. Diagram recipe: Claude mein structure, phir ChatGPT/Gemini mein polish

**Q:** Concept 8's diagram recipe structures a diagram as SVG in Claude, then redraws it for polish in ChatGPT or Gemini. Which statement captures both why the order is what it is and what survives when the leading tools change?

- The order is basically arbitrary, since any tool can do either of the two steps about equally well, so just pick whichever you have open
- **Structure first in the strongest reasoning model, then polish in the strongest text-heavy image model; the two-step chain outlasts the named leaders** ✅
- Always do both of the steps inside one single tool, so that you never lose any labels in the handoff between two different models
- Polish the image first and structure it second, on the theory that a beautiful finished draft is much easier to reason carefully about

**Explanation:** Concept 8 says deciding what belongs in a diagram is a reasoning task, which is Claude's strength, and rendering text-heavy images well is a different strength, which is ChatGPT's or Gemini's, so chaining them beats asking either to do the other's job. The named leaders will rotate; what survives is structure-first-then-polish.
*(Concept 8: Multimodal)*

---

### Q19. Ek prompt se Pomodoro timer artifact ban gaya

**Q:** After a single prompt, AI renders a working Pomodoro timer in a side panel of the chat. A user assumes it is just a screenshot preview. What is actually true about that object, per Concept 9?

- **It is an artifact (Artifacts in Claude, Canvas in ChatGPT and Gemini): a persistent object you can edit in place, iterate on, and share by link** ✅
- It is only a static preview of the result; to change anything at all about it you have to regenerate the entire app again from scratch
- It only runs for as long as that one chat tab stays open, and it disappears permanently the very moment that you close the tab on it
- Anyone you try to share it with first has to have their own paid account before they are even able to open and use the thing at all

**Explanation:** Concept 9 explains the panel holds an artifact: persistent, iterable in place (saying 'make the button bigger' edits it rather than regenerating), and shareable through a public link that recipients can open without an account. It is not a static screenshot, it does not vanish when the tab closes, and the recipient does not need a paid plan.
*(Concept 9: Building small apps with one prompt)*

---

### Q20. Bill splitter vs real-time multiplayer game — one-prompt build ki limit

**Q:** Using the Goal / Input / Output recipe, which request is realistic for a one-prompt build, and which needs real engineering beyond a single prompt?

- A real-time multiplayer game with accounts and matchmaking is a perfectly fine one-prompt build, while a single-screen bill splitter is too trivial
- Both of these are realistic one-prompt builds today; honestly nothing much in this whole space still needs more than a single prompt anymore
- **A single-screen bill splitter with no accounts and no services is a realistic one-prompt build; internet multiplayer needs real engineering** ✅
- Neither one is actually possible from just a prompt; all real app building of any kind still requires you to sit down and write the code yourself

**Explanation:** Concept 9 says small things that fit on one screen with no accounts and no external services work, like the bill splitter, while networking, accounts, and matchmaking, like internet multiplayer, are still beyond a one-prompt build. The bill splitter is not too simple to bother with, and both-or-neither misreads the boundary the concept draws.
*(Concept 9: Building small apps with one prompt)*

---

### Q21. 18 numbers ka median/average — code chala ya nahi?

**Q:** You paste eighteen numbers and ask for the median, average, and outliers. The reply is a confident paragraph of numbers with no visible code block. Concept 10 says what happened, and what should you do?

- The numbers are guaranteed to be correct, because models compute deterministically, so you can simply read them off and accept them as final
- The model genuinely cannot do arithmetic at all on its own, so the only safe fix here is to sit down and compute the whole thing yourself
- The model needs a larger context window to handle all eighteen numbers at once, and quietly upgrading the plan would clear the problem up
- **The model answered from a glance without running code, the silent failure; ask it to write and run code and show it, and check a count first** ✅

**Explanation:** Concept 10 calls this the silent failure mode: the model chooses whether to run code based on phrasing, and on small questions it may answer from a glance, which looks identical to a real analysis. The fix is to ask explicitly for code and to demand a verifiable specific, like the exact count or column names, up front.
*(Concept 10: Data analysis)*

---

### Q22. Code chal chuka, phir bhi 3 cheezein manually check karni hain

**Q:** An AI did run code on your uploaded spreadsheet and produced charts. Concept 10 says reliability is high but not infinite. Which three things still deserve a manual check?

- The font of the chart it drew, the exact color palette that it happened to choose, and the file name it saved the final output under
- **The final totals (it may have summed the wrong column), the graph labels (sometimes confidently wrong), and any column it may have misread** ✅
- Only the spelling in the summary text it wrote, since the underlying math itself is always reliably right the moment any code has run
- Nothing at all really needs checking here; once actual code has run on the file, every single part of the output is effectively verified

**Explanation:** Concept 10 lists exactly these checks even when code ran: the totals, since it may have summed the wrong column; the graph labels, since captions are sometimes confidently wrong while the numbers are right; and the column interpretation, since a misread column makes the whole analysis unsound. Cosmetic items are not the risk, and 'nothing to check' is the trap.
*(Concept 10: Data analysis)*

---

### Q23. Cowork jaisa desktop app messy client folder reorganize kare — safe workflow

**Q:** You want an AI desktop app like Cowork to reorganize a messy client folder. Concept 11 prescribes a specific safe workflow. What is it?

- **Tell it the task, ask for a plan rather than action, review and edit the proposed file operations, and only then approve the execution** ✅
- Grant it full disk access right away so it has absolutely everything it could need, and then simply let it reorganize the whole folder freely
- Let it act on the messy folder immediately, and then just undo anything at all that you happen to dislike afterward from the recycle bin
- Ask it to go ahead and reorganize the folder, and then have it email you a full report of everything that it changed after the fact

**Explanation:** Concept 11's safe workflow is exactly this: state the task, ask for a plan rather than action, review and edit the proposed file operations, then approve. Granting full access up front, acting first and undoing later, or reorganizing then reporting are all unsafe, because AI-deleted files often skip the recycle bin and edits overwrite with no history.
*(Concept 11: AI desktop apps and permissions)*

---

### Q24. Naye AI desktop app ko kitni file access deni chahiye

**Q:** A user is deciding how much file access to give a new AI desktop app. Concept 11 gives two facts and a principle. Which option states them correctly?

- AI-deleted files always land safely in the recycle bin and edits always keep their history, so broad access on day one is genuinely low-risk
- The right permission scope is simply whatever happens to match how reputable and well-known the company that built the tool currently is
- **AI-deleted files often do NOT reach the recycle bin and edits overwrite with no history; scope tightly and grow scope with track record** ✅
- Once an app has worked correctly even one single time for you, it has effectively earned full disk access from that point onward

**Explanation:** Concept 11 states both hard facts, that deletions often bypass the recycle bin and that edits overwrite without history unless you use version control, and the principle that scope should grow with track record in your specific workflow, not with how reputable the vendor is and not after a single success.
*(Concept 11: AI desktop apps and permissions)*

---

### Q25. Ek hi tool par loyal rehna, kyunki woh kabhi leaderboard top par tha

**Q:** A worker uses one AI tool for every task and is loyal to it because it topped a leaderboard once. Concept 12 pushes back. What is the reasoning?

- They are basically right; once a model tops a public leaderboard it tends to stay the single best one for the foreseeable future
- **AI is jagged (different models lead different tasks) and the leader rotates every few months, so keep a few tabs open and re-check Arena** ✅
- They should instead just go and pick whichever single model happens to be cheapest right now, and then use only that one for everything
- They should pick whichever model is strongest at writing prose and then use that same one for everything, including images and code too

**Explanation:** Concept 12 says there is no single best model, because AI is jagged and the leader changes every few months, so the habits are to try the same prompt in two or three tools, not marry one of them, and check Arena monthly. Loyalty to a past leader, one cheap model for everything, or one writing model for everything are the failure modes.
*(Concept 12: Cost, speed, and which model to use when)*

---

### Q26. Text 50 baar iterate kar sakte hain, video nahi

**Q:** Concept 12 says you can iterate on text fifty times in an afternoon but cannot do that with video. What does this cost-and-speed difference imply for how you prompt?

- Avoid images and video entirely from now on, since honestly only text is really worth using for any kind of serious, careful work
- Iterate on video exactly as freely as you already do on text, since the cost difference between them is far too small to change behavior
- Always generate the expensive video first to lock that part in, and then go back and fill in all of the surrounding text afterward
- **Each image or video round is slow and costly, and images have no early-stop, so front-load the prompt, even using a text AI to write it** ✅

**Explanation:** Concept 12 draws the implication directly: cheap, fast text invites heavy iteration, while images, at several cents with no early-stop, and video, at minutes and dollars per round, reward front-loading the prompt, including using a text AI to write the image prompt. It does not say to avoid those modalities or to treat them as equally cheap.
*(Concept 12: Cost, speed, and which model to use when)*

---

### Q27. Do Claude models ek doosre ko check karein — kya yeh real cross-model verification hai?

**Q:** For a high-stakes memo, a user runs two Claude models against each other and calls it cross-model verification. Concept 13 says this misses the point. Why, and what is the correct setup?

- **Same-family models share priors and blind spots, so it is not real cross-checking; draw from different families and treat the score as progress** ✅
- Two models is simply far too few to rely on; you really must always use at least four of them before any answer can be properly trusted
- It is already correct exactly as it stands; any two models that check each other is plenty, no matter which family they each come from
- Cross-model checking is fairly pointless anyway, because all of the major models end up sharing essentially all of the same training data

**Explanation:** Concept 13 says two Claude models cross-checking is not real cross-model checking, because their priors are too similar; the value comes from genuinely different families catching each other's blind spots. It also warns the result is a progress signal, since models can share misconceptions, so humans still verify load-bearing facts. The number of models is not the point, and they do not all share the same data.
*(Concept 13: Models checking models)*

---

### Q28. Concept 6 ka sycophancy warning vs Concept 13 ka self-grading — contradiction?

**Q:** A reader objects: 'Concept 6 warned that a model grading its own work tends toward sycophancy, but Concept 13 tells me to make a model grade its own draft. Which is it?' How does Concept 13 resolve this?

- The two concepts flatly contradict one another, so one of the two of them must therefore simply be wrong and ought to be ignored here
- Self-grading is always perfectly safe to do; Concept 6's warning was only ever meant to apply when you grade other people's drafts
- **The difference is the rubric: 'is this good?' returns praise, but named criteria scored 1 to 10 force the model to name what is missing** ✅
- You should honestly never self-grade your own work at all; only genuine multi-model checking can ever produce a real, honest quality signal

**Explanation:** Concept 13 addresses this directly: without a rubric, self-grading collapses into 'great work', which is exactly Concept 6's closed loop, but named, scored criteria force the model to name what is missing, which turns the self-critique into a forcing function rather than flattery. The single-model loop is useful; the multi-model version is the high-stakes graduation. The concepts do not contradict, and self-grading is neither always safe nor always useless.
*(Concept 13: Models checking models)*

---

### Q29. Ek move jo poore course ke neeche chhupa hai

**Q:** The page claims almost every technique on it is one of two moves in disguise. A reader wants the single sentence to remember if they forget everything else. Which is it?

- Write noticeably longer prompts whenever the answer comes back shallow, and shorter prompts whenever it comes back far too verbose for you
- **Get the right context in and keep the wrong context out: attaching a file gets context in, and a fresh chat keeps the wrong context out** ✅
- Always reach straight for the single most capable model available and turn thinking mode on for absolutely every question that you ask it
- Trust the model's confidence as a guide, on the reasoning that a fluent, well-written, professional-sounding answer is usually a correct one

**Explanation:** The recap names one move underneath everything: get the right context in, keep the wrong context out. Briefing with files and constraints is getting context in; starting a new chat when the topic changes is keeping the wrong context out. The other options contradict Concept 4 (it is context, not length), Concept 12 (AI is jagged, no single best), and Concept 2 (confidence is not accuracy).
*(The one move underneath everything)*

---

### Q30. Manager AI ko 2022 wala "clever toy" samajhta hai

**Q:** A manager dismisses AI as the 'clever toy' they tried in 2022 and refuses to hand it anything hard. Based on the 'what changed' section and Concept 5, what is the corrective?

- The manager is basically right; nothing fundamental has actually changed about AI since 2022, only the marketing and the hype around it
- Only the user interface really changed since then; the underlying capability of the models is essentially identical to what it was in 2022
- The right response is honestly to just wait a few more years, until the tools finally settle down and stabilize, before trying them again
- **Context windows grew about a thousandfold, real reasoning and built-in search and code arrived, and the reliable-task length jumped to an hour** ✅

**Explanation:** The opening 'what changed' section lists the real shifts, with context windows up about a thousandfold, real reasoning, built-in search and code execution, multimodal, and desktop apps, and Concept 5's METR trajectory shows the reliable-task length climbing fast. The corrective is to re-test your assumptions, not to assume nothing changed or to keep waiting.
*(A short note on what changed since you last looked)*

---
[⬅ Practice Projects](06-practice-projects.md) · [⬆ Index](README.md)
