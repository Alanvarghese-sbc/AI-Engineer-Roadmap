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

