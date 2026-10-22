# 04 — 2. Core AI and Machine Learning

AI/ML/DL ki bunyadi vocabulary — jo terms book se pehle bhi exist karti thi.

---

These are the foundational ideas behind everything in this book.

```
AI ⊃ ML ⊃ DL ⊃ LLMs
(Each is a subset of the one before it)
```

### AI (Artificial Intelligence)

Making computers do things that normally require human intelligence, such as understanding language, recognizing images, making decisions, solving problems.

> 🔹 **Example:** When your phone's keyboard predicts your next word in Urdu or English, that's AI. When Careem estimates your ride time based on traffic, that's AI.

### ML (Machine Learning)

A way of teaching computers by showing them examples instead of writing explicit rules. The computer finds patterns in data and learns from them.

> 🔹 **Example:** YouTube recommends videos you might like. Nobody programmed a rule that says "if user watched cricket highlights, suggest more cricket." The system learned this pattern from billions of viewing habits.

> 💡 **Analogy:** Imagine teaching a child to recognize mangoes. You don't explain the biology. You show them dozens of mangoes and say "mango." Eventually, they recognize mangoes they've never seen, even different varieties like Chaunsa and Sindhri. That's machine learning.

### DL (Deep Learning)

A more powerful version of machine learning that uses "neural networks" with many layers. It can learn extremely complex patterns, like understanding speech, generating images, or translating between languages.

> 🔹 **Example:** When Google Translate converts an Urdu paragraph into fluent English, deep learning powers that translation.

> 💡 **Analogy:** If ML is learning to recognize simple shapes, DL is learning to recognize faces in a crowded Saddar Bazaar: far more complex, but the same principle of learning from examples.

### Model

A program that has been trained on data and can now make predictions or generate outputs. When people say "GPT-4" or "Claude," they're referring to models.

> 💡 **Analogy:** A model is like a student who has studied millions of textbooks. You ask questions, they answer based on everything they've read. Different models are like different students: some are better at math, others at creative writing.

### Foundation Model

A very large, general-purpose model trained on enormous data. It can be adapted to many different tasks without retraining from scratch. Claude, GPT-4, and Gemini are foundation models.

> 💡 **Analogy:** A foundation model is like a university graduate with a broad education. They haven't specialized yet, but they can quickly adapt to many jobs: accounting, writing, research, management.

### Neural Network

A computing system inspired by the human brain, with layers of interconnected "nodes" that process information, each layer extracting increasingly complex patterns.

> 💡 **Analogy:** Imagine a series of sieves with different mesh sizes. You pour raw data through the first sieve (catches large patterns), then the next (catches finer patterns), then the next (catches the finest details). A neural network works similarly, with each layer refining the information.

### Transformer

The specific neural network architecture that powers all modern LLMs. Invented in 2017, it's especially good at understanding relationships between words, knowing that "bank" means something different in "river bank" vs. "bank account."

> 💡 **Analogy:** Older AI read sentences word by word, like reading through a keyhole (you see one word at a time and guess the meaning. Transformers read the entire sentence at once, like opening the whole door) they see every word simultaneously and understand how each word relates to every other word. This is why they're so much better at understanding language.

> 💡 **Why it matters:** Every AI model in this book (Claude, GPT, Gemini) is built on transformers. You don't need to understand the math, but you'll see the term often.

### Multimodal Model

A model that can work with multiple types of input (text, images, audio, video) not just one.

> 🔹 **Example:** You photograph a restaurant bill and ask Claude "What's the total?" The model understands both the image and your text question. That's multimodal capability.

### Reasoning Model

A model designed to "think through" complex problems step by step before answering, rather than responding instantly. Often more accurate on hard problems.

> 💡 **Analogy:** In a cricket match, some batsmen play instinctive shots (fast, sometimes reckless). Others study the field, read the bowler, and plan each shot deliberately. A reasoning model is the second type: slower but more reliable on difficult deliveries.

### Training

The process of feeding massive amounts of data to a model so it learns patterns. This happens before you ever interact with the model; it's the "education" phase.

> 💡 **Analogy:** Training is like a chef spending years at culinary school: tasting thousands of dishes, learning techniques, practicing recipes. By the time they open their restaurant (when you use the model), the learning has already happened.

### Pretraining

The first, most expensive phase of training. The model reads enormous amounts of text (books, websites, code, conversations) and learns general knowledge about language and the world.

### Post-Training

Additional training after pretraining to make the model helpful, safe, and aligned with human expectations. This is where a model learns to follow instructions, be polite, and refuse harmful requests.

> 💡 **Analogy:** Pretraining is like getting a general education (school and university). Post-training is like workplace orientation: learning company culture, communication style, and professional norms.

### Fine-Tuning

Training an existing model further on a specific, smaller dataset to make it an expert in a particular domain.

> 🔹 **Example:** Taking a general-purpose model and fine-tuning it on thousands of Pakistani tax rulings so it becomes especially good at tax advisory.

> 💡 **Analogy:** A general doctor completing additional training to become a cardiologist. Same foundational education, now specialized.

### Parameters

The internal numbers of a model that get adjusted during training. More parameters generally means a more capable model. Modern LLMs have billions or trillions of parameters.

> 💡 **Analogy:** Parameters are like the individual threads in a massive carpet. During training, each thread is adjusted (color, tension, placement) until the complete pattern emerges. A model with 100 billion parameters has 100 billion threads forming an incredibly complex pattern.

### Weights

The specific numerical values of the parameters after training. When someone says "downloading the weights," they mean the file containing all those trained numbers: the model's learned knowledge.

### Dataset

A collection of data used to train or evaluate an AI model.

> 🔹 **Example:** A dataset for training a spam filter might contain 1 million emails, each labeled "spam" or "not spam." A dataset for training a translation model might contain millions of English-Urdu sentence pairs.

### Benchmark

A standardized test for measuring and comparing how well different AI models perform.

> 🔹 **Example:** Just like CSS or Cambridge exams let you compare students, benchmarks like MMLU (general knowledge) or HumanEval (coding ability) let researchers compare AI models fairly.

### Inference

The process of a trained model generating a response to your input. Every time you ask Claude a question and get an answer, that's inference.

> 💡 **Analogy:** Training is studying for an exam. Inference is sitting the exam. The learning already happened: now the model applies what it learned. You pay for inference (each API call costs money), not for training.

---

---
[⬅ Prev](03-agent-factory-book-specific-terms.md) · [Next ➡](05-llm-basics.md)
