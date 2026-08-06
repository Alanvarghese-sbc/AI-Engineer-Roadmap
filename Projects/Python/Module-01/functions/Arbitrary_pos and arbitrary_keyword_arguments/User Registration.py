def register(**user):
    for key,value in user.items():
        print(f"{key} : {value}")

register(
    name="Alan Varghese",
    course="mca",
    specilization="AI and ML"
)