# 14 — Sources & Further Reading

Ye course chand primary sources par khara hai — framing aur quotes yahin se aayi hain, technical
details official docs se.

## "Loop Engineering" Ki Origin

- Addy Osmani, *Loop Engineering*: wo essay jisne pattern ka naam rakha aur five-parts-plus-spine model
  set kiya. [addyosmani.com/blog/loop-engineering](https://addyosmani.com/blog/loop-engineering/)
- Avi Chawla, *Loop Engineering, Clearly Explained*: inner-loop anatomy, 4 nested engineering layers
  (prompt → context → harness → loop), doom-loop framing, loops ke liye tool-design rules.
  [dailydoseofds.com/p/loop-engineering-clearly-explained](https://www.dailydoseofds.com/p/loop-engineering-clearly-explained/)
- Data Science Dojo, *The 4 Layers of AI Engineering*: one-failure-mode-per-layer framing aur "which
  layer are you still doing by hand" self-check, Concept 1 ki note mein paraphrase hui.
- Rakesh Gohel, *How to Actually Use Fable 5* (infographic): self-learning vs self-improving distinction,
  aur prompt-harder-and-start-over vs run-log-distill-repeat wala contrast, Concept 12 ki note mein.
  [rakeshgohel.substack.com](https://rakeshgohel.substack.com)
- Sydney Runkle (LangChain), *The Art of Loop Engineering*: four-loop stack (agent, verification,
  event-driven, hill-climbing), trace-driven improvement loop, aur swyx ki "loopcraft" framing ka pointer.
  [langchain.com/blog/the-art-of-loop-engineering](https://www.langchain.com/blog/the-art-of-loop-engineering)
- Lamis (Anthropic, Applied AI), *Context Engineering: Memory and Dreaming* (AI DevCon 2026 talk):
  in-band vs out-of-band memory split, dreaming consolidation process, shared memory stores ke production
  guardrails (Concept 14 ki note), aur school/head-teacher analogy (Concept 12 ki note).
  [youtube.com/watch?v=tQ41RxfZZVg](https://www.youtube.com/watch?v=tQ41RxfZZVg)
- Letta (Charles Packer, Sarah Wooders, et al.), *Sleep-time Compute* (April 2025): dreaming idea ka
  sab se pehla productized version — ek background agent jo idle time mein primary agent ki memory
  rewrite karta hai, MemGPT lineage se, plus caveat ke offline consolidation sirf tab kaam deta hai jab
  future tasks past jaisay hon. [letta.com/blog/sleep-time-compute](https://www.letta.com/blog/sleep-time-compute/)
- Stanford / SambaNova / UC Berkeley, *Agentic Context Engineering (ACE)*: repeated memory rewriting ke
  do failure modes (brevity bias, context collapse) naam karta hai, fix (dreaming note mein) incremental
  delta updates hai, monolithic rewrites nahi. [arxiv.org/abs/2510.04618](https://arxiv.org/abs/2510.04618)
- OWASP, *Top 10 for Agentic Applications (2026)*: Memory aur Context Poisoning ko alag agentic threat
  define karta hai — injected content memory mein persist karti hai aur original attack ke baad bhi
  behavior influence karti hai. Dreaming note ki poisoning warning isi se hai.
- Simon Willison, *Designing agentic loops* (Sep 2025): sab se pehla saaf statement ke loop **design**
  karna hi skill hai, agent ko drive karna nahi. Term se pehle ki baat. [simonwillison.net](https://simonwillison.net/)
- TrueFoundry, *Loop Engineering at Enterprise Grade*: failure-stacking math, loop parts ki
  standing-permission framing, team-scale inventory problem. Concept 14 ki note ke governance analyses
  isi ka representative hain. [truefoundry.com/blog/loop-engineering-enterprise-agent-runtime](https://www.truefoundry.com/blog/loop-engineering-enterprise-agent-runtime)
- *The New Stack*, "The Anthropic leader who built Claude Code says he ditched prompting — now he just
  writes loops." [thenewstack.io/loop-engineering](https://thenewstack.io/loop-engineering/)
- Boris Cherny ka "my job is to write loops" quote CNBC interview se hai (Business Insider ne report
  kiya). Peter Steinberger ka "design loops that prompt your agents" X ki post se hai.
- Andrew Ng: teen product-development loops (coding minutes mein, developer feedback hours mein, external
  feedback din mein) aur "taste" ko human's **context advantage** ki tarah reframe karna. X ki post se.
  [x.com/AndrewYNg/status/2071988145667928442](https://x.com/AndrewYNg/status/2071988145667928442)
- Andrej Karpathy: *"Don't tell it what to do, give it success criteria and watch it go,"* aur
  AutoResearch project — ek agent jo training script tweak karta hai, result measure karta hai, aur jo
  kaam kare wo rakh leta hai, bina kisi human editing ke rounds ke darmiyan. X ki posts se.

## Claude Code (Official Docs)

- Routines: cloud scheduled automations, triggers, run caps, per-plan daily limits ke sath launch
  announcement — [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines) aur
  [claude.com/blog/introducing-routines-in-claude-code](https://claude.com/blog/introducing-routines-in-claude-code)
- Channels: chalti session mein event-driven input — [code.claude.com/docs/en/channels](https://code.claude.com/docs/en/channels)
- Scheduled tasks: `/loop`, cron tools, Desktop tasks, background-session carryover rule —
  [code.claude.com/docs/en/scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks)
- Changelog: background sessions, retry watchdog, `ultracode` rename — sab se pehle yahan supersede hoti
  hain — [code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog)
- Memory: `CLAUDE.md`, auto memory, Auto Dream research preview ka consolidation pass —
  [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)
- Delba de Oliveira (Anthropic, Claude Code team), *Building verification loops in Claude Code with
  skills* (July 22, 2026): verification-skills interlude ka source — checks skills ki tarah packaged,
  4 deployment homes (standalone, embedded, chained, on-every-PR), graduation signals, wrapper-skill
  pattern, Anthropic ka apna internal `/code-review` → `/simplify` → `/verify` → `/design` chain, aur
  `/verify`, Code Review, Rubrics in Managed Agents ke pointers —
  [claude.com/blog/building-verification-loops-in-claude-code-with-skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills)
- Code Review aur Rubrics in Managed Agents likhte waqt research previews ya beta thin. Availability/
  behavior par bharosa karne se pehle live docs check karo.

## OpenCode (Official Docs)

- CLI: `opencode run`, `serve`, `--attach` — [opencode.ai/docs/cli](https://opencode.ai/docs/cli/)
- Agents aur subagents: primary agents, subagents, per-agent models — [opencode.ai/docs/agents](https://opencode.ai/docs/agents/)
- GitHub integration: Action, schedule, PR/issue triggers, `opencode github install` —
  [opencode.ai/docs/github](https://opencode.ai/docs/github/)

## Model Identifiers

- Anthropic, *What's new in Claude Sonnet 5*: `claude-sonnet-5` model string ka source, Sonnet 4.6 se
  direct migration, adaptive-thinking default, naya tokenizer —
  [platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5)
- Anthropic, *Model IDs and versioning*: dateless IDs 4.6-generation se pinned snapshot hain, major-
  version releases jaise Sonnet 5 minor segment omit karte hain, 4.5-generation models jaise Haiku 4.5
  dated canonical ID (`claude-haiku-4-5-20251001`) + dateless alias rakhte hain —
  [platform.claude.com/docs/en/about-claude/models/model-ids-and-versions](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions)
- Anthropic, *Introducing Claude Fable 5 and Mythos 5*: Opus se upar flagship generation, mid-2026 ship
  hui, yaad dehani ke chapter ke model examples illustrations hain, frontier nahi —
  [anthropic.com/news/claude-fable-5-mythos-5](https://www.anthropic.com/news/claude-fable-5-mythos-5)

*Sab links early July 2026 tak current hain. Yeh tools baar baar update hote hain, isliye kisi limit,
flag, ya model string par bharosa karne se pehle live docs se confirm karo.*

## Ek Line Mein Poori Cheez

> Prompt batata hai kya karna hai. Loop batata hai kab rukna hai. Agent ko turn-by-turn prompt karna
> chhoro. Wo loop design karo jo aapki jagah agent ko prompt kare — matlab ek heartbeat, chaar working
> parts, aur ek spine jo yaad rakhe — aur wo engineer bane raho jo dekhta hai kya ship hua.

---
[⬅ Where to Go Next](13-where-to-go-next.md) · [Agla: Test Your Understanding ➡](15-test-your-understanding.md) · [⬆ Index](README.md)
