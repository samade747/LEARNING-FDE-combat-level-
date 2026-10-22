# 02 — Part 2: Markdown, the Writing Language (Concepts 3-7)

Markdown ki dusun features hain, lekin tumhe sirf **5** chahiye. Yeh almost har specification, request,
aur context file cover kar lete hain, aur is part ka aakhri concept (7) unko ek complete spec mein
assemble kar deta hai.

## Concept 3: Headings — AI ko batao kya sab se zyada matter karta hai

`#` ek heading banata hai. Zyada `#` symbols = deeper level:

```text
# Document title          (one per document)
## Major section
### Subsection
```

Yehi poori syntax hai. Jo matter karta hai wo yeh hai ke headings AI ke liye **kya karti hain**: yeh
dikhati hain kaunsi information sab se zyada important hai, aur kaunsi detail kis section ke neeche
aati hai. `## Hard constraints` ke neeche jo bhi hai usay **follow karna zaroori hai**. `## Nice to
have` ke neeche jo bhi hai wo **optional** hai. Headings ke bina, AI guess karta hai. Lekin heading
koi lock nahi hoti — agent phir bhi ek constraint miss kar sakta hai jo heading ke neeche ho, isliye
har result ko apne hard constraints ke against check karo.

**3 rules jo 90% heading mistakes rokte hain:**

| Rule | AI ke liye kyun matter karta hai |
| --- | --- |
| Har document mein ek hi `#` title | Do titles do alag documents ki tarah parhe jate hain — agent unko separate tasks samajh sakta hai. |
| Levels skip mat karo (`#` → `###`) | Skipped level tree todti hai — agent subsection ko ghalat parent se attach kar sakta hai. |
| Headings ko **claims** banao, labels nahi | `## Budget` kam bolta hai `## Budget: PKR 50,000 hard ceiling` se. Heading khud limit carry karti hai. |

**Example:** ek school administrator ne messy notes (20 guests, teen vegetarian, budget 25k, kids
table, etc.) ko Markdown document mein Goal/Hard constraints/Already handled/Open questions headings
ke neeche restructure karwaya — agent ne har fact sahi heading ke neeche rakha, aur jahan do headings
fit hoti thi wahan judgment call explain kiya.

## Concept 4: Lists — bullets sets ke liye, numbers sequences ke liye

```text
Features the page must have:        Steps to publish:
- Course list with fees             1. Review the draft
- WhatsApp contact button           2. Fix the timings table
- Holiday banner                    3. Publish
- Urdu/English toggle               4. Send the link to parents
```

**Dash (`-`)** = bullet = ek **set** — order matter nahi karta, har item independently true hai.
**Number (`1.`)** = step = ek **sequence** — order hi point hai, step 3 assume karta hai step 2 ho
chuka hai.

Yeh cosmetic nahi hai: numbered list do, agent order ko instruction ka hissa samajhta hai (step 4
pehle kabhi start nahi karega). Bullets do, agent kisi bhi efficient order mein kaam karta hai.
Ghalat list type ghalat signal bhejta hai.

**Nesting** sub-items ko parent se jorti hai:

```markdown
- Contact section
  - Phone number (clickable on mobile)
  - WhatsApp link (tapping it opens a chat)
  - Map pin, not a full embedded map
```

**Checkable-bullet habit:** ek **checkable bullet** wo requirement hai jisay reviewer bina discussion
ke ✅ ya ❌ mark kar sake. "Page should be fast" checkable nahi. "Page loads in under 3 seconds on a
3G connection" checkable hai. Har bullet reread karo aur poocho: kya main ya agent isay objectively
verify kar sakte hain? Yeh wahi grade-out-of-10 discipline hai, ek bullet ke time par.

## Concept 5: Code Blocks — AI ko exactly dikhana tum kya matlab rakhte ho

