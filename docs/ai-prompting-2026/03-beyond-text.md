# 03 — Part 3: Beyond Text (Concepts 8-10)

AI sirf ek text box nahi hai. Yeh images dekh sakta hai, audio dono directions mein kaam kar sakta hai,
chhoti working apps bana sakta hai, aur aapke data par code chala sakta hai. Zyada tar log inme se kuch
try hi nahi karte.

## Concept 8 — Multimodal: Images, Audio, Aur Aage Kya

**Image input.** AI images ko coarsely dekhta hai. Strong hai: overall scene aur composition, distinct
bare object shapes, whiteboard contents (diagrams sameet), handwritten/cursive text (decent, high
stakes par double-check karo). Weak hai: fine details ("yeh kaunse gym machines hain?" fail hota hai
kyunke gym machines slightly blurry lens se milte-julte lagte hain, AI confidently ghalat jawab de
sakta hai), cluttered scene mein chhoti cheezein count karna, image ke edge par small print parhna.

Ek real-world test: ek teacher ne whiteboard photo li jahan uska sar neural network diagram mein
"convolutional" word block kar raha tha. AI ne baaqi diagram se sahi word infer kar liya. Yehi AI acha
karta hai: gist se infer karna. Zoom-in karna acha nahi karta.

**Image output.** Modern AI text prompts se images generate kar sakta hai. Do practical tips:

1. **Image prompt likhne ke liye text AI use karo.** "Mujhe ek fantasy forest illustration ke liye
   prompt generate karo, Studio Ghibli style mein." Text AI aapse pehli koshish mein zyada acha rich
   image prompt likhta hai.
2. **Visual vocabulary banao.** Cinematic, watercolor, cyberpunk, anime, isometric, low-poly, art-deco
   jaise words levers hain. Image models captioned images par trained hain aur yeh styles naam se
   seekhi hain.

Image generation ek **diffusion model** hai — random pixel grids se noise remove karne ke liye trained,
step by step, jab tak image emerge na ho. Text ki tarah pixel-by-pixel nahi — poori image ek saath
generate hoti hai. Isi liye aap image generation ko beech mein rok nahi sakte time bachane ke liye,
jaise text response interrupt kar sakte ho.

Failure modes jo abhi bhi watch karne laayak hain: garbled text on signs ("HAPRY BIRTDAY"), inconsistent
characters across frames, hand/finger errors (chhe fingers, fused hands), cluttered backgrounds with
implausible objects, wrong aspect ratio.

### Power-User Recipe — Designer-Quality Diagrams Bina Designer Ke

Agar aapko kabhi document, slide, ya chapter ke liye diagram chahiye, ek workflow hai jo designer-quality
output ~15 minute mein deta hai, bina Figma ke aur bina visual design skill ke:

1. **Claude ko concept ko SVG ki tarah visualize karne ko kaho.** "Isko diagram ki tarah visualize karo.
   SVG mein output karo. Text ka har label, arrow, aur relationship present ho." Claude iske liye achi
   choice hai kyunke iski reasoning ability major models mein sabse strong mein se hai.
2. **SVG ko PNG mein convert karo.** Claude se seedha render karwao, ya online converter use karo, ya
   browser mein high zoom par screenshot lo. 2x resolution par render karo.
3. **PNG ko ChatGPT (ya Gemini) mein paste karo, redraw karne ko kaho.** ChatGPT ka in-product image
   generation is step ke liye strong hota hai kyunke yeh text-heavy images mein unusually acha hai:
   labels preserve karta hai, typography sahi karta hai. Prompt: "Is diagram ko professional design
   quality ke saath redraw karo. Har label, box, arrow, exact structural relationships preserve karo.
   Typography, spacing, color palette, visual hierarchy improve karo. Information wahi rahe, sirf
   visual finish badle."
4. **Result par iterate karo.** Original SVG ke saath side by side compare karo, correction type karo.

**Jo pattern survive karta hai:** structure pehle sabse strong reasoning model mein, polish doosra
sabse strong text-heavy image model mein. Tools ka leader rotate hoga; yeh two-step chain move rahega.

**Audio in, audio out.** Wahi shift jo images ke saath hui, ab audio ke saath ho rahi hai. Long-form
dictation nuance capture karti hai jo typed prompts miss karte hain. Meeting transcripts ko context ki
tarah use karo: ek ghante ki meeting recording daal kar poochho "decisions, open questions, aur action
items owner ke hisaab se summarize karo." Yeh in-page sabse high-leverage workflows mein se ek hai
kisi bhi meetings wali job ke liye.

