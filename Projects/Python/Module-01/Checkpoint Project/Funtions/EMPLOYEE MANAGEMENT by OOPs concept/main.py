from storage import load_employees
from employee import add_employee,find_employees,sort_employees,delete_employee,update_employee,display_employees,salary_statistics


def main():
    employees = load_employees()
    print("Loaded employees:", employees)

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






    
        