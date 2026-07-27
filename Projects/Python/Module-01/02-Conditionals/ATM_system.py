Balance = 10000

amount = int(input("Amount : "))
pin = int(input("Pin : "))

if pin == 1234:
    if amount <= Balance:
        Balance -= amount
        print(f"Transaction Complete \nAvailable Balance \"{Balance}\"")
    else:
        print("Insufficient Balance")
else:
    print("Incorrect PIN")