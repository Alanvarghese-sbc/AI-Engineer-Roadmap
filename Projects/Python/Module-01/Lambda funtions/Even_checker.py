even = lambda x : x % 2 == 0

print(even(23))

checker = lambda x : print("Even") if x % 2 == 0 else print("Odd")

checker(20)