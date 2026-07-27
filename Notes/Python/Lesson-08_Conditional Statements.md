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

# Lesson 8 (Part 3): `if...elif...else` — Notes

This lesson enables **multiple decisions**, not just a binary True/False choice.

## Why Do We Need `elif`?

Using separate `if` statements for a grading system causes a bug:

```python
marks = 82

if marks >= 90:
    print("Grade A")

if marks >= 80:
    print("Grade B")

if marks >= 70:
    print("Grade C")
```
```
Grade B
Grade C
```

❌ Wrong — a student should get exactly **one** grade, but every matching `if` runs independently.

## Solution: `elif`

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail")
```
```
Grade B
```

As soon as Python finds a `True` condition, it runs that block and **stops checking the rest** — the remaining `elif`/`else` are skipped entirely.

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

Think of it as asking questions in order, stopping at the first `Yes`:

```
Is marks >= 90? → Yes → Grade A ✅ Stop
        │ No
Is marks >= 80? → Yes → Grade B ✅ Stop
        │ No
Is marks >= 70? → Yes → Grade C ✅ Stop
        │ No
Else → Fail
```

## Examples

**Traffic signal:**
```python
signal = input("Enter signal color: ")

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Get Ready")
elif signal == "green":
    print("Go")
else:
    print("Invalid Signal")
```

**Age category:**
```python
age = 22

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")
```
```
Adult
```

**BMI category (simple):**
```python
bmi = 24

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
```

## Common Mistake: Wrong Condition Order

```python
marks = 95

if marks >= 50:
    print("Pass")
elif marks >= 90:
    print("Grade A")
```
```
Pass
```

❌ `marks >= 50` is checked first and matches, so Python never even evaluates `marks >= 90` — even though 95 clearly deserves "Grade A" too.

**Correct order:**
```python
if marks >= 90:
    print("Grade A")
elif marks >= 50:
    print("Pass")
```

> 👉 **Always check the most specific / highest-priority conditions first.**

# Lesson 8 (Part 4): Nested `if` Statements — Notes

**Estimated Time:** 3–4 hours
**Difficulty:** ⭐⭐⭐⭐☆

Used constantly in login systems, banking apps, e-commerce, admin dashboards, AI decision pipelines, and backend APIs.

## 🎯 Learning Objectives

- Understand nested `if`
- Write multi-level decision logic
- Validate user input step by step
- Build authentication systems
- Avoid deeply nested code when possible

## What is a Nested `if`?

An `if` statement placed **inside** another `if` statement. Like airport security: check the ticket first; only if that passes, check the ID; only if that passes, allow entry. Each decision depends on the previous one succeeding.

## Basic Syntax

```python
if condition1:
    # runs if condition1 is True

    if condition2:
        # runs only if BOTH condition1 and condition2 are True
```

The inner `if` is indented one level deeper than the outer `if`.

## Example 1 — Login System

```python
username = input("Username: ")

if username == "admin":
    password = input("Password: ")

    if password == "python123":
        print("Login Successful")
    else:
        print("Wrong Password")

else:
    print("Invalid Username")
```

**Flow:**
```
Enter Username
      │
Username Correct?
 ┌────┴────┐
Yes        No
 │          │
Ask Password  Invalid Username
 │
Password Correct?
 ┌────┴─────┐
Yes         No
 │          │
Login     Wrong Password
```

## Example 2 — ATM Machine

```python
balance = 5000
pin = int(input("Enter PIN: "))

if pin == 1234:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        print("Transaction Successful")
    else:
        print("Insufficient Balance")

else:
    print("Incorrect PIN")
```

## Example 3 — College Admission

```python
marks = int(input("Enter Marks: "))

if marks >= 60:
    age = int(input("Enter Age: "))

    if age >= 17:
        print("Admission Granted")
    else:
        print("Age Not Eligible")

else:
    print("Marks Too Low")
```

## Example 4 — File Access

```python
logged_in = True
is_admin = False

if logged_in:
    if is_admin:
        print("Access Granted")
    else:
        print("Admin Access Required")

else:
    print("Please Login")
```

## Common Mistake: Too Much Nesting

```python
if A:
    if B:
        if C:
            if D:
                print("Done")
```

This becomes hard to read and maintain. Logical operators (`and`, `or`), covered next, can flatten many nested `if` chains into a single condition.

## When Should You Use Nested `if`?

Use it when the second condition should only be checked **if the first is already true** — e.g. don't ask for a password if the username itself was already wrong.

## Looking Ahead: Logical Operators Simplify This

```python
# Nested version
if username == "admin":
    if password == "python123":
        print("Login Successful")

# Flattened with 'and' (covered next lesson)
if username == "admin" and password == "python123":
    print("Login Successful")
```

Shorter, cleaner, and the style seen in professional Python code.

