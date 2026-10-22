# Project 2 — Audit the Confident Answer

**Time:** ~20 min · **Tool:** any free AI assistant

## Steps

1. Real sawal lo jo is hafte AI se poochte (kaunsa laptop, kaunsa loan, client ko kya charge
   karna, tenant ko kaise handle karna). Full confident recommendation leto.
2. **Reasoning Receipt** chalao — har claim ko ACCEPT/REJECT/MODIFY/SURFACED/MISSED label do,
   1-sentence why ke sath.
3. **Error Taxonomy** chalao — same answer 6 error types ke liye scan karo, khaas kar fabricated
   source, stale number, false confidence.
4. AI se khud apni recommendation grade karwao:

   ```text
   Go back through the recommendation you just gave me. List every
   factual claim as a numbered list. For each one, tell me plainly
   whether you actually know it or are estimating, and mark it KNOW
   or GUESS. For anything with a source, give me the exact title and
   year so I can look it up.
   ```

5. Ek named source search karo — real ho to milega, fabricated ho to nahi. Ek number aaj ke
   actual price/figure se check karo. Jo claim fail ho jaye, wo tumhara catch hai.

## Done

- [ ] Ek labeled row jo real catch hai (source nahi mili, number stale thi, ya confidence bina
      basis ke)
- [ ] Pata hai yeh kaunsa 6 error types mein se tha
- [ ] Receipt Decision Dossier mein add ki
