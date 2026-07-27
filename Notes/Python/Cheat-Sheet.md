# Lesson 2: Variables — Cheat Sheet

## Creating & Assigning

```python
name = "Alan"        # str
age = 23              # int
height = 1.69          # float
is_student = True      # bool
```

## Reassigning

```python
age = 23
age = 24               # value changes
age = "Twenty Four"    # type can change too (dynamic typing)
```

## Printing

```python
print(name)
print(name, age)       # multiple values in one print
```

## Checking Type

```python
type(name)              # <class 'str'>
type(age)               # <class 'int'>
print(type(name))
```

## Naming Rules — Quick Reference

| Rule | Example |
|---|---|
| ✅ Letters, numbers, underscores | `student_name`, `age2` |
| ✅ camelCase or snake_case both work | `studentName` / `student_name` |
| ❌ Can't start with a number | ~~`2name`~~ |
| ❌ No hyphens | ~~`my-name`~~ |
| ❌ No reserved keywords | ~~`class`~~ |
| ❌ No spaces | ~~`student name`~~ |
| ⚠️ Case-sensitive | `name` ≠ `Name` |

## Best Practice

| ✅ Good | ❌ Avoid |
|---|---|
| `first_name` | `a` |
| `total_price` | `x` |
| `is_logged_in` | `abc` |

## One-liner Reminders

- `=` → **assign**, not "equals"
- No need to declare type upfront
- `type()` tells you the *current* type — it can change after reassignment

# Lesson 3: Data Types — Cheat Sheet

## The 5 Basics

| Type | Example | `type()` output | Notes |
|---|---|---|---|
| `int` | `age = 23` | `<class 'int'>` | whole numbers |
| `float` | `height = 1.69` | `<class 'float'>` | has a decimal point |
| `str` | `name = "Alan"` | `<class 'str'>` | anything in quotes, even `"25"` |
| `bool` | `is_student = True` | `<class 'bool'>` | only `True` / `False` |
| `NoneType` | `data = None` | `<class 'NoneType'>` | means "nothing yet" |

## Quick Checks

```python
type(23)        # <class 'int'>
type(1.69)      # <class 'float'>
type("Alan")    # <class 'str'>
type(True)      # <class 'bool'>
type(None)      # <class 'NoneType'>
```

## `+` Behaves Differently by Type

```python
23 + 5        # 28   (int addition)
"23" + "5"    # "235" (string concatenation)
"23" + 5      # ❌ TypeError — can't mix str and int with +
```

## Dynamic Typing

```python
value = 10        # int
value = "Hello"    # str
value = False      # bool
```
Same variable, type changes freely on reassignment.

## Mutable vs Immutable — Quick Reference

| Immutable | Mutable |
|---|---|
| `int`, `float`, `bool`, `str` | `list`, `dict`, `set` |

## Gotchas

- `"99.99"` is a **string**, not a float — quotes always mean `str`.
- `age + 5` fails if `age` is a string like `"23"`.
- `None` ≠ `0`, `False`, or `""` — it specifically means "no value."
# Lesson 4: Type Casting — Cheat Sheet

## Conversion Functions

| Function | Converts to | Example | Result |
|---|---|---|---|
| `int()` | integer | `int("25")` | `25` |
| `int()` | integer (truncates!) | `int(25.99)` | `25` |
| `float()` | float | `float("10")` | `10.0` |
| `str()` | string | `str(100)` | `"100"` |
| `bool()` | boolean | `bool(1)` | `True` |

## Implicit vs Explicit

```python
# Implicit — Python does it automatically
10 + 5.5        # → 15.5 (int auto-promoted to float)

# Explicit — you do it manually
int("25")
float(15)
str(True)
bool(0)
```

## Truthy vs Falsy

**Falsy (only these):**
```python
False, 0, 0.0, "", None
```

**Truthy:** everything else — e.g. `1`, `-5`, `"Python"`, `[1]`, `100`.

## `int()` on Floats — Truncates, Doesn't Round

```python
int(25.99)   # 25, not 26
int(7.9)     # 7, not 8
```

## Invalid Conversions

```python
int("Alan")     # ❌ ValueError
int("12.5")     # ❌ ValueError — can't parse decimal string directly
int(float("12.5"))   # ✅ 12 — float first, then int
```

## Watch Out With `input()`

```python
age = input("Enter age: ")   # always returns a STRING
age = int(age)                 # convert before doing math
```
# Lesson 5: Operators — Cheat Sheet

## Arithmetic

