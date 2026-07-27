# Mini Project: Login System

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "python123":
        print("Login Successful")
    else:
        print("Invalid Username or Password")
else:
    print("Invalid Username or Password")