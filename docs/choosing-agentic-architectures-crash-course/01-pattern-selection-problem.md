# 01 — Part 1: The Pattern-Selection Problem (Concepts 1-3)

## Concept 1 — Pattern Selection: Build Se Pehle Ka Design Work

Zyada tar courses sikhate hain har pattern kaise **banayen**. Yeh course alag sawal poochta hai:
**diya gaya task, kaunsa pattern banana chahiye?** Yeh build se pehle ata hai, aur usay aana chahiye,
lekin usually taught nahi hoti — ek awkward wajah se: har pattern ka implementation well-documented
hai; unke darmiyan choose karne ka decision logic nahi hai.

Pattern catalog mature hai. ReAct 2022 ka paper hai. Planning-then-execution classical AI ke STRIPS
se ati hai, 2023 mein LLMs ke liye rediscover hui. Reflection 2023 se formalized hai. Multi-agent
architectures har major framework sikhata hai. Kisi bhi pattern ka tutorial 5 minute mein mil jata hai.
**Jo asaani se nahi milta:** diya gaya specific task, specific constraints ke sath, kaunsa pattern fit
karta hai?

**Iska failure mode:** engineers jo pattern recently dekha ya talks mein sabse impressive laga usi
taraf default karte hain. Multi-agent demos khaas kar tempting hain kyunki woh "real AI" jaisi lagti
hain. Teams hafton orchestration banane mein lagati hain us problem ke liye jo single agent 2 well-
defined tools ke sath ek din mein solve kar sakta tha.

**Ulta failure mode bhi real hai, kam discuss hota hai.** Engineers "bas ek single agent ek bohat lambi
system prompt ke sath use karo" ki taraf jate hain jab task genuinely structural decomposition maangta
hai. Agent context ke neeche collapse ho jata hai jo ek mental model mein fit nahi hoti. Tool-calling
errors cascade karti hain. Reflection hi woh fix ban jati hai jo team ko pata hai, isliye har jagah add
kar dete hain, aur ab har response 30 seconds leti hai.

**Discipline jo yeh course sikhata hai: pattern selection architectural fit-matching hai, capability
matching nahi.** "Best pattern kya hai?" mat pucho (koi ek best nahi hai). Pucho: "yeh task asal mein
kya maangta hai, aur sabse chota pattern kaunsa hai jo yeh de sakta hai?"

**Yeh ab pehle se zyada matter kyun karta hai:** 2023 mein agentic systems experimental the, galat
pattern chunna ek weekend waste karta tha. 2026 mein agentic systems production mein real users serve
kar rahe hain; jo pattern aap chunte ho woh aapki deployment topology, eval discipline, aur operational
cost decide karta hai scale par. Ab galat choice mehnga compound hoti hai: galat assumption ke liye
banayi gayi infrastructure, galat failure modes ke liye likhi gayi evals, galat incidents respond
karne wale runbooks.

## Concept 2 — Har Pattern Task Ke Baare Mein Alag Cheez Assume Karta Hai

Pattern selection ko tractable banane wala deep idea: **har agentic pattern task kaisa dikhta hai iske
baare mein ek bet hai.** Jab bet reality se match kare, pattern value add karta hai. Jab bet galat ho,
pattern overhead ban jata hai — kabhi invisible overhead (sirf tokens ki cost), kabhi catastrophic
overhead (poora system tootna).

**5 patterns kya bet lagate hain:**

- **Sequential workflow** bet lagata hai steps pehle se pata hain aur har run mein identical hain —
  solution path fixed aur articulable hai runtime se pehle. Agar sahi ho, LLM ki zaroorat nahi agla
  step decide karne ke liye; LLM calls sirf un steps ke liye reserve hoti hain jo genuinely
  interpretation maangte hain. Cost predictable, latency bounded. Agar galat ho (steps input ke
  mutabiq vary karte hain), workflow galat path force karta hai ya noisily fail hota hai
- **Single agent + ReAct + tools** bet lagata hai path pehle se pata nahi aur agent khud figure karega
  — task itna open-ended hai ke agla step ab tak jo observe hua usse decide hona chahiye. Agar sahi
  ho, ReAct ka loop (reason → act → observe → repeat) hi handle kar sakta hai, kyunki koi predetermined
  plan step 3 tak galat ho jata. Agar galat ho (path stable tha aur likha ja sakta tha), ReAct latency,
  cost, aur agent ke loop/revisit karne ka risk add karta hai
- **Planning + ReAct execution** bet lagata hai major stages aur dependencies pehle se articulate ho
  sakte hain, lekin har stage adaptive reasoning maangta hai — kaam ki **shape** pata hai (research →
  analyze → synthesize → report) jabke har stage ka **content** investigation maangta hai. Agar sahi
  ho, plan scaffolding deta hai aur agent ko bhatakne se rokta hai. Agar galat ho, plan overhead ban
  jata hai jisse execution vaise bhi diverge ho jati hai
