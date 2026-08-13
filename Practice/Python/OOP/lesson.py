class Employee:

    company = "ABC TECH"

    def __init__(self, id, name, department, salary):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary

    @staticmethod
    def is_valid_salary(salary):
        return isinstance(salary, int) and salary >= 0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,new_salary):
        if self.is_valid_salary(new_salary):
            self._salary = new_salary
        else:
            print("invalid Salary")

    def display(self):
        print(f"ID : {self.id}")
        print(f"Name : {self.name}")
        print(f"Department : {self.department}")
        print(f"Salary : {self.salary}")

    def __str__(self):

        return f"ID : {self.id} | Name : {self.name} | Department : {self.department} | Salary : {self.salary}"

    @classmethod
    def change_company(cls, new_comapany):
        cls.company = new_comapany

class Developer(Employee):
    pass
                
employee = Employee(
    101,
    "Alan",
    "Ai",
    55000
)
employee2 = Employee(102, "John", "IT", 60000)
# print(employee.name)
# print(employee.department)
# print(employee.id)
# print(employee.salary)

employee.display()
employee2.display()

print(employee.salary)

employee.salary = "abc"

print(employee.salary)
print(employee)
print(employee2)

print(employee.company)
print(employee2.company)

Employee.company = "Google"

print(employee.company)
print(employee2.company)

employee.company = "Microsoft"

print(employee.company)
print(employee2.company)
print(Employee.company)

print(employee.__dict__)
print(employee2.__dict__)
print(Employee.__dict__)

Employee.change_company("Dell")

print(Employee.company)
print(employee.company)
print(employee2.company)

print(Employee.is_valid_salary(5000))
print(Employee.is_valid_salary(-2))
print(Employee.is_valid_salary("200"))

developer = Developer("Alan")
