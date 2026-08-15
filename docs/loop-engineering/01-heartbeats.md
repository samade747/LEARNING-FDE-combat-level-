# 01 — Heartbeats: Loop Kab Start Hota Hai

Heartbeat wo cheez hai jo har run start karti hai. **4 kisam** hote hain — "jab tak session khula hai
repeat karo" se lekar "bina kisi insaan ke chalta rahe" tak.

| Heartbeat | Analogy | Kahan rehta hai timer |
| --- | --- | --- |
| **In-session** | Kitchen timer — sirf tab tak bajta hai jab tak aap kitchen mein ho | Aapki open session ke andar |
| **Conditional (run-until-done)** | "Jab tak taster na kahe ready hai, pakate raho" | Ek checker decide karta hai |
| **Scheduled** | Alarm clock — chahe ghar ho ya na ho, waqt pe bajta hai | Scheduler (cron / cloud) ke andar |
| **Event-driven** | Doorbell — jab tak koi bell na dabaye kuch nahi hota | Event catcher (Routine/Channel) |

**Bunyadi baat:** loop ek single action nahi hota. Ye hai "kaam karo, wait karo, phir karo" — baar baar.
Sawal sirf ye hai ke ye "jaagne wali cheez" **kahan rehti hai**.

- **In-session loop** ka timer aapki **open session** mein hota hai. Session band = timer khatam.
- **Scheduled task/Routine** ka timer **bahar** hota hai, ek scheduler pe jo kabhi sota nahi. Har tick
  pe ek nayi, chhoti si run shuru hoti hai, kaam khatam, phir band — agli baar phir nayi.

---

## Concept 4: In-Session Loops (Jab Tak Aap Dekh Rahe Ho)

Sab se simple heartbeat. Ek prompt ko timer pe dobara chalate ho **jab tak session khula hai**. Achha
hai jab aap kisi cheez ko "watch" karna chahte ho — deploy, lamba test run, CI job.

**Claude Code:**
```text
/loop 5m check if the deployment finished and tell me what happened
```
Cancel karne ke liye:
```text
show my running loops
cancel the deploy-check loop
```

**OpenCode** (koi `/loop` command nahi, shell se banana parta hai):
```bash
while true; do
  opencode run "check if the deployment finished; if it did, say DONE"
  sleep 300   # 5 minutes
done
```

**3 rungs — kitna "awake" rehna padta hai:**

| Rung | Option | Terminal band hone ke baad chalta hai? | Laptop so jaye to bhi chalta hai? |
| --- | --- | --- | --- |
| Bottom | In-session `/loop` | Nahi | Nahi |
| Middle | Background session (`--bg`) with `/loop` | Haan | Nahi (machine on chahiye) |
| Top | Scheduled task / Routine | Haan | Haan (cloud pe chalta hai) |

**Real project (15 min):** ISS Loop — real International Space Station ki location har minute
dikhata hai. Terminal band karo, watching mar jati hai — yehi is concept ka poora point hai.

---

## Concept 5: Conditional Loop / Run-Until-Done

Ye timer pe nahi rukta — ek **condition** pura hone pe rukta hai. Jaise: "Tests pass hone tak chalao"
na ke "5 minute baad phir check karo".

**Zaroori usool:** Jo agent kaam karta hai, wahi apna kaam approve nahi kar sakta. Ek **alag command
ya checker** decide karta hai ke "done" hai.

**Claude Code — `/goal`:**
```text
/goal All tests in test/auth pass and `npm run lint` is clean.
```
Har turn ke baad, ek chhota alag model (default Haiku) transcript parh kar puchta hai "kya hum done
hain?". Checker khud commands nahi chala sakta — sirf jo output dikhta hai wahi dekhta hai. Isliye
condition aisi likhni chahiye jo **command se prove ho sake**, jaise "tests pass, lint clean" — na ke
"auth code achha hai".

**OpenCode — shell se:**
```bash
for i in $(seq 1 8); do          # tries ki hadd — kabhi bhi hamesha ke liye loop na karo
  opencode run "Make the tests in test/auth pass and fix any lint errors."
  if npm test -- test/auth && npm run lint; then
    echo "Condition met on try $i"; break
  fi
done
```

### Har Loop Ke 3 Zaroori Stops

| Stop | Kya hai | Na ho to kya hota hai |
| --- | --- | --- |
| **Success condition** | Loop ko kaise pata chale kaam khatam | "Done" define hi nahi hoti |
| **Limit** | Max tries / minutes / spend | Impossible goal poora token budget kha jata hai |
| **No-progress check** | Same mistake baar baar to ruk jao | Puri limit ek hi ghalti dohrane mein khatam |

