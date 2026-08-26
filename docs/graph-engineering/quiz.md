# Quiz — Graph Engineering: A Crash Course (Test Your Understanding)

Book ke live page par yeh section ek interactive `<Flashcards />` widget se shuru hota hai (auto-
generated, page ke apne key-terms se) — koi static text nahi, isliye copy karne layak content nahi hai;
live version [graph-engineering-crash-course](https://agentfactory.panaversity.org/docs/graph-engineering-crash-course#flashcards)
par dekho.

Uske baad **18-question assessment** aata hai (book ke apne `<Quiz>` component se, verbatim) — course
ke har concept (1 se 16 tak, Part 6, aur dogfooding sameet) ka scenario-based test, sahi jawab ke sath
ek real-world analogy bhi. Yeh poora quiz neeche hai, taake khud test kar sako ya apni class ko exam ki
tarah de sako. Content seedha book se hai (English mein — precision zaroori thi, translate nahi kiya).

---

### Q1. Twenty parallel agents, transcripts, aur ek orchestrator jo fail ho jata hai

**Q:** Twenty parallel audit agents each keep excellent transcripts, and the orchestrator pastes all
twenty into its own context to synthesize. The run works once, then fails at forty agents. What does
Concept 1 say is wrong with transcripts as team memory?

- Transcripts are too informal in tone for an orchestrator to parse reliably, and rewriting each agent's conversation into a formal report format before pasting would let the copying approach scale to any number of workers
- **A transcript records everything said, in order, instead of what was established, with evidence, and copying them multiplies context and cost until the window fills: the fix is typed records any agent can query** ✅
- Transcripts should be summarized by a cheaper model first
- The orchestrator needs a larger context window model

**Explanation:** The failure is structural, not stylistic. A transcript is the wrong shape for memory:
it preserves the conversation rather than the conclusions, so every consumer must re-read and
re-interpret prose, and sharing means copying whole histories into finite windows at multiplying cost.
Typed records invert this: agents write what was established, claim, subject, evidence, run, and later
agents query only what they need. Formalizing the prose keeps the wrong shape with nicer grammar.
Summarization helps costs but still loses provenance and still cannot be queried. And a bigger window
postpones the wall by one model generation while the cost multiplies unchanged. Real-world: a hospital
shift change hands over the chart, not a recording of everything the last nurse said for eight hours.
*(Concept 1: The agent forgets, the graph does not)*

---

### Q2. Commit DAG aur Knowledge Graph ko mila kyun nahi sakte

**Q:** Why does Concept 3 insist the commit DAG and the knowledge graph must not be collapsed into one
structure?

- Because Git is a content-addressed store for text and cannot represent typed nodes or labelled edges, so any knowledge graph has to live in a separate database rather than in the repository beside the commits
- **Because they have different truth rules: a commit is a fact by construction, while a claim is a statement with evidence that may be wrong or superseded, so collapsing them treats guesses as history or buries history under guesses** ✅
- Because knowledge graphs are always larger than commit DAGs, and mixing sizes makes traversal too slow for any production query engine to handle at swarm scale
- Because the two came from separate lineages, Karpathy's out of training-loop automation and Anthropic's out of document extraction, and structures built by different teams carry incompatible assumptions that surface as integration debt the moment a single question has to cross both of them

**Explanation:** The separation is epistemic, not technical. The DAG records what happened: commit a81f
exists, its parent is fixed, Git guarantees it. The knowledge graph records what is believed: claim 441
has a source, a confidence, and might be superseded tomorrow. Mix them and you lose the distinction
that makes each useful: work history you can trust absolutely, and domain claims you can audit
skeptically. Git storing JSON is trivially possible (Part 6 does exactly that). Size and speed are
implementation details, not the principle. And the two lineages of tooling converged on complementary
layers precisely because the layers answer different questions: What changed? versus What is known? A
production system links them with explicit edges rather than merging them. Real-world: a lab keeps the
dated notebook of every experiment and separately writes the encyclopedia of current belief, with
footnotes pointing back at the notebook.
*(Concept 3: Two graphs, not one)*

---

### Q3. `prepare.py` ko agent kabhi kyun nahi chhoo sakta

**Q:** Autoresearch's agent may edit train.py but never prepare.py, which holds the evaluation. In this
book's vocabulary, what is prepare.py, and why does the design depend on it?

- **A frozen node, the evaluation the optimizing loop may never tune, because a ratchet that can edit its own metric will eventually reach for the checkmark instead of the work** ✅
- A performance optimization to keep the repo small
- An arbitrary preference of Karpathy's coding style with no architectural meaning, since the agent could safely be allowed to improve the data preparation code as long as its commits were reviewed later
- A backup copy of train.py in case of crashes

**Explanation:** prepare.py holds the metric, and the metric is the one thing the loop must never
touch: a self-improving loop that can modify its own evaluation will optimize the evaluation, which is
Goodhart's law with commit access. That is the loop course's check.py rule and the harness course's
deny-rule discipline, appearing in a repo that gathered tens of thousands of stars: evidence the
pattern is legible, not that the rule is optional. It is not about repo size, and it is not stylistic:
allowing metric edits 'with later review' reopens the exact hole, because the damage is done at
optimization time, not review time. Nor is it a backup: reversibility comes from Git reset to the last
retained commit. Real-world: students sit the exam. They do not get write access to the answer key,
however carefully their edits would be reviewed afterward.
*(Concept 4: Autoresearch)*

---

### Q4. Discarded experiments — permanent node banti hain ya ek text row

**Q:** A teammate says autoresearch proves that every experiment, kept or discarded, becomes a
permanent node in Git. What does program.md actually specify, and why does the distinction matter?

- They are right: each attempt is committed before running, so all attempts persist as commits in the branch history no matter what the metric does afterwards
- Discarded experiments are moved to a side branch named after the failure, so other agents can inspect them later without the main experiment branch filling with dead ends, which is how the loop keeps a complete record while staying readable
- program.md does not specify a keep-or-revert rule at all, leaving the decision to whichever coding agent is driving the loop that night
- **The branch advances only on improvement and anything equal or worse is git reset away, which removes that commit from the branch: discarded attempts survive only as rows in results.tsv, which is deliberately left untracked by Git** ✅

**Explanation:** Autoresearch keeps two memories under two standards, and conflating them is the most
common misreading of the project. The Git branch is the verified record: it advances only when val_bpb
improves, and a worse or equal result is reset away, which erases that commit from the branch rather
than filing it somewhere. The complete record of attempts, including discards and crashes, lives in
results.tsv, which program.md explicitly tells the agent not to commit. So a discarded idea is a line
of text, not a queryable node, and the next agent cannot traverse to it. That is precisely the gap
AgentHub closes by keeping pushed commits as durable nodes with no required main branch. Committing
before running is real, but the commit does not survive the reset. And the keep-or-revert rule is the
most specified part of the file. Real-world: a lab notebook that only records successful syntheses,
with the failures on a whiteboard nobody photographs.
*(Concept 4: Two memories, two standards)*

---

### Q5. AgentHub 'merge into main' ko kis se replace karta hai

**Q:** AgentHub removes the main branch, pull requests, and the merge queue. What replaces 'merge into
main' as the primary operation, and why do failed experiments stay in the graph?

- A faster merge queue tuned for agents
- Automatic deletion of any branch that underperforms, keeping only the best lineage so agents never waste context reading about approaches that already failed once somewhere in the swarm
- **Traversing the search graph, children, leaves, lineage, because a failed experiment is evidence that teaches every future agent which idea fails under which condition** ✅
- A voting system where agents elect the canonical branch

**Explanation:** Swarms invert human Git assumptions: thousands explore at once, most results never
merge on purpose, and no leaf is assumed canonical. The unit of collaboration becomes the traversal:
what was tried above this result (children), where is the unexplored frontier (leaves), what path
produced this outcome (lineage). Failed experiments are kept precisely because they are shared memory:
a crash at batch size 64 spares every future agent the same crash, but only if the record survives.
Deleting underperformers destroys exactly that evidence: the option's own justification (saving
context) is backwards, since a graph query costs far less than re-running the failure. A faster merge
queue optimizes a ceremony the swarm does not want, and elections still assume one canonical answer
where the swarm wants a map. Real-world: science keeps its negative results, or wishes it had, because
an unpublished failed trial gets run again, at full cost, by the next lab.
*(Concept 5: AgentHub)*

