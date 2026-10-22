# 08 — 6. Programming and Software Terms

Software engineering ki vocabulary jo AI-era mein bhi zaroori hai.

---

You don't need to be a programmer, but you'll encounter these throughout.

### Python

The most popular programming language in AI: readable, versatile, and the primary language in this book. Nearly every AI framework supports Python first.

> 💡 **Why Python?** Python reads almost like English. `if age > 18: print("Adult")` is understandable even if you've never coded. This readability is why the AI world chose Python, and why this book teaches it. You don't need to know Python before starting; Part 4 teaches you from scratch.

### TypeScript

A typed superset of JavaScript used for web applications and realtime interfaces. Covered in Part 9 of this book.

### Frontend

The part of an application users see and interact with: buttons, menus, text, images on screen.

> 🔹 **Example:** When you use Daraz.pk, the product images, search bar, shopping cart, and checkout page are the frontend.


### Backend

The part running behind the scenes (servers, databases, business logic) that users never see directly.

> 🔹 **Example:** When you click "Place Order" on Daraz, the backend processes your payment, checks inventory, notifies the seller, and schedules delivery.

### Full-Stack

A developer or application that handles both **frontend** and **backend**.

### API (Application Programming Interface)

A set of rules allowing different software programs to communicate with each other. APIs are how agents interact with the outside world.

> 💡 **Analogy:** A restaurant menu is like an API. You (the customer) look at the menu (API documentation), place an order (make a request), and the kitchen (server) prepares your meal (sends a response). You don't need to know how the kitchen works; you just use the menu.

### SDK (Software Development Kit)

A pre-built toolkit for developing applications on a specific platform.

> 💡 **Analogy:** An SDK is like a LEGO set: pre-shaped pieces with instructions so you can build specific things quickly, instead of carving every piece from raw wood.

### CLI (Command-Line Interface)

A text-based way of interacting with a computer by typing commands instead of clicking buttons.

> 🔹 **Example:** Instead of dragging a file to a folder, you type `mv report.pdf documents/`. Claude Code runs entirely through the CLI.

### HTTP / HTTPS

The communication protocol of the web. Every website visit, every API call uses HTTP (or its secure version, HTTPS).

> 💡 **Analogy:** HTTP is the postal system of the internet. Your browser writes a letter (request), addresses it to a website, and the website sends a reply (response) back through the same system.

### REST (Representational State Transfer)

A widely-used standard for designing web APIs: simple, predictable, and based on HTTP.

### Endpoint

A specific URL where an API receives requests. Each endpoint handles one specific function.

> 🔹 **Example:** `api.weather.com/current?city=Karachi` is an endpoint: the specific address where you ask for Karachi's weather.

### Request / Response

**Request:** A message from client to server asking for something. **Response:** The server's reply.

> 💡 **Analogy:** You ask a waiter for the soup of the day (request). The waiter returns with "haleem" (response).

### JSON (JavaScript Object Notation)

A lightweight, human-readable format for storing and exchanging data. The standard data format in the AI world.

> 🔹 \*\*Example:

```json
{
  "name": "Ahmed Khan",
  "city": "Lahore",
  "role": "Software Engineer"
}
```

Each piece of data has a clear label and value. Software reads JSON effortlessly.

### Schema

The structure or blueprint of how data is organized: what fields exist, what type each field is, and which are required.

> 💡 **Analogy:** A blank NADRA form is a schema: "Name goes here (text), CNIC goes here (number), Date of Birth goes here (date)." The filled-in form is the data; the blank form is the schema.

### Validation

Checking that data matches the expected **schema**: right format, right type, nothing missing.

> 🔹 **Example:** An online form rejecting your submission because you typed letters in the phone number field: that's validation catching an error.

### Library / Package

Pre-written code built and shared by others so you don't have to write common functionality from scratch.

> 🔹 **Example:** Instead of writing your own email-sending code, you use a library called `sendgrid` that handles all the complexity.

### Framework

A larger, more structured toolkit than a **library**. A framework provides the architecture of your application and defines how your code is organized.

> 💡 **Analogy:** A library is like buying individual furniture. A framework is like buying a pre-built house where you customize the rooms. FastAPI is a framework; a JSON parsing tool is a library.

### Dependency

An external library your project requires to work.

> 🔹 **Example:** Your project uses FastAPI, and FastAPI needs a library called Starlette. Starlette is a dependency: your project depends on it indirectly.

### Repo (Repository)

A project folder tracked by **Git** containing all code, files, and the complete history of changes.

### Git

A version control system that records every change to your code: who changed what, when, and why. You can always go back to any previous version.

