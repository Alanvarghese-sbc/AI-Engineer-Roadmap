# Lesson 4: Type Casting (Type Conversion) — Notes

**Estimated Time:** 2–3 hours
**Difficulty:** ⭐⭐☆☆☆

## 🎯 Learning Objectives

- Understand what type casting is
- Convert between different data types
- Understand implicit and explicit conversion
- Know when conversion is required
- Avoid common type-related errors

## What is Type Casting?

**Type casting** means converting a value from one data type to another.

```python
age = "23"        # this is a string

age = int("23")   # convert to int
print(age + 2)     # 25
```

## Why Do We Need Type Casting?

```python
age = "23"
print(age + 5)     # ❌ TypeError — can't add str and int
```

```python
age = int("23")
print(age + 5)     # ✅ 28
```

## Two Types of Type Conversion

### 1. Implicit Type Conversion

Python automatically converts types when it's safe to do so — no action needed from you.

```python
num1 = 10       # int
num2 = 5.5       # float

result = num1 + num2

print(result)        # 15.5
print(type(result))  # <class 'float'>
```

Python automatically converted `10` (`int`) to `10.0` (`float`) before adding.

### 2. Explicit Type Conversion

You manually convert the type using built-in functions:

```python
int()
float()
str()
bool()
```

## `int()` — Convert to Integer

```python
age = "23"
age = int(age)

print(age)         # 23
print(type(age))   # <class 'int'>
```

```python
print(int("100"))   # 100
print(int(25.99))   # 25 — decimal part is DROPPED, not rounded
```

## `float()` — Convert to Float

```python
age = 23
age = float(age)

print(age)   # 23.0
```

```python
print(float("10"))   # 10.0
print(float(15))      # 15.0
```

## `str()` — Convert to String

```python
age = 23
age = str(age)

print(type(age))   # <class 'str'>
```

```python
print(str(100))    # "100"
print(str(True))   # "True"
```

## `bool()` — Convert to Boolean

```python
print(bool(1))        # True
print(bool(0))        # False
print(bool(""))       # False
print(bool("Hello"))  # True
```

## Truthy and Falsy Values

These specific values are considered **falsy**:

```python
False
0
0.0
""
None
```

**Everything else is generally truthy**, e.g. `bool(100)` → `True`.

## Invalid Conversions

```python
int("25")     # ✅ works — "25" is numeric text
int("Alan")   # ❌ ValueError: invalid literal for int()
```

`"Alan"` can't be interpreted as a number, so Python raises an error instead of guessing.

## Common Mistakes

**❌ Forgetting to convert before math**
```python
age = "23"
print(age + 5)   # TypeError
```
**✔ Correct**
```python
age = int(age)
print(age + 5)
```

---

**❌ `int()` on a decimal-looking string**
```python
int("12.5")   # ValueError — int() can't parse a decimal string directly
```
**✔ Correct — convert to float first, then int**
```python
int(float("12.5"))   # 12
```