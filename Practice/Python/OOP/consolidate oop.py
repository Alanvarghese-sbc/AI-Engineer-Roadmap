from abc import ABC,abstractmethod

class Employee(ABC):

    def __init__(self,name,department, salary):
        self.name = name 
        self.department = department
        self.salary = salary

    @abstractmethod
    def work(self):
        pass

    def display(self):
        print("Parent method")
        print(f"Name : {self.name}")
        print(f"Department : {self.department}")
        print(f"Salary : {self.salary}")


class Developer(Employee):

    def __init__(self, name, department,salary):
        super().__init__(name, department, salary)

    def work(self):
        print(f"Developer is writing code {self.name}")

    def display(self):
           super().display()
           print("Role : Developer")

    

class Manager(Employee):
    def __init__(self, name, department, salary):
        super().__init__(name, department,salary)


    def work(self):
        print(f"Manager is managing works {self.name}")

    def display(self):
        super().display()
        print("Role : Manager")

d1 = Developer("Alan", "CS", 1000)

m1 = Manager("Alwyn", "Bio", 1000)

d1.display()
m1.display()

d1.work()
m1.work()