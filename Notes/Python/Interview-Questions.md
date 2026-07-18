## ❓ Interview Questions & Answers
 
**1. What is Python?**
Python is a high-level, interpreted, general-purpose, object-oriented programming language created by Guido van Rossum, first released in 1991.
 
**2. Why is Python called a high-level language?**
Because its syntax is close to human language and abstracts away low-level details (like memory management), making it far easier to read and write than machine code or low-level languages.
 
**3. What is an interpreter?**
A program that reads and executes source code directly, typically line by line, rather than translating the whole program into machine code ahead of time like a compiler does. (CPython specifically compiles to bytecode first, then runs that bytecode on the Python Virtual Machine.)
 
**4. Name five areas where Python is used.**
Web development, artificial intelligence, data science, automation, and web scraping (also common: machine learning, deep learning, game development, cybersecurity).
 
**5. What is the purpose of `print()`?**
It outputs/displays information — text, numbers, booleans, variables, etc. — to the screen (standard output).
 
**6. What is a comment?**
Text in code (starting with `#` in Python) that is ignored by the interpreter at runtime. Comments explain *why* the code does something, for the benefit of humans reading it later.
 
**7. What is the difference between source code and machine code?**
Source code is the human-readable code a developer writes (e.g. `print("Hello")`). Machine code is the low-level binary instructions (`1010...`) that the CPU actually executes. Compilers/interpreters bridge the two.
 
**8. What is a library?**
A collection of pre-written, reusable code (functions, classes, modules) that you can import into your program instead of writing that functionality from scratch — e.g. NumPy for numerical computing, FastAPI for building APIs.

# Lesson 2: Variables — Interview Questions & Answers

**1. What is a variable?**
A named container/reference that stores a value in memory, so the value can be reused, updated, or referred to later by that name (e.g. `age = 23`).

**2. What does the `=` operator do?**
It's the **assignment operator** — it assigns the value on the right-hand side to the variable name on the left. It does *not* mean mathematical equality (that's `==` in Python).

**3. Can a variable change its value?**
Yes. Variables can be reassigned at any time, and can even change type, since Python is dynamically typed:
```python
age = 23
age = "Twenty Four"
age = True
```

**4. What are the rules for naming variables?**
- Can contain letters, numbers, and underscores
- Cannot start with a number
- Cannot contain spaces or hyphens
- Cannot be a reserved keyword (e.g. `class`, `for`, `if`)
- Case-sensitive

**5. Is Python case-sensitive?**
Yes. `name` and `Name` are treated as two completely different variables.

**6. What does `type()` do?**
It returns the data type of a variable's current value at runtime, e.g. `type(23)` → `<class 'int'>`, `type("Alan")` → `<class 'str'>`.

**7. Why should we use meaningful variable names?**
Descriptive names (`first_name`, `total_price`) make code self-documenting and easier to read, debug, and maintain — compared to vague names like `a`, `x`, or `abc`, which force a reader to guess what they represent.