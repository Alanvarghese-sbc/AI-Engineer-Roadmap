for m in range(1,9):
    for n in range(1,9):
        print(f"({m},{n})", end=" ")
    print("")
    
print()
    
for m in range(8,0,-1):
    for n in range(1,9):
        letter = chr(96+n)
        print(f"({letter},{m})", end=" ")
    print("")