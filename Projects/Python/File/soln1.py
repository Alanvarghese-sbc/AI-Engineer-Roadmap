with open("employee.txt", "w") as file:
    file.write("Alan\n")
    file.write("Computer Application\n")
    file.write("25000\n")


with open("employee.txt", "r") as file:

    data = file.read() #reads the entire file into one string. So data becomes approximately: "Alan\nComputer Application\n25000\n"
    file.seek(0)
# Read line by line
    for line in file:
        print(line.strip())
    file.seek(0)

    lines = file.readlines()  #['Alan\n', 'Computer Application\n', '25000\n']
print(data)

print(lines)

with open("employee.txt", "a") as file:
    file.write("Python\n")
    file.write("SQL\n")


