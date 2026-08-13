class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}")


class Developer(Employee):

    def write_code(self):
        print(f"{self.name} is writing Python code. ")

    def display(self):
        print(f"Developer: {self.name}")
        print(f"Salary: {self.salary}")

employee = Employee("John", 40000)
developer = Developer("Alan", 5000)
developer.display()
developer.write_code()
employee.display()
developer.display()

