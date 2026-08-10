# 👨‍💼 Employee Management System

A console-based **Employee Management System built with Python** to practice core Python programming concepts such as functions, lists, dictionaries, loops, lambda functions, sorting, CRUD operations, and menu-driven programs.

---

## 📌 Project Overview

This project allows users to manage employee records through a simple command-line interface.

Each employee contains:

* Employee ID
* Name
* Department
* Salary
* Experience
* Skills

The application supports adding, viewing, searching, updating, deleting, sorting employees, and calculating salary statistics.

---

## 🚀 Features

### 1. Add Employee

Allows the user to create a new employee record.

The program collects:

* Employee ID
* Employee name
* Department
* Salary
* Experience
* Skills

Multiple skills can be entered using commas.

Example:

```text
Python, SQL, FastAPI, Django
```

---

### 2. Display Employees

Displays all employees in a formatted table.

Example:

```text
--------------------------------------------------------------------------------
| Id    | Name            | Department      |     Salary | Experience | Skills              |
--------------------------------------------------------------------------------
| 101   | Alan Varghese   | AI              |     550000 |       0y   | Python, SQL         |
--------------------------------------------------------------------------------
```

---

### 3. Find Employee

Searches for an employee using their unique employee ID.

Example:

```text
Enter the id: 101
```

The employee's complete information is displayed if found.

---

### 4. Delete Employee

Deletes an employee using their employee ID.

Example:

```text
Enter the employee Id to delete: 101
```

The program confirms the deletion after successfully removing the employee.

---

### 5. Update Employee

Allows existing employee information to be modified.

The user can update:

* Name
* Department
* Salary
* Experience

Pressing **Enter** without entering a value keeps the existing value.

Example:

```text
Name [Alan Varghese]:
Department [AI]: Machine Learning
Salary [550000]:
Experience [0]: 1
```

Only the changed fields are updated.

---

### 6. Salary Statistics

Calculates salary-related statistics for all employees.

Displays:

* Total Payroll
* Average Salary
* Highest Salary
* Lowest Salary

Example:

```text
==============================
SALARY STATISTICS
==============================
  Total Payroll: 2200000
 Average Salary: 550000.00
 Highest Salary: 750000
  Lowest Salary: 400000
```

---

### 7. Sort Employees

Employees can be sorted according to:

1. Salary
2. Name
3. Experience

The user can also choose:

* Ascending
* Descending

The sorting functionality uses Python's `sorted()` function with a `lambda` function.

Example:

```python
sorted(
    employees,
    key=lambda employee: employee["salary"],
    reverse=reverse
)
```

---

### 8. Exit

Closes the Employee Management System.

---

## 🧠 Python Concepts Practiced

This project was created as a Python fundamentals checkpoint and uses several important concepts.

### Variables

```python
salary = 550000
experience = 1.5
```

### Lists

```python
employees = []
skills = ["Python", "SQL"]
```

### Dictionaries

Employee information is stored using dictionaries:

```python
employee = {
    "id": 101,
    "name": "Alan Varghese",
    "department": "AI",
    "salary": 550000,
    "experience": 0,
    "skills": ["Python", "SQL"]
}
```

### Functions

The project is divided into separate functions:

```text
add_employee()
display_employees()
display_employee()
find_employees()
delete_employee()
update_employee()
salary_statistics()
sort_employees()
main()
```

### `*args`

Previously practiced for functions that accept multiple values:

```python
def total_salary(*salaries):
    ...
```

### `**kwargs`

Previously practiced for passing employee details as keyword arguments:

```python
def display_employee(**details):
    ...
```

### Lambda Functions

Used for filtering and sorting:

```python
lambda employee: employee["salary"]
```

### `filter()`

Used to filter employees based on conditions:

```python
filter(
    lambda employee: employee["salary"] > 60000,
    employees
)
```

### `map()`

Previously practiced for modifying salary values:

```python
map(lambda salary: salary * 1.1, salaries)
```

### `reduce()`

Previously practiced for combining multiple values:

```python
reduce(lambda x, y: x + y, salaries)
```

### Recursion

Previously practiced using a recursive function:

```python
def experience_years(year):
    if year == 0:
        return

    print(year)
    experience_years(year - 1)
```

### Sorting

The project uses:

```python
sorted()
```

with:

```python
key=lambda ...
```

and:

```python
reverse=True
```

### CRUD Operations

The project implements the fundamental CRUD operations:

| Operation | Function                                  |
| --------- | ----------------------------------------- |
| Create    | `add_employee()`                          |
| Read      | `display_employees()`, `find_employees()` |
| Update    | `update_employee()`                       |
| Delete    | `delete_employee()`                       |

---

## 🗂️ Project Structure

Current project:

```text
EMPLOYEE MANAGEMENT/
│
├── EMPLOYEE MANAGEMENT.py
└── README.md
```

The Python file contains:

```text
Employee Data
     │
     ├── add_employee()
     ├── display_employees()
     ├── display_employee()
     ├── find_employees()
     ├── delete_employee()
     ├── update_employee()
     ├── salary_statistics()
     ├── sort_employees()
     │
     └── main()
```

---

## ▶️ How to Run

### 1. Clone or download the project

Place the project in your desired directory.

### 2. Make sure Python is installed

Check:

```bash
python --version
```

### 3. Run the program

```bash
python "EMPLOYEE MANAGEMENT.py"
```

---

## 🖥️ Main Menu

When the program starts:

```text
==============================
     EMPLOYEE MANAGEMENT
==============================

1. Add Employee
2. Display Employees
3. Find Employee
4. Delete Employee
5. Update Employee
6. Salary Statistics
7. Sort Employees
8. Exit

Enter your choice (1-8):
```

---

## 💾 Current Data Storage

Currently, employee information is stored **in memory** using a Python list of dictionaries.

Example:

```python
employees = [
    {
        "id": 101,
        "name": "Alan Varghese",
        "department": "AI",
        "salary": 550000,
        "experience": 0,
        "skills": ["Python", "SQL"]
    }
]
```

### Important

The data is **not permanently stored**.

When the program closes, newly added or modified employees are lost.

Future versions can use:

* JSON
* CSV
* SQLite
* MySQL

for permanent storage.

---

## 🔮 Future Improvements

Possible improvements for future versions:

* [ ] Add `try/except` input validation
* [ ] Prevent duplicate employee IDs
* [ ] Validate salary and experience
* [ ] Add employee count
* [ ] Search by name
* [ ] Search by department
* [ ] Filter employees by salary
* [ ] Filter employees by skills
* [ ] Edit employee skills
* [ ] Add confirmation before deletion
* [ ] Store data in JSON
* [ ] Add CSV support
* [ ] Add SQLite database
* [ ] Separate code into multiple Python modules
* [ ] Add unit tests
* [ ] Build a GUI version
* [ ] Convert the project into a web application using FastAPI/Django

---

## 🎯 Learning Objective

The main purpose of this project is to apply Python fundamentals in a practical application instead of solving isolated coding exercises.

The project combines:

```text
Python Fundamentals
        ↓
Functions
        ↓
Lists & Dictionaries
        ↓
CRUD Operations
        ↓
Lambda / Filter / Map / Reduce
        ↓
Sorting
        ↓
Menu-Driven Application
        ↓
Employee Management System
```

---

## 👨‍💻 Author

**Alan Varghese**

MCA Graduate | Software Developer | Python | Data Structures | SQL

---

## 📄 License

This project is created for **learning and educational purposes**.
