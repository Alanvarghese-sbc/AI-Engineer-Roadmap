while True:
    try:
        num = int(input("Enter number:"))
        print(num)
        break
    except ValueError:
        print("error try again")