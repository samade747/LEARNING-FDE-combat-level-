# 00 — Overview: Kya Badla, 2023 Se Ab Tak

## Ek Fact Jo Sab Kuch Underlie Karta Hai

Model **stateless** hai — iski apni koi memory nahi turns ke darmiyan, aur har baar sirf jo abhi
iski context window mein hai usi se jawab deta hai. Neeche jo bhi likha hai, sab isi ek fact ka
downstream hai. Isi liye ek insight poore page mein chalta hai: **almost har "advanced technique" yeh
page sikhata hai, do moves mein se ek hai — sahi context andar lana, ya ghalat context bahar rakhna.**
Model sirf woh dekhta hai jo iski context window mein hai is response ke liye. Aapka kaam hai control
karna ke usme kya jata hai.

> Note: examples ChatGPT, Claude, aur Gemini reference karte hain kyunke zyada tar readers mein se
> ek inka use karta hai. Skills kisi bhi modern chat AI par transfer hoti hain.

## Kya Badla Hai Jab Se Aapne Aakhri Baar Dekha Tha

Agar aapne ChatGPT 2022 ya 2023 mein use kiya aur usko "clever toy" samajh kar chhor diya, to jo tool
aapko yaad hai wo ab wahi tool nahi hai. Kuch changes jo chupke se hue:

- **Context windows roughly 1000x bare hain.** 2022 ka model kuch hazaar words rakhta tha. 2026 ka
  model sau hazaar, kabhi kabhi ek million rakhta hai. Yeh badalta hai ke aap prompt mein kya bhar
  sakte ho: poori kitab, kayi din ki speech, contracts ka poora folder.
- **Reasoning real ban gayi.** "Think step by step" kabhi magic phrase thi. Ab models ke paas explicit
  thinking modes hain jo seconds, kabhi minutes chalte hain, jawab dene se pehle kayi approaches
  explore karte hue. Ek saal pehle, sabse hard task jo AI reliably khatam kar sakti thi, wo utna tha
  jitna ek insaan ko kuch minute lagte. Aaj yeh utna hai jitna ek insaan ko ek ghanta ya zyada lagta.
- **Web search built-in tool ban gaya.** Model khud decide karta hai kab sawal ko fresh information
  chahiye, search chalata hai, kuch pages parhta hai, aur jo milta hai use answer mein use karta hai.
- **Code execution bhi built-in tool ban gaya.** Model chhota program likh sakta hai, chala sakta hai,
  result dekh sakta hai, aur us result ko answer mein use kar sakta hai.
- **Multimodal sidebar hona band ho gaya.** Aap photo, PDF, spreadsheet, voice memo, ya files ka
  folder prompt mein daal kar sawal poochh sakte ho.
- **Tools ne aapko yaad rakhna shuru kar diya.** Teeno tools ab aapki apni ek short profile likhte hain
  ke aap kaun ho aur kaise kaam karte ho, aur har nayi chat se pehle load karte hain.
- **Desktop apps aaye.** Cowork, OpenWork jaisi products aapki files dhoond sakti hain, emails draft
  kar sakti hain, spreadsheets update kar sakti hain — permission ke saath.
- **Command-line agents developers ke liye aaye.** Claude Code, OpenCode terminal mein rehte hain,
  poore codebase ke across padhte hain, kayi files ek saath edit karte hain, tests chalate hain.

Agar aapka mental model in tools ka 18 mahine bhi purana hai, to aap unko shayad 20% capability par
use kar rahe ho jo aaj mumkin hai. Yeh page yeh gap band karta hai.

---
[⬆ Index](README.md) · [Agla: Part 1 — How AI Knows Things ➡](01-how-ai-knows-things.md)
