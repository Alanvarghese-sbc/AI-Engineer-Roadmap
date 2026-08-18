# from validation import get_float,get_integer
# from storage import save_employees,load_employees


# def employee_exist(employees, id):
#     # for emp in employees:
#     #     if emp['id'] == id:
#     #         return True
#     return any(emp["id"] == id for emp in employees)

#     # return False

# def add_employee(employees):

#     # while True:
#     #     try:  
#     #         id = int(input("Enter employee ID : "))
#     #         break
#     #     except ValueError:
#     #         print("Enter a valid number : ")

#     while True:
#          employee_id = get_integer("Enter employee ID : ",1)
#          if employee_exist(employees, employee_id):
#              print("Employee Id already Exist.\n Try Again")
#          else:
#             break
         
#     name = input("Enter employee name : ")
#     dept = input("Enter department : ")
#     # while True:
#     #     try:
#     #         salary = int(input("Enter salary : "))
#     #         break
#     #     except ValueError:
#     #          print("Enter a valid number : ")
#     salary = get_integer("Enter salary : ",0)

#     # while True:
#     #         try:
#     #             experience = float(input("Enter experience : "))
#     #             break
#     #         except ValueError:
#     #              print("Enter a valid number : ")

#     experience = get_float("Enter the experience : ",0)
        
#     skills = []
#     user_skills = input("Enter skills by comma separared")
#     # raw_skills_list = user_skills.split(",")
#     # for skill in raw_skills_list:
#     #     cleaned_skill = skill.strip()
#     #     if cleaned_skill:
#     #         skills.append(cleaned_skill)
#     skills = [skill.strip() for skill in user_skills.split(",") if skill.strip()]


#     employee = {
#         "id": employee_id,
#         "name": name,
#         "department":dept,
#         "salary": salary,
#         "experience": experience,
#         "skills":skills
#     }
#     employees.append(employee)
#     save_employees(employees)






# def display_employees(employees):

#     header_format = "| {:<5} | {:<15} | {:<15} | {:>10} | {:>6} | {:<20} |"
#     row_format = "| {:<5} | {:<15} | {:<15} | {:>10} | {:>6} | {:<20} |"

#     print("-" * 80)
#     print(header_format.format("Id", "Name", "Department", "Salary", "Experience", "Skills"))
#     print("-" * 80)

#     for emp in employees:
#         skills_str = ", ".join(emp['skills'])
        
#         print(row_format.format(
#             emp['id'],
#             emp['name'],
#             emp['department'],
#             f"{emp['salary']}rs", # Kept your currency formatting clean
#             f"{emp['experience']}y",   # Kept your year suffix clean
#             skills_str
#         ))
    


    
#     # print("=" *30)
#     # print("Employees List")
#     # print("="*30)
#     # for emp in employees:
#     #     print(f"{'Id':<20} : {emp['id']}")
#     #     print(f"{'Name':<20} : {emp['name']}")
#     #     print(f"{'Department':<20} : {emp['department']}")
#     #     print(f"{'Salary':<20} : {emp['salary']}")
#     #     print(f"{'Experience':<20} : {emp['experience']}")
#     #     print(f"{'Skills':<20}:{', '.join(emp['skills'])}")
#     #     print("="*30)


# def display_employee(employee):
#     print(f"{'Id':<20} : {employee['id']}")
#     print(f"{'Name':<20} : {employee['name']}")
#     print(f"{'Department':<20} : {employee['department']}")
#     print(f"{'Salary':<20} : {employee['salary']}")
#     print(f"{'Experience':<20} : {employee['experience']}")
#     print(",".join(employee['skills']))


# def find_employees(employees):
#     employee_id = get_integer("Enter the id : ",1)

#     for employee in employees:
#         if employee["id"] == employee_id:
#             # print(f"Name : {employee['name']}")
#             display_employee(employee)
#             return


    

#     print("Employee not found.")

# def delete_employee(employees):
#     employee_id = get_integer('Enter the employee Id to delete: ',1)

#     for employee in employees:
#         if employee['id'] == employee_id:
#             name = employee['name']
#             employees.remove(employee)
#             save_employees(employees)
#             print(f"Employee '{name}' is removed Successfullt")
#             return
        
#     print("Employee not found")

# def update_employee(employees):
#     employee_id = get_integer("Enter employee ID to update : ",1)

#     for employee in employees:
#         if employee['id'] == employee_id:
#             print("\nPress Enter to keep the current value.\n")

#             name = input(f"Name [{employee['name']}]: ").strip()
#             dpt = input(f"Department [{employee['department']}]: ").strip()

#             salary = get_integer(
#                 f"Salary [{employee['salary']}]: ",
#                 0,
#                 employee['salary']

