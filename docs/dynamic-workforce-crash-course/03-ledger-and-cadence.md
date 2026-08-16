# 03 — Scenarios 6-7: Ledger Aur Cadence

## Scenario 6 — Ledger Jo Handoff Ho Sake (~10 min)

Aap ne is course mein jo kuch bhi kiya, ek **row** likhi: yeh gap detect hua, yeh hire propose hua, aap
ne probation par approve kiya, budget barhaya, is cost par yeh kaam resolve hua, pause kiya. **6 mahine
baad, yeh chalti hui history hi honest jawab hai.**

**Draft karo:**
```text
Play the new operator who just inherited this company. Connect to the
ledger and answer three of the five questions above from the records
alone: when each role was first needed, what each role has cost so
far, and which roles were paused and later resumed.
```

**Done jab:** Aap apni company ki ordered hiring story pakre huye ho, ledger se seedhi, har role ke
sath real cost number, aur ek staffing decision naam le sako jo yeh history badal dega.

## Scenario 7 — Cadence Par Rakho (~10 min)

Ab tak aap khud shuru karte the har scan. Weak spot: company sirf tab grow hoti hai jab **aap** dekhna
yaad rakho. **Yeh move dekhna company ko handover karta hai.**

**Routine** ek schedule par reminder hai. Waqt aane par 3 cheezein ek move mein: task **likhta hai**,
worker ko **deta hai**, usay **jagata hai**.

**Zaroori catch:** Routine hamesha assigned Worker ko ring karta hai. Lekin Worker sirf **on call** ho
to jawab deta hai. Agar off-call hai, ring khali phone par jati hai, task pada rehta hai.

| Worker Ka Setup | Routine Ki Ring Ka Kya Hota Hai |
| --- | --- |
| **On call** (wake-on-demand on) | Phone bajta hai, Worker turant task karta hai |
| **Off call, timer on** | Ring miss hoti hai, lekin timer thodi der baad task dhoond leta hai |
| **Off call, timer off** (default) | Ring dead phone par jati hai, task pada rehta hai jab tak aap khud na jagao |

**Setup 2 steps, order mein:** (1) CEO ko on call karo, (2) routine ko point karo.

**3-step build:**
```text
Step 1: Put my CEO on call... Then make a project called "Workforce
Operations."
Step 2: In the Workforce Operations project, set up a routine that
hands the CEO a "scan Northwind for capability gaps" task every Monday
morning.
Step 3: move the routine's next run to a couple of minutes from now,
then leave it completely alone... Show me the gap-scan task appear and
go from waiting, to in progress, to done or in-review on its own.
```

**Done jab:** CEO on call hai (timer off), "Workforce Operations" project mein weekly gap-scan routine
hai, aur Step 3 mein aap ne task ko khud se board approval tak jaate dekha ho, koi manual poke nahi.

## Aap Ne Kya Banaya

Aap ne workforce ko khud grow hona sikhaya, aur ek lever apne haath mein rakha jo matter karta hai. Real
gap dekha, hire likha, sasti probation par prove kiya, wahi board gate se guzara, authority sirf tab
badhi jab kamayi, phir pause/resume kiya jaise demand badli.

**Discipline ek sentence mein:** **Authority woh cheez hai jo aap extend karte ho, default nahi.** Aap
board rehte ho kaam karne se nahi — decide karne se **kaun** kar sakta hai, **kitna** kharch kar sakta
hai, **kya** chhu sakta hai — aur ek honest ledger rakh kar jo agla operator parh sake.

---
[⬅ Probation Aur Lifecycle](02-probation-and-lifecycle.md) · [⬆ Index](README.md)