| Op | Meaning | Example | Result |
|---|---|---|---|
| `+` | Add | `5 + 2` | `7` |
| `-` | Subtract | `5 - 2` | `3` |
| `*` | Multiply | `5 * 2` | `10` |
| `/` | Divide (always float) | `5 / 2` | `2.5` |
| `//` | Floor divide | `5 // 2` | `2` |
| `%` | Modulus (remainder) | `5 % 2` | `1` |
| `**` | Power | `5 ** 2` | `25` |

## Assignment Shortcuts

```python
x += n   # x = x + n
x -= n    # x = x - n
x *= n     # x = x * n
x /= n      # x = x / n
```

## Comparison (returns bool)

| Op | Meaning |
|---|---|
| `==` | Equal |
| `!=` | Not equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater or equal |
| `<=` | Less or equal |

## Logical

| Op | Rule |
|---|---|
| `and` | True only if BOTH are True |
| `or` | True if AT LEAST ONE is True |
| `not` | Flips True ↔ False |

## Identity vs Membership

```python
x is None        # same object? (identity)
"A" in "Alan"    # exists inside? (membership)
```

## Precedence (high → low, simplified)

```
()  →  **  →  * / // %  →  + -  →  comparisons  →  not  →  and  →  or
```

**Rule of thumb:** when unsure, use parentheses `()` to make order explicit.

## Gotchas

- `/` always returns `float`, even `10 / 2` → `5.0`
- `//` truncates toward negative infinity, not just "removes decimals" for negatives
- `==` compares **value**; `is` compares **identity** — not the same thing
# Lesson 7: Strings (Part 1) — Cheat Sheet

## Creating Strings

```python
name = "Alan"       # double quotes
name = 'Alan'         # single quotes — same thing
message = """
Multi
line
string
"""
```

## Length

```python
len("Python")   # 6
len("")           # 0
len(" ")            # 1
```

## Indexing

```
Character :  P  y  t  h  o  n
Positive  :  0  1  2  3  4  5
Negative  : -6 -5 -4 -3 -2 -1
```

```python
word = "Python"
word[0]     # 'P'   first character
word[-1]     # 'n'   last character
word[3]       # 'h'   4th character
```

## Common Patterns

```python
name[0]      # first character
name[-1]      # last character
len(name)      # total number of characters
```

## Errors to Watch For

```python
name = "Alan"
name[10]   # ❌ IndexError: string index out of range
```

## Quick Reference Table

| Task | Code |
|---|---|
| First character | `s[0]` |
| Last character | `s[-1]` |
| Length | `len(s)` |
| Nth character | `s[n-1]` (0-indexed) |
| Nth from end | `s[-n]` |

# Lesson 7 (Part 2): String Slicing — Cheat Sheet

## Syntax

```python
string[start:stop:step]
```

**Rule:** `start` included, `stop` excluded.

## Reference Table

```
Character : P  y  t  h  o  n
Positive  : 0  1  2  3  4  5
Negative  : -6 -5 -4 -3 -2 -1
```

| Slice | Result | Meaning |
|---|---|---|
| `word[0:2]` | `"Py"` | index 0 up to (not incl.) 2 |
| `word[:4]` | `"Pyth"` | start omitted → from 0 |
| `word[2:]` | `"thon"` | stop omitted → to the end |
| `word[:]` | `"Python"` | full copy |
| `word[-3:]` | `"hon"` | last 3 characters |
| `word[:-2]` | `"Pyth"` | everything except last 2 |
| `word[::2]` | `"Pto"` | every 2nd character |
| `word[::-1]` | `"nohtyP"` | reversed |
| `word[::-2]` | `"nhy"` | reversed, every 2nd char |

## Quick Recipes

```python
s[0]           # first character (indexing)
s[-1]           # last character
s[:n]            # first n characters
s[-n:]            # last n characters
s[::-1]            # reverse the whole string
```

## Safety Note

Out-of-range slice bounds do **not** raise an error (unlike indexing):
```python
"Python"[0:100]   # "Python" — no error, just stops at the actual end
```

# Lesson 7 (Part 3): String Methods — Cheat Sheet

## Case Conversion

```python
"alan".upper()          # "ALAN"
"ALAN".lower()            # "alan"
"alan varghese".title()    # "Alan Varghese"
"python is fun".capitalize()  # "Python is fun"
```

## Whitespace Cleanup

```python
"  Alan  ".strip()     # "Alan"    — both ends
"  Alan  ".lstrip()      # "Alan  " — left only
"  Alan  ".rstrip()        # "  Alan" — right only
```

