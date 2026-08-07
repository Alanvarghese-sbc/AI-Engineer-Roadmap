def square(x):
    return x*x


numbers = [1,2,3,4,5,6,7,8]

result = list(map(square, numbers))

print(result)