# 07 — One-Page Map Template + 5 Try-This-Now Prompts

## One-Page Map — Copy Karo

Niche ka block document mein copy karo, apni real workflow ke liye fill karo. Yeh hai jo colleague,
outside reviewer, ya workflow lene wale ko do.

```text
DELEGATION MAP: [workflow name]
Owner: [one named person]        Last reviewed: [date]      Next review: [date]

ELIGIBILITY  (both must pass before any step below is mapped)
Data gate: [may this data enter this tool? who confirmed, and when?]
Input gate: [can everything each step needs actually be supplied?]

STEPS
#  Step                    Owner          Criterion (reversibility /     Carried by
                                          stakes / accountability only)
1  ...                     AI             reversible, low stakes         Skill
2  ...                     AI             reversible, checked at step 4  code execution
3  ...                     Collaborative  high stakes, human judges      Skill + gate
4  ...                     Human          this step is the decision      named reviewer
5  ...                     Human          irreversible                   named signer

GATES  (one line per collaborative or human step)
Step 3: reviewed by [name], at [when], checking [what specifically]
Step 4: approved by [name], before [what happens next]

BASELINE  (measured before any change)
Time per run: ___    Revision rounds: ___    Manual steps: ___
Metric this workflow optimises for: [time | consistency | accuracy | variance]

IF IT GOES WRONG
Stopped by: [who, and can they act without permission?]
Scope check: [how do we find out how many outputs were affected?]
Told: [who, within what time]
Map change: [recorded here, with a date]
```

**3 lines sabse zyada kaam karti, aur sabse zyada missing rehti:** owner, next review date, aur
har gate kya check kar raha. Bina inke map decision describe karti. Inke sath map ek **operation**
describe karti.

## Try This Now — 5 Prompts

### 1. Extract aur Phir Attack

Real document lo jis par act karna hai (brief, policy, email thread):

```text
From the attached document, extract every distinct requirement or
action it asks for. For each one: a short label, the exact section
it comes from, and whether it is stated directly or only implied.
Return it as a table.
```

Phir same conversation mein:

```text
Now review your own list. Which of these are ambiguous as written?
Which could two people on my team read differently? What did you
extract as one requirement that is really two?
```

_Notice:_ 2nd pass usually list change karti. Nahi karti to pucho document unusually clear thi ya
pass shallow tha.

### 2. Wo Step Dhoondo Jo Undo Nahi Ho Sakta

```text
Here is a workflow: [your steps].

For each step, answer three questions and nothing else. Can it be
undone? What does an error cost in the bad case, not the average
case? Is this step the decision somebody answers for, or an input
that somebody else judges afterwards? Do not recommend anything yet.
```

_Notice:_ recommendation hold-back karna hi point hai. Analysis+recommendation saath maango to
recommendation milegi jiske liye analysis likhi gayi hai.

### 3. Timing Se Diagnose Karo

Jab next baar output disappoint kare, kuch change karne se pehle:

```text
Before we fix this, help me diagnose it. I will describe what
happened and when. Ask me one question at a time to work out
whether this is under-specification, context overload, a wrong
feature or model, stale configuration, or a task that does not fit.
Do not suggest a fix until you have a diagnosis.
```

_Notice:_ kitni baar under-specification par land karta, aur kitni baar tumhara instinct model
change karne ka tha.

### 4. Ek Fix Promote Karo

Ek correction dhoondo jo 2 baar se zyada ki hai:

```text
I keep making this correction: [the correction].

Is this a rule, a reference, or a procedure? Then write it in the
form its home needs: a standing instruction, a knowledge-base entry,
or the steps of a Skill.
```

_Notice:_ procedures sabse zyada misfiled hoti. Answer mein order hai to procedure hai, 1-line
instruction order kho degi.

### 5. 3 Tareeqon Se Bolo

```text
Here is an AI-assisted workflow my team runs: [describe it, including
the human review step].

Write three descriptions of it: one for a technical colleague, one
for an executive, one for a risk or compliance function. Each must
name the human checkpoint. Do not use the phrases "fully automated",
"handles", or "as good as a person".
```

_Notice:_ kya executive version mein gate abhi bhi hai. Yehi version hai jahan sabse zyada gayab
hoti.
