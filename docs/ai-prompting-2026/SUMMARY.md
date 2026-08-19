# AI Prompting in 2026 — Crash Course — Summary

Foundations chapter 2/6. 13 Concepts. Core insight: model **stateless** hai — almost har "advanced
technique" ek move hai do disguises mein: **sahi context andar lao, ghalat context bahar rakho.**

## 00 — Overview

Kya badla 2023 se: context windows ~1000x bare, reasoning real hui (explicit thinking modes), web
search + code execution built-in tools ban gaye, multimodal normal ho gaya, tools ne memory rakhni
shuru ki, desktop apps (Cowork, OpenWork) aur command-line agents (Claude Code, OpenCode) aaye.

## 01 — How AI Knows Things (Concepts 1-3)

1. **Novice vs Power User** — briefing ka farq (car/self-review/business-idea/blog examples). Mental
   model: AI = smart-lekin-naya colleague, aapke baare mein kuch nahi jaanta.
2. **Pretrained Knowledge** — text se seekha, experience se nahi. Strong (cooking, popular topics) vs
   sparse (niche/regional) vs absent (private data, post-cutoff). Confidently ghalat forum post →
   confidently ghalat model output (regional folk game example).
3. **3 Retrieval Modes**: pretrained, web search (stale-rescue but source-currency check nahi karta),
   deep research (dozens sources, multi-section report). Web search actually kaam kaise karta hai:
   separate retrieval-layer model pages ko summary mein reduce karta hai — fix: source-type specify
   karo, quotes mango. AI vs Google table (link chahiye vs answer chahiye).

## 02 — Talking to AI Well (Concepts 4-7)

4. **Context Is the Whole Game** — window khaali nahi hoti (system prompt pehle se load, waiter
   analogy). Apni layer add kar sakte ho (chhoti rakho, prune karo — Anthropic ne July 2026 apni
   instructions se zyada tar delete kiya). Context rot — topic badle to nayi conversation. Chat =
   working memory, storage nahi. **Projects/Notebooks** = context ek baar front-load. Memory = tool ka
   note (model ko memory nahi deti) — padho, zabani correct karo, clean-slate mode, confidentiality
   warning (client details resurface ho sakti hain).
5. **Reasoning ("Think Hard")** — built-in reasoning modes explicit invoke karo. METR 2025 study: task
   length har 7 mahine mein double. Thinking mode kab skip karo: quick lookups.
6. **Sycophancy** — models agreement-biased (Washington Post Nov 2025: ~10x "yes" vs "no"). Bait verbs
   (find/defend/confirm/prove) vs neutral (evaluate/compare/critique). Number force karo (1-10 scale +
   justification) — vague feedback sasta hai, number commit karwata hai.
7. **Brainstorm-Iterate Loop** — sabse highest-leverage habit. 6 steps: context do, 3-5 options mango,
   explicit feedback do, naye options, iterate, phir detail karo. Outline-before-drafting = same loop
   writing ke liye. Domain-agnostic.

## 03 — Beyond Text (Concepts 8-10)

8. **Multimodal** — image input strong (scene/whiteboard/handwriting) weak (fine details/counting).
   Image output: text-AI se image-prompt likhwao, visual vocabulary use karo; diffusion model (poori
   image ek sath, interrupt nahi ho sakta). Power-user recipe: SVG (Claude) → PNG → redraw (ChatGPT
   text-heavy image strength) → iterate. Audio table (transcription excellent, speaker-ID weak on 4+,
   tone unreliable).
9. **Ek Prompt Se Chhoti Apps Banana** — Goal/Input/Output recipe. Artifact = persistent editable
   object (Claude Artifacts, ChatGPT/Gemini Canvas). Hard: multiplayer, live language feedback.
10. **Data Analysis** — model code likhta/chalata hai (choose karta hai, guarantee nahi). Silent failure:
    explicitly poochho + code-block visibility check + verifiable specific demand. Bubble tea example.
    Double-check: totals, graph labels.

## 04 — Working Safely and Choosing Tools (Concepts 11-13)

11. **AI Desktop Apps & Permissions** — Cowork/OpenWork file access. 2 hard facts: deleted files
    recycle bin mein nahi jatin; edits history nahi rakhtin (no version control). Safe workflow: task →
    plan (not action) → review → approve. Permission ladder table.
12. **Cost, Speed, Model Choice** — text/speech/images/video/deep-research cost-latency table. AI
    jagged hai — same prompt 2-3 models try karo. Arena leaderboard monthly check karo.
13. **Models Checking Models** — ground truth na ho to alag-family models ek doosre ko grade karwao.
    Single-model self-critique loop (rubric 1-10, 9.5 tak iterate). Full multi-model recipe (8 steps,
    3rd family high-stakes ke liye). Caveat: score progress signal hai, truth signal nahi — high-stakes
    (legal/medical/financial) ke liye human expert zaroori.

## 05 — Recap + 12 Practice Prompts (~28 min)

13-concept one-liner recap + 12 ready-to-run prompts covering: web-search trigger, pretrained-only,
context-rich personal, neutral-framing rewrite, brainstorm-iterate, outline-first, think-hard,
grade-and-improve, image-input, small-app, data-analysis (silent-failure expose), cross-model review.

## 06 — Practice Projects

4 shippable projects (30 min–4 hrs each), chained: **Project 1 Snake Battle** (build→wish→rules→grade
→ship via Netlify drag-drop, index.html). **Project 2 Whack-a-Mole** (options-first, Goal/Input/Output
spec, rubric-score-iterate loop, model comparison). **Project 3 A Page That Is You** (novice-vs-brief
contrast, real checkable evidence, "become a stranger" grading — you can't self-grade this one).
**Project 4 AI Mini Textbook (Capstone, 2-4hrs)**: chapter (10 sections: goals/explanation/terms/
examples/mistakes/diagram/flashcards/quiz/revision-plan) + process notebook (B1-B6: topic brief,
sources, 8+ prompt log, rubric scoring, verified-claims checking table, reflection). Safety rules:
no private info, verify claims, no cheating, no invented sources. Troubleshooting table + FAQ. Note:
book's live site also has a Flashcards widget + 30-question quiz (interactive, not reproduced here).
