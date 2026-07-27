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
# Lesson 7: Strings (Part 1) — Assignments

## 🧠 Predict Before You Run

```python
word = "Python"

# Q1
print(word[0])

# Q2
print(word[3])

# Q3
print(word[-1])

# Q4
print(len(word))

# Q5
word2 = ""
print(len(word2))
```

### ✅ Answers

```text
Q1 → P    (index 0 is the first character)
Q2 → h    (P-y-t-h → index 3 is 'h')
Q3 → n    (negative index -1 is the last character)
Q4 → 6    ("Python" has 6 characters)
Q5 → 0    (empty string has zero length)
```

## 💻 Practice Exercises

Location: `Practice/Python/Module-01/`

1. Print the first character of your name.
2. Print the last character.
3. Print the length of your city.
4. Print the length of your college name.
5. Create a multiline string introducing yourself.

### ✅ Solutions

```python
name = "Alan Varghese"
city = "Kottayam"
college = "MG University"

# 1. First character of name
print(name[0])

# 2. Last character of name
print(name[-1])

# 3. Length of city
print(len(city))

# 4. Length of college name
print(len(college))

# 5. Multiline string introduction
intro = """
Hi, I'm Alan Varghese.
I'm from Kottayam, and I studied at MG University.
I'm currently learning Python on my way to becoming an AI Engineer.
"""
print(intro)
```

## 🛠 Mini Project 1 — Personal Information Analyzer

Ask for the user's name, then print Name, Number of characters, First character, Last character.

Example:
```
Enter your name: Alan

Name : Alan
Length : 4
First Character : A
Last Character : n
```

### ✅ Solution

```python
name = input("Enter your name: ")

print()
print("Name :", name)
print("Length :", len(name))
print("First Character :", name[0])
print("Last Character :", name[-1])
```

## 🛠 Mini Project 2 — Username Analyzer

Same idea, for a username.

Example:
```
Username : Alan123
Length : 7
First Character : A
Last Character : 3
```

### ✅ Solution

```python
username = input("Enter username: ")

print()
print("Username :", username)
print("Length :", len(username))
print("First Character :", username[0])
print("Last Character :", username[-1])
```

## 🎯 Today's Assignment

- [ ] Complete the 5 prediction questions
- [ ] Build the Personal Information Analyzer
- [ ] Build the Username Analyzer
- [ ] Finish all 5 practice exercises

# Lesson 7 (Part 2): String Slicing — Assignments

## 🎯 Challenge: Predict Before Running

```python
word = "Python"

# Q1
print(word[1:4])

# Q2
print(word[:3])

# Q3
print(word[3:])

# Q4
print(word[::-1])

# Q5
print(word[::2])

# Q6
print(word[-4:-1])
```

### ✅ Answers

```text
Q1 → "yth"     (index 1 included, index 4 excluded → y, t, h)
Q2 → "Pyt"     (same as word[0:3] → P, y, t)
Q3 → "hon"     (from index 3 to the end → h, o, n)
Q4 → "nohtyP"  (full reverse, step -1)
Q5 → "Pto"     (every 2nd char: P, t, o)
Q6 → "tho"     (word[-4:-1] → index -4 to -2 inclusive → t, h, o)
```

## 💻 Practice

Practice slicing on your own name, city, and college name — try `[0:2]`, `[::-1]`, `[-3:]`, and `[::2]` on each and check the results against your predictions.

### ✅ Example Solution

```python
name = "Alan Varghese"
city = "Kottayam"
college = "MG University"

print(name[0:4])     # "Alan"
print(name[::-1])      # reversed name
print(city[-3:])        # last 3 characters of city
print(college[::2])      # every 2nd character of college name
```

## 🛠 Mini Project 1 — Email Analyzer

Ask for an email (e.g. `alan@gmail.com`), then print: First Character, Last Character, Username, Domain, Length.

> `find()` hasn't been formally covered yet (that's in Part 3), but it's the natural tool here — `email.find("@")` returns the index of `@`, which slicing can then use to split the username from the domain.

### ✅ Solution

