# 04 — Automate Karna Aur Monthly Audit (Scenarios 6-7)

## Scenario 6: Khud Se Act Karna (~15 min)

Ab tak aap message karte thay, agent reply karta tha. **Schedules ye ulta karti hain** — agent clock/
interval pe act karta hai, bina aapke message kiye.

**3 flavors:**
- **Cron** — precise times ("har subah 7am", "Monday 9am") — **sab se zyada use hota hai**, aapki
  zindagi clock times pe organized hai
- **Heartbeat** — ambient checks fixed cadence pe ("har 30 minute urgent unread scan karo")
- **Hooks** — event triggers (webhook fire, session reset) — out of scope yahan

**Scenario 2 hisson mein:** 6a ek fast demo hai (proactive mechanism wired hai prove karta hai), 6b
**asal keeper** hai (real schedule jo kal aapko serve kare).

### 6a: Demo Heartbeat Dekho (Phir Band Karo)

```text
Schedule a five-minute demo heartbeat with a low-cost task: every
five minutes, check the gateway log for errors and post a one-line
summary. Once I see one fire in the log, disable just this demo.
```
**Done jab:** Log mein ek heartbeat-driven tool call dikhi **aur** demo disable ho chuki.

### 6b: Ek Real Schedule Rakho

```text
I'd like to add one real schedule that actually serves me. Look at
what you know about me from USER.md and suggest two or three
options I might keep.
```
Agent options deta hai (7am summary, Monday priorities list, end-of-day check). Jo chuno:
```text
Go with the [name your choice]. Set it up, confirm when it'll next
fire, and commit the schedule file to my backup repo.
```
**Done jab:** Chuni hui schedule chal rahi hai, backup repo mein committed hai, agent ne bataya agli
dafa kab fire hogi. **Chhoro isay on.**

## Scenario 7: Monthly AI Employee Audit (~10 min/mahina)

Aapka AI Employee waqt ke sath **accumulate** hota hai: skills, credentials, MCP tools, memory entries,
autonomous tool calls. **Har addition ek chhota approved decision hai — chain opaquely compound hoti
hai.** Defense install-time vigilance nahi (jo exist nahi karta, wo aap pakar nahi sakte) — **fixed
cadence pe 10-minute review.**

```text
Run my OpenClaw monthly audit. Walk through everything that's been
installed, stored, scheduled, or written since the last audit, and
flag anything I didn't explicitly approve.
```

**Done jab:** 10 minute report review kiya ho **aur** kam se kam ek decision liya ho (bhoola hua
credential delete, over-broad approval revoke, stale memory prune, unused skill uninstall). **Agle
mahine ke liye calendar mark karo.**

---
[⬅ Skill Aur Tool](03-extend-skill-tool.md) · [Agla: NemoClaw Sandbox ➡](05-sandbox-nemoclaw.md)
