# 04 — The Two Modes of General Agent Use

Thesis ab tak general agents — Claude Code, OpenCode, Claude Cowork, OpenWork — ko Agent Factory ke
**manufacturing tools** ki tarah treat kar rahi thi: instruments jo insan AI Workers design/build karne
ke liye use karte hain. Yeh ek zaroori mode hai — lekin akela mode nahi.

General agents **do bilkul alag tareeqon** se use ho sakte hain.

**Pehla mode:** insan general agent use kar ke ek **immediate problem solve** karta hai. Agent reason,
likhne, code, analyze, plan, ya session ke andar ek outcome produce karne mein madad karta hai. Jab
problem solve ho jaye, session khatam. Zaroori nahi ke kuch permanent manufacture hua ho.

**Doosra mode:** insan general agent use kar ke aisi cheez banata hai jo session se **zinda bach jaye**:
ek agent harness, workflow, tool-using system, ya custom AI Worker. General agent khud final worker
nahi — yeh manufacturing instrument hai jo worker design, assemble, test, aur deploy karta hai. Deploy
hone ke baad, custom agent apni khud ki harness/runtime mein chalta rehta hai.

**_Mode 1_ session ke andar problem solve karne ke liye general agent use karta hai. _Mode 2_ ek custom
AI Worker manufacture karne mein madad ke liye general agent use karta hai jo session khatam hone ke
baad bhi chalta rahe.**

Zyada tar professionals Mode 1 mein lambe arse rahenge is se pehle ke woh koi Worker ship karein. Woh
persistent AI labor ke manufacturing tools ki tarah general agents use karne se pehle, direct
problem-solving ke liye use karenge.

| Mode | Audience aur Tools | Aakhir mein Kya Ship Hota Hai | Kis Se Governed |
| --- | --- | --- | --- |
| **Problem-solving engagement** | Engineer — Claude Code/OpenCode; Domain expert — Claude Cowork/OpenWork | Ek immediate outcome | Seven Principles |
| **Manufacturing engagement** | Koi bhi, hamesha Claude Code/OpenCode | Workforce ka ek hissa | Seven Invariants |

**Mode 1 — Problem-solving engagement.** Ek developer Claude Code kholta hai aur ek service refactor
karta hai. Ek finance analyst Claude Cowork kholta hai aur quarterly close model rebuild karta hai.
Engagement shuru hota hai, kaam ship hota hai, engagement khatam. Koi specialized AI Worker manufacture
nahi hota — general agent khud is engagement ka worker hai. Outcome seedha insan ko deliver hota hai.

Problem-solving engagements audience ke hisaab se split hote hain. Engineers Claude Code/OpenCode use
karte hain — terminal-native tools, code/infra/systems work ke liye tune. Domain experts Claude
Cowork/OpenWork use karte hain — knowledge-work tools, documents/spreadsheets/briefs/reviews ke liye
tune. Same engagement mode, same governance, do interface families. Yeh mode **Seven Principles of
General Agent Problem Solving** se governed hai:

1. **Bash is the Key.** Agent act kar sakta hai, sirf describe nahi.
2. **Code as Universal Interface.** Precision structured formats se — schemas, tables, code blocks —
   prose se nahi.
3. **Verification as Core Step.** Har meaningful output ship hone se pehle check hota hai. "Looks
   right" hi failure mode hai.
4. **Small, Reversible Decomposition.** Kaam atomic steps mein move karta hai; har step undo ho sakta
   hai.
5. **Persisting State in Files.** Conversation volatile hai; filesystem durable hai. Jo matter karta
   hai woh file mein rehta hai.
6. **Constraints and Safety.** Explicit permissions, explicit scope. Autonomy per-task-type earn hoti
   hai, default se grant nahi hoti.
7. **Observability.** Aap dekh sakte ho agent ne kya kiya. Koi black boxes nahi, koi surprises nahi.

*(In Seven Principles ki poori depth [Harness Engineering](../harness-engineering/README.md) chapter mein hai.)*

**Mode 2 — Manufacturing engagement.** Manufacturing hamesha engineering tools se anchor hoti hai:
Claude Code ya OpenCode, har baar, chahe insan koi bhi ho. Ek AI Worker banana fundamentally ek coding
task hai — chahe Worker ki working domain finance, marketing, ya law ho. Wahi developer Claude Code use
kar ke ek code-reviewing AI Worker spec/build/deploy karta hai. Finance analyst — aksar ek engineer ke
sath partnered — Claude Code use kar ke ek close-process Worker spec/deploy karta hai jo har month-end
chalta hai. General agent ka output outcome nahi — woh worker hai jo outcome produce karta hai. Yeh
mode **Seven Invariants of the Agent Factory** se governed hai (agla file) — structural rules jo
manufactured workforce ko coherent, governable, aur durable rehne ke liye maanni parti hain.

**Principles session govern karte hain. Invariants architecture govern karte hain. Principles conduct
hain. Invariants constitution hain.** Ek problem-solving engagement principle-governed hai kyunke uska
output ek outcome hai jo ship ho kar khatam ho jata hai — comply karne ke liye koi continuing
architecture nahi. Ek manufacturing engagement invariant-governed hai kyunke uska output ek workforce
mein apni jagah leta hai jo sessions, agents, aur product cycles ke across khadi rehti hai.

Isi liye 10-80-10 rule dono modes par equally apply hota hai: chahe aap general agent ko apna problem
solve karne ke liye direct kar rahe ho ya aisa Worker banane ke liye jo aapka problem solve kare, insan
ka waqt phir bhi intent, execution, aur verification mein split hota hai.

**Yeh do modes is book ke graduate karne wale insan ka naam bhi batate hain.** Yeh book us insan ko
train karti hai jise market ab **Forward Deployed Engineer** kehta hai — vendor-neutral, poori pipeline
carry karne wala — jo Digital FTEs manufacture karta hai aur unhein AI-Native Companies mein assemble
karta hai. Insan, unit, enterprise: aap kya bante ho, aap kya banate ho, banayi hui cheezein mil kar kya
banti hain. FDE Mode 2 ka embodiment hai — ek engineer poora manufacturing engagement chalata hai, spec
se production tak, us organization ke andar jise woh workforce chahiye. Aur market ka title address hai,
insan nahi: client ki company ke andar deployed, market is engineer ko FDE kehta hai; seedha hire kiya
gaya, wahi engineer AI-Native Company Architect hai. Book insan train karti hai. Market naam supply
karta hai.

*(Is role ka poora naqsha — demand, jo vendor lock-in yeh escape karta hai, aur iske sath har role — dekho*
[The Roles This Book Trains](../roles-this-book-trains/README.md)*.)*

---
[⬅ 03 — Personal Agents aur Two-Layer Model](03-personal-agents-and-two-layer-model.md) · [Agla: 05 — Seven Invariants Part 1 ➡](05-seven-invariants-part1.md)
