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

# Lesson 3: Data Types — Interview Questions & Answers

**1. What is a data type?**
A classification that tells Python (and the programmer) what kind of value a variable holds and what operations can be performed on it — e.g. numbers can be added, strings can be concatenated.

**2. Name five basic Python data types.**
`int`, `float`, `str`, `bool`, and `NoneType` (also commonly listed: `list`, `dict`, `tuple`, `set`).

**3. Difference between `int` and `float`.**
`int` represents whole numbers with no decimal point (`23`, `-5`). `float` represents numbers with a decimal point (`1.69`, `3.14159`), used when fractional precision is needed.

**4. Difference between `"25"` and `25`.**
`25` is an `int` — you can do math with it (`25 + 5 = 30`). `"25"` is a `str` — the same `+` operator instead concatenates text (`"25" + "5"` → `"255"`). Quotes always make it a string, regardless of what's inside them.

**5. What is `None`?**
A special value representing "nothing" or "no value yet" — Python's `NoneType`. It's commonly used as a placeholder before real data is available, e.g. `user_profile = None`.

**6. What is dynamic typing?**
The ability of a variable to hold a value of one type and later be reassigned to a value of a completely different type, without declaring a type up front:
```python
value = 10        # int
value = "Hello"    # now str
value = False      # now bool
```

**7. What does `type()` do?**
Returns the data type of the value a variable currently holds, e.g. `type(23)` → `<class 'int'>`.

**8. Difference between mutable and immutable? (basic answer)**
Mutable objects can be changed in place after creation (e.g. `list`, `dict`, `set`). Immutable objects cannot — any "change" actually creates a new object (e.g. `int`, `float`, `bool`, `str`).