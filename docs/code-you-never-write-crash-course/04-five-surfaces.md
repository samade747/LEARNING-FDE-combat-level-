# 04 — Part 3: Ek Problem, Paanch Surfaces (Concepts 9-11)

Part 1-2 ki saari skills har jagah same chalti hain. Jo change hota hai: **code kahan chalta hai,
aur kya touch kar sakta hai.** 3 kisam ki jagah: browser sandbox (Claude.ai/ChatGPT/Gemini),
**terminal** (plain text window jahan tum computer ko instructions type karte, apne folder ke andar
khula — Claude Code, OpenCode), desktop app (Cowork, OpenWork).

> **Running job:** 12 monthly expense CSVs ka folder. Merge karo, category se total, duplicate
> transactions flag, one-page HTML report + chart.

Bank/school portal/fitness app, almost har "export"/"download" button CSV deta hai, Excel bhi same
tarah khulti/save hoti.

## Concept 9 — Claude.ai: Home Surface (ChatGPT, Gemini)

Browser chat jahan yeh course rehta, zyadatar code problems yahan solve hongi. Code AI company ki
taraf **sandbox** mein chalta hai — uploads jate hain, results/files/charts aate hain, **tumhare**
computer par kuch touch nahi hota. **Yeh zero-risk surface hai seekhne ke liye.** ChatGPT/Gemini
same tareeqe se kaam karte.

Running job yahan chalaya: 12 CSV attach karo, merge/total/flag-duplicates/HTML-report maango,
rules do (comma separators, refunds negative, unparseable rows skip+list). Finished HTML page
aati, Concept 6 checks run karo (row count match? ek mahina jo jaante ho sahi dikhta?).

| Strength | Limit |
|---|---|
| Zero installation, zero machine risk | Sandbox sirf jo upload karo dekhta — 40 files = 40 uploads |
| One-off/exploratory jobs ke liye perfect | Sandbox temporary — scripts download karo ya chat ke sath "die" ho jate |
| Full brief→code→verify→iterate loop visible | Recurring jobs = har baar re-upload, tedious daily |

**Boundary:** Chat sandbox workshop hai jo visit karte ho — tumhari files ka ghar nahi. Jab problem
tumhare computer/folders/routines ke baare mein ho jaye, tum visit se bade ho gaye ho.

## Concept 10 — Claude Code & OpenCode: Agent Tumhare Folder Mein

**Claude Code** (Anthropic) aur **OpenCode** (open-source, many models). Dono terminal mein rehte.
Picture: **terminal ek chat box hai jo folder ke andar baitha hai.** Install karne ke baad sentences
type karte ho, **agent** (multi-step kaam karne wala, files par act kar sakta AI) answer karta.
Agent files already-there dekhta — upload nahi — code chalata, scripts forever save karta, apne
errors khud fix karta.

Running job dobara: folder path bolo, files simply _there_ hain. No attachments. Next January:
"monthly-report script ko 2026 folder par chalao."

Yeh surface sabse demanding jobs ke liye: code jo apne machine par chale, schedule par, systems
touch kare jo browser tab kabhi nahi pahunch sakta. (Network engineer example — 40 devices daily
health check.)

**Claude Code vs OpenCode?** Same chat-in-folder experience. Claude Code polished, Claude chalata.
OpenCode model choose karne deta, free/self-hosted bhi. Dono mein seekho.

> Non-programmers yahan bhi fit hote — in tools ki marketing developers ke liye hai, par boundary
> galat hai. "Chat with an agent jo yeh folder dekh sakta" code jaanne ki zaroorat nahi — **tumhari
> files aur tumhara problem** jaanne ki zaroorat hai.

## Concept 11 — Cowork & OpenWork: Delegation Ek Safety Ritual Ke Sath

**Claude Cowork** (Anthropic), **OpenWork** (open-source, Different AI) — desktop apps, terminal
jaisi file-touching power, normal application window mein, knowledge workers ke liye (developers
nahi). Underneath: folder reorganize ya report build karte waqt yeh aksar **code likh+chala**
rahe hote — same Python, different clothes.

Defining feature: **plan-then-approve** — app plan likhta, approval ka wait karta. Running job do
to plan reply mile ga: "12 CSVs parhunga, in columns par merge karunga, refunds negative treat
karunga, duplicates flag karunga bina delete kiye, report.html banaunga." Plan **plain English**
mein parho, galat assumption pakdo kuch chalne se pehle, approve karo. **Yeh Concept 6 ka
plain-English replay hai — work se pehle move kiya gaya, baad mein nahi.**

| Situation | Reach for | Why |
|---|---|---|
| One-off question, ek/kuch files | Claude.ai/ChatGPT/Gemini | Upload, compute, check, done |
| Learning/borrowed computer | Claude.ai | Sandbox kuch hurt nahi kar sakta |
| Folders mein repeat hoga | Claude Code/OpenCode | No upload, scripts stay, errors heal |
| App chahiye + plan approve karna | Cowork/OpenWork | Plan-then-approve built-in |
| Schedule par chale, doosre systems touch kare | Claude Code/OpenCode | Sirf apne machine ka code so-ke-waqt chal sakta |

**Honest advice:** Claude.ai par raho jab tak uploading hafte ki annoying cheez na ban jaye — wohi
graduation signal hai (Agentic Coding Crash Course, Cowork Crash Course aage wait kar rahe).
