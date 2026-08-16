# 01 — Part 1: The Discipline (Concepts 1-3)

Courses 3-8 ka thesis tha ke ek AI-native company end-to-end buildable hai. **Course 9 add karta hai
ke buildable trustworthy nahi hai.** Jisne bhi ek Worker production mein bheja hai aur usay confusing
tarike se fail hote dekha hai, yeh janta hai. Worker apne unit tests pass karta hai. Integration tests
green hain. Demo achi gayi. Phir bhi production mein kabhi galat tool chunta hai, training mein
acknowledge kiya hua constraint ignore karta hai, ya jawab confabulate karta hai jab usay escalate
karna chahiye tha. Kyun? Un tests mein se koi bhi woh cheez measure nahi karti jo asal mein fail ho
rahi hai: **agent ka behavior**, un conditions ke tehat jo tests ne anticipate nahi kiye.

## Concept 1 — Traditional Tests Agents Ke Liye Kyun Kaafi Nahi

Function ke liye unit test poochta hai: *diye gaye input par, kya function yeh output deta hai?*
Failure unambiguous hai: assertion pass ya fail hoti hai. Ab dekho jab "function" ek AI agent ban
jaye to kya badalta hai. Input concrete value nahi, natural-language task hai, ambiguous. Output
return value nahi, model calls, tool invocations, intermediate decisions, handoffs, retries, aur
eventual response ki sequence hai. **Koi bhi assumption jispar unit test khara hai, agent ke liye
nahi hoti.**

Agent 5 tareeqon se mushkil hai:

1. **Probabilistic** — same model, same prompt, alag runs par alag outputs. Ek run test pass kar sakta
   hai bina agli baar ka guarantee die.
2. **Multi-step** — plan karta hai, tools call karta hai, results dekhta hai, phir plan karta hai. Sirf
   final response check karne wala test ek run pass kar sakta hai jahan har intermediate step galat
   tha lekin agent luckily sahi answer par pahunch gaya.
3. **Tool-using** — sahi tool, sahi arguments, sahi order? Har sawal apna evaluation problem hai.
4. **Context-sensitive** — konse documents retrieve hue, konse prior messages, konse Skills installed,
   kaunsa model — sab behavior badalte hain.
5. **External systems se connected** — side effects hote hain. Traditional unit test external world
   mock karta hai; agent eval ko staging-equivalent infra chahiye ya careful mocks.

Traditional tests obsolete nahi hain — Course 9 ka lab (Decision 1) unhe pehle confirm karta hai:
tools par unit tests, durability layer par integration tests, Paperclip surface par API tests. Yeh
zaroori hain. Naya woh layer hai jo **inke upar** baithta hai aur agent ko khud measure karta hai —
**behavior evaluation**, ya evals.

**Concrete example:** Maya ka Tier-1 Support agent billing error ticket receive karta hai. Sab
traditional tests pass hote hain — Inngest wrapper theek chalta hai, tools integration-tested hain,
response-generation function string return karta hai. Lekin production mein, agent **galat customer**
lookup karta hai (similar email, alag account), uski purchase history confirm karta hai, aur $89 refund
**galat insaan ko** issue kar deta hai. Koi traditional test yeh nahi pakarta, kyunki har component
sahi kaam kar raha tha. Failure agent ki reasoning mein hai ke kaunsa customer lookup karna hai. Sirf
ek behavior eval ("sahi argument customer-lookup tool ko diya gaya tha?") isay pakarti hai.

> **PRIMM sawal:** Maya ka Tier-1 Support agent 200 tickets/din handle karta hai. Har tool par unit
> tests hain, approval primitive par integration tests hain, ek nightly synthetic end-to-end test bhi
> hai — sab green. 6 hafte se production mein hai. Predict karo: production failures ka kitna fraction
> yeh test suite pakregi? Jawab Concept 3 ke aakhir mein.

## Concept 2 — TDD Analogy Aur Uski Limits

**TDD woh discipline thi jisne SaaS engineering ko reliable banaya.** Pehle code ship hota tha jab
development mein chal jaye; TDD ke baad, code ship hota hai jab apni tests pass kare. EDD wahi shape
hai: pehle agents demo achi hone par ship hote the; EDD ke baad, agents ship hote hain jab unki eval
suite pass ho.

**TDD se jo carry hota hai:**
- **Loop shape** — red-green-refactor, EDD mein "failing eval, passing eval, refactor prompt/tool/
  workflow" ban jata hai
- **Regression net** — dono change ko safe banate hain
- **CI/CD integration** — har commit/change par suite chalti hai
- **Dataset as artifact** — golden dataset bhi version-controlled, reviewed hota hai, codebase ka hissa
- **Team discipline** — TDD ko mainstream hone mein 10 saal lage; EDD abhi usi adoption curve par hai

**Jahan TDD ke assumptions tootte hain:**
- **Determinism** — TDD test deterministic hai; agent eval probabilistic hai, **distribution** grade
  karta hai (`pass_rate >= threshold across N runs`), single point nahi