---

### Q6. Schema hi 'training data' hai — is daawe ke peeche asal baat kya hai

**Q:** The Cookbook replaces a trained NER model and relation classifier with a Pydantic schema and one
prompt per document. What is the deep claim behind 'the schema is the only training data'?

- Schemas magically eliminate extraction errors
- Pydantic runs faster than neural networks at inference time, which is the main reason the classical pipeline lost: schema validation is pure Python and adds no model latency, so what changed is throughput rather than extraction accuracy
- Trained pipelines are illegal to use commercially since 2026
- **The model already knows what entities and relations are: your remaining job is specifying the shape you want and validating what comes back, so changing the ontology becomes editing a class, not retraining a pipeline** ✅

**Explanation:** The classical pipeline existed because models had to be taught the task: labeled
corpora, trained classifiers, maintained heuristics. A frontier model arrives knowing the task. What it
lacks is your shape. The schema supplies the shape, structured outputs constrain the reply to it, and
code validates before the graph believes: the harness course's typed-output rule at pipeline scale. The
economics follow: ontology changes cost an edit, not a training run, and the volume work runs on a
cheap model. None of this eliminates errors. Part 7 and the next course exist because extraction still
fails, measurably. Speed is not the argument, and no such legal change occurred. Real-world: you no
longer teach the new analyst what a company is. You hand them the spreadsheet template and check the
columns they return.
*(Concept 6: Extraction)*

