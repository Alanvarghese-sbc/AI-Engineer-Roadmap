from abc import ABC,abstractmethod

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass



class Developer(Employee):

    def work(self):
        print("Developer is writing code")


class Manager(Employee):

    def work(self):
        print("Manager is managing the team")

d1 = Developer()
m1 = Manager()

d1.work()
m1.work()

e1 = Employee()