> 💡 **Analogy:** Git is like "Track Changes" in Microsoft Word, but for entire software projects. Every edit is recorded. Every version is recoverable. Essential for team collaboration.

### GitHub

A cloud platform for hosting Git repositories: the world's largest code-sharing platform where developers collaborate.

### Environment Variable / `.env`

A setting stored outside your code (in a file called `.env`) containing sensitive information like passwords and API keys.

> 🔹 **Example:** Your OpenAI API key is stored as `OPENAI_API_KEY=sk-abc123...` in `.env` so it never appears in your public code.

### Synchronous

Operations happening one at a time, in sequence. Each step waits for the previous one to finish.

> 💡 **Analogy:** A single checkout counter at a store. Each customer is served completely before the next one starts. Simple but slow when there's a queue.

### Asynchronous

Operations that can run simultaneously. The program starts a task and moves on without waiting for it to finish.

> 💡 **Analogy:** Multiple checkout counters open at once, plus a self-service kiosk. Customers are served in parallel. Much faster overall: this is how modern AI agents handle multiple tool calls.

### Event-Driven Architecture

A software design where the system responds to events (things that happen) rather than following a rigid, predetermined sequence.

> 🔹 **Example:** A doorbell is event-driven (it only rings when pressed. You don't check the door every 5 minutes; you respond when the event occurs. AI agents often work this way) responding to incoming messages, tool results, and notifications.

### Variable

A named container in code that stores a value. `price = 500` means the variable `price` holds 500.

### Function

A reusable block of code that performs a specific task: accepts inputs, does work, returns an output.

> 💡 **Analogy:** A function is like a roti-making machine. You put in dough (input), the machine does its work, and out comes a roti (output). You can use the same machine thousands of times.

### Type Annotation

Declaring what kind of data a variable or function expects: text, number, list, etc.

> 🔹 **Example:** `age: int = 25` tells both the program and other developers: "age should always be a whole number."

### Dataclass

A Python feature for creating clean, structured data containers, like a template with named fields.

> 🔹 **Example:**
>
> ```python
> @dataclass
> class Student:
>     name: str
>     age: int
>     grade: str
> ```
>
> Now you can write `student = Student("Ahmed", 20, "A")` and the data is organized, labeled, and type-checked automatically. Much cleaner than tracking three separate variables.

### Decorator

A Python feature (written with `@`) that adds functionality to a function or class without changing its code. `@dataclass` in the example above is a decorator.

### Syntax

The grammar rules of a programming language: how code must be structured for the computer to understand it.

### Boilerplate

Repetitive, standard code needed for setup that doesn't contain your unique logic.

> 💡 **Analogy:** The "Dear Sir/Madam" opening and "Yours sincerely" closing of a formal letter. Necessary but not the interesting part.

### Linter

A tool that checks code for errors, style violations, and potential bugs, like a grammar-checker for code.

> 🔹 **Example:** You write `x=1+2` (no spaces around operators). The linter flags it and suggests `x = 1 + 2`: more readable. It also catches real bugs, like using a variable before defining it. **ruff** is the linter used throughout this book.

### Debugging

Finding and fixing errors (bugs) in code.

### Refactoring

Restructuring existing code to make it cleaner or more efficient without changing what it does.

> 💡 **Analogy:** Reorganizing your wardrobe. Same clothes, but now arranged by season and type: easier to find what you need.

### pytest

Python's most popular testing framework. You write test cases describing what code should do, and pytest verifies that it actually does it.

> 🔹 **Example:** You write a test: `assert calculate_gst(1000) == 180`. This says "when I calculate GST on Rs. 1,000, the answer must be Rs. 180." If your code returns 170, pytest tells you the test failed: catching the bug before it reaches customers.

### pyright

A Python type checker: ensures you're not accidentally passing text where a number is expected, catching errors before they cause problems.

> 🔹 **Example:** Your function expects `age: int` but somewhere in your code you accidentally pass `"twenty-five"` (text). Pyright catches this mismatch instantly, before you even run the program.

### ruff

A very fast Python linter and formatter that enforces consistent code style and catches common mistakes. Think of it as a grammar-checker and style-guide enforcer for your Python code.

### uv

A modern, blazing-fast Python package manager for installing and managing project dependencies. Replaces older tools like pip for project management: often 10-100x faster.

### pip

Python's traditional, built-in package installer. `pip install requests` downloads the `requests` library from the internet and installs it on your computer.

---

---
[⬅ Prev](07-agentic-ai-concepts.md) · [Next ➡](09-data-and-database-terms.md)
