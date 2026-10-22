# Project 1 — Call It Before It Happens

**Time:** ~15 min · **Tool:** any free AI assistant

## Steps

1. Ek real decision pick karo jo is hafte karne wale ho (offer lena/na lena, kharidna/wait karna,
   conversation karna/chhodna).
2. **Prediction Lock** likho AI se kuch poochne se pehle (Discipline 1 ke 4 lines): real decision,
   settling fact, position+reason, confidence+flip-condition.
3. Ab **premortem** chalao — isi baar AI ko decision batao (yeh ek baar exception hai, kyunke
   tum chahte ho AI attack kare, agree na kare):

   ```text
   I've decided to [your decision]. Picture it's six months from now and
   this turned out to be a mistake. Don't reassure me. List the three
   most likely reasons it failed, most likely first, and keep them
   specific to my situation.
   ```

4. 3 reasons ko apni Line 4 ke against parho. Usually ek failure mode hoti jo tumne nahi dekhi —
   yehi catch hai. Ek safeguard sentence likho uske khilaf.

## Done

- [ ] Ek failure mode naam ki jo premortem ne surface ki jo pehle nahi dekhi thi
- [ ] Ek safeguard line likhi uske khilaf
- [ ] Dono lines apni Decision Dossier ke pehle page ke liye rakhi
