# 🤖 Rule-Based AI Chatbot

A simple **rule-based chatbot built with Python** that responds to predefined user inputs.

This project demonstrates how basic chatbot behavior can be created using **Python dictionaries, loops, conditional logic, string methods, and input normalization** — without using machine learning or external AI APIs.

---

## ✨ Features

* 💬 Responds to predefined questions and commands
* 🔤 Converts user input to lowercase
* 🧹 Removes unnecessary spaces using `.strip()`
* 🔄 Maps similar phrases to canonical inputs using a synonym dictionary
* 🧠 Uses dictionary lookup instead of repetitive `if-elif` statements
* 🔁 Runs continuously until an exit command is entered
* ❓ Provides a fallback response for unknown inputs
* ⏳ Displays a simple "thinking" message before responding

---

## 🧠 How It Works

The chatbot uses **two dictionaries**.

### 1. Response Database

The `database` dictionary contains the chatbot's canonical questions and responses:

```python
database = {
    "hello": "Hi there! How can I help you today?",
    "how are you": "I'm just a bunch of if-else logic, but I'm doing great!",
    "what is your name": "I'm ChatBot, your friendly rule-based assistant.",
}
```

### 2. Synonym Mapping

The `synonyms` dictionary maps different ways of asking something to a single canonical key:

```python
synonyms = {
    "hi": "hello",
    "hey": "hello",
    "hiya": "hello",

    "how are you doing": "how are you",
    "how r u": "how are you",

    "your name": "what is your name",
    "who are you": "what is your name"
}
```

For example:

```text
User: hey
       ↓
synonyms
       ↓
hello
       ↓
database
       ↓
Hi there! How can I help you today?
```

This approach avoids storing the same response multiple times.

---

## 🔄 Input Processing

Before processing the user's message, the chatbot normalizes the input:

```python
user_input = str(input("Enter your input message : ")).strip().lower()
```

This means:

* `.strip()` removes extra spaces from the beginning and end.
* `.lower()` converts the input to lowercase.

So:

```text
"   HELLO   "
```

becomes:

```text
"hello"
```

---

## 🔑 Canonical Input

The chatbot then checks whether the user's input exists in the synonym mapping:

```python
modify_input = synonyms.get(user_input, user_input)
```

If the input exists:

```text
"hey" → "hello"
```

If it doesn't exist, the original input is retained.

For example:

```text
"hey"   → "hello"
"hi"    → "hello"
"help"  → "help"
```

The resulting key is then used to search the response database.

---

## 🚀 Example

```text
Enter your input message : hey
Chatbot is thinking !....
Hi there! How can I help you today?

Enter your input message : who are you
Chatbot is thinking !....
I'm ChatBot, your friendly rule-based assistant.

Enter your input message : how r u
Chatbot is thinking !....
I'm just a bunch of if-else logic, but I'm doing great!

Enter your input message : xyz
Chatbot is thinking !....
I do not understand.

Enter your input message : exit
Goodbye! Talk to you soon.
```

---

## 🛠️ Technologies Used

* **Python 3**
* Python Dictionaries
* `while` loops
* `if` statements
* String methods
* `.get()` dictionary method
* User input handling

No external libraries are required.

---

## 📁 Project Structure

```text
rule-based-ai-chatbot/
│
├── chatbot.py
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/rule-based-ai-chatbot.git
```

### 2. Enter the project directory

```bash
cd rule-based-ai-chatbot
```

### 3. Run the chatbot

```bash
python chatbot.py
```

---

## 💡 Concepts Practiced

This project was built to practice fundamental Python concepts:

* Variables
* Dictionaries
* Key-value mapping
* String manipulation
* `.strip()`
* `.lower()`
* `.get()`
* `while True`
* `break`
* Conditional statements
* Default values
* Basic input normalization
* Separating canonical responses from alternative user phrases

---

## 🔮 Possible Future Improvements

The chatbot can be extended with:

* More conversational responses
* More synonym mappings
* Multiple response variations
* Randomized responses
* Conversation history
* Better intent detection
* Regular expressions
* JSON-based datasets
* A graphical user interface
* Web-based interface
* Natural Language Processing (NLP)

---

## 📌 Project Purpose

This project is a **learning exercise in Python fundamentals and basic chatbot architecture**.

It demonstrates an important idea used in more advanced conversational systems:

> Different user inputs can be normalized into a common representation before processing.

---

## 👨‍💻 Author

**Suleman Khokhar**

Computer Science Student | Python Learner | Aspiring AI & EdTech Builder

---

⭐ If you found this project useful, consider giving the repository a star!
