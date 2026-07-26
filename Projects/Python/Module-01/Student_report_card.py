# Mini Project: Student Report Card

name = input("Enter your name: ")
age = int(input("Enter your age: "))
python_marks = int(input("Enter Python marks: "))
ai_marks = int(input("Enter AI marks: "))

total = python_marks + ai_marks
average = total / 2

print("==========================")
print("      REPORT CARD")
print("==========================")
print()
print(f"Name      : {name}")
print(f"Age       : {age}")
print(f"Python    : {python_marks}")
print(f"AI        : {ai_marks}")
print()
print(f"Total     : {total}")
print(f"Average   : {average:.2f}")