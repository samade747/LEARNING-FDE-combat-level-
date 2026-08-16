# Summary — Project 1: Watch Loop (ISS Loop)

**Concept:** 4 — In-Session Loop
**Source:** 100% official (`panaversity/agentfactory-labs`)

## Kya Sikhata Hai

Sabse simple heartbeat — **"jab tak main dekh raha hoon, chalti raho."**

## Kyun Zaroori Hai

Yeh sabse pehla, sabse chota heartbeat hai — poori loop-engineering discipline isi se shuru hoti hai.
Iske bina samajh nahi ata ke "timer kahan rehta hai" wala sawal kyun matter karta hai.

## Kaise Kaam Karta Hai

`/loop show me the location of the ISS every minute` type karte ho, aur har minute real
International Space Station ki live position aati hai (`.claude/skills/iss-position/` ek script se
NASA-tracker API fetch karti hai, kabhi memory se guess nahi karti).

**Asal lesson:** terminal band karo to watching **mar jati hai** — kyunki timer aapke apne session ke
andar rehta hai, kahin bahar nahi. In-session loop ek "kitchen timer" jaisa hai — kitchen mein ho
tabhi tak bajta hai.

## Maine Kya Test Kiya

`PYTHONIOENCODING=utf-8 python .claude/skills/iss-position/scripts/iss.py` khud chalaya — real live
position mili (26.7°N 95.1°E, North-East India). Windows-specific emoji encoding bug bhi mila aur fix
[`README.md`](README.md) mein note kiya.

---
[⬆ Poori Project List](../../README.md#runnable-projects-poore-12-har-ek-ki-real-jagah)
