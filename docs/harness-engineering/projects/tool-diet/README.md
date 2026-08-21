# Harness Project 4 — The Tool Diet

**Concept:** 6, 7 · **Time:** 1-2 hrs, phir ek hafta beats · **Difficulty:** Medium

Yeh project naya scaffold nahi maangta — apni **already-built triage loop** (Loop Engineering ka
[`daily-triage-demo`](../../../loop-engineering/projects/daily-triage-demo/)) use karo. Kaam sirf uski
tool list ko kaatna hai.

## Steps

1. `daily-triage-demo/.claude/settings.json` (aur agar koi skill/subagent config hai) mein list karo
   loop kaunse tools dekh sakti hai — `Bash`, `Read`, `Write`, `Edit`, koi connector, etc.
2. Har tool ke liye poocho: "kya `daily-triage` skill ko yeh **asal mein** chahiye?" — jo nahi, use
   `permissions.deny` ya `allowedTools` se hata do.
3. `tool-list-worksheet.md` (isi folder mein) fill karo — before/after list.
4. Ek hafta (ya kam se kam 5-6 real runs) chhoti list pe chalao, `progress.md`/log mein note karo
   kabhi "wrong tool" incident hua (agent ne galat tool try kiya, blocked hua, ya confuse hua).

## Done jab (self-check)

- [ ] Before/after tool count worksheet mein likha
- [ ] Wrong-tool incidents ka before/after compare kiya (ya confirm kiya list pehle se hi lean thi —
      yeh bhi ek valid result hai)

---
[⬆ Harness Practice Log](../../11-practice-log.md) · [Poori list](../../07-practice-projects.md)
