def countdown(n):
    if n == -1:
        return

    print(n)

    countdown(n-1)


countdown(10)


def countup(n):
    if n == -1:
        return

    countup(n-1)

    print(n)

countup(10)


def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n-1)

print(f"factorial : {factorial(5)}")

def total(n):
    if n == 0:
        return 0

    return n + total(n-1)


print(f"Total : {total(5)}")

def fibonacci(n):

    if n == 0:
        return 0
    
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(8))

def power(base,exponent):
    if exponent == 0: 
        return 1
    
    return base * power(base, exponent-1)

print(power(3,3))
print(power(3,0))


def reverse(text):
    if text == "":
        return ""

    return reverse(text[1:]) + text[0]

print(reverse("python"))    


def print_items(items, index=0):
    if index == len(items):
        return

    print(items[index])

    print_items(items, index+1)

numbers = [10, 20, 30, 40]

print(print_items(numbers))
    

    