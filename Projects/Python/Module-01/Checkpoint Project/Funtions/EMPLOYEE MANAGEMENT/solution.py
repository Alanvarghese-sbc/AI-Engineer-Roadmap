employees = []

def add_employee(employees):
    id = int(input("Enter employee ID : "))
    name = input("Enter employee name : ")
    dept = input("Enter department : ")
    salary = int(input("Enter salary : "))
    experience = float(input("Enter experience : "))
    skills = []
    user_skills = input("Enter skills by comma separared")
    raw_skills_list = user_skills.split(",")
    for skill in raw_skills_list:
        cleaned_skill = skill.strip()
        if cleaned_skill:
            skills.append(cleaned_skill)


    employee = {
        "id": id,
        "name": name,
        "department":dept,
        "salary": salary,
        "experience": experience,
        "skills":skills
    }
    employees.append(employee)


def display_employees(employees):

    header_format = "| {:<5} | {:<15} | {:<15} | {:>10} | {:>6} | {:<20} |"
    row_format = "| {:<5} | {:<15} | {:<15} | {:>10} | {:>6} | {:<20} |"

    print("-" * 80)
    print(header_format.format("Id", "Name", "Department", "Salary", "Experience", "Skills"))
    print("-" * 80)

    for emp in employees:
        skills_str = ", ".join(emp['skills'])
        
        print(row_format.format(
            emp['id'],
            emp['name'],
            emp['department'],
            f"{emp['salary']}rs", # Kept your currency formatting clean
            f"{emp['experience']}y",   # Kept your year suffix clean
            skills_str
        ))
    


    
    # print("=" *30)
    # print("Employees List")
    # print("="*30)
    # for emp in employees:
    #     print(f"{'Id':<20} : {emp['id']}")
    #     print(f"{'Name':<20} : {emp['name']}")
    #     print(f"{'Department':<20} : {emp['department']}")
    #     print(f"{'Salary':<20} : {emp['salary']}")
    #     print(f"{'Experience':<20} : {emp['experience']}")
    #     print(f"{'Skills':<20}:{', '.join(emp['skills'])}")
    #     print("="*30)


def display_employee(employee):
    print(f"{'Id':<20} : {employee['id']}")
    print(f"{'Name':<20} : {employee['name']}")
    print(f"{'Department':<20} : {employee['department']}")
    print(f"{'Salary':<20} : {employee['salary']}")
    print(f"{'Experience':<20} : {employee['experience']}")
    print(",".join(employee['skills']))


def find_employees(employees):
    employee_id = int(input("Enter the id : "))

    for employee in employees:
        if employee["id"] == employee_id:
            # print(f"Name : {employee['name']}")
            display_employee(employee)
            return

    print("Employee not found.")

def delete_employee(employees):
    employee_id = int(input('Enter the employee Id to delete: '))

    for employee in employees:
        if employee['id'] == employee_id:
            name = employee['name']
            employees.remove(employee)
            print(f"Employee '{name}' is removed Successfullt")
            return
        
    print("Employee not found")

def update_employee(employees):
    employee_id = int(input("Enter employee ID to update : "))

    for employee in employees:
        if employee['id'] == employee_id:
            print("\nPress Enter to keep the current value.\n")

            name = input(f"Name [{employee['name']}]: ")
            dpt = input(f"Department [{employee['department']}]: ")
            salary = input(f"Salary [{employee['salary']}]: ")
            exp = input(f"Experience [{employee['experience']}]: ")

            if name.strip():
                employee['name'] = name.strip()

            if dpt.strip():
                employee['department'] = dpt.strip()

            if salary.strip():
                employee['salary'] = int(salary)

            if exp.strip():
                employee['experience'] = float(exp)

            print("\nEmployee updated successfully.\n")

            display_employee(employee)
            return
        
    print("Employee not found.")

def salary_statistics(employees):

    salaries = []

    if not employees:
         print("No employees available.")
         return

    for employee in employees:
        salaries.append(employee['salary'])

    total = sum(salaries)
    average = total/len(salaries)

    print("=" *30)
    print("SALARY STATISTICS")
    print("=" *30)
    print(f"{'Total Payroll':>15}:{total}")
    print(f"{'Average Salary':>15}:{average:.2f}")
    print(f"{'Highest Salary':>15}:{max(salaries)}")
    print(f"{'Lowest Salary':>15}:{min(salaries)}")

def sort_employees(employees):
    print("\n1. Salary")
    print("2. Name")
    print("3. Experience")

    choice = input("Choose sorting option: ")

    # if choice == "1":
    #     return sorted(
    #             employees,
    #             key=lambda employee : employee['salary'],
    #         )
    # elif choice == "2":
    #     return sorted(
    #             employees,
    #             key=lambda employee : employee['name']
    #         )
    # elif choice == "3":
    #     return sorted(
    #             employees,
    #             key=lambda employee : employee['Experience']
    #         )
    # else:
    #     print("Invalid Input")
    #     return 
    if choice == "1":
        key = lambda employee: employee["salary"]

    elif choice == "2":
        key = lambda employee: employee["name"]

    elif choice == "3":
        key = lambda employee: employee["experience"]

    else:
        print("Invalid choice")
        return

    order = input("Ascending or descending? (a/d): ")

    reverse = order.lower() == "d"

    return sorted(
        employees,
        key=key,
        reverse=reverse
    )
    


# print(employees)

def main():
    while True:
        print("=" *30)
        print("     EMPLOYEE MANAGEMENT")
        print("=" *30)
        # print("\n1. Add Employee\n2. Display Employees\n3. Find Employee\n4. Delete Employee\n5. Update Employee\n6. Salary Statistics\n7. Sort Employees\n8. Exit")
        print("""
            1. Add Employee
            2. Display Employees
            3. Find Employee
            4. Delete Employee
            5. Update Employee
            6. Salary Statistics
            7. Sort Employees
            8. Exit
            """)
        choice = input("\nEnter your choice(1-8): ")
        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            display_employees(employees)
        elif choice == "3":
            find_employees(employees)
        elif choice == "4":
            delete_employee(employees)
        elif choice == "5":
            update_employee(employees)
        elif choice == "6":
            salary_statistics(employees)
        elif choice == "7":
            sorted_employees = sort_employees(employees)
            if sorted_employees:
                display_employees(sorted_employees)
        elif choice == "8":
            break
        else:
            print("Invalid Input-(Try something b/w '1-8')")


if __name__ == "__main__":
    main()





    
        