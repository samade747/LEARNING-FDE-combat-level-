# 09 — Sources & Further Reading

Ye course chand primary sources par khara hai — framing aur quotes yahin se aayi hain, mechanical
details official docs se.

## "Harness Engineering" Ki Origin

- Mitchell Hashimoto, *My AI Adoption Journey* (Feb 5, 2026): Step 5, "Engineer the Harness" — founding
  rule set karta hai: har agent mistake ko **impossible** bana do. Term ki origin isi ko widely credit
  kiya jata hai. [mitchellh.com/writing/my-ai-adoption-journey](https://mitchellh.com/writing/my-ai-adoption-journey)
- Ryan Lopopolo (OpenAI), *Harness engineering: leveraging Codex in an agent-first world*: Feb 11, 2026
  wali formal definition, ek internal beta zero hand-written lines ke sath ship karne se. *"Humans
  steer. Agents execute."* isi se aaya. [openai.com/index/harness-engineering](https://openai.com/index/harness-engineering/)
- LangChain, *The Anatomy of an Agent Harness*: *"Agent = Model + Harness"* formulation.
  [langchain.com/blog/the-anatomy-of-an-agent-harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness)
- LangChain, *State of Agent Engineering* (late 2025): 1,300+ professionals ka survey jiske numbers
  Concept 10 ke observability-vs-evals gap ke peeche hain. [langchain.com/state-of-agent-engineering](https://www.langchain.com/state-of-agent-engineering)
- Addy Osmani, *Agent Harness Engineering*: harness ke parts ka practitioner tour (prompts, tools,
  context policies, hooks, sandboxes, subagents, feedback loops, recovery paths) — usi writer se jisne
  loop engineering naam diya tha. [addyosmani.com/blog/agent-harness-engineering](https://addyosmani.com/blog/agent-harness-engineering/)

## Evidence Aur Frameworks

- *Agent Harness Engineering: A Survey* (2026): binding-constraint thesis — harness-akela coding
  benchmarks par 10x tak, terminal-agent benchmarks par double-digit point gains.
  [openreview.net/pdf?id=eONq7FdiHa](https://openreview.net/pdf?id=eONq7FdiHa)
- *What makes a harness a harness* (June 2026): Concept 1 ke 4 necessary elements (agent loop, tool
  interface, context management, control mechanisms) — Claude Code, Codex CLI, Aider, Cline, OpenHands,
  SWE-agent par apply hue. [arxiv.org/abs/2606.10106](https://arxiv.org/abs/2606.10106)
- *The Complete Guide to Agent Harness* (harness-engineering.ai, 2026): Concept 1 ka compounding-failure
  arithmetic + six-component production model (recovery sameet).
  [harness-engineering.ai/blog/agent-harness-complete-guide](https://harness-engineering.ai/blog/agent-harness-complete-guide/)
- deepset (May 2026): Concept 10 ke 4 failure classes ki framing, aur evidence ke harness-only changes
  agents ko 20+ leaderboard positions move karte hain. [deepset.ai/blog/harness-engineering](https://www.deepset.ai/blog/harness-engineering)
- Faros AI (May 2026): five-layer production-harness model aur teen-phase maturity arc (prompt → context
  → harness). [faros.ai/blog/harness-engineering](https://www.faros.ai/blog/harness-engineering)
- Augment Code, *Harness Engineering for AI Coding Agents*: attribution history — Karpathy misattribution
  correction sameet (context engineering aur agentic engineering Karpathy ki terms hain, harness
  engineering nahi). [augmentcode.com/guides/harness-engineering-ai-coding-agents](https://www.augmentcode.com/guides/harness-engineering-ai-coding-agents)
- Confucius Code Agent (Meta + Harvard, Dec 2025): AX, UX, DX ke ird gird harness design — Concept 7 ka
  Agent Experience treatment yahin se. [arxiv.org/abs/2512.10398](https://arxiv.org/abs/2512.10398)
- Gartner, *2026 Hype Cycle for Agentic AI*: ADLC, context graphs, agent-experience profiles. Governance,
  security, FinOps core agent tech ke sath uth rahe hain.
- MCP security literature (2026): tool poisoning, rug pulls — Concept 5 ki deeper note ke peeche layered
  defenses (enforced server allowlists, version pinning, deny-by-default egress).
- ai-boost, *awesome-harness-engineering*: papers, patterns, tools ka community corpus.
  [github.com/ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering)
- Denis Sergeevitch, *agents-best-practices*: open-source, provider-neutral skill — harness design/audit
  ke liye, isi kitaab wale Agent Skills format mein packaged. [github.com/DenisSergeevitch/agents-best-practices](https://github.com/DenisSergeevitch/agents-best-practices)

## Claude Code (Official Docs)

- Settings: `settings.json`, `$schema`, scopes, `sandbox` keys — [code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings)
- Permissions: allow/ask/deny rules, matchers, precedence — [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions)
- Hooks: event list, matchers, stdin JSON, exit-code behavior per event — [code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks)
- Subagents: frontmatter fields, `tools` name list, command-level control ke liye PreToolUse hooks —
  [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents)
- Checkpointing: `/rewind` kya track karta hai, kya nahi — [code.claude.com/docs/en/checkpointing](https://code.claude.com/docs/en/checkpointing)
- Changelog: har mechanical detail sab se pehle yahan supersede hoti hai — [code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog)

## OpenCode (Official Docs)

- Permissions: `permission` block, per-agent overrides, `permission.task` — [opencode.ai/docs/permissions](https://opencode.ai/docs/permissions/)
- Plugins: `tool.execute.before` / `tool.execute.after` aur plugin event surface — [opencode.ai/docs/plugins](https://opencode.ai/docs/plugins/)
- Agents: subagent config, models, permission blocks — [opencode.ai/docs/agents](https://opencode.ai/docs/agents/)

*Sab links mid-July 2026 tak current hain. Yeh tools baar baar update hote hain, isliye kisi bhi rule
name, hook event, ya setting par bharosa karne se pehle live docs se confirm karo.*

## Ek Line Mein Poori Cheez

> Model intelligence deta hai. Harness **trust** deta hai. Jo allowed hai usay **constrain** karo, jo
> pata hona chahiye wo **inform** karo, jo hua usay **verify** karo, jo ghalat hua usay **correct** karo
> (aaj raat ka run, aur system hamesha ke liye), aur jo sirf insaan decide kar sakta hai wo **escalate**
> karo. Aur in paanchon ke neeche ek rule: **guardrail hamesha harness mein rehta hai, prompt mein
> kabhi nahi.**

---
[⬅ Appendix (Hook Pipeline)](08-appendix-hook-pipeline.md) · [Agla: Test Your Understanding ➡](10-test-your-understanding.md) · [⬆ Index](README.md)
