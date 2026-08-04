# Lesson 9 (Part 1): `while` Loop — Notes

**Duration:** 2–3 days (for the full Lesson 9 series)
**Difficulty:** ⭐⭐⭐⭐☆

## Why Do We Need Loops?

Printing `"Hello"` five times by hand with five `print()` calls works, but it doesn't scale — what about 1,000 times? A **loop** repeats a block of code automatically.

## Types of Loops in Python

```
Loops
├── while
└── for
```

This lesson (Lesson 9) covers, in order: `while`, `for`, `range()`, nested loops, `break`, `continue`, `pass`, loop `else`, and a checkpoint project.

## What is a `while` Loop?

Keeps running **as long as a condition is True** — e.g. "keep asking for the password while the user keeps entering the wrong one."

## Syntax

```python
while condition:
    # code
```

## Example 1 — Counting

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```
```
1
2
3
4
5
```

**How it works:** Python checks the condition before each pass. If `True`, the body runs, then loops back to check again. Once `count` becomes `6`, `6 <= 5` is `False`, and the loop stops.

## Example 2 — Print Hello 3 Times

```python
i = 1

while i <= 3:
    print("Hello")
    i += 1
```

## Example 3 — Multiples of 5

```python
num = 5

while num <= 50:
    print(num)
    num += 5
```
```
5
10
15
...
50
```

## Example 4 — Looping on User Input

```python
password = ""

while password != "python123":
    password = input("Enter Password: ")

print("Login Successful")
```

The loop keeps asking until the correct password is entered.

## Infinite Loops

```python
count = 1

while count <= 5:
    print(count)
    # count is never updated!
```

Since `count` never changes, `count <= 5` is always `True` — this prints forever. This is called an **infinite loop**. Always make sure something inside the loop eventually makes the condition `False`.

## Common Mistakes

**❌ Forgetting to update the loop variable**
```python
while x < 10:
    print(x)
# infinite loop — x never changes
```

**✔ Correct**
```python
while x < 10:
    print(x)
    x += 1
```

**Starting with a False condition** simply means the loop body never runs at all:
```python
while False:
    print("Hello")
# prints nothing
```

## Real-World Uses

Login retry systems, ATM menus, chat applications, game loops, menu-driven CLI programs, reading data until the end of a file.

# Lesson 9 (Part 2): `for` Loop — Notes

**Estimated Time:** 4–5 hours
**Difficulty:** ⭐⭐⭐⭐☆

One of the most-used Python concepts across AI, Data Science, ML, Automation, and Backend development.

## 🎯 Learning Objectives

- Understand the `for` loop
- Iterate over sequences
- Use `range()`
- Loop through strings, lists, tuples, dictionaries
- Write cleaner code than `while` loops

## What is a `for` Loop?

Used to **iterate over a sequence** — a string, list, tuple, dictionary, set, range, file, or other iterable. Instead of asking "should I keep looping?" (like `while`), a `for` loop asks **"give me the next item"** — and stops automatically once there are no more items.

## `while` vs `for`

```python
# while — you manually track and update the variable
count = 1
while count <= 5:
    print(count)
    count += 1

# for — Python automatically moves to the next value
for number in range(1, 6):
    print(number)
```

## Syntax

```python
for variable in sequence:
    # code
```

```python
for letter in "Python":
    print(letter)
```

## Examples

**Print numbers with `range()`:**
```python
for i in range(1, 6):
    print(i)
```
```
1
2
3
4
5
```

**Loop through a string — one character at a time:**
```python
for ch in "Python":
    print(ch)
```
```
P
y
t
h
o
n
```

**Loop through a list:**
```python
languages = ["Python", "Java", "C++", "Go"]

for language in languages:
    print(language)
```

**Loop through a tuple:**
```python
numbers = (10, 20, 30)

for num in numbers:
    print(num)
```

**Loop through a dictionary:**
```python
student = {"name": "Alan", "age": 23, "course": "MCA"}

for key in student:
    print(key)   # prints just the keys by default
```

To get keys and values together:
```python
for key, value in student.items():
    print(key, ":", value)
```
```
name : Alan
age : 23
course : MCA
```

**Summing numbers:**
```python
total = 0
for i in range(1, 6):
    total += i

print(total)   # 15
```

**Multiplication table:**
```python
number = 7
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```

## Common Mistakes

**❌ Forgetting the colon**
```python
for i in range(5)   # SyntaxError
```
**✔ Correct**
```python
for i in range(5):
```

**❌ Wrong indentation**
```python
for i in range(5):
print(i)   # IndentationError
```

**❌ Modifying the loop variable doesn't change what comes next**
```python
for i in range(5):
    i = 100   # has no effect — the next value still comes from range()
```

## `while` vs `for` — When to Use Which

**Use `for`** when you know how many times to repeat, or you're iterating over a known collection.

**Use `while`** when you don't know how many iterations are needed, and the loop depends on a condition becoming false.

Examples: password retry → `while`; print numbers 1–100 → `for`.

## Real-World Uses

Processing datasets row by row, training ML models across multiple epochs, reading files line by line, iterating through API responses, processing images/videos, generating reports, cleaning data, building AI pipelines.

