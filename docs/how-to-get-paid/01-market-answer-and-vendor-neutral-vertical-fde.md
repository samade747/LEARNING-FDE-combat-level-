# 01 — Market Ka Jawab: FDE, Do Gates, aur Humara Jawab

## Market Ka Jawab: Forward Deployed Engineer

Market ne pehle se hi us insaan ka naam rakh diya hai jo gap band karta hai, aur role ko uske hisaab se price kiya hai. Yeh Palantir mein invent hua tha aur ab poori industry mein phail raha hai. FDE ek normal software engineer ka **ulta** karta hai. Headquarters mein product banane ki jagah, FDE customer ki company ke **andar** jata hai, wahi baithta hai jo asli kaam karte hain, aur wahin solution banata hai, real data par, jab tak real value na lande.

Yeh job description in-hi do problems ke against parho. Yeh us developer ko absorb karta hai jise kaam nahi mil raha, kyunki yeh **kaam hai**. Aur yeh us pilot ko theek karta hai jisne return nahi diya, kyunki yeh **exactly** woh step hai jo woh pilot skip kar gaya. Ek role, dono taraf.

Demand numbers loud hain: FDE job postings **9 mahinon mein 800% se zyada** bar gayin, jabke candidate pool sirf ~50% bara. 2026 ki ek hafte mein, AWS aur Microsoft ne mil kar naye FDE units ke liye **3.5 billion dollars** commit kiye. OpenAI ne role ke around ek poori deployment company banai. Anthropic isi ke liye hire karta hai, aur baray consulting giants bhi.

Services industry ne bhi arithmetic chala liya hai. Sanjeev Aggarwal, India ki outsourcing industry ka ek pioneer, kehte hain ke roughly 100 FDEs ki ek firm, 100 million dollar ka business bana sakti hai — woh kaam jo purana model 2,000 se 2,500 logon se staff karta tha. Yeh unki projection hai, measurement nahi. Lekin dhyan do yeh kis ki projection hai: woh insaan jisne purana pyramid banaya tha, ab uske replacement ko describe kar raha hai.

**Ek boundary in numbers par, kyunki inhein galat parhna aasan hai.** Yeh enterprise buying describe karte hain. $3.5 billion ke peeche engagements Unilever aur Novo Nordisk jaisi companies ko jate hain, un vendors se staffed jinke paas sales teams aur balance sheets hain. Yeh aapka pehla buyer nahi. Aapka pehla buyer ek 20-se-200-person firm hai jahan **ek partner personally decide karta hai**, abhi koi AI budget line nahi hai, aur sabse gehra dar hai shehar ki pehli firm hone ka jo yeh try kare. Demand real hai, aur jo demand aap asal mein reach kar sakte ho, headline se patli, dheemi, aur choti hai. Isi buyer ke liye plan karo, aur headline sirf **context** ban jati hai, promise nahi.

## Market Ke Band Kiye Hue Do Gates

Yehi numbers dobara parho, Karachi, Lagos, ya Manila mein baithe developer ki tarah, aur do problems zahir hoti hain.

**Pehla problem lock-in hai, aur yeh client ko nuqsan pohanchata hai.** Palantir ka har FDE Palantir ke platform par banata hai. OpenAI ka har FDE OpenAI ke stack par banata hai. Engineer client ki company mein gehra jata hai, ek vendor ka product har jagah wire karta hai, aur chala jata hai. Client ab **locked-in** hai: azaad tab tak jab tak wahin build karte rahein. Andrew Ng ne note kiya hai ke clients aise FDEs dhundne mein struggle karte hain jo ek vendor se bandhe na hon, kyunki vendor ke liye lock-in hi role ka poora point hai.

**Doosra problem hiring door hai, aur yeh aapko nuqsan pohanchata hai.** Vendor FDE role vendor ke payroll par rehta hai. Aaj yeh zyada tar ek senior door hai: 5+ saal ka tajurba, aksar US ya European work address. Jo billions FDE units par kharch ho rahe hain, woh open global market se disrupted developers hire karne par kharch nahi ho rahe. To era ka sabse tezi se barhta hua services role, zyada tar duniya ke developers ke liye, ek aisa role hai jo woh parh sakte hain lekin enter nahi kar sakte.

Dono gates ki ek hi wajah hai: **vendor ka platform** hi woh cheez hai jo deploy ho rahi hai, aur vendor decide karta hai kaun isay deploy karega. Platform hata do, dono gates khul jate hain — lekin baaki kuch khud-ba-khud nahi khulta. Experience, trust, sales access, aur jurisdiction abhi bhi saamne khare hain, aur yeh page apni zyada tar length inhi par kharch karta hai. Lekin platform hatana ek harder sawal khada karta hai: **client ke darwaze se aap uski jagah kya sath le jate ho?**

