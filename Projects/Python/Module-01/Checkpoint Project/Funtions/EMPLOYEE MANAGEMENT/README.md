# Employee Management System

A console-based **Employee Management System built with Python**.
The project started as a simple CRUD application and was progressively improved with input validation, list comprehensions, JSON file persistence, and modular programming.

## Features

* Add new employees
* Prevent duplicate employee IDs
* Display all employees in a formatted table
* Find an employee by ID
* Delete an employee
* Update employee information
* Keep existing values while updating
* Validate integer and floating-point inputs
* Prevent negative salary and experience values
* Store employee skills as a list
* Calculate salary statistics
* Sort employees by:

  * Salary
  * Name
  * Experience
* Sort in ascending or descending order
* Save employee data permanently to a JSON file
* Load saved employees when the program starts
* Handle missing or corrupted JSON files
* Organize the application into separate Python modules

## Technologies Used

* Python 3
* JSON
* File Handling
* Functions
* Lists
* Dictionaries
* List Comprehensions
* Lambda Functions
* `sorted()`
* Exception Handling
* Modular Programming

## Project Structure

```text
Employee-Management-System/
│
├── main.py
├── employee.py
├── validation.py
├── storage.py
├── employees.json
└── README.md
```

### `main.py`

Responsible for starting the application and handling the main menu.

```text
main()
    ↓
Load employees
    ↓
Display menu
    ↓
User selects operation
    ↓
Call appropriate function
```

### `employee.py`

Contains the main employee-management operations:

* `employee_exist()`
* `add_employee()`
* `display_employees()`
* `display_employee()`
* `find_employees()`
* `delete_employee()`
* `update_employee()`
* `salary_statistics()`
* `sort_employees()`

### `validation.py`

Contains reusable input-validation functions:

* `get_integer()`
* `get_float()`

These functions handle:

* Invalid numeric input
* Minimum allowed values
* Optional default values

For example:

```python
salary = get_integer(
    f"Salary [{employee['salary']}]: ",
    0,
    employee['salary']
)
```

Pressing **Enter** keeps the existing salary.

### `storage.py`

Handles JSON persistence:

* `load_employees()`
* `save_employees()`

Employee data is stored in:

```text
employees.json
```

The application loads the data when it starts and saves changes after adding, updating, or deleting employees.

## Employee Data Structure

Each employee is represented as a dictionary:

```python
{
    "id": 101,
    "name": "Alan",
    "department": "AI",
    "salary": 550000,
    "experience": 0,
    "skills": ["Python", "SQL"]
}
```

Multiple employees are stored inside a list:

```python
employees = [
    {
        "id": 101,
        "name": "Alan",
        "department": "AI",
        "salary": 550000,
        "experience": 0,
        "skills": ["Python", "SQL"]
    }
]
```

## Input Validation

The project uses reusable validation functions instead of repeatedly writing `try-except` blocks.

### Integer Validation

```python
def get_integer(prompt, min_value=None, default=None):
    while True:
        val = input(prompt).strip()

        if not val:
            return default

        try:
            val = int(val)

            if min_value is not None and val < min_value:
                print(
                    f"Enter a value greater than or equal to {min_value}."
                )
                continue

            return val

        except ValueError:
            print("Enter a valid number.")
```

### Float Validation

A similar helper is used for floating-point values such as employee experience.

This allows the same validation logic to be reused throughout the application.

## Duplicate ID Prevention

Before adding an employee, the program checks whether the ID already exists.

```python
return any(emp["id"] == id for emp in employees)
```

This uses Python's `any()` function together with a generator expression.

Example:

```text
Enter employee ID: 101

Employee ID already exists.
Try Again
```

## List Comprehension

Employee skills are processed using a list comprehension:

```python
skills = [
    skill.strip()
    for skill in user_skills.split(",")
    if skill.strip()
]
```

Salary statistics also use list comprehension:

```python
salaries = [employee["salary"] for employee in employees]
```

## Sorting

Employees can be sorted using `sorted()` and lambda functions.

Example:

```python
key = lambda employee: employee["salary"]

return sorted(
    employees,
    key=key,
    reverse=reverse
)
```

Available sorting options:

```text
1. Salary
2. Name
3. Experience
```

The user can choose:

```text
Ascending
Descending
```

The original employee list is not modified because `sorted()` returns a new list.

## Salary Statistics

The application calculates:

* Total payroll
* Average salary
* Highest salary
* Lowest salary

Example:

```text
==============================
SALARY STATISTICS
==============================
  Total Payroll: 125000
  Average Salary: 31250.00
  Highest Salary: 50000
  Lowest Salary: 25000
```

## JSON Persistence

Employee data is stored in `employees.json`.

### Saving

```python
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)
```

### Loading

```python
with open("employees.json", "r") as file:
    return json.load(file)
```

The application also handles:

* Missing JSON file
* Empty/corrupted JSON file

If the file does not exist, the application starts with an empty employee list.

## CRUD Operations

The project implements the four fundamental CRUD operations:

| Operation | Function                                  |
| --------- | ----------------------------------------- |
| Create    | `add_employee()`                          |
| Read      | `display_employees()`, `find_employees()` |
| Update    | `update_employee()`                       |
| Delete    | `delete_employee()`                       |

## Example Menu

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

## How to Run

Make sure Python 3 is installed.

Run the application from the project directory:

```bash
python main.py
```

On some systems:

```bash
python3 main.py
```

The program will automatically load existing employee data from:

```text
employees.json
```

If the file does not exist, a new employee list will be created.

## Concepts Practiced

This project helped practice the following Python concepts:

### Beginner

* Variables
* Data types
* Input/output
* Conditions
* Loops
* Lists
* Dictionaries
* Strings

### Intermediate

* Functions
* Function parameters
* Return values
* `try-except`
* File handling
* JSON
* List comprehensions
* Generator expressions
* `any()`
* `sum()`
* `min()`
* `max()`
* `sorted()`
* Lambda functions

### Application Development

* CRUD operations
* Input validation
* Data persistence
* Modular programming
* Separation of responsibilities
* Reusable helper functions

## Future Improvements

Possible future versions could include:

* Object-Oriented Programming using classes
* Search employees by name or department
* Filter employees by salary or experience
* Update employee skills
* Delete confirmation
* Better error handling
* CSV export/import
* Database integration using SQLite
* Login/authentication
* GUI using Tkinter
* REST API using FastAPI
* Web version using Django
* Unit testing with `pytest`

## Learning Progression

The project evolved through several stages:

```text
Basic Python
     ↓
Lists & Dictionaries
     ↓
Functions
     ↓
CRUD Operations
     ↓
Exception Handling
     ↓
Input Validation
     ↓
List Comprehensions
     ↓
Lambda & Sorting
     ↓
File Handling
     ↓
JSON Persistence
     ↓
Modular Programming
     ↓
Object-Oriented Programming
     ↓
Database
     ↓
API / Web Application
```

## Author

**Alan Varghese**

MCA Graduate | Python Developer | Software Development Enthusiast
