import json

employee = {
    "id": 101,
    "name": "Alan",
    "salary": 25000,
    "skills": ["Python", "SQL"]
}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)

with open("employee.json", "r") as file:
    employee = json.load(file)

print(employee)