## Search & Replace

```python
"I love Java".replace("Java", "Python")   # "I love Python"
"Python Programming".find("Program")        # 7   (index, or -1 if not found)
"banana".count("a")                            # 3
```

## Prefix / Suffix Checks

```python
"resume.pdf".startswith("res")   # True
"resume.pdf".endswith(".pdf")      # True
```

## Split & Join

```python
"Python Java C++".split()            # ['Python', 'Java', 'C++']
"Apple,Mango,Banana".split(",")        # ['Apple', 'Mango', 'Banana']
" ".join(["I", "Love", "Python"])        # "I Love Python"
```

## Quick Reference Table

| Method | Purpose | Example → Result |
|---|---|---|
| `.upper()` | ALL CAPS | `"a"` → `"A"` |
| `.lower()` | all lowercase | `"A"` → `"a"` |
| `.title()` | Cap Every Word | `"a b"` → `"A B"` |
| `.capitalize()` | Cap first only | `"ab"` → `"Ab"` |
| `.strip()` | trim both ends | `" a "` → `"a"` |
| `.replace(a,b)` | swap text | see above |
| `.find(x)` | index or `-1` | see above |
| `.count(x)` | occurrences | see above |
| `.startswith(x)` | bool | see above |
| `.endswith(x)` | bool | see above |
| `.split(sep)` | str → list | see above |
| `sep.join(list)` | list → str | see above |

## Chaining Methods

Methods can be chained since each returns a new string:

```python
"   alan   ".strip().title()   # "Alan"
```

# Lesson 7 (Part 4): Escape Characters & Formatting — Cheat Sheet

## Escape Characters

| Escape | Meaning | Example → Output |
|---|---|---|
| `\n` | New line | `"A\nB"` → `A` / `B` |
| `\t` | Tab | `"A\tB"` → `A    B` |
| `\"` | Literal double quote | `"say \"hi\""` → `say "hi"` |
| `\'` | Literal single quote | `'It\'s'` → `It's` |
| `\\` | Literal backslash | `"C:\\Users"` → `C:\Users` |

## Raw Strings — Skip Escaping Entirely

```python
print(r"C:\Users\Alan")   # C:\Users\Alan
```
Handy for file paths and regex patterns.

## f-String Basics

```python
name = "Alan"
print(f"Hello {name}")
```

## f-Strings with Expressions & Methods

```python
a, b = 10, 20
print(f"Sum = {a+b}")             # Sum = 30

name = "alan"
print(f"{name.upper()}")           # ALAN
```

## Number Formatting

```python
pi = 3.14159265
f"{pi:.2f}"   # "3.14"  — 2 decimal places
f"{pi:.0f}"    # "3"     — no decimals
```

## Alignment (width = 10 in these examples)

```python
f"{name:<10}"   # left-aligned:   "Alan      "
f"{name:>10}"    # right-aligned:  "      Alan"
f"{name:^10}"     # center-aligned: "   Alan   "
```

## Quick Recipe: Report-Style Output

```python
print(f"Name    : {name}")
print(f"Average : {average:.2f}")
```

# Lesson 8 (Part 1): Conditional Statements (`if`) — Cheat Sheet

## Basic Syntax

```python
if condition:
    # runs only if condition is True
```

## Comparison Operators

| Op | Meaning |
|---|---|
| `==` | equal |
| `!=` | not equal |
| `>` | greater than |
| `<` | less than |
| `>=` | greater or equal |
| `<=` | less or equal |

## Common Patterns

```python
# With user input
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible")

# With strings
if password == "python123":
    print("Login Successful")

# With booleans directly (Pythonic)
if logged_in:
    print("Welcome!")
# instead of: if logged_in == True:
```

## Rules to Remember

- Requires a **colon** `:` at the end of the `if` line.
- The block **must be indented** (4 spaces is convention).
- `=` assigns, `==` compares — don't mix them up in a condition.
- Code **outside** the indented block always runs, regardless of the condition.

## Common Errors

| Mistake | Fix |
|---|---|
| `if age = 18:` | `if age == 18:` |
| `if age > 18` (no colon) | `if age > 18:` |
| Inconsistent indentation | Use 4 spaces consistently |

# Lesson 8 (Part 2): `if...else` — Cheat Sheet

## Syntax

```python
if condition:
    # runs if True
else:
    # runs if False
```

Exactly **one** branch runs — never both.

