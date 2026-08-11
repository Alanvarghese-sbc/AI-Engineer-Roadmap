import json

def load_employees():
    try:
        with open("employees.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Warning: employees.json is corrupted or empty.")
        return []



def save_employees(employees):
    with open("employees.json", "w") as file:
        json.dump(employees,file, indent=4)