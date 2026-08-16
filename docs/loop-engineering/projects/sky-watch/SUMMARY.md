# Summary — Project 3: Sky Watch

**Concept:** 6 — Unattended Schedule (Routine)
**Source:** 100% official (`panaversity/agentfactory-labs`)

## Kya Sikhata Hai

Loop jo **laptop band hone ke baad bhi** chalti hai — kisi aur ki machine (Anthropic ke cloud
servers) par.

## Kyun Zaroori Hai

Yehi wo heartbeat hai jo "loop engineering" ko asal mein matter karti hai — kaam **bina aapke, so'te
waqt** hota hai. Project 1 (in-session) se seedha contrast hai: yahan timer aapke session ke **bahar**
rehta hai.

## Kaise Kaam Karta Hai

```text
/schedule every day at midnight, run the sky-watch skill for today and write me the forecast
```

Har raat, laptop khula ho, so'ta ho, ya bag mein ho — yeh chalti hai, NASA se asteroid data check
karti hai, subah ek forecast ready hota hai. **Asal lesson:** yeh "forward-looking" hai (kal ki
warning, aaj ki nahi jaisa Project 6/Doorbell hai) — aur **quiet din bhi "all clear" bolti hai**, yeh
failure nahi hai, yehi ek watch ka poora point hai.

## Maine Kya Test Kiya

`python .claude/skills/sky-watch/scripts/skywatch.py` khud chalaya — real NASA data mila: 1 flagged
hazardous asteroid (`2014 UR116`, 157.8× the Moon distance), 27 close approaches agle 7 din mein.

---
[⬆ Poori Project List](../../README.md#runnable-projects-poore-12-har-ek-ki-real-jagah)