## Even / Odd Pattern

```python
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

## Common Patterns

```python
# Eligibility check
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# Password check
if password == "AI123":
    print("Access Granted")
else:
    print("Wrong Password")

# Nested if (checking two things without 'and' yet)
if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Invalid credentials")
else:
    print("Invalid credentials")
```

## Rules to Remember

- Both `if` and `else` need a trailing colon `:`.
- Both blocks must be indented consistently.
- Code outside the `if`/`else` block always runs, regardless of which branch fired.
- `>` is strict — `18 > 18` is `False`; use `>=` if you want to include equality.

## Common Errors

| Mistake | Fix |
|---|---|
| `if age >= 18` (no colon) | `if age >= 18:` |
| `if age = 18:` | `if age == 18:` |
| Inconsistent indentation between `if` and `else` bodies | Match indentation exactly |

# Lesson 8 (Part 3): `if...elif...else` — Cheat Sheet

## Syntax

```python
if condition1:
    # code
elif condition2:
    # code
elif condition3:
    # code
else:
    # code
```

## Key Behavior

- Python checks conditions **top to bottom**.
- Stops at the **first `True`** — runs that block, skips everything else in the chain.
- `else` is optional; can have any number of `elif`s.

## Order Matters!

```python
# ❌ Wrong order — broader condition catches everything first
if marks >= 50:
    print("Pass")
elif marks >= 90:
    print("Grade A")   # never reached

# ✅ Correct — most specific/highest condition first
if marks >= 90:
    print("Grade A")
elif marks >= 50:
    print("Pass")
```

## Common Patterns

**Grading:**
```python
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "F"
```

**Range/category check:**
```python
if age < 13:
    category = "Child"
elif age < 18:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior Citizen"
```

**Exact match chain:**
```python
if day == 1:
    print("Monday")
elif day == 6:
    print("Saturday")
else:
    print("Invalid")
```

## Quick Reminder

Every `if`/`elif`/`else` line ends with `:`, and every body must be indented.

# Lesson 8 (Part 4): Nested `if` Statements — Cheat Sheet

## Syntax

```python
if condition1:
    # runs if condition1 is True

    if condition2:
        # runs only if BOTH condition1 and condition2 are True
    else:
        # condition1 True, condition2 False

else:
    # condition1 is False — inner if is never even checked
```

## Common Pattern: Login-Style Check

```python
if username == "admin":
    password = input("Password: ")
    if password == "python123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")
```

## Common Pattern: Amount/Balance Check

```python
if pin == 1234:
    if amount <= balance:
        print("Transaction Successful")
    else:
        print("Insufficient Balance")
else:
    print("Incorrect PIN")
```

## Rule of Thumb

Use nested `if` only when the inner check should happen **because** the outer check passed. If you're just combining independent conditions, prefer `and`/`or` (next lesson) over nesting:

```python
# Nested — fine when dependent
if logged_in:
    if is_admin:
        print("Access Granted")

# Flattened — cleaner when just combining conditions
if logged_in and is_admin:
    print("Access Granted")
```

## Watch Out For

- **Over-nesting** (3+ levels deep) hurts readability — look for ways to flatten with logical operators.
- Indentation must be **consistent** at each nesting level, or Python raises `IndentationError` or misattributes a block.

# Lesson 8 (Part 5): Logical Operators — Cheat Sheet

## The Three Operators

| Operator | Rule | Analogy |
|---|---|---|
| `and` | BOTH must be True | needs Key 1 AND Key 2 |
| `or` | AT LEAST ONE must be True | Employee Card OR Visitor Pass |
| `not` | flips True ↔ False | "NOT logged in" |

## Truth Tables

**`and`**

| A | B | Result |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

**`or`**

| A | B | Result |
|---|---|---|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

## Precedence (high → low)

```
not  →  and  →  or
```
Use parentheses to make intent explicit when combining all three.

## Common Patterns

```python
# Both conditions required
if age >= 18 and citizen:
    ...

# Either condition is enough
if day == "Saturday" or day == "Sunday":
    ...

# Negation
if not logged_in:
    ...
```

## Gotchas

```python
# ❌ Doesn't check two usernames — always True!
if username == "admin" or "Alan":

# ✅ Correct — each comparison must be spelled out
if username == "admin" or username == "Alan":
```

```python
# ⚠️ Using 'or' where 'and' was probably meant
if age >= 18 or citizen:   # True even if age=10, as long as citizen is True

# Probably meant:
if age >= 18 and citizen:
```