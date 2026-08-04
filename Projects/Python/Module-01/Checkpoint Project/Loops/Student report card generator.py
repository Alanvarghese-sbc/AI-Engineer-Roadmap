# Checkpoint Challenge: Student Report Card Generator
# Combines: loops + conditionals + lists

names = ["Alan", "Priya", "Rahul", "Sneha"]
marks_list = [85, 92, 67, 78]

total = 0
highest = marks_list[0]
lowest = marks_list[0]

for i in range(len(names)):
    name = names[i]
    marks = marks_list[i]
    total += marks

    if marks > highest:
        highest = marks
    if marks < lowest:
        lowest = marks

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{name}: {marks} marks — Grade {grade}")

average = total / len(marks_list)

print()
print("Total marks  :", total)
print("Average marks:", average)
print("Highest marks:", highest)
print("Lowest marks :", lowest)# Checkpoint Challenge: Student Report Card Generator
# Combines: loops + conditionals + lists

names = ["Alan", "Priya", "Rahul", "Sneha"]
marks_list = [85, 92, 67, 78]

total = 0
highest = marks_list[0]
lowest = marks_list[0]

for i in range(len(names)):
    name = names[i]
    marks = marks_list[i]
    total += marks

    if marks > highest:
        highest = marks
    if marks < lowest:
        lowest = marks

    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{name}: {marks} marks — Grade {grade}")

average = total / len(marks_list)

print()
print("Total marks  :", total)
print("Average marks:", average)
print("Highest marks:", highest)
print("Lowest marks :", lowest)