Kabhi kabhi prompt mein text hota hai jo AI ko **dekhna** hai, **act nahi karna**. Ek error message.
Output format ka example. Kisi aur ka quote. Triple backticks (` ``` `) mein wrap karna ek **code
fence** banata hai — ek signal ke "yeh data hai, instruction nahi."

````markdown
```python
def greet(name):
    return f"Assalam-o-Alaikum, {name}!"
```
````

Opening fence ke baad language tag (`python`, `bash`, `text`, `html`) batata hai yeh block kaise
parhna hai. Single backticks inline mein wahi kaam karte hain.

Bina fence ke, AI har cheez ko follow-karne-wali instruction samajhta hai. Fence ke sath, wrapped text
analyze/copy hoti hai. **Fence ek strong signal hai, safety lock nahi** — kabhi aisa text paste mat
karo jo tum nahi chahte act ho, kisi bhi tool mein jo act kar sakta hai.

| Situation | Bina fence | Fence ke sath |
| --- | --- | --- |
| Error message dikhana diagnose ke liye | Agent error ke andar wale lafzon par "helpfully" act kar sakta hai | Agent error ko literal artifact ki tarah analyze karta hai |
| Example output dikhana jo match ho | Agent format paraphrase karta hai | Agent format exactly reproduce karta hai |
| Kisi aur ka text quote karna apne prompt mein | Agent unki voice ko apni instruction se confuse kar sakta hai | Quoted text aur tumhari ask ke beech clean boundary |

**Sabse useful trick:** AI ko correct output ka **example** dikhao — format ko teen paragraphs mein
describe karne ke bajaye, ek example row fence mein dikhao:

```text
The timings table must look exactly like this:

| Course        | Days     | Time          | Monthly fee |
| ------------- | -------- | ------------- | ----------- |
| Matric Math   | Mon-Wed  | 4:00-5:30 pm  | PKR 3,500   |

Same columns, same order, same fee format.
```

Ek concrete example ko misread karna, description se bohat zyada mushkil hai.

## Concept 6: Links aur Images — duniya ki taraf point karna

```markdown
[link text](https://example.com)
![description of the image](path/or/url.png)
```

**Links kyun matter karte hain:** prompt mein link do to AI us page ko visit kar ke parh sakta hai.
Apni school ki fee policy memory se summarize karne ke bajaye (aur ghalat karne ke bajaye), policy
page link karo aur likho "fees must match this."

**Images kyun matter karti hain:** brackets se pehle `!` lagana image ko document ke **andar** rakhta
hai, sirf link nahi. Brackets ke andar wale lafz image ka **alt text** hain — jo AI ya screen reader
dekhti hai jab picture nahi dekh sakti. Yeh batata hai AI ko kahan dhyan dena hai. Page-design mockup
ke liye acha alt text: `![Mockup: banner on top, course table in the middle, contact buttons pinned
to bottom]`.

## Concept 7: Tumhari pehli complete specification

Upar ki saari cheezein ek document mein assemble hoti hain — ek **specification**. Yeh shape tum
sainkron baar likhoge, abhi web pages ke liye, baad mein ek **Digital FTE** (ek AI agent jo poora role
carry kare, employee jaisa) ke liye bhi. Skeleton:

```markdown
# [What you are building] Specification

## Goal

One paragraph: what this is and who it serves.

## Context

Links and facts the agent needs. Attach files; link sources.

## Requirements

- Checkable bullet
- Checkable bullet
- Checkable bullet

## Hard constraints

- Things that must not be violated (budget, deadline, platform)

## Out of scope

- Things you are explicitly NOT asking for

## Expected output

A fenced example, a format description, or a mockup image.
```

Is skeleton ke 2 sections sabse zyada kaam karte hain. **Out of scope** agent ka sabse common failure
(enthusiastic over-delivery — woh login system jo kisi ne nahi manga) khatam karta hai. **Expected
output** doosra sabse common failure (format drift) khatam karta hai.

**Spec ko run karne se pehle validate karo.** Pehla draft agent ko handover mat karo aur umeed mat
rakho — agent ko kaho spec par **attack** kare:

> Here is my specification: [paste spec]
>
> Do not build anything yet. First, review the spec itself:
> 1. List every ambiguity: every place where two reasonable
>    readers would build two different things.
> 2. List every missing constraint you would need to guess.
> 3. Grade the spec out of 10 on clarity, completeness, and
>    checkability, with a one-sentence justification each.
> 4. Suggest the single change that would raise the grade most.

Yehi grade-and-iterate loop hai jo [AI Prompting 2026](../ai-prompting-2026/README.md) mein tha, ab
apni spec par aimed. 2-3 rounds mein spec 6 se 9 tak chali jati hai — yeh agentic work ki sab se
sasti quality improvement hai, kyunke har artifact jo spec se banta hai, uski clarity inherit karta
hai. Ek unclear bullet fix karna ek minute leta hai; jo agent ne us se banaya use fix karna ek
afternoon leta hai.

> **Spec hi deliverable hai.** AI-native work mein, specification kaam se pehle ka paperwork nahi —
> yeh **asal kaam hai**. Agent ka output tumhari spec ka product hai, to spec behtar karo aur har
> regeneration behtar hoti jayegi. Book isay **spec-driven development** kehti hai — pehle
> specification likhna, phir har cheez usi se regenerate karna.

---
[⬅ Part 1 — The Two Languages](01-two-languages.md) · [Agla: Part 3 — HTML, the Reading Language ➡](03-html-reading-language.md)
