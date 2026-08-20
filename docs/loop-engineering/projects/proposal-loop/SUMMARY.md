# Summary — Bonus Project: Proposal Loop

**Concept:** OODA-style state machine (observe → orient → decide → act) driving a multi-turn
exchange to a terminal state, plus spine discipline (README as permanent record).
**Source:** Inspired by a shared example ("AI Multi-Agent Marriage Proposal Loop", Gemini-based,
real people's inboxes) — **not** an official book project. Rebuilt here with fictional personas,
one real mailbox, and Claude instead of a separate LLM API.

## Kya Sikhata Hai

**Ek loop do "voices" chala sakti hai** agar state machine clearly define ho — har state par
decide karo agla message kaun bhejega aur kya likhega, jab tak terminal state (ACCEPTED /
REJECTED_HARD) na aa jaye. Yeh bilkul wahi shape hai jo daily-triage capstone mein thi (PASS ya
escalate), sirf yahan "checker" ki jagah "conversation state" hai.

## Kyun Zaroori Hai

Asal duniya mein event-driven loops (jaise Project 6 ka Doorbell) bhi isi tarah kaam karte hain:
ek trigger aata hai, loop uska "state" samajhta hai, aur us state ke mutabiq agla action leta hai —
kabhi khud jawab de deta hai, kabhi insaan tak escalate karta hai. Yahan "insaan tak escalate"
ki jagah "conversation terminal state tak pahonchna" hai.

## Kaise Kaam Karta Hai

Is session mein already-connected Gmail MCP connector (`samad.x747@gmail.com`) use kiya — koi
alag Python script ya API key nahi, Claude khud tool calls kar ke dono personas (Rayan, Meher) ki
taraf se likhta gaya. Har reply **real Gmail thread** mein gaya (`create_draft` +
`replyToMessageId`, phir `send_message(draftId=...)`), sirf naya email nahi. Do independent paths
chalaye — Hard Rejection aur Joyful Acceptance — dono real bheje gaye, spam se bachne ke liye har
path sirf 5 messages tak limited rakha.

**Privacy design choice:** original example ke real logon ke naam/emails ki jagah fictional
personas aur ek hi real (apni) mailbox use ki — taake koi third-party ki private info repo mein na
aaye.

## Maine Kya Test Kiya

Dono threads live bheje aur unke **real message IDs** confirm kiye (README mein poora log hai).
Path 1 → `REJECTED_HARD` (5/5 sent), Path 2 → `ACCEPTED` (5/5 sent). Threading verify ki —
`create_draft` ka returned `threadId` first message ke id se match hua, matlab replies asal mein
usi thread mein gayin, alag emails ki tarah nahi.

---
[⬆ Poori Project List](../../README.md#runnable-projects-poore-12-har-ek-ki-real-jagah)
