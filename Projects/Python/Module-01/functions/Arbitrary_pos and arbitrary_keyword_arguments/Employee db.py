def employee(id, **details):
    print(f"ID : {id}")
    print(f"Department : {details['dept']}")
    print(f"Role : {details['role']}")


employee(101, dept="IT", role="Developer")
