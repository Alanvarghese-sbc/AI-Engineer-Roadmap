password = input("Enter your password: ")

has_number = False
for char in password:
    if char.isdigit():
        has_number = True

print("Password Length      :", len(password))
print("Contains '@'         :", "@" in password)
print("Contains a number    :", has_number)
print("Starts with capital  :", password[:1].isupper())