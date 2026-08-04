a = 10
b = 5

operator = "*"

match operator:

    case "+":
        print(a + b)

    case "-":
        print(a - b)

    case "*":
        print(a * b)

    case "/":
        print(a / b)

    case _:
        print("Invalid")