# Checkpoint Project: Smart Banking System (CLI)
# Combines: if, if...else, if...elif...else, nested if, logical operators, match-case

correct_username = "admin"
correct_password = "python123"
correct_pin = 1234
balance = 10000

username = input("Username: ")
password = input("Password: ")

if username == correct_username and password == correct_password:
    print("Login Successful\n")

    pin = int(input("Enter PIN: "))

    if pin == correct_pin:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option: ")

        match choice:
            case "1":
                print("Your balance is:", balance)

            case "2":
                amount = float(input("Enter deposit amount: "))
                if amount > 0:
                    balance += amount
                    print("Deposit successful. New balance:", balance)
                else:
                    print("Invalid deposit amount")

            case "3":
                amount = float(input("Enter withdrawal amount: "))
                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        print("Withdrawal successful. New balance:", balance)
                    else:
                        print("Insufficient balance")
                else:
                    print("Invalid withdrawal amount")

            case "4":
                print("Thank you for banking with us. Goodbye!")

            case _:
                print("Invalid option")

    else:
        print("Incorrect PIN")

else:
    print("Invalid Username or Password")