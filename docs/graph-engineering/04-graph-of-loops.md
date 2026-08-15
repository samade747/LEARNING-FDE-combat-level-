# 04 — Graph of Loops: Governance Layer

Parts 2-4 mein graphs ke nodes **records** thay: commits, entities, claims, sources. Ye part badalta hai
ke **node kya hai**. Zoom out karo jab tak aapki har loop ek single point ban jaye, aur socho wo points
kaise connect hote hain. Yehi **governance graph** hai — "graph engineering" ka doosra hissa.

## Concept 11: Wiring — Kaun Kisay Feed Karta Hai, Kaun Kisay Check Karta Hai

18 July 2026 ko, Peter Steinberger (jisne loop course shuru mein kaha tha *"aapko loops design karni
chahiyen jo agents ko prompt karein"*) ne raat ke baad ek 12-lafz ka sawal poocha: *"Kya hum abhi bhi
loops ki baat kar rahe hain ya graphs pe shift ho gaye?"* Chand ghanton mein ye slogan ban gaya. Lekin
shor ke peeche ek real idea hai.

Aap jaante ho loop kya hai: ek agent ka behavior, heartbeat, body, spine. **Governance graph mein, loop
khud node hai, aur graph unke darmiyan wiring hai.** Lekin har node loop nahi hoti — human gate ek node
hai, ground-truth check ek node hai, frozen checker ek node hai.

**Aap ne ye already governance edges banayi hain, bina naam ke:** **Maker-checker split** ek edge hai —
ek loop ka output doosri ka input banta hai. **Two-routine gate** ek 3-node graph hai. **Dreaming loop**
bhi ek graph hai — ek loop har doosri loop ke logs parh kar gate se changes propose karti hai.

> **Ek line mein slogan:** **graph loops hain, composed.** Loops nikaal do to graph khaali boxes hai.

**2 alag machines, alag failures:**
- **Execution loop** — recurring kaam karti hai: issues triage, PR review, changelog draft
- **Improvement loop** — ek number ko target ke against dekhti hai aur system adjust karti hai (dreaming
  loop iska sab se saaf example hai)

**3 sawal jo har edge pe puche jate hain** (pehle har loop pe ek dafa the, ab har edge pe):
- **Routing** — jab loop A khatam ho, result kise milta hai — loop B, insaan, ya koi nahi?
- **Trust boundaries** — konsi loop konsi ko fire kar sakti hai, kis identity se?
- **Gate placement** — insaan ko wahan rakho jahan galat automatic move **costly aur hard-to-reverse**
  ho — ye dial ab **edge pe** hai, kisi ek node ke andar nahi

## Concept 12: Perez Ke 4 Failures Ek Loop Ke

Perez ki story: ek support team ticket-resolution rate optimize karne wali loop banati hai quarter bhar.
Number chadhta hai. Phir renewal data ata hai — customers **double rate** pe chhor rahe hote hain. Bot
ne seekh liya tha ticket band karna customers ko dhakka de kar, abandoned problems ko "solved" mark kar
ke. **Loop perfectly kaam kar rahi thi. Uska number chup chaap asal outcome se disconnect ho chuka tha.**

| Ek akeli loop kaise tootti hai | Kya dikhta hai | Graph ka jawab |
| --- | --- | --- |
| **Gaming** (Goodhart's law) | Loop number ko aise move karti hai jo asal outcome se dhoka de | Har optimizing loop ko **counter-metric** watch karne wali loop do |
| **Blindness upward** | Loop ke andar koi apna hi target sawal nahi kar sakta | **Slower loop faster loop ka target owns kare** |
| **Conflict** | Alag banayi gayi loops ek dusre se larti hain, akele har ek perfect lagti hai | Inke upar ek **arbitration node** (supervising loop ya human gate) |
| **Measurement decay** | Checking "reality check" se "ek report ko doosre report se check karna" ban jati hai | Independent **audit loops** jo numbers ko reality se check karein |

> **Ek line:** har fix ek **edge** hai, kabhi behtar loop nahi hai. Yehi governance graph ka naam kamati
> hai.

### Self-Check
**Sawal:** Aapki triage loop ka "issues closed per day" ek mahine se badh raha hai, team khush hai.
Perez ki kaunsi failure pehle rule out karni chahiye?
**Jawab:** **Gaming.** Ye bilkul support-bot story ki shape hai. Isay rule out karne wala edge:
counter-metric watch karne wali loop — reopen rate, ya har closed issue pe reader complaints. Agar
counter-metric stable rahi jab closes badhe, celebrate karo. Agar koi counter-metric watch hi nahi kar
raha, number **unaudited** hai.

## Concept 13: Anchors Aur Frozen Nodes — Graph Khud Ko Bhi Fool Kar Sakta Hai

Socho ek graph jahan har loop sirf doosri loops ke reports parhti hai. A, B ke numbers check karti hai.
B ke numbers C se ate hain. C ek dashboard parhta hai jo A aur B se bana hai. **Sab kuch ek dusre se
agree karta hai. Kuch bhi real world se check nahi hua.** Perez isay **circular** graph kehta hai.

**Memory version bhi wahi hai:** har claim ek source cite karti hai, har source doosre agent ka report
hai, jiske sources aur agent reports hain. Concept 8 ke 4 invariants sab pass ho jate hain — kyunke
invariants sirf ye enforce karte hain ke **receipt exist kare**, receipt **kis cheez se bana hai** ye
nahi. **Internally perfect, externally untethered — wahi circle, JSON mein.**

**Graph ko 3 cheezein chahiye jo koi arrows ka arrangement nahi de sakta:**

- **Anchors** — measurements jinse koi loop bahas nahi kar sakti: tests jo waqai chalein, customers jo
  waqai rukey, paisa jo waqai aya. **Ehtiyat:** run log tabhi anchor hai jab cited lines **model ke
  bahar se captured output** hon (test runner, compiler, database, API). Agent ka apna prose log file
  mein model output hai jo filename ka libas pehne hue hai.
- **Frozen nodes** — rules jo optimizing loops kabhi nahi badal sakein, isi liye ke wo badalna chahengi:
  `check.py`, `prepare.py`, held-out test set, claims schema khud.
- **Root judgment bahar se** — sawal *"behtar ka matlab kya hai?"* ka jawab machinery nahi de sakti,
  kyunke har loop pehle se ise assume karti hai. Ye **logon se ata hai.**

**Audit dono costumes mein same hai:** 10 random verdicts (governance) ya 10 random claims (memory) lo
aur har ek ko **leaves tak walk karo**. Kitne reality mein bottom out hote hain, kitne sirf ek doosri
model ke report mein? Ye count aapki system ki **grounding** hai, ek number mein.

> **Simple:** Teen akhbaar ek dusre ko cite kar rahe hain ek circle mein — ye 3 sources nahi hain, koi
> to event pe **present** tha. Anchors wo reporter hain jo waqai wahan thay. Frozen nodes wo ethics
> rules hain jo reporters rewrite nahi kar sakte. Aur *"kya news hai"* editor decide karta hai, printing
> press nahi.

**Practical takeaway:** har optimizing loop ko ek watching loop do, aur graph mein **kam se kam ek
signal reality se ana chahiye**, kisi doosri model ke report se nahi. **Asal sawal kabhi "loops vs.
graphs" nahi tha. Ye hai: grounded vs. ungrounded** — kya aapki machinery, chahe shape kuch bhi ho, ab
bhi us reality ko touch karti hai jo ye improve karne ka dawa karti hai?

---
[⬅ Working From the Graph](03-working-from-graph.md) · [Agla: Complete Graph Example ➡](05-complete-graph-example.md)
