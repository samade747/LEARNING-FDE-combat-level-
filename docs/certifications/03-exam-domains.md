# 03 — Exam Domains: Blueprint Weights + Yeh Book Kahan Cover Karti Hai

**Yeh file PCAR-F/CCAR-F push ke liye sab se zaroori hai — study time domain-weight ke hisaab se
allocate karo, sab domains equal time mat do.**

## CCAR-F: Architect, Foundations

Program ka pehla exam, March 2026 mein launch hua. Judgment zyada test karta hai, recall kam —
scenario trade-offs pe built questions.

| Domain | Weight | Yeh Book Kahan Cover Karti Hai |
| --- | --- | --- |
| **Agentic Architecture** | **27%** | [Choosing Agentic Architectures](../choosing-agentic-architectures-crash-course/README.md), [Loop Engineering](../loop-engineering/README.md), [Harness Engineering](../harness-engineering/README.md), [Graph Engineering](../graph-engineering/README.md) |
| Claude Code Configuration | 20% | [Claude Code and OpenCode](../agentic-coding/README.md), [Plugins for AI Agents](../plugins-crash-course/README.md) |
| Prompt Engineering | 20% | [AI Prompting in 2026](../ai-prompting-2026/README.md), [Spec-Driven Development](../spec-driven-development/README.md) |
| Tool Design and MCP | 18% | [Connector-Native Apps](../connector-native-apps/README.md), Skills & Connectors *(🔲 abhi is repo mein nahi)* |
| Context Management | 15% | [Building the Context Layer](../context-layer-crash-course/README.md), [The Four Layers](../four-layers/README.md), [RAG on Postgres](../postgres-ai-crash-course/README.md) |

**Agentic Architecture sab se bara domain hai (27%) — aur is book ka sab se deeply covered area bhi**,
4 alag courses ke zariye. **PCAR-F ke liye study priority: pehle Agentic Architecture, phir Claude Code
Config aur Prompt Engineering (dono 20%), phir Tool Design/MCP (18%), phir Context Management (15%).**

## CCDV-F: Developer, Foundations

Un logon ke liye jo build karte hain — Claude applications, agents, workflows integrate/ship karne ki
ability validate karta hai. **Domain weights bohat uneven hain — study time equally split mat karo.**

| Domain | Weight | Yeh Book Kahan Cover Karti Hai |
| --- | --- | --- |
| **Applications and Integration** | **33.1%** | [Python in the AI Era](../python-crash-course/README.md), [Deploy Your Agent Harness](../deploying-agents-crash-course/README.md), [Claude Code and OpenCode](../agentic-coding/README.md) |
| **Model Selection and Optimization** | **16.8%** | [The Four Layers](../four-layers/README.md), [Open Source LLMs](../open-source-llms/README.md) |
| Agents and Workflows | 14.7% | [Build AI Agents with the OpenAI Agents SDK](../build-agents-crash-course/README.md), [Loop Engineering](../loop-engineering/README.md), [Choosing Agentic Architectures](../choosing-agentic-architectures-crash-course/README.md) |
| Prompt and Context Engineering | 11.0% | [AI Prompting in 2026](../ai-prompting-2026/README.md), [Building the Context Layer](../context-layer-crash-course/README.md), [RAG on Postgres](../postgres-ai-crash-course/README.md) |
| Tools and MCPs | 10.6% | [Connector-Native Apps](../connector-native-apps/README.md), Skills & Connectors *(🔲)*, [Give Your AI Agent a Nervous System](../ai-agent-nervous-system-crash-course/README.md) |
| Security and Safety | 8.1% | [AI Identity](../ai-identity-crash-course/README.md) |
| Claude Code | 3.1% | [Claude Code and OpenCode](../agentic-coding/README.md) |
| Eval, Testing, and Debugging | 2.6% | [Trusting the Checker](../trusting-the-checker/README.md), [Eval-Driven Development](../eval-driven-development-crash-course/README.md) |

**Top do rows exam ka aadha hain.** Applications and Integration (33.1%) + Model Selection and
Optimization (16.8%) = ~50%. Claude Code + Eval mil kar 6% se kam hain — inhe padho, lekin same time
mat do.

## CCAO-F: Associate, Foundations

On-ramp un logon ke liye jo Claude adoption **influence** karte hain, integration code khud nahi
likhte: consultants, pre-sales engineers, project managers, adoption leads. Capabilities, limitations,
use cases, adoption patterns test karta hai — implementation nahi.

**7 published domains hain, teen exam ka half se zyada:**

| Domain | Weight |
| --- | --- |
| Output Evaluation and Validation | 21% |
| Workflow Integration | 16% |
| Governance and Responsible Use | 15% |

**Sab se bara domain prompt-writing nahi hai — output evaluate karna, problems spot karna, result
pass karne se pehle validate karna hai.** Yeh credential asal mein judgment test karta hai.

Is book ka **"Foundations (Everyone)"** section seedha is level ke liye hai — book-to-exam ka sab se
strong fit yahin hai:

| Exam area | Yeh Book Padho | Is Repo Mein |
| --- | --- | --- |
| What Claude is and is not | [What AI Actually Is](../what-ai-actually-is-crash-course/README.md) | ✅ |
| Getting useful output | [AI Prompting in 2026](../ai-prompting-2026/README.md) | ✅ |
| Working in the formats agents use | [Markdown In, HTML Out](../markdown-html-crash-course/README.md) | ✅ |
| What is buildable without an engineer | Code You Never Write | 🔲 |
| Extending Claude with skills and connectors | Skills & Connectors | 🔲 |
| Judgment about where AI belongs | How to Think in the AI Era | 🔲 |
| Claude in a browser and a desktop | [General Agents on the Web](../general-agents-web/README.md), [Cowork and OpenWork](../cowork/README.md) | ✅ |
| Advising on adoption | [Roles This Book Trains](../roles-this-book-trains/README.md), Selling as a Vertical FDE | ✅ / 🔲 (`how-to-sell/` folder khaali hai) |

**Note:** `docs/roles-this-book-trains/` aur `docs/ai-prompting-2026/` root README.md ke status table
mein 🔲 dikhte hain lekin **actually poore documented hain** — root README ka status table stale hai,
[07-practice-log.md](07-practice-log.md) mein flag kiya hai.

## CCAR-P: Architect, Professional

Capstone — Architect Foundations ko extend karta hai **stakeholder communication aur lifecycle
management** ke sath. Senior architects ke liye jo discovery se production/iteration tak poora solution
own karte hain. CCAR-F ka poora mapping yahan bhi apply hota hai, plus:

| Exam area | Yeh Book Padho |
| --- | --- |
| Everything in CCAR-F | [Upar wali CCAR-F table](#ccar-f-architect-foundations) |
| Stakeholder communication | Selling as a Vertical FDE *(🔲, `how-to-sell/` khaali hai)*, [Getting Paid as a Vertical FDE](../how-to-get-paid/README.md) *(partial — sections 04-05 abhi missing)* |
| Operating model and handover | [Human-Agent Teams](../human-agent-teams-crash-course/README.md), [Designing Agent Experiences](../designing-agent-experiences-crash-course/README.md) |
| Lifecycle and iteration | [Eval-Driven Development](../eval-driven-development-crash-course/README.md), [Deploy Your Agent Harness](../deploying-agents-crash-course/README.md) |
| Governance and access | [AI Identity](../ai-identity-crash-course/README.md) |

---
[⬅ Index](README.md) · [Peechay: Stage Two](02-stage-two-anthropic.md) ·
[Agla: Gaps + Study Plan ➡](04-gaps-and-study-plan.md)
