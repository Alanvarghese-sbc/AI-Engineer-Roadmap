# Lesson 5: Operators — Notes

**Estimated Time:** 3–4 hours
**Difficulty:** ⭐⭐☆☆☆

Almost every Python program uses operators — for calculating salary, comparing marks, checking logins, validating passwords, and building AI/ML models.

## 🎯 Learning Objectives

- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Identity Operators
- Membership Operators
- Bitwise Operators (basic intro)
- Operator Precedence

## What is an Operator?

A symbol that performs an operation on values or variables.

```python
a = 10
b = 20
print(a + b)
```

`+` is the **operator**; `a` and `b` are the **operands**.

## 1. Arithmetic Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `5 + 2 = 7` |
| `-` | Subtraction | `5 - 2 = 3` |
| `*` | Multiplication | `5 * 2 = 10` |
| `/` | Division | `5 / 2 = 2.5` |
| `//` | Floor Division | `5 // 2 = 2` |
| `%` | Modulus | `5 % 2 = 1` |
| `**` | Power | `5 ** 2 = 25` |

```python
print(20 + 10)    # 30
print(20 - 5)      # 15
print(5 * 4)        # 20
print(10 / 2)        # 5.0  — division ALWAYS returns a float
print(10 // 3)        # 3   — decimal part removed
print(10 % 3)          # 1   — the remainder
print(2 ** 3)           # 8   — 2 × 2 × 2
```

Modulus is extremely useful for checking even/odd:
```python
10 % 2 = 0   # even
11 % 2 = 1   # odd
```

## 2. Assignment Operators

Regular assignment:
```python
age = 23
```

Shortcut operators — combine an operation with assignment:

| Operator | Equivalent to |
|---|---|
| `+=` | `age = age + 1` |
| `-=` | `score = score - 5` |
| `*=` | `salary = salary * 2` |
| `/=` | `marks = marks / 2` |

```python
x = 10
x += 5
print(x)   # 15
```

## 3. Comparison Operators

Return `True` or `False`.

| Operator | Meaning |
|---|---|
| `==` | Equal |
| `!=` | Not Equal |
| `>` | Greater |
| `<` | Less |
| `>=` | Greater or Equal |
| `<=` | Less or Equal |

```python
print(10 == 10)   # True
print(10 != 5)      # True
print(10 > 20)        # False
```

## 4. Logical Operators

Used with Boolean values.

| Operator | Meaning |
|---|---|
| `and` | Both must be True |
| `or` | At least one True |
| `not` | Reverses the value |

```python
True and True    # True — everything else with 'and' is False
False or False    # False — everything else with 'or' is True
not True            # False
```

**Truth table:**

| A | B | A and B | A or B |
|---|---|---|---|
| True | True | True | True |
| True | False | False | True |
| False | True | False | True |
| False | False | False | False |

## 5. Identity Operators

`is` / `is not` — check whether two variables refer to the **same object** (not just equal values).

```python
x = None
print(x is None)   # True
```

Covered in more depth later when discussing objects.

## 6. Membership Operators

`in` / `not in` — check whether something exists inside a collection.

```python
name = "Alan"
print("A" in name)   # True
```

## 7. Bitwise Operators (basic intro)

```
&   |   ^   ~   <<   >>
```

Operate on the binary representation of integers. Covered in more detail in a later lesson.

## 8. Operator Precedence

Like BODMAS/PEMDAS in math — multiplication/division happen before addition/subtraction.

```python
print(5 + 2 * 3)     # 11 — multiplication first
print((5 + 2) * 3)   # 21 — parentheses override precedence
```

Use parentheses to make your intent explicit, even when not strictly required.