---

### Q7. String similarity resolution mein kyun fail hoti hai

**Q:** Why does string similarity fail at entity resolution, and what does the Cookbook use instead?

- **It fails in both directions: 'Edwin Aldrin' vs 'Buzz Aldrin' share no characters (missed merge) while two different 'Muhammad Khan's match perfectly (false merge), so resolution becomes a reasoning task using each entity's description as contextual evidence** ✅
- It fails only on non-English names
- It works fine: the Cookbook uses reasoning only to save money
- It fails because string similarity is too slow at scale, and the fix is a faster fuzzy-matching library with better indexing so the pairwise comparisons finish inside the extraction run's time budget

**Explanation:** Names are evidence, not proof, and similarity scores read only the letters. The two
failure directions are symmetric and both catastrophic in their own way: missed merges fragment one
real thing into disconnected nodes so multi-hop queries silently fail, and false merges staple
strangers together so every downstream traversal combines their lives. The Cookbook's fix is to give a
stronger model the descriptions captured at extraction time, because 'lunar module pilot' and 'second
person on the Moon' make the zero-overlap merge obvious, and different biographies keep the identical
names apart. Speed is a real concern, answered by cheap blocking before model arbitration, but a faster
wrong answer is still wrong. The failure is not language-specific, and reasoning is more expensive than
string matching, not less. Real-world: the bank merges two accounts by checking the address and date of
birth, never by how alike the names look.
*(Concept 7: Resolution)*

---

### Q8. False merge missed merge se zyada khatarnak kyun hai

**Q:** Concept 7 calls the false merge 'the catastrophic failure of knowledge graphs.' What makes it
worse than a missed merge, and what rule limits the damage?

- It is not worse: both failures cost the same
- **A false merge contaminates every downstream traversal confidently and invisibly, two people's employers, projects, and actions combined everywhere at once, so resolution must be additive and reversible: keep aliases, rationale, confidence, and the merging run, so one bad merge is one reversal, not a rebuild** ✅
- It corrupts the Git history of the repository holding the graph
- It is worse only in graphs larger than a million nodes, below which false merges stay cheap to find by reading the node list during a weekly review