| Audio task | Kitna acha kaam karta hai | Kis se hoshiyar raho |
| --- | --- | --- |
| Clear speech transcription | Excellent | Heavy accents, technical jargon, overlapping speakers |
| Speaker identification | 2 speakers par decent, 4+ par weak | Kisi ko quote karne se pehle hamesha check karo |
| Tone, sarcasm, emotion | Improving lekin unreliable | AI se uncertainty flag karwao |
| Music/non-speech audio analysis | Limited | Specialized tool use karo |
| Real-time voice conversation | Casual ke liye acha, technical depth ke liye weak | Precision chahiye to text par switch karo |

## Concept 9 — Ek Prompt Se Chhoti Apps Banana

Modern AI ek single prompt se chhote games, websites, aur tools bana sakta hai. Bare software ke liye
nahi, lekin chhoti useful cheezon ke liye, yeh genuinely accessible hai un logon ke liye jinhone kabhi
code nahi likha.

App chat ke andar side panel mein render hoti hai — aur wo panel mein cheez sirf preview nahi, ek
**artifact** hai: conversation ka produce kiya hua ek persistent object, jise aap edit, iterate,
shareable link par publish, embed, ya code ki tarah download kar sakte ho. Claude mein isko
**Artifacts**, ChatGPT mein **Canvas**, Gemini mein **Canvas** kehte hain.

Recipe sirf teen slots hai:

```
Goal: what should this thing do?
Input: what does the user provide?
Output: what does the user see?
```

Examples jo aaj kaam karte hain: Pomodoro timer, bill splitter, outfit picker (weather se), fireworks
simulator, place-obstacles game.

Jo abhi bhi hard hai: **internet par multiplayer** (networking, accounts, matchmaking abhi bhi
single-prompt build se pare hain), **different language mein live AI feedback** (French-conversation
tutor jo real-time pronunciation correct kare — genuinely hard hai).

Intuition jo aap banate ho: chhoti cheezein jo ek screen par fit hoti hain, bina accounts, bina
external services ke — kaam karti hain. Iske pare kuch bhi ek se zyada prompt aur usually real
engineering maangta hai.

## Concept 10 — Data Analysis (Model Code Likhta Aur Chalata Hai)

Jab aap AI se koi sawal poochte ho jisko calculation ya graphing chahiye — "meri electricity bill iss
saal kaise badli" se le kar "pichle quarter kaunse products sabse zyada bike" tak — modern tools chupke
se kuch remarkable karte hain: model code likhta hai, chalata hai, aur result wapis deta hai. Code
execution bas ek aur tool hai jo model call kar sakta hai, web search ki tarah.

**Sabse pehle: confirm karo ke AI actually code chala raha hai, guess nahi kar raha.** Yeh is poore
section ka silent failure mode hai. AI har sawal par automatically code nahi chalata — yeh **choose**
karta hai, sawal ki phrasing dekh kar. Chhote sawalon par yeh kabhi code skip kar ke ek glance se
answer de deta hai — jo bahar se real analysis jaisa hi lagta hai. Teen habits isko rokte hain:

1. **Explicitly poochho.** "Isko answer karne ke liye code likho aur chalao. Jo code chalaya wo dikhao."
2. **Check karo ke code visibly wahan hai.** Agar response mein koi code block nahi jo chala ho, model
   ne shayad code nahi chalaya.
3. **Analysis se pehle ek verifiable specific demand karo.** "Analysis se pehle exact row count, column
   names, aur date range batao." Agar model file actually parh raha hai, yeh answers sahi honge.

**Bubble tea shop example.** Ek chhoti business ke paas ek saal ka sales data hai. Owner poochta hai:
"Kaunse drinks mein saal ke across sabse bare changes hue? Graph karo. Isko answer karne ke liye code
likho aur chalao aur dikhao." AI month-over-month changes per drink compute karta hai, notice karta hai
ke zyada tar drinks flat hain aur chaar stand out karte hain, un chaar ka colored line graph banata
hai. "Strawberry matcha rose sharply spring mein; agle saal wo promotion phir se chalane ke baare mein
sochein." Yeh generic answer nahi — asal data mein grounded answer hai.

Kya double-check karna hai, chahe code chala ho:

- **Final totals** — code precise hai, lekin AI ne shayad ghalat column sum kiya ho.
- **Graph labels** — numbers usually sahi hote hain; captions kabhi confidently ghalat hote hain.
- **Koi bhi cheez jo AI ne misinterpret ki column ki wajah se.**

AI data analysis ko treat karo jaise ek sharp junior analyst ke kaam ko: useful, fast, almost hamesha
sahi, kabhi kabhi instructive tareeqon se ghalat.

---
[⬅ Part 2 — Talking to AI Well](02-talking-to-ai-well.md) · [⬆ Index](README.md) · [Agla: Part 4 — Working Safely and Choosing Tools ➡](04-working-safely-and-choosing-tools.md)
