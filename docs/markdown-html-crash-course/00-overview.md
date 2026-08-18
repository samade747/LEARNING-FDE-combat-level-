# 00 — Overview: Prove It in Two Minutes

## Poori Cheez Ek Tasveer Mein

Aap agent ko Markdown mein likhte ho (yeh spec hai). Agent aapko HTML mein jawab deta hai (yeh report
hai jo aap parhte ho). Agent agle agent ko context Markdown mein pass karta hai.

Isi ke peeche ek hi sawal baitha hai, aur yehi is course ke har format decision ko decide karta hai:
**yeh cheez aakhir mein kaun parhega?**

- Koi insaan browser mein parhega → **HTML**.
- Koi AI parhega (future chat sameet) → **Markdown**.
- Honestly pata nahi → **Markdown**. Insaan Markdown kaafi acha parh leta hai; AI HTML ghalat parhta
  hai. Aur aap kisi bhi waqt Markdown ko HTML mein render kar sakte ho jab insaan ko chahiye ho.

## Prove It in Two Minutes

Kisi theory se pehle, poora course ek baar chala kar dekho. [Claude.ai](https://claude.ai) (ya ChatGPT,
Gemini) kholo aur yeh paste karo:

> Make me a small web page as an HTML artifact: a welcome card for a
> neighborhood tuition center. A colorful holiday-notice banner on top,
> three example courses with monthly fees in a neat table, and a
> WhatsApp contact button. Keep it readable on a phone.

Claude ek pal sochta hai, phir chat ke saath ek panel kholta hai aur usme ek real, styled page banata
hai: banner, table, button. Yeh panel ek **artifact** hai: ek live document jo AI conversation ke saath
banata hai, uske andar nahi. (ChatGPT aur Gemini isko **Canvas** kehte hain — same idea.) Agar aapko
rendered page ke bajaye code ki wall mili, bolo `show it to me as a rendered artifact` aur yeh flip ho
jayega. Ab artifact panel par share/publish control dhoondo, tap karo, aur resulting link apne phone
par kholo.

Do minute, aur aap already is poore course ki har cheez ek baar, accidentally kar chuke ho: kuch
structured lines gayin, ek designed page aayi, aur ek link ne usko shareable bana diya. Neeche ke 14
concepts har step ko deliberate banate hain, taake yeh tab bhi kaam karte rahein jab stakes demo se
zyada high hon.

**Course ka naqsha:**

- **Part 1** split ko frame karta hai.
- **Part 2** vo Markdown sikhata hai jo aap haath se likhte ho.
- **Part 3** sikhata hai HTML demand karna, judge karna, aur publish karna — jo aap kabhi khud nahi
  likhte.
- **Part 4** ek exercise ko teen tareeqon se chalata hai jinse aap is book mein agents se milenge.

Iske baad aap ek clean Markdown spec likh sakenge, usko readable HTML artifact mein badal sakenge jo
koi doosra link se khol sake, aur kisi bhi output ke liye decide kar sakenge ke wo Markdown, HTML, ya
feed ke liye plain text hona chahiye.

---
[⬆ Index](README.md) · [Agla: Part 1 — The Two Languages ➡](01-two-languages.md)
