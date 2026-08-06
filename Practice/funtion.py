def welcome():
    print("Welcome to python")

def line():
    print("=" * 30)

def header():
    print("Student Management Sysytem")

def footer():
    print("Thank you")

def menu():
    print(f"1. Add Student\n2. View Student\n3. Delete Student\n4. Exit")



welcome()
welcome()

line()
line()
line()
welcome()
line()
line()
header()
line()
menu()
line()
footer()
line()


def add(*numbers):
    return sum(numbers)



print(add(10,20,30,40,50))



def cart(customer, *products):
    print(f"Customer : {customer}")
    print("Products:")

    for product in products:
        print("-", product)

cust = "Alan Varghese"

# cart_p = ("mango","apple","orange")

cart(cust, "mango","apple","orange")

def marks(name, *marks):
    print(f"Student Name : {name}")
    sum = 0 
    for mark in marks:
        sum+=mark
    print(f"Total : {sum}")
    print(f"Average : {sum/2}")


marks("alan",45,50,100)


