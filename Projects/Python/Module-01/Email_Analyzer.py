email = input("Enter your email: ")
lower_email = email.lower()

at_position = lower_email.find("@")
username = lower_email[:at_position]
domain = lower_email[at_position + 1:]

print("Original email :", email)
print("Lowercase email:", lower_email)
print("Position of @  :", at_position)
print("Username       :", username)
print("Domain         :", domain)
print("Ends with .com :", lower_email.endswith(".com"))