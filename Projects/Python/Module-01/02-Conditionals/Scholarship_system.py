pass_percentage = int("Percentage : (sign is not required)")
quota = input("Sports quota (yes/no)").strip().lower()

if pass_percentage >= 90 or quota == "yes":
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")

    