#             )
#             # while True:
#             #     salary = input(f"Salary [{employee['salary']}]: ").strip()
#             #     if not salary:
#             #         break
#             #     if salary:
#             #         try:
#             #             salary = int(salary)
#             #             if salary < 0:
#             #                 print("Salary cannot be negative")
#             #                 # salary = input("Enter salary again: ").strip()
#             #                 continue
#             #             employee['salary'] = salary
#             #             break
#             #         except ValueError:
#             #             print("Enter a valid salary!")
#             # salary = get_integer(f"Salary [{employee['salary']}]: ",0)
#             # exp = input(f"Experience [{employee['experience']}]: ").strip()
#             exp = get_float(
#                 f"Experience [{employee['experience']}]: ",
#                 0,
#                 employee['experience']
#             )

#             if name:
#                 employee['name'] = name.strip()

#             if dpt:
#                 employee['department'] = dpt.strip()

#             employee['salary'] = salary

#             # if exp:
#             #     employee['experience'] = float(exp)
#             employee['experience'] = exp

#             save_employees(employees)

#             print("\nEmployee updated successfully.\n")

#             display_employee(employee)

#             return
        
#     print("Employee not found.")

# def salary_statistics(employees):

#     if not employees:
#          print("No employees available.")
#          return

#     # for employee in employees:
#     #     salaries.append(employee['salary'])
#     salaries = [employee["salary"] for employee in employees]

#     total = sum(salaries)
#     average = total/len(salaries)

#     print("=" *30)
#     print("SALARY STATISTICS")
#     print("=" *30)
#     print(f"{'Total Payroll':>15}:{total}")
#     print(f"{'Average Salary':>15}:{average:.2f}")
#     print(f"{'Highest Salary':>15}:{max(salaries)}")
#     print(f"{'Lowest Salary':>15}:{min(salaries)}")

# def sort_employees(employees):
#     print("\n1. Salary")
#     print("2. Name")
#     print("3. Experience")

#     choice = input("Choose sorting option: ")

#     # if choice == "1":
#     #     return sorted(
#     #             employees,
#     #             key=lambda employee : employee['salary'],
#     #         )
#     # elif choice == "2":
#     #     return sorted(
#     #             employees,
#     #             key=lambda employee : employee['name']
#     #         )
#     # elif choice == "3":
#     #     return sorted(
#     #             employees,
#     #             key=lambda employee : employee['Experience']
#     #         )
#     # else:
#     #     print("Invalid Input")
#     #     return 
#     if choice == "1":
#         key = lambda employee: employee["salary"]

#     elif choice == "2":
#         key = lambda employee: employee["name"]

#     elif choice == "3":
#         key = lambda employee: employee["experience"]

#     else:
#         print("Invalid choice")
#         return

#     order = input("Ascending or descending? (a/d): ")

#     reverse = order.lower() == "d"

#     return sorted(
#         employees,
#         key=key,
#         reverse=reverse
#     )
    


# # print(employees)

class EmployeeManager:
    def __init__(self):
        self.employees = []

   
        
    def add_employee(self, employee):
        if self.employee_exists(employee.id):
            print(f"Employee with ID {employee.id} already exists")
            return
        self.employees.append(employee)
        print(f"Employee {employee.name} added successfully")

    def find_employee(self, employee_id):
        for employee in self.employees:
            if employee.id == employee_id:
                return employee
        return None

    def employee_exists(self, employee_id):
        return self.find_employee(employee_id) is not None

    def delete_employee(self, employee_id):
        for employee in self.employees:
            if employee.id == employee_id:
                self.employees.remove(employee)
            
                print(f"Employee with {employee_id} ID is deleted successfully")
                return
    
        print("Employee not found")

    def update_employee_name(self, employee_id, new_name):

        employee = self.find_employee(employee_id)

        if employee:
            employee.name = new_name
            print("Employee name updated successfully")
        else:
            print("Employee not found")

    def update_employee_department(self, employee_id, new_department):
        employee = self.find_employee(employee_id)

        if employee:
            employee.department = new_department
        else:
            print("Employee not found")


    def update_employee_salary(self, employee_id, new_salary):
        employee = self.find_employee(employee_id)

        if employee:
            employee.salary = new_salary
            print("Employee salary updated successfully")
        else:
            print("Employee not found")

    def update_employee_experience(self, employee_id, new_experience):
        employee = self.find_employee(employee_id)

        if employee:
            employee.experience = new_experience
            print("Experience updated successfully")
        else:
            print("Employee not found")

    def add_employee_skill(self, employee_id, skill):
            
        employee = self.find_employee(employee_id)

        if employee:
            employee.add_skill(skill)
            print("Skill added successfully")
        else:
            print("Employee not found")

    def remove_employee_skill(self, employee_id, skill):
        employee = self.find_employee(employee_id)
        
        if employee:
            employee.remove_skill(skill)
        else:
            print("Employee not found")

    def list_employees(self):
        if not self.employees:
            print("No employees found")
            return

        for employee in self.employees:
            print(employee)

    def count_employees(self):
        return len(self.employees)

    
    def find_by_department(self, department):
        employees = []
        for employee in self.employees:
            if employee.department.lower() == department.lower():
                employees.append(employee)

        return employees

    def find_by_skill(self, skill):
        employees = []
        for employee in self.employees:
            for employee_skill in employee.skills:
                if employee_skill.lower() ==skill.lower():
                    employees.append(employee)
                    break

        return employees

    def sort_by_salary(self):
        return sorted(self.employees, key=lambda employee: employee.salary)





    # def __str__(self):
    #     for employee in self.employees:
    #                 return f"{self.id} | {self.name} | {self.department} | {self.salary} | {self.experience} | {', '.join(self.skills)}"

            


