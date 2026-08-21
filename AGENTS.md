# Rules — LEARNING-FDE-combat-level-

*Yeh repo ki "spine" ka rules file hai — har session/run ke start mein padho. Short rakha gaya hai
(Loop Engineering course se seekha: bloated rules file har beat par cost karti hai).*

## Repo Kya Hai

Panaversity ke **The AI Agent Factory** book se guzarte hue banayi gayi study notes, "Forward
Deployed Engineer (FDE) combat-level" training ke liye. Poora naqsha aur status root `README.md`
mein hai — kaunse chapters cover hue, kaunse baqi.

## Standing Content Rules

1. **Mixed Roman Urdu + English** — hamesha, dono docs aur chat replies mein
2. **Har chapter ka apna `docs/[kebab-case-slug]/` folder** — `README.md` index + numbered
   `00-*.md`, `01-*.md`... concept-part files, book ke apne sections follow karte hue
3. **Content hamesha Zia Tutor AI MCP se nikaalo, training-knowledge se kabhi nahi** —
   `read_agent_factory_lesson` se full lesson parho, summarize mat karo apne se
4. **Naye chapter par kaam shuru karne se pehle `outline_agent_factory` se book ki authoritative
   structure confirm karo** (jaisa root `README.md` mein hai)
5. **Har chapter ke practice projects ko `docs/[slug]/projects/[project-slug]/` mein real, runnable
   scaffold do** — sirf prose steps nahi. Jo bhi applicable ho: `.claude/settings.json` (deny rules
   ya hooks), sample bad/good code, `README.md` (setup + steps + "Done jab" checklist), aur
   `AGENTS.md`+`CLAUDE.md` guardrail pointer. Koi script/hook shamil ho to **commit se pehle khud
   chala kar verify karo** (jaisa `lint_check.py`, `validate.sh` ke sath kiya) — untested script
   commit karna is repo ke "test before claiming done" pattern ke khilaf hai. Chapter ki apni
   `NN-practice-log.md` (agar hai) ko in scaffolds ki taraf link karo, sirf concept-doc section ki
   taraf nahi.
6. **Har chapter "complete" tab hi hai jab uska "Test Your Understanding" / quiz section bhi ho** —
   yeh appendices/deferred sections jitna hi zaroori hai (dekho neeche Critical Rule). Agar
   `read_agent_factory_lesson` ke outline mein aisi section dikhe, use bhi doc karo (jaisa
   `10-test-your-understanding.md` + `quiz.md` Loop aur Harness Engineering mein hai).

## ⚠️ Critical Rule (Isi Se Yeh File Bani)

**Ek chapter ko "complete" tab hi mano jab uska POORA content cover ho — appendices, "second read"
sections, aur "advanced reference" sections sameet.** Book khud kai courses ko 2 hisson mein rakhti
hai: ek "core path" (Parts 1-N, jaldi padhne wala) aur ek "deferred/appendix" hissa (jaisa Loop
Engineering ka "Routines Appendix" — jismein 4 extra practice projects the jo pehli baar miss ho
gaye the). `read_agent_factory_lesson` ka `sections` / `remaining_outline` field check karo end tak —
sirf `next: null` hone tak fetch karna "done" ka matlab hai, book ka apna "core vs deferred" split
scope-cutting ki wajah nahi honi chahiye.

## Fetch Discipline (Bade Courses Ke Liye)

- Ek window ~25K tokens se bara ho to tool-results file mein persist hota hai — Python se
  `sections`/`window_to`/`next`/`total_est_tokens` probe karo
- `from_heading=<next>` se tab tak page karo jab tak `next` explicitly `null` na ho
- Bade courses (50K+ estimated tokens) ke liye: pehla window khud parho, baqi windows ke liye
  `general-purpose` Agent background mein spawn karo (fetch + clean + concatenate ek scratchpad
  file mein) — jabke aap already-fetched hisse ke docs likhte raho. Yeh sabse effective pattern hai.
- Markdown images/`<img>`/`<iframe>` regex se strip karo, **code blocks kabhi mat chhero**

## Push Discipline

- Har chapter/batch complete hone par: `git add`, descriptive commit message +
  `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>`, `git push origin main` — bina
  puche, standing instruction hai
- Root-level files (README.md, *-Summary.md, *-Final-Prep.md, progress.md, todolist.md) badalne
  par bhi yehi push discipline chalti hai jab tak user ne alag na kaha ho

## Spine Discipline

- `progress.md` (root) — har significant kaam ke baad **Done / In progress / Open** sections
  update karo, isi pattern se jo khud Loop Engineering course sikhata hai
- `todolist.md` (root) — Active/Done/Backlog rakho, sync rakho progress.md ke sath