**Ralph loop:** Sab se simple mashhoor run-until-done loop. Same prompt baar baar chalta hai, ek state
file parhta/update karta hai. Sirf 2 stops rakhta hai (success + time cap) — na stuck-check, na
separate checker. Isi wajah se lesson clear sikhata hai: vague condition wala Ralph loop time cap tak
bhatakta rehta hai.

**Doom Loop se bacho:** Lambi run apne hi context mein purana tool output, dead ends jama karti rehti
hai — jitna zyada mess, utna kharab decision, jo aur mess banata hai. Bachaav: lambi runs ko **compact**
karo (summary bana do), bara output **files** mein rakho (context mein pointer rakho), messy subtasks
**subagent** ko do.

---

## Concept 6: Unattended Schedules (Aap Sote Waqt Bhi Chalta Hai)

Yehi heartbeat loop engineering ko matter karta hai — kaam chahe aap computer pe ho ya na ho.

**Claude Code — Routines:** Anthropic ke servers pe chalne wali cloud automation. Laptop khula ho,
sota ho, ya bag mein ho — farq nahi parta.

**Har Routine ke 4 blanks:**

1. **Prompt** — kya karna hai (goal + rules + "done" ka matlab)
2. **Repos** — kin repos ko chhoo sakta hai
3. **Connectors** — kin cheezon tak pohanch sakta hai (Slack, email...)
4. **Trigger** — kab shuru hoga (schedule / API call / GitHub event)

```text
/schedule every weekday at 9am, run the daily-triage skill   # banana
/schedule list                                               # dekhna
/schedule run the triage routine now                         # abhi chalana
/schedule update the triage routine to every two hours        # timing badalna
```

**2 zaroori rules yaad rakho:**

- **Daily cap hoti hai** (launch pe: 5 Pro, 15 Max, 25 Team/Enterprise per din). Apna arithmetic pehle
  kar lo — Routine cap pe chup chaap ruk sakti hai.
- **Sirf `claude/` branches pe push kar sakta hai** (default). `main` pe seedha nahi likh sakta — ye
  safety hai, hurdle nahi.

**OpenCode — apna cron ya GitHub Actions** (koi vendor cloud zaroori nahi):
```bash
0 9 * * 1-5 cd /path/to/repo && opencode run "check the CI dashboard and summarize any failures"
```

**Real project (overnight):** Sky Watch — har subah NASA ke asteroid feed se check karta hai, dangerous
kuch ho to bataता hai. Schedule bana ke laptop band karo — subah forecast wahan hoga.

---

## Concept 7: Event-Driven (Jab Kuch Ho To React Karo)

Schedule kehta hai "har ghante check karo". Event kehta hai "jis waqt X ho, react karo". PR khulta hai,
message aata hai, aur loop turant chalta hai.

| Event kahan se aata hai | Use karo | Kaam chalta hai | Laptop band? |
| --- | --- | --- | --- |
| GitHub (PR, release) | Routine, GitHub trigger | fresh cloud session | chalta hai |
| GitHub, Routine ke bagair | Claude Code GitHub Action (CI) | fresh CI runner | chalta hai |
| Chat message (Telegram, Discord) | Channel | already running session | nahi, machine chahiye |
| Koi bhi web request | Routine, API trigger | fresh cloud session | chalta hai |

**Asal sawal:** "Ye Routine hai ya nahi" nahi — balke **"kaam kis ke computer pe chal raha hai?"**
Aapka apna laptop band hone pe mar jata hai. Anthropic ke servers ya GitHub ke runners nahi, kyunke wo
kabhi aapke thay hi nahi.

**Real project:** The Doorbell — kisi ne PR khola aur bina kisi prompt ke review a jata hai. Laptop band
karo, koi aur PR khole to bhi review ata hai — kyunke ye kabhi aapki machine pe chal hi nahi raha tha.

---

## Konsa Heartbeat Chuno?

Sab se **halka** loop chuno jo fit ho:

- **Kaam khatam hota hai aur command prove kar sakti hai** → Conditional loop
- **Kaam repeat hota hai** → Schedule ya Event
- **Kaam ek dafa hota hai** → Koi loop nahi — simple session hi sahi tareeqa hai

---
[⬅ Overview](00-overview.md) · [Agla: Body ➡](02-body.md)
