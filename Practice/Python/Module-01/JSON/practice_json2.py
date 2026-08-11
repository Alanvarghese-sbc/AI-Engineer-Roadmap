import json

employees = [
    {
        "id": 101,
        "name": "Alan",
        "salary": 25000,
        "skills": ["Python", "SQL"]
    },
    {
        "id": 102,
        "name": "John",
        "salary": 30000,
        "skills": ["Java", "MySQL"]
    }
]

with open("employee.json", "w") as file:
    json.dump(employees, file, indent=4)

with open("employee.json", "r") as file:
    employees = json.load(file)
print(employees)