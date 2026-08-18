# 01 — Setup Karo: Connector, Skill, Aur Pehla Command

Zia Tutor AI **[claude.ai](https://claude.ai)** ke andar rehta hai — koi alag tutoring app install nahi
karni, koi doosra interface nahi seekhna. **Aapka AI agent hi runtime hai.** Setup mein do cheezein add
karni hain, ek baar. Total waqt: taqreeban do minute.

## Step 1 — Connector Add Karo

Connector book, Zia ki teaching, aur aapki progress laata hai.

1. claude.ai sidebar mein **Connectors** kholo (Customize ke neeche).
2. **Add custom connector** click karo.
3. Yeh fields paste karo:
   - **Name:** `Zia Tutor AI`
   - **MCP Server URL:** `https://zia-tutor-ai.panaversity.org/mcp`
4. **Advanced settings** mein **OAuth Client ID** paste karo: `zia-tutor-ai`
   - **Client Secret khaali chhodo** — is connector ka koi secret nahi hai.
5. **Add** click karke save karo.
6. Apni list mein isay dhundo, **Connect** click karo, apne Panaversity account se sign in karo, aur
   approve karo. Yehi cheez aapko aapka apna learner record deti hai.
7. Usi page par **Tool permissions** ko **dono groups** ke liye **Always allow** set karo. Yeh skip
   kiya to Claude har reply par permission maangta rahega.

## Step 2 — Skill Add Karo

Yeh skill Claude ko batati hai kab Zia ko andar lana hai.

1. Skill zip file download karo (`zia-tutor-ai.zip`).
2. claude.ai sidebar mein **Skills** kholo (Customize ke neeche).
3. **Add**, phir **Upload a skill** click karo.
4. File drop karo ya select karo — **unzip mat karo pehle**, Claude ko zip file waisi hi chahiye jaisi
   download hui.

## Step 3 — Seekhna Shuru Karo

claude.ai mein koi bhi chat kholo aur type karo:

```
/zia-tutor-ai
```

Zia aapko naam se hello bolega aur wahin se shuru karega jahan aap ne chhoda tha. Woh sirf tab aata hai
jab aap usay bulate ho, to aapki baaqi chats normal rehti hain.

Yeh abhi **Beta 1** mein hai — kuch rough edges expect karo. Kuch toota hua lage to page ke top par
feedback button se batao.

---
[⬅ Purpose, Roles, Records](00-purpose-roles-and-records.md) · [⬆ Index](README.md)