- **Reflection** bet lagata hai output quality speed se zyada matter karti hai aur quality checkable
  hai — ek critique pass woh defects pakar sakta hai jo generator ne miss kiye, aur "good output" ke
  criteria explicit hain. Agar sahi ho, reflection reliability improve karta hai (galat SQL, weak legal
  arguments, factual mistakes pakarta hai). Agar galat ho (criteria vague hain, ya critic aur generator
  same blind spots share karte hain), reflection latency/cost add karta hai bina quality improve kiye
- **Multi-agent specialist system** bet lagata hai koi single agent iski expertise, context, ya
  capacity nahi rakhta — task genuinely specialist roles mein partition hota hai (researcher + writer
  + reviewer), aur specialists ke across coordination ek agent mein overload se sasta hai. Agar sahi
  ho, specialists apne domains mein generalist se behtar output dete hain. Agar galat ho ("specialists"
  mostly same kaam kar rahe hain, ya coordination overhead kaam par haavi hai), aap ne complexity add
  ki jo kuch nahi kamati aur naye failure modes (routing errors, integration errors, ownership
  ambiguity) introduce karti hai

**Pattern bet hai; task ki asal properties decide karti hain bet sahi hai ya nahi.** Yehi wajah hai
pattern selection fit-matching hai. Aap "kaunsa pattern sabse powerful hai?" nahi puch rahe. Aap puch
rahe ho "kaunse pattern ka bet mere paas jo task ke baare mein pata hai usse sabse achi tarah match
karta hai?"

## Concept 3 — 2 Failure Modes: Overshooting Aur Undershooting

Concept 2 ne naam diya ke har pattern ek bet hai. Concept 3 naam deta hai 2 tareeqon ka jisse woh bet
galat jati hai — real production systems mein roughly equal frequency ke sath hote hain.

**Overshooting** — task ki zaroorat se zyada elaborate pattern chunna. Yeh zyada famous failure mode
hai, talks/demos se giri jane wali. Examples:
- 3-agent system (researcher, writer, reviewer) ek single LinkedIn-post generation ke liye. "Researcher"
  ka output 2 paragraphs hain jo "writer" ko summarize karne parte hain. Reviewer 5% outputs reject
  karta hai un issues ke liye jo ek self-checking prompt pakar leta. **3 agents, 3x cost, koi
  measurable quality improvement nahi**
- Fixed workflow ko planning add karna — planner har baar wahi plan produce karta hai (kyunki task
  same hai), isliye har run ek extra LLM call ke liye pay karta hai kuch bhi na paate hue
- Bina checkable criteria wale task ko reflection add karna — critic aur generator same model, same
  training data, aur usually same blind spots share karte hain

**Overshooting trap:** aap ne aisi capability pay ki jo task ko chahiye nahi thi, aur usay undo karna
asaan nahi kyunki orchestration ab load-bearing hai. 6 mahine se production mein chalta multi-agent
system hatana refactor nahi, rewrite hai.

**Undershooting** — task ki asal zaroorat se simpler pattern chunna. Yeh failure mode talks kam
dikhate hain kyunki dramatize karna kam impressive hai, lekin utni hi common hai. Examples:
- Single agent, 4,000-token system prompt, billing/technical/account/refund sab handle kar raha —
  agent billing rules ko technical rules se confuse karta hai. **Task genuinely specialist routing
  maangta tha; ek agent context hold nahi kar saka**
- Fixed pipeline hona chahiye tha wahan ReAct + tools use karna — agent kabhi steps skip karta hai,
  kabhi completed work revisit karta hai, kabhi non-existent tool calls invent karta hai
- Genuinely verification maangne wale outputs par reflection skip karna — subtle errors wali SQL
  queries production mein ship hoti hain, citation mistakes wale legal drafts clients ko bhej diye
  jate hain

**Undershooting trap:** aap ne kuch brittle ship kiya jo manual oversight se ya luck se survive karta
hai. Production gaps reveal karta hai; remediation mein woh pattern add karna parta hai jo shuru mein
hona chahiye tha.

**Dono failure modes equally important kyun hain:** pattern selection ki discussions overshooting par
focus karti hain kyunki woh zyada visible failure hai. Lekin undershooting utni hi common hai, aur
arguably zyada dangerous — aisi systems produce karta hai jo **lagta hai** kaam kar rahi hain jab tak
nahi karti, subtle failure modes ke sath. Jo team overshooting avoid karna seekh le lekin undershooting
kabhi pehchane nahi, usne discipline ka aadha hi seekha hai.

Part 2 ki decision tree dono failure modes surface karne ke liye design hui hai — har sawal ek **task
property** poochta hai. Jawab elaborate pattern justify na kare to simpler pattern par route karta hai
(overshoot rokna). Jawab justify kare to explicitly wahan route karta hai (upgrade ko conscious banake
undershoot rokna).

---
[⬅ Overview](00-overview.md) · [⬆ Index](README.md)

*(Baqi parts — Decision Tree, 5 Patterns, Failure Signals, Decision Lab, Honest Frontiers, Closing —
likhe ja rahe hain.)*
