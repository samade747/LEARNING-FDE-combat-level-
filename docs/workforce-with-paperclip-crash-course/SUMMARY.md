# Building a Workforce with Paperclip — 90-Minute Crash Course — Summary

Mode 2 (Manufacturing), Phase 3 · Scale the Workforce. **7 Scenarios** — kuch nahi se ek AI company
jo real cheezein banaye, aap board ki tarah chalate ho. Paperclip = AI-agents-company chalane ka
operating system. Collaboration pattern: **Aap** (board) → apna general agent → **Paperclip** (company
hold karta hai, employees jagata hai) → **CEO** (pehla hire, plan+delegate karta hai, khud kaam nahi
karta) → **Team** (specialists, real kaam karte hain).

## 00 — Scenarios 1-2: Setup Aur Company
- **Scenario 1 (~15 min):** Company = self-contained AI org (goal + agent-team + task-board + budget).
  Setup: Paperclip laptop pe khada karo, company "Northwind" banao (goal: newsletter, 1000 subscribers/
  90 days), monthly budget ceiling $20, naye-hire sign-off required. Done jab: dashboard goal+budget+
  approval-gate dikhaye.
- **Scenario 2 (~10 min):** CEO = pehla agent, koi manager nahi (seedha board ko report karta hai).
  Local coding-agent adapter se hire karo (no separate API key). **Zaroori:** CEO ko bhi aap approve
  karte ho — yehi poora point hai. Done jab: dashboard idle CEO, heartbeat enabled dikhaye.

## 01 — Scenarios 3-4: Strategy Aur Team
- **Scenario 3 (~15 min):** Heartbeat = scheduled kaam-ka-waqt. Pehli heartbeat pe CEO strategy draft
  kar ke `in_review` mein daalta hai, **aage nahi badhta jab tak sign-off na ho**. Approve karne pe
  activity-log row `actor_type = user` prove karti hai ke board ne decide kiya.
- **Scenario 4 (~20 min):** Task = work-unit (assignee agent hota hai), flow: backlog→todo→in_progress→
  in_review→done. Approved strategy ke baad CEO goal ko tasks mein todta hai, delegate karta hai — yahin
  company "workforce" banti hai. Sharp CEO tasks banane se **pehle** hire-request file karta hai. Hire =
  approval-inbox item. Approve karne pe CEO khud sub-tasks assign karta hai. Approve ke baad CEO ki
  heartbeat pause karna best practice — "autonomy ek grant hai, wapas le sakte ho."

## 02 — Scenarios 5-6: Budget Aur Audit Trail
- **Scenario 5 (~5 min):** Har agent spending-cap carry karta hai. Rule: 80% pe warning, 100% pe agent
  **pause**. Honest catch: budget sirf per-token-billed spend count karta hai — keyless local runtime
  $0 record karta hai, rail tab bite karega jab paid model wire ho. Warning: paid API key shell-export
  karo, file mein kabhi mat likho.
- **Scenario 6 (~10 min):** Audit trail = `activity_log` (per-action row) + `cost_events` (dollar
  story), embedded Postgres mein — koi bhi outsider (CFO/legal) seconds mein history reconstruct kar
  sake. `actor_type` column (user vs agent) human-decision ko agent-action se alag karta hai.

## 03 — Scenario 7 + Monthly Operating
- **Scenario 7 (~10 min):** Workspace = real folder/git-repo jahan company point ho, taake agent asal
  files likhe (comments se aage). Example: CMO ko task do landing-page.html banane ka, heartbeat fire
  karo, file disk pe dekho. "Yehi demo aur company ke beech ki line hai."
- **Har mahine — Company Operate Karo (~10 min):** Company chalana one-time setup nahi, standing
  responsibility hai. Monthly audit prompt: sab hires/config/schedules/approvals since-last-audit walk
  through, koi bhi bina-explicit-signoff cheez flag karo. **Common "loose knobs":** budget-cap-less hire
  (ceiling inherit kar leti hai), overloaded agent, drifted config file, parked in_review task.
- **Kya banaya:** ~1 ghante mein real company — goal, CEO-hire, strategy-approval, specialist-approval,
  delegated-work, real-workspace, ledger-audit. Har move governance move tha, prompt nahi. **2 durable
  takeaways:** `AGENTS.md` artifact (general agent har session parhta hai), aur stance: **autonomy ek
  grant hai, default nahi.**