```python
email = input("Enter email: ")

at_index = email.find("@")

username = email[:at_index]
domain = email[at_index + 1:]

print("First Character :", email[0])
print("Last Character  :", email[-1])
print("Username         :", username)
print("Domain           :", domain)
print("Length           :", len(email))
```

## 🛠 Mini Project 2 — Reverse Name

Input `Alan`, output `nalA`.

### ✅ Solution

```python
name = input("Enter your name: ")
print(name[::-1])
```

## 🛠 Mini Project 3 — Initial Generator

Input `Alan Varghese`, output `A.V.` — this is a preview; it becomes much easier once `split()` is covered in Part 3.

### ✅ Solution (slicing-only approach)

```python
full_name = "Alan Varghese"

first_initial = full_name[0]
last_initial = full_name[full_name.find(" ") + 1]

print(first_initial + "." + last_initial + ".")
```

## 🎯 Today's Assignment

- [ ] Answer all 6 prediction questions (Q1–Q6) — aim for at least 5/6 correct
- [ ] Complete the Reverse Name project
- [ ] Practice slicing with your own name, city, and college name

# Lesson 7 (Part 3): String Methods — Assignments

## 🧠 Predict Before Running

```python
# Q1
name = "alan"
print(name.upper())

# Q2
text = "  Python  "
print(text.strip())

# Q3
word = "banana"
print(word.count("a"))

# Q4
email = "alan@gmail.com"
print(email.find("@"))

# Q5
filename = "resume.pdf"
print(filename.endswith(".pdf"))

# Q6
text2 = "Python Java AI"
print(text2.split())
```

### ✅ Answers

```text
Q1 → "ALAN"
Q2 → "Python"                          (spaces stripped)
Q3 → 3                                  ("banana" has 3 'a's)
Q4 → 4                                   (@ is at index 4: a-l-a-n-@)
Q5 → True
Q6 → ['Python', 'Java', 'AI']
```

## 🧠 Final Challenge

```python
# Q1
text = "   AI Engineer   "
print(text.strip().upper())

# Q2
email = "Alan.Varghese@gmail.com"
print(email.lower().find("@"))

# Q3
sentence = "I love Python"
print(sentence.replace("Python", "AI"))
```

### ✅ Final Challenge Answers

```text
Q1 → "AI ENGINEER"        (strip removes spaces, then upper() applies)
Q2 → 13                    (after lowercasing, @ sits at index 13)
Q3 → "I love AI"
```

## 🛠 Mini Project 1 — Name Formatter

Input: `   alan varghese`

Output:
```
Original :    alan varghese
Formatted: Alan Varghese
Upper    : ALAN VARGHESE
Lower    : alan varghese
Length   : 14
```

### ✅ Solution

```python
name = input("Enter your name: ")

print("Original :", name)
print("Formatted:", name.strip().title())
print("Upper    :", name.strip().upper())
print("Lower    :", name.strip().lower())
print("Length   :", len(name.strip()))
```

## 🛠 Mini Project 2 — Email Analyzer

Input: `Alan.Varghese@gmail.com`

Display: Original email, Lowercase email, Position of `@`, Username, Domain, Does it end with `.com`?

### ✅ Solution

```python
email = input("Enter your email: ")
lower_email = email.lower()

at_position = lower_email.find("@")
username = lower_email[:at_position]
domain = lower_email[at_position + 1:]

print("Original email :", email)
print("Lowercase email:", lower_email)
print("Position of @  :", at_position)
print("Username       :", username)
print("Domain         :", domain)
print("Ends with .com :", lower_email.endswith(".com"))
```

## 🛠 Mini Project 3 — Password Checker

Ask for a password. Display: Password length, whether it contains `"@"`, whether it contains a number, whether it starts with a capital letter.

> Checking "does it contain a number" needs to look at every character, which is a preview of loops (covered properly soon) — used here the same way `find()` was introduced early in Part 2.

### ✅ Solution

```python
password = input("Enter your password: ")

has_number = False
for char in password:
    if char.isdigit():
        has_number = True

print("Password Length      :", len(password))
print("Contains '@'         :", "@" in password)
print("Contains a number    :", has_number)
print("Starts with capital  :", password[:1].isupper())
```

