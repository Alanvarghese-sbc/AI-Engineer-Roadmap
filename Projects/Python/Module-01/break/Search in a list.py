numbers = [12, 45, 78, 90, 23]

num = int(input("Enter the number : "))

found = False

for n in numbers:
    if n == num:
        print("Number found")
        found = True
        break
else:
    print("Not found")


