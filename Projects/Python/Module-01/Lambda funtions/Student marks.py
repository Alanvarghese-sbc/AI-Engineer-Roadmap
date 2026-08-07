
students = [
    ("Alan", 90),
    ("John", 75),
    ("Mary", 95)
]

sorted_students = sorted(
    students,
    key=lambda student:student[1]
)

print(sorted_students)