- **Drift** — model retrain/upgrade hone se agent behavior Tuesday ko Monday se alag ho sakta hai. TDD
  ka koi analog nahi. Regression evals aur production evals iske responses hain
- **Context-dependent correctness** — agent ki "sahi behavior" poore context window par depend karti
  hai; golden dataset ko care se banana parta hai
- **Cost** — TDD test milliseconds ki cost, agent eval model-call API fees + tool time — EDD ka apna
  economic dimension hai
- **Grader subjectivity** — TDD assertion unambiguous hai; eval ka grader (LLM-as-judge ya human)
  natural-language response judge karta hai — khud apna failure mode rakhta hai
- **"Passing" target move karta hai** — threshold set karna ek judgment call hai jo TDD kabhi nahi
  maangta

## Concept 3 — "Behavior" Ka Matlab: Final Answer vs Trace vs Path

Naive jawab hai "agent ka response." Agar agent ne customer ke sawal ka sahi jawab diya, to agent ne
sahi behave kiya. Yeh likhna sabse asaan hai, aur **profoundly insufficient hai.**

Maya ke Tier-1 Support agent ka example dubara: customer billing dispute puchta hai. Agent jawab deta
hai: *"$89 refund process kar diya... 3-5 business days mein statement par dikhega."* Output eval isay
pass kar dega. Ab dekho agent ne asal mein kya kiya:

1. Customer ka message parha, refund request pehchani.
2. Customer-lookup tool call kiya, **email** ko lookup key ki tarah use kiya.
3. Lookup ne 3 matches wapis diye (ek personal account, ek small-business account, teesra flagged
   duplicate).
4. Agent ne bina check kiye **pehla result** chun liya.
5. Us account par recent charges dekhe, ek $89 charge mila jo coincidentally refundable lagta tha.
6. Refund issue kar diya.
7. Response likha.

**Output sahi hai. Behavior galat hai.** Agent ne **galat customer** ko refund diya jo dispute amount
se match hota tha. Real customer ko kabhi refund nahi mila; galat insaan ko free $89 mil gaya. 3 mahine
baad auditor pakarta hai, tab tak aisi dozens mismatches ho chuki hoti hain.

**Concept 3 ka core insight:** agent ka "behavior" uska **poora execution path** hai, sirf final
response nahi. Sirf final response evaluate karna aisa hai jaise exam ka last paragraph parh kar grade
dena — jo students explicitly galat conclude karte hain unhe pakarte ho, jo galat reason karke accident
se sahi conclusion par pahunch jate hain unhe miss karte ho.

**3 levels, har ek apni eval layer maangta hai:**

- **Level 1 — Final output.** Jo agent ne aakhir mein kaha ya kiya. Output evals (Concept 5) isay
  grade karte hain. Factual errors, format violations, hallucinations pakarte hain — lekin miss karte
  hain jab output sahi lage phir bhi process broken ho.
- **Level 2 — Tool-use record.** Kaunse tools, kis arguments ke sath, kis order mein. Tool-use evals
  (Concept 6) isay grade karte hain. Galat tool selection, galat arguments, missed tool calls pakarte
  hain — lekin miss karte hain reasoning failures jo tool calls ke **darmiyan** hoti hain.
- **Level 3 — Full trace.** Poora execution path: model calls, tool calls, handoffs, guardrail checks,
  intermediate reasoning, retries. Trace evals (Concepts 6, 8) isay grade karte hain. Reasoning
  failures pakarte hain jo sahi tool calls produce karti hain, galat specialist ko handoffs, guardrail
  bypasses. Limit: structured traces aur LLM-as-judge graders chahiye, jinke apne evaluation problems
  hain.

**Yeh 3 levels alternatives nahi, ek stack hain.** Output evals sasti aur asaan hain, isliye frequently
chalti hain. Trace evals mehngi hain lekin woh failures pakarti hain jo output evals nahi dekh sakti,
isliye har meaningful change par chalti hain. Ek serious EDD discipline teenon use karti hai.

Courses 3-8 ki architecture ki har layer ek level par fail hoti hai: Tier-1 Support agent ki wrong-
customer failure Level 2 hai. Claudia ka Maya jaisa refund approve na karna Level 3 hai (uski reasoning
ne ek signed action banaya jo envelope check pass karta hai lekin Maya ki asal judgment se contradict
karta hai). Manager-Agent ka galat hire recommend karna bhi Level 3 hai.

> **Concept 1 PRIMM ka jawab:** Honest jawab (3) ya (4) ke qareeb hai — aisi test suite production
> failures ka roughly 10-30% pakregi, kabhi kam. Unit tests tool bugs aur integration bugs pakarte
> hain. Agent-reasoning failures (galat customer disambiguation, galat tool selection, hallucinated
> facts, broken handoff logic) — jo **majority** production failures banate hain — nahi pakarte. **Yehi
> wajah hai output evals + tool-use evals + trace evals traditional test stack ke ilawa zaroori hain**,
> uski jagah nahi.

---
[⬅ Overview](00-overview-and-tracks.md) · [⬆ Index](README.md)
