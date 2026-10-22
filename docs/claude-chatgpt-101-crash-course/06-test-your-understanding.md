# 06 — Test Your Understanding (12-Question Assessment)

Yeh scenarios tumhe kisi aur ke workspace mein daal dete hain, jahan ek decision already wait kar
rahi hai. **Pattern se jawab do, product-naam se nahi** — notice karo har sawal asal mein kaunsa
concept test kar raha hai. Book ke apne `<Quiz>` block se verbatim (English, precision ke liye).
Answer key `quiz.md` mein.

1. **Q:** A consultant has used ChatGPT daily for a year and refuses to open Claude, on the grounds
   that switching would mean learning a whole second product. What does the course say is wrong with
   that reasoning?
   - Most of what he learned is actually the discipline, and it transfers; the new part is only
     where a second product keeps its switches
   - Claude is the stronger product for consulting work, so the year he spent in the other tool was
     mostly wasted effort he could have avoided
   - Running one task in two assistants is the only reliable way to detect a hallucination, since two
     models rarely invent the same wrong fact
   - Vendors change their interfaces so often that loyalty to any single product is guaranteed to
     leave him stranded within a year or two
   *(Source: 1. Two cockpits, one discipline)*

2. **Q:** An analyst always leaves the assistant on its fastest setting, and complains that it keeps
   making arithmetic slips in a multi-step margin calculation. What is the course's diagnosis?
   - Arithmetic is the one job that no tier handles reliably, so the calculation should be moved to a
     spreadsheet and out of the assistant entirely
   - He picked the tier by habit rather than by task, and multi-step reasoning is exactly the kind of
     work the thinking tier exists to absorb
   - The model names on his account changed in a recent release, so the setting he believes is fast
     is now pointing at something different
   - His context is too thin, and attaching the underlying figures as a file would let the fast tier
     complete the same work without slipping
   *(Source: 2. Models and thinking modes)*

3. **Q:** Two colleagues send the same eight words, 'Summarize this contract and flag unusual terms.'
   One gets a useful answer and one gets a vague one. The prompts are identical. What most likely
   explains the gap?
   - The useful answer came from the thinking tier, because flagging unusual terms is comparison work
     rather than routine summarizing work
   - One of them had standing instructions saved that told the assistant to lead with the answer and
     to write for a business audience
   - One of them attached the contract, so the assistant could read the document instead of guessing
     what such a contract usually says
   - The vague answer came from a chat that had run long enough that earlier context had been pushed
     out of the conversation window
   *(Source: 3. Context you attach)*

4. **Q:** A freelancer asks whether she should create a project for a one-hour job she will never
   repeat: rewriting a single bio for a conference program. What does the course's test say?
   - Yes, because a project is the only place where uploaded files stay available across more than
     one conversation with the assistant
   - Yes, because starting a project now costs nothing and gives her somewhere to keep the work if
     the client ever comes back with more
   - No, because projects are a paid-plan feature and a single short rewrite is not enough work to
     justify upgrading an account for it
   - No, because the test is repetition, and she has not explained that background or uploaded the
     very same file three separate times
   *(Source: 4. Projects: a room for one stream of work)*

5. **Q:** A researcher keeps two clients in two projects and is worried that details from one will
   surface in the other's work. Which product behavior addresses that specific worry?
   - ChatGPT's project-only memory, which walls off the project so that memories from outside it are
     not referenced in any of its chats
   - Claude's retrieval mode, which searches project knowledge rather than loading all of it once the
     material grows past the context window
   - Standing instructions, which can be written to tell the assistant never to mention one client
     while it is working on the other client
   - An incognito or temporary chat, which keeps the conversation out of history so nothing from it
     can reach the other project later
   *(Source: 4. Projects: a room for one stream of work)*

6. **Q:** A manager writes 'I am currently negotiating the Henderson renewal' into his custom
   instructions, and three months later the assistant is still bringing up a deal that closed long
   ago. Which mistake does the course name?
   - He should have used an incognito chat, because commercially sensitive negotiations do not belong
     in any stored context at all
   - He put evolving context where stable rules belong: a live negotiation is what memory is for, and
     instructions are for what stays true
   - He should have created a project for the renewal, because standing instructions cannot hold
     files and a negotiation always involves documents
   - He never reviewed his stored context, and the course's rule is to wipe stored memory fully clean
     at the start of every quarter
   *(Source: 5. Memory and standing instructions)*

