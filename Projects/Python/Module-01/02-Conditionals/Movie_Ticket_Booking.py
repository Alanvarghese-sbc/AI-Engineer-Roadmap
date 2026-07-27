age = int(input("Age : "))

if age >= 18:
    has_id = input("You have an Id (yes/no)?").strip().lower()
    if has_id == "yes":
        print("Booking Confirmed")
    else:
        print("ID required for Booking")
else:
    print("You must be 18 or older to book a ticket")

    