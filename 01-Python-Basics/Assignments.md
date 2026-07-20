# 📘 Assignments

## Lesson 1

### Exercise 1

Print your name.

---

### Exercise 2

Print your college name.

---

### Exercise 3

Print your favorite movie.

---

## Mini Project

Developer Profile

Requirements:

- Display name
- Education
- Goal
- Skills
- Country

---

## Challenge

Create a "Dream Company" profile using only print().

# Lesson 3: Data Types — Assignments

## 💻 Practice Exercises

Location: `Practice/Python/Module-01/`

### Exercise 1

Create one variable for each type and print all values:

```python
name = "Alan"
age = 23
height = 1.69
student = True
country = None
```

### Exercise 2

Print the type of every variable from Exercise 1 using `type()`.

### Exercise 3

Change one variable into different types, printing `type(value)` after every change:

```python
value = 10
value = "Ten"
value = 10.5
value = True
```

### Exercise 4

Store your:

- Name
- Age
- Height
- Weight
- Dream Company
- Is MCA Graduate? (boolean)

Print everything.

## 🛠 Mini Project — Employee Information System

Create variables for:

- Employee Name
- Employee ID
- Age
- Department
- Salary
- Experience
- Full Time (`True`/`False`)
- Email
- Phone
- Country

Print them in a formatted way, e.g.:

```
==============================
      EMPLOYEE PROFILE
==============================

Employee Name :
Employee ID :
Age :
Department :
Salary :
Experience :
Full Time :
Email :
Phone :
Country :

==============================
```

## ⚠️ Common Mistakes to Avoid

**❌ Adding a string and an integer**
```python
age = "23"
print(age + 5)   # TypeError
```
**✔ Correct**
```python
age = 23
print(age + 5)
```

---

**❌ Assuming quotes still give you a number**
```python
price = "99.99"   # this is a string, not a float, because of the quotes
```

## 🎯 Today's Assignment

- [ ] Complete all 4 practice exercises
- [ ] Build the **Employee Information System** mini project
- [ ] Commit your changes to Git with a clear message:

```bash
git add .
git commit -m "Complete Lesson 3: Python data types"
```
# Lesson 4: Type Casting — Assignments

## 🧠 Predict Before You Code

Without running Python, work out what each line prints — then check yourself against the Solutions section below.

```python
print(int(7.9))
print(float(8))
print(str(25))
print(bool(0))
print(bool("AI"))
```

## 💻 Practice Exercises

Location: `Practice/Python/Module-01/`

1. Convert `"25"` to an integer.
2. Convert `45` to a float.
3. Convert `99.99` to an integer.
4. Convert `100` to a string.
5. Print the types before and after a conversion (e.g. of `num = "25"`).
6. Try `bool(0)`, `bool(1)`, `bool(-5)`, `bool("")`, `bool("Python")`, `bool(None)` and note what each returns.

### ✅ Solutions

```python
# Predict-before-you-code answers:
print(int(7.9))       # 7      (decimal truncated, not rounded)
print(float(8))        # 8.0
print(str(25))         # "25"
print(bool(0))         # False
print(bool("AI"))      # True  (non-empty string is truthy)

# 1. Convert "25" to an integer
value1 = "25"
value1 = int(value1)
print(value1)             # 25
print(type(value1))       # <class 'int'>

# 2. Convert 45 to a float
value2 = 45
value2 = float(value2)
print(value2)             # 45.0

# 3. Convert 99.99 to an integer
value3 = 99.99
value3 = int(value3)
print(value3)             # 99 (truncated, not rounded)

# 4. Convert 100 to a string
value4 = 100
value4 = str(value4)
print(value4)             # "100"
print(type(value4))       # <class 'str'>

# 5. Print type before and after conversion
num = "25"
print(type(num))    # <class 'str'>
num = int(num)
print(type(num))    # <class 'int'>

# 6. Truthy / falsy exploration
print(bool(0))        # False
print(bool(1))        # True
print(bool(-5))       # True   (any nonzero number is truthy)
print(bool(""))       # False  (empty string)
print(bool("Python")) # True   (non-empty string)
print(bool(None))     # False
```

## 🛠 Mini Project — Student Marks Converter

Starting variables:

```python
student_name = "Alan"
marks = "95"
attendance = "90.5"
```

Convert `marks` → integer, `attendance` → float, then print:

```
==========================
    STUDENT REPORT
==========================

Name       : Alan
Marks      : 95
Attendance : 90.5

Marks Type       : int
Attendance Type  : float
```

### ✅ Solution

```python
student_name = "Alan"
marks = "95"
attendance = "90.5"

marks = int(marks)
attendance = float(attendance)

print("==========================")
print("    STUDENT REPORT")
print("==========================")
print()
print("Name       :", student_name)
print("Marks      :", marks)
print("Attendance :", attendance)
print()
print("Marks Type       :", type(marks).__name__)
print("Attendance Type  :", type(attendance).__name__)
```

## ⚠️ Common Mistakes to Avoid

**❌ Adding a string and an integer without converting**
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

**❌ Using `int()` directly on a decimal string**
```python
int("12.5")   # ValueError
```
**✔ Correct**
```python
int(float("12.5"))   # 12
```

## 🎯 Today's Tasks

- [ ] Answer the "predict before you code" questions first
- [ ] Complete all 6 practice exercises
- [ ] Build the **Student Marks Converter** mini project
- [ ] Commit your changes to Git