7. **Q:** A lawyer uses an incognito chat to think through a sensitive matter, and tells a colleague
   the conversation 'does not exist anywhere.' How should the course correct her?
   - Incognito applies only to memory and not to history, so the conversation is still listed in her
     sidebar where anyone at her screen could open it
   - She is right about the vendor but wrong about her firm, because an organization's retention
     policy is the only thing that ever keeps such a chat
   - It is kept out of history and out of memory, but the vendor still retains a copy temporarily, so
     it is memory-free rather than trace-free
   - Incognito chats can be converted back into normal chats later, so the content can re-enter both
     history and memory without warning
   *(Source: 5. Memory and standing instructions)*

8. **Q:** A reader follows a 2025 tutorial that tells him to open canvas in ChatGPT to edit a long
   document, and cannot find the button anywhere. What is actually going on?
   - Canvas is now a paid-plan feature, so the button is hidden on his account until he upgrades to a
     plan that includes the editing panel
   - Canvas only appears once a response passes a length threshold, so a short draft will never
     trigger the side panel the tutorial describes
   - He is looking in the wrong product, since the side-by-side editing surface the tutorial
     describes has always belonged to Claude artifacts
   - OpenAI retired canvas on its current models and moved that same work into the thread as inline
     writing blocks and code blocks instead
   *(Source: 6. Artifacts and writing blocks)*

9. **Q:** An accountant has a project holding one client's filings and a written method for preparing
   their year-end pack. She wants the method applied to a second client. What does the course's split
   tell her?
   - The method belongs in a standalone skill, because a skill carries the how and can be redirected
     at whichever project supplies the what
   - She should duplicate the project, because the method and the filings were built together and
     separating them will break the instructions
   - She should build a custom GPT, because a separately configured assistant is the only way to
     reuse a method across two different clients
   - She should install a plugin, because reusing one method across two clients is precisely the job
     that a bundled package is designed for
   *(Source: 7. Skills and plugins)*

10. **Q:** An operations lead hears MCP described as USB-C for AI tools and concludes that connecting
    his company's ticketing system is a routine, low-stakes step. Where does the shorthand mislead
    him?
    - MCP is a developer standard rather than a user-facing one, so a business user cannot connect a
      system without engineering help anyway
    - A standard plug makes connecting easy, but it is still a decision about what the assistant may
      read and do, which is not standardized
    - USB-C describes Claude connectors accurately and ChatGPT apps only loosely, since the two
      ecosystems implement the protocol in different ways
    - Ticketing systems are the one category the standard does not cover well, so the comparison
      holds for storage and calendars but not for tickets
    *(Source: 8. Connectors, apps, and routing the question)*

11. **Q:** Someone starts a research run to find out which of two suppliers currently has the shorter
    published lead time, then waits several minutes for a cited report. What does the course call
    this?
    - A reasonable use of research, because a cited report is the only defensible evidence to bring
      to a supplier decision of any size
    - A permission problem, because supplier lead times usually sit behind a connected system rather
      than on the open web where research looks
    - Misrouting, and the most common daily waste in both cockpits, since one current fact is what
      the web search toggle answers in seconds
    - A context problem, because the assistant was never told which two suppliers to compare or where
      their published lead times are listed
    *(Source: 8. Connectors, apps, and routing the question)*

12. **Q:** A team reproduces last quarter's commission report with an assistant, matches their own
    numbers exactly, and proposes letting it run this quarter's report unreviewed. What does the
    course say the test earned them?
    - Nothing yet, because a single matching run is not a sample, and the loop requires the same case
      to be reproduced several times over
    - Confidence in the instructions rather than in the assistant, so the same instructions would now
      work unreviewed in either product
    - Proof for similar work, which is enough to remove review from the recurring report while
      keeping it for anything unusual
    - Earned confidence for similar future work and nothing more, since passing a test never
      transfers the accountability for what ships
    *(Source: 9. Prove it on work you already know)*

---
[⬅ Terms + Where This Leads](05-terms-and-where-to-go.md) · [Answer Key ➡](quiz.md) · [⬆ Index](README.md)