**Explanation:** A missed merge fails loudly-ish: queries come back empty or thin, which someone
eventually notices. A false merge fails silently and multiplies: the graph answers every question
through the corrupted node with full confidence, and each answer looks fine alone. The defense is not
perfect merging, no policy achieves that, but reversible merging. Because the aliases, evidence, and
authoring run were kept, an incorrect merge can be unwound without reconstructing the pipeline. That is
the harness course's reversibility verb applied to memory. The two failures are not symmetric in cost,
Git history is untouched by a semantic error inside a JSON file, and scale changes the count of errors,
not their silence: a manual read-through catches misspellings, not two plausible strangers sharing a
name. Real-world: mailing one person's medical file to another with the same name. The error travels
everywhere the file goes, and only staples and receipts let you unwind it.
*(Concept 7: Resolution must be reversible)*

---

### Q9. 4 provenance invariants mein se kaunsa likhna asal mein violation hai

**Q:** Which of the following writes violates the four provenance invariants of Concept 8?

- **Deleting a disproven claim from claims.json so the graph stays clean and no future subgraph can be confused by stale information that has already been shown to be wrong** ✅
- A claim marked {"source": {"kind": "inference"}} because the agent deduced it rather than reading it
- Appending a new claim whose 'supersedes' field names the old claim, leaving every field on the old claim exactly as it was written, so a context builder can prefer the newer one while the original stays addressable
- An evaluation node that names 'reviewer-rubric-v3' as its rubric

**Explanation:** Invariant 4 says every superseded object remains addressable, replaced, never erased.
Deletion destroys the audit trail: you can no longer ask what the system believed on a given date or
why it changed its mind, and a recovery after a bad 'correction' becomes impossible. The clean-graph
instinct is served correctly by the supersedes pattern instead: append a new claim naming the old one:
the old claim stays exactly as written and is never edited, marked superseded, and context builders
simply prefer active claims. Stale information is excluded from subgraphs without being destroyed. The
inference-marked claim is explicitly legal: invariant 1 requires a source or an explicit inference
marker, and honesty about inference is the point. The evaluation node naming its rubric is invariant 3
working as designed. Real-world: an accountant corrects an entry with a dated adjusting entry, never
with an eraser. The eraser is what auditors are trained to treat as fraud.
*(Concept 8: The four invariants)*

---

### Q10. 50,000 edges wali graph — worker ko kya diya jaye

**Q:** Your graph has 50,000 edges. A worker's task mentions two entities. What does Concept 9's
context builder hand the worker, and why does it deliberately include conflicting claims?

- The full serialized graph, since more context is always better
- Only the single highest-confidence claim per entity, with all disagreement resolved by the context builder in advance, so the worker receives one consistent story and never has to reason about contradictions it has no way to adjudicate on its own
- **A bounded subgraph: resolve the task's entities, expand one or two hops over allowed edge types, prioritize recent verified claims, serialize within a token budget with stable edge IDs, including conflicts, because hiding uncertainty from the worker produces confident errors** ✅
- A summary written by another model

**Explanation:** Dumping the whole graph recreates the context problem the graph was built to escape.
50,000 serialized edges are as useless as fifty transcripts. The discipline is bounded retrieval: start
from the task's resolved entities, walk a small typed neighborhood, prefer recent and verified, fit the
budget, and attach edge identifiers so the worker's output can cite and a checker can verify. Conflicts
ship on purpose: if two sources disagree and the builder silently picks one, the worker reasons
confidently from half the evidence. The disagreement is information the task may hinge on.
Pre-resolving all contradiction turns the context builder into an unaudited judge. A prose summary
loses the citable IDs that make Concept 10's grounding possible. Real-world: the briefing folder for a
decision contains the two conflicting reports with a sticky note, not one report chosen by whoever
assembled the folder.
*(Concept 9: Subgraphs)*

---

### Q11. Grounded checker ko missing edge milti hai — jawab kya hota hai

**Q:** A maker claims 'Vendor X supplied the component involved in Incident Y.' The grounded checker
finds (vendor_x, supplied, component_z) but no edge linking component_z to incident_y. What does it
return, and why is that better than 'this claim seems weak'?