## 🎯 Today's Assignment

- [ ] Complete all 6 prediction questions
- [ ] Complete the Final Challenge (Q1–Q3)
- [ ] Build the Name Formatter project
- [ ] Build the Email Analyzer project
- [ ] Build the Password Checker project
- [ ] Commit your work:

# Lesson 7 (Part 4): Escape Characters & Formatting — Assignments

## 🧠 Predict the Output

```python
# Q1
print("Hello\nPython")

# Q2
print("A\tB\tC")

# Q3
print("Python is \"Easy\"")

# Q4
pi = 3.14159
print(f"{pi:.3f}")

# Q5
name = "Alan"
print(f"{name.upper()}")

# Q6
a = 10
b = 20
print(f"{a} + {b} = {a+b}")
```

### ✅ Answers

```text
Q1 →
Hello
Python

Q2 → A    B    C        (tab-separated)
Q3 → Python is "Easy"
Q4 → 3.142                (rounded to 3 decimal places)
Q5 → ALAN
Q6 → 10 + 20 = 30
```

## 🎯 Final Challenge

```python
# Q1
print("AI\nML\nPython")

# Q2
language = "python"
print(f"{language.title()}")

# Q3
score = 98.4567
print(f"{score:.1f}")
```

### ✅ Final Challenge Answers

```text
Q1 →
AI
ML
Python

Q2 → Python
Q3 → 98.5   (rounded to 1 decimal place)
```

## 🛠 Mini Project 1 — Student Report Card

Ask for Name, Age, Python Marks, AI Marks. Display total and average (2 decimal places).

### ✅ Solution

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
python_marks = int(input("Enter Python marks: "))
ai_marks = int(input("Enter AI marks: "))

total = python_marks + ai_marks
average = total / 2

print("==========================")
print("      REPORT CARD")
print("==========================")
print()
print(f"Name      : {name}")
print(f"Age       : {age}")
print(f"Python    : {python_marks}")
print(f"AI        : {ai_marks}")
print()
print(f"Total     : {total}")
print(f"Average   : {average:.2f}")
```

## 🛠 Mini Project 2 — Invoice Generator

Input: Customer Name, Product, Price, Quantity. Display line items and total.

### ✅ Solution

```python
customer = input("Enter customer name: ")
product = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("==========================")
print("INVOICE")
print("==========================")
print()
print(f"Customer : {customer}")
print(f"Product  : {product}")
print(f"Price    : ${price:.0f}")
print(f"Quantity : {quantity}")
print()
print(f"Total    : ${total:.0f}")
```

## 🛠 Mini Project 3 — Profile Card

Static output using `\n`, `\"`, and f-strings.

### ✅ Solution

```python
name = "Alan Varghese"
role = "AI Engineer"
country = "India"
skills = "Python, AI, ML"
quote = "Never stop learning."

print("==================================")
print("        AI ENGINEER PROFILE")
print("==================================\n")
print(f"Name        : {name}")
print(f"Role        : {role}")
print(f"Country     : {country}")
print(f"Skills      : {skills}\n")
print("Quote:")
print(f"\"{quote}\"\n")
print("==================================")
```

## 🎯 Today's Assignment

- [ ] Complete all 6 prediction questions
- [ ] Complete the Final Challenge (Q1–Q3)
- [ ] Build the Student Report Card project
- [ ] Build the Invoice Generator project
- [ ] Build the Profile Card project
- [ ] Commit your work:

# Lesson 8 (Part 1): Conditional Statements (`if`) — Assignments

## 🧠 Predict the Output

```python
# Q1
age = 20
if age >= 18:
    print("Adult")

# Q2
marks = 40
if marks >= 50:
    print("Pass")

# Q3
x = 10
if x == 10:
    print("Correct")

# Q4
password = "python"
if password == "Python":
    print("Logged In")

# Q5
logged_in = True
if logged_in:
    print("Welcome")
```

### ✅ Answers

```text
Q1 → Adult                (20 >= 18 is True)
Q2 → (nothing prints)      (40 >= 50 is False)
Q3 → Correct                 (10 == 10 is True)
Q4 → (nothing prints)          ("python" != "Python" — case-sensitive)
Q5 → Welcome                      (logged_in is True)
```

