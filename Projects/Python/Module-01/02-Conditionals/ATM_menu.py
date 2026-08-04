choice = input("1: Check Balance  2: Deposit  3: Withdraw  4: Exit\nChoose an option: ")

match choice:
    case "1":
        print("Checking balance...")
    case "2":
        print("Processing deposit...")
    case "3":
        print("Processing withdrawal...")
    case "4":
        print("Exiting. Goodbye!")
    case _:
        print("Invalid option")