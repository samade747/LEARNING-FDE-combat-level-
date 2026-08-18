# 04 — What Fills the Pod: Two Systems of Record

## Sawal: Darwaze Se Kya Andar Aata Hai?

Ek Palantir engineer Palantir ka pehle se bana hua ontology aur tooling le kar aata hai — asal
leverage, lekin wahi cage bhi jo pichle part mein describe hua. Vendor hata do — bacha kya? Agar
honest jawab hai "method, uske sar mein," to woh sirf hours bech rahi hai — wahi services pyramid
jise replace karna tha.

**Do cheezein travel karti hain, aur dono Systems of Record hain:**

**Pehla — method, jo usne khud nahi banaya.** Yeh book, deep aur pehle se governed, website ke tor
par human readers ke liye aur MCP par agents ke liye serve hoti hai. Yeh sikhati hai outcome kaise
specify karo, Worker kaise manufacture karo, loop kaise chalao, checker par kaise bharosa karo, aur
production mein result kaise prove karo. Har graduate ke paas wahi ek hai, aur yeh Karachi ki
accounting firm aur Chicago ki firm mein identical hai.

**Doosra — profession, jo usne khud banaya.** Ek vertical, ek jurisdiction, uske aur ek committed
domain expert ke through governed: law, standards, expert ke derived procedures, invariants,
decision map. Yeh ek professional outcome se shuru hoti hai, poori tarah cover kiya gaya, aur
engagement-by-engagement mota hota jaata hai. **Yeh kisi aur ke paas nahi.**

Dono MCP bolti hain, isliye agent dono ek sath parh sakta hai: ek batati hai Worker kaise banayein,
doosri batati hai profession kya maangti hai.

## Dev Shop Objection Ka Jawab

Bai ki shart thi shared primitives, taake engineer kabhi scratch se shuru na kare. Dono Systems of
Record is shart ko poora karte hain. Method har client par identical hai — exactly wohi property jo
woh maangta hai. Profession ek vertical/jurisdiction ke liye "what work must obey" ki primitive
layer hai. Koi bhi code nahi jo har customer ke liye fork hoti ho — yehi maintenance curve modta hai:
aap ek governed corpus maintain karte ho, code ke bajaye.

## Yeh Kaise Mota Hota Hai

Bai ka rule: jo bespoke aur ek customer ke liye unique hai woh sirf usi ke liye rahe; jo generalize
ho sakta hai woh waqt ke sath generalize ho jaye. Vendor-neutral version isi rule ko alag manzil tak
le jata hai: jo generalize hota hai woh vendor ke platform mein nahi jaata — woh **vertical System
of Record** mein jata hai. Standard jo teen clients govern karne laga, procedure jo expert ne ek
baar likhi aur ab har firm par sign off karta hai, invariant jo jurisdiction ki har firm mein hold
hua. **Yehi mechanically "mota hona" hai, aur isi liye doosra client pehle se sasta serve hota hai.**

## Ek Pod Ka Ek Insan

AWS jo client ko bhejta hai dekho: 5-6 engineers ka pod, on-site ~45 din ke liye. Yehi forward
deployment dikhti hai jab log haath se banate hain — chhoti team chahiye hoti hai. Yeh book badalti
hai pod mein **kaun** hota hai. Ek graduate wahi kaam akela client tak le jata hai. Jo log uske
bagal baithte the, ab woh Digital FTEs hain — Workers jo engineer banata aur chalata hai. **Team of
five ek human tak simat jati hai jo Workers ki ek workforce command karta hai.**

**Risk jo yeh paida karta hai.** Bai khud puchta hai: kya kai FDEs ek project par kaam karna
chahiye? Uska jawab: haan, single point of failure se bachne ke liye — ek insan jiske paas sari
information ho, chhutti par chala jaye, aur engagement ruk jaye. Ek pod ka ek insan hi yeh risk
apni khalis shakal mein hai. Book ka jawab: risk gayab nahi hota — insan ke sar se **artifacts**
mein move hota hai: spec, evals, governed corpus, deployed Worker aur uska runbook. Test: agar aap
do hafte unreachable ho jaayen, kya koi doosra graduate aapke repository se aapka engagement pick
kar sakta hai? Agar nahi, to yeh pod of one nahi — yeh **bus factor of one** hai.

## Teesra Darwaza: Freelance FDE

Ab teesra address khula hai — open freelance market. Upwork ek dedicated FDE category chalata hai:
pehli integration $2,000-5,000, custom implementation $5,000-15,000, enterprise deployments
$15,000+, ongoing support $4,000-10,000/mahina, strategic consulting $150-250/ghanta. UK mein
contract FDEs £600-750/din mid-level, £1,200-2,000/din principal level.

Honest reading: category exist karti hai, supply nahi. Marketplace ne shelf pehle bana di, kisi ne
bhi usay stock nahi kiya — jo trained reader ke liye ek **opening** hai. Yeh darwaza teen tareeqon
se doosron se alag hai: (1) yeh **native market** hai vendor-neutral FDE ka — vendor ka FDE
freelance kar hi nahi sakta, uska role vendor ke payroll aur platform se welded hota hai. (2) retainer
tier maintenance-work-in-disguise nahi — yeh Digital FTE subscription model hai bahar se chalaya
gaya. (3) **is darwaze ki koi border nahi** — Karachi, Lagos, ya Bangalore se wahi contract clear ho
sakta hai.

## Directly Hire Karo, Title Gayab Ho Jata Hai

"FDE" kabhi engineer ya unki skills ki description nahi thi. Yeh batata hai woh **kahan** kaam karte
hain: client ki company ke andar, ek outsider ke tor par, poori line end-to-end carry karte huay.
Sawal simple hai: unki company kiski hai? Apni company ke andar banao — yeh chaar core roles hain.
Client ki company ke andar banao — wahi kaam FDE kehlata hai. Ab us engineer ko directly hire karo.
Client ki company unki apni company ban jaati hai. Woh ab forward deployed nahi — sirf deployed hain.
Kaam wahi hai, sirf address badla. Naam **AI-Native Company Architect** ban jata hai.

Yeh sirf vendor-neutral FDE ki freedom hai: woh company mein poori tarah join ho sakta hai. Discipline
insan mein rehti hai, kisi vendor ke platform mein nahi — yeh unke sath andar chali jaati hai. Vendor
ka FDE yeh nahi kar sakta: jis din woh Palantir ya OpenAI chhorta hai, poora platform peeche reh jata
hai. **Client aapko FDE ki tarah rent kar sakta hai, phir aapko in-house AI-Native Company Architect
bana sakta hai — bina ek bhi step khoye.**

---
[⬅ Market aur Services Industry](03-the-fde-market-and-services-industry.md) · [⬆ Index](README.md) · [Agla: Skill Author aur Connector/Plugin Engineer ➡](05-skill-author-connector-plugin-engineer.md)
