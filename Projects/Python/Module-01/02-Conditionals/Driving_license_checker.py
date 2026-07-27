age = int(input("Age : "))
medical_cert = input("Have Medical Certificate ? (yes/no)").strip().lower();


if age >= 18 and medical_cert == "yes" :
    print("Eligible for license")
else:
    print("not Eligible")

    