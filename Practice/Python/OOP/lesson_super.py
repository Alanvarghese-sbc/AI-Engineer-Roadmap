class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    
    def display(self):
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}")

class Developer(Employee):


    def __init__(self, name, salary, role):
        super().__init__(name, salary)
        self.role = role

    def display(self):
        super().display()
        print(f"Role : {self.role}")

developer = Developer("Alan", 50000, "Developer")
developer.display()