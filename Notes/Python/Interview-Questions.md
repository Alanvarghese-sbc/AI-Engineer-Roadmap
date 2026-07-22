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
# Lesson 4: Type Casting — Interview Questions & Answers

**1. What is type casting?**
Converting a value from one data type to another — e.g. turning the string `"23"` into the integer `23` with `int("23")` — so operations valid for that type (like arithmetic) can be performed.

**2. What is the difference between implicit and explicit conversion?**
**Implicit** conversion happens automatically, done by Python itself when it's safe (e.g. `10 + 5.5` automatically converts `10` to `10.0`). **Explicit** conversion is done manually by the programmer using functions like `int()`, `float()`, `str()`, `bool()`.

**3. What does `int()` do?**
Converts a value to an integer. For floats it truncates (removes) the decimal part rather than rounding — `int(25.99)` → `25`. For numeric strings it parses the number — `int("100")` → `100`.

**4. What does `float()` do?**
Converts a value to a floating-point number, e.g. `float(15)` → `15.0`, `float("10")` → `10.0`.

**5. What does `str()` do?**
Converts a value of any type into its string representation, e.g. `str(100)` → `"100"`, `str(True)` → `"True"`.

**6. What does `bool()` do?**
Converts a value to `True` or `False` based on Python's truthy/falsy rules. Falsy values include `False`, `0`, `0.0`, `""`, and `None`; virtually everything else is truthy.

**7. What happens if you run `int("Alan")`?**
It raises a `ValueError: invalid literal for int()`, because `"Alan"` isn't a string that represents a number, so Python can't safely convert it.

**8. Why is type casting important when using `input()`?**
`input()` always returns a **string**, even if the user types a number. If you need to do math with that input (e.g. calculate an average from entered marks), you must explicitly convert it with `int()` or `float()` first, or you'll get a `TypeError` or unexpected string concatenation instead of addition.
# Lesson 5: Operators — Interview Questions & Answers

> This lesson's source material didn't include a dedicated interview Q&A section, so these are drawn directly from its core concepts to keep the format consistent.

**1. What is an operator in Python?**
A symbol that performs an operation on one or more values (operands) — e.g. in `a + b`, `+` is the operator and `a`, `b` are the operands.

**2. What's the difference between `/` and `//`?**
`/` is regular division and **always returns a float**, even for evenly divisible numbers (`10 / 2` → `5.0`). `//` is floor division — it divides and then drops the decimal part, returning the floor of the result (`10 // 3` → `3`).

**3. What does the modulus operator (`%`) do, and what's it commonly used for?**
It returns the **remainder** of a division (`10 % 3` → `1`). It's commonly used to check even/odd (`n % 2 == 0`) or to detect divisibility.

**4. What is the difference between `=` and `==`?**
`=` is the **assignment** operator — it stores a value in a variable. `==` is the **comparison** operator — it checks whether two values are equal and returns `True`/`False`.

**5. What do assignment shortcut operators like `+=` do?**
They combine an operation with assignment in one step. `x += 5` is shorthand for `x = x + 5`. Similarly `-=`, `*=`, `/=` shorten subtraction, multiplication, and division assignment.

**6. Explain `and`, `or`, and `not`.**
- `and` → `True` only if **both** operands are `True`.
- `or` → `True` if **at least one** operand is `True`; `False` only if both are `False`.
- `not` → reverses a Boolean value (`not True` → `False`).

**7. What is the difference between `==` and `is`?**
`==` checks if two values are **equal**. `is` checks if two variables refer to the **same object in memory** (identity), which is a stricter, different check.

**8. What does operator precedence mean, and how do parentheses affect it?**
Precedence determines the order operations are evaluated in when an expression has multiple operators — similar to BODMAS/PEMDAS in math (e.g. `5 + 2 * 3` evaluates the `*` first, giving `11`). Parentheses `()` override default precedence and make evaluation order explicit: `(5 + 2) * 3` → `21`.