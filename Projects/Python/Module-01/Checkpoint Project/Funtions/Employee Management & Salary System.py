from functools import reduce

def display_employee(**details):

    print("*" *30)
    print("    EMPLOYEE PROFILE       ")
    print("*" *30)

    for key, values in details.items():
        print(f"{key.title()} : {values}")


def calculate_salary(basis, bonus=0):
    return basis + bonus


def total_salary(*salaries):
    total = 0
    for salary in salaries:
        total+=salary

    return total


def average_salary(*salaries):

    if not salaries:
        return 0

    return sum(salaries)/len(salaries)

# def highest_salary(*salaries):
#     high_sal = salaries[0]
#     for salary in salaries:
#         if salary > high_sal:
#             high_sal = salary
#     return high_sal;

def highest_salary(*salaries):
    if not salaries:
        return None
    return reduce(lambda x,y:x if x>y else y,salaries)



def display_skills(*skills):
    print("Skills:")
    for skill in skills:
        print("-",skill)
    

def filter_high_salary(employees):
    # for employee in employees:
    #     if employee['salary']>60000:
    #         print(employee['name'])

    return filter(lambda x:x['salary']>60000, employees)

   

def increase_salary(salaries):
    return list(map(lambda x : round(x*1.1),  salaries))


def total_payroll(salaries):
    return reduce(lambda x,y : x+y, salaries)


def experience_years(year):
    if year == 0:
        return
    print(year)
    experience_years(year-1)
    

def sort_employees(employees):
    return sorted(
        employees,
        key=lambda emp : emp['salary']
    )

def employee_report(**details):

    skills = details.pop('skills', [])

    display_employee(**details)
    display_skills(*skills)

# pop() modifies the dictionary.

# Since details is created locally by **kwargs, this isn't a serious problem here. But you could avoid modifying it:
# def employee_report(**details):
#     skills = details.get("skills", [])

#     employee_details = {
#         key: value
#         for key, value in details.items()
#         if key != "skills"
#     }

#     display_employee(**employee_details)
#     display_skills(*skills)

# explantion for the abve
# employee_details = {}

# for key, value in details.items():

#     if key != "skills":
#         employee_details[key] = value

# This is much easier to understand when you're learning.


salary = (50000,60000,45000,70000)
employees = [
    {"name": "Alan", "salary": 55000},
    {"name": "John", "salary": 40000},
    {"name": "Mary", "salary": 75000},
    {"name": "David", "salary": 65000}
]

display_employee(
    id=101,
    name="Alan Varghese",
    department="AI",
    salary=55000,
    experience=1.5
)

print(calculate_salary(50000, 5000))

display_skills(
    "Python",
    "SQL",
    "FastAPI",
    "Django"
)


  
high_earners = filter_high_salary(employees)

for emp in high_earners:
    print(emp['name'])

new_salary = increase_salary(salary)
print(new_salary)

print(total_payroll(salary))
experience_years(5)

sorted_employees = (sort_employees(employees))

for employee in sorted_employees:
    print(employee["name"],employee["salary"])

employee_report(
    id=101,
    name="Alan Varghese",
    department="AI",
    salary=55000,
    experience=1.5,
    skills=["Python", "SQL", "FastAPI", "Django"]
)