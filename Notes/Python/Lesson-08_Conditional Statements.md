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

