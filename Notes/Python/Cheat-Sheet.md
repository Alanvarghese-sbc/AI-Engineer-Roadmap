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