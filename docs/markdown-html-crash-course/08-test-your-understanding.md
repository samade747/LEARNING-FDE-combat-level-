# 08 — Test Your Understanding (Assessment)

> **Note:** Yeh file chapter ki numbering mein aage (08) rakhi gayi hai kyunke README pehle se files
> 02–07 (Parts 2-4, Recap, Practice Projects, Appendix) promise karti hai jo abhi disk par exist nahi
> karti — sirf `00-overview.md` aur `01-two-languages.md` likhi ja chuki hain. Woh ek alag, bara gap hai
> is quiz-addition task se; is file ka number is gap ke resolve hone tak stable rakha gaya hai.

Book ke live page par yeh section ek interactive `<Flashcards />` widget se shuru hota hai (auto-
generated, page ke apne key-terms se) — koi static text nahi, isliye copy karne layak content nahi hai;
live version [markdown-html-crash-course](https://agentfactory.panaversity.org/docs/markdown-html-crash-course#flashcards)
par dekho.

Uske baad **32-question assessment** aata hai (book ke apne `<Quiz>` component se, verbatim) — course
ke har concept (Part 1 se Part 4 tak, plus appendix aur recap) ka scenario-based test, sahi jawab ke
sath explanation bhi. Yeh poora quiz neeche hai, taake khud test kar sako ya apni class ko exam ki
tarah de sako. Content seedha book se hai (English mein — precision zaroori thi, translate nahi kiya).

---

### Q1. Tuition center owner ki ek lambi friendly paragraph — professional page vague ban gaya

**Q:** A tuition center owner types one long friendly paragraph asking for 'a professional page' with courses, fees, and a holiday notice buried mid-sentence. The draft demotes the notice to the footer yet sounds completely sure of itself. Per Concept 1, what actually went wrong?

- The model is too weak for layout work, so the only real fix is switching to a stronger model and resubmitting exactly the same friendly paragraph again.
- **The prose made the agent infer what mattered, and a wrong inference does not look wrong, it looks confident; explicit structure removes the guessing.** ✅
- The paragraph was too short for the agent to work with, and adding several more sentences of warm description would have fixed the draft.
- The agent ignored the request and reached for a generic landing page template, which is the default behavior whenever input arrives as prose.

**Explanation:** Concept 1 shows the same request twice to make this point: prose forces the agent to infer importance, and every inference is a place it can guess wrong while sounding sure. A stronger model still has to guess from the same vague input, more warm prose adds more to infer, and agents do not discard prose requests in favor of templates. The fix is structure: headings and bullets that declare what governs what.
*(Concept 1: Why agents need structure)*

---

### Q2. Sports day plan mein "heat" constraint bury ho gaya tha

**Q:** A school administrator asks an agent to 'draft the sports day plan, and keep the younger kids out of the afternoon heat.' The draft schedules under-8 races at 2 p.m. anyway. Per Concept 1, what fixed it on the next attempt?

- She switched to a model with a longer context window, which finally gave the agent enough room to take the heat concern into account.
- She repeated the heat concern three times across the paragraph, because agents weight a requirement by how many times the request mentions it.
- She asked the agent to read the request more carefully before drafting, which made it slow down and catch the buried constraint by itself.
- **She moved the constraint under a '## Hard constraints' heading as one bullet; its visibility in the structure changed, not its wording.** ✅

**Explanation:** In Concept 1's example the constraint was buried mid-sentence, so the agent weighted it as a preference; under its own heading as one bullet, the next draft complied perfectly. The constraint did not change, its visibility in the structure did. Context window size was never the issue, repetition is not how agents weight requirements, and 'read more carefully' leaves the structure that caused the miss untouched.
*(Concept 1: Why agents need structure)*

---

### Q3. Planning session ki spec HTML mein convert kar di — implementation session confuse ho gaya

**Q:** After reading the Anthropic piece, a reader converts everything to HTML, including the spec their planning session hands to an implementation session. The next session misreads it. What does Concept 2 say went wrong?

- **HTML's advantages are reader-side; to a downstream agent its tags and inline CSS are noise, so artifacts passed between agents stay Markdown.** ✅
- The HTML was simply malformed, and a well-formed page with valid tags would have been just as reliable a handoff format as Markdown.
- Specs must be written in plain prose with no markup at all, because any formatting confuses an agent that is trying to read instructions.
- The implementation session needed the spec as a published link rather than a file, since agents parse hosted pages more reliably than raw text.

**Explanation:** Concept 2's warning is that every HTML advantage (readable past 100 lines, navigable, shareable) is a reader-side advantage that vanishes when the reader has no eyes and no browser, so artifacts that move between agents stay Markdown. Well-formed markup is still extra tokens and lower parse reliability for an agent, prose without structure recreates the Concept 1 problem, and hosting a page does not make its tags easier to parse.
*(Concept 2: Markdown in, HTML out)*

---

### Q4. Deciding question: "who reads this output last?"

**Q:** An output will be processed by a verification agent today and might be read by your manager next week. The course's deciding question, who reads this output last, gives what answer?

- Produce HTML now, because a human will eventually read it and the agent can be told to ignore the tags while it runs verification.
- Produce both formats from the start, because keeping a parallel HTML and Markdown copy of every artifact is the standard professional habit.
- **Keep it Markdown: a human reads Markdown fine, an agent reads HTML poorly, and you can render to HTML when a person needs it.** ✅
- Produce plain text with no formatting of any kind, since that is the only format both an agent and a manager can read equally well.

**Explanation:** The Concept 2 rule: when an agent reads it now and a person reads it later, Markdown is the safer default, because a human handles Markdown well while an agent handles HTML poorly, and rendering to HTML later is cheap. Telling an agent to ignore tags still costs tokens and parse reliability, maintaining duplicate formats is never suggested, and unformatted text throws away the structure Concept 1 says agents need.
*(Concept 2: Markdown in, HTML out)*

---

### Q5. Heading level skip ho gaya, aur beech mein doosra `#` title aa gaya

**Q:** A spec jumps straight from its '#' title to '###' subsections, and a second '#' title appears halfway down to introduce the report section. What does Concept 3 predict?

- Nothing fails, because heading levels are purely visual decoration and agents read only the words inside each heading, never the depth.
- **The skipped level can misattach subsections to the wrong parent, and the second title reads as two documents fused into one file.** ✅
- The agent will refuse to process the document until the heading hierarchy validates, the way a compiler rejects a program with syntax errors.
- The agent silently rewrites the heading tree into a corrected version before it reads anything, so the structure you actually typed never reaches the model.

**Explanation:** Concept 3's rules table names both failures: never skip levels, because a broken tree lets the agent misattach a subsection to the wrong parent, and one '#' title per document, because two titles mean two documents fused together that the agent may treat as separate tasks. Hierarchy is meaning to an agent, not decoration, and nothing validates or quietly repairs your tree for you.
*(Concept 3: Headings, tell the AI what matters most)*

---

### Q6. "## Budget" vs "## Budget: PKR 50,000 hard ceiling"

**Q:** Two specs differ in one line: one heading says '## Budget' and the other says '## Budget: PKR 50,000 hard ceiling'. Why does Concept 3 prefer the second?

- **A heading can be a claim that carries the constraint itself, so the limit governs everything beneath it rather than hiding in prose.** ✅
- Longer headings always rank higher in the agent's attention, so padding every heading with several extra words reliably makes its whole section more important.
- Numbers are only machine-readable when they appear inside a heading, because agents tend to skip numerals that appear in ordinary body sentences.
- The second version renders in a larger font in most tools, and visual size is what tells an agent which sections matter the most.

**Explanation:** Concept 3's third rule is to make headings claims, not labels: '## Budget: PKR 50,000 hard ceiling' carries the constraint in the tree itself, where everything beneath it inherits it. Heading length and rendered font size are not the mechanism, and agents read numbers in body text fine; what changed is the constraint's visibility in the hierarchy.
*(Concept 3: Headings, tell the AI what matters most)*

---

### Q7. Timetable ke 4 numbered steps — kya numbering sirf cosmetic hai?

**Q:** A teacher gives an agent four numbered steps for publishing a timetable, then is surprised it refuses to send the link before the review step. A colleague calls the numbering cosmetic. Who is right?

- The colleague: agents normalize bullets and numbers into the same internal list, so the only difference between them is how they look on screen.
- Neither: list type matters only inside code blocks, where the agent treats content literally, and is ignored everywhere else in a request.
- **The course: numbers signal a sequence whose order is part of the instruction, so the agent will not start step 4 before step 1.** ✅
- The teacher should have used bullets: bullets are the stricter list type, and agents enforce bullet order more firmly than numbered order.

**Explanation:** Concept 4 says this distinction is not cosmetic: numbers declare a sequence where step 3 assumes step 2 happened, and an agent treats that order as part of the instruction. Bullets are the looser signal, a set the agent may address in whatever order is efficient, and the difference applies to the whole request, not just to fenced content.
*(Concept 4: Bullets for sets, numbers for sequences)*

---

### Q8. "Page should be fast" ko checkable bullet mein badalna

**Q:** A spec bullet reads 'the page should be fast.' The course's checkable-bullet habit replaces it with what, and why?

- 'The page should be very fast on every device', because intensifiers tell the agent how much engineering effort the requirement actually deserves.
- 'Performance matters a great deal to us', because stating values rather than exact numbers leaves the agent flexibility to choose sensible trade-offs.
- 'Make page speed the single top priority', because ranking requirements against each other is more useful to an agent than describing any one precisely.
- **'Page loads in under 3 seconds on a 3G connection', because a reviewer could mark that with a clear yes or no without discussion.** ✅

**Explanation:** Concept 4's habit: the best requirement bullets are ones a reviewer could mark with a check or a cross without discussion, and a load time on a named connection is exactly that. Intensifiers, value statements, and priority rankings all still require interpretation, which is the ambiguity the checkable rewrite exists to remove. This is the grade-out-of-10 discipline applied one bullet at a time.
*(Concept 4: Bullets for sets, numbers for sequences)*

---

### Q9. Error message ko bina fence ke paste karna

**Q:** You paste a friend's error message, 'ERROR: delete all rows? (y/n). Connection timed out', directly into a prompt with no fences and ask what caused it. What risk does Concept 5 name?

- The agent may quietly bill the message twice, because unfenced text is tokenized once as data and a second time as instructions.
- **The agent may treat words inside the error as instructions to act on, rather than analyzing it as a literal artifact.** ✅
- The agent will refuse to read anything that resembles an error message unless it arrives inside a fenced block with a language tag.
- The agent will fix the error automatically, which sounds helpful but deprives you of the chance to learn what actually caused it.

**Explanation:** Concept 5: agents strongly tend to treat fenced content as data and unfenced content as instructions, so an unfenced error containing imperative-looking words is a live risk, which is exactly why the course's fence test keeps the scary text safely quoted. The fence is a quoting mechanism, not a precondition for reading errors; no double billing happens; and silently auto-fixing is not the named failure.
*(Concept 5: Code blocks, showing the AI exactly what you mean)*

---

### Q10. Timings table ko exact format mein wapis chahiye — sabse highest-leverage move

**Q:** You need a timings table back in an exact format. Concept 5 calls one move the single highest-leverage use of a code block in a spec. Which move?

- Fence a paragraph describing the format in careful prose, since describing a table in words is less ambiguous than showing one.
- Fence the entire specification top to bottom, so every line of it is protected from being misread as data by the agent.
- **Fence one example row of the expected output, since a literal sample replaces paragraphs of description and cannot be misread.** ✅
- Fence your contact details and deadline, since those are the facts whose exact reproduction matters most in the final deliverable.

**Explanation:** Concept 5 says to fence your expected output: one example row replaces three paragraphs of format description, and the agent cannot misread it. Fencing everything inverts the mechanism, because fences mark literal data rather than instructions; describing a format in prose is what the example exists to replace; and contact details are ordinary context, not format-critical output.
*(Concept 5: Code blocks, showing the AI exactly what you mean)*

---

### Q11. Fee policy summarize karna vs policy page link karna

**Q:** A spec needs the school's fee policy. One author summarizes the policy from memory; another links the policy page and writes 'fees must match this.' Why does Concept 6 prefer the link?

- Links make the spec shorter, and shorter specs are better because agents lose accuracy steadily with every extra paragraph of input.
- Links prove to the agent that the author did real research, which raises how much weight it gives the rest of the specification.
- Summaries are simply forbidden in specifications, because the skeleton's Context section accepts only links and file attachments, never paraphrased facts from memory.
- **A link is context the agent can fetch, so a possibly wrong summary from memory is replaced by the source of truth itself.** ✅

**Explanation:** Concept 6: modern agents follow links, so linking the policy page moves a paragraph of possibly wrong context out of your head and replaces it with the source of truth. That is the get-the-right-context-in move expressed as syntax. Shortness and looking diligent are not the mechanism, and summarized facts are allowed in a Context section; they are just riskier than the source.
*(Concept 6: Links and images, pointing at the world)*

---

### Q12. Mockup screenshot ke brackets mein alt text kis liye hai

**Q:** Your spec embeds a mockup screenshot. Per Concept 6, what is the alt text in the brackets actually for?

- **It is what agents, screen readers, and search engines read when they cannot see the image, your chance to flag what matters.** ✅
- It is the caption rendered in small text underneath the mockup, so it should carry your branding and the document's version number.
- It is the filename the agent uses when saving its own copy, so it should stay short and contain no spaces.
- It is decorative metadata that no software actually reads anymore, kept in the syntax only for compatibility with very old tools.

**Explanation:** Concept 6 says the description in the brackets is what an agent, a screen reader, and a search engine read when they cannot see the image, which makes it your chance to point at what the agent should notice in a mockup. It is not a rendered caption, not a filename, and far from dead syntax; it is the image's text interface.
*(Concept 6: Links and images, pointing at the world)*

---

### Q13. Login system + payments — 14 extra features requested hi nahi thin

**Q:** An agent returns your tuition page with a login system, online payments, and fourteen extra features burying the three you wanted. Which missing spec section does Concept 7 blame?

- Expected output, because a fenced sample of the final page would have shown the agent exactly how many features were wanted.
- **Out of scope, because stating what you are explicitly not asking for is the section that kills enthusiastic over-delivery.** ✅
- Context, because an agent that had been given more background links would have inferred the project's true boundaries on its own.
- Goal, because a longer goal paragraph naming every stakeholder would have constrained the agent's enthusiasm about extra features.

**Explanation:** Concept 7 says Out of scope kills the agent's most common failure, enthusiastic over-delivery: the login system you never asked for, the seventeen features that bury the three you wanted. Expected output targets the second most common failure, format drift, not feature creep; and more context links or a longer goal never state the negative, which prose almost never does on its own.
*(Concept 7: Your first complete specification)*

---

### Q14. Pehla spec likh kar seedha build karne bhej diya — kya move miss hui

**Q:** A reader writes their first spec and immediately hands it to an agent to build. The course says they skipped the move that separates a spec from a wish. What is it?

- **Asking the agent to attack the spec first: list ambiguities and missing constraints, grade it out of 10, and name the best single fix.** ✅
- Having a second human read the whole spec aloud to you, because only people can catch the kinds of ambiguity that matter in real projects.
- Translating the whole spec into HTML before building, because agents follow visually designed specifications more faithfully than they follow plain Markdown ones.
- Rewriting the spec three separate times from scratch, because sheer repetition is what gradually surfaces all the constraints you forgot to state.

**Explanation:** Concept 7's validation prompt is the move: do not build yet, list every ambiguity, list every missing constraint, grade the spec out of 10, and name the single change that raises the grade most. Two or three rounds typically lift a spec from 6 to 9, the cheapest quality improvement in agentic work. Specs stay in Markdown, and neither a read-aloud nor blind rewriting is the course's loop.
*(Concept 7: Your first complete specification)*

---

### Q15. Nine-screen Markdown report vs 4-minute HTML+charts version

**Q:** A principal gets a nine-screen Markdown report on admission trends and reads two screens. Re-prompted as HTML with charts and a findings table, she absorbs it in four minutes and forwards the link. What is the course's argument here?

- HTML compresses information so the report became objectively much shorter, and shorter documents are the ones busy professionals actually finish reading.
- The first report failed because Markdown cannot represent numeric data in tables at all, so the figures were simply invisible until HTML arrived.
- Boards expect polished documents, so the gain was mostly social polish: the same unread report, now dressed well enough to forward.
- **Read versus skimmed is the entire argument: the same information became something she actually read, navigated, and could share as a link.** ✅

**Explanation:** Concept 8 frames the difference as read versus skimmed and says that difference is the entire argument: density, navigability, and shareability turned nine skimmed screens into four absorbed minutes. Markdown renders tables fine, so the data was never invisible; the information did not shrink; and the forwarding worked because a link opens for anyone, not because of social polish.
*(Concept 8: Why ask for HTML at all)*

---

### Q16. Parents ka slow-data phone par interactive report load hi nahi hota

**Q:** You publish an interactive report for parents who will open it on phones with slow data, and several say it never loads. Which fix does the course's caveat prescribe?

- Switch the report back to a Markdown artifact, since the feeds rule says phone readers should always receive plain text instead of pages.
- Publish the page on a faster rung of the hosting ladder, since load time is a property of the host, not the file.
- **Put the budget in the brief: lightweight, single file, no external fonts or libraries, under 200 KB, so the agent inlines what it needs.** ✅
- Split the report into a dozen separate small pages connected by navigation links, since no single self-contained HTML file can ever be made small enough.

**Explanation:** Concept 8's caveat names this exact cost: external fonts, large images, and big libraries can balloon an artifact to several megabytes, a real problem on slow mobile data, and the fix is to say so in the brief with a size budget. The feeds rule is about post bodies, not browsers; hosting does not shrink the file; and the appendix's 6 KB page proves one light self-contained file is achievable.
*(Concept 8: Why ask for HTML at all)*

---

### Q17. Vague "make an HTML report" vs named reader + components + reading mode

**Q:** Two people request an HTML report from the same data. One writes 'make an HTML report about my sales data'; the other names two co-founders reading once on laptops, the exact components, and a three-screen limit. Why does the second win, per Concept 9?

- It is longer, and longer prompts reliably produce better HTML because the agent allocates effort in proportion to the words you type.
- **It supplies the brief: reader, components, and reading mode are what agents cannot guess, while rendering them is what agents do well.** ✅
- It includes a hard number, and a quantified constraint automatically switches the agent's layout engine into its more capable rendering mode.
- It avoids the word 'report', which agents associate with plain text documents and which therefore quietly suppresses their richer visual output styles.

**Explanation:** Concept 9 says the trigger is trivial and the brief is everything: name the reader, the components, the interaction, and the reading mode, because agents are excellent at rendering components and mediocre at guessing which ones you wanted. Length alone is not the mechanism, no quantified constraint switches the agent into a special mode, and the word 'report' suppresses nothing.
*(Concept 9: You don't write HTML; you prompt for it)*

---

### Q18. Impressive artifact aya hai — forward karne se pehle 4 sawal se grade karna

**Q:** An artifact comes back and looks impressive. Before forwarding it, Concept 9 grades it with four questions out of 10 each. Which set is it?

- It asks whether the color palette is tasteful, the font feels modern, the animation runs smoothly, and the overall finish looks like professional design work.
- It asks whether the page loaded quickly, the HTML validates against the official standard, an accessibility audit passes, and the source code is commented clearly.
- **It asks whether every fact is represented, the key point findable in 10 seconds, the page readable on a phone, and the link forwardable.** ✅
- It asks whether the artifact is longer than the Markdown version, includes at least one chart, uses a tabbed layout, and needed under three regenerations.

**Explanation:** Concept 9's rubric grades fidelity and usefulness, not polish: every fact from the source represented, the most important thing findable in 10 seconds, readable on a phone, and a link you would actually forward. Anything under 9, name the gap and regenerate, because iterating an artifact is cheap. Visual taste, validator output, and raw length are not what the rubric measures.
*(Concept 9: You don't write HTML; you prompt for it)*

---

### Q19. Draggable Now/Next/Later cards — konsa artifact rakhte hain?

**Q:** You ask for draggable Now / Next / Later cards to prioritize thirty items, drag for ten minutes, and copy the export back. Which artifact does Concept 10 say you keep?

- The HTML editor, carefully saved and versioned, because a working interface is far more valuable than any one text snapshot of it.
- Both artifacts equally, archived together side by side, because the interface and its export only make sense as a matched, inseparable pair.
- Neither one, because a throwaway exercise is purely for thinking and produces nothing worth carrying into the next session at all.
- **The Markdown the export button produced: the interface is the throwaway, and the text it exports is what continues the conversation.** ✅

**Explanation:** Pattern 5's point: the HTML editor is the throwaway and the Markdown it exports is the thing you keep, the agent to agent rule in action, interface discarded, text preserved. The export button is what makes the pattern work because it closes the loop back to text. Keeping or archiving the editor inverts the rule, and the exercise absolutely produces a durable output: the prioritized list.
*(Concept 10: The five HTML patterns)*

---

### Q20. Project structure decide karne ke liye HTML se pehle kya mangna hai

**Q:** You are deciding how to structure a project and want HTML to help. What does Pattern 1 have you ask for first?

- **A side-by-side grid of five distinctly different approaches, each card labeled with its trade-off, with no recommendation yet.** ✅
- A single deep page on the agent's preferred approach, since exploring more than one option mostly wastes tokens and your attention.
- An implementation plan straight away, since the fastest path to evaluating a structure is watching the agent begin building it.
- A long Markdown essay weighing each approach in prose, since comparison is an argument and arguments are clearest as prose.

**Explanation:** Pattern 1 replaces one linear plan with a web of small pages, starting with an options-comparison grid you can look at before anything is recommended or executed: five approaches, each labeled with the trade-off it makes. You approve direction visually first; the deep page on the winner and the implementation plan come after. A prose essay is exactly the wall of text the pattern exists to replace.
*(Concept 10: The five HTML patterns)*

---

### Q21. Messy notes — 11 files, 3 folders — chat ya terminal?

**Q:** Your 'messy notes' turn out to be eleven files across three folders, and you want spec.md and report.html as real files in version control. Which motion fits, and why?

- Chat, because pasting the files into Claude.ai one at a time keeps you closer to the conversation while it assembles the spec.
- Chat, but with the notes condensed by hand into one paragraph first, since summarizing context yourself is the power user habit.
- **Terminal, because Claude Code or OpenCode gathers its own context from the folder and writes real files onto your disk.** ✅
- Desktop only, because Cowork and OpenWork are the only surfaces in the book that are permitted to create files on disk.

**Explanation:** Concept 14's choosing table sends context that lives across many files to the terminal motion: the agent gathers its own context, every file in the folder rather than what you remembered to paste, and the outputs are real files, spec.md into version control and report.html ready to share. Chat strains exactly here because it sees only what you paste, and terminal surfaces write files too, so desktop is not the only file-writing option.
*(Concept 14: The three motions)*

---

### Q22. Cowork/OpenWork ke prompt mein ek non-negotiable line

**Q:** Moving the exercise to Cowork or OpenWork, the course adds one non-negotiable line to the prompt. Which line, and what makes it non-negotiable there?

- 'Use your most capable model', because desktop apps default to smaller models and the exercise needs the strongest one available to work.
- **'Propose a plan first; write nothing until I approve', because once an agent can touch your files, you review before it acts.** ✅
- 'Stay inside this one folder forever', because desktop agents are otherwise guaranteed to scan and index the entire drive by default.
- 'Reply only in Markdown', because desktop surfaces cannot display HTML and silently discard any rich output an agent tries to produce.

**Explanation:** Motion 3's prompt adds the plan-first wording: propose a plan, and do not write anything until I approve. The course calls this non-negotiable the moment an agent can touch your files, the permission discipline carried over from AI Prompting in 2026. Model choice is not the addition, desktop agents do not index your whole drive by default, and the exercise's desktop output is an HTML report, so banning rich output is backwards.
*(Concept 14: The three motions)*

---

### Q23. Styled HTML announcement Facebook post body mein paste kar diya

**Q:** Proud of a styled HTML announcement, a teacher pastes the raw HTML into a Facebook post body. What does the feeds section say happens, and what should the body have been?

- Facebook renders the page inline exactly as designed, so the only real concern is whether the fonts load inside the feed quickly.
- Facebook converts the markup into its own native formatting automatically, so most of the styling survives in a simplified but acceptable feed form.
- The post is rejected by the platform's filters as suspicious code, so the safe move is posting a screenshot of the rendered page instead.
- **It lands as a wall of angle brackets, the one always-wrong move; the body should be plain text tuned to the platform.** ✅

**Explanation:** The feeds section is blunt: pasting raw HTML as a post body is the one move that is always wrong, because a feed renders its own interface and pours your content into its box, so the markup lands as a wall of angle brackets. Facebook neither renders nor converts your markup, and the post is not filtered out; it simply publishes as unreadable text. The body belongs in plain text tuned to the platform.
*(Concept 11: When the destination is a feed, not a browser)*

---

### Q24. WhatsApp/LinkedIn par share karna hai — HTML skill kahan kaam aati hai

**Q:** You will share a course page link on WhatsApp and LinkedIn, and you want the post itself to look good. Where does the feeds section say your HTML skill still pays off?

- **In the page being linked: brief in Open Graph tags so the platform's scraped preview card, the most-seen part of the post, looks designed.** ✅
- In the message text itself: WhatsApp renders full HTML inside chat bubbles, so a styled body tag makes the message stand out beautifully.
- Nowhere at all: once a social feed is the destination, HTML knowledge becomes entirely irrelevant and only sharp copywriting decides how the post performs.
- In LinkedIn's post body: LinkedIn quietly honors Markdown headings and bold text, so structured markup survives there even though raw HTML does not.

**Explanation:** The feeds section moves HTML to two side channels: the linked page, whose Open Graph tags (og:title, og:description, og:image) the platform scrapes to build the preview card, usually the most-seen part of the post, and an image card rendered from HTML to a PNG. WhatsApp renders no HTML in messages, LinkedIn does not even honor Markdown bold, and the skill is far from irrelevant; it just leaves the post body.
*(Concept 11: When the destination is a feed, not a browser)*

---

### Q25. Coaching academy brochure — Claude.ai one-click publish sahi rung hai?

**Q:** A coaching academy's brochure page needs to stay up for years on its own domain, and the owner publishes it with Claude.ai's one-click publish because it was easiest. What does the ladder say?

- The right call: every rung of the ladder is equivalent in durability, and the publish control is simply the cheapest of the equal options.
- **The wrong rung: Claude.ai publish is for 'seen, not owned'; a durable page on your own domain wants GitHub Pages or Netlify.** ✅
- The wrong rung, but only barely: a GitHub Gist's raw link was the intended home for any page meant to stay up over multiple years.
- The right call for now, because the ladder says to start every project at the top rung and migrate downward only after the link breaks.

**Explanation:** The ladder's advice is to pick the lowest rung that meets the need, and this need (durable, own domain, returning audience) is what GitHub Pages or Netlify with a custom domain exist for. Claude.ai publish trades ownership for speed: the page lives on Anthropic's infrastructure and the URL is theirs. A raw Gist link serves plain text rather than a rendered page, and no migrate-after-breakage rule exists.
*(Concept 12: Publishing, from artifact to link)*

---

### Q26. Git touch nahi karna, phir bhi durable URL chahiye — konsa rung?

**Q:** A non-developer wants a real, durable URL for one HTML file, refuses to touch Git, and wants the least friction possible. Which rung does the ladder point to?

- GitHub Pages: a repository, a settings toggle, and a first build remain the gentlest available path for someone who refuses Git.
- A raw GitHub Gist link shared directly, since raw links render gists as styled pages without any account or renderer in between.
- Claude.ai publish, since it is the only rung that produces a durable URL while also requiring no setup of any kind from the author.
- **Netlify Drop: make a free account, drag the file onto the page, and get a live URL in seconds, no repo and no Git.** ✅

**Explanation:** The ladder describes Netlify's Drop flow as exactly this path: a free account needing only an email, drag an HTML file onto the page, live URL in seconds, usually the gentlest route to a real durable URL without touching Git. GitHub Pages requires a repo and suits people comfortable in Git; a raw Gist link serves as plain text, the section's one named gotcha; and Claude.ai publish is the rung you do not own.
*(Concept 12: Publishing, from artifact to link)*

---

### Q27. CA ke 3 readers — model, memo, engagement letter — teenon ke liye format

**Q:** A chartered accountant must get three things to three readers: the working year-end model to an audit partner who will change assumptions, a memo the directors will only read, and a signed engagement letter that must be filed unchanged. Per Concept 13, which set of formats fits?

- Send all three as PDF, because PDF is the universal professional format and one consistent format keeps the client's records tidy.
- **XLSX for the model the partner will recalculate, an HTML link for the read-only memo, and PDF for the engagement letter that must not change.** ✅
- DOCX for all three, because Word opens and edits everywhere, which gives each reader the best chance of being able to use the file.
- An HTML link for all three, because a link beats an attachment every time and nobody has to install anything to open it.

**Explanation:** Concept 13 chooses the container by what the reader will do: the partner edits and recalculates, so XLSX (the workbook is the HTML of data); the directors only read, so a link still wins; the engagement letter is signed and filed and must never change, so PDF, whose uneditability is the feature. One format for all three ignores the verb that distinguishes them: PDF-for-all freezes the model the partner needs to edit, DOCX-for-all forces a spreadsheet into prose, and a link is wrong for a document that must be signed and filed.
*(Concept 13: When the destination is a document, not a browser)*

---

### Q28. Markdown/HTML asymmetry "numbers mein" — CSV vs XLSX

**Q:** Concept 13 says the same Markdown-in/HTML-out asymmetry shows up again 'expressed in numbers.' Which mapping does it draw between data formats?

- CSV is the HTML of data and XLSX is the Markdown of data, because a spreadsheet's formulas are the precise, machine-first layer.
- Both CSV and XLSX are machine formats, so the asymmetry does not apply to data at all; you choose between them purely on file size.
- **CSV is the Markdown of data (plain text, machine-first, handed tool to tool), and the workbook is the HTML of data (formatting, formulas, charts, for a human to read and edit).** ✅
- PDF is the Markdown of data and CSV is the HTML of data, because a PDF preserves the exact layout a downstream tool needs in order to parse the numbers.

**Explanation:** Concept 13 maps CSV onto Markdown's role, plain text, machine-first, the format one tool hands the next and that you paste back to an agent, and the workbook (XLSX, or XLSB for heavy models) onto HTML's role, formatting, formulas, and charts, the surface a human opens to read and edit. The same question decides it: a machine reads it next, ship CSV; a person opens it in Excel, ship the workbook. The asymmetry is not suspended for data, and both PDF mappings invert the roles.
*(Concept 13: When the destination is a document, not a browser)*

---

### Q29. Appendix ke 3 closing moves — poore course ka compression

**Q:** After the appendix's tuition page, the course closes with three moves that compress the whole crash course. Which sequence is it?

- Read the HTML line by line, memorize its CSS section, and retype the page from memory to prove the structure truly sank in.
- Validate the spec, regenerate the page twice more, and pick whichever of the three generated versions reads best on your laptop.
- **Open the saved file on your phone, change it by prompting rather than typing, and publish it through a rung of the ladder.** ✅
- Screenshot the page for your records, post the screenshot to a feed, and archive the original spec in case anyone ever asks for it.

**Explanation:** The appendix ends with exactly three moves: open it (get the page onto your phone, notice you read it rather than skimmed it), change it by prompting, not typing (add a course row and a dismissible banner without touching a tag), and publish it (any rung of the ladder, then watch the preview card render). The appendix explicitly says not to read the HTML line by line; scrolling past it is the lesson.
*(Appendix: One spec, the HTML it became)*

---

### Q30. Tuition page "complete" hai — ek honest gap link preview mein baaqi hai

**Q:** The appendix calls its tuition page complete except for one honest gap in the link preview. What is the gap, and when can it be closed?

- **A preview image needs og:image pointing at a hosted picture, which a self-contained file lacks until the page is published somewhere.** ✅
- The page is missing its og:title and og:description, which cannot be written into a self-contained file and must be injected by the host.
- WhatsApp ignores Open Graph tags entirely, so no preview card of any kind can exist for this page until Facebook shares it first.
- The preview card requires a paid developer account on each platform, which is why the spec listed Open Graph as out of scope.

**Explanation:** The appendix names one honest gap: a preview image needs og:image pointing at a hosted picture, which a single self-contained file does not have until you publish the page somewhere, so you add the tag once the page has a home. og:title and og:description are already inline in the file, so self-contained files carry them fine; WhatsApp does scrape Open Graph for previews; and the spec listed payments and login as out of scope, not Open Graph, which was a hard constraint.
*(Appendix: One spec, the HTML it became)*

---

### Q31. Ek sentence jo poori course compress karta hai

**Q:** The course asks you to keep exactly one sentence if you forget everything else. Which sentence is it?

- Always answer in HTML and always ask in plain prose, because structure slows you down more than ambiguity ever will in practice.
- **Write Markdown precise enough for a machine; demand HTML rich enough for a human. Every format decision in the course unfolds from it.** ✅
- Learn enough HTML to stop depending on agents, because briefing and judging are temporary skills on the way to writing tags yourself.
- Specs are paperwork that merely precedes the real work, so spend as little time on them as possible and let regeneration absorb the errors.

**Explanation:** The recap's one sentence: write Markdown precise enough for a machine; demand HTML rich enough for a human. It compresses the asymmetry (Concept 2), the writing skills of Part 2, and the briefing skills of Part 3 into a single rule. The others invert the course: prose-in maximizes ambiguity, the FAQ says the skill is briefing and judging rather than typing tags, and Concept 7 insists the spec is the deliverable, not paperwork.
*(A short recap before you try the prompts)*

---

### Q32. "Thoda warm, nahi, less orange" — color preference kaise express karein

**Q:** A preference like 'a bit warmer, no, less orange' is miserable to put into words. Which move does the course recommend, and what closes the loop back to the agent?

- Asking the agent to generate forty candidate palettes as a numbered Markdown list, then replying with the number of the one you like most.
- Uploading a photo of a color you like so the agent can estimate the values, then pasting those values into a fresh chat.
- **Asking for controls, a slider for the value you cannot articulate, plus a copy-as-text button whose export you paste back to the agent.** ✅
- Granting the agent screen access so it can watch you point at colors on screen, then letting it write the values into the file directly.

**Explanation:** Concept 8's copy back loop: some preferences are miserable to express in words, so ask the agent to build controls for them plus a copy button, and 'make it warmer, no, less orange' becomes thirty seconds of dragging a slider and one paste. The export is what closes the loop, because the agent receives your choice precisely as text. Numbered lists keep you typing descriptions, and neither photo estimation nor screen access is the course's pattern.
*(Concept 8: Why ask for HTML at all)*

---
[⬆ Index](README.md)