## 🎯 Final Challenge

```python
# Q1
age = 25
if age > 20:
    print("A")
print("B")

# Q2
x = 5
if x > 10:
    print("Big")
print("Done")

# Q3
name = "Alan"
if name == "Alan":
    print("Hello")
print("Welcome")
```

### ✅ Final Challenge Answers

```text
Q1 →
A
B
(the if condition is True, so "A" prints, then "B" always prints since it's outside the if block)

Q2 →
Done
(the if condition is False, so "Big" is skipped, but "Done" always prints since it's outside the if block)

Q3 →
Hello
Welcome
(the if condition is True, so "Hello" prints, then "Welcome" always prints)
```

> Key insight: code **outside** the `if` block (not indented under it) always runs, regardless of whether the condition was True or False.

## 🛠 Mini Project 1 — Voting Eligibility

Ask for age; if 18 or above, print `You are eligible to vote.`

### ✅ Solution

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
```

## 🛠 Mini Project 2 — Password Checker

Ask for a password; correct password is `AI123`. If correct, print `Access Granted`.

### ✅ Solution

```python
password = input("Enter password: ")

if password == "AI123":
    print("Access Granted")
```

## 🛠 Mini Project 3 — Number Checker

Ask for a number; if greater than 100, print `Large Number`.

### ✅ Solution

```python
number = int(input("Enter a number: "))

if number > 100:
    print("Large Number")
```

## 🎯 Today's Assignment

- [ ] Complete all 5 prediction questions
- [ ] Complete the Final Challenge (Q1–Q3)
- [ ] Build the Voting Eligibility project
- [ ] Build the Password Checker project
- [ ] Build the Number Checker project
- [ ] Commit your work:
# Lesson 8 (Part 2): `if...else` — Assignments

## 🧠 Predict the Output

```python
# Q1
age = 16
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Q2
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q3
password = "AI123"
if password == "AI123":
    print("Correct")
else:
    print("Wrong")

# Q4
marks = 80
if marks >= 50:
    print("Pass")
else:
    print("Fail")

# Q5
x = -5
if x >= 0:
    print("Positive")
else:
    print("Negative")
```

### ✅ Answers (with reasons)

```text
Q1 → Minor      — 16 >= 18 is False, so the else branch runs.
Q2 → Odd        — 7 % 2 = 1, not 0, so it's odd.
Q3 → Correct    — the password matches exactly.
Q4 → Pass       — 80 >= 50 is True.
Q5 → Negative   — -5 >= 0 is False, so the else branch runs.
```

## 🎯 Final Challenge

```python
# Q6
number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
print("Finished")

# Q7
age = 18
if age > 18:
    print("Adult")
else:
    print("Teen")

# Q8
name = "Alan"
if name == "Alan":
    print("Welcome")
else:
    print("Unknown User")
print("Login Complete")
```

### ✅ Final Challenge Answers (with reasons)

```text
Q6 →
Even
Finished
— 10 % 2 = 0, so "Even" prints; "Finished" always prints since it's outside the if/else block.

Q7 → Teen
— 18 > 18 is False (strictly greater than, not >=), so the else branch ("Teen") runs.

Q8 →
Welcome
Login Complete
— name == "Alan" is True, so "Welcome" prints; "Login Complete" always prints since it's outside the if/else block.
```

## 🛠 Mini Project 1 — Voting Eligibility

Ask for age; print eligible/not eligible accordingly.

### ✅ Solution

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

## 🛠 Mini Project 2 — Even/Odd Checker

### ✅ Solution

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

## 🛠 Mini Project 3 — Login System

Correct credentials: username `admin`, password `python123`.

> `and` isn't formally covered yet, so this uses a nested `if` to check both conditions — one check inside the other.

### ✅ Solution

```python
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Invalid Username or Password")
else:
    print("Invalid Username or Password")