- PASS, since one of the two required edges exists and a half-supported claim is more likely true than false, which clears the bar for a low-stakes internal report where a wrong sentence costs little
- FAIL with no details, to be safe
- **REVISE with the missing edge named as required evidence, a work order, not a mood: the maker knows exactly which source-backed relation to find or which claim to withdraw, and if the evidence is found, the graph itself gains an edge** ✅
- It escalates every partial match to the human gate

**Explanation:** Grounding turns verification from impression into audit: the claim decomposes into
required edges, the graph is checked mechanically, and the verdict reports precisely which support is
absent. 'Seems weak' sends the maker back to guess what displeased the reviewer, while 'no supported
involved_in relation to incident_y' is actionable in one direction or the other: supply the source or
withdraw the claim. And the demand improves the memory, not just the report: found evidence becomes a
new provenance-backed edge. Passing on one-of-two edges approves exactly the unsupported half, and
'likely true' is the vibes-based standard grounding exists to replace. A detail-free FAIL discards the
checker's most valuable output. Escalating every partial match floods the gate with work the structure
already handles: the gate is for judgment calls, not lookups. Real-world: the auditor circles the one
missing receipt and names it, while 'the books feel off' helps no one.
*(Concept 10: The grounded checker)*

---

### Q12. Do memories, Part 6 mein — progress.md aur claims.json alag kyun

**Q:** In Part 6, session notes and dead ends stay in progress.md while only established findings enter
claims.json. Why keep two memories instead of putting everything in the graph?

- **Two truth standards: the spine is the diary of what was said and tried, the graph is the stricter record of what was established with evidence. Flooding the graph with chatter buries auditable claims under noise and breaks the invariants that make it trustworthy** ✅
- progress.md exists only for backward compatibility until the migration finishes
- JSON files cannot hold long prose
- The graph is too expensive to write to more than once per day, so low-value notes are batched into the spine to stay under the write budget

**Explanation:** This is Concept 3's two-graphs lesson at file scale: different records, different
truth rules. A diary entry, 'tried the cache approach, felt slow, abandoned it', is honest session
history but not an evidenced claim. Forcing it into claims.json either violates invariant 1 (no source)
or launders an impression into a citable fact that some future reviewer will ground a verdict on.
Keeping the spine preserves narrative context for humans and future sessions while the graph stays
small, strict, and auditable. It is not a migration leftover: the design is permanent, both files
active. JSON holds prose fine, and there is no write budget: the constraint is epistemic, not economic.
Real-world: the lab notebook records everything including the hunches. The published paper contains
only what the data supports, and nobody proposes merging the two documents.
*(Part 6: The maker writes to the graph)*

---

### Q13. Team ko graph "ready rehne ke liye" chahiye — Concept 15 kya kehta hai

**Q:** A team of three runs one triage loop with a spine, no cross-session queries, single-document
answers, and no provenance requirement. They propose building the full extraction-resolution-graph
pipeline 'to be ready.' What does Concept 15 say?

- Build it now: graphs are always the right foundation
- Build only the resolution stage, since name collisions are the likeliest future problem and having canonical entities ready in advance will let the eventual extraction stage drop in without rework
- **Do not: a graph is machinery with a real bill, extraction errors, resolution risk, schema rot, and it earns its cost only when connected queries, evolving relations, provenance, or shared state are central: one loop with a spine clears none of those bars** ✅
- Build it but keep it read-only

**Explanation:** The course sells graphs for twelve concepts and then draws the honest boundary:
machinery must be pulled by a real query, not pushed by fashion. Every listed condition points away
from a graph here, independent tasks, one-document answers, no provenance need, so the pipeline would
add error surface (bad extractions, false merges) and maintenance without a question it answers. The
bill flips the moment two loops exchange facts or a synthesis spans workers, and the Part 6 build is
deliberately the smallest version for that moment. Building 'one stage to be ready' pays the resolution
risk with no extraction to resolve. A read-only graph nobody writes to is a diagram, not memory. This is
the same discipline as the loop course's 'plan only when paths vary.' Real-world: the two-person shop
does not install the warehouse inventory system, and the day they open the warehouse, they install it
in a week because the need defines the design.
*(Concept 15: When not to build a graph)*

