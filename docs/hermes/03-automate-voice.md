# 03 — Automate Aur Voice (Scenarios 6-7)

## Scenario 6: Khud Se Act Karo, Phir Brain Backup Karo (~15 min)

### 6a: Ek Scheduled Job, Plain Language Mein

```text
Set up one scheduled job in natural language and deliver it to
my phone: every weekday at 8am, a short morning digest built from
what you already know about me, my notes, and what we worked on
recently. Show me the schedule before you save it, and run it
once now.
```

Ye pehla job **jaan-boojh kar** koi outside tool nahi maangta — memory files + recent notes se digest
banata hai, jo scheduled run ke paas hamesha hoti hain.

> **Ehtiyat: Scheduled jobs leaner chalti hain aapke live chat se.** Fresh session mein wake hoti hai,
> default mein **koi web search nahi, koi messaging tools nahi** (scheduler khud delivery karta hai).
> Web se fresh info chahiye ho to: `enabled_toolsets=["web"]` set karwao us specific job pe.

**6a done jab:** Scheduled job exist karti hai **aur** test run fire ho kar digest phone pe unattended
ata hai.

### 6b: Worker Ko Backup Karo

Ab tak Hermes ke paas kuch hai jo protect karne layak hai: ek skill jo usne likhi, aapka model, ek
routine — ek ghanta pehle in mein se kuch exist nahi karta tha.

```text
Back everything up so I won't lose what it has learned, and show
me how I'd restore it on a new machine. Confirm the backup
captured config, skills, memories, and sessions.
```

> **Upgrade jo maang lo:** Workspace ko **private Git repo** mein backup karwao, zip nahi. Har skill ki
> **poori history** mil jati hai timestamp ke sath — cheapest tareeqa dekhne ka agent ka behavior kaise
> badla, aur galat lesson seekha to rollback karne ka.

**Done jab:** Job khud phone pe chalta hai, backup exist karta hai, aur `hermes import` one-liner saved
hai. **Aapka AI Employee ab neend mein bhi kaam karta hai, aur dead laptop survive karta hai.**

## Scenario 7: Voice Do (Bonus, ~10 min)

**Goal:** Telegram bot ko message karo, wo **spoken audio** se jawab de, free, koi nayi key nahi.

```text
Give my Hermes a voice: set it up so when I message my Telegram
bot it replies with audio I can listen to, using the free option.
```

Agent voice package + `ffmpeg` install karta hai, free **Edge** default text-to-speech set karta hai,
Telegram ke liye Auto Voice Reply on karta hai. **Sab non-interactive hai.**

**Done jab:** Phone se message bhejo, spoken reply mile jo aap play kar ke sun sako.

> **Bonus:** Ek **microphone loop** terminal se chal sakta hai — local mic sunta hai, apni machine pe
> transcribe karta hai, usi free Edge voice se jawab deta hai — hands-free chat.

---
[⬅ Memory Aur Model-Swap](02-memory-model-swap.md) · [Agla: Monthly Audit + Beyond ➡](04-beyond-audit.md)