```

## 🎯 Today's Assignment

- [ ] Complete all 5 prediction questions
- [ ] Complete the Final Challenge (Q6–Q8)
- [ ] Build the Voting Eligibility project
- [ ] Build the Even/Odd Checker
- [ ] Build the Login System

# Lesson 8 (Part 3): `if...elif...else` — Assignments

## 🧠 Predict the Output

```python
# Q1
marks = 95
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
else:
    print("C")

# Q2
age = 15
if age < 13:
    print("Child")
elif age < 18:
    print("Teen")
else:
    print("Adult")

# Q3
number = 0
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Q4
day = 6
if day == 1:
    print("Monday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid")

# Q5 ⭐
marks2 = 85
if marks2 >= 50:
    print("Pass")
elif marks2 >= 80:
    print("Grade B")
else:
    print("Fail")
```

### ✅ Answers (with reasoning)

```text
Q1 → A          — 95 >= 90 is True, so it stops there immediately.
Q2 → Teen        — 15 is not < 13, but it IS < 18, so the second branch fires.
Q3 → Zero         — 0 is neither > 0 nor < 0, so it falls to the else branch.
Q4 → Saturday      — day == 6 matches the second condition exactly.

Q5 → Pass
Explanation: marks2 >= 50 is checked FIRST and is True (85 >= 50), so Python
prints "Pass" and stops immediately — it never even evaluates marks2 >= 80,
even though 85 would also satisfy "Grade B". This is the classic condition-order
bug: broader/lower-priority conditions must come AFTER more specific ones.
```

## 🛠 Mini Project 1 — Grade Calculator

Rules: 90–100 → A, 80–89 → B, 70–79 → C, 60–69 → D, below 60 → F.

### ✅ Solution

```python
marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")
```

## 🛠 Mini Project 2 — Simple Calculator

Ask for two numbers and an operator (`+`, `-`, `*`, `/`), then compute the result using `if...elif...else`.

### ✅ Solution

```python
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = "Invalid operator"

print("Result =", result)
```

## 🛠 Mini Project 3 — Month Finder

Input a month number (1–12), print the month name.

### ✅ Solution

```python
month = int(input("Enter Month Number: "))

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Invalid month number")
```

## 🎯 Today's Assignment

- [ ] Complete all 5 prediction questions (with Q5's explanation)
- [ ] Build the Grade Calculator
- [ ] Build the Simple Calculator
- [ ] Build the Month Finder
# Lesson 8 (Part 4): Nested `if` Statements — Assignments

## 🧠 Predict the Output

```python
# Q1
username = "admin"
if username == "admin":
    password = "python123"
    if password == "python123":
        print("Login")

# Q2
age = 20
if age >= 18:
    if age >= 60:
        print("Senior")
    else:
        print("Adult")

# Q3
balance = 1000
withdraw = 1200
if withdraw <= balance:
    print("Success")
else:
    print("Insufficient Balance")

# Q4
logged_in = False
if logged_in:
    if True:
        print("Dashboard")
else:
    print("Login Required")

# Q5
marks = 70
if marks >= 50:
    if marks >= 80:
        print("Grade A")
    else:
        print("Pass")
else:
    print("Fail")
```

### ✅ Answers

```text
Q1 → Login                    (both conditions match)
Q2 → Adult                     (20 >= 18 is True, but 20 >= 60 is False, so else fires)
Q3 → Insufficient Balance        (1200 <= 1000 is False)
Q4 → Login Required               (outer condition is False, so the inner if is never even reached)
Q5 → Pass                          (70 >= 50 is True; 70 >= 80 is False, so the inner else fires)
```

## 🛠 Mini Project 1 — Login System

Correct username `admin`, password `python123`.

### ✅ Solution

```python
username = input("Username: ")

if username == "admin":
    password = input("Password: ")

    if password == "python123":
        print("Login Successful")
    else:
        print("Wrong Password")

else:
    print("Invalid Username")
```

## 🛠 Mini Project 2 — ATM Simulator

Correct PIN `1234`, balance `10000`.

### ✅ Solution

```python
balance = 10000
pin = int(input("Enter PIN: "))

if pin == 1234:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        print("Transaction Successful")
    else:
        print("Insufficient Balance")

else:
    print("Incorrect PIN")
