from functools import reduce

number = [1,2,3,4]

total = reduce(lambda x,y:x+y,number)

print(total)