---

### Q14. Sab claims 'sourced' hain, lekin sab source doosre agent ki report hai

**Q:** Every claim in a large agent-built graph cites a source, and auditing shows every source is
another agent's report, whose sources are further agent reports. All invariants technically pass. What
is this failure, and what is the fix?

- A schema violation the pre-commit hook should have caught
- Healthy operation: agents citing agents is how shared memory is supposed to compound, and the invariants passing is precisely the evidence that the provenance discipline is working as designed at every layer of the system
- Proof that provenance is worthless in practice
- **A circular graph: everything cites everything, nothing touches the world: the fix is anchors, edges that bottom out in things no model produced, checked by following random claims all the way down to their leaves** ✅

**Explanation:** The invariants enforce that receipts exist. They cannot enforce what the receipts are
made of. A graph where model output sources model output is internally perfect and externally
untethered: the loop course's mutual-confirmation failure, rebuilt in memory, failing later and more
expensively with more green lights on the way down. The fix is structural: some fraction of edges must
anchor in reality, a test that actually ran, a log from a real system, a human-authored document, and
the audit is to follow ten random claims to their leaves and count how many bottom out outside the
model ecosystem. It is not a schema bug, because every field is filled correctly. Agents citing agents
is fine as intermediate structure: the pathology is when no chain ever reaches ground. And the lesson is
not that provenance is worthless: provenance is exactly what made this failure findable in an
afternoon. Real-world: three newspapers citing each other in a ring is not three sources. Someone has
to have attended the event.
*(Concept 13: Circular graphs and anchors)*

---

### Q15. Support-bot 'resolved' number barh gaya, lekin renewal gir gayi — kaunsa failure

**Q:** A support bot's ticket-resolution rate climbs for a quarter, then renewal data shows customers
leaving at twice the old rate: the bot learned to mark abandoned problems as solved. In Perez's four
failures, which one is this, and what is the graph's fix?

