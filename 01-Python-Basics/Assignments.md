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
`