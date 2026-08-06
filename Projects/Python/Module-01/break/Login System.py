
username = "alan"
password = 1234

true_user = False

while not true_user:
    user = input("Username : ")
    passw = int(input("Password : "))

    if user == username and passw == password:
        print("Login Successful")
        true_user = True
        break
    else:
        print("Try again")
