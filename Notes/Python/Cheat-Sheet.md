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