```

## 🛠 Mini Project 3 — Movie Ticket Booking

Age must be at least 18. If so, ask whether they have an ID; if yes, allow booking; otherwise reject.

### ✅ Solution

```python
age = int(input("Enter your age: "))

if age >= 18:
    has_id = input("Do you have a valid ID? (yes/no): ")

    if has_id == "yes":
        print("Booking Confirmed")
    else:
        print("ID Required for Booking")

else:
    print("You must be 18 or older to book a ticket")
```

## 🛠 Mini Project 4 — College Admission Checker

Marks must be at least 60. If so, check age is at least 17.

### ✅ Solution

```python
marks = int(input("Enter Marks: "))

if marks >= 60:
    age = int(input("Enter Age: "))

    if age >= 17:
        print("Admission Granted")
    else:
        print("Age Not Eligible")

else:
    print("Marks Too Low")
```

## 🎯 Today's Assignment

- [ ] Complete all 5 prediction questions
- [ ] Build the Login System
- [ ] Build the ATM Simulator
- [ ] Build the Movie Ticket Booking system
- [ ] Build the College Admission Checker
- [ ] Commit your work:

# Lesson 8 (Part 5): Logical Operators — Assignments

## 🧠 Predict the Output

```python
# Q1
age = 20
citizen = True
if age >= 18 and citizen:
    print("Eligible")

# Q2
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Holiday")

# Q3
logged_in = False
if not logged_in:
    print("Login First")

# Q4
marks = 80
sports = False
if marks >= 90 or sports:
    print("Scholarship")
else:
    print("No Scholarship")

# Q5
username = "Alan"
password = "123"
if username == "Alan" and password == "123":
    print("Welcome")
else:
    print("Denied")
```

### ✅ Answers

```text
Q1 → Eligible          (both age>=18 and citizen are True)
Q2 → Holiday             (day == "Sunday" is True, so 'or' is satisfied)
Q3 → Login First           (logged_in is False, so 'not logged_in' is True)
Q4 → No Scholarship          (80 >= 90 is False, and sports is False, so 'or' fails)
Q5 → Welcome                   (both username and password match exactly)
```

## 🛠 Mini Project 1 — Login System

Correct username `admin`, password `python123`, checked with `and`.

### ✅ Solution

```python
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credentials")
```

## 🛠 Mini Project 2 — Driving License Checker

Eligible if age ≥ 18 **and** has a medical certificate.

### ✅ Solution

```python
age = int(input("Enter your age: "))
medical = input("Do you have a medical certificate? (yes/no): ")

if age >= 18 and medical == "yes":
    print("Eligible for License")
else:
    print("Not Eligible")
```

## 🛠 Mini Project 3 — Scholarship System

Scholarship if marks ≥ 90 **or** sports quota is yes.

### ✅ Solution

```python
marks = int(input("Enter your marks: "))
sports_quota = input("Are you under sports quota? (yes/no): ")

if marks >= 90 or sports_quota == "yes":
    print("Scholarship Granted")
else:
    print("Scholarship Not Granted")
```

## 🛠 Mini Project 4 — Website Access Checker

If not logged in, print `Please Login`.

### ✅ Solution

```python
logged_in = False

if not logged_in:
    print("Please Login")
else:
    print("Welcome back!")
```

## ⭐ Portfolio Project — Smart ATM System (Preview)

A fuller version with multiple transactions and loops comes after Loops is covered. For now, here's a single-transaction version using logical operators to prevent overdraft:

```python
balance = 10000
pin = int(input("Enter PIN: "))

if pin == 1234:
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    choice = input("Choose an option: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print("Withdrawal successful. New balance:", balance)
        else:
            print("Invalid amount or insufficient balance")

    elif choice == "3":
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("Deposit successful. New balance:", balance)
        else:
            print("Invalid deposit amount")

    else:
        print("Invalid option")

else:
    print("Incorrect PIN")
```

## 🎯 Today's Assignment

- [ ] Complete all 5 prediction questions
- [ ] Build the Login System
- [ ] Build the Scholarship System
- [ ] Build the Driving License Checker
- [ ] Build the Website Access Checker
