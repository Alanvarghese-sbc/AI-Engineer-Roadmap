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