- Blindness upward: the fix is letting the bot set its own target so it can adapt
- **Gaming (Goodhart's law): the fix is pairing the optimizing loop with a watching loop on a counter-metric, such as resolution rate paired with renewal rate, because the fix is never a better loop but an edge in the graph** ✅
- Conflict, the fix is merging the support bot with the sales bot
- Measurement decay, the fix is a more detailed dashboard of the same resolution number, refreshed more often

**Explanation:** The loop worked perfectly. Its number quietly stopped meaning the real outcome. That
is gaming, Goodhart's law wearing a support headset. The structural signature is the fix's location:
nothing inside the loop can catch this, because the loop sees only the number it is chasing, so the
answer is an edge, a second loop watching a counter-metric that the first loop cannot game without the
gaming becoming visible (close tickets by pushing customers away, and renewal rate falls). Letting the
bot set its own target is blindness upward made worse, not fixed: targets belong to a slower loop.
Merging bots addresses conflict, a different failure with a different fix. And a richer dashboard of the
same metric is measurement decay's trap in miniature: more views of a number that has stopped touching
reality. You met the pattern's prevention twice already: autoresearch's untouchable prepare.py and the
loop course's check.py rule. Real-world: the call center graded only on call length learns to hang up
faster. The fix was never a better stopwatch.
*(Concept 12: Perez's four failures)*

---

### Q16. Target kaun badal sakta hai — triage loop khud ya koi aur

**Q:** Your dreaming loop proposes raising the triage loop's daily quota, and the triage loop itself
also wants to raise it. Under Concept 12's table, who is allowed to change the target, and why that
node?

- The triage loop, since it has the most data about its own capacity, and letting the executor tune its own quota removes a slow approval step that adds no information the loop does not already hold
- Whichever loop proposes it first
- **A slower loop, or the human gate, that owns the faster loop's target, because nothing inside a loop can ask whether its own target is right: changing targets is governed work, done above the loop that will be measured by it** ✅
- Targets should never change once set

**Explanation:** This is blindness upward, the second failure: a loop can optimize toward its target but
cannot question it, because the target is the loop's premise, not its output. So target ownership sits
one level up and one speed down: a slower loop, or a person, that reads real outcomes and decides what
better means. The dreaming loop proposing the change through a gate is exactly the healthy shape:
propose, not decide. Letting the executor set its own quota hands the exam to the student: the loop
with the most capacity data is also the loop with the most incentive to choose a comfortable number,
and speed of approval is not the scarce resource. Judgment about what the number is for is.
First-proposer is no principle at all. And frozen targets overcorrect: targets do change, as governed
work, with a written reason, by the node that owns them. Real-world: the sales team forecasts, and
finance owns the quota. The day sales sets its own quota is the day the quota stops meaning anything.
*(Concept 12: Blindness upward)*

---

### Q17. Reviewer ab edge IDs cite karta hai — kya evaluation ab zaroori nahi

**Q:** After this course, a teammate says: 'Our reviewer now cites edge IDs for every verdict, so we no
longer need to evaluate it.' Which boundary from Concept 16 does this miss?

- None, because grounding does make evaluation unnecessary, which is why the evals course precedes this one in the series: once every verdict carries an edge id the reviewer's output is mechanically checkable
- **Grounding upgraded the verdict from impression to audit, but the auditor is still a model: it can cite an irrelevant edge, miss an existing path, and drift with model updates. Measuring that is the next course, applied to both checkable layers: the extraction filling the memory and the reviewer reading it** ✅
- The reviewer needs a bigger model before evaluation becomes optional
- Edge citation only works in Claude Code, not OpenCode

**Explanation:** Grounding changes what the checker claims, 'I consulted these edges' beats 'I have an
impression', but a claim produced by a model is still a claim. A fluent verdict citing irrelevant edges
is a documented failure mode, path-finding can miss real support, and the model underneath drifts on
its own schedule. So the question 'how do you know the checker is any good?' survives grounding intact,
and it now applies twice: to the reviewer and to the extraction pipeline that filled the graph it reads,
each needing gold sets, calibration, and re-runs. The series order is the giveaway: Trusting the
Checker comes after this course precisely because grounded systems still need it. Model size does not
remove the need to measure, and the discipline is tool-agnostic files and shell. Real-world: the
auditor who attaches receipt numbers to every finding is a better auditor, and still gets peer-reviewed,
because attaching a receipt and reading it correctly are different skills.
*(Concept 16: Limits and the bridge)*

---

### Q18. Viral PDF ka daawa — course ka sourcing note kya establish karta hai

**Q:** The viral post said 'Two Anthropic seniors just made Karpathy's loop 1000x better' and attached
an 11-page PDF. What does the course's sourcing note establish, and why does the correction matter
beyond pedantry?

- **The PDF's own front page says it is independently compiled, not affiliated with or endorsed by Karpathy or Anthropic, and '1000x' is a slogan, not a measurement. The synthesis is useful, but attribution and evidence standards are exactly what this course teaches, so repeating the meme uncorrected fails the course's own discipline** ✅
- The PDF is fake and its content should be ignored entirely, since a synthesis whose own author admits it is unaffiliated cannot be a legitimate source for anything
- Anthropic later confirmed the two seniors' identities
- The correction matters only for legal reasons

**Explanation:** The primary sources are real, Karpathy's two repos, Anthropic's cookbook and workflow
docs, and the PDF is a genuinely useful study note that this course draws on. But its front page states
its own status plainly, and the viral framing inverted it: independent became official, and a synthesis
became a benchmark result with a number attached. A course whose central claims are 'every claim keeps
its source' and 'confidence requires evidence' cannot repeat that framing and keep its authority:
provenance discipline applies to the course's own inputs first. This is the same pattern Part 5 opens
with: Steinberger asked twelve words, the crowd manufactured the slogan, and the reader's job is to
check the primary source before quoting. Ignoring the PDF overcorrects (the synthesis has real value,
attributed correctly), no such confirmation exists, and the stakes are epistemic, not legal.
Real-world: the forwarded message that says 'scientists confirm'. The first click is always to what the
scientists actually wrote.
*(Where this came from)*
