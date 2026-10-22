# 11 — 9. Realtime and Voice Agent Terms

Voice agents aur realtime systems ki vocabulary.

---

### Realtime

Processing and responding to data as it arrives, with minimal delay: as opposed to batch processing where data is collected and processed later.

### Streaming

Sending data continuously in small pieces as it becomes available, rather than waiting for the complete result.

> 🔹 **Example:** When Claude's response appears word by word instead of all at once, that's streaming. When you watch a YouTube video without downloading the whole file first, that's streaming.

### WebSocket

A communication protocol maintaining a persistent, two-way connection between client and server; both sides can send messages at any time without waiting.

> 💡 **Analogy:** A phone call (WebSocket) vs. exchanging postal letters (HTTP). On a call, both people speak whenever they want. With letters, you send one and wait for a reply.

### SSE (Server-Sent Events)

A technology for a server to push real-time updates to a client, providing one-way streaming over a standard HTTP connection.

> 🔹 **Example:** A live cricket score ticker that updates automatically without you refreshing the page. The server pushes new scores as they happen.

### Event Stream

A continuous flow of events (data points, notifications, status changes) that a system listens to and reacts to in real time.

### Voice Agent

An AI agent communicating through spoken language, listening to your voice, understanding it, and responding with speech.

> 🔹 **Example:** Calling a bank's AI assistant that understands your spoken question about your account balance and reads the answer back to you: in Urdu or English.

### ASR (Automatic Speech Recognition)

Technology converting spoken language into text.

> 🔹 **Example:** Dictating a WhatsApp message using the microphone button: ASR converts your voice to typed text.

### STT (Speech to Text)

Another term for **ASR**: converting spoken words into written text.

### TTS (Text to Speech)

Converting written text into spoken audio: the opposite of STT.

> 🔹 **Example:** Google Maps reading navigation directions aloud. An AI tutor reading an explanation to a student.

### VAD (Voice Activity Detection)

Technology detecting when someone is speaking vs. when there's silence, so the system knows when to listen and when the speaker has finished.

> 🔹 **Example:** You're talking to a voice agent and pause to think mid-sentence. Without good VAD, the agent jumps in during your pause, thinking you're done. With good VAD, it detects you're just pausing (not finished) and waits for you to continue.

### Transcription

The written text output of converting speech to text, the document produced by **ASR**.

> 🔹 **Example:** A 30-minute meeting is recorded. ASR processes the audio and produces a text transcript: "Ahmed: Let's discuss the Q3 targets... Sara: I think we should focus on Lahore first..." That written output is the transcription.

### Synthesis (Speech)

Generating natural-sounding spoken audio from text (the audio produced by **TTS**. Modern synthesis sounds nearly human) with natural pauses, intonation, and emphasis.

### Turn-Taking

Managing who speaks when in a voice conversation. The system waits for the human to finish, then responds. Good turn-taking feels natural; bad turn-taking feels like two people constantly talking over each other on a bad phone connection.

### Interruption / Barge-In

When a user starts speaking while the AI is still responding, cutting it off mid-sentence. Well-designed voice agents handle this gracefully: they stop immediately and listen.

> 🔹 **Example:** You ask a voice agent for directions to Clifton Beach. It starts describing a route via University Road, but you know that road is blocked today, so you interrupt: "No, avoid University Road." A good voice agent stops instantly and recalculates. A bad one keeps talking over you.

---

---
[⬅ Prev](10-cloud-and-deployment-terms.md) · [Next ➡](12-security-safety-and-enterprise-terms.md)
