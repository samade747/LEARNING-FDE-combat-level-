# 09 — 7. Data and Database Terms

Databases, schemas, aur data pipelines ki vocabulary.

---

### Database

An organized collection of data stored electronically: designed to be easily searched, updated, and managed.

> 💡 **Analogy:** A massive, perfectly organized filing cabinet. Each drawer (**table**) holds records of one type. Each folder (**row**) is one record. Each paper inside (**column**) is one piece of data.

### SQL (Structured Query Language)

The standard language for communicating with databases: asking questions, adding records, updating data.

> 🔹 **Example:** `SELECT name, phone FROM customers WHERE city = 'Karachi'` asks the database: "Give me the name and phone of every customer in Karachi."

### Table / Row / Column

**Table:** A collection of related data in rows and columns (like a spreadsheet). **Row:** One complete record (one customer, one order). **Column:** One field across all records (name, email, phone).

> 🔹 **Example:** A "Customers" table:
>
> | Name (column)      | City (column) | Phone (column) |
> | ------------------ | ------------- | -------------- |
> | Ahmed Khan (row 1) | Karachi       | 0300-1234567   |
> | Sara Ali (row 2)   | Lahore        | 0321-9876543   |
>
> The table has 3 columns and 2 rows. Each row is one customer. Each column is one piece of information about every customer.

### Query

A request for specific data from a database. Every SQL statement is a query.

> 🔹 **Example:** "Show me all orders from Karachi placed in the last 7 days" is a human query. In SQL: `SELECT * FROM orders WHERE city = 'Karachi' AND date > '2026-03-31'`. Same request, one in English, one in the database's language.

### PostgreSQL

A powerful, free, open-source database used widely in production applications, including many AI agent backends.

### NoSQL

Databases that store data in flexible formats other than strict tables (documents, key-value pairs, or graphs). Useful when data doesn't fit neatly into rows and columns.

> 🔹 **Example:** MongoDB stores data as JSON-like documents. A "customer" document can have different fields for different customers, unlike a rigid table where every row must have the same columns.

### Cache

A high-speed storage layer saving copies of frequently accessed data for faster retrieval.

> 💡 **Analogy:** Keeping your most-used spices on the kitchen counter instead of in a high cabinet. Slower to organize initially, but much faster when cooking. A cache trades storage space for speed.

### Queue / Message Broker

A system managing messages between application components, ensuring tasks are processed reliably and in order, even under heavy load.

> 💡 **Analogy:** A ticket system at a busy NADRA office. Everyone takes a number and is served in order. Even if 50 people arrive at once, nobody gets lost: the queue manages the flow.

### Kafka

A popular open-source message broker designed for handling massive streams of real-time data, commonly used in enterprise AI deployments.

### Transaction

A set of database operations that must all succeed together or all fail together, no half-done state allowed.

> 🔹 **Example:** Transferring Rs. 50,000 between JazzCash accounts: deducting from Account A and adding to Account B must both happen, or neither should. A transaction guarantees this.

### Data Pipeline

An automated sequence of steps moving data from sources to destinations, transforming it along the way.

> 💡 **Analogy:** A wheat supply chain: harvest from the farm (extract), mill into flour (transform), deliver to the bakery (load). A data pipeline does the same with information.

### ETL (Extract, Transform, Load)

The standard data pipeline pattern: **Extract** data from sources → **Transform** it (clean, restructure, enrich) → **Load** it into a destination system.

> 🔹 **Example:** Every night, an ETL pipeline (1) **extracts** sales data from 50 retail branches, (2) **transforms** it (converting currencies, removing duplicates, calculating totals) and (3) **loads** the clean data into a central database for the morning dashboard.

### Persistent Storage

Data that survives after a program ends or a computer restarts. Files on your hard drive are persistent. Data in RAM disappears when you shut down.

> 💡 **Analogy:** Writing notes in a notebook (persistent; they're still there tomorrow) vs. writing on a whiteboard that gets erased every evening (non-persistent). Agents need persistent storage to remember things across sessions.

---

---
[⬅ Prev](08-programming-and-software-terms.md) · [Next ➡](10-cloud-and-deployment-terms.md)
