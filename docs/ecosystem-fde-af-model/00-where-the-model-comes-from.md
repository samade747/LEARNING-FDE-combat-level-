# 00 — Yeh Model Kahan Se Aaya

Model is book mein invent nahi hua. Teen sources ek hi future ki taraf ishara karte hain: ek company ne
kya prove kiya, market kya predict karta hai, aur yeh book dono ko combine karke kya add karti hai.

## Palantir Ne Kya Prove Kiya

Palantir ek bari US software company hai jo governments aur bari companies ke liye data systems banati
hai. Bees saal pehle usay ek problem thi jo har software company ko hoti hai. Agar ek company sabko ek
hi finished product bechti hai, product kisi ke bhi real kaam mein bilkul fit nahi hota. Agar har
customer ke liye custom software banaya jaye, sainkron alag systems maintain karne parte hain, aur kaam
kabhi aasan nahi hota.

Palantir ne teesra rasta dhoonda. Yeh ek core platform banati hai. Phir **Forward Deployed Engineers
(FDEs)** har customer ke andar bhejti hai taake platform ko customer ki real needs ke mutabiq fit karein.
Sabse zaroori step yeh hai: jab kai customers ko wahi improvement chahiye ho, Palantir usay shared
platform mein add karti hai. Aage aane wale customers isay bina dobara banaye use kar sakte hain. Log
is process ko ek gravel road ke highway banne se compare karte hain: har project agle project ke liye
rasta behtar karta hai.

Yeh approach kaam karti thi, lekin bees saal tak rare rahi kyunke customization mehngi thi — teams ko
saalon lagte the. AI ne demand aur cost, dono badal diye. Ek language model ek general capability hai,
finished business solution nahi — kisi ko usay company ke data, rules, workflows se jorna hota hai. AI
engineers ko yeh kaam bohot tez karne mein help karta hai. Ek engineer AI agents ke saath ab woh kar
sakta hai jo pehle ek team ko saalon lagta tha.

Isiliye yeh role 2026 mein tezi se phel raha hai. OpenAI ki bari FDE team hai. Anthropic aur Google Cloud
bhi hire kar rahe hain. a16z (Andreessen Horowitz) ne FDE ko "startups ki hottest job" kaha hai. Kam cost
ka matlab yeh bhi hai ke ab ek graduate ek mid-size firm ke liye is model ko use kar sakta hai, jabke
purana model billion-dollar contracts par depend karta tha.

## Market Kya Predict Karta Hai

Alex Becker (HYROS founder) ne ek widely-shared prediction ki: aaj zyada tar business software finished
app ki tarah bikta hai — subscribe karo, jaisa aaya waisa use karo. Becker kehta hai yeh din khatam ho
rahe hain. Iske bajaye companies ek **open base** (jo woh badal sakte hain) ke liye pay karengi, aur ek
AI agent simple prompt se pieces jorega aur missing features add karega.

Uske hisaab se ek software company teen positions mein se ek mein survive karegi:

1. Ek base provide karo jo doosre uspar bana sakein.
2. Essential services provide karo (payments, messaging, hosting).
3. Ek product own karo jiski value zyada log use karne se barhti hai (network effect).

Ek aakhri prediction sabse zyada matter karti hai: jeetne wale bases un mein AI ke liye correct context
pehle se built-in hoga — "LLM optimized with the correct context built into them already."

Doosre forecasters bhi aisi hi change describe karte hain, lekin warning ke saath. **AI Futures Project**
ka forecast: har economy mein do workforces — insaan aur AI agents. AI companies ek waqt mein ek
profession automate karti hain (jaise accounting pehle, phir law, medicine).

Us forecast mein ek AI lab apna khud ka model ek profession ki knowledge par train karti hai. Lab
experts interview karti hai, data kharidti hai, training jari rakhti hai jab tak profession ki zyada tar
knowledge lab ke model ke andar na aa jaye. Lekin jo log system bana rahe hain unki us profession mein
kam ya koi experience na ho. Profession finished system paati hai, jabke lab zyada control aur economic
value rakhti hai.

FDE AF Model iske ulta plan hai. Humare model mein accountants aur unke saath kaam karne wale graduates
accounting vertical banate hain, doctors healthcare vertical. Har profession apna khud ka AI banati hai,
apni knowledge rakhti hai, aur result ki maalik hoti hai.

Agar forecasters sahi hain aur agle saal koi bara lab ek general accounting AI release kare, kya yeh
accounting vertical ki zaroorat khatam kar dega? Nahi — teen wajah:

1. **Verticals labs ke models use karti hain, unse compete nahi karteen.** Farq yeh hai: knowledge model
   ke andar training nahi hoti, model ke bahar ek governed System of Record mein rehti hai jo profession
   ki hai. Model isay parhta hai jab zaroorat ho. User apna khud ka model laata hai, to model behtar hone
   par vertical ko woh improvements free milte hain.
2. **Ek general AI khud ko company ke andar deploy nahi kar sakti.** Usay company ke data, workflows,
   aur logon ke mutabiq fit karna padta hai — yeh Layer 4 ka kaam hai, FDE ka lead kiya hua. Zyada
   capable models is kaam ko zyada valuable banate hain, kam nahi.
3. **Har profession aur country mein trusted AI vertical banane ka limited waqt hai.** Pehla strong
   domain ecosystem replace karna mushkil ho jata hai — profession ka trust, experienced experts, rights-
   cleared knowledge, aur detailed local rules.

## Yeh Book Kya Add Karti Hai

Har source mein kuch missing hai. Becker demand describe karta hai, lekin uski picture mein har service
team profession ki knowledge har client ke liye zero se dobara banati hai. Palantir ne delivery model
prove kiya (aur usi se apna Skywise aviation platform bana liya, jo Airbus ke liye custom kaam se shuru
hua tha), lekin poora pattern ek company ke andar band raha — aap isay seekh kar khud nahi chala sakte.

FDE AF Model dono ideas combine karta hai aur do cheezein badalta hai. **Pehla:** yeh har profession ki
knowledge ko vertical layer mein ek permanent ghar deta hai. Knowledge ek baar likhi jaati hai aur reuse
hoti hai, har client ke liye dobara banayi nahi jaati. **Doosra:** yeh poore pattern ko teachable banata
hai, to graduates isay seekh sakte aur chala sakte hain, ek company ke andar band rakhne ke bajaye. Model
continuous improvement ko bhi ek formal rule banata hai: customer work se reusable lessons shared
platform mein add hone ke liye evaluate hone chahiye.

---
[⬆ Index](README.md) · [Agla: Layer 0 Aur Layer 1 ➡](01-layer-0-and-layer-1.md)
