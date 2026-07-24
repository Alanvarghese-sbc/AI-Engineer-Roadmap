# Lesson 6: User Input — Notes

**Estimated Time:** 3–4 hours
**Difficulty:** ⭐⭐☆☆☆

From this lesson onward, programs start feeling like real software — they can **interact with the user** instead of using only fixed, hardcoded values.

## 🎯 Learning Objectives

- Take input from users
- Understand how `input()` works
- Convert user input into different data types
- Build interactive programs
- Avoid common mistakes with input

## What is User Input?

Previously, programs used fixed values:

```python
name = "Alan"
age = 23

print(name)
print(age)
```

No matter who runs it, it always prints the same thing. To make programs genuinely interactive, we need the **user** to supply the values.

## The `input()` Function

```python
name = input("Enter your name: ")
print(name)
```

`input()` pauses the program and waits for the user to type something and press Enter. The text passed to `input()` is the **prompt** — it tells the user what to enter.

```
Enter your name: Alan

Alan
```

## Storing User Input

```python
city = input("Enter your city: ")
print(city)
```

If the user types `Kottayam`, then `city` now holds `"Kottayam"`.

## ⚠️ Critical Rule: `input()` ALWAYS Returns a String

```python
age = input("Enter age: ")
print(type(age))
```

Even if the user types `23`, the result is `<class 'str'>` — **not** an int.

### Why this matters

```python
age = input("Enter age: ")
print(age + 5)   # ❌ TypeError — trying to add str + int
```

### The fix — convert explicitly

```python
age = int(input("Enter age: "))
print(age + 5)   # ✅ 28
```

## Taking Different Types of Input

**Integer:**
```python
age = int(input("Enter age: "))
print(type(age))   # <class 'int'>
```

**Float:**
```python
height = float(input("Enter height: "))
```

**String:** no conversion needed — `input()` already returns a string.
```python
name = input("Enter name: ")
```

**Boolean — not direct.** If the user types `True`, Python stores the string `"True"`, not the boolean `True`. Proper boolean-style input parsing is covered later.

## Multiple Inputs

```python
name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

print(name)
print(age)
print(city)
```

## Using Input in Calculations

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 + num2)
```

Entering `10` then `20` prints `30`.

## Common Mistake: Forgetting to Convert

```python
num1 = input("Enter number: ")
num2 = input("Enter number: ")

print(num1 + num2)
```

Entering `10` then `20` prints `1020` — not addition, but **string concatenation**, since both values are still strings.

**Fix:**
```python
num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))

print(num1 + num2)   # 30
```

## 🧠 Key Concepts

`input()` · Prompt · User Input · String Concatenation · Type Conversion with `int()`/`float()` · Interactive Programs