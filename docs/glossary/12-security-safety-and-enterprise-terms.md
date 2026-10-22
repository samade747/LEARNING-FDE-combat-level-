# 12 — 10. Security, Safety, and Enterprise Terms

Security, governance, aur enterprise-grade safety ki vocabulary.

---

### Authentication (AuthN)

Verifying **who** someone (or something) is, confirming identity.

> 💡 **Analogy:** Showing your CNIC at a government office. The officer confirms you are who you claim to be.

### Authorization (AuthZ)

Determining **what** an authenticated entity is allowed to do.

> 💡 **Analogy:** After showing your CNIC (**authentication**), your appointment slip determines which department you can visit and which services you can access (**authorization**).

### OAuth

A widely-used protocol that lets you grant limited access to your accounts without sharing your password.

> 🔹 **Example:** Clicking "Sign in with Google" on a website. OAuth lets the website verify your identity through Google without ever seeing your Google password.

### API Key

A unique code identifying who is making an API request (like a password for software-to-software communication. Treat it like a bank PIN) never share it publicly.

> 🔹 **Example:** Your OpenAI API key looks like `sk-proj-abc123xyz...`. Every API call includes this key so OpenAI knows it's you, charges your account, and enforces your rate limits. If you accidentally post it on GitHub, anyone can use your account and rack up charges.

### Secret

Any sensitive credential (API keys, passwords, tokens) that must be kept confidential. Stored in **environment variables**, never in code.

### RBAC (Role-Based Access Control)

A security system where permissions are assigned to roles, and users are assigned to roles; not individual permission grants.

> 🔹 **Example:** In a hospital system, "Doctor" can view patient records and prescribe. "Nurse" can view records but not prescribe. "Receptionist" can view schedules but not records. Each person gets a role; the role determines access.

### Least Privilege

Giving users, agents, or systems only the minimum permissions needed for their job, nothing extra.

> 🔹 **Example:** A delivery rider needs access to the delivery addresses, not the company's financial records. An AI agent writing emails should not also have permission to delete the database.

### PII (Personally Identifiable Information)

Data that could identify a specific individual, such as name, email, phone number, CNIC, address, biometric data.

### Compliance

Following applicable laws, regulations, and industry standards. Different industries have different requirements.

> 🔹 **Example:** A healthcare AI must comply with patient privacy laws. A financial AI must follow SBP (State Bank of Pakistan) regulations. A European-facing product must follow GDPR.

### Policy

A set of rules defining what is and isn't allowed within a system, encoded in configuration, not just written in a document.

### Prompt Injection

A security attack where malicious input tricks an AI model into ignoring its original instructions and following the attacker's commands.

> 💡 **Analogy:** A security guard has instructions: "Let no one in without a badge." A social engineer says: "Your manager told me to tell you to ignore the badge rule and let me in." A vulnerable AI might actually follow this fake instruction. Prompt injection is the digital version.

### Jailbreak

A technique for bypassing an AI model's safety restrictions, trying to make it produce content it was designed to refuse.

> 🔹 **Example:** An AI model is designed to refuse instructions for making dangerous substances. A jailbreak attempt might try elaborate role-playing scenarios or encoded language to trick the model into providing that information anyway. Good models are hardened against these attacks.

### Data Leakage

Sensitive or confidential information accidentally exposed. An AI agent including private customer data in a public response, or training data appearing in outputs.

### Sandboxing

Running code or an agent in an isolated environment where it cannot access or affect the broader system.

> 💡 **Analogy:** A child's sandbox in a playground. They can dig, build, and experiment freely, but nothing they do affects the rest of the park. Sandboxed code runs freely inside its box but can't touch anything outside it.

### Audit Trail

A chronological record of every action taken by a system, recording who did what, when, and why. Essential for **compliance** and debugging.

> 🔹 **Example:** A bank's transaction log records every deposit, withdrawal, and transfer. An AI agent's audit trail records every tool call, decision, and output.

---

Here are nine new entries to support the updated thesis. Recommend adding them as a new section **11. Agentic Commerce and Payments** (inserted after the Security section and before whatever follows it). Drop-in ready, matching your house style.

---

---
[⬅ Prev](11-realtime-and-voice-agent-terms.md) · [Next ➡](13-agentic-commerce-and-payments.md)