## Humara Jawab: Vendor-Neutral Vertical FDE

Is book ke jawab mein do lafz hain, aur har lafz ek problem solve karta hai.

**Vendor-neutral** lock-in solve karta hai. Aap kisi platform se bandhe nahi. Jab agle quarter behtar model aata hai, aapka client switch karta hai. Jab agle saal sasta runtime aata hai, client switch karta hai. Client abhi azaadi khareedta hai, baad mein switching costs nahi deta. Aur aapko outright hire karke rakha ja sakta hai, bina ek step khoye, kyunki aapki discipline aapke andar rehti hai, kisi vendor ke product mein nahi.

**Vertical** empty-hands problem solve karta hai. Vendor ka engineer vendor ka platform sath le kar jata hai. Platform hata do, specialization ko kahin land karna zaroori hai. Warna aap ek generalist consultant ho jiske paas ek client se doosre tak reuse karne ko kuch nahi. Yeh **profession** par land karta hai. [Ownership argument](../what-you-carry-in/README.md) isay elimination se prove karti hai. Aap model, runtime, apne hours, ek vendor ka platform, ya is book ka method own nahi kar sakte, kyunki har ek rented, replaced, absorbed, ya shared hai. Wahid asset jo bachta hai, ek profession ka governed knowledge hai, ek jurisdiction mein, ek committed expert ke sath bana hua. To vendor-neutral FDE client ke darwaze do Systems of Record le kar jata hai: shared method, jo yeh book har graduate ko deti hai, aur profession, jo **aapki hai**.

Pehli wali koi figure of speech nahi. [Agent Factory System of Record](https://agentfactory.panaversity.org/docs/ecosystem/system-of-record) MCP par live hai, aur koi bhi MCP-speaking agent isse connect ho sakta hai aur guess karne ki jagah book se jawab de sakta hai. Yeh apna agent connect karo aage parhne se pehle, kyunki is page ka baaki hissa aasan ho jata hai jab method pehle se aapke sawal jawab de raha ho. Yeh wahi cheez bhi hai jo aap ek profession ke liye banane wale ho — pehle isay reader ki tarah use karo, phir builder ki tarah copy karo.

Commit karne se pehle ek trade naam le lo. Vendor ka FDE subsidized hota hai, kabhi client ke liye free, kyunki vendor isay lock-in mein wapis kama leta hai. Vendor-neutral FDE ko client ya aapki apni firm pay karti hai. Yehi feature hai, bug nahi: client optionality ke liye pay kar raha hai, aur aapko us cheez ke liye pay kiya ja raha hai jo koi rival copy nahi kar sakta.

## Technology Kahan Sikhai Jati Hai

Yeh page **monetization** sikhata hai. Yeh technology nahi sikhata, aur koshish bhi nahi karega, kyunki book ke paas iske liye pehle se ek canonical jagah hai: **Getting Started: Crash Courses**. Woh page poora curriculum rakhta hai, order mein, mode decision ke sath jo uske center mein hai, aur har depth ka waqt bhi.

Skills ke liye wahan jao, aur usay route karne do. Sab **6 Foundations** se shuru karte hain, browser tab mein, kuch install kiye bagair, chahe coding aati ho ya nahi. Phir ek decision: AI se apna kaam karo (Mode 1), ya AI banao jo kaam khud kare (Mode 2). Yeh road **Mode 2** maangti hai, kyunki vertical FDE manufactured Workers bechta hai, personal productivity nahi.

Do numbers is planning ke liye matter karte hain. Pehli shipped Digital FTE tak sabse tez route roughly **15 hours** focused kaam hai. Ek governed workforce, evaluations se proven, roughly **28 hours**. Yeh hours woh legs hain jinpar aap yeh road chalte ho — semesters nahi, shaamon ke din.

:::info Kaun Page Jeetta Hai
Jab yeh page aur Getting Started kisi course ka naam, sequence, ya hour count par disagree karein, **Getting Started jeetta hai**. Yeh curriculum ka apna source of truth hai.
:::

---
[⬅ Piche: Do Problems, Ek Gap](00-two-problems-one-gap.md) · [⬆ Index](README.md) · [Agla: Nau Stations Ka Roadmap ➡](02-nine-stations-roadmap.md)
