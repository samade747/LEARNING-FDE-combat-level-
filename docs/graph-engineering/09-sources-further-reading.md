# 09 — Sources & Further Reading

Ye course chand primary sources par khara hai — framing aur quotes yahin se aayi hain, technical
details official docs se.

## Is Kitaab Ke Andar

- [Loop Engineering](../loop-engineering/README.md): ratchet, spine, maker-checker split, dreaming
  loop, aur two-routine gate — Part 5 ka har governance edge wahin ek loop ki tarah pehle bana tha.
- [Harness Engineering](../harness-engineering/README.md): typed output aur reversibility discipline,
  dono yahan memory-scale par promote hue.
- **Trusting the Checker** (agla course): grounded reviewer, aur extraction pipeline, kitne achhe hain —
  yeh measure karta hai.
- **Leaving the Laptop** (agla course): graph aur uske loops laptop band hone ke baad kahan rehte hain.
- **Human-Agent Teams**: loops ka graph org chart par kya ban jata hai.

## Primary Sources

- Andrej Karpathy, **autoresearch** (7 March 2026 release): [github.com/karpathy/autoresearch](https://github.com/karpathy/autoresearch).
  Teen-file harness, ratchet loop, aur commit-DAG memory. `program.md` khud parho quote karne se pehle
  — Concept 4 ke "do memories" correction ka source: experiments ek dedicated branch par chalte hain,
  branch sirf improvement par aage barhta hai, barabar/bura kuch bhi `git reset` se hat jata hai, aur
  `results.tsv` har attempt record karti hai jabke Git se deliberately untracked rehti hai.
- Andrej Karpathy, **AgentHub** (9-10 March 2026 ke aas paas publish hui, **ab public nahi**): agent-first
  collaboration layer — bare Git repo, SQLite, message board, aur `children`/`leaves`/`lineage` CLI.
  Khud "just a sketch. Thinking..." kehti hai. Original repo hafton mein private ho gaya, koi license
  file nahi thi. Preserved community forks hi ab code parhne ka tareeqa hain — historical artifact ki
  tarah lo, dependency ki tarah nahi. AgentHub integration thread autoresearch repo mein abhi bhi public
  hai aur behtar primary reference hai.
- Anthropic, **Knowledge Graph Construction with Claude** (Cookbook, 23 March 2026): [platform.claude.com/cookbook/capabilities-knowledge-graph-guide](https://platform.claude.com/cookbook/capabilities-knowledge-graph-guide) —
  structured outputs se extraction (Haiku par), reasoning ki tarah resolution (Sonnet par), NetworkX
  assembly, aur citations ke sath subgraph querying. Part 3 ka source.
- Erik Schluntz aur Barry Zhang, **Building Effective Agents** (Anthropic Engineering, Dec 2024): 5
  composable workflow patterns jo Concept 10 ground karta hai.
- Anthropic, **How we built our multi-agent research system** (Anthropic Engineering, 2025): [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system) —
  orchestrator-worker architecture, single agent se breadth-first advantage, aur ~15x token cost jo
  Concept 14 ka budget-note cite karta hai (ordinary chat interactions ke against, single-agent run ke
  against nahi — live post confirm karo quote karne se pehle).
- Anthropic, **Introducing dynamic workflows in Claude Code** (28 May 2026, ab GA): [claude.com/blog/introducing-dynamic-workflows-in-claude-code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) —
  Part 2 ka source: generated orchestration, dus se sau tak parallel fresh-context sub-agents, checked
  results, resumable progress, `ultracode` setting. Reference docs mein asal limits: 16 concurrent
  agents, 1,000 agents per run. [code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows)
- Peter Steinberger, 18 July 2026 ki post ("Are we still talking loops or did we shift to graphs yet?"):
  wo baarah lafz jinhon ne is season ko naam diya. [x.com/steipete/status/2078277297791189132](https://x.com/steipete/status/2078277297791189132)
- Carlos E. Perez (Intuition Machine), *From Loop Engineering to Graph Engineering?* (19 July 2026):
  Part 5 ka source — support-bot ki kahani, single loop ke 4 failures aur unke structural fixes,
  circular-graph warning, anchors aur frozen nodes. [medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c](https://medium.com/intuitionmachine/from-loop-engineering-to-graph-engineering-d3ebeb08511c)
- *Graph Engineering: The Karpathy Loop, Improved 1000x by Itself* (independent synthesis PDF, July
  2026): staged build path, two-graphs distinction, 4 invariants, closing traceability test. **Apne
  pehle page par khud kehti hai:** Karpathy ya Anthropic se affiliated ya endorsed nahi hai — useful
  study note ki tarah parho, primary sources pehle.

## Origin Story — Ek Zaroori Correction

Viral post ne dawa kiya: *"Two Anthropic seniors just made Karpathy's loop 1000x better with Graph
Engineering — dropped 11-page PDF."* Us PDF ka apna pehla page italics mein saaf likhta hai:
**independently compiled, not affiliated with Andrej Karpathy and Anthropic, and not endorsed.**
"1000x" ek slogan hai, measurement nahi.

■ **Kyun matter karta hai:** is poore course ka central daawa yehi hai — *"har claim apna source rakhe,"
"confidence ko evidence chahiye."* Ek aisa course jo yeh sikhata ho, agar apne khud ke inputs par
provenance discipline apply na kare — to apni authority khud kho deta hai. Ek genuine convergence jo
meme miss kar gaya: 19 May 2026 ko Karpathy khud **Anthropic ke pretraining team mein shamil ho gaye**
(Claude se pretraining research accelerate karne ke liye) — to loop tradition aur graph tradition Anthropic
mein mil gayin, lekin us tarah nahi jis tarah viral post ne daawa kiya, aur us PDF mein nahi.

*Sab links late July 2026 tak current hain. Har repo, preview feature, aur number tez badalta hai —
live source se confirm kiye bina kisi par bharosa mat karo.*

## Ek Line Mein Poori Cheez

> Agent bhool jata hai, graph nahi bhoolta. Do graphs rakho — kaam ke liye ek DAG, facts ke liye ek
> knowledge graph — schema se doosri graph bharo, naam reversibly merge karo, har edge par ek receipt
> lagao, workers ko subgraph do file-dump nahi, aur har checker ko edge cite karne do ya maangne do.
> Phir loops khud wire karo: har optimizing number par ek watcher, har target ka malik ek dheema loop,
> nodes ke darmiyan ek gate, aur anchors jin se koi loop bahas nahi kar sakta. Graph claims store karta
> hai, truth nahi — grounded versus ungrounded hi wo axis hai jo har rename se bach jata hai.

---
[⬅ Practice Projects](08-practice-projects.md) · [Agla: Test Your Understanding ➡](10-test-your-understanding.md) · [⬆ Index](README.md)
