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


# Lesson 5: Operators — Assignments

## 🧠 Practice: Predict Arithmetic Output

Predict before running, then check against the solutions below.

```python
print(20 + 5)
print(20 - 5)
print(20 * 5)
print(20 / 5)
print(20 // 3)
print(20 % 3)
print(2 ** 5)
```

## 💻 Practice: Predict Comparison & Logical Output

```python
print(5 > 2)
print(5 == 2)
print(5 != 2)
print(True and False)
print(True or False)
print(not True)
```

### ✅ Solutions (both predict exercises)

```python
# Arithmetic
print(20 + 5)     # 25
print(20 - 5)      # 15
print(20 * 5)        # 100
print(20 / 5)          # 4.0
print(20 // 3)           # 6
print(20 % 3)              # 2
print(2 ** 5)                # 32

# Comparison & Logical
print(5 > 2)          # True
print(5 == 2)           # False
print(5 != 2)             # True
print(True and False)       # False
print(True or False)          # True
print(not True)                 # False
```

## 🧠 Quick Quiz

Answer without running Python first:

```python
print(15 // 4)
print(15 % 4)
print(2 ** 4)
print(10 == 10)
print(10 != 10)
```

### ✅ Quiz Answers

```python
print(15 // 4)   # 3   (15 / 4 = 3.75, floor to 3)
print(15 % 4)      # 3   (15 = 3*4 + 3, remainder 3)
print(2 ** 4)         # 16  (2×2×2×2)
print(10 == 10)         # True
print(10 != 10)           # False
```

## 🛠 Mini Project — Simple Calculator

Starting variables:

```python
num1 = 25
num2 = 10
```

Print Addition, Subtraction, Multiplication, Division, Floor Division, Modulus, Power:

```
Addition       : 35
Subtraction    : 15
Multiplication : 250
Division       : 2.5
Floor Division : 2
Modulus        : 5
Power          : 95367431640625
```

### ✅ Solution

```python
num1 = 25
num2 = 10

print("Addition       :", num1 + num2)
print("Subtraction    :", num1 - num2)
print("Multiplication :", num1 * num2)
print("Division       :", num1 / num2)
print("Floor Division :", num1 // num2)
print("Modulus        :", num1 % num2)
print("Power          :", num1 ** num2)
```

## 🎯 Today's Assignment

1. Complete the **Simple Calculator** mini project.
2. Create a second program demonstrating assignment, comparison, and logical operators.


### ✅ Solution — Operators Demo Program

```python
# Assignment operators
x = 10
print("Start value:", x)

x += 5
print("After += 5:", x)

x -= 3
print("After -= 3:", x)

x *= 2
print("After *= 2:", x)

x /= 4
print("After /= 4:", x)

# Comparison operators
a = 10
b = 20

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

# Logical operators
is_logged_in = True
has_permission = False

print("Can access (and) :", is_logged_in and has_permission)
print("Can view (or)    :", is_logged_in or has_permission)
print("Not logged in    :", not is_logged_in)
```

# Lesson 6: User Input — Assignments

## 💻 Practice Exercises

Location: `Practice/Python/Module-01/`

**Exercise 1** — Ask for the user's name, print `Hello <name>`.

**Exercise 2** — Ask for age, print `Next year you will be <age+1>.`

**Exercise 3** — Ask for height, print `Your height is <height> meters.`

**Exercise 4** — Ask for favorite programming language, print `Python is a great language!` (or reflect their answer).

**Exercise 5** — Take two numbers, print Sum, Difference, Product, Division.

### ✅ Solutions

```python
# Exercise 1
name = input("Enter your name: ")
print("Hello", name)

# Exercise 2
age = int(input("Enter your age: "))
print("Next year you will be", age + 1, "years old.")

# Exercise 3
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters.")

# Exercise 4
language = input("Enter your favorite programming language: ")
print(language, "is a great language!")

# Exercise 5
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum        :", num1 + num2)
print("Difference :", num1 - num2)
print("Product    :", num1 * num2)
print("Division   :", num1 / num2)
```

## 🛠 Mini Project 1 — Student Registration System

Take input: Name, Age, College, Course, CGPA. Output:

```
==========================
 STUDENT REGISTRATION
==========================

Name      :
Age       :
College   :
Course    :
CGPA      :

==========================
```

### ✅ Solution

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
college = input("Enter your college: ")
course = input("Enter your course: ")
cgpa = float(input("Enter your CGPA: "))

print("==========================")
print(" STUDENT REGISTRATION")
print("==========================")
print()
print("Name      :", name)
print("Age       :", age)
print("College   :", college)
print("Course    :", course)
print("CGPA      :", cgpa)
print()
print("==========================")
```

## 🛠 Mini Project 2 — BMI Calculator

Ask for Weight (kg) and Height (m). Formula: `BMI = weight / (height × height)`.

### ✅ Solution

```python
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)

print("Your BMI is:", bmi)
```

## 🛠 Mini Project 3 — Simple Interest Calculator

Ask for Principal, Rate, Time. Formula: `SI = (P × R × T) / 100`.

### ✅ Solution

```python
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period (years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)
```

## 🎯 Today's Assignment

- [ ] Complete the 5 practice exercises
- [ ] Build the Student Registration System
- [ ] Build the BMI Calculator
- [ ] Build the Simple Interest Calculator

```bash
git add .
git commit -m "Complete Lesson 6: User Input"
```

## 🧠 Final Challenge (Think Before Running)

**Q1**
```python
age = input("Enter age: ")
print(type(age))
```
User enters `23`. What prints?

**Q2**
```python
num1 = input("First: ")
num2 = input("Second: ")
print(num1 + num2)
```
User enters `5` then `6`. What prints?

**Q3**
```python
num = int(input("Enter: "))
print(num * 2)
```
User enters `8`. What prints?

### ✅ Final Challenge Answers

```text
Q1 → <class 'str'>          (input() always returns a string, even for "23")
Q2 → 56                     (string concatenation, NOT addition — "5" + "6")
Q3 → 16                     (converted to int first, then 8 * 2 = 16)
```