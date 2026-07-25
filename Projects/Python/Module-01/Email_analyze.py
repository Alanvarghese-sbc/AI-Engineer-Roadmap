# Mini Project: Email Analyzer

email = input("Enter email: ")

at_index = email.find("@")

username = email[:at_index]
domain = email[at_index + 1:]

print("First Character :", email[0])
print("Last Character  :", email[-1])
print("Username         :", username)
print("Domain           :", domain)
print("Length           :", len(email))