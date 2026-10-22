# 14 — 12. Monitoring, Quality, and LLMOps

Evals, observability, aur production mein AI quality track karne ki vocabulary.

---

### LLMOps

The operational practices for deploying, monitoring, and maintaining LLM-based applications in production. Like DevOps, but specific to AI systems, handling model versioning, prompt management, evaluation, and drift.

> 💡 **Analogy:** DevOps is how you keep a traditional web application running smoothly. LLMOps is how you keep an AI agent running smoothly, which is harder because AI behavior is non-deterministic, prompts need versioning, models get updated, and quality can silently degrade over time.

### Logging

Recording events, actions, and errors during system operation. Logs are the "diary" of a running application, essential for diagnosing problems.

### Tracing

Following a single request through every service and step it touches, from the user's message to the final response.

> 💡 **Analogy:** Tracking a parcel from TCS: from pickup, through sorting facilities, onto delivery vehicles, to your doorstep. Tracing does this for requests through software systems.

### Telemetry

Automatically collecting and transmitting performance data from a running system, including CPU usage, response times, error rates, memory consumption.

### Observability

The ability to understand what's happening inside a system by examining its external outputs (logs, metrics, traces). An "observable" system lets you diagnose problems without guessing.

> 💡 **Analogy:** A car's dashboard gives observability into the engine: speed, fuel, temperature, warning lights. Without it, you'd have to open the hood every time something felt wrong.

### Evaluation / Evals

Systematic testing of an AI system's output quality, measuring accuracy, helpfulness, safety, and consistency against defined criteria.

> 🔹 **Example:** You build a customer support agent and run 500 test questions through it. You measure: Did it answer correctly? (accuracy: 94%). Did it stay polite? (100%). Did it hallucinate any policy details? (3 out of 500). Did it know when to escalate? (97%). These numbers are your eval results: they tell you if the agent is ready for production.

### Offline Eval / Online Eval

**Offline eval:** Testing against pre-prepared test cases _before_ deployment (like a dress rehearsal. **Online eval:** Monitoring quality _while live_ and serving real users) like audience reviews after opening night.

### A/B Testing

Comparing two versions by showing Version A to half the users and Version B to the other half, then measuring which performs better.

> 🔹 **Example:** Testing two different system prompts: does Prompt A or Prompt B produce more helpful customer service responses? Split traffic 50/50 and measure satisfaction scores.

### Regression Test

Verifying that new changes haven't broken functionality that previously worked.

> 💡 **Analogy:** After remodeling your kitchen, you check that the plumbing, electricity, and gas still work; not just that the new cabinets look nice.

### Prompt Versioning

Tracking changes to prompts over time, like version control for code. Version 1 of a prompt may behave very differently from Version 5; you need to know which version is in production.

> 🔹 **Example:** Your customer support agent's system prompt has gone through 12 iterations. Version 8 accidentally made the agent too apologetic ("I'm so sorry" in every response). Version 9 fixed it. Without prompt versioning, you'd never track down what changed or roll back if needed.

### Model Versioning

Tracking which version of an AI model is being used. Model updates can change behavior; you need to identify when a model upgrade caused a quality change.

### Drift

Gradual degradation of system performance over time, often because real-world data changes from what the model was trained on.

> 🔹 **Example:** A spam filter trained in 2023 becomes less effective by 2026 because spammers changed tactics. The real world "drifted" away from the training data.

### Monitoring

Continuously watching a system's health, checking for errors, slowdowns, anomalies, and unexpected behavior in real time.

### SLA (Service Level Agreement)

A formal commitment about system performance, typically guaranteeing uptime, response time, and availability.

> 🔹 **Example:** "Our API will be available 99.9% of the time and respond within 200 milliseconds." If the provider misses this, contractual penalties may apply.

### SLO (Service Level Objective)

An internal performance target, usually stricter than the external **SLA**: the goal you aim for to comfortably meet your commitments.

> 🔹 **Example:** Your SLA promises customers 99.9% uptime (8.7 hours downtime/year max). Your internal SLO targets 99.95% uptime (4.4 hours/year). By aiming higher internally, you have a safety margin, even if something goes wrong, you still meet the customer-facing commitment.

### Incident

An unplanned event that disrupts or degrades service, such as a crash, data loss, security breach, or major performance problem.

### Rollback

Reverting a system to a previous, known-good version when a new update causes problems.

> 💡 **Analogy:** A tailor alters your suit and it looks worse. Rollback: undo the alterations and return to the previous version that actually fit.

---

---
[⬅ Prev](13-agentic-commerce-and-payments.md) · [Next ➡](15-protocols-and-standards.md)
