class Employee:
    def display(self):
        print("Employee")

class Developer(Employee):
    def display(self):
        print("Developer")

class Manager(Employee):
    def display(self):
        print("Manager")

employees = [
    Employee(),
    Developer(),
    Manager()
]

for employee in employees:
    employee.display()
    