# Lesson 8 (Part 1): Conditional Statements (`if`) — Notes

**Estimated Time:** 4–5 hours
**Difficulty:** ⭐⭐⭐☆☆

This is where programs stop following instructions blindly and start **making decisions**.

## 🎯 Learning Objectives

- Understand Boolean expressions
- Use `if` statements
- Compare values
- Write decision-making programs
- Avoid common mistakes with indentation

## Why Do We Need `if`?

Like an ATM: if the PIN is correct, allow access; otherwise, deny it. Without a decision mechanism, a program can only ever do the same thing regardless of input.

**Real-life examples:**
- If age ≥ 18 → allow voting
- If password is correct → login
- If marks ≥ 50 → pass
- If stock > 0 → allow purchase
- If temperature > 30 → turn on AC

## Basic Syntax

```python
if condition:
    # code runs only if condition is True
```

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```
```
You are eligible to vote.
```

## How It Works

Python evaluates the condition (`age >= 18`) down to `True` or `False`. If `True`, the indented block runs. If `False`, it's skipped entirely.

```python
marks = 30

if marks >= 50:
    print("Pass")
# nothing prints — the condition was False
```

## Indentation (Very Important)

Python uses indentation, not braces, to define blocks.

```python
if True:
    print("Hello")   # ✅ correctly indented
```

```python
if True:
print("Hello")        # ❌ IndentationError
```

Convention: use **4 spaces** for each indentation level (most editors do this automatically).

## Comparison Operators (Review)

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

```python
salary = 50000

if salary > 30000:
    print("Eligible")
```

## Multiple Statements Inside `if`

```python
age = 23

if age >= 18:
    print("Adult")
    print("Can Vote")
    print("Can Apply for Driving License")
```

All three lines run because they're all indented inside the `if` block.

## Using User Input

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
```

```python
password = input("Enter password: ")

if password == "python123":
    print("Login Successful")
```

## Using Boolean Variables Directly

```python
logged_in = True

if logged_in:
    print("Welcome!")
```

This is equivalent to `if logged_in == True:`, but shorter and more "Pythonic" — comparing a boolean to `True`/`False` explicitly is usually unnecessary.

## Common Mistakes

**❌ Using `=` instead of `==`**
```python
if age = 18:   # SyntaxError
```
**✔ Correct**
```python
if age == 18:
```
Remember: `=` assigns, `==` compares.

**❌ Missing the colon**
```python
if age > 18   # SyntaxError — missing ':'
```
**✔ Correct**
```python
if age > 18:
```

**❌ Bad indentation** — always indent the code that belongs inside the `if`.

# Lesson 8 (Part 2): `if...else` — Notes

**Estimated Time:** 4–5 hours
**Difficulty:** ⭐⭐⭐☆☆

## 🎯 Learning Objectives

- Understand `else`
- Write `if...else` programs
- Make decisions based on user input
- Avoid common mistakes

## Why Do We Need `else`?

With only `if`, a false condition means the program says nothing at all:

```python
age = 15

if age >= 18:
    print("Eligible to Vote")
# prints nothing if age < 18 — not very informative
```

Adding `else` gives the program a response for **both** outcomes:

```python
age = 15

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")
```
```
Not Eligible to Vote
```

## Syntax

```python
if condition:
    # runs if condition is True
else:
    # runs if condition is False
```

**Exactly one** of the two blocks runs — never both, never neither.

## Flow

```
Condition
    │
 ┌──┴──┐
True  False
 │      │
if    else
```

## Examples

**Voting eligibility:**
```python
age = 22

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

**Even or odd (using modulus):**
```python
number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```
`%` gives the remainder — `10 % 2 = 0`, `11 % 2 = 1`. A remainder of `0` when dividing by 2 means the number is even.

**Password check:**
```python
password = input("Enter Password: ")

if password == "AI123":
    print("Access Granted")
else:
    print("Wrong Password")
```

**Pass or fail:**
```python
marks = int(input("Enter Marks: "))

if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

**Positive or negative:**
```python
number = int(input("Enter Number: "))

if number >= 0:
    print("Positive")
else:
    print("Negative")
```
(Zero currently falls into "Positive" here — handled separately once `elif` is covered.)

## Indentation

```python
if True:
    print("Hello")
else:
    print("Bye")
```

Missing indentation under `if` or `else` raises `IndentationError`.

## Common Mistakes

- **Missing colon:** `if age >= 18` → should be `if age >= 18:`
- **Using `=` instead of `==`:** `if age = 18:` → should be `if age == 18:`
- **Wrong indentation** — always indent the body of both `if` and `else` consistently.