class Employee:

    # total_employees = 0

    def __init__(self, id, name, department, salary, experience, skills):
        self.id = id
        self.name = name
        self.department = department
        self.salary = salary
        self.experience = experience
        self.skills = skills

        # Employee.total_employees += 1

    @classmethod
    def from_string(cls, data):
        parts = data.split(",")

        id = int(parts[0])
        name = parts[1]
        department = parts[2]
        salary  = int(parts[3])
        experience = float(parts[4])
        skills = parts[5].split("|")
        return cls(id, name, department, salary, experience, skills)

    # @classmethod
    # def get_total_employees(cls):
    #     return cls.total_employees
    
    @staticmethod
    def is_valid_salary(salary):
        return isinstance(salary, int) and salary >= 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self._name = new_name.strip()
        else:
            print("Invalid input")

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, new_department):
        if isinstance(new_department, str) and new_department.strip():
            self._department = new_department.strip()
        else:
            print("Invalid department")
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):

        if self.is_valid_salary(new_salary):
            self._salary = new_salary
        else:
            print("Invalid Salary")

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, new_experience):

        if isinstance(new_experience, (int, float)) and new_experience>=0:
            self._experience = new_experience
        else:
            print("Invalid experience")
        

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("Experience:", self.experience)
        print("Skills:", self.skills)

    # def update_salary(self, new_salary):
    #     if isinstance(new_salary, int) and new_salary>=0:    
    #         self.salary = new_salary
    #     else:
    #         print("Invalid Salary")

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)

    def remove_skill(self, skill):
        if skill in self.skills:
            self.skills.remove(skill)
            print(f"{skill} removed successfully")
        else:
            print("skill not found")


    # def update_name(self, new_name):
    #     if new_name.strip():
    #         self.name = new_name
    #     else:
    #         print("Invalid name")

    # def update_department(self, new_department):
    #     if new_department.strip():
    #         self.department = new_department
    #     else:
    #         print("invalid Department")

    # def update_experience(self, new_experience):
    #     if isinstance(new_experience, (int, float)) and new_experience >= 0:
    #         self.experience = new_experience
    #     else:
    #         print("Invalid Experience")

    def __str__(self):
        return f"{self.id} | {self.name} | {self.department} | {self.salary} | {self.experience} | {', '.join(self.skills)}"

manager = EmployeeManager()


employee = Employee(100, "Alan Varghese", "CS", 56000, 0,["css","html"])
manager.add_employee(employee)
employee.display()
# print(manager.employees)

for employee in manager.employees:
    print(employee)

found = manager.find_employee(100)

if found:
    print("Employee found:")
    print(found)
else:
    print("Employee not found")

print(manager.find_employee(999))

# manager.delete_employee(100)
# print(manager.employees)

manager.update_employee_salary(100, 70000)

print(manager.find_employee(100))

manager.update_employee_name(100, "Alan v")
print(manager.find_employee(100))

manager.update_employee_department(100, "AI")
print(manager.find_employee(100))

manager.update_employee_experience(100, 2)

print(manager.find_employee(100))

employee.salary = 80000
print(employee.salary)

employee.salary = -500
print(employee.salary)

employee2 = Employee(
    100,
    "John",
    "IT",
    60000,
    2,
    ["Python", "SQL"]
)

manager.add_employee(employee2)

manager.list_employees()

print(manager.employee_exists(100))
print(manager.employee_exists(999))

print("Total employees:", manager.count_employees())

employee3 = Employee(
    102, "Alex", "AI", 70000, 3, ["Python", "ML"]
)

manager.add_employee(employee3)

results = manager.find_by_department("AI")

if not results:
    print("No employee")
else:
    for employee in results:
        print(employee)

print("List")

print("By dpt")
manager.list_employees()

results = manager.find_by_department("AI")
for employee in results:
    print(employee)

results = manager.sort_by_salary()
print("sort-salary")
for employee in results:
    print(employee)

# print(Employee.get_total_employees())

employee = Employee.from_string(
    "100,Alan,CS,56000,2,Python|SQL"
)

print(employee)

manager.list_employees()
# employee.update_salary(10000)
# employee.display()

# employee.add_skill("Python")
# employee.display()

# employee.remove_skill("Python")
# employee.display()

# print(employee)
