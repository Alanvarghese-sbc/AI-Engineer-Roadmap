# Lesson 3: Data Types — Notes

**Estimated Time:** 2–3 hours
**Difficulty:** ⭐⭐☆☆☆

## 🎯 Learning Objectives

- Understand what a data type is
- Identify Python's built-in data types
- Use `type()`
- Understand mutable vs immutable (basic idea)
- Know when to use each type

## What is a Data Type?

Like organizing a room — books go on a bookshelf, clothes in a wardrobe, plates in a cabinet — Python stores different kinds of data using **data types**, and each type behaves differently.

## Why Do We Need Data Types?

```python
age = 23
print(age + 5)
```
```
28
```

Python knows `23` is a **number**, so `+` does addition.

```python
age = "23"
print(age + "5")
```
```
235
```

Here `"23"` is **text**, so `+` does string concatenation, not math. Same operator, different behavior — because the data type is different.

## Python's Basic Data Types

### 1. Integer (`int`) — whole numbers

```python
age = 23
marks = 95
temperature = -5

print(type(age))   # <class 'int'>
```

### 2. Float (`float`) — decimal numbers

```python
height = 1.69
price = 250.75
pi = 3.14159

print(type(height))   # <class 'float'>
```

### 3. String (`str`) — text

```python
name = "Alan"
college = "MG University"
```

Everything inside quotes is a string — **even numbers**:

```python
number = "25"   # this is a string, NOT an integer
```

### 4. Boolean (`bool`) — only two values

```python
is_student = True
is_logged_in = False
```

Used in conditions, loops, authentication, and AI decision-making.

### 5. NoneType — "nothing"

```python
data = None
user_profile = None   # means "no profile exists yet"
```

## Checking Types

```python
name = "Alan"
age = 23
height = 1.69
student = True

print(type(name))     # <class 'str'>
print(type(age))      # <class 'int'>
print(type(height))   # <class 'float'>
print(type(student))  # <class 'bool'>
```

## Dynamic Typing

A variable's type can change as it's reassigned:

```python
value = 10
print(type(value))    # <class 'int'>

value = "Hello"
print(type(value))    # <class 'str'>

value = False
print(type(value))    # <class 'bool'>
```

This behavior is called **dynamic typing**.

## Mutable vs Immutable (Introduction)

Some data types can be changed in place after creation; some can't.

| Immutable (can't change in place) | Mutable (can change — covered later) |
|---|---|
| `int` | `list` |
| `float` | `dict` |
| `bool` | `set` |
| `str` | |

For now, just remember the distinction — it will matter a lot once we get to collections (lists, dicts, sets).

## 📚 New Terms

Data Type · Integer · Float · String · Boolean · None · Dynamic Typing · Mutable · Immutable