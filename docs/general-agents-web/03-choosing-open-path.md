# 03 — Choosing, Aur Open Path

## Concept 10: Web, Desktop, Ya Terminal — Jo Kaam Touch Kare Uske Hisaab Se Chuno

Rule chhota hai: **jo kaam touch kare uske hisaab se chuno.**

| Kaam Ko Chahiye... | Surface | Course |
| --- | --- | --- |
| Connector-and-document kaam, devices ke darmiyan continuity, kuch install nahi | **Web** | Ye course |
| Kaam jo machine band hone pe bhi chale | **Web** (repo work ke liye, cloud Routine) | Loop Engineering |
| Aapki local files, desktop apps, browser jahan aap login ho | **Desktop** | Cowork & OpenWork |
| Code, repositories, command line | **Coding agents** | Agentic Coding |
| Regulated data (PHI, privileged matter, financial data) | **Koi nahi, abhi** — pehle compliance se likhit jawab lo | Cowork course |

**Regulated data ka apna paragraph:** Tiers 1 aur 2 vendor ki custody hain **by definition**. Isliye
sawal *"ye surface careful hai?"* nahi — sawal hai *"ye data is custody mein rehne ki ijazat hai?"* Sirf
compliance team, **likhit mein**, ye jawab de sakti hai.

**Ek rule jo mix ko mess banne se rokta hai:** **jaano har deliverable kaunse tier mein utri.** Tier 3
mein deliverable (Drive, repo, firm records) ko farq nahi parta kaunse surface ne banaya.

### Self-Check
**Sawal:** 3 tasks: (a) Slack/Notion se weekly summary, travel ke dauran bhi. (b) laptop pe 200 files
clean karna. (c) privileged client documents se memo. Route karo, deciding fact naam do.
**Jawab:** (a) **Web** — sirf connectors touch karta hai, machine band hone pe bhi survive karna chahiye.
(b) **Desktop** — local filesystem touch karta hai, jo browser-only remote session khud reach nahi kar
sakti. (c) **Koi nahi, abhi** — privileged matter custody ka sawal hai, compliance likhit jawab de pehle.

## Concept 11: Open Path — Koi Vendor Cloud Nahi

Is course ne is book ka pattern tora — dono tabs (Cowork web, ChatGPT Work) **closed products** hain.
**Asal sawal:** kya ye surface bina kisi vendor cloud ke ho sakti hai?

**Haan, mehnat se. 2 open paths:**

- **OpenWork, remote/shared workspaces** — self-hosted OpenWork worker (URL + access token), ya
  organization ke shared cloud workers. **Machine doing the work aap dekh rahe machine nahi — lekin
  infrastructure aap ya aapki organization control karti hai.**
- **OpenCode, apna scheduler** — repo-attached kaam ke liye, cron ya GitHub Actions apne clock pe.
  Koi vendor cloud nahi, koi plan tiers nahi.

**Trade, saaf lafzon mein:** **Companies aapko spine bech dete hain. Open path aapko banana parta hai.**
Vendor surface pe, sab kuch pehle din se kaam karta hua milta hai — sessions, sync, phone gate,
scheduler. Lekin ye unki custody, unke format, unki keemat mein rehta hai. Open path pe, sab kuch aapko
setup, chalana, fix karna hai — badle mein: **custody** (aapke control ki machines pe data) aur
**choice** (kaunsa model aapke prompts dekhta hai).

> **Simple:** Vendor ka surface ek furnished office hai — desk, drawers, doorbell, sab pehle din se kaam
> karte hue, unki building ke andar. Open path ek khaali kamra hai jo aap khud furnish karte ho — zyada
> mehnat, lekin aapki building, aapke rules.

### Self-Check
**Sawal:** Ek NGO weekly donor-report automation chahti hai. Unki data policy donor records ko third-
party consumer platforms pe rakhne se mana karti hai, koi engineer bhi nahi. Kaunsa path force hota hai,
kya khota hai, honest sentence kya hai?
**Jawab:** Policy **open path** force karti hai — donor records vendor platform ke Tiers 1/2 mein nahi
ja sakte. Wo khoti hain: free spine, sync, phone gate, managed scheduler — jo ab kisi ko banani/chalani
hai. Honest sentence: *"Ye path subscription fee ko ek operator se trade karta hai. Koi to yahan
setup, updates, aur wo subah jab ye tootey, uski zimmedari le. Bina engineer ke, yehi asal decision hai,
software nahi."*

## Concept 12: Ye Surface Kya Nahi Kar Sakti

**Surface kaam behtar nahi banati.** Remote session weak brief ko **unattended** bana deti hai, **behtar
nahi**. Har quality lever aapki taraf hai: brief (8), plan review (aapka akela intercept), tier decision
(5), gate test (7), walked-before-scheduled rule (9).

**Surface hafton purani, metered, staged, aur vendor-shaped hai.** Har mechanical fact yahan (plan
tiers, run limits, button names, product names bhi) is book ka sab se tezi se purana hone wala material
hai. **Lasting layer** yehi hai jo aapko le kar jana chahiye: stop-typing test, window-not-runtime
architecture, 3 tiers ki 1-line discipline, 6-part reading lens, 4-step loop, schedule ke 4 jawab.

> **Ek discipline poore churn se bachati hai:** **kuch bhi zaroori sirf platform pe nahi rehta.** Tier
> 3, hamesha, kisi bhi cheez ke liye jise khona bura lagega.

**Agla safar:** Cowork & OpenWork (knowledge workers ke liye), Agentic Coding (engineers ke liye),
Spec-Driven Development (brief ko spec banana), Loop Engineering (schedules jo **act** karein), Harness
Engineering + Trusting the Checker (safe + measurable), Leaving the Laptop (runtime decision).

> **Closing thought:** Chat box wahan hai jahan aap design karte ho. Agent surface wahan hai jahan wo
> chalta hai. July 2026 mein dono ek address pe move ho gaye, aur division of labor sharper hui, kamzor
> nahi. **Shape seekho. Address dobara badlega.**

---
[⬅ Working Unwatched](02-working-unwatched.md) · [Agla: Practice Projects ➡](04-practice-projects.md)
