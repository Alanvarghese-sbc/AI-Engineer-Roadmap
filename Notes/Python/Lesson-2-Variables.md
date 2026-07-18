# Lesson 2: Variables — Notes

**Estimated Time:** 1–2 hours

Variables are one of the most fundamental concepts in programming — almost every program uses them.

## 🎯 Learning Objectives

- Explain what a variable is
- Understand how variables store values
- Follow Python variable naming rules
- Use meaningful variable names
- Use multiple variables in one program
- Understand dynamic typing (intro)
- Use the `type()` function

## What is a Variable?

Think of labeled boxes:

```
+-----------------+   +-----------------+   +-----------------+
| Name            |   | Age             |   | Country         |
| Alan            |   | 23              |   | India           |
+-----------------+   +-----------------+   +-----------------+
```

A variable is exactly like one of these boxes:

- The **label** is the variable name.
- The **content** is the value.

```python
name = "Alan"
age = 23
country = "India"
```

## Variable = Name + Value

```python
name = "Alan"
```

- Variable name → `name`
- Value → `"Alan"`
- `=` → assignment operator

> **Important:** `=` means **assign**, not "equals" in the mathematical sense.

## How Variables Work (Conceptually)

```python
age = 23
```

Think of it as:

```
age ─────────► 23
```

The variable *refers to* the value.

## Creating Variables

```python
name = "Alan"
age = 23
height = 1.69
is_student = True
```

You don't need to declare the type beforehand — Python figures it out (dynamic typing).

## Reassigning Variables

Variables can change:

```python
age = 23
print(age)

age = 24
print(age)
```

```
23
24
```

## Printing Variables

```python
name = "Alan"
print(name)
```
```
Alan
```

Multiple variables:

```python
name = "Alan"
age = 23

print(name)
print(age)
```

## Variable Naming Rules

**Valid:**
```python
name = "Alan"
student_name = "Alan"
studentName = "Alan"
age2 = 23
```

**Invalid:**
```python
2name = "Alan"      # starts with a number
my-name = "Alan"    # hyphen not allowed
class = "MCA"       # reserved keyword
```

## Naming Best Practices

**Good** — descriptive:
```python
first_name = "Alan"
total_price = 500
is_logged_in = True
```

**Avoid** — vague single letters/abbreviations:
```python
a = "Alan"
x = 500
abc = True
```

## Python is Case-Sensitive

```python
name = "Alan"
Name = "Alex"
```

These are **two different variables**.

## Checking a Variable's Type

Use the built-in `type()` function:

```python
name = "Alan"
age = 23

print(type(name))
print(type(age))
```
```
<class 'str'>
<class 'int'>
```

Data types will be covered in detail in the next lesson.

## 📌 Habit to Build

Don't just make the program work — **experiment**. E.g. after:

```python
age = 23
```

try:

```python
age = 24
age = "Twenty Four"
age = True
```

and print `type(age)` each time to see what happens. Asking "what happens if I change this?" builds